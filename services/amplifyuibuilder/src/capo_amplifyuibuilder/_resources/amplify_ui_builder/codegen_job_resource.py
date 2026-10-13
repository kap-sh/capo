from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_amplifyuibuilder._auth._signers
import capo_amplifyuibuilder._auth._sigv4
from capo_amplifyuibuilder._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.app_id
    import capo_amplifyuibuilder.types.codegen_job_summary
    import capo_amplifyuibuilder.types.get_codegen_job_request
    import capo_amplifyuibuilder.types.get_codegen_job_response
    import capo_amplifyuibuilder.types.list_codegen_jobs_limit
    import capo_amplifyuibuilder.types.list_codegen_jobs_request
    import capo_amplifyuibuilder.types.list_codegen_jobs_response
    import capo_amplifyuibuilder.types.start_codegen_job_data
    import capo_amplifyuibuilder.types.start_codegen_job_request
    import capo_amplifyuibuilder.types.start_codegen_job_response
    import capo_amplifyuibuilder.types.uuid
    from capo_amplifyuibuilder._services.amplify_ui_builder import (
        AmplifyUIBuilderClient,
        AmplifyUIBuilderClientConfig,
    )
    from capo_amplifyuibuilder._services.async_amplify_ui_builder import (
        AsyncAmplifyUIBuilderClient,
        AsyncAmplifyUIBuilderClientConfig,
    )


class CodegenJobResource:
    def __init__(self, service: AmplifyUIBuilderClient) -> None:
        self._service = service

    def create(
        self,
        app_id: "capo_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        codegen_job_to_create: "capo_amplifyuibuilder.types.start_codegen_job_data.StartCodegenJobData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse"
    ):
        """<p>Starts a code generation job for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The idempotency token used to ensure that the code generation job request completes only once.</p>
            codegen_job_to_create: <p>The code generation job resource configuration.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job.start_codegen_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartCodegenJob")
        )
        input_: capo_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "codegen_job_to_create": codegen_job_to_create,
        }
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

    def read(
        self,
        app_id: "capo_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse":
        """<p>Returns an existing code generation job.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the code generation job.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app associated with the code generation job.</p>
            id: <p>The unique ID of the code generation job.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job.get_codegen_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCodegenJob")
        )
        input_: capo_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        app_id: "capo_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_codegen_jobs_limit.ListCodegenJobsLimit"
        ] = None,
    ) -> (
        "capo_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse"
    ):
        """<p>Retrieves a list of code generation jobs for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of jobs to retrieve.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest]",
        ) -> OperationResponse[
            "capo_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs

            output, http_response = (
                capo_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs.list_codegen_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCodegenJobs")
        )
        input_: capo_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
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


class AsyncCodegenJobResource:
    def __init__(self, service: AsyncAmplifyUIBuilderClient) -> None:
        self._service = service

    async def create(
        self,
        app_id: "capo_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        codegen_job_to_create: "capo_amplifyuibuilder.types.start_codegen_job_data.StartCodegenJobData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse"
    ):
        """<p>Starts a code generation job for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The idempotency token used to ensure that the code generation job request completes only once.</p>
            codegen_job_to_create: <p>The code generation job resource configuration.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job.async_start_codegen_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartCodegenJob")
        )
        input_: capo_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "codegen_job_to_create": codegen_job_to_create,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        app_id: "capo_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse":
        """<p>Returns an existing code generation job.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the code generation job.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app associated with the code generation job.</p>
            id: <p>The unique ID of the code generation job.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job.async_get_codegen_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCodegenJob")
        )
        input_: capo_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        app_id: "capo_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_codegen_jobs_limit.ListCodegenJobsLimit"
        ] = None,
    ) -> (
        "capo_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse"
    ):
        """<p>Retrieves a list of code generation jobs for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of jobs to retrieve.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs.async_list_codegen_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCodegenJobs")
        )
        input_: capo_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
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
