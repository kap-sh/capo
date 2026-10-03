from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_qconnect._auth._signers
import capo_qconnect._auth._sigv4
from capo_qconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_qconnect.types.contact_attributes
    import capo_qconnect.types.content_metadata
    import capo_qconnect.types.content_summary
    import capo_qconnect.types.content_type
    import capo_qconnect.types.create_knowledge_base_request
    import capo_qconnect.types.create_knowledge_base_response
    import capo_qconnect.types.delete_import_job_request
    import capo_qconnect.types.delete_import_job_response
    import capo_qconnect.types.delete_knowledge_base_request
    import capo_qconnect.types.delete_knowledge_base_response
    import capo_qconnect.types.description
    import capo_qconnect.types.external_source_configuration
    import capo_qconnect.types.get_import_job_request
    import capo_qconnect.types.get_import_job_response
    import capo_qconnect.types.get_knowledge_base_request
    import capo_qconnect.types.get_knowledge_base_response
    import capo_qconnect.types.import_job_summary
    import capo_qconnect.types.import_job_type
    import capo_qconnect.types.knowledge_base_summary
    import capo_qconnect.types.knowledge_base_type
    import capo_qconnect.types.list_import_jobs_request
    import capo_qconnect.types.list_import_jobs_response
    import capo_qconnect.types.list_knowledge_bases_request
    import capo_qconnect.types.list_knowledge_bases_response
    import capo_qconnect.types.max_results
    import capo_qconnect.types.message_template_search_expression
    import capo_qconnect.types.message_template_search_result_data
    import capo_qconnect.types.name
    import capo_qconnect.types.next_token
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.quick_response_search_expression
    import capo_qconnect.types.quick_response_search_result_data
    import capo_qconnect.types.remove_knowledge_base_template_uri_request
    import capo_qconnect.types.remove_knowledge_base_template_uri_response
    import capo_qconnect.types.rendering_configuration
    import capo_qconnect.types.search_content_request
    import capo_qconnect.types.search_content_response
    import capo_qconnect.types.search_expression
    import capo_qconnect.types.search_message_templates_request
    import capo_qconnect.types.search_message_templates_response
    import capo_qconnect.types.search_quick_responses_request
    import capo_qconnect.types.search_quick_responses_response
    import capo_qconnect.types.server_side_encryption_configuration
    import capo_qconnect.types.source_configuration
    import capo_qconnect.types.start_content_upload_request
    import capo_qconnect.types.start_content_upload_response
    import capo_qconnect.types.start_import_job_request
    import capo_qconnect.types.start_import_job_response
    import capo_qconnect.types.tags
    import capo_qconnect.types.time_to_live
    import capo_qconnect.types.update_knowledge_base_template_uri_request
    import capo_qconnect.types.update_knowledge_base_template_uri_response
    import capo_qconnect.types.upload_id
    import capo_qconnect.types.uri
    import capo_qconnect.types.uuid
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.vector_ingestion_configuration
    from capo_qconnect._services.async_q_connect import (
        AsyncQConnectClient,
        AsyncQConnectClientConfig,
    )
    from capo_qconnect._services.q_connect import QConnectClient, QConnectClientConfig


class KnowledgeBase:
    def __init__(self, service: QConnectClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_qconnect.types.name.Name",
        knowledge_base_type: "capo_qconnect.types.knowledge_base_type.KnowledgeBaseType",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        client_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        source_configuration: Optional[
            "capo_qconnect.types.source_configuration.SourceConfiguration"
        ] = None,
        rendering_configuration: Optional[
            "capo_qconnect.types.rendering_configuration.RenderingConfiguration"
        ] = None,
        vector_ingestion_configuration: Optional[
            "capo_qconnect.types.vector_ingestion_configuration.VectorIngestionConfiguration"
        ] = None,
        server_side_encryption_configuration: Optional[
            "capo_qconnect.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
    ) -> (
        "capo_qconnect.types.create_knowledge_base_response.CreateKnowledgeBaseResponse"
    ):
        """<p>Creates a knowledge base.</p> <note> <p>When using this API, you cannot reuse <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html">Amazon AppIntegrations</a> DataIntegrations with external knowledge bases such as Salesforce and ServiceNow. If you do, you'll get an <code>InvalidRequestException</code> error. </p> <p>For example, you're programmatically managing your external knowledge base, and you want to add or remove one of the fields that is being ingested from Salesforce. Do the following:</p> <ol> <li> <p>Call <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_DeleteKnowledgeBase.html">DeleteKnowledgeBase</a>.</p> </li> <li> <p>Call <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html">DeleteDataIntegration</a>.</p> </li> <li> <p>Call <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> to recreate the DataIntegration or a create different one.</p> </li> <li> <p>Call CreateKnowledgeBase.</p> </li> </ol> </note>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the knowledge base.</p>
            knowledge_base_type: <p>The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically. </p>
            source_configuration: <p>The source of the knowledge base content. Only set this argument for EXTERNAL or Managed knowledge bases.</p>
            rendering_configuration: <p>Information about how to render the content.</p>
            vector_ingestion_configuration: <p>Contains details about how to ingest the documents in a data source.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, <code>kms:Decrypt</code>, and <code>kms:GenerateDataKey*</code> permissions to the IAM identity using the key to invoke Amazon Q in Connect.</p> <p>For more information about setting up a customer managed key for Amazon Q in Connect, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html">Enable Amazon Q in Connect for your instance</a>.</p>
            description: <p>The description.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.create_knowledge_base_request.CreateKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.create_knowledge_base_response.CreateKnowledgeBaseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_knowledge_base

            output, http_response = (
                capo_qconnect._operations.wisdom_service.create_knowledge_base.create_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.create_knowledge_base_request.CreateKnowledgeBaseRequest = {
            "name": name,
            "knowledge_base_type": knowledge_base_type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if source_configuration is not None:
            input_["source_configuration"] = source_configuration
        if rendering_configuration is not None:
            input_["rendering_configuration"] = rendering_configuration
        if vector_ingestion_configuration is not None:
            input_["vector_ingestion_configuration"] = vector_ingestion_configuration
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )
        if description is not None:
            input_["description"] = description
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
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_knowledge_base_response.GetKnowledgeBaseResponse":
        """<p>Retrieves information about the knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.get_knowledge_base_request.GetKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.get_knowledge_base_response.GetKnowledgeBaseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_knowledge_base

            output, http_response = (
                capo_qconnect._operations.wisdom_service.get_knowledge_base.get_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.get_knowledge_base_request.GetKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
    ) -> (
        "capo_qconnect.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse"
    ):
        """<p>Deletes the knowledge base.</p> <note> <p>When you use this API to delete an external knowledge base such as Salesforce or ServiceNow, you must also delete the <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html">Amazon AppIntegrations</a> DataIntegration. This is because you can't reuse the DataIntegration after it's been associated with an external knowledge base. However, you can delete and recreate it. See <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html">DeleteDataIntegration</a> and <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> in the <i>Amazon AppIntegrations API Reference</i>.</p> </note>

        Args:
            knowledge_base_id: <p>The knowledge base to delete content from. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_knowledge_base

            output, http_response = (
                capo_qconnect._operations.wisdom_service.delete_knowledge_base.delete_knowledge_base(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
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
        config_overrides: Optional[QConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_knowledge_bases_response.ListKnowledgeBasesResponse":
        """<p>Lists the knowledge bases.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.list_knowledge_bases_request.ListKnowledgeBasesRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.list_knowledge_bases_response.ListKnowledgeBasesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_knowledge_bases

            output, http_response = (
                capo_qconnect._operations.wisdom_service.list_knowledge_bases.list_knowledge_bases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.list_knowledge_bases_request.ListKnowledgeBasesRequest = {}
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

    def delete_import_job(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        import_job_id: "capo_qconnect.types.uuid.Uuid",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_import_job_response.DeleteImportJobResponse":
        """<p>Deletes the quick response import job.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base.</p>
            import_job_id: <p>The identifier of the import job to be deleted.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.delete_import_job_request.DeleteImportJobRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.delete_import_job_response.DeleteImportJobResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_import_job

            output, http_response = (
                capo_qconnect._operations.wisdom_service.delete_import_job.delete_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_import_job_request.DeleteImportJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "import_job_id": import_job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_import_job(
        self,
        import_job_id: "capo_qconnect.types.uuid.Uuid",
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_import_job_response.GetImportJobResponse":
        """<p>Retrieves the started import job.</p>

        Args:
            import_job_id: <p>The identifier of the import job to retrieve.</p>
            knowledge_base_id: <p>The identifier of the knowledge base that the import job belongs to.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.get_import_job_request.GetImportJobRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.get_import_job_response.GetImportJobResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_import_job

            output, http_response = (
                capo_qconnect._operations.wisdom_service.get_import_job.get_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.get_import_job_request.GetImportJobRequest = {
            "import_job_id": import_job_id,
            "knowledge_base_id": knowledge_base_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_import_jobs(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_import_jobs_response.ListImportJobsResponse":
        """<p>Lists information about import jobs.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.list_import_jobs_request.ListImportJobsRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.list_import_jobs_response.ListImportJobsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_import_jobs

            output, http_response = (
                capo_qconnect._operations.wisdom_service.list_import_jobs.list_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.list_import_jobs_request.ListImportJobsRequest = {
            "knowledge_base_id": knowledge_base_id
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

    def remove_knowledge_base_template_uri(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
    ) -> "capo_qconnect.types.remove_knowledge_base_template_uri_response.RemoveKnowledgeBaseTemplateUriResponse":
        """<p>Removes a URI template from a knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.remove_knowledge_base_template_uri_request.RemoveKnowledgeBaseTemplateUriRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.remove_knowledge_base_template_uri_response.RemoveKnowledgeBaseTemplateUriResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.remove_knowledge_base_template_uri

            output, http_response = (
                capo_qconnect._operations.wisdom_service.remove_knowledge_base_template_uri.remove_knowledge_base_template_uri(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.remove_knowledge_base_template_uri_request.RemoveKnowledgeBaseTemplateUriRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_content(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.search_content_response.SearchContentResponse":
        """<p>Searches for content in a specified knowledge base. Can be used to get a specific content resource by its name.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.search_content_request.SearchContentRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.search_content_response.SearchContentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_content

            output, http_response = (
                capo_qconnect._operations.wisdom_service.search_content.search_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.search_content_request.SearchContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "search_expression": search_expression,
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

    def search_message_templates(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.message_template_search_expression.MessageTemplateSearchExpression",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.search_message_templates_response.SearchMessageTemplatesResponse":
        """<p>Searches for Amazon Q in Connect message templates in the specified knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression for querying the message template.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.search_message_templates_request.SearchMessageTemplatesRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.search_message_templates_response.SearchMessageTemplatesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_message_templates

            output, http_response = (
                capo_qconnect._operations.wisdom_service.search_message_templates.search_message_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.search_message_templates_request.SearchMessageTemplatesRequest = {
            "knowledge_base_id": knowledge_base_id,
            "search_expression": search_expression,
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

    def search_quick_responses(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.quick_response_search_expression.QuickResponseSearchExpression",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        attributes: Optional[
            "capo_qconnect.types.contact_attributes.ContactAttributes"
        ] = None,
    ) -> "capo_qconnect.types.search_quick_responses_response.SearchQuickResponsesResponse":
        """<p>Searches existing Amazon Q in Connect quick responses in an Amazon Q in Connect knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression for querying the quick response.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            attributes: <p>The <a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-attrib-list.html#user-defined-attributes">user-defined Connect Customer contact attributes</a> to be resolved when search results are returned.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.search_quick_responses_request.SearchQuickResponsesRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.search_quick_responses_response.SearchQuickResponsesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_quick_responses

            output, http_response = (
                capo_qconnect._operations.wisdom_service.search_quick_responses.search_quick_responses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.search_quick_responses_request.SearchQuickResponsesRequest = {
            "knowledge_base_id": knowledge_base_id,
            "search_expression": search_expression,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if attributes is not None:
            input_["attributes"] = attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_content_upload(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_type: "capo_qconnect.types.content_type.ContentType",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        presigned_url_time_to_live: Optional[
            "capo_qconnect.types.time_to_live.TimeToLive"
        ] = None,
    ) -> "capo_qconnect.types.start_content_upload_response.StartContentUploadResponse":
        """<p>Get a URL to upload content to a knowledge base. To upload content, first make a PUT request to the returned URL with your file, making sure to include the required headers. Then use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_CreateContent.html">CreateContent</a> to finalize the content creation process or <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_UpdateContent.html">UpdateContent</a> to modify an existing resource. You can only upload content to a knowledge base of type CUSTOM.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            content_type: <p>The type of content to upload.</p>
            presigned_url_time_to_live: <p>The expected expiration time of the generated presigned URL, specified in minutes.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.start_content_upload_request.StartContentUploadRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.start_content_upload_response.StartContentUploadResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.start_content_upload

            output, http_response = (
                capo_qconnect._operations.wisdom_service.start_content_upload.start_content_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.start_content_upload_request.StartContentUploadRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_type": content_type,
        }
        if presigned_url_time_to_live is not None:
            input_["presigned_url_time_to_live"] = presigned_url_time_to_live

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_import_job(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        import_job_type: "capo_qconnect.types.import_job_type.ImportJobType",
        upload_id: "capo_qconnect.types.upload_id.UploadId",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        client_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        metadata: Optional[
            "capo_qconnect.types.content_metadata.ContentMetadata"
        ] = None,
        external_source_configuration: Optional[
            "capo_qconnect.types.external_source_configuration.ExternalSourceConfiguration"
        ] = None,
    ) -> "capo_qconnect.types.start_import_job_response.StartImportJobResponse":
        """<p>Start an asynchronous job to import Amazon Q in Connect resources from an uploaded source file. Before calling this API, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a> to upload an asset that contains the resource data.</p> <ul> <li> <p>For importing Amazon Q in Connect quick responses, you need to upload a csv file including the quick responses. For information about how to format the csv file for importing quick responses, see <a href="https://docs.aws.amazon.com/console/connect/quick-responses/add-data">Import quick responses</a>.</p> </li> </ul>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p> <ul> <li> <p>For importing Amazon Q in Connect quick responses, this should be a <code>QUICK_RESPONSES</code> type knowledge base.</p> </li> </ul>
            import_job_type: <p>The type of the import job.</p> <ul> <li> <p>For importing quick response resource, set the value to <code>QUICK_RESPONSES</code>.</p> </li> </ul>
            upload_id: <p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>.</p>
            client_token: <p>The tags used to organize, track, or control access for this resource.</p>
            metadata: <p>The metadata fields of the imported Amazon Q in Connect resources.</p>
            external_source_configuration: <p>The configuration information of the external source that the resource data are imported from.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.start_import_job_request.StartImportJobRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.start_import_job_response.StartImportJobResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.start_import_job

            output, http_response = (
                capo_qconnect._operations.wisdom_service.start_import_job.start_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.start_import_job_request.StartImportJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "import_job_type": import_job_type,
            "upload_id": upload_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if metadata is not None:
            input_["metadata"] = metadata
        if external_source_configuration is not None:
            input_["external_source_configuration"] = external_source_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_knowledge_base_template_uri(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        template_uri: "capo_qconnect.types.uri.Uri",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
    ) -> "capo_qconnect.types.update_knowledge_base_template_uri_response.UpdateKnowledgeBaseTemplateUriResponse":
        """<p>Updates the template URI of a knowledge base. This is only supported for knowledge bases of type EXTERNAL. Include a single variable in <code>${variable}</code> format; this interpolated by Amazon Q in Connect using ingested content. For example, if you ingest a Salesforce article, it has an <code>Id</code> value, and you can set the template URI to <code>https://myInstanceName.lightning.force.com/lightning/r/Knowledge__kav/*${Id}*/view</code>. </p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            template_uri: <p>The template URI to update.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.update_knowledge_base_template_uri_request.UpdateKnowledgeBaseTemplateUriRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.update_knowledge_base_template_uri_response.UpdateKnowledgeBaseTemplateUriResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_knowledge_base_template_uri

            output, http_response = (
                capo_qconnect._operations.wisdom_service.update_knowledge_base_template_uri.update_knowledge_base_template_uri(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.update_knowledge_base_template_uri_request.UpdateKnowledgeBaseTemplateUriRequest = {
            "knowledge_base_id": knowledge_base_id,
            "template_uri": template_uri,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncKnowledgeBase:
    def __init__(self, service: AsyncQConnectClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_qconnect.types.name.Name",
        knowledge_base_type: "capo_qconnect.types.knowledge_base_type.KnowledgeBaseType",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        source_configuration: Optional[
            "capo_qconnect.types.source_configuration.SourceConfiguration"
        ] = None,
        rendering_configuration: Optional[
            "capo_qconnect.types.rendering_configuration.RenderingConfiguration"
        ] = None,
        vector_ingestion_configuration: Optional[
            "capo_qconnect.types.vector_ingestion_configuration.VectorIngestionConfiguration"
        ] = None,
        server_side_encryption_configuration: Optional[
            "capo_qconnect.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
    ) -> (
        "capo_qconnect.types.create_knowledge_base_response.CreateKnowledgeBaseResponse"
    ):
        """<p>Creates a knowledge base.</p> <note> <p>When using this API, you cannot reuse <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html">Amazon AppIntegrations</a> DataIntegrations with external knowledge bases such as Salesforce and ServiceNow. If you do, you'll get an <code>InvalidRequestException</code> error. </p> <p>For example, you're programmatically managing your external knowledge base, and you want to add or remove one of the fields that is being ingested from Salesforce. Do the following:</p> <ol> <li> <p>Call <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_DeleteKnowledgeBase.html">DeleteKnowledgeBase</a>.</p> </li> <li> <p>Call <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html">DeleteDataIntegration</a>.</p> </li> <li> <p>Call <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> to recreate the DataIntegration or a create different one.</p> </li> <li> <p>Call CreateKnowledgeBase.</p> </li> </ol> </note>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the knowledge base.</p>
            knowledge_base_type: <p>The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically. </p>
            source_configuration: <p>The source of the knowledge base content. Only set this argument for EXTERNAL or Managed knowledge bases.</p>
            rendering_configuration: <p>Information about how to render the content.</p>
            vector_ingestion_configuration: <p>Contains details about how to ingest the documents in a data source.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, <code>kms:Decrypt</code>, and <code>kms:GenerateDataKey*</code> permissions to the IAM identity using the key to invoke Amazon Q in Connect.</p> <p>For more information about setting up a customer managed key for Amazon Q in Connect, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html">Enable Amazon Q in Connect for your instance</a>.</p>
            description: <p>The description.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_knowledge_base_request.CreateKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_knowledge_base_response.CreateKnowledgeBaseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_knowledge_base

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_knowledge_base.async_create_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.create_knowledge_base_request.CreateKnowledgeBaseRequest = {
            "name": name,
            "knowledge_base_type": knowledge_base_type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if source_configuration is not None:
            input_["source_configuration"] = source_configuration
        if rendering_configuration is not None:
            input_["rendering_configuration"] = rendering_configuration
        if vector_ingestion_configuration is not None:
            input_["vector_ingestion_configuration"] = vector_ingestion_configuration
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )
        if description is not None:
            input_["description"] = description
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
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_knowledge_base_response.GetKnowledgeBaseResponse":
        """<p>Retrieves information about the knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_knowledge_base_request.GetKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_knowledge_base_response.GetKnowledgeBaseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_knowledge_base

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_knowledge_base.async_get_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.get_knowledge_base_request.GetKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> (
        "capo_qconnect.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse"
    ):
        """<p>Deletes the knowledge base.</p> <note> <p>When you use this API to delete an external knowledge base such as Salesforce or ServiceNow, you must also delete the <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html">Amazon AppIntegrations</a> DataIntegration. This is because you can't reuse the DataIntegration after it's been associated with an external knowledge base. However, you can delete and recreate it. See <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html">DeleteDataIntegration</a> and <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> in the <i>Amazon AppIntegrations API Reference</i>.</p> </note>

        Args:
            knowledge_base_id: <p>The knowledge base to delete content from. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_knowledge_base

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_knowledge_base.async_delete_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
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
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_knowledge_bases_response.ListKnowledgeBasesResponse":
        """<p>Lists the knowledge bases.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_knowledge_bases_request.ListKnowledgeBasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_knowledge_bases_response.ListKnowledgeBasesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_knowledge_bases

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_knowledge_bases.async_list_knowledge_bases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.list_knowledge_bases_request.ListKnowledgeBasesRequest = {}
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

    async def delete_import_job(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        import_job_id: "capo_qconnect.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_import_job_response.DeleteImportJobResponse":
        """<p>Deletes the quick response import job.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base.</p>
            import_job_id: <p>The identifier of the import job to be deleted.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_import_job_request.DeleteImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_import_job_response.DeleteImportJobResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_import_job

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_import_job.async_delete_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_import_job_request.DeleteImportJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "import_job_id": import_job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_import_job(
        self,
        import_job_id: "capo_qconnect.types.uuid.Uuid",
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_import_job_response.GetImportJobResponse":
        """<p>Retrieves the started import job.</p>

        Args:
            import_job_id: <p>The identifier of the import job to retrieve.</p>
            knowledge_base_id: <p>The identifier of the knowledge base that the import job belongs to.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_import_job_request.GetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_import_job_response.GetImportJobResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_import_job

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_import_job.async_get_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.get_import_job_request.GetImportJobRequest = {
            "import_job_id": import_job_id,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_import_jobs(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_import_jobs_response.ListImportJobsResponse":
        """<p>Lists information about import jobs.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_import_jobs_request.ListImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_import_jobs_response.ListImportJobsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_import_jobs

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_import_jobs.async_list_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.list_import_jobs_request.ListImportJobsRequest = {
            "knowledge_base_id": knowledge_base_id
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

    async def remove_knowledge_base_template_uri(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.remove_knowledge_base_template_uri_response.RemoveKnowledgeBaseTemplateUriResponse":
        """<p>Removes a URI template from a knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.remove_knowledge_base_template_uri_request.RemoveKnowledgeBaseTemplateUriRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.remove_knowledge_base_template_uri_response.RemoveKnowledgeBaseTemplateUriResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.remove_knowledge_base_template_uri

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.remove_knowledge_base_template_uri.async_remove_knowledge_base_template_uri(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.remove_knowledge_base_template_uri_request.RemoveKnowledgeBaseTemplateUriRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_content(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.search_content_response.SearchContentResponse":
        """<p>Searches for content in a specified knowledge base. Can be used to get a specific content resource by its name.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.search_content_request.SearchContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.search_content_response.SearchContentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_content

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.search_content.async_search_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.search_content_request.SearchContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "search_expression": search_expression,
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

    async def search_message_templates(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.message_template_search_expression.MessageTemplateSearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.search_message_templates_response.SearchMessageTemplatesResponse":
        """<p>Searches for Amazon Q in Connect message templates in the specified knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression for querying the message template.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.search_message_templates_request.SearchMessageTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.search_message_templates_response.SearchMessageTemplatesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_message_templates

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.search_message_templates.async_search_message_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.search_message_templates_request.SearchMessageTemplatesRequest = {
            "knowledge_base_id": knowledge_base_id,
            "search_expression": search_expression,
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

    async def search_quick_responses(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.quick_response_search_expression.QuickResponseSearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        attributes: Optional[
            "capo_qconnect.types.contact_attributes.ContactAttributes"
        ] = None,
    ) -> "capo_qconnect.types.search_quick_responses_response.SearchQuickResponsesResponse":
        """<p>Searches existing Amazon Q in Connect quick responses in an Amazon Q in Connect knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression for querying the quick response.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            attributes: <p>The <a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-attrib-list.html#user-defined-attributes">user-defined Connect Customer contact attributes</a> to be resolved when search results are returned.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.search_quick_responses_request.SearchQuickResponsesRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.search_quick_responses_response.SearchQuickResponsesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_quick_responses

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.search_quick_responses.async_search_quick_responses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.search_quick_responses_request.SearchQuickResponsesRequest = {
            "knowledge_base_id": knowledge_base_id,
            "search_expression": search_expression,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_content_upload(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_type: "capo_qconnect.types.content_type.ContentType",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        presigned_url_time_to_live: Optional[
            "capo_qconnect.types.time_to_live.TimeToLive"
        ] = None,
    ) -> "capo_qconnect.types.start_content_upload_response.StartContentUploadResponse":
        """<p>Get a URL to upload content to a knowledge base. To upload content, first make a PUT request to the returned URL with your file, making sure to include the required headers. Then use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_CreateContent.html">CreateContent</a> to finalize the content creation process or <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_UpdateContent.html">UpdateContent</a> to modify an existing resource. You can only upload content to a knowledge base of type CUSTOM.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            content_type: <p>The type of content to upload.</p>
            presigned_url_time_to_live: <p>The expected expiration time of the generated presigned URL, specified in minutes.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.start_content_upload_request.StartContentUploadRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.start_content_upload_response.StartContentUploadResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.start_content_upload

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.start_content_upload.async_start_content_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.start_content_upload_request.StartContentUploadRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_type": content_type,
        }
        if presigned_url_time_to_live is not None:
            input_["presigned_url_time_to_live"] = presigned_url_time_to_live

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_import_job(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        import_job_type: "capo_qconnect.types.import_job_type.ImportJobType",
        upload_id: "capo_qconnect.types.upload_id.UploadId",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        metadata: Optional[
            "capo_qconnect.types.content_metadata.ContentMetadata"
        ] = None,
        external_source_configuration: Optional[
            "capo_qconnect.types.external_source_configuration.ExternalSourceConfiguration"
        ] = None,
    ) -> "capo_qconnect.types.start_import_job_response.StartImportJobResponse":
        """<p>Start an asynchronous job to import Amazon Q in Connect resources from an uploaded source file. Before calling this API, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a> to upload an asset that contains the resource data.</p> <ul> <li> <p>For importing Amazon Q in Connect quick responses, you need to upload a csv file including the quick responses. For information about how to format the csv file for importing quick responses, see <a href="https://docs.aws.amazon.com/console/connect/quick-responses/add-data">Import quick responses</a>.</p> </li> </ul>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p> <ul> <li> <p>For importing Amazon Q in Connect quick responses, this should be a <code>QUICK_RESPONSES</code> type knowledge base.</p> </li> </ul>
            import_job_type: <p>The type of the import job.</p> <ul> <li> <p>For importing quick response resource, set the value to <code>QUICK_RESPONSES</code>.</p> </li> </ul>
            upload_id: <p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>.</p>
            client_token: <p>The tags used to organize, track, or control access for this resource.</p>
            metadata: <p>The metadata fields of the imported Amazon Q in Connect resources.</p>
            external_source_configuration: <p>The configuration information of the external source that the resource data are imported from.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.start_import_job_request.StartImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.start_import_job_response.StartImportJobResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.start_import_job

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.start_import_job.async_start_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.start_import_job_request.StartImportJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "import_job_type": import_job_type,
            "upload_id": upload_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if metadata is not None:
            input_["metadata"] = metadata
        if external_source_configuration is not None:
            input_["external_source_configuration"] = external_source_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_knowledge_base_template_uri(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        template_uri: "capo_qconnect.types.uri.Uri",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.update_knowledge_base_template_uri_response.UpdateKnowledgeBaseTemplateUriResponse":
        """<p>Updates the template URI of a knowledge base. This is only supported for knowledge bases of type EXTERNAL. Include a single variable in <code>${variable}</code> format; this interpolated by Amazon Q in Connect using ingested content. For example, if you ingest a Salesforce article, it has an <code>Id</code> value, and you can set the template URI to <code>https://myInstanceName.lightning.force.com/lightning/r/Knowledge__kav/*${Id}*/view</code>. </p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            template_uri: <p>The template URI to update.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_knowledge_base_template_uri_request.UpdateKnowledgeBaseTemplateUriRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_knowledge_base_template_uri_response.UpdateKnowledgeBaseTemplateUriResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_knowledge_base_template_uri

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_knowledge_base_template_uri.async_update_knowledge_base_template_uri(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.update_knowledge_base_template_uri_request.UpdateKnowledgeBaseTemplateUriRequest = {
            "knowledge_base_id": knowledge_base_id,
            "template_uri": template_uri,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
