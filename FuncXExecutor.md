# **FuncXExecutor:**

**Pytest Suite:**

test_fail.py:
- test_no_deps:
    - Requires Access to Locally Defined Class (ManufacturedTestFailure)
    - Marked w/ `@pytest.mark.local`

test_file_apps.py:
- test_files:
    - Requires Access to Defined File Paths
    - Incorrect Param Format for File Path For Non-Local Tests
    - Marked w/ `@pytest.mark.local`
- test_increment:
    - Requires Access to Defined File Paths
    - Incorrect Param Format for File Path For Non-Local Tests
    - Marked w/ `@pytest.mark.local`

**User Instructions:**

Define and Configure Globus Compute Endpoint:
- Ensure your system has Globus Compute and Globus-Compute-Endpoint properly installed (https://funcx.readthedocs.io/en/latest/endpoints.html)
- Run the command `globus-compute-endpoint configure <ENDPOINT_NAME>`
    - This command will create endpoint <ENDPOINT_NAME> that you will submit your parsl apps to
- Run the command `vi $HOME/.globus_compute/<ENDPOINT_NAME>/config.yaml` to visit and edit endpoint configuration
    - This will enable you to set the provider, executor, launchers, blocks, and nodes regarding your endpoint
    - Sample `config.yaml`
        ```yaml
        display_name: test_endpoint
        engine:
        provider:
            init_blocks: 2
            max_blocks: 2
            min_blocks: 2
            type: LocalProvider
        type: HighThroughputEngine
        ```

Verify Parsl Version and Compatability w/ FuncXExec:
- Edit Pytest suite according to Pytest comments above
- Run the command `pytest parsl/tests/ --config parsl/tests/configs/funcx.py  -k 'not cleannet' --full-trace`
    - All test cases should pass if properly configured
    - Else, consult Ved Kommalapati within Parsl and FuncX Slack Channels
- Verify that endpoint and user side have same python version (Error if not verified)
```
   File "/usr/local/lib/python3.10/site-packages/dill/_dill.py", line 805, in _create_code
     return CodeType(args[0], 0, 0, *args[1:])
 TypeError: code expected at most 16 arguments, got 21
```
Set Up funcXExecutor:
- Ensure your workflow effectively follows Parsl Guidelines (visit Parsl repository for further context)
    - Example: Functions are declared as either python_app or bash_app
- Load configuration that leverages `FuncXExec`
- User can define parameters (example below):
    ```yaml
    endpoint_id='8e7f13f5-5a89-49c6-85b4-f8929cb0d8ae', 
    label='threads', 
    max_threads=16, 
    storage_access=None,
    thread_name_prefix='', 
    working_dir=None
    ```
- Example:
    ```python
    def fresh_config():
        return Config(
            executors=[FuncXExec(endpoint_id = 'fa11b360-9f04-4df8-903e-81fc706fd21c', max_threads = 16)]
        )

    parsl.load(fresh_config())
    ```

Helpful Resources:
- https://funcx.readthedocs.io/en/latest/endpoints.html
- https://funcx.readthedocs.io/en/latest/tutorial.html
- https://parsl.readthedocs.io/en/stable/