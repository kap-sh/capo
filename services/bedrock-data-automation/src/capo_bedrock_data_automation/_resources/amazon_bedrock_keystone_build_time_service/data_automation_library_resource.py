from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_data_automation._auth._signers
import capo_bedrock_data_automation._auth._sigv4
from capo_bedrock_data_automation._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.client_token
    import capo_bedrock_data_automation.types.create_data_automation_library_request
    import capo_bedrock_data_automation.types.create_data_automation_library_response
    import capo_bedrock_data_automation.types.data_automation_library_arn
    import capo_bedrock_data_automation.types.data_automation_library_description
    import capo_bedrock_data_automation.types.data_automation_library_name
    import capo_bedrock_data_automation.types.data_automation_library_summary
    import capo_bedrock_data_automation.types.data_automation_project_filter
    import capo_bedrock_data_automation.types.delete_data_automation_library_request
    import capo_bedrock_data_automation.types.delete_data_automation_library_response
    import capo_bedrock_data_automation.types.encryption_configuration
    import capo_bedrock_data_automation.types.get_data_automation_library_request
    import capo_bedrock_data_automation.types.get_data_automation_library_response
    import capo_bedrock_data_automation.types.list_data_automation_libraries_request
    import capo_bedrock_data_automation.types.list_data_automation_libraries_response
    import capo_bedrock_data_automation.types.max_results
    import capo_bedrock_data_automation.types.next_token
    import capo_bedrock_data_automation.types.tag_list
    import capo_bedrock_data_automation.types.update_data_automation_library_request
    import capo_bedrock_data_automation.types.update_data_automation_library_response
    from capo_bedrock_data_automation._services.async_bedrock_data_automation import (
        AsyncBedrockDataAutomationClient,
        AsyncBedrockDataAutomationClientConfig,
    )
    from capo_bedrock_data_automation._services.bedrock_data_automation import (
        BedrockDataAutomationClient,
        BedrockDataAutomationClientConfig,
    )


class DataAutomationLibraryResource:
    def __init__(self, service: BedrockDataAutomationClient) -> None:
        self._service = service

    def create(
        self,
        library_name: "capo_bedrock_data_automation.types.data_automation_library_name.DataAutomationLibraryName",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        library_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.create_data_automation_library_response.CreateDataAutomationLibraryResponse":
        """Creates an Amazon Bedrock Data Automation Library

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.create_data_automation_library_response.CreateDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_library

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_library.create_data_automation_library(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.create_data_automation_library_request

            return capo_bedrock_data_automation.types.create_data_automation_library_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateDataAutomationLibrary", redact_input=_redact_input),
        )
        input_: capo_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest = {
            "library_name": library_name
        }
        if library_description is not None:
            input_["library_description"] = library_description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse":
        """Gets an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.get_data_automation_library_request.GetDataAutomationLibraryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library.get_data_automation_library(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.get_data_automation_library_response

            return capo_bedrock_data_automation.types.get_data_automation_library_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDataAutomationLibrary", redact_output=_redact_output),
        )
        input_: capo_bedrock_data_automation.types.get_data_automation_library_request.GetDataAutomationLibraryRequest = {
            "library_arn": library_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        library_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.update_data_automation_library_response.UpdateDataAutomationLibraryResponse":
        """Updates an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.update_data_automation_library_response.UpdateDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_library

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_library.update_data_automation_library(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.update_data_automation_library_request

            return capo_bedrock_data_automation.types.update_data_automation_library_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateDataAutomationLibrary", redact_input=_redact_input),
        )
        input_: capo_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest = {
            "library_arn": library_arn
        }
        if library_description is not None:
            input_["library_description"] = library_description
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

    def delete(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.delete_data_automation_library_response.DeleteDataAutomationLibraryResponse":
        """Deletes an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.delete_data_automation_library_request.DeleteDataAutomationLibraryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.delete_data_automation_library_response.DeleteDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_library

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_library.delete_data_automation_library(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDataAutomationLibrary")
        )
        input_: capo_bedrock_data_automation.types.delete_data_automation_library_request.DeleteDataAutomationLibraryRequest = {
            "library_arn": library_arn
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
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse":
        """Lists all existing Amazon Bedrock Data Automation Libraries

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.list_data_automation_libraries_request.ListDataAutomationLibrariesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_libraries

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_libraries.list_data_automation_libraries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.list_data_automation_libraries_response

            return capo_bedrock_data_automation.types.list_data_automation_libraries_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListDataAutomationLibraries", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_data_automation.types.list_data_automation_libraries_request.ListDataAutomationLibrariesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_filter is not None:
            input_["project_filter"] = project_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDataAutomationLibraryResource:
    def __init__(self, service: AsyncBedrockDataAutomationClient) -> None:
        self._service = service

    async def create(
        self,
        library_name: "capo_bedrock_data_automation.types.data_automation_library_name.DataAutomationLibraryName",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        library_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.create_data_automation_library_response.CreateDataAutomationLibraryResponse":
        """Creates an Amazon Bedrock Data Automation Library

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.create_data_automation_library_response.CreateDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_library

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_library.async_create_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.create_data_automation_library_request

            return capo_bedrock_data_automation.types.create_data_automation_library_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateDataAutomationLibrary", redact_input=_redact_input),
        )
        input_: capo_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest = {
            "library_name": library_name
        }
        if library_description is not None:
            input_["library_description"] = library_description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse":
        """Gets an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_data_automation_library_request.GetDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library.async_get_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.get_data_automation_library_response

            return capo_bedrock_data_automation.types.get_data_automation_library_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDataAutomationLibrary", redact_output=_redact_output),
        )
        input_: capo_bedrock_data_automation.types.get_data_automation_library_request.GetDataAutomationLibraryRequest = {
            "library_arn": library_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        library_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.update_data_automation_library_response.UpdateDataAutomationLibraryResponse":
        """Updates an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.update_data_automation_library_response.UpdateDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_library

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_library.async_update_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.update_data_automation_library_request

            return capo_bedrock_data_automation.types.update_data_automation_library_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateDataAutomationLibrary", redact_input=_redact_input),
        )
        input_: capo_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest = {
            "library_arn": library_arn
        }
        if library_description is not None:
            input_["library_description"] = library_description
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

    async def delete(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.delete_data_automation_library_response.DeleteDataAutomationLibraryResponse":
        """Deletes an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.delete_data_automation_library_request.DeleteDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.delete_data_automation_library_response.DeleteDataAutomationLibraryResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_library

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_library.async_delete_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDataAutomationLibrary")
        )
        input_: capo_bedrock_data_automation.types.delete_data_automation_library_request.DeleteDataAutomationLibraryRequest = {
            "library_arn": library_arn
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
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse":
        """Lists all existing Amazon Bedrock Data Automation Libraries

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_data_automation_libraries_request.ListDataAutomationLibrariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_libraries

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_libraries.async_list_data_automation_libraries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.list_data_automation_libraries_response

            return capo_bedrock_data_automation.types.list_data_automation_libraries_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListDataAutomationLibraries", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_data_automation.types.list_data_automation_libraries_request.ListDataAutomationLibrariesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_filter is not None:
            input_["project_filter"] = project_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
