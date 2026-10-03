from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_m2._auth._signers
import capo_m2._auth._sigv4
from capo_m2._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_m2.types.application_summary
    import capo_m2.types.application_version_summary
    import capo_m2.types.arn
    import capo_m2.types.auth_secrets_manager_arn
    import capo_m2.types.batch_job_definition
    import capo_m2.types.batch_job_execution_status
    import capo_m2.types.batch_job_execution_summary
    import capo_m2.types.batch_job_identifier
    import capo_m2.types.batch_job_parameters_map
    import capo_m2.types.boolean
    import capo_m2.types.cancel_batch_job_execution_request
    import capo_m2.types.cancel_batch_job_execution_response
    import capo_m2.types.client_token
    import capo_m2.types.create_application_request
    import capo_m2.types.create_application_response
    import capo_m2.types.create_data_set_export_task_request
    import capo_m2.types.create_data_set_export_task_response
    import capo_m2.types.create_data_set_import_task_request
    import capo_m2.types.create_data_set_import_task_response
    import capo_m2.types.create_deployment_request
    import capo_m2.types.create_deployment_response
    import capo_m2.types.data_set_export_config
    import capo_m2.types.data_set_export_task
    import capo_m2.types.data_set_import_config
    import capo_m2.types.data_set_import_task
    import capo_m2.types.data_set_summary
    import capo_m2.types.definition
    import capo_m2.types.delete_application_from_environment_request
    import capo_m2.types.delete_application_from_environment_response
    import capo_m2.types.delete_application_request
    import capo_m2.types.delete_application_response
    import capo_m2.types.deployment_summary
    import capo_m2.types.engine_type
    import capo_m2.types.entity_description
    import capo_m2.types.entity_name
    import capo_m2.types.entity_name_list
    import capo_m2.types.get_application_request
    import capo_m2.types.get_application_response
    import capo_m2.types.get_application_version_request
    import capo_m2.types.get_application_version_response
    import capo_m2.types.get_batch_job_execution_request
    import capo_m2.types.get_batch_job_execution_response
    import capo_m2.types.get_data_set_details_request
    import capo_m2.types.get_data_set_details_response
    import capo_m2.types.get_data_set_export_task_request
    import capo_m2.types.get_data_set_export_task_response
    import capo_m2.types.get_data_set_import_task_request
    import capo_m2.types.get_data_set_import_task_response
    import capo_m2.types.get_deployment_request
    import capo_m2.types.get_deployment_response
    import capo_m2.types.identifier
    import capo_m2.types.identifier_list
    import capo_m2.types.kms_key_id
    import capo_m2.types.list_application_versions_request
    import capo_m2.types.list_application_versions_response
    import capo_m2.types.list_applications_request
    import capo_m2.types.list_applications_response
    import capo_m2.types.list_batch_job_definitions_request
    import capo_m2.types.list_batch_job_definitions_response
    import capo_m2.types.list_batch_job_executions_request
    import capo_m2.types.list_batch_job_executions_response
    import capo_m2.types.list_batch_job_restart_points_request
    import capo_m2.types.list_batch_job_restart_points_response
    import capo_m2.types.list_data_set_export_history_request
    import capo_m2.types.list_data_set_export_history_response
    import capo_m2.types.list_data_set_import_history_request
    import capo_m2.types.list_data_set_import_history_response
    import capo_m2.types.list_data_sets_request
    import capo_m2.types.list_data_sets_response
    import capo_m2.types.list_deployments_request
    import capo_m2.types.list_deployments_response
    import capo_m2.types.max_results
    import capo_m2.types.next_token
    import capo_m2.types.start_application_request
    import capo_m2.types.start_application_response
    import capo_m2.types.start_batch_job_request
    import capo_m2.types.start_batch_job_response
    import capo_m2.types.stop_application_request
    import capo_m2.types.stop_application_response
    import capo_m2.types.string100
    import capo_m2.types.string200
    import capo_m2.types.tag_map
    import capo_m2.types.timestamp
    import capo_m2.types.update_application_request
    import capo_m2.types.update_application_response
    import capo_m2.types.version
    from capo_m2._services.async_m2 import Asyncm2Client, Asyncm2ClientConfig
    from capo_m2._services.m2 import m2Client, m2ClientConfig


class Application:
    def __init__(self, service: m2Client) -> None:
        self._service = service

    def create(
        self,
        name: "capo_m2.types.entity_name.EntityName",
        engine_type: "capo_m2.types.engine_type.EngineType",
        definition: "capo_m2.types.definition.Definition",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        description: Optional[
            "capo_m2.types.entity_description.EntityDescription"
        ] = None,
        tags: Optional["capo_m2.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
        kms_key_id: Optional[str] = None,
        role_arn: Optional["capo_m2.types.arn.Arn"] = None,
    ) -> "capo_m2.types.create_application_response.CreateApplicationResponse":
        """<p>Creates a new application with given parameters. Requires an existing runtime environment and application definition file.</p>

        Args:
            name: <p>The unique identifier of the application.</p>
            description: <p>The description of the application.</p>
            engine_type: <p>The type of the target platform for this application.</p>
            definition: <p>The application definition for this application. You can specify either inline JSON or an S3 bucket location.</p>
            tags: <p>A list of tags to apply to the application.</p>
            client_token: <p>A client token is a unique, case-sensitive string of up to 128 ASCII characters with ASCII values of 33-126 inclusive. It's generated by the client to ensure idempotent operations, allowing for safe retries without unintended side effects.</p>
            kms_key_id: <p>The identifier of a customer managed key.</p>
            role_arn: <p>The Amazon Resource Name (ARN) that identifies a role that the application uses to access Amazon Web Services resources that are not part of the application or are in a different Amazon Web Services account.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.create_application_request.CreateApplicationRequest = {
            "name": name,
            "engine_type": engine_type,
            "definition": definition,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_application_response.GetApplicationResponse":
        """<p>Describes the details of a specific application.</p>

        Args:
            application_id: <p>The identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_application_request.GetApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
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
        application_id: "capo_m2.types.identifier.Identifier",
        current_application_version: "capo_m2.types.version.Version",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        description: Optional[
            "capo_m2.types.entity_description.EntityDescription"
        ] = None,
        definition: Optional["capo_m2.types.definition.Definition"] = None,
    ) -> "capo_m2.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates an application and creates a new version.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to update.</p>
            description: <p>The description of the application to update.</p>
            current_application_version: <p>The current version of the application to update.</p>
            definition: <p>The application definition for this application. You can specify either inline JSON or an S3 bucket location.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.update_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id,
            "current_application_version": current_application_version,
        }
        if description is not None:
            input_["description"] = description
        if definition is not None:
            input_["definition"] = definition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes a specific application. You cannot delete a running application.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to delete.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.delete_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
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
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        names: Optional["capo_m2.types.entity_name_list.EntityNameList"] = None,
        environment_id: Optional["capo_m2.types.identifier.Identifier"] = None,
    ) -> "capo_m2.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists the applications associated with a specific Amazon Web Services account. You can provide the unique identifier of a specific runtime environment in a query parameter to see all applications associated with that environment.</p>

        Args:
            next_token: <p>A pagination token to control the number of applications displayed in the list.</p>
            max_results: <p>The maximum number of applications to return.</p>
            names: <p>The names of the applications.</p>
            environment_id: <p>The unique identifier of the runtime environment where the applications are deployed.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_applications

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if names is not None:
            input_["names"] = names
        if environment_id is not None:
            input_["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_batch_job_execution(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        execution_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        auth_secrets_manager_arn: Optional[
            "capo_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
        ] = None,
    ) -> "capo_m2.types.cancel_batch_job_execution_response.CancelBatchJobExecutionResponse":
        """<p>Cancels the running of a specific batch job execution.</p>

        Args:
            application_id: <p>The unique identifier of the application.</p>
            execution_id: <p>The unique identifier of the batch job execution.</p>
            auth_secrets_manager_arn: <p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for Cancel Batch Job Execution operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.cancel_batch_job_execution_request.CancelBatchJobExecutionRequest]",
        ) -> OperationResponse[
            "capo_m2.types.cancel_batch_job_execution_response.CancelBatchJobExecutionResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.cancel_batch_job_execution

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.cancel_batch_job_execution.cancel_batch_job_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.cancel_batch_job_execution_request.CancelBatchJobExecutionRequest = {
            "application_id": application_id,
            "execution_id": execution_id,
        }
        if auth_secrets_manager_arn is not None:
            input_["auth_secrets_manager_arn"] = auth_secrets_manager_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_set_export_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        export_config: "capo_m2.types.data_set_export_config.DataSetExportConfig",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
        kms_key_id: Optional["capo_m2.types.kms_key_id.KMSKeyId"] = None,
    ) -> "capo_m2.types.create_data_set_export_task_response.CreateDataSetExportTaskResponse":
        """<p>Starts a data set export task for a specific application.</p>

        Args:
            application_id: <p>The unique identifier of the application for which you want to export data sets.</p>
            export_config: <p>The data set export task configuration.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a data set export. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires.</p>
            kms_key_id: <p>The identifier of a customer managed key.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.create_data_set_export_task_request.CreateDataSetExportTaskRequest]",
        ) -> OperationResponse[
            "capo_m2.types.create_data_set_export_task_response.CreateDataSetExportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_data_set_export_task

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.create_data_set_export_task.create_data_set_export_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.create_data_set_export_task_request.CreateDataSetExportTaskRequest = {
            "application_id": application_id,
            "export_config": export_config,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_set_import_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        import_config: "capo_m2.types.data_set_import_config.DataSetImportConfig",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
    ) -> "capo_m2.types.create_data_set_import_task_response.CreateDataSetImportTaskResponse":
        """<p>Starts a data set import task for a specific application.</p>

        Args:
            application_id: <p>The unique identifier of the application for which you want to import data sets.</p>
            import_config: <p>The data set import task configuration.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a data set import. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.create_data_set_import_task_request.CreateDataSetImportTaskRequest]",
        ) -> OperationResponse[
            "capo_m2.types.create_data_set_import_task_response.CreateDataSetImportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_data_set_import_task

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.create_data_set_import_task.create_data_set_import_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.create_data_set_import_task_request.CreateDataSetImportTaskRequest = {
            "application_id": application_id,
            "import_config": import_config,
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

    def create_deployment(
        self,
        environment_id: "capo_m2.types.identifier.Identifier",
        application_id: "capo_m2.types.identifier.Identifier",
        application_version: "capo_m2.types.version.Version",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
    ) -> "capo_m2.types.create_deployment_response.CreateDeploymentResponse":
        """<p>Creates and starts a deployment to deploy an application into a runtime environment.</p>

        Args:
            environment_id: <p>The identifier of the runtime environment where you want to deploy this application.</p>
            application_id: <p>The application identifier.</p>
            application_version: <p>The version of the application to deploy.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a deployment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.create_deployment_request.CreateDeploymentRequest]",
        ) -> OperationResponse[
            "capo_m2.types.create_deployment_response.CreateDeploymentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_deployment

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.create_deployment.create_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.create_deployment_request.CreateDeploymentRequest = {
            "environment_id": environment_id,
            "application_id": application_id,
            "application_version": application_version,
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

    def delete_application_from_environment(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        environment_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.delete_application_from_environment_response.DeleteApplicationFromEnvironmentResponse":
        """<p>Deletes a specific application from the specific runtime environment where it was previously deployed. You cannot delete a runtime environment using DeleteEnvironment if any application has ever been deployed to it. This API removes the association of the application with the runtime environment so you can delete the environment smoothly.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to delete.</p>
            environment_id: <p>The unique identifier of the runtime environment where the application was previously deployed.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.delete_application_from_environment_request.DeleteApplicationFromEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_m2.types.delete_application_from_environment_response.DeleteApplicationFromEnvironmentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.delete_application_from_environment

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.delete_application_from_environment.delete_application_from_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.delete_application_from_environment_request.DeleteApplicationFromEnvironmentRequest = {
            "application_id": application_id,
            "environment_id": environment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_application_version(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        application_version: "capo_m2.types.version.Version",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_application_version_response.GetApplicationVersionResponse":
        """<p>Returns details about a specific version of a specific application.</p>

        Args:
            application_id: <p>The unique identifier of the application.</p>
            application_version: <p>The specific version of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_application_version_request.GetApplicationVersionRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_application_version_response.GetApplicationVersionResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_application_version

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_application_version.get_application_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_application_version_request.GetApplicationVersionRequest = {
            "application_id": application_id,
            "application_version": application_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_batch_job_execution(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        execution_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_batch_job_execution_response.GetBatchJobExecutionResponse":
        """<p>Gets the details of a specific batch job execution for a specific application.</p>

        Args:
            application_id: <p>The identifier of the application.</p>
            execution_id: <p>The unique identifier of the batch job execution.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_batch_job_execution_request.GetBatchJobExecutionRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_batch_job_execution_response.GetBatchJobExecutionResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_batch_job_execution

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_batch_job_execution.get_batch_job_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_batch_job_execution_request.GetBatchJobExecutionRequest = {
            "application_id": application_id,
            "execution_id": execution_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_set_details(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        data_set_name: "capo_m2.types.string200.String200",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_data_set_details_response.GetDataSetDetailsResponse":
        """<p>Gets the details of a specific data set.</p>

        Args:
            application_id: <p>The unique identifier of the application that this data set is associated with.</p>
            data_set_name: <p>The name of the data set.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.execution_timeout_exception.ExecutionTimeoutException: <p> Failed to connect to server, or didn’t receive response within expected time period.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_unavailable_exception.ServiceUnavailableException: <p>Server cannot process the request at the moment.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_data_set_details_request.GetDataSetDetailsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_data_set_details_response.GetDataSetDetailsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_data_set_details

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_data_set_details.get_data_set_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_data_set_details_request.GetDataSetDetailsRequest = {
            "application_id": application_id,
            "data_set_name": data_set_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_set_export_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        task_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_data_set_export_task_response.GetDataSetExportTaskResponse":
        """<p>Gets the status of a data set import task initiated with the <a>CreateDataSetExportTask</a> operation.</p>

        Args:
            application_id: <p>The application identifier.</p>
            task_id: <p>The task identifier returned by the <a>CreateDataSetExportTask</a> operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_data_set_export_task_request.GetDataSetExportTaskRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_data_set_export_task_response.GetDataSetExportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_data_set_export_task

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_data_set_export_task.get_data_set_export_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_data_set_export_task_request.GetDataSetExportTaskRequest = {
            "application_id": application_id,
            "task_id": task_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_set_import_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        task_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_data_set_import_task_response.GetDataSetImportTaskResponse":
        """<p>Gets the status of a data set import task initiated with the <a>CreateDataSetImportTask</a> operation.</p>

        Args:
            application_id: <p>The application identifier.</p>
            task_id: <p>The task identifier returned by the <a>CreateDataSetImportTask</a> operation. </p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_data_set_import_task_request.GetDataSetImportTaskRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_data_set_import_task_response.GetDataSetImportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_data_set_import_task

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_data_set_import_task.get_data_set_import_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_data_set_import_task_request.GetDataSetImportTaskRequest = {
            "application_id": application_id,
            "task_id": task_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployment(
        self,
        deployment_id: "capo_m2.types.identifier.Identifier",
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.get_deployment_response.GetDeploymentResponse":
        """<p>Gets details of a specific deployment with a given deployment identifier.</p>

        Args:
            deployment_id: <p>The unique identifier for the deployment.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.get_deployment_request.GetDeploymentRequest]",
        ) -> OperationResponse[
            "capo_m2.types.get_deployment_response.GetDeploymentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_deployment

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.get_deployment.get_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_deployment_request.GetDeploymentRequest = {
            "deployment_id": deployment_id,
            "application_id": application_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_application_versions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_application_versions_response.ListApplicationVersionsResponse":
        """<p>Returns a list of the application versions for a specific application.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of application versions to return.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_application_versions_request.ListApplicationVersionsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_application_versions_response.ListApplicationVersionsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_application_versions

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_application_versions.list_application_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_application_versions_request.ListApplicationVersionsRequest = {
            "application_id": application_id
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

    def list_batch_job_definitions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        prefix: Optional[str] = None,
    ) -> "capo_m2.types.list_batch_job_definitions_response.ListBatchJobDefinitionsResponse":
        """<p>Lists all the available batch job definitions based on the batch job resources uploaded during the application creation. You can use the batch job definitions in the list to start a batch job.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of batch job definitions to return.</p>
            application_id: <p>The identifier of the application.</p>
            prefix: <p>If the batch job definition is a FileBatchJobDefinition, the prefix allows you to search on the file names of FileBatchJobDefinitions.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_batch_job_definitions_request.ListBatchJobDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_batch_job_definitions_response.ListBatchJobDefinitionsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_definitions

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_definitions.list_batch_job_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_batch_job_definitions_request.ListBatchJobDefinitionsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if prefix is not None:
            input_["prefix"] = prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_batch_job_executions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        execution_ids: Optional["capo_m2.types.identifier_list.IdentifierList"] = None,
        job_name: Optional["capo_m2.types.string100.String100"] = None,
        status: Optional[
            "capo_m2.types.batch_job_execution_status.BatchJobExecutionStatus"
        ] = None,
        started_after: Optional["capo_m2.types.timestamp.Timestamp"] = None,
        started_before: Optional["capo_m2.types.timestamp.Timestamp"] = None,
    ) -> "capo_m2.types.list_batch_job_executions_response.ListBatchJobExecutionsResponse":
        """<p>Lists historical, current, and scheduled batch job executions for a specific application.</p>

        Args:
            next_token: <p>A pagination token to control the number of batch job executions displayed in the list.</p>
            max_results: <p>The maximum number of batch job executions to return.</p>
            application_id: <p>The unique identifier of the application.</p>
            execution_ids: <p>The unique identifier of each batch job execution.</p>
            job_name: <p>The name of each batch job execution.</p>
            status: <p>The status of the batch job executions.</p>
            started_after: <p>The time after which the batch job executions started.</p>
            started_before: <p>The time before the batch job executions started.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_batch_job_executions_request.ListBatchJobExecutionsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_batch_job_executions_response.ListBatchJobExecutionsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_executions

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_executions.list_batch_job_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_batch_job_executions_request.ListBatchJobExecutionsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if execution_ids is not None:
            input_["execution_ids"] = execution_ids
        if job_name is not None:
            input_["job_name"] = job_name
        if status is not None:
            input_["status"] = status
        if started_after is not None:
            input_["started_after"] = started_after
        if started_before is not None:
            input_["started_before"] = started_before

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_batch_job_restart_points(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        execution_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        auth_secrets_manager_arn: Optional[
            "capo_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
        ] = None,
    ) -> "capo_m2.types.list_batch_job_restart_points_response.ListBatchJobRestartPointsResponse":
        """<p>Lists all the job steps for a JCL file to restart a batch job. This is only applicable for Micro Focus engine with versions 8.0.6 and above.</p>

        Args:
            application_id: <p>The unique identifier of the application.</p>
            execution_id: <p>The unique identifier of the batch job execution.</p>
            auth_secrets_manager_arn: <p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for List Batch Job Restart Points operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_batch_job_restart_points_request.ListBatchJobRestartPointsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_batch_job_restart_points_response.ListBatchJobRestartPointsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_restart_points

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_restart_points.list_batch_job_restart_points(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_batch_job_restart_points_request.ListBatchJobRestartPointsRequest = {
            "application_id": application_id,
            "execution_id": execution_id,
        }
        if auth_secrets_manager_arn is not None:
            input_["auth_secrets_manager_arn"] = auth_secrets_manager_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_data_set_export_history(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_data_set_export_history_response.ListDataSetExportHistoryResponse":
        """<p>Lists the data set exports for the specified application.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_data_set_export_history_request.ListDataSetExportHistoryRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_data_set_export_history_response.ListDataSetExportHistoryResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_data_set_export_history

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_data_set_export_history.list_data_set_export_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_data_set_export_history_request.ListDataSetExportHistoryRequest = {
            "application_id": application_id
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

    def list_data_set_import_history(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_data_set_import_history_response.ListDataSetImportHistoryResponse":
        """<p>Lists the data set imports for the specified application.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_data_set_import_history_request.ListDataSetImportHistoryRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_data_set_import_history_response.ListDataSetImportHistoryResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_data_set_import_history

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_data_set_import_history.list_data_set_import_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_data_set_import_history_request.ListDataSetImportHistoryRequest = {
            "application_id": application_id
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

    def list_data_sets(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        prefix: Optional["capo_m2.types.string200.String200"] = None,
        name_filter: Optional["capo_m2.types.string200.String200"] = None,
    ) -> "capo_m2.types.list_data_sets_response.ListDataSetsResponse":
        """<p>Lists the data sets imported for a specific application. In Amazon Web Services Mainframe Modernization, data sets are associated with applications deployed on runtime environments. This is known as importing data sets. Currently, Amazon Web Services Mainframe Modernization can import data sets into catalogs using <a href="https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateDataSetImportTask.html">CreateDataSetImportTask</a>.</p>

        Args:
            application_id: <p>The unique identifier of the application for which you want to list the associated data sets.</p>
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            prefix: <p>The prefix of the data set name, which you can use to filter the list of data sets.</p>
            name_filter: <p>Filter dataset name matching the specified pattern. Can use * and % as wild cards.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.execution_timeout_exception.ExecutionTimeoutException: <p> Failed to connect to server, or didn’t receive response within expected time period.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_unavailable_exception.ServiceUnavailableException: <p>Server cannot process the request at the moment.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_data_sets_request.ListDataSetsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_data_sets_response.ListDataSetsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_data_sets

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_data_sets.list_data_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_data_sets_request.ListDataSetsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if prefix is not None:
            input_["prefix"] = prefix
        if name_filter is not None:
            input_["name_filter"] = name_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_deployments(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_deployments_response.ListDeploymentsResponse":
        """<p>Returns a list of all deployments of a specific application. A deployment is a combination of a specific application and a specific version of that application. Each deployment is mapped to a particular application version.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            application_id: <p>The application identifier.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.list_deployments_request.ListDeploymentsRequest]",
        ) -> OperationResponse[
            "capo_m2.types.list_deployments_response.ListDeploymentsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_deployments

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.list_deployments.list_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_deployments_request.ListDeploymentsRequest = {
            "application_id": application_id
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

    def start_application(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "capo_m2.types.start_application_response.StartApplicationResponse":
        """<p>Starts an application that is currently stopped.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to start.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.start_application_request.StartApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.start_application_response.StartApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.start_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.start_application.start_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.start_application_request.StartApplicationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_batch_job(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        batch_job_identifier: "capo_m2.types.batch_job_identifier.BatchJobIdentifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        job_params: Optional[
            "capo_m2.types.batch_job_parameters_map.BatchJobParametersMap"
        ] = None,
        auth_secrets_manager_arn: Optional[
            "capo_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
        ] = None,
    ) -> "capo_m2.types.start_batch_job_response.StartBatchJobResponse":
        """<p>Starts a batch job and returns the unique identifier of this execution of the batch job. The associated application must be running in order to start the batch job.</p>

        Args:
            application_id: <p>The unique identifier of the application associated with this batch job.</p>
            batch_job_identifier: <p>The unique identifier of the batch job.</p>
            job_params: <p>The collection of batch job parameters. For details about limits for keys and values, see <a href="https://www.ibm.com/docs/en/workload-automation/9.3.0?topic=zos-coding-variables-in-jcl">Coding variables in JCL</a>.</p>
            auth_secrets_manager_arn: <p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for Start Batch Job execution operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.start_batch_job_request.StartBatchJobRequest]",
        ) -> OperationResponse[
            "capo_m2.types.start_batch_job_response.StartBatchJobResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.start_batch_job

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.start_batch_job.start_batch_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.start_batch_job_request.StartBatchJobRequest = {
            "application_id": application_id,
            "batch_job_identifier": batch_job_identifier,
        }
        if job_params is not None:
            input_["job_params"] = job_params
        if auth_secrets_manager_arn is not None:
            input_["auth_secrets_manager_arn"] = auth_secrets_manager_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_application(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        force_stop: Optional["capo_m2.types.boolean.Boolean"] = None,
    ) -> "capo_m2.types.stop_application_response.StopApplicationResponse":
        """<p>Stops a running application.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to stop.</p>
            force_stop: <p>Stopping an application process can take a long time. Setting this parameter to true lets you force stop the application so you don't need to wait until the process finishes to apply another action on the application. The default value is false.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_m2.types.stop_application_request.StopApplicationRequest]",
        ) -> OperationResponse[
            "capo_m2.types.stop_application_response.StopApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.stop_application

            output, http_response = (
                capo_m2._operations.aws_supernova_control_plane_service.stop_application.stop_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.stop_application_request.StopApplicationRequest = {
            "application_id": application_id
        }
        if force_stop is not None:
            input_["force_stop"] = force_stop

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncApplication:
    def __init__(self, service: Asyncm2Client) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_m2.types.entity_name.EntityName",
        engine_type: "capo_m2.types.engine_type.EngineType",
        definition: "capo_m2.types.definition.Definition",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        description: Optional[
            "capo_m2.types.entity_description.EntityDescription"
        ] = None,
        tags: Optional["capo_m2.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
        kms_key_id: Optional[str] = None,
        role_arn: Optional["capo_m2.types.arn.Arn"] = None,
    ) -> "capo_m2.types.create_application_response.CreateApplicationResponse":
        """<p>Creates a new application with given parameters. Requires an existing runtime environment and application definition file.</p>

        Args:
            name: <p>The unique identifier of the application.</p>
            description: <p>The description of the application.</p>
            engine_type: <p>The type of the target platform for this application.</p>
            definition: <p>The application definition for this application. You can specify either inline JSON or an S3 bucket location.</p>
            tags: <p>A list of tags to apply to the application.</p>
            client_token: <p>A client token is a unique, case-sensitive string of up to 128 ASCII characters with ASCII values of 33-126 inclusive. It's generated by the client to ensure idempotent operations, allowing for safe retries without unintended side effects.</p>
            kms_key_id: <p>The identifier of a customer managed key.</p>
            role_arn: <p>The Amazon Resource Name (ARN) that identifies a role that the application uses to access Amazon Web Services resources that are not part of the application or are in a different Amazon Web Services account.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_application

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.create_application_request.CreateApplicationRequest = {
            "name": name,
            "engine_type": engine_type,
            "definition": definition,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "capo_m2.types.get_application_response.GetApplicationResponse":
        """<p>Describes the details of a specific application.</p>

        Args:
            application_id: <p>The identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.get_application_request.GetApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_application

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
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
        application_id: "capo_m2.types.identifier.Identifier",
        current_application_version: "capo_m2.types.version.Version",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        description: Optional[
            "capo_m2.types.entity_description.EntityDescription"
        ] = None,
        definition: Optional["capo_m2.types.definition.Definition"] = None,
    ) -> "capo_m2.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates an application and creates a new version.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to update.</p>
            description: <p>The description of the application to update.</p>
            current_application_version: <p>The current version of the application to update.</p>
            definition: <p>The application definition for this application. You can specify either inline JSON or an S3 bucket location.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.update_application

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id,
            "current_application_version": current_application_version,
        }
        if description is not None:
            input_["description"] = description
        if definition is not None:
            input_["definition"] = definition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "capo_m2.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes a specific application. You cannot delete a running application.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to delete.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.delete_application

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
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
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        names: Optional["capo_m2.types.entity_name_list.EntityNameList"] = None,
        environment_id: Optional["capo_m2.types.identifier.Identifier"] = None,
    ) -> "capo_m2.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists the applications associated with a specific Amazon Web Services account. You can provide the unique identifier of a specific runtime environment in a query parameter to see all applications associated with that environment.</p>

        Args:
            next_token: <p>A pagination token to control the number of applications displayed in the list.</p>
            max_results: <p>The maximum number of applications to return.</p>
            names: <p>The names of the applications.</p>
            environment_id: <p>The unique identifier of the runtime environment where the applications are deployed.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_applications

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if names is not None:
            input_["names"] = names
        if environment_id is not None:
            input_["environment_id"] = environment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_batch_job_execution(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        execution_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        auth_secrets_manager_arn: Optional[
            "capo_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
        ] = None,
    ) -> "capo_m2.types.cancel_batch_job_execution_response.CancelBatchJobExecutionResponse":
        """<p>Cancels the running of a specific batch job execution.</p>

        Args:
            application_id: <p>The unique identifier of the application.</p>
            execution_id: <p>The unique identifier of the batch job execution.</p>
            auth_secrets_manager_arn: <p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for Cancel Batch Job Execution operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.cancel_batch_job_execution_request.CancelBatchJobExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.cancel_batch_job_execution_response.CancelBatchJobExecutionResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.cancel_batch_job_execution

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.cancel_batch_job_execution.async_cancel_batch_job_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.cancel_batch_job_execution_request.CancelBatchJobExecutionRequest = {
            "application_id": application_id,
            "execution_id": execution_id,
        }
        if auth_secrets_manager_arn is not None:
            input_["auth_secrets_manager_arn"] = auth_secrets_manager_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_set_export_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        export_config: "capo_m2.types.data_set_export_config.DataSetExportConfig",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
        kms_key_id: Optional["capo_m2.types.kms_key_id.KMSKeyId"] = None,
    ) -> "capo_m2.types.create_data_set_export_task_response.CreateDataSetExportTaskResponse":
        """<p>Starts a data set export task for a specific application.</p>

        Args:
            application_id: <p>The unique identifier of the application for which you want to export data sets.</p>
            export_config: <p>The data set export task configuration.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a data set export. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires.</p>
            kms_key_id: <p>The identifier of a customer managed key.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.create_data_set_export_task_request.CreateDataSetExportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.create_data_set_export_task_response.CreateDataSetExportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_data_set_export_task

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.create_data_set_export_task.async_create_data_set_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.create_data_set_export_task_request.CreateDataSetExportTaskRequest = {
            "application_id": application_id,
            "export_config": export_config,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_set_import_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        import_config: "capo_m2.types.data_set_import_config.DataSetImportConfig",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
    ) -> "capo_m2.types.create_data_set_import_task_response.CreateDataSetImportTaskResponse":
        """<p>Starts a data set import task for a specific application.</p>

        Args:
            application_id: <p>The unique identifier of the application for which you want to import data sets.</p>
            import_config: <p>The data set import task configuration.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a data set import. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.create_data_set_import_task_request.CreateDataSetImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.create_data_set_import_task_response.CreateDataSetImportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_data_set_import_task

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.create_data_set_import_task.async_create_data_set_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.create_data_set_import_task_request.CreateDataSetImportTaskRequest = {
            "application_id": application_id,
            "import_config": import_config,
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

    async def create_deployment(
        self,
        environment_id: "capo_m2.types.identifier.Identifier",
        application_id: "capo_m2.types.identifier.Identifier",
        application_version: "capo_m2.types.version.Version",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        client_token: Optional["capo_m2.types.client_token.ClientToken"] = None,
    ) -> "capo_m2.types.create_deployment_response.CreateDeploymentResponse":
        """<p>Creates and starts a deployment to deploy an application into a runtime environment.</p>

        Args:
            environment_id: <p>The identifier of the runtime environment where you want to deploy this application.</p>
            application_id: <p>The application identifier.</p>
            application_version: <p>The version of the application to deploy.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a deployment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>One or more quotas for Amazon Web Services Mainframe Modernization exceeds the limit.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.create_deployment_request.CreateDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.create_deployment_response.CreateDeploymentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.create_deployment

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.create_deployment.async_create_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.create_deployment_request.CreateDeploymentRequest = {
            "environment_id": environment_id,
            "application_id": application_id,
            "application_version": application_version,
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

    async def delete_application_from_environment(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        environment_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "capo_m2.types.delete_application_from_environment_response.DeleteApplicationFromEnvironmentResponse":
        """<p>Deletes a specific application from the specific runtime environment where it was previously deployed. You cannot delete a runtime environment using DeleteEnvironment if any application has ever been deployed to it. This API removes the association of the application with the runtime environment so you can delete the environment smoothly.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to delete.</p>
            environment_id: <p>The unique identifier of the runtime environment where the application was previously deployed.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.delete_application_from_environment_request.DeleteApplicationFromEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.delete_application_from_environment_response.DeleteApplicationFromEnvironmentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.delete_application_from_environment

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.delete_application_from_environment.async_delete_application_from_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.delete_application_from_environment_request.DeleteApplicationFromEnvironmentRequest = {
            "application_id": application_id,
            "environment_id": environment_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_application_version(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        application_version: "capo_m2.types.version.Version",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "capo_m2.types.get_application_version_response.GetApplicationVersionResponse":
        """<p>Returns details about a specific version of a specific application.</p>

        Args:
            application_id: <p>The unique identifier of the application.</p>
            application_version: <p>The specific version of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.get_application_version_request.GetApplicationVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.get_application_version_response.GetApplicationVersionResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_application_version

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.get_application_version.async_get_application_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_application_version_request.GetApplicationVersionRequest = {
            "application_id": application_id,
            "application_version": application_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_batch_job_execution(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        execution_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "capo_m2.types.get_batch_job_execution_response.GetBatchJobExecutionResponse":
        """<p>Gets the details of a specific batch job execution for a specific application.</p>

        Args:
            application_id: <p>The identifier of the application.</p>
            execution_id: <p>The unique identifier of the batch job execution.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.get_batch_job_execution_request.GetBatchJobExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.get_batch_job_execution_response.GetBatchJobExecutionResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_batch_job_execution

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.get_batch_job_execution.async_get_batch_job_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_batch_job_execution_request.GetBatchJobExecutionRequest = {
            "application_id": application_id,
            "execution_id": execution_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_set_details(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        data_set_name: "capo_m2.types.string200.String200",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "capo_m2.types.get_data_set_details_response.GetDataSetDetailsResponse":
        """<p>Gets the details of a specific data set.</p>

        Args:
            application_id: <p>The unique identifier of the application that this data set is associated with.</p>
            data_set_name: <p>The name of the data set.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.execution_timeout_exception.ExecutionTimeoutException: <p> Failed to connect to server, or didn’t receive response within expected time period.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_unavailable_exception.ServiceUnavailableException: <p>Server cannot process the request at the moment.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.get_data_set_details_request.GetDataSetDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.get_data_set_details_response.GetDataSetDetailsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_data_set_details

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.get_data_set_details.async_get_data_set_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_data_set_details_request.GetDataSetDetailsRequest = {
            "application_id": application_id,
            "data_set_name": data_set_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_set_export_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        task_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "capo_m2.types.get_data_set_export_task_response.GetDataSetExportTaskResponse":
        """<p>Gets the status of a data set import task initiated with the <a>CreateDataSetExportTask</a> operation.</p>

        Args:
            application_id: <p>The application identifier.</p>
            task_id: <p>The task identifier returned by the <a>CreateDataSetExportTask</a> operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.get_data_set_export_task_request.GetDataSetExportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.get_data_set_export_task_response.GetDataSetExportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_data_set_export_task

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.get_data_set_export_task.async_get_data_set_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_data_set_export_task_request.GetDataSetExportTaskRequest = {
            "application_id": application_id,
            "task_id": task_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_set_import_task(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        task_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "capo_m2.types.get_data_set_import_task_response.GetDataSetImportTaskResponse":
        """<p>Gets the status of a data set import task initiated with the <a>CreateDataSetImportTask</a> operation.</p>

        Args:
            application_id: <p>The application identifier.</p>
            task_id: <p>The task identifier returned by the <a>CreateDataSetImportTask</a> operation. </p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.get_data_set_import_task_request.GetDataSetImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.get_data_set_import_task_response.GetDataSetImportTaskResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_data_set_import_task

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.get_data_set_import_task.async_get_data_set_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_data_set_import_task_request.GetDataSetImportTaskRequest = {
            "application_id": application_id,
            "task_id": task_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_deployment(
        self,
        deployment_id: "capo_m2.types.identifier.Identifier",
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "capo_m2.types.get_deployment_response.GetDeploymentResponse":
        """<p>Gets details of a specific deployment with a given deployment identifier.</p>

        Args:
            deployment_id: <p>The unique identifier for the deployment.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.get_deployment_request.GetDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.get_deployment_response.GetDeploymentResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.get_deployment

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.get_deployment.async_get_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.get_deployment_request.GetDeploymentRequest = {
            "deployment_id": deployment_id,
            "application_id": application_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_application_versions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_application_versions_response.ListApplicationVersionsResponse":
        """<p>Returns a list of the application versions for a specific application.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of application versions to return.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.list_application_versions_request.ListApplicationVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.list_application_versions_response.ListApplicationVersionsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_application_versions

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.list_application_versions.async_list_application_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_application_versions_request.ListApplicationVersionsRequest = {
            "application_id": application_id
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

    async def list_batch_job_definitions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        prefix: Optional[str] = None,
    ) -> "capo_m2.types.list_batch_job_definitions_response.ListBatchJobDefinitionsResponse":
        """<p>Lists all the available batch job definitions based on the batch job resources uploaded during the application creation. You can use the batch job definitions in the list to start a batch job.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of batch job definitions to return.</p>
            application_id: <p>The identifier of the application.</p>
            prefix: <p>If the batch job definition is a FileBatchJobDefinition, the prefix allows you to search on the file names of FileBatchJobDefinitions.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.list_batch_job_definitions_request.ListBatchJobDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.list_batch_job_definitions_response.ListBatchJobDefinitionsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_definitions

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_definitions.async_list_batch_job_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_batch_job_definitions_request.ListBatchJobDefinitionsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if prefix is not None:
            input_["prefix"] = prefix

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_batch_job_executions(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        execution_ids: Optional["capo_m2.types.identifier_list.IdentifierList"] = None,
        job_name: Optional["capo_m2.types.string100.String100"] = None,
        status: Optional[
            "capo_m2.types.batch_job_execution_status.BatchJobExecutionStatus"
        ] = None,
        started_after: Optional["capo_m2.types.timestamp.Timestamp"] = None,
        started_before: Optional["capo_m2.types.timestamp.Timestamp"] = None,
    ) -> "capo_m2.types.list_batch_job_executions_response.ListBatchJobExecutionsResponse":
        """<p>Lists historical, current, and scheduled batch job executions for a specific application.</p>

        Args:
            next_token: <p>A pagination token to control the number of batch job executions displayed in the list.</p>
            max_results: <p>The maximum number of batch job executions to return.</p>
            application_id: <p>The unique identifier of the application.</p>
            execution_ids: <p>The unique identifier of each batch job execution.</p>
            job_name: <p>The name of each batch job execution.</p>
            status: <p>The status of the batch job executions.</p>
            started_after: <p>The time after which the batch job executions started.</p>
            started_before: <p>The time before the batch job executions started.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.list_batch_job_executions_request.ListBatchJobExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.list_batch_job_executions_response.ListBatchJobExecutionsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_executions

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_executions.async_list_batch_job_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_batch_job_executions_request.ListBatchJobExecutionsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if execution_ids is not None:
            input_["execution_ids"] = execution_ids
        if job_name is not None:
            input_["job_name"] = job_name
        if status is not None:
            input_["status"] = status
        if started_after is not None:
            input_["started_after"] = started_after
        if started_before is not None:
            input_["started_before"] = started_before

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_batch_job_restart_points(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        execution_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        auth_secrets_manager_arn: Optional[
            "capo_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
        ] = None,
    ) -> "capo_m2.types.list_batch_job_restart_points_response.ListBatchJobRestartPointsResponse":
        """<p>Lists all the job steps for a JCL file to restart a batch job. This is only applicable for Micro Focus engine with versions 8.0.6 and above.</p>

        Args:
            application_id: <p>The unique identifier of the application.</p>
            execution_id: <p>The unique identifier of the batch job execution.</p>
            auth_secrets_manager_arn: <p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for List Batch Job Restart Points operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.list_batch_job_restart_points_request.ListBatchJobRestartPointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.list_batch_job_restart_points_response.ListBatchJobRestartPointsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_restart_points

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.list_batch_job_restart_points.async_list_batch_job_restart_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_batch_job_restart_points_request.ListBatchJobRestartPointsRequest = {
            "application_id": application_id,
            "execution_id": execution_id,
        }
        if auth_secrets_manager_arn is not None:
            input_["auth_secrets_manager_arn"] = auth_secrets_manager_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_set_export_history(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_data_set_export_history_response.ListDataSetExportHistoryResponse":
        """<p>Lists the data set exports for the specified application.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.list_data_set_export_history_request.ListDataSetExportHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.list_data_set_export_history_response.ListDataSetExportHistoryResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_data_set_export_history

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.list_data_set_export_history.async_list_data_set_export_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_data_set_export_history_request.ListDataSetExportHistoryRequest = {
            "application_id": application_id
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

    async def list_data_set_import_history(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_data_set_import_history_response.ListDataSetImportHistoryResponse":
        """<p>Lists the data set imports for the specified application.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            application_id: <p>The unique identifier of the application.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.list_data_set_import_history_request.ListDataSetImportHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.list_data_set_import_history_response.ListDataSetImportHistoryResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_data_set_import_history

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.list_data_set_import_history.async_list_data_set_import_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_data_set_import_history_request.ListDataSetImportHistoryRequest = {
            "application_id": application_id
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

    async def list_data_sets(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
        prefix: Optional["capo_m2.types.string200.String200"] = None,
        name_filter: Optional["capo_m2.types.string200.String200"] = None,
    ) -> "capo_m2.types.list_data_sets_response.ListDataSetsResponse":
        """<p>Lists the data sets imported for a specific application. In Amazon Web Services Mainframe Modernization, data sets are associated with applications deployed on runtime environments. This is known as importing data sets. Currently, Amazon Web Services Mainframe Modernization can import data sets into catalogs using <a href="https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateDataSetImportTask.html">CreateDataSetImportTask</a>.</p>

        Args:
            application_id: <p>The unique identifier of the application for which you want to list the associated data sets.</p>
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            prefix: <p>The prefix of the data set name, which you can use to filter the list of data sets.</p>
            name_filter: <p>Filter dataset name matching the specified pattern. Can use * and % as wild cards.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.execution_timeout_exception.ExecutionTimeoutException: <p> Failed to connect to server, or didn’t receive response within expected time period.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.service_unavailable_exception.ServiceUnavailableException: <p>Server cannot process the request at the moment.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.list_data_sets_request.ListDataSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.list_data_sets_response.ListDataSetsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_data_sets

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.list_data_sets.async_list_data_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_data_sets_request.ListDataSetsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if prefix is not None:
            input_["prefix"] = prefix
        if name_filter is not None:
            input_["name_filter"] = name_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_deployments(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        next_token: Optional["capo_m2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_m2.types.max_results.MaxResults"] = None,
    ) -> "capo_m2.types.list_deployments_response.ListDeploymentsResponse":
        """<p>Returns a list of all deployments of a specific application. A deployment is a combination of a specific application and a specific version of that application. Each deployment is mapped to a particular application version.</p>

        Args:
            next_token: <p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of objects to return.</p>
            application_id: <p>The application identifier.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.list_deployments_request.ListDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.list_deployments_response.ListDeploymentsResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.list_deployments

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.list_deployments.async_list_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.list_deployments_request.ListDeploymentsRequest = {
            "application_id": application_id
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

    async def start_application(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "capo_m2.types.start_application_response.StartApplicationResponse":
        """<p>Starts an application that is currently stopped.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to start.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.start_application_request.StartApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.start_application_response.StartApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.start_application

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.start_application.async_start_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.start_application_request.StartApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_batch_job(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        batch_job_identifier: "capo_m2.types.batch_job_identifier.BatchJobIdentifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        job_params: Optional[
            "capo_m2.types.batch_job_parameters_map.BatchJobParametersMap"
        ] = None,
        auth_secrets_manager_arn: Optional[
            "capo_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
        ] = None,
    ) -> "capo_m2.types.start_batch_job_response.StartBatchJobResponse":
        """<p>Starts a batch job and returns the unique identifier of this execution of the batch job. The associated application must be running in order to start the batch job.</p>

        Args:
            application_id: <p>The unique identifier of the application associated with this batch job.</p>
            batch_job_identifier: <p>The unique identifier of the batch job.</p>
            job_params: <p>The collection of batch job parameters. For details about limits for keys and values, see <a href="https://www.ibm.com/docs/en/workload-automation/9.3.0?topic=zos-coding-variables-in-jcl">Coding variables in JCL</a>.</p>
            auth_secrets_manager_arn: <p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for Start Batch Job execution operation.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.start_batch_job_request.StartBatchJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.start_batch_job_response.StartBatchJobResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.start_batch_job

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.start_batch_job.async_start_batch_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.start_batch_job_request.StartBatchJobRequest = {
            "application_id": application_id,
            "batch_job_identifier": batch_job_identifier,
        }
        if job_params is not None:
            input_["job_params"] = job_params
        if auth_secrets_manager_arn is not None:
            input_["auth_secrets_manager_arn"] = auth_secrets_manager_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_application(
        self,
        application_id: "capo_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        force_stop: Optional["capo_m2.types.boolean.Boolean"] = None,
    ) -> "capo_m2.types.stop_application_response.StopApplicationResponse":
        """<p>Stops a running application.</p>

        Args:
            application_id: <p>The unique identifier of the application you want to stop.</p>
            force_stop: <p>Stopping an application process can take a long time. Setting this parameter to true lets you force stop the application so you don't need to wait until the process finishes to apply another action on the application. The default value is false.</p>

        Raises:
            capo_m2.errors.access_denied_exception.AccessDeniedException: <p>The account or role doesn't have the right permissions to make the request.</p>
            capo_m2.errors.conflict_exception.ConflictException: <p>The parameters provided in the request conflict with existing resources.</p>
            capo_m2.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_m2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_m2.errors.throttling_exception.ThrottlingException: <p>The number of requests made exceeds the limit.</p>
            capo_m2.errors.validation_exception.ValidationException: <p>One or more parameters provided in the request is not valid.</p>
            capo_m2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_m2.types.stop_application_request.StopApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_m2.types.stop_application_response.StopApplicationResponse"
        ]:
            import capo_m2._operations.aws_supernova_control_plane_service.stop_application

            (
                output,
                http_response,
            ) = await capo_m2._operations.aws_supernova_control_plane_service.stop_application.async_stop_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_m2.types.stop_application_request.StopApplicationRequest = {
            "application_id": application_id
        }
        if force_stop is not None:
            input_["force_stop"] = force_stop

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
