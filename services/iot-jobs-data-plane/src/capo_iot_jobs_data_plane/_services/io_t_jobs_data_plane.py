"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#IotLaserThingJobManagerExternalService``."""

import uuid
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_iot_jobs_data_plane._auth._signers
import capo_iot_jobs_data_plane._auth._sigv4
from capo_iot_jobs_data_plane._auth._identity import Credentials
from capo_iot_jobs_data_plane._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iot_jobs_data_plane._auth._zapros_handler import AuthMiddleware
from capo_iot_jobs_data_plane._services._aws_config import aws_config
from capo_iot_jobs_data_plane._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.client_request_token_v2
    import capo_iot_jobs_data_plane.types.command_arn
    import capo_iot_jobs_data_plane.types.command_execution_parameter_map
    import capo_iot_jobs_data_plane.types.command_execution_timeout_in_seconds
    import capo_iot_jobs_data_plane.types.describe_job_execution_job_id
    import capo_iot_jobs_data_plane.types.describe_job_execution_request
    import capo_iot_jobs_data_plane.types.describe_job_execution_response
    import capo_iot_jobs_data_plane.types.details_map
    import capo_iot_jobs_data_plane.types.execution_number
    import capo_iot_jobs_data_plane.types.expected_version
    import capo_iot_jobs_data_plane.types.get_pending_job_executions_request
    import capo_iot_jobs_data_plane.types.get_pending_job_executions_response
    import capo_iot_jobs_data_plane.types.include_execution_state
    import capo_iot_jobs_data_plane.types.include_job_document
    import capo_iot_jobs_data_plane.types.job_execution_status
    import capo_iot_jobs_data_plane.types.job_id
    import capo_iot_jobs_data_plane.types.start_command_execution_request
    import capo_iot_jobs_data_plane.types.start_command_execution_response
    import capo_iot_jobs_data_plane.types.start_next_pending_job_execution_request
    import capo_iot_jobs_data_plane.types.start_next_pending_job_execution_response
    import capo_iot_jobs_data_plane.types.step_timeout_in_minutes
    import capo_iot_jobs_data_plane.types.target_arn
    import capo_iot_jobs_data_plane.types.thing_name
    import capo_iot_jobs_data_plane.types.update_job_execution_request
    import capo_iot_jobs_data_plane.types.update_job_execution_response


class IoTJobsDataPlaneClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class IoTJobsDataPlaneClient:
    """A client for the ``IoTJobsDataPlane`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = IoTJobsDataPlaneClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[IoTJobsDataPlaneClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: IoTJobsDataPlaneClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def describe_job_execution(
        self,
        job_id: "capo_iot_jobs_data_plane.types.describe_job_execution_job_id.DescribeJobExecutionJobId",
        thing_name: "capo_iot_jobs_data_plane.types.thing_name.ThingName",
        *,
        config_overrides: Optional[IoTJobsDataPlaneClientConfig] = None,
        include_job_document: Optional[
            "capo_iot_jobs_data_plane.types.include_job_document.IncludeJobDocument"
        ] = None,
        execution_number: Optional[
            "capo_iot_jobs_data_plane.types.execution_number.ExecutionNumber"
        ] = None,
    ) -> "capo_iot_jobs_data_plane.types.describe_job_execution_response.DescribeJobExecutionResponse":
        """<p>Gets details of a job execution.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">DescribeJobExecution</a> action.</p>

        Args:
            job_id: <p>The unique identifier assigned to this job when it was created.</p>
            thing_name: <p>The thing name associated with the device the job execution is running on.</p>
            include_job_document: <p>Optional. Unless set to false, the response contains the job document. The default is true.</p>
            execution_number: <p>Optional. A number that identifies a particular job execution on a particular device. If not specified, the latest job execution is returned.</p>

        Raises:
            capo_iot_jobs_data_plane.errors.certificate_validation_exception.CertificateValidationException: <p>The certificate is invalid.</p>
            capo_iot_jobs_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The contents of the request were invalid.</p>
            capo_iot_jobs_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_jobs_data_plane.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_jobs_data_plane.errors.terminal_state_exception.TerminalStateException: <p>The job is in a terminal state.</p>
            capo_iot_jobs_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_jobs_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_jobs_data_plane.types.describe_job_execution_request.DescribeJobExecutionRequest]",
        ) -> OperationResponse[
            "capo_iot_jobs_data_plane.types.describe_job_execution_response.DescribeJobExecutionResponse"
        ]:
            import capo_iot_jobs_data_plane._operations.iot_laser_thing_job_manager_external_service.describe_job_execution

            output, http_response = (
                capo_iot_jobs_data_plane._operations.iot_laser_thing_job_manager_external_service.describe_job_execution.describe_job_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_jobs_data_plane.types.describe_job_execution_request.DescribeJobExecutionRequest = {
            "job_id": job_id,
            "thing_name": thing_name,
        }
        if include_job_document is not None:
            input_["include_job_document"] = include_job_document
        if execution_number is not None:
            input_["execution_number"] = execution_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_pending_job_executions(
        self,
        thing_name: "capo_iot_jobs_data_plane.types.thing_name.ThingName",
        *,
        config_overrides: Optional[IoTJobsDataPlaneClientConfig] = None,
    ) -> "capo_iot_jobs_data_plane.types.get_pending_job_executions_response.GetPendingJobExecutionsResponse":
        """<p>Gets the list of all jobs for a thing that are not in a terminal status.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">GetPendingJobExecutions</a> action.</p>

        Args:
            thing_name: <p>The name of the thing that is executing the job.</p>

        Raises:
            capo_iot_jobs_data_plane.errors.certificate_validation_exception.CertificateValidationException: <p>The certificate is invalid.</p>
            capo_iot_jobs_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The contents of the request were invalid.</p>
            capo_iot_jobs_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_jobs_data_plane.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_jobs_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_jobs_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_jobs_data_plane.types.get_pending_job_executions_request.GetPendingJobExecutionsRequest]",
        ) -> OperationResponse[
            "capo_iot_jobs_data_plane.types.get_pending_job_executions_response.GetPendingJobExecutionsResponse"
        ]:
            import capo_iot_jobs_data_plane._operations.iot_laser_thing_job_manager_external_service.get_pending_job_executions

            output, http_response = (
                capo_iot_jobs_data_plane._operations.iot_laser_thing_job_manager_external_service.get_pending_job_executions.get_pending_job_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_jobs_data_plane.types.get_pending_job_executions_request.GetPendingJobExecutionsRequest = {
            "thing_name": thing_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_command_execution(
        self,
        target_arn: "capo_iot_jobs_data_plane.types.target_arn.TargetArn",
        command_arn: "capo_iot_jobs_data_plane.types.command_arn.CommandArn",
        *,
        config_overrides: Optional[IoTJobsDataPlaneClientConfig] = None,
        parameters: Optional[
            "capo_iot_jobs_data_plane.types.command_execution_parameter_map.CommandExecutionParameterMap"
        ] = None,
        execution_timeout_seconds: Optional[
            "capo_iot_jobs_data_plane.types.command_execution_timeout_in_seconds.CommandExecutionTimeoutInSeconds"
        ] = None,
        client_token: Optional[
            "capo_iot_jobs_data_plane.types.client_request_token_v2.ClientRequestTokenV2"
        ] = None,
    ) -> "capo_iot_jobs_data_plane.types.start_command_execution_response.StartCommandExecutionResponse":
        """<p>Using the command created with the <code>CreateCommand</code> API, start a command execution on a specific device.</p>

        Args:
            target_arn: <p>The Amazon Resource Number (ARN) of the device where the command execution is occurring.</p>
            command_arn: <p>The Amazon Resource Number (ARN) of the command. For example, <code>arn:aws:iot:<region>:<accountid>:command/<commandName></code> </p>
            parameters: <p>A list of parameters that are required by the <code>StartCommandExecution</code> API when performing the command on a device.</p>
            execution_timeout_seconds: <p>Specifies the amount of time in second the device has to finish the command execution. A timer is started as soon as the command execution is created. If the command execution status is not set to another terminal state before the timer expires, it will automatically update to <code>TIMED_OUT</code>.</p>
            client_token: <p>The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you retry the request using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, Amazon Web Services SDKs will automatically generate a unique client request.</p>

        Raises:
            capo_iot_jobs_data_plane.errors.conflict_exception.ConflictException: <p>A conflict has occurred when performing the API request.</p>
            capo_iot_jobs_data_plane.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred when performing the API request.</p>
            capo_iot_jobs_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_jobs_data_plane.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this request.</p>
            capo_iot_jobs_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_jobs_data_plane.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_jobs_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_jobs_data_plane.types.start_command_execution_request.StartCommandExecutionRequest]",
        ) -> OperationResponse[
            "capo_iot_jobs_data_plane.types.start_command_execution_response.StartCommandExecutionResponse"
        ]:
            import capo_iot_jobs_data_plane._operations.iot_laser_thing_job_manager_external_service.start_command_execution

            output, http_response = (
                capo_iot_jobs_data_plane._operations.iot_laser_thing_job_manager_external_service.start_command_execution.start_command_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_jobs_data_plane.types.start_command_execution_request.StartCommandExecutionRequest = {
            "target_arn": target_arn,
            "command_arn": command_arn,
        }
        if parameters is not None:
            input_["parameters"] = parameters
        if execution_timeout_seconds is not None:
            input_["execution_timeout_seconds"] = execution_timeout_seconds
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_next_pending_job_execution(
        self,
        thing_name: "capo_iot_jobs_data_plane.types.thing_name.ThingName",
        *,
        config_overrides: Optional[IoTJobsDataPlaneClientConfig] = None,
        status_details: Optional[
            "capo_iot_jobs_data_plane.types.details_map.DetailsMap"
        ] = None,
        step_timeout_in_minutes: Optional[
            "capo_iot_jobs_data_plane.types.step_timeout_in_minutes.StepTimeoutInMinutes"
        ] = None,
    ) -> "capo_iot_jobs_data_plane.types.start_next_pending_job_execution_response.StartNextPendingJobExecutionResponse":
        """<p>Gets and starts the next pending (status IN_PROGRESS or QUEUED) job execution for a thing.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">StartNextPendingJobExecution</a> action.</p>

        Args:
            thing_name: <p>The name of the thing associated with the device.</p>
            status_details: <p>A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.</p> <p>The maximum length of the value in the name/value pair is 1,024 characters.</p>
            step_timeout_in_minutes: <p>Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by calling <code>UpdateJobExecution</code>, setting the status to <code>IN_PROGRESS</code>, and specifying a new timeout value in field <code>stepTimeoutInMinutes</code>) the job execution status will be automatically set to <code>TIMED_OUT</code>. Note that setting the step timeout has no effect on the in progress timeout that may have been specified when the job was created (<code>CreateJob</code> using field <code>timeoutConfig</code>).</p> <p>Valid values for this parameter range from 1 to 10080 (1 minute to 7 days).</p>

        Raises:
            capo_iot_jobs_data_plane.errors.certificate_validation_exception.CertificateValidationException: <p>The certificate is invalid.</p>
            capo_iot_jobs_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The contents of the request were invalid.</p>
            capo_iot_jobs_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_jobs_data_plane.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_jobs_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_jobs_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_jobs_data_plane.types.start_next_pending_job_execution_request.StartNextPendingJobExecutionRequest]",
        ) -> OperationResponse[
            "capo_iot_jobs_data_plane.types.start_next_pending_job_execution_response.StartNextPendingJobExecutionResponse"
        ]:
            import capo_iot_jobs_data_plane._operations.iot_laser_thing_job_manager_external_service.start_next_pending_job_execution

            output, http_response = (
                capo_iot_jobs_data_plane._operations.iot_laser_thing_job_manager_external_service.start_next_pending_job_execution.start_next_pending_job_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_jobs_data_plane.types.start_next_pending_job_execution_request.StartNextPendingJobExecutionRequest = {
            "thing_name": thing_name
        }
        if status_details is not None:
            input_["status_details"] = status_details
        if step_timeout_in_minutes is not None:
            input_["step_timeout_in_minutes"] = step_timeout_in_minutes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_job_execution(
        self,
        job_id: "capo_iot_jobs_data_plane.types.job_id.JobId",
        thing_name: "capo_iot_jobs_data_plane.types.thing_name.ThingName",
        status: "capo_iot_jobs_data_plane.types.job_execution_status.JobExecutionStatus",
        *,
        config_overrides: Optional[IoTJobsDataPlaneClientConfig] = None,
        status_details: Optional[
            "capo_iot_jobs_data_plane.types.details_map.DetailsMap"
        ] = None,
        step_timeout_in_minutes: Optional[
            "capo_iot_jobs_data_plane.types.step_timeout_in_minutes.StepTimeoutInMinutes"
        ] = None,
        expected_version: Optional[
            "capo_iot_jobs_data_plane.types.expected_version.ExpectedVersion"
        ] = None,
        include_job_execution_state: Optional[
            "capo_iot_jobs_data_plane.types.include_execution_state.IncludeExecutionState"
        ] = None,
        include_job_document: Optional[
            "capo_iot_jobs_data_plane.types.include_job_document.IncludeJobDocument"
        ] = None,
        execution_number: Optional[
            "capo_iot_jobs_data_plane.types.execution_number.ExecutionNumber"
        ] = None,
    ) -> "capo_iot_jobs_data_plane.types.update_job_execution_response.UpdateJobExecutionResponse":
        """<p>Updates the status of a job execution.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotjobsdataplane.html">UpdateJobExecution</a> action.</p>

        Args:
            job_id: <p>The unique identifier assigned to this job when it was created.</p>
            thing_name: <p>The name of the thing associated with the device.</p>
            status: <p>The new status for the job execution (IN_PROGRESS, FAILED, SUCCESS, or REJECTED). This must be specified on every update.</p>
            status_details: <p> Optional. A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.</p> <p>The maximum length of the value in the name/value pair is 1,024 characters.</p>
            step_timeout_in_minutes: <p>Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by again calling <code>UpdateJobExecution</code>, setting the status to <code>IN_PROGRESS</code>, and specifying a new timeout value in this field) the job execution status will be automatically set to <code>TIMED_OUT</code>. Note that setting or resetting the step timeout has no effect on the in progress timeout that may have been specified when the job was created (<code>CreateJob</code> using field <code>timeoutConfig</code>).</p> <p>Valid values for this parameter range from 1 to 10080 (1 minute to 7 days). A value of -1 is also valid and will cancel the current step timer (created by an earlier use of <code>UpdateJobExecutionRequest</code>).</p>
            expected_version: <p>Optional. The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)</p>
            include_job_execution_state: <p>Optional. When included and set to true, the response contains the JobExecutionState data. The default is false.</p>
            include_job_document: <p>Optional. When set to true, the response contains the job document. The default is false.</p>
            execution_number: <p>Optional. A number that identifies a particular job execution on a particular device.</p>

        Raises:
            capo_iot_jobs_data_plane.errors.certificate_validation_exception.CertificateValidationException: <p>The certificate is invalid.</p>
            capo_iot_jobs_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The contents of the request were invalid.</p>
            capo_iot_jobs_data_plane.errors.invalid_state_transition_exception.InvalidStateTransitionException: <p>An update attempted to change the job execution to a state that is invalid because of the job execution's current state (for example, an attempt to change a request in state SUCCESS to state IN_PROGRESS). In this case, the body of the error message also contains the executionState field.</p>
            capo_iot_jobs_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_jobs_data_plane.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_jobs_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_jobs_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_jobs_data_plane.types.update_job_execution_request.UpdateJobExecutionRequest]",
        ) -> OperationResponse[
            "capo_iot_jobs_data_plane.types.update_job_execution_response.UpdateJobExecutionResponse"
        ]:
            import capo_iot_jobs_data_plane._operations.iot_laser_thing_job_manager_external_service.update_job_execution

            output, http_response = (
                capo_iot_jobs_data_plane._operations.iot_laser_thing_job_manager_external_service.update_job_execution.update_job_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_jobs_data_plane.types.update_job_execution_request.UpdateJobExecutionRequest = {
            "job_id": job_id,
            "thing_name": thing_name,
            "status": status,
        }
        if status_details is not None:
            input_["status_details"] = status_details
        if step_timeout_in_minutes is not None:
            input_["step_timeout_in_minutes"] = step_timeout_in_minutes
        if expected_version is not None:
            input_["expected_version"] = expected_version
        if include_job_execution_state is not None:
            input_["include_job_execution_state"] = include_job_execution_state
        if include_job_document is not None:
            input_["include_job_document"] = include_job_document
        if execution_number is not None:
            input_["execution_number"] = execution_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
