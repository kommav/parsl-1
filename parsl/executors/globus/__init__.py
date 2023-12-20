import logging
import typeguard
import concurrent.futures as cf
import heapq

from typing import List, Optional

from parsl.data_provider.staging import Staging
from parsl.executors.status_handling import NoStatusHandlingExecutor
from parsl.utils import RepresentationMixin
from parsl.executors.errors import UnsupportedFeatureError

from globus_compute_sdk import Executor
from globus_compute_sdk.serialize import DillCodeSource
from globus_compute_sdk import Client


logger = logging.getLogger(__name__)

# Not Necessary in Executor as we don't have a method that "collects results"
# class ExecComp:
#     def __init__(self, exec, val):
#         self.exec = exec
#         self.val = val

#     def __lt__(self, other):
#         return self.val < other.val

class GlobusExec(NoStatusHandlingExecutor, RepresentationMixin):
    """A thread-based executor.

    Parameters
    ----------
    max_threads : int
        Number of threads. Default is 2.
    thread_name_prefix : string
        Thread name prefix
    storage_access : list of :class:`~parsl.data_provider.staging.Staging`
        Specifications for accessing data this executor remotely.
    endpoint_id : string
        Represents endpoint that the user is submitting tasks to. Default Endpoint = Globus Compute Tutorial Endpoint
    """

    @typeguard.typechecked
    def __init__(self, label: str = 'threads', max_threads: int = 2,
                 thread_name_prefix: str = '', storage_access: Optional[List[Staging]] = None,
                 working_dir: Optional[str] = None,
                 endpoint_list = ['4b116d3c-1703-4f8f-9f6f-39921e5864df']):
        NoStatusHandlingExecutor.__init__(self)
        self.label = label
        self.max_threads = max_threads
        self.thread_name_prefix = thread_name_prefix
        self.endpoint_list = endpoint_list

        # we allow storage_access to be None now, which means something else to [] now
        # None now means that a default storage access list will be used, while
        # [] is a list with no storage access in it at all
        self.storage_access = storage_access
        self.working_dir = working_dir
        # self.end_status_dict = dict()
        # self.pq = []      

    def start(self):
        self.Executor_list = []
        c = Client()
        self.index = 0
        for x in self.endpoint_list:
            self.Executor_list.append(Executor(endpoint_id = x, funcx_client = c))
            # self.pq.append(ExecComp(Executor(endpoint_id = x, funcx_client = c), 0))
            # self.end_status_dict[] = 0

    def submit(self, func, resource_specification, *args, **kwargs):
        """Submits work to the thread pool.

        This method is simply pass through and behaves like a submit call as described
        here `Python docs: <https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor>`_

        """
        if resource_specification:
            logger.error("Ignoring the resource specification. "
                         "Parsl resource specification is not supported in ThreadPool Executor. "
                         "Please check WorkQueue Executor if resource specification is needed.")
            raise UnsupportedFeatureError('resource specification', 'ThreadPool Executor', 'WorkQueue Executor')
        self.index += 1
        return self.Executor_list[self.index % len(self.Executor_list)].submit(func, *args, **kwargs)

    def scale_out(self, workers=1):
        """Scales out the number of active workers by 1.

        This method is notImplemented for threads and will raise the error if called.

        Raises:
             NotImplemented exception
        """
        raise NotImplementedError

    def scale_in(self, blocks):
        """Scale in the number of active blocks by specified amount.

        This method is not implemented for threads and will raise the error if called.

        Raises:
             NotImplemented exception
        """
        raise NotImplementedError

    def shutdown(self, block=True):
        """Shutdown the ThreadPool. The underlying concurrent.futures thread pool
        implementation will not terminate tasks that are being executed, because it
        does not provide a mechanism to do that. With block set to false, this will
        return immediately and it will appear as if the DFK is shut down, but
        the python process will not be able to exit until the thread pool has
        emptied out by task completions. In either case, this can be a very long wait.

        Kwargs:
            - block (Bool): To block for confirmations or not

        """
        logger.debug("Shutting down executor, which involves waiting for running tasks to complete")
        # x = self.executor.shutdown(wait=block)
        logger.debug("Done with executor shutdown")
        # return x

    def monitor_resources(self):
        """Resource monitoring sometimes deadlocks when using threads, so this function
        returns false to disable it."""
        return False