from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_omics._auth._signers
import capo_omics._auth._sigv4
from capo_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_omics.types.batch_id
    import capo_omics.types.cache_behavior
    import capo_omics.types.cancel_run_request
    import capo_omics.types.configuration_name
    import capo_omics.types.delete_run_request
    import capo_omics.types.engine_settings
    import capo_omics.types.get_run_request
    import capo_omics.types.get_run_response
    import capo_omics.types.list_runs_request
    import capo_omics.types.list_runs_response
    import capo_omics.types.networking_mode
    import capo_omics.types.numeric_id_in_arn
    import capo_omics.types.run_export_list
    import capo_omics.types.run_group_id
    import capo_omics.types.run_id
    import capo_omics.types.run_list_item
    import capo_omics.types.run_list_token
    import capo_omics.types.run_log_level
    import capo_omics.types.run_name
    import capo_omics.types.run_output_uri
    import capo_omics.types.run_parameters
    import capo_omics.types.run_request_id
    import capo_omics.types.run_retention_mode
    import capo_omics.types.run_role_arn
    import capo_omics.types.run_status
    import capo_omics.types.scratch_storage_mode
    import capo_omics.types.session_policy
    import capo_omics.types.start_run_request
    import capo_omics.types.start_run_response
    import capo_omics.types.storage_type
    import capo_omics.types.tag_map
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_owner_id
    import capo_omics.types.workflow_type
    import capo_omics.types.workflow_version_name
    from capo_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from capo_omics._services.omics import OmicsClient, OmicsClientConfig


class RunResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        role_arn: "capo_omics.types.run_role_arn.RunRoleArn",
        output_uri: "capo_omics.types.run_output_uri.RunOutputUri",
        request_id: "capo_omics.types.run_request_id.RunRequestId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        workflow_id: Optional["capo_omics.types.workflow_id.WorkflowId"] = None,
        workflow_type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        run_id: Optional["capo_omics.types.run_id.RunId"] = None,
        name: Optional["capo_omics.types.run_name.RunName"] = None,
        cache_id: Optional["capo_omics.types.numeric_id_in_arn.NumericIdInArn"] = None,
        cache_behavior: Optional[
            "capo_omics.types.cache_behavior.CacheBehavior"
        ] = None,
        run_group_id: Optional["capo_omics.types.run_group_id.RunGroupId"] = None,
        priority: Optional[int] = None,
        parameters: Optional["capo_omics.types.run_parameters.RunParameters"] = None,
        storage_capacity: Optional[int] = None,
        log_level: Optional["capo_omics.types.run_log_level.RunLogLevel"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        retention_mode: Optional[
            "capo_omics.types.run_retention_mode.RunRetentionMode"
        ] = None,
        storage_type: Optional["capo_omics.types.storage_type.StorageType"] = None,
        workflow_owner_id: Optional[
            "capo_omics.types.workflow_owner_id.WorkflowOwnerId"
        ] = None,
        workflow_version_name: Optional[
            "capo_omics.types.workflow_version_name.WorkflowVersionName"
        ] = None,
        networking_mode: Optional[
            "capo_omics.types.networking_mode.NetworkingMode"
        ] = None,
        scratch_storage_mode: Optional[
            "capo_omics.types.scratch_storage_mode.ScratchStorageMode"
        ] = None,
        configuration_name: Optional[
            "capo_omics.types.configuration_name.ConfigurationName"
        ] = None,
        session_policy: Optional[
            "capo_omics.types.session_policy.SessionPolicy"
        ] = None,
        engine_settings: Optional[
            "capo_omics.types.engine_settings.EngineSettings"
        ] = None,
    ) -> "capo_omics.types.start_run_response.StartRunResponse":
        """<p>Starts a new run and returns details about the run, or duplicates an existing run. A run is a single invocation of a workflow. If you provide request IDs, Amazon Web Services HealthOmics identifies duplicate requests and starts the run only once. Monitor the progress of the run by calling the <code>GetRun</code> API operation.</p> <p>To start a new run, the following inputs are required:</p> <ul> <li> <p>A service role ARN (<code>roleArn</code>).</p> </li> <li> <p>The run's workflow ID (<code>workflowId</code>, not the <code>uuid</code> or <code>runId</code>).</p> </li> <li> <p>An Amazon S3 location (<code>outputUri</code>) where the run outputs will be saved.</p> </li> <li> <p>All required workflow parameters (<code>parameter</code>), which can include optional parameters from the parameter template. The run cannot include any parameters that are not defined in the parameter template. To see all possible parameters, use the <code>GetRun</code> API operation. </p> </li> <li> <p>For runs with a <code>STATIC</code> (default) storage type, specify the required storage capacity (in gibibytes). A storage capacity value is not required for runs that use <code>DYNAMIC</code> storage.</p> </li> </ul> <p> <code>StartRun</code> can also duplicate an existing run using the run's default values. You can modify these default values and/or add other optional inputs. To duplicate a run, the following inputs are required:</p> <ul> <li> <p>A service role ARN (<code>roleArn</code>).</p> </li> <li> <p>The ID of the run to duplicate (<code>runId</code>).</p> </li> <li> <p>An Amazon S3 location where the run outputs will be saved (<code>outputUri</code>).</p> </li> </ul> <p>To learn more about the optional parameters for <code>StartRun</code>, see <a href="https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html">Starting a run</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p> <p>Use the <code>retentionMode</code> input to control how long the metadata for each run is stored in CloudWatch. There are two retention modes:</p> <ul> <li> <p>Specify <code>REMOVE</code> to automatically remove the oldest runs when you reach the maximum service retention limit for runs. It is recommended that you use the <code>REMOVE</code> mode to initiate major run requests so that your runs do not fail when you reach the limit.</p> </li> <li> <p>The <code>retentionMode</code> is set to the <code>RETAIN</code> mode by default, which allows you to manually remove runs after reaching the maximum service retention limit. Under this setting, you cannot create additional runs until you remove the excess runs.</p> </li> </ul> <p>To learn more about the retention modes, see <a href="https://docs.aws.amazon.com/omics/latest/dev/run-retention.html">Run retention mode</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p> <p>You can use Amazon Q CLI to analyze run logs and make performance optimization recommendations. To get started, see the <a href="https://github.com/awslabs/mcp/tree/main/src/aws-healthomics-mcp-server">Amazon Web Services HealthOmics MCP server</a> on GitHub.</p>

        Args:
            workflow_id: <p>The run's workflow ID. The <code>workflowId</code> is not the UUID.</p>
            workflow_type: <p>The run's workflow type. The <code>workflowType</code> must be specified if you are running a <code>READY2RUN</code> workflow. If you are running a <code>PRIVATE</code> workflow (default), you do not need to include the workflow type. </p>
            run_id: <p>The ID of a run to duplicate.</p>
            role_arn: <p>A service role for the run. The <code>roleArn</code> requires access to Amazon Web Services HealthOmics, S3, Cloudwatch logs, and EC2. An example <code>roleArn</code> is <code>arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ</code>. In this example, the Amazon Web Services account ID is <code>123456789012</code> and the role name is <code>omics-service-role-serviceRole-W8O1XMPL7QZ</code>.</p>
            name: <p>A name for the run. This is recommended to view and organize runs in the Amazon Web Services HealthOmics console and CloudWatch logs.</p>
            cache_id: <p>Identifier of the cache associated with this run. If you don't specify a cache ID, no task outputs are cached for this run.</p>
            cache_behavior: <p>The cache behavior for the run. You specify this value if you want to override the default behavior for the cache. You had set the default value when you created the cache. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior">Run cache behavior</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            run_group_id: <p>The run's group ID. Use a run group to cap the compute resources (and number of concurrent runs) for the runs that you add to the run group.</p>
            priority: <p>Use the run priority (highest: 1) to establish the order of runs in a run group when you start a run. If multiple runs share the same priority, the run that was initiated first will have the higher priority. Runs that do not belong to a run group can be assigned a priority. The priorities of these runs are ranked among other runs that are not in a run group. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/creating-run-groups.html#run-priority">Run priority</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            parameters: <p>Parameters for the run. The run needs all required parameters and can include optional parameters. The run cannot include any parameters that are not defined in the parameter template. To retrieve parameters from the run, use the GetRun API operation.</p>
            storage_capacity: <p>The <code>STATIC</code> storage capacity (in gibibytes, GiB) for this run. The default run storage capacity is 1200 GiB. If your requested storage capacity is unavailable, the system rounds up the value to the nearest 1200 GiB multiple. If the requested storage capacity is still unavailable, the system rounds up the value to the nearest 2400 GiB multiple. This field is not required if the storage type is <code>DYNAMIC</code> (the system ignores any value that you enter).</p>
            output_uri: <p>An output S3 URI for the run. The S3 bucket must be in the same region as the workflow. The role ARN must have permission to write to this S3 bucket.</p>
            log_level: <p>A log level for the run.</p>
            tags: <p>Tags for the run. You can add up to 50 tags per run. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html">Adding a tag</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            request_id: <p>An idempotency token used to dedupe retry requests so that duplicate runs are not created.</p>
            retention_mode: <p>The retention mode for the run. The default value is <code>RETAIN</code>. </p> <p>Amazon Web Services HealthOmics stores a fixed number of runs that are available to the console and API. In the default mode (<code>RETAIN</code>), you need to remove runs manually when the number of run exceeds the maximum. If you set the retention mode to <code>REMOVE</code>, Amazon Web Services HealthOmics automatically removes runs (that have mode set to <code>REMOVE</code>) when the number of run exceeds the maximum. All run logs are available in CloudWatch logs, if you need information about a run that is no longer available to the API.</p> <p>For more information about retention mode, see <a href="https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html">Specifying run retention mode</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            storage_type: <p>The storage type for the run. If you set the storage type to <code>DYNAMIC</code>, Amazon Web Services HealthOmics dynamically scales the storage up or down, based on file system utilization. By default, the run uses <code>STATIC</code> storage type, which allocates a fixed amount of storage. For more information about <code>DYNAMIC</code> and <code>STATIC</code> storage, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html">Run storage types</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            workflow_owner_id: <p>The 12-digit account ID of the workflow owner that is used for running a shared workflow. The workflow owner ID can be retrieved using the <code>GetShare</code> API operation. If you are the workflow owner, you do not need to include this ID.</p>
            workflow_version_name: <p>The name of the workflow version. Use workflow versions to track and organize changes to the workflow. If your workflow has multiple versions, the run uses the default version unless you specify a version name. To learn more, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html">Workflow versioning</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            networking_mode: <p>Optional configuration for run networking behavior. If not specified, this will default to RESTRICTED.</p>
            scratch_storage_mode: <p>Optional configuration for enabling scratch ephemeral storage mounted at /tmp. If not specified, this will default to SHARED. This configuration is applicable only for CPU tasks. For tasks using GPUs, scratch storage is always LOCAL.</p>
            configuration_name: <p>Optional configuration name to use for the workflow run.</p>
            session_policy: Optional inline policy json for scoping down permissions via a session policy on the IAM role provided in the roleArn parameter.
            engine_settings: <p>Engine-specific settings for the workflow run. Use this field to specify configuration options that are specific to the workflow engine (for example, Nextflow profiles).</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.start_run_request.StartRunRequest]",
        ) -> OperationResponse["capo_omics.types.start_run_response.StartRunResponse"]:
            import capo_omics._operations.omics.start_run

            output, http_response = capo_omics._operations.omics.start_run.start_run(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.start_run_request.StartRunRequest = {
            "role_arn": role_arn,
            "output_uri": output_uri,
            "request_id": request_id,
        }
        if workflow_id is not None:
            input_["workflow_id"] = workflow_id
        if workflow_type is not None:
            input_["workflow_type"] = workflow_type
        if run_id is not None:
            input_["run_id"] = run_id
        if name is not None:
            input_["name"] = name
        if cache_id is not None:
            input_["cache_id"] = cache_id
        if cache_behavior is not None:
            input_["cache_behavior"] = cache_behavior
        if run_group_id is not None:
            input_["run_group_id"] = run_group_id
        if priority is not None:
            input_["priority"] = priority
        if parameters is not None:
            input_["parameters"] = parameters
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if log_level is not None:
            input_["log_level"] = log_level
        if tags is not None:
            input_["tags"] = tags
        if retention_mode is not None:
            input_["retention_mode"] = retention_mode
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if workflow_owner_id is not None:
            input_["workflow_owner_id"] = workflow_owner_id
        if workflow_version_name is not None:
            input_["workflow_version_name"] = workflow_version_name
        if networking_mode is not None:
            input_["networking_mode"] = networking_mode
        if scratch_storage_mode is not None:
            input_["scratch_storage_mode"] = scratch_storage_mode
        if configuration_name is not None:
            input_["configuration_name"] = configuration_name
        if session_policy is not None:
            input_["session_policy"] = session_policy
        if engine_settings is not None:
            input_["engine_settings"] = engine_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_omics.types.run_id.RunId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        export: Optional["capo_omics.types.run_export_list.RunExportList"] = None,
    ) -> "capo_omics.types.get_run_response.GetRunResponse":
        """<p>Gets detailed information about a specific run using its ID.</p> <p>Amazon Web Services HealthOmics stores a configurable number of runs, as determined by service limits, that are available to the console and API. If <code>GetRun</code> does not return the requested run, you can find all run logs in the CloudWatch logs. For more information about viewing the run logs, see <a href="https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html">CloudWatch logs</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The run's ID.</p>
            export: <p>The run's export format.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.get_run_request.GetRunRequest]",
        ) -> OperationResponse["capo_omics.types.get_run_response.GetRunResponse"]:
            import capo_omics._operations.omics.get_run

            output, http_response = capo_omics._operations.omics.get_run.get_run(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_run_request.GetRunRequest = {"id": id}
        if export is not None:
            input_["export"] = export

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_omics.types.run_id.RunId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run and returns a response with no body if the operation is successful. You can only delete a run that has reached a <code>COMPLETED</code>, <code>FAILED</code>, or <code>CANCELLED</code> stage. A completed run has delivered an output, or was cancelled and resulted in no output. When you delete a run, only the metadata associated with the run is deleted. The run outputs remain in Amazon S3 and logs remain in CloudWatch.</p> <p>To verify that the workflow is deleted:</p> <ul> <li> <p>Use <code>ListRuns</code> to confirm the workflow no longer appears in the list.</p> </li> <li> <p>Use <code>GetRun</code> to verify the workflow cannot be found.</p> </li> </ul>

        Args:
            id: <p>The run's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.delete_run_request.DeleteRunRequest]",
        ) -> OperationResponse[None]:
            import capo_omics._operations.omics.delete_run

            output, http_response = capo_omics._operations.omics.delete_run.delete_run(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_run_request.DeleteRunRequest = {"id": id}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_name.RunName"] = None,
        run_group_id: Optional["capo_omics.types.run_group_id.RunGroupId"] = None,
        batch_id: Optional["capo_omics.types.batch_id.BatchId"] = None,
        starting_token: Optional["capo_omics.types.run_list_token.RunListToken"] = None,
        max_results: Optional[int] = None,
        status: Optional["capo_omics.types.run_status.RunStatus"] = None,
    ) -> "capo_omics.types.list_runs_response.ListRunsResponse":
        """<p>Retrieves a list of runs and returns each run's metadata and status.</p> <p>Amazon Web Services HealthOmics stores a configurable number of runs, as determined by service limits, that are available to the console and API. If the <code>ListRuns</code> response doesn't include specific runs that you expected, you can find all run logs in the CloudWatch logs. For more information about viewing the run logs, see <a href="https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html">CloudWatch logs</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>Filter the list by run name.</p>
            run_group_id: <p>Filter the list by run group ID.</p>
            batch_id: <p>Filter by batch ID.</p>
            starting_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of runs to return in one page of results.</p>
            status: <p>The status of a run.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_runs_request.ListRunsRequest]",
        ) -> OperationResponse["capo_omics.types.list_runs_response.ListRunsResponse"]:
            import capo_omics._operations.omics.list_runs

            output, http_response = capo_omics._operations.omics.list_runs.list_runs(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_runs_request.ListRunsRequest = {}
        if name is not None:
            input_["name"] = name
        if run_group_id is not None:
            input_["run_group_id"] = run_group_id
        if batch_id is not None:
            input_["batch_id"] = batch_id
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_run(
        self,
        id: "capo_omics.types.run_id.RunId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> None:
        """<p>Cancels a run using its ID and returns a response with no body if the operation is successful. To confirm that the run has been cancelled, use the <code>ListRuns</code> API operation to check that it is no longer listed.</p>

        Args:
            id: <p>The run's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.cancel_run_request.CancelRunRequest]",
        ) -> OperationResponse[None]:
            import capo_omics._operations.omics.cancel_run

            output, http_response = capo_omics._operations.omics.cancel_run.cancel_run(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.cancel_run_request.CancelRunRequest = {"id": id}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRunResource:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        role_arn: "capo_omics.types.run_role_arn.RunRoleArn",
        output_uri: "capo_omics.types.run_output_uri.RunOutputUri",
        request_id: "capo_omics.types.run_request_id.RunRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        workflow_id: Optional["capo_omics.types.workflow_id.WorkflowId"] = None,
        workflow_type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        run_id: Optional["capo_omics.types.run_id.RunId"] = None,
        name: Optional["capo_omics.types.run_name.RunName"] = None,
        cache_id: Optional["capo_omics.types.numeric_id_in_arn.NumericIdInArn"] = None,
        cache_behavior: Optional[
            "capo_omics.types.cache_behavior.CacheBehavior"
        ] = None,
        run_group_id: Optional["capo_omics.types.run_group_id.RunGroupId"] = None,
        priority: Optional[int] = None,
        parameters: Optional["capo_omics.types.run_parameters.RunParameters"] = None,
        storage_capacity: Optional[int] = None,
        log_level: Optional["capo_omics.types.run_log_level.RunLogLevel"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        retention_mode: Optional[
            "capo_omics.types.run_retention_mode.RunRetentionMode"
        ] = None,
        storage_type: Optional["capo_omics.types.storage_type.StorageType"] = None,
        workflow_owner_id: Optional[
            "capo_omics.types.workflow_owner_id.WorkflowOwnerId"
        ] = None,
        workflow_version_name: Optional[
            "capo_omics.types.workflow_version_name.WorkflowVersionName"
        ] = None,
        networking_mode: Optional[
            "capo_omics.types.networking_mode.NetworkingMode"
        ] = None,
        scratch_storage_mode: Optional[
            "capo_omics.types.scratch_storage_mode.ScratchStorageMode"
        ] = None,
        configuration_name: Optional[
            "capo_omics.types.configuration_name.ConfigurationName"
        ] = None,
        session_policy: Optional[
            "capo_omics.types.session_policy.SessionPolicy"
        ] = None,
        engine_settings: Optional[
            "capo_omics.types.engine_settings.EngineSettings"
        ] = None,
    ) -> "capo_omics.types.start_run_response.StartRunResponse":
        """<p>Starts a new run and returns details about the run, or duplicates an existing run. A run is a single invocation of a workflow. If you provide request IDs, Amazon Web Services HealthOmics identifies duplicate requests and starts the run only once. Monitor the progress of the run by calling the <code>GetRun</code> API operation.</p> <p>To start a new run, the following inputs are required:</p> <ul> <li> <p>A service role ARN (<code>roleArn</code>).</p> </li> <li> <p>The run's workflow ID (<code>workflowId</code>, not the <code>uuid</code> or <code>runId</code>).</p> </li> <li> <p>An Amazon S3 location (<code>outputUri</code>) where the run outputs will be saved.</p> </li> <li> <p>All required workflow parameters (<code>parameter</code>), which can include optional parameters from the parameter template. The run cannot include any parameters that are not defined in the parameter template. To see all possible parameters, use the <code>GetRun</code> API operation. </p> </li> <li> <p>For runs with a <code>STATIC</code> (default) storage type, specify the required storage capacity (in gibibytes). A storage capacity value is not required for runs that use <code>DYNAMIC</code> storage.</p> </li> </ul> <p> <code>StartRun</code> can also duplicate an existing run using the run's default values. You can modify these default values and/or add other optional inputs. To duplicate a run, the following inputs are required:</p> <ul> <li> <p>A service role ARN (<code>roleArn</code>).</p> </li> <li> <p>The ID of the run to duplicate (<code>runId</code>).</p> </li> <li> <p>An Amazon S3 location where the run outputs will be saved (<code>outputUri</code>).</p> </li> </ul> <p>To learn more about the optional parameters for <code>StartRun</code>, see <a href="https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html">Starting a run</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p> <p>Use the <code>retentionMode</code> input to control how long the metadata for each run is stored in CloudWatch. There are two retention modes:</p> <ul> <li> <p>Specify <code>REMOVE</code> to automatically remove the oldest runs when you reach the maximum service retention limit for runs. It is recommended that you use the <code>REMOVE</code> mode to initiate major run requests so that your runs do not fail when you reach the limit.</p> </li> <li> <p>The <code>retentionMode</code> is set to the <code>RETAIN</code> mode by default, which allows you to manually remove runs after reaching the maximum service retention limit. Under this setting, you cannot create additional runs until you remove the excess runs.</p> </li> </ul> <p>To learn more about the retention modes, see <a href="https://docs.aws.amazon.com/omics/latest/dev/run-retention.html">Run retention mode</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p> <p>You can use Amazon Q CLI to analyze run logs and make performance optimization recommendations. To get started, see the <a href="https://github.com/awslabs/mcp/tree/main/src/aws-healthomics-mcp-server">Amazon Web Services HealthOmics MCP server</a> on GitHub.</p>

        Args:
            workflow_id: <p>The run's workflow ID. The <code>workflowId</code> is not the UUID.</p>
            workflow_type: <p>The run's workflow type. The <code>workflowType</code> must be specified if you are running a <code>READY2RUN</code> workflow. If you are running a <code>PRIVATE</code> workflow (default), you do not need to include the workflow type. </p>
            run_id: <p>The ID of a run to duplicate.</p>
            role_arn: <p>A service role for the run. The <code>roleArn</code> requires access to Amazon Web Services HealthOmics, S3, Cloudwatch logs, and EC2. An example <code>roleArn</code> is <code>arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ</code>. In this example, the Amazon Web Services account ID is <code>123456789012</code> and the role name is <code>omics-service-role-serviceRole-W8O1XMPL7QZ</code>.</p>
            name: <p>A name for the run. This is recommended to view and organize runs in the Amazon Web Services HealthOmics console and CloudWatch logs.</p>
            cache_id: <p>Identifier of the cache associated with this run. If you don't specify a cache ID, no task outputs are cached for this run.</p>
            cache_behavior: <p>The cache behavior for the run. You specify this value if you want to override the default behavior for the cache. You had set the default value when you created the cache. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior">Run cache behavior</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            run_group_id: <p>The run's group ID. Use a run group to cap the compute resources (and number of concurrent runs) for the runs that you add to the run group.</p>
            priority: <p>Use the run priority (highest: 1) to establish the order of runs in a run group when you start a run. If multiple runs share the same priority, the run that was initiated first will have the higher priority. Runs that do not belong to a run group can be assigned a priority. The priorities of these runs are ranked among other runs that are not in a run group. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/creating-run-groups.html#run-priority">Run priority</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            parameters: <p>Parameters for the run. The run needs all required parameters and can include optional parameters. The run cannot include any parameters that are not defined in the parameter template. To retrieve parameters from the run, use the GetRun API operation.</p>
            storage_capacity: <p>The <code>STATIC</code> storage capacity (in gibibytes, GiB) for this run. The default run storage capacity is 1200 GiB. If your requested storage capacity is unavailable, the system rounds up the value to the nearest 1200 GiB multiple. If the requested storage capacity is still unavailable, the system rounds up the value to the nearest 2400 GiB multiple. This field is not required if the storage type is <code>DYNAMIC</code> (the system ignores any value that you enter).</p>
            output_uri: <p>An output S3 URI for the run. The S3 bucket must be in the same region as the workflow. The role ARN must have permission to write to this S3 bucket.</p>
            log_level: <p>A log level for the run.</p>
            tags: <p>Tags for the run. You can add up to 50 tags per run. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html">Adding a tag</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            request_id: <p>An idempotency token used to dedupe retry requests so that duplicate runs are not created.</p>
            retention_mode: <p>The retention mode for the run. The default value is <code>RETAIN</code>. </p> <p>Amazon Web Services HealthOmics stores a fixed number of runs that are available to the console and API. In the default mode (<code>RETAIN</code>), you need to remove runs manually when the number of run exceeds the maximum. If you set the retention mode to <code>REMOVE</code>, Amazon Web Services HealthOmics automatically removes runs (that have mode set to <code>REMOVE</code>) when the number of run exceeds the maximum. All run logs are available in CloudWatch logs, if you need information about a run that is no longer available to the API.</p> <p>For more information about retention mode, see <a href="https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html">Specifying run retention mode</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            storage_type: <p>The storage type for the run. If you set the storage type to <code>DYNAMIC</code>, Amazon Web Services HealthOmics dynamically scales the storage up or down, based on file system utilization. By default, the run uses <code>STATIC</code> storage type, which allocates a fixed amount of storage. For more information about <code>DYNAMIC</code> and <code>STATIC</code> storage, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html">Run storage types</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            workflow_owner_id: <p>The 12-digit account ID of the workflow owner that is used for running a shared workflow. The workflow owner ID can be retrieved using the <code>GetShare</code> API operation. If you are the workflow owner, you do not need to include this ID.</p>
            workflow_version_name: <p>The name of the workflow version. Use workflow versions to track and organize changes to the workflow. If your workflow has multiple versions, the run uses the default version unless you specify a version name. To learn more, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html">Workflow versioning</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            networking_mode: <p>Optional configuration for run networking behavior. If not specified, this will default to RESTRICTED.</p>
            scratch_storage_mode: <p>Optional configuration for enabling scratch ephemeral storage mounted at /tmp. If not specified, this will default to SHARED. This configuration is applicable only for CPU tasks. For tasks using GPUs, scratch storage is always LOCAL.</p>
            configuration_name: <p>Optional configuration name to use for the workflow run.</p>
            session_policy: Optional inline policy json for scoping down permissions via a session policy on the IAM role provided in the roleArn parameter.
            engine_settings: <p>Engine-specific settings for the workflow run. Use this field to specify configuration options that are specific to the workflow engine (for example, Nextflow profiles).</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.start_run_request.StartRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_run_response.StartRunResponse"
        ]:
            import capo_omics._operations.omics.start_run

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_run.async_start_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.start_run_request.StartRunRequest = {
            "role_arn": role_arn,
            "output_uri": output_uri,
            "request_id": request_id,
        }
        if workflow_id is not None:
            input_["workflow_id"] = workflow_id
        if workflow_type is not None:
            input_["workflow_type"] = workflow_type
        if run_id is not None:
            input_["run_id"] = run_id
        if name is not None:
            input_["name"] = name
        if cache_id is not None:
            input_["cache_id"] = cache_id
        if cache_behavior is not None:
            input_["cache_behavior"] = cache_behavior
        if run_group_id is not None:
            input_["run_group_id"] = run_group_id
        if priority is not None:
            input_["priority"] = priority
        if parameters is not None:
            input_["parameters"] = parameters
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if log_level is not None:
            input_["log_level"] = log_level
        if tags is not None:
            input_["tags"] = tags
        if retention_mode is not None:
            input_["retention_mode"] = retention_mode
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if workflow_owner_id is not None:
            input_["workflow_owner_id"] = workflow_owner_id
        if workflow_version_name is not None:
            input_["workflow_version_name"] = workflow_version_name
        if networking_mode is not None:
            input_["networking_mode"] = networking_mode
        if scratch_storage_mode is not None:
            input_["scratch_storage_mode"] = scratch_storage_mode
        if configuration_name is not None:
            input_["configuration_name"] = configuration_name
        if session_policy is not None:
            input_["session_policy"] = session_policy
        if engine_settings is not None:
            input_["engine_settings"] = engine_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        id: "capo_omics.types.run_id.RunId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        export: Optional["capo_omics.types.run_export_list.RunExportList"] = None,
    ) -> "capo_omics.types.get_run_response.GetRunResponse":
        """<p>Gets detailed information about a specific run using its ID.</p> <p>Amazon Web Services HealthOmics stores a configurable number of runs, as determined by service limits, that are available to the console and API. If <code>GetRun</code> does not return the requested run, you can find all run logs in the CloudWatch logs. For more information about viewing the run logs, see <a href="https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html">CloudWatch logs</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The run's ID.</p>
            export: <p>The run's export format.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_run_request.GetRunRequest]",
        ) -> AsyncOperationResponse["capo_omics.types.get_run_response.GetRunResponse"]:
            import capo_omics._operations.omics.get_run

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_run.async_get_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_run_request.GetRunRequest = {"id": id}
        if export is not None:
            input_["export"] = export

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_omics.types.run_id.RunId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run and returns a response with no body if the operation is successful. You can only delete a run that has reached a <code>COMPLETED</code>, <code>FAILED</code>, or <code>CANCELLED</code> stage. A completed run has delivered an output, or was cancelled and resulted in no output. When you delete a run, only the metadata associated with the run is deleted. The run outputs remain in Amazon S3 and logs remain in CloudWatch.</p> <p>To verify that the workflow is deleted:</p> <ul> <li> <p>Use <code>ListRuns</code> to confirm the workflow no longer appears in the list.</p> </li> <li> <p>Use <code>GetRun</code> to verify the workflow cannot be found.</p> </li> </ul>

        Args:
            id: <p>The run's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_run_request.DeleteRunRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_run

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_run.async_delete_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_run_request.DeleteRunRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.run_name.RunName"] = None,
        run_group_id: Optional["capo_omics.types.run_group_id.RunGroupId"] = None,
        batch_id: Optional["capo_omics.types.batch_id.BatchId"] = None,
        starting_token: Optional["capo_omics.types.run_list_token.RunListToken"] = None,
        max_results: Optional[int] = None,
        status: Optional["capo_omics.types.run_status.RunStatus"] = None,
    ) -> "capo_omics.types.list_runs_response.ListRunsResponse":
        """<p>Retrieves a list of runs and returns each run's metadata and status.</p> <p>Amazon Web Services HealthOmics stores a configurable number of runs, as determined by service limits, that are available to the console and API. If the <code>ListRuns</code> response doesn't include specific runs that you expected, you can find all run logs in the CloudWatch logs. For more information about viewing the run logs, see <a href="https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html">CloudWatch logs</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>Filter the list by run name.</p>
            run_group_id: <p>Filter the list by run group ID.</p>
            batch_id: <p>Filter by batch ID.</p>
            starting_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of runs to return in one page of results.</p>
            status: <p>The status of a run.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_runs_request.ListRunsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_runs_response.ListRunsResponse"
        ]:
            import capo_omics._operations.omics.list_runs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_runs.async_list_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_runs_request.ListRunsRequest = {}
        if name is not None:
            input_["name"] = name
        if run_group_id is not None:
            input_["run_group_id"] = run_group_id
        if batch_id is not None:
            input_["batch_id"] = batch_id
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_run(
        self,
        id: "capo_omics.types.run_id.RunId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Cancels a run using its ID and returns a response with no body if the operation is successful. To confirm that the run has been cancelled, use the <code>ListRuns</code> API operation to check that it is no longer listed.</p>

        Args:
            id: <p>The run's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.cancel_run_request.CancelRunRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.cancel_run

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.cancel_run.async_cancel_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.cancel_run_request.CancelRunRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
