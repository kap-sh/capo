from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_emr_serverless._auth._signers
import capo_emr_serverless._auth._sigv4
from capo_emr_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.attempt_number
    import capo_emr_serverless.types.cancel_job_run_request
    import capo_emr_serverless.types.cancel_job_run_response
    import capo_emr_serverless.types.client_token
    import capo_emr_serverless.types.configuration_overrides
    import capo_emr_serverless.types.date
    import capo_emr_serverless.types.duration
    import capo_emr_serverless.types.get_dashboard_for_job_run_request
    import capo_emr_serverless.types.get_dashboard_for_job_run_response
    import capo_emr_serverless.types.get_job_run_request
    import capo_emr_serverless.types.get_job_run_response
    import capo_emr_serverless.types.iam_role_arn
    import capo_emr_serverless.types.job_driver
    import capo_emr_serverless.types.job_run_attempt_summary
    import capo_emr_serverless.types.job_run_execution_iam_policy
    import capo_emr_serverless.types.job_run_id
    import capo_emr_serverless.types.job_run_mode
    import capo_emr_serverless.types.job_run_state_set
    import capo_emr_serverless.types.job_run_summary
    import capo_emr_serverless.types.list_job_run_attempts_request
    import capo_emr_serverless.types.list_job_run_attempts_response
    import capo_emr_serverless.types.list_job_runs_request
    import capo_emr_serverless.types.list_job_runs_response
    import capo_emr_serverless.types.next_token
    import capo_emr_serverless.types.retry_policy
    import capo_emr_serverless.types.shutdown_grace_period_in_seconds
    import capo_emr_serverless.types.start_job_run_request
    import capo_emr_serverless.types.start_job_run_response
    import capo_emr_serverless.types.string256
    import capo_emr_serverless.types.tag_map
    from capo_emr_serverless._services.async_emr_serverless import (
        AsyncEMRServerlessClient,
        AsyncEMRServerlessClientConfig,
    )
    from capo_emr_serverless._services.emr_serverless import (
        EMRServerlessClient,
        EMRServerlessClientConfig,
    )


class JobRunResource:
    def __init__(self, service: EMRServerlessClient) -> None:
        self._service = service

    def create(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        execution_role_arn: "capo_emr_serverless.types.iam_role_arn.IAMRoleArn",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        execution_iam_policy: Optional[
            "capo_emr_serverless.types.job_run_execution_iam_policy.JobRunExecutionIamPolicy"
        ] = None,
        job_driver: Optional["capo_emr_serverless.types.job_driver.JobDriver"] = None,
        configuration_overrides: Optional[
            "capo_emr_serverless.types.configuration_overrides.ConfigurationOverrides"
        ] = None,
        tags: Optional["capo_emr_serverless.types.tag_map.TagMap"] = None,
        execution_timeout_minutes: Optional[
            "capo_emr_serverless.types.duration.Duration"
        ] = None,
        name: Optional["capo_emr_serverless.types.string256.String256"] = None,
        mode: Optional["capo_emr_serverless.types.job_run_mode.JobRunMode"] = None,
        retry_policy: Optional[
            "capo_emr_serverless.types.retry_policy.RetryPolicy"
        ] = None,
    ) -> "capo_emr_serverless.types.start_job_run_response.StartJobRunResponse":
        """<p>Starts a job run.</p>

        Args:
            application_id: <p>The ID of the application on which to run the job.</p>
            client_token: <p>The client idempotency token of the job run to start. Its value must be unique for each request.</p>
            execution_role_arn: <p>The execution role ARN for the job run.</p>
            execution_iam_policy: <p>You can pass an optional IAM policy. The resulting job IAM role permissions will be an intersection of this policy and the policy associated with your job execution role.</p>
            job_driver: <p>The job driver for the job run.</p>
            configuration_overrides: <p>The configuration overrides for the job run.</p>
            tags: <p>The tags assigned to the job run.</p>
            execution_timeout_minutes: <p>The maximum duration, in minutes, for the job run. If the job run exceeds this duration, Amazon EMR Serverless cancels it automatically.</p> <p>For BATCH mode job runs, the maximum value is 10080 minutes (7 days) starting with Amazon EMR release 7.11. Setting a value of 0 to disable the timeout is no longer supported for BATCH mode job runs.</p>
            name: <p>The optional job run name. This doesn't have to be unique.</p>
            mode: <p>The mode of the job run when it starts.</p>
            retry_policy: <p>The retry policy when job run starts.</p>

        Raises:
            capo_emr_serverless.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.start_job_run_request.StartJobRunRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.start_job_run_response.StartJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.start_job_run

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.start_job_run.start_job_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.start_job_run_request.StartJobRunRequest = {
            "application_id": application_id,
            "client_token": client_token,
            "execution_role_arn": execution_role_arn,
        }
        if execution_iam_policy is not None:
            input_["execution_iam_policy"] = execution_iam_policy
        if job_driver is not None:
            input_["job_driver"] = job_driver
        if configuration_overrides is not None:
            input_["configuration_overrides"] = configuration_overrides
        if tags is not None:
            input_["tags"] = tags
        if execution_timeout_minutes is not None:
            input_["execution_timeout_minutes"] = execution_timeout_minutes
        if name is not None:
            input_["name"] = name
        if mode is not None:
            input_["mode"] = mode
        if retry_policy is not None:
            input_["retry_policy"] = retry_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        attempt: Optional[
            "capo_emr_serverless.types.attempt_number.AttemptNumber"
        ] = None,
    ) -> "capo_emr_serverless.types.get_job_run_response.GetJobRunResponse":
        """<p>Displays detailed information about a job run.</p>

        Args:
            application_id: <p>The ID of the application on which the job run is submitted.</p>
            job_run_id: <p>The ID of the job run.</p>
            attempt: <p>An optimal parameter that indicates the amount of attempts for the job. If not specified, this value defaults to the attempt of the latest job.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.get_job_run_request.GetJobRunRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.get_job_run_response.GetJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_job_run

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.get_job_run.get_job_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_job_run_request.GetJobRunRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
        if attempt is not None:
            input_["attempt"] = attempt

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        shutdown_grace_period_in_seconds: Optional[
            "capo_emr_serverless.types.shutdown_grace_period_in_seconds.ShutdownGracePeriodInSeconds"
        ] = None,
    ) -> "capo_emr_serverless.types.cancel_job_run_response.CancelJobRunResponse":
        """<p>Cancels a job run.</p>

        Args:
            application_id: <p>The ID of the application on which the job run will be canceled.</p>
            job_run_id: <p>The ID of the job run to cancel.</p>
            shutdown_grace_period_in_seconds: <p>The duration in seconds to wait before forcefully terminating the job after cancellation is requested.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.cancel_job_run_request.CancelJobRunRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.cancel_job_run_response.CancelJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.cancel_job_run

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.cancel_job_run.cancel_job_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.cancel_job_run_request.CancelJobRunRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
        if shutdown_grace_period_in_seconds is not None:
            input_["shutdown_grace_period_in_seconds"] = (
                shutdown_grace_period_in_seconds
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        created_at_after: Optional["capo_emr_serverless.types.date.Date"] = None,
        created_at_before: Optional["capo_emr_serverless.types.date.Date"] = None,
        states: Optional[
            "capo_emr_serverless.types.job_run_state_set.JobRunStateSet"
        ] = None,
        mode: Optional["capo_emr_serverless.types.job_run_mode.JobRunMode"] = None,
    ) -> "capo_emr_serverless.types.list_job_runs_response.ListJobRunsResponse":
        """<p>Lists job runs based on a set of parameters.</p>

        Args:
            application_id: <p>The ID of the application for which to list the job run.</p>
            next_token: <p>The token for the next set of job run results.</p>
            max_results: <p>The maximum number of job runs that can be listed.</p>
            created_at_after: <p>The lower bound of the option to filter by creation date and time.</p>
            created_at_before: <p>The upper bound of the option to filter by creation date and time.</p>
            states: <p>An optional filter for job run states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>
            mode: <p>The mode of the job runs to list.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.list_job_runs_request.ListJobRunsRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.list_job_runs_response.ListJobRunsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_job_runs

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.list_job_runs.list_job_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.list_job_runs_request.ListJobRunsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if created_at_after is not None:
            input_["created_at_after"] = created_at_after
        if created_at_before is not None:
            input_["created_at_before"] = created_at_before
        if states is not None:
            input_["states"] = states
        if mode is not None:
            input_["mode"] = mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_dashboard_for_job_run(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        attempt: Optional[
            "capo_emr_serverless.types.attempt_number.AttemptNumber"
        ] = None,
        access_system_profile_logs: Optional[bool] = None,
    ) -> "capo_emr_serverless.types.get_dashboard_for_job_run_response.GetDashboardForJobRunResponse":
        """<p>Creates and returns a URL that you can use to access the application UIs for a job run.</p> <p>For jobs in a running state, the application UI is a live user interface such as the Spark or Tez web UI. For completed jobs, the application UI is a persistent application user interface such as the Spark History Server or persistent Tez UI.</p> <note> <p>The URL is valid for one hour after you generate it. To access the application UI after that hour elapses, you must invoke the API again to generate a new URL.</p> </note>

        Args:
            application_id: <p>The ID of the application.</p>
            job_run_id: <p>The ID of the job run.</p>
            attempt: <p>An optimal parameter that indicates the amount of attempts for the job. If not specified, this value defaults to the attempt of the latest job.</p>
            access_system_profile_logs: <p>Allows access to system profile logs for Lake Formation-enabled jobs. Default is false.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.get_dashboard_for_job_run_request.GetDashboardForJobRunRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.get_dashboard_for_job_run_response.GetDashboardForJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_dashboard_for_job_run

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.get_dashboard_for_job_run.get_dashboard_for_job_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_dashboard_for_job_run_request.GetDashboardForJobRunRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
        if attempt is not None:
            input_["attempt"] = attempt
        if access_system_profile_logs is not None:
            input_["access_system_profile_logs"] = access_system_profile_logs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_job_run_attempts(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[EMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_emr_serverless.types.list_job_run_attempts_response.ListJobRunAttemptsResponse":
        """<p>Lists all attempt of a job run.</p>

        Args:
            application_id: <p>The ID of the application for which to list job runs.</p>
            job_run_id: <p>The ID of the job run to list.</p>
            next_token: <p>The token for the next set of job run attempt results.</p>
            max_results: <p>The maximum number of job run attempts to list.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_emr_serverless.types.list_job_run_attempts_request.ListJobRunAttemptsRequest]",
        ) -> OperationResponse[
            "capo_emr_serverless.types.list_job_run_attempts_response.ListJobRunAttemptsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_job_run_attempts

            output, http_response = (
                capo_emr_serverless._operations.aws_toledo_web_service.list_job_run_attempts.list_job_run_attempts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.list_job_run_attempts_request.ListJobRunAttemptsRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncJobRunResource:
    def __init__(self, service: AsyncEMRServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        client_token: "capo_emr_serverless.types.client_token.ClientToken",
        execution_role_arn: "capo_emr_serverless.types.iam_role_arn.IAMRoleArn",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        execution_iam_policy: Optional[
            "capo_emr_serverless.types.job_run_execution_iam_policy.JobRunExecutionIamPolicy"
        ] = None,
        job_driver: Optional["capo_emr_serverless.types.job_driver.JobDriver"] = None,
        configuration_overrides: Optional[
            "capo_emr_serverless.types.configuration_overrides.ConfigurationOverrides"
        ] = None,
        tags: Optional["capo_emr_serverless.types.tag_map.TagMap"] = None,
        execution_timeout_minutes: Optional[
            "capo_emr_serverless.types.duration.Duration"
        ] = None,
        name: Optional["capo_emr_serverless.types.string256.String256"] = None,
        mode: Optional["capo_emr_serverless.types.job_run_mode.JobRunMode"] = None,
        retry_policy: Optional[
            "capo_emr_serverless.types.retry_policy.RetryPolicy"
        ] = None,
    ) -> "capo_emr_serverless.types.start_job_run_response.StartJobRunResponse":
        """<p>Starts a job run.</p>

        Args:
            application_id: <p>The ID of the application on which to run the job.</p>
            client_token: <p>The client idempotency token of the job run to start. Its value must be unique for each request.</p>
            execution_role_arn: <p>The execution role ARN for the job run.</p>
            execution_iam_policy: <p>You can pass an optional IAM policy. The resulting job IAM role permissions will be an intersection of this policy and the policy associated with your job execution role.</p>
            job_driver: <p>The job driver for the job run.</p>
            configuration_overrides: <p>The configuration overrides for the job run.</p>
            tags: <p>The tags assigned to the job run.</p>
            execution_timeout_minutes: <p>The maximum duration, in minutes, for the job run. If the job run exceeds this duration, Amazon EMR Serverless cancels it automatically.</p> <p>For BATCH mode job runs, the maximum value is 10080 minutes (7 days) starting with Amazon EMR release 7.11. Setting a value of 0 to disable the timeout is no longer supported for BATCH mode job runs.</p>
            name: <p>The optional job run name. This doesn't have to be unique.</p>
            mode: <p>The mode of the job run when it starts.</p>
            retry_policy: <p>The retry policy when job run starts.</p>

        Raises:
            capo_emr_serverless.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.start_job_run_request.StartJobRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.start_job_run_response.StartJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.start_job_run

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.start_job_run.async_start_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.start_job_run_request.StartJobRunRequest = {
            "application_id": application_id,
            "client_token": client_token,
            "execution_role_arn": execution_role_arn,
        }
        if execution_iam_policy is not None:
            input_["execution_iam_policy"] = execution_iam_policy
        if job_driver is not None:
            input_["job_driver"] = job_driver
        if configuration_overrides is not None:
            input_["configuration_overrides"] = configuration_overrides
        if tags is not None:
            input_["tags"] = tags
        if execution_timeout_minutes is not None:
            input_["execution_timeout_minutes"] = execution_timeout_minutes
        if name is not None:
            input_["name"] = name
        if mode is not None:
            input_["mode"] = mode
        if retry_policy is not None:
            input_["retry_policy"] = retry_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        attempt: Optional[
            "capo_emr_serverless.types.attempt_number.AttemptNumber"
        ] = None,
    ) -> "capo_emr_serverless.types.get_job_run_response.GetJobRunResponse":
        """<p>Displays detailed information about a job run.</p>

        Args:
            application_id: <p>The ID of the application on which the job run is submitted.</p>
            job_run_id: <p>The ID of the job run.</p>
            attempt: <p>An optimal parameter that indicates the amount of attempts for the job. If not specified, this value defaults to the attempt of the latest job.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_job_run_request.GetJobRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_job_run_response.GetJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_job_run

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_job_run.async_get_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_job_run_request.GetJobRunRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
        if attempt is not None:
            input_["attempt"] = attempt

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        shutdown_grace_period_in_seconds: Optional[
            "capo_emr_serverless.types.shutdown_grace_period_in_seconds.ShutdownGracePeriodInSeconds"
        ] = None,
    ) -> "capo_emr_serverless.types.cancel_job_run_response.CancelJobRunResponse":
        """<p>Cancels a job run.</p>

        Args:
            application_id: <p>The ID of the application on which the job run will be canceled.</p>
            job_run_id: <p>The ID of the job run to cancel.</p>
            shutdown_grace_period_in_seconds: <p>The duration in seconds to wait before forcefully terminating the job after cancellation is requested.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.cancel_job_run_request.CancelJobRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.cancel_job_run_response.CancelJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.cancel_job_run

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.cancel_job_run.async_cancel_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.cancel_job_run_request.CancelJobRunRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
        if shutdown_grace_period_in_seconds is not None:
            input_["shutdown_grace_period_in_seconds"] = (
                shutdown_grace_period_in_seconds
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        created_at_after: Optional["capo_emr_serverless.types.date.Date"] = None,
        created_at_before: Optional["capo_emr_serverless.types.date.Date"] = None,
        states: Optional[
            "capo_emr_serverless.types.job_run_state_set.JobRunStateSet"
        ] = None,
        mode: Optional["capo_emr_serverless.types.job_run_mode.JobRunMode"] = None,
    ) -> "capo_emr_serverless.types.list_job_runs_response.ListJobRunsResponse":
        """<p>Lists job runs based on a set of parameters.</p>

        Args:
            application_id: <p>The ID of the application for which to list the job run.</p>
            next_token: <p>The token for the next set of job run results.</p>
            max_results: <p>The maximum number of job runs that can be listed.</p>
            created_at_after: <p>The lower bound of the option to filter by creation date and time.</p>
            created_at_before: <p>The upper bound of the option to filter by creation date and time.</p>
            states: <p>An optional filter for job run states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>
            mode: <p>The mode of the job runs to list.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.list_job_runs_request.ListJobRunsRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.list_job_runs_response.ListJobRunsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_job_runs

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.list_job_runs.async_list_job_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.list_job_runs_request.ListJobRunsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if created_at_after is not None:
            input_["created_at_after"] = created_at_after
        if created_at_before is not None:
            input_["created_at_before"] = created_at_before
        if states is not None:
            input_["states"] = states
        if mode is not None:
            input_["mode"] = mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_dashboard_for_job_run(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        attempt: Optional[
            "capo_emr_serverless.types.attempt_number.AttemptNumber"
        ] = None,
        access_system_profile_logs: Optional[bool] = None,
    ) -> "capo_emr_serverless.types.get_dashboard_for_job_run_response.GetDashboardForJobRunResponse":
        """<p>Creates and returns a URL that you can use to access the application UIs for a job run.</p> <p>For jobs in a running state, the application UI is a live user interface such as the Spark or Tez web UI. For completed jobs, the application UI is a persistent application user interface such as the Spark History Server or persistent Tez UI.</p> <note> <p>The URL is valid for one hour after you generate it. To access the application UI after that hour elapses, you must invoke the API again to generate a new URL.</p> </note>

        Args:
            application_id: <p>The ID of the application.</p>
            job_run_id: <p>The ID of the job run.</p>
            attempt: <p>An optimal parameter that indicates the amount of attempts for the job. If not specified, this value defaults to the attempt of the latest job.</p>
            access_system_profile_logs: <p>Allows access to system profile logs for Lake Formation-enabled jobs. Default is false.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.get_dashboard_for_job_run_request.GetDashboardForJobRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.get_dashboard_for_job_run_response.GetDashboardForJobRunResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.get_dashboard_for_job_run

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.get_dashboard_for_job_run.async_get_dashboard_for_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.get_dashboard_for_job_run_request.GetDashboardForJobRunRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
        if attempt is not None:
            input_["attempt"] = attempt
        if access_system_profile_logs is not None:
            input_["access_system_profile_logs"] = access_system_profile_logs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_job_run_attempts(
        self,
        application_id: "capo_emr_serverless.types.application_id.ApplicationId",
        job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[AsyncEMRServerlessClientConfig] = None,
        next_token: Optional["capo_emr_serverless.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_emr_serverless.types.list_job_run_attempts_response.ListJobRunAttemptsResponse":
        """<p>Lists all attempt of a job run.</p>

        Args:
            application_id: <p>The ID of the application for which to list job runs.</p>
            job_run_id: <p>The ID of the job run to list.</p>
            next_token: <p>The token for the next set of job run attempt results.</p>
            max_results: <p>The maximum number of job run attempts to list.</p>

        Raises:
            capo_emr_serverless.errors.internal_server_exception.InternalServerException: <p>Request processing failed because of an error or failure with the service.</p>
            capo_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_emr_serverless.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_emr_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_emr_serverless.types.list_job_run_attempts_request.ListJobRunAttemptsRequest]",
        ) -> AsyncOperationResponse[
            "capo_emr_serverless.types.list_job_run_attempts_response.ListJobRunAttemptsResponse"
        ]:
            import capo_emr_serverless._operations.aws_toledo_web_service.list_job_run_attempts

            (
                output,
                http_response,
            ) = await capo_emr_serverless._operations.aws_toledo_web_service.list_job_run_attempts.async_list_job_run_attempts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_emr_serverless.types.list_job_run_attempts_request.ListJobRunAttemptsRequest = {
            "application_id": application_id,
            "job_run_id": job_run_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
