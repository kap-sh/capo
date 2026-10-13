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
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.blueprint_name
    import capo_bedrock_data_automation.types.blueprint_schema
    import capo_bedrock_data_automation.types.blueprint_stage
    import capo_bedrock_data_automation.types.blueprint_stage_filter
    import capo_bedrock_data_automation.types.blueprint_summary
    import capo_bedrock_data_automation.types.blueprint_version
    import capo_bedrock_data_automation.types.client_token
    import capo_bedrock_data_automation.types.create_blueprint_request
    import capo_bedrock_data_automation.types.create_blueprint_response
    import capo_bedrock_data_automation.types.data_automation_project_filter
    import capo_bedrock_data_automation.types.delete_blueprint_request
    import capo_bedrock_data_automation.types.delete_blueprint_response
    import capo_bedrock_data_automation.types.encryption_configuration
    import capo_bedrock_data_automation.types.get_blueprint_request
    import capo_bedrock_data_automation.types.get_blueprint_response
    import capo_bedrock_data_automation.types.list_blueprints_request
    import capo_bedrock_data_automation.types.list_blueprints_response
    import capo_bedrock_data_automation.types.max_results
    import capo_bedrock_data_automation.types.next_token
    import capo_bedrock_data_automation.types.resource_owner
    import capo_bedrock_data_automation.types.tag_list
    import capo_bedrock_data_automation.types.type
    import capo_bedrock_data_automation.types.update_blueprint_request
    import capo_bedrock_data_automation.types.update_blueprint_response
    from capo_bedrock_data_automation._services.async_bedrock_data_automation import (
        AsyncBedrockDataAutomationClient,
        AsyncBedrockDataAutomationClientConfig,
    )
    from capo_bedrock_data_automation._services.bedrock_data_automation import (
        BedrockDataAutomationClient,
        BedrockDataAutomationClientConfig,
    )


class BlueprintResource:
    def __init__(self, service: BedrockDataAutomationClient) -> None:
        self._service = service

    def create(
        self,
        blueprint_name: "capo_bedrock_data_automation.types.blueprint_name.BlueprintName",
        type: "capo_bedrock_data_automation.types.type.Type",
        schema: "capo_bedrock_data_automation.types.blueprint_schema.BlueprintSchema",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        blueprint_stage: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse":
        """Creates an Amazon Bedrock Data Automation Blueprint

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
            req: "OperationRequest[capo_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint.create_blueprint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.create_blueprint_request

            return capo_bedrock_data_automation.types.create_blueprint_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.create_blueprint_response

            return capo_bedrock_data_automation.types.create_blueprint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateBlueprint",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest = {
            "blueprint_name": blueprint_name,
            "type": type,
            "schema": schema,
        }
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage
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
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        blueprint_version: Optional[
            "capo_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
        ] = None,
        blueprint_stage: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
    ) -> (
        "capo_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse"
    ):
        """Gets an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created
            blueprint_version: Optional field to get a specific Blueprint version
            blueprint_stage: Optional field to get a specific Blueprint stage

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.get_blueprint_request.GetBlueprintRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint.get_blueprint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.get_blueprint_response

            return capo_bedrock_data_automation.types.get_blueprint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetBlueprint", redact_output=_redact_output),
        )
        input_: capo_bedrock_data_automation.types.get_blueprint_request.GetBlueprintRequest = {
            "blueprint_arn": blueprint_arn
        }
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        schema: "capo_bedrock_data_automation.types.blueprint_schema.BlueprintSchema",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        blueprint_stage: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse":
        """Updates an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created

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
            req: "OperationRequest[capo_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_blueprint

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_blueprint.update_blueprint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.update_blueprint_request

            return capo_bedrock_data_automation.types.update_blueprint_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.update_blueprint_response

            return capo_bedrock_data_automation.types.update_blueprint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateBlueprint",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest = {
            "blueprint_arn": blueprint_arn,
            "schema": schema,
        }
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        blueprint_version: Optional[
            "capo_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.delete_blueprint_response.DeleteBlueprintResponse":
        """Deletes an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created
            blueprint_version: Optional field to delete a specific Blueprint version

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.delete_blueprint_request.DeleteBlueprintRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.delete_blueprint_response.DeleteBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_blueprint

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_blueprint.delete_blueprint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBlueprint")
        )
        input_: capo_bedrock_data_automation.types.delete_blueprint_request.DeleteBlueprintRequest = {
            "blueprint_arn": blueprint_arn
        }
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version

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
        blueprint_arn: Optional[
            "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
        ] = None,
        resource_owner: Optional[
            "capo_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        blueprint_stage_filter: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage_filter.BlueprintStageFilter"
        ] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse":
        """Lists all existing Amazon Bedrock Data Automation Blueprints

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.list_blueprints_request.ListBlueprintsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_blueprints

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_blueprints.list_blueprints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.list_blueprints_response

            return capo_bedrock_data_automation.types.list_blueprints_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListBlueprints", redact_output=_redact_output),
        )
        input_: capo_bedrock_data_automation.types.list_blueprints_request.ListBlueprintsRequest = {}
        if blueprint_arn is not None:
            input_["blueprint_arn"] = blueprint_arn
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if blueprint_stage_filter is not None:
            input_["blueprint_stage_filter"] = blueprint_stage_filter
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


class AsyncBlueprintResource:
    def __init__(self, service: AsyncBedrockDataAutomationClient) -> None:
        self._service = service

    async def create(
        self,
        blueprint_name: "capo_bedrock_data_automation.types.blueprint_name.BlueprintName",
        type: "capo_bedrock_data_automation.types.type.Type",
        schema: "capo_bedrock_data_automation.types.blueprint_schema.BlueprintSchema",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_stage: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse":
        """Creates an Amazon Bedrock Data Automation Blueprint

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
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint.async_create_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.create_blueprint_request

            return capo_bedrock_data_automation.types.create_blueprint_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.create_blueprint_response

            return capo_bedrock_data_automation.types.create_blueprint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateBlueprint",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest = {
            "blueprint_name": blueprint_name,
            "type": type,
            "schema": schema,
        }
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage
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
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_version: Optional[
            "capo_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
        ] = None,
        blueprint_stage: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
    ) -> (
        "capo_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse"
    ):
        """Gets an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created
            blueprint_version: Optional field to get a specific Blueprint version
            blueprint_stage: Optional field to get a specific Blueprint stage

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_blueprint_request.GetBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint.async_get_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.get_blueprint_response

            return capo_bedrock_data_automation.types.get_blueprint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetBlueprint", redact_output=_redact_output),
        )
        input_: capo_bedrock_data_automation.types.get_blueprint_request.GetBlueprintRequest = {
            "blueprint_arn": blueprint_arn
        }
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        schema: "capo_bedrock_data_automation.types.blueprint_schema.BlueprintSchema",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_stage: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse":
        """Updates an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created

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
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_blueprint

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_blueprint.async_update_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.update_blueprint_request

            return capo_bedrock_data_automation.types.update_blueprint_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.update_blueprint_response

            return capo_bedrock_data_automation.types.update_blueprint_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateBlueprint",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest = {
            "blueprint_arn": blueprint_arn,
            "schema": schema,
        }
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_version: Optional[
            "capo_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.delete_blueprint_response.DeleteBlueprintResponse":
        """Deletes an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created
            blueprint_version: Optional field to delete a specific Blueprint version

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.delete_blueprint_request.DeleteBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.delete_blueprint_response.DeleteBlueprintResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_blueprint

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_blueprint.async_delete_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBlueprint")
        )
        input_: capo_bedrock_data_automation.types.delete_blueprint_request.DeleteBlueprintRequest = {
            "blueprint_arn": blueprint_arn
        }
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version

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
        blueprint_arn: Optional[
            "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
        ] = None,
        resource_owner: Optional[
            "capo_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        blueprint_stage_filter: Optional[
            "capo_bedrock_data_automation.types.blueprint_stage_filter.BlueprintStageFilter"
        ] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse":
        """Lists all existing Amazon Bedrock Data Automation Blueprints

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_blueprints_request.ListBlueprintsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_blueprints

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_blueprints.async_list_blueprints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.list_blueprints_response

            return capo_bedrock_data_automation.types.list_blueprints_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListBlueprints", redact_output=_redact_output),
        )
        input_: capo_bedrock_data_automation.types.list_blueprints_request.ListBlueprintsRequest = {}
        if blueprint_arn is not None:
            input_["blueprint_arn"] = blueprint_arn
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if blueprint_stage_filter is not None:
            input_["blueprint_stage_filter"] = blueprint_stage_filter
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
