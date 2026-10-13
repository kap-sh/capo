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
    import capo_bedrock_data_automation.types.blueprint_filter
    import capo_bedrock_data_automation.types.client_token
    import capo_bedrock_data_automation.types.create_data_automation_project_request
    import capo_bedrock_data_automation.types.create_data_automation_project_response
    import capo_bedrock_data_automation.types.custom_output_configuration
    import capo_bedrock_data_automation.types.data_automation_library_configuration
    import capo_bedrock_data_automation.types.data_automation_library_filter
    import capo_bedrock_data_automation.types.data_automation_project_arn
    import capo_bedrock_data_automation.types.data_automation_project_description
    import capo_bedrock_data_automation.types.data_automation_project_name
    import capo_bedrock_data_automation.types.data_automation_project_stage
    import capo_bedrock_data_automation.types.data_automation_project_stage_filter
    import capo_bedrock_data_automation.types.data_automation_project_summary
    import capo_bedrock_data_automation.types.data_automation_project_type
    import capo_bedrock_data_automation.types.delete_data_automation_project_request
    import capo_bedrock_data_automation.types.delete_data_automation_project_response
    import capo_bedrock_data_automation.types.encryption_configuration
    import capo_bedrock_data_automation.types.get_data_automation_project_request
    import capo_bedrock_data_automation.types.get_data_automation_project_response
    import capo_bedrock_data_automation.types.list_data_automation_projects_request
    import capo_bedrock_data_automation.types.list_data_automation_projects_response
    import capo_bedrock_data_automation.types.max_results
    import capo_bedrock_data_automation.types.next_token
    import capo_bedrock_data_automation.types.override_configuration
    import capo_bedrock_data_automation.types.resource_owner
    import capo_bedrock_data_automation.types.standard_output_configuration
    import capo_bedrock_data_automation.types.tag_list
    import capo_bedrock_data_automation.types.update_data_automation_project_request
    import capo_bedrock_data_automation.types.update_data_automation_project_response
    from capo_bedrock_data_automation._services.async_bedrock_data_automation import (
        AsyncBedrockDataAutomationClient,
        AsyncBedrockDataAutomationClientConfig,
    )
    from capo_bedrock_data_automation._services.bedrock_data_automation import (
        BedrockDataAutomationClient,
        BedrockDataAutomationClientConfig,
    )


class DataAutomationProjectResource:
    def __init__(self, service: BedrockDataAutomationClient) -> None:
        self._service = service

    def create(
        self,
        project_name: "capo_bedrock_data_automation.types.data_automation_project_name.DataAutomationProjectName",
        standard_output_configuration: "capo_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        project_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
        ] = None,
        project_stage: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
        project_type: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_type.DataAutomationProjectType"
        ] = None,
        custom_output_configuration: Optional[
            "capo_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        override_configuration: Optional[
            "capo_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
        ] = None,
        data_automation_library_configuration: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.create_data_automation_project_response.CreateDataAutomationProjectResponse":
        """Creates an Amazon Bedrock Data Automation Project

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
            req: "OperationRequest[capo_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.create_data_automation_project_response.CreateDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_project

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_project.create_data_automation_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.create_data_automation_project_request

            return capo_bedrock_data_automation.types.create_data_automation_project_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateDataAutomationProject", redact_input=_redact_input),
        )
        input_: capo_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest = {
            "project_name": project_name,
            "standard_output_configuration": standard_output_configuration,
        }
        if project_description is not None:
            input_["project_description"] = project_description
        if project_stage is not None:
            input_["project_stage"] = project_stage
        if project_type is not None:
            input_["project_type"] = project_type
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if override_configuration is not None:
            input_["override_configuration"] = override_configuration
        if data_automation_library_configuration is not None:
            input_["data_automation_library_configuration"] = (
                data_automation_library_configuration
            )
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
        project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        project_stage: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse":
        """Gets an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created
            project_stage: Optional field to delete a specific DataAutomationProject stage

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.get_data_automation_project_request.GetDataAutomationProjectRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_project

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_project.get_data_automation_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.get_data_automation_project_response

            return capo_bedrock_data_automation.types.get_data_automation_project_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDataAutomationProject", redact_output=_redact_output),
        )
        input_: capo_bedrock_data_automation.types.get_data_automation_project_request.GetDataAutomationProjectRequest = {
            "project_arn": project_arn
        }
        if project_stage is not None:
            input_["project_stage"] = project_stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        standard_output_configuration: "capo_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        project_stage: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
        project_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
        ] = None,
        custom_output_configuration: Optional[
            "capo_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        override_configuration: Optional[
            "capo_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
        ] = None,
        data_automation_library_configuration: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.update_data_automation_project_response.UpdateDataAutomationProjectResponse":
        """Updates an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.update_data_automation_project_response.UpdateDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_project

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_project.update_data_automation_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.update_data_automation_project_request

            return capo_bedrock_data_automation.types.update_data_automation_project_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateDataAutomationProject", redact_input=_redact_input),
        )
        input_: capo_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest = {
            "project_arn": project_arn,
            "standard_output_configuration": standard_output_configuration,
        }
        if project_stage is not None:
            input_["project_stage"] = project_stage
        if project_description is not None:
            input_["project_description"] = project_description
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if override_configuration is not None:
            input_["override_configuration"] = override_configuration
        if data_automation_library_configuration is not None:
            input_["data_automation_library_configuration"] = (
                data_automation_library_configuration
            )
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
        project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.delete_data_automation_project_response.DeleteDataAutomationProjectResponse":
        """Deletes an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.delete_data_automation_project_request.DeleteDataAutomationProjectRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.delete_data_automation_project_response.DeleteDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_project

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_project.delete_data_automation_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDataAutomationProject")
        )
        input_: capo_bedrock_data_automation.types.delete_data_automation_project_request.DeleteDataAutomationProjectRequest = {
            "project_arn": project_arn
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
        project_stage_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage_filter.DataAutomationProjectStageFilter"
        ] = None,
        blueprint_filter: Optional[
            "capo_bedrock_data_automation.types.blueprint_filter.BlueprintFilter"
        ] = None,
        resource_owner: Optional[
            "capo_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        library_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_filter.DataAutomationLibraryFilter"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse":
        """Lists all existing Amazon Bedrock Data Automation Projects

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.list_data_automation_projects_request.ListDataAutomationProjectsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_projects

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_projects.list_data_automation_projects(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.list_data_automation_projects_response

            return capo_bedrock_data_automation.types.list_data_automation_projects_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListDataAutomationProjects", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_data_automation.types.list_data_automation_projects_request.ListDataAutomationProjectsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_stage_filter is not None:
            input_["project_stage_filter"] = project_stage_filter
        if blueprint_filter is not None:
            input_["blueprint_filter"] = blueprint_filter
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if library_filter is not None:
            input_["library_filter"] = library_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDataAutomationProjectResource:
    def __init__(self, service: AsyncBedrockDataAutomationClient) -> None:
        self._service = service

    async def create(
        self,
        project_name: "capo_bedrock_data_automation.types.data_automation_project_name.DataAutomationProjectName",
        standard_output_configuration: "capo_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        project_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
        ] = None,
        project_stage: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
        project_type: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_type.DataAutomationProjectType"
        ] = None,
        custom_output_configuration: Optional[
            "capo_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        override_configuration: Optional[
            "capo_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
        ] = None,
        data_automation_library_configuration: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.create_data_automation_project_response.CreateDataAutomationProjectResponse":
        """Creates an Amazon Bedrock Data Automation Project

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
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.create_data_automation_project_response.CreateDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_project

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_project.async_create_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.create_data_automation_project_request

            return capo_bedrock_data_automation.types.create_data_automation_project_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateDataAutomationProject", redact_input=_redact_input),
        )
        input_: capo_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest = {
            "project_name": project_name,
            "standard_output_configuration": standard_output_configuration,
        }
        if project_description is not None:
            input_["project_description"] = project_description
        if project_stage is not None:
            input_["project_stage"] = project_stage
        if project_type is not None:
            input_["project_type"] = project_type
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if override_configuration is not None:
            input_["override_configuration"] = override_configuration
        if data_automation_library_configuration is not None:
            input_["data_automation_library_configuration"] = (
                data_automation_library_configuration
            )
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
        project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        project_stage: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse":
        """Gets an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created
            project_stage: Optional field to delete a specific DataAutomationProject stage

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_data_automation_project_request.GetDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_project

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_project.async_get_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.get_data_automation_project_response

            return capo_bedrock_data_automation.types.get_data_automation_project_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDataAutomationProject", redact_output=_redact_output),
        )
        input_: capo_bedrock_data_automation.types.get_data_automation_project_request.GetDataAutomationProjectRequest = {
            "project_arn": project_arn
        }
        if project_stage is not None:
            input_["project_stage"] = project_stage

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        standard_output_configuration: "capo_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        project_stage: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
        project_description: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
        ] = None,
        custom_output_configuration: Optional[
            "capo_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        override_configuration: Optional[
            "capo_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
        ] = None,
        data_automation_library_configuration: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.update_data_automation_project_response.UpdateDataAutomationProjectResponse":
        """Updates an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.update_data_automation_project_response.UpdateDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_project

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_project.async_update_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.update_data_automation_project_request

            return capo_bedrock_data_automation.types.update_data_automation_project_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateDataAutomationProject", redact_input=_redact_input),
        )
        input_: capo_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest = {
            "project_arn": project_arn,
            "standard_output_configuration": standard_output_configuration,
        }
        if project_stage is not None:
            input_["project_stage"] = project_stage
        if project_description is not None:
            input_["project_description"] = project_description
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if override_configuration is not None:
            input_["override_configuration"] = override_configuration
        if data_automation_library_configuration is not None:
            input_["data_automation_library_configuration"] = (
                data_automation_library_configuration
            )
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
        project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.delete_data_automation_project_response.DeleteDataAutomationProjectResponse":
        """Deletes an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.delete_data_automation_project_request.DeleteDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.delete_data_automation_project_response.DeleteDataAutomationProjectResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_project

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_project.async_delete_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDataAutomationProject")
        )
        input_: capo_bedrock_data_automation.types.delete_data_automation_project_request.DeleteDataAutomationProjectRequest = {
            "project_arn": project_arn
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
        project_stage_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_project_stage_filter.DataAutomationProjectStageFilter"
        ] = None,
        blueprint_filter: Optional[
            "capo_bedrock_data_automation.types.blueprint_filter.BlueprintFilter"
        ] = None,
        resource_owner: Optional[
            "capo_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        library_filter: Optional[
            "capo_bedrock_data_automation.types.data_automation_library_filter.DataAutomationLibraryFilter"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse":
        """Lists all existing Amazon Bedrock Data Automation Projects

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_data_automation_projects_request.ListDataAutomationProjectsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_projects

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_projects.async_list_data_automation_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.list_data_automation_projects_response

            return capo_bedrock_data_automation.types.list_data_automation_projects_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListDataAutomationProjects", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_data_automation.types.list_data_automation_projects_request.ListDataAutomationProjectsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_stage_filter is not None:
            input_["project_stage_filter"] = project_stage_filter
        if blueprint_filter is not None:
            input_["blueprint_filter"] = blueprint_filter
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if library_filter is not None:
            input_["library_filter"] = library_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
