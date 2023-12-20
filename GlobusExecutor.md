# **GlobusExecutor:**

Purpose:
- Enhanced Scalability
- Performance
- Fault Tolerance / Load Balancing
- Cost Efficiency
- Provides Large Compute Resource w/o Single HPC
- Mobile High Performance Parallelized Computing

Architecture Idea 1:
- Executor Implementation 1
    - User submits list of endpoints
    - Priority Queue of Endpoints is Created
        - Updated as tasks are submitted and completed
        - Updating Queue based off Task Completion not possible in Executor
            - Dataflow Idea Emergence
        - Current Implementation: Naive iteration through endpoints
- Executor Implementation 2
    - User submits list of endpoints
    - Singular endpoint is initially used
    - Additional endpoints are leveraged when scaling is necessary
- Executor Implementation 3
    - Single HTEX
    - Submits tasks to endpoints
        - Submission and receiving results must be wrapped into python_apps
    - Dictionary maintained
        - Availability status of each endpoint (# free workers, # active tasks, etc.)
Architecture Idea 2:
- Dataflow
    - Update `dflow.py` and `strategy.py` to acccommodate submitting to "executors" on multiple endpoints while maintaining a priority queue that recommends the ideal endpoint to submit to

Exisiting Implementation:
- Single endpoint implementation is fully functional and packaged
- View `FuncXExecutor.md` for usage clarifications
- Naive Multi-endpoint implementation is fully functional

Current Progress:
- View `parsl.executors.globus` and `multi_endpoint_test.py`