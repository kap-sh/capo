"""Generated from Smithy shape ``com.amazonaws.kendra#AWSKendraFrontendService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_kendra._auth._signers
import capo_kendra._auth._sigv4
from capo_kendra._auth._identity import Credentials
from capo_kendra._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_kendra._auth._zapros_handler import AuthMiddleware
from capo_kendra._pagination import resolve_path as _resolve_path
from capo_kendra._services._aws_config import aws_config
from capo_kendra._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_kendra.types.access_control_configuration_id
    import capo_kendra.types.access_control_configuration_name
    import capo_kendra.types.amazon_resource_name
    import capo_kendra.types.associate_entities_to_experience_request
    import capo_kendra.types.associate_entities_to_experience_response
    import capo_kendra.types.associate_entity_list
    import capo_kendra.types.associate_personas_to_entities_request
    import capo_kendra.types.associate_personas_to_entities_response
    import capo_kendra.types.attribute_filter
    import capo_kendra.types.attribute_suggestions_get_config
    import capo_kendra.types.attribute_suggestions_update_config
    import capo_kendra.types.batch_delete_document_request
    import capo_kendra.types.batch_delete_document_response
    import capo_kendra.types.batch_delete_featured_results_set_request
    import capo_kendra.types.batch_delete_featured_results_set_response
    import capo_kendra.types.batch_get_document_status_request
    import capo_kendra.types.batch_get_document_status_response
    import capo_kendra.types.batch_put_document_request
    import capo_kendra.types.batch_put_document_response
    import capo_kendra.types.capacity_units_configuration
    import capo_kendra.types.clear_query_suggestions_request
    import capo_kendra.types.click_feedback_list
    import capo_kendra.types.client_token_name
    import capo_kendra.types.collapse_configuration
    import capo_kendra.types.create_access_control_configuration_request
    import capo_kendra.types.create_access_control_configuration_response
    import capo_kendra.types.create_data_source_request
    import capo_kendra.types.create_data_source_response
    import capo_kendra.types.create_experience_request
    import capo_kendra.types.create_experience_response
    import capo_kendra.types.create_faq_request
    import capo_kendra.types.create_faq_response
    import capo_kendra.types.create_featured_results_set_request
    import capo_kendra.types.create_featured_results_set_response
    import capo_kendra.types.create_index_request
    import capo_kendra.types.create_index_response
    import capo_kendra.types.create_query_suggestions_block_list_request
    import capo_kendra.types.create_query_suggestions_block_list_response
    import capo_kendra.types.create_thesaurus_request
    import capo_kendra.types.create_thesaurus_response
    import capo_kendra.types.custom_document_enrichment_configuration
    import capo_kendra.types.data_source_configuration
    import capo_kendra.types.data_source_id
    import capo_kendra.types.data_source_name
    import capo_kendra.types.data_source_sync_job_metric_target
    import capo_kendra.types.data_source_sync_job_status
    import capo_kendra.types.data_source_type
    import capo_kendra.types.data_source_vpc_configuration
    import capo_kendra.types.delete_access_control_configuration_request
    import capo_kendra.types.delete_access_control_configuration_response
    import capo_kendra.types.delete_data_source_request
    import capo_kendra.types.delete_experience_request
    import capo_kendra.types.delete_experience_response
    import capo_kendra.types.delete_faq_request
    import capo_kendra.types.delete_index_request
    import capo_kendra.types.delete_principal_mapping_request
    import capo_kendra.types.delete_query_suggestions_block_list_request
    import capo_kendra.types.delete_thesaurus_request
    import capo_kendra.types.describe_access_control_configuration_request
    import capo_kendra.types.describe_access_control_configuration_response
    import capo_kendra.types.describe_data_source_request
    import capo_kendra.types.describe_data_source_response
    import capo_kendra.types.describe_experience_request
    import capo_kendra.types.describe_experience_response
    import capo_kendra.types.describe_faq_request
    import capo_kendra.types.describe_faq_response
    import capo_kendra.types.describe_featured_results_set_request
    import capo_kendra.types.describe_featured_results_set_response
    import capo_kendra.types.describe_index_request
    import capo_kendra.types.describe_index_response
    import capo_kendra.types.describe_principal_mapping_request
    import capo_kendra.types.describe_principal_mapping_response
    import capo_kendra.types.describe_query_suggestions_block_list_request
    import capo_kendra.types.describe_query_suggestions_block_list_response
    import capo_kendra.types.describe_query_suggestions_config_request
    import capo_kendra.types.describe_query_suggestions_config_response
    import capo_kendra.types.describe_thesaurus_request
    import capo_kendra.types.describe_thesaurus_response
    import capo_kendra.types.description
    import capo_kendra.types.disassociate_entities_from_experience_request
    import capo_kendra.types.disassociate_entities_from_experience_response
    import capo_kendra.types.disassociate_entity_list
    import capo_kendra.types.disassociate_personas_from_entities_request
    import capo_kendra.types.disassociate_personas_from_entities_response
    import capo_kendra.types.document_attribute_key_list
    import capo_kendra.types.document_id_list
    import capo_kendra.types.document_info_list
    import capo_kendra.types.document_list
    import capo_kendra.types.document_metadata_configuration_list
    import capo_kendra.types.document_relevance_override_configuration_list
    import capo_kendra.types.entity_ids_list
    import capo_kendra.types.entity_persona_configuration_list
    import capo_kendra.types.experience_configuration
    import capo_kendra.types.experience_id
    import capo_kendra.types.experience_name
    import capo_kendra.types.facet_list
    import capo_kendra.types.faq_file_format
    import capo_kendra.types.faq_id
    import capo_kendra.types.faq_name
    import capo_kendra.types.featured_document_list
    import capo_kendra.types.featured_results_set_description
    import capo_kendra.types.featured_results_set_id
    import capo_kendra.types.featured_results_set_id_list
    import capo_kendra.types.featured_results_set_name
    import capo_kendra.types.featured_results_set_status
    import capo_kendra.types.get_query_suggestions_request
    import capo_kendra.types.get_query_suggestions_response
    import capo_kendra.types.get_snapshots_request
    import capo_kendra.types.get_snapshots_response
    import capo_kendra.types.group_id
    import capo_kendra.types.group_members
    import capo_kendra.types.hierarchical_principal_list
    import capo_kendra.types.index_edition
    import capo_kendra.types.index_id
    import capo_kendra.types.index_name
    import capo_kendra.types.integer
    import capo_kendra.types.interval
    import capo_kendra.types.language_code
    import capo_kendra.types.list_access_control_configurations_request
    import capo_kendra.types.list_access_control_configurations_response
    import capo_kendra.types.list_data_source_sync_jobs_request
    import capo_kendra.types.list_data_source_sync_jobs_response
    import capo_kendra.types.list_data_sources_request
    import capo_kendra.types.list_data_sources_response
    import capo_kendra.types.list_entity_personas_request
    import capo_kendra.types.list_entity_personas_response
    import capo_kendra.types.list_experience_entities_request
    import capo_kendra.types.list_experience_entities_response
    import capo_kendra.types.list_experiences_request
    import capo_kendra.types.list_experiences_response
    import capo_kendra.types.list_faqs_request
    import capo_kendra.types.list_faqs_response
    import capo_kendra.types.list_featured_results_sets_request
    import capo_kendra.types.list_featured_results_sets_response
    import capo_kendra.types.list_groups_older_than_ordering_id_request
    import capo_kendra.types.list_groups_older_than_ordering_id_response
    import capo_kendra.types.list_indices_request
    import capo_kendra.types.list_indices_response
    import capo_kendra.types.list_query_suggestions_block_lists_request
    import capo_kendra.types.list_query_suggestions_block_lists_response
    import capo_kendra.types.list_tags_for_resource_request
    import capo_kendra.types.list_tags_for_resource_response
    import capo_kendra.types.list_thesauri_request
    import capo_kendra.types.list_thesauri_response
    import capo_kendra.types.max_results_integer_for_list_access_control_configurations_request
    import capo_kendra.types.max_results_integer_for_list_data_source_sync_jobs_request
    import capo_kendra.types.max_results_integer_for_list_data_sources_request
    import capo_kendra.types.max_results_integer_for_list_entity_personas_request
    import capo_kendra.types.max_results_integer_for_list_experiences_request
    import capo_kendra.types.max_results_integer_for_list_faqs_request
    import capo_kendra.types.max_results_integer_for_list_featured_results_sets_request
    import capo_kendra.types.max_results_integer_for_list_indices_request
    import capo_kendra.types.max_results_integer_for_list_principals_request
    import capo_kendra.types.max_results_integer_for_list_query_suggestions_block_lists
    import capo_kendra.types.max_results_integer_for_list_thesauri_request
    import capo_kendra.types.metric_type
    import capo_kendra.types.minimum_number_of_querying_users
    import capo_kendra.types.minimum_query_count
    import capo_kendra.types.mode
    import capo_kendra.types.next_token
    import capo_kendra.types.object_boolean
    import capo_kendra.types.principal_list
    import capo_kendra.types.principal_ordering_id
    import capo_kendra.types.put_principal_mapping_request
    import capo_kendra.types.query_id
    import capo_kendra.types.query_request
    import capo_kendra.types.query_result
    import capo_kendra.types.query_result_type
    import capo_kendra.types.query_suggestions_block_list_id
    import capo_kendra.types.query_suggestions_block_list_name
    import capo_kendra.types.query_text
    import capo_kendra.types.query_text_list
    import capo_kendra.types.relevance_feedback_list
    import capo_kendra.types.retrieve_request
    import capo_kendra.types.retrieve_result
    import capo_kendra.types.role_arn
    import capo_kendra.types.s3_path
    import capo_kendra.types.scan_schedule
    import capo_kendra.types.server_side_encryption_configuration
    import capo_kendra.types.sorting_configuration
    import capo_kendra.types.sorting_configuration_list
    import capo_kendra.types.spell_correction_configuration
    import capo_kendra.types.start_data_source_sync_job_request
    import capo_kendra.types.start_data_source_sync_job_response
    import capo_kendra.types.stop_data_source_sync_job_request
    import capo_kendra.types.string
    import capo_kendra.types.submit_feedback_request
    import capo_kendra.types.suggestion_query_text
    import capo_kendra.types.suggestion_types
    import capo_kendra.types.tag_key_list
    import capo_kendra.types.tag_list
    import capo_kendra.types.tag_resource_request
    import capo_kendra.types.tag_resource_response
    import capo_kendra.types.thesaurus_id
    import capo_kendra.types.thesaurus_name
    import capo_kendra.types.time_range
    import capo_kendra.types.untag_resource_request
    import capo_kendra.types.untag_resource_response
    import capo_kendra.types.update_access_control_configuration_request
    import capo_kendra.types.update_access_control_configuration_response
    import capo_kendra.types.update_data_source_request
    import capo_kendra.types.update_experience_request
    import capo_kendra.types.update_featured_results_set_request
    import capo_kendra.types.update_featured_results_set_response
    import capo_kendra.types.update_index_request
    import capo_kendra.types.update_query_suggestions_block_list_request
    import capo_kendra.types.update_query_suggestions_config_request
    import capo_kendra.types.update_thesaurus_request
    import capo_kendra.types.user_context
    import capo_kendra.types.user_context_policy
    import capo_kendra.types.user_group_resolution_configuration
    import capo_kendra.types.user_token_configuration_list
    import capo_kendra.types.visitor_id


class kendraClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class kendraClient:
    """A client for the ``kendra`` service.

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
        self._config = kendraClientConfig(
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
        self, config_overrides: Optional[kendraClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: kendraClientConfig = config_overrides or {}
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

    def associate_entities_to_experience(
        self,
        id: "capo_kendra.types.experience_id.ExperienceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        entity_list: "capo_kendra.types.associate_entity_list.AssociateEntityList",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.associate_entities_to_experience_response.AssociateEntitiesToExperienceResponse":
        """<p>Grants users or groups in your IAM Identity Center identity source access to your Amazon Kendra experience. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html">Building a search experience with no code</a>.</p>

        Args:
            id: <p>The identifier of your Amazon Kendra experience.</p>
            index_id: <p>The identifier of the index for your Amazon Kendra experience.</p>
            entity_list: <p>Lists users or groups in your IAM Identity Center identity source.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_already_exist_exception.ResourceAlreadyExistException: <p>The resource you want to use already exists. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.associate_entities_to_experience_request.AssociateEntitiesToExperienceRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.associate_entities_to_experience_response.AssociateEntitiesToExperienceResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.associate_entities_to_experience

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.associate_entities_to_experience.associate_entities_to_experience(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.associate_entities_to_experience_request.AssociateEntitiesToExperienceRequest = {
            "id": id,
            "index_id": index_id,
            "entity_list": entity_list,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_personas_to_entities(
        self,
        id: "capo_kendra.types.experience_id.ExperienceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        personas: "capo_kendra.types.entity_persona_configuration_list.EntityPersonaConfigurationList",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.associate_personas_to_entities_response.AssociatePersonasToEntitiesResponse":
        """<p>Defines the specific permissions of users or groups in your IAM Identity Center identity source with access to your Amazon Kendra experience. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html">Building a search experience with no code</a>.</p>

        Args:
            id: <p>The identifier of your Amazon Kendra experience.</p>
            index_id: <p>The identifier of the index for your Amazon Kendra experience.</p>
            personas: <p>The personas that define the specific permissions of users or groups in your IAM Identity Center identity source. The available personas or access roles are <code>Owner</code> and <code>Viewer</code>. For more information on these personas, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html#access-search-experience">Providing access to your search page</a>.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_already_exist_exception.ResourceAlreadyExistException: <p>The resource you want to use already exists. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.associate_personas_to_entities_request.AssociatePersonasToEntitiesRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.associate_personas_to_entities_response.AssociatePersonasToEntitiesResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.associate_personas_to_entities

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.associate_personas_to_entities.associate_personas_to_entities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.associate_personas_to_entities_request.AssociatePersonasToEntitiesRequest = {
            "id": id,
            "index_id": index_id,
            "personas": personas,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_document(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        document_id_list: "capo_kendra.types.document_id_list.DocumentIdList",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        data_source_sync_job_metric_target: Optional[
            "capo_kendra.types.data_source_sync_job_metric_target.DataSourceSyncJobMetricTarget"
        ] = None,
    ) -> "capo_kendra.types.batch_delete_document_response.BatchDeleteDocumentResponse":
        """<p>Removes one or more documents from an index. The documents must have been added with the <code>BatchPutDocument</code> API.</p> <p>The documents are deleted asynchronously. You can see the progress of the deletion by using Amazon Web Services CloudWatch. Any error messages related to the processing of the batch are sent to your Amazon Web Services CloudWatch log. You can also use the <code>BatchGetDocumentStatus</code> API to monitor the progress of deleting your documents.</p> <p>Deleting documents from an index using <code>BatchDeleteDocument</code> could take up to an hour or more, depending on the number of documents you want to delete.</p>

        Args:
            index_id: <p>The identifier of the index that contains the documents to delete.</p>
            document_id_list: <p>One or more identifiers for documents to delete from the index.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.batch_delete_document_request.BatchDeleteDocumentRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.batch_delete_document_response.BatchDeleteDocumentResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.batch_delete_document

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.batch_delete_document.batch_delete_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.batch_delete_document_request.BatchDeleteDocumentRequest = {
            "index_id": index_id,
            "document_id_list": document_id_list,
        }
        if data_source_sync_job_metric_target is not None:
            input_["data_source_sync_job_metric_target"] = (
                data_source_sync_job_metric_target
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_featured_results_set(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        featured_results_set_ids: "capo_kendra.types.featured_results_set_id_list.FeaturedResultsSetIdList",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.batch_delete_featured_results_set_response.BatchDeleteFeaturedResultsSetResponse":
        """<p>Removes one or more sets of featured results. Features results are placed above all other results for certain queries. If there's an exact match of a query, then one or more specific documents are featured in the search results.</p>

        Args:
            index_id: <p>The identifier of the index used for featuring results.</p>
            featured_results_set_ids: <p>The identifiers of the featured results sets that you want to delete.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.batch_delete_featured_results_set_request.BatchDeleteFeaturedResultsSetRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.batch_delete_featured_results_set_response.BatchDeleteFeaturedResultsSetResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.batch_delete_featured_results_set

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.batch_delete_featured_results_set.batch_delete_featured_results_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.batch_delete_featured_results_set_request.BatchDeleteFeaturedResultsSetRequest = {
            "index_id": index_id,
            "featured_results_set_ids": featured_results_set_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_document_status(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        document_info_list: "capo_kendra.types.document_info_list.DocumentInfoList",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.batch_get_document_status_response.BatchGetDocumentStatusResponse":
        """<p>Returns the indexing status for one or more documents submitted with the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html"> BatchPutDocument</a> API.</p> <p>When you use the <code>BatchPutDocument</code> API, documents are indexed asynchronously. You can use the <code>BatchGetDocumentStatus</code> API to get the current status of a list of documents so that you can determine if they have been successfully indexed.</p> <p>You can also use the <code>BatchGetDocumentStatus</code> API to check the status of the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_BatchDeleteDocument.html"> BatchDeleteDocument</a> API. When a document is deleted from the index, Amazon Kendra returns <code>NOT_FOUND</code> as the status.</p>

        Args:
            index_id: <p>The identifier of the index to add documents to. The index ID is returned by the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_CreateIndex.html">CreateIndex </a> API.</p>
            document_info_list: <p>A list of <code>DocumentInfo</code> objects that identify the documents for which to get the status. You identify the documents by their document ID and optional attributes.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.batch_get_document_status_request.BatchGetDocumentStatusRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.batch_get_document_status_response.BatchGetDocumentStatusResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.batch_get_document_status

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.batch_get_document_status.batch_get_document_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.batch_get_document_status_request.BatchGetDocumentStatusRequest = {
            "index_id": index_id,
            "document_info_list": document_info_list,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_put_document(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        documents: "capo_kendra.types.document_list.DocumentList",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        role_arn: Optional["capo_kendra.types.role_arn.RoleArn"] = None,
        custom_document_enrichment_configuration: Optional[
            "capo_kendra.types.custom_document_enrichment_configuration.CustomDocumentEnrichmentConfiguration"
        ] = None,
    ) -> "capo_kendra.types.batch_put_document_response.BatchPutDocumentResponse":
        """<p>Adds one or more documents to an index.</p> <p>The <code>BatchPutDocument</code> API enables you to ingest inline documents or a set of documents stored in an Amazon S3 bucket. Use this API to ingest your text and unstructured text into an index, add custom attributes to the documents, and to attach an access control list to the documents added to the index.</p> <p>The documents are indexed asynchronously. You can see the progress of the batch using Amazon Web Services CloudWatch. Any error messages related to processing the batch are sent to your Amazon Web Services CloudWatch log. You can also use the <code>BatchGetDocumentStatus</code> API to monitor the progress of indexing your documents.</p> <p>For an example of ingesting inline documents using Python and Java SDKs, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-adding-binary-doc.html">Adding files directly to an index</a>.</p>

        Args:
            index_id: <p>The identifier of the index to add the documents to. You need to create the index first using the <code>CreateIndex</code> API.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM access roles for Amazon Kendra</a>.</p>
            documents: <p>One or more documents to add to the index.</p> <p>Documents have the following file size limits.</p> <ul> <li> <p>50 MB total size for any file</p> </li> <li> <p>5 MB extracted text for any file</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a>.</p>
            custom_document_enrichment_configuration: <p>Configuration information for altering your document metadata and content during the document ingestion process when you use the <code>BatchPutDocument</code> API.</p> <p>For more information on how to create, modify and delete document metadata, or make other content alterations when you ingest documents into Amazon Kendra, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html">Customizing document metadata during the ingestion process</a>.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.batch_put_document_request.BatchPutDocumentRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.batch_put_document_response.BatchPutDocumentResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.batch_put_document

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.batch_put_document.batch_put_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.batch_put_document_request.BatchPutDocumentRequest = {
            "index_id": index_id,
            "documents": documents,
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if custom_document_enrichment_configuration is not None:
            input_["custom_document_enrichment_configuration"] = (
                custom_document_enrichment_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def clear_query_suggestions(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> None:
        """<p>Clears existing query suggestions from an index.</p> <p>This deletes existing suggestions only, not the queries in the query log. After you clear suggestions, Amazon Kendra learns new suggestions based on new queries added to the query log from the time you cleared suggestions. If you do not see any new suggestions, then please allow Amazon Kendra to collect enough queries to learn new suggestions.</p> <p> <code>ClearQuerySuggestions</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p>The identifier of the index you want to clear query suggestions from.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.clear_query_suggestions_request.ClearQuerySuggestionsRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.clear_query_suggestions

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.clear_query_suggestions.clear_query_suggestions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.clear_query_suggestions_request.ClearQuerySuggestionsRequest = {
            "index_id": index_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_access_control_configuration(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        name: "capo_kendra.types.access_control_configuration_name.AccessControlConfigurationName",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        access_control_list: Optional[
            "capo_kendra.types.principal_list.PrincipalList"
        ] = None,
        hierarchical_access_control_list: Optional[
            "capo_kendra.types.hierarchical_principal_list.HierarchicalPrincipalList"
        ] = None,
        client_token: Optional[
            "capo_kendra.types.client_token_name.ClientTokenName"
        ] = None,
    ) -> "capo_kendra.types.create_access_control_configuration_response.CreateAccessControlConfigurationResponse":
        """<p>Creates an access configuration for your documents. This includes user and group access information for your documents. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p> <p>You can use this to re-configure your existing document level access control without indexing all of your documents again. For example, your index contains top-secret company documents that only certain employees or users should access. One of these users leaves the company or switches to a team that should be blocked from accessing top-secret documents. The user still has access to top-secret documents because the user had access when your documents were previously indexed. You can create a specific access control configuration for the user with deny access. You can later update the access control configuration to allow access if the user returns to the company and re-joins the 'top-secret' team. You can re-configure access control for your documents as circumstances change.</p> <p>To apply your access control configuration to certain documents, you call the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html">BatchPutDocument</a> API with the <code>AccessControlConfigurationId</code> included in the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_Document.html">Document</a> object. If you use an S3 bucket as a data source, you update the <code>.metadata.json</code> with the <code>AccessControlConfigurationId</code> and synchronize your data source. Amazon Kendra currently only supports access control configuration for S3 data sources and documents indexed using the <code>BatchPutDocument</code> API.</p> <important> <p>You can't configure access control using <code>CreateAccessControlConfiguration</code> for an Amazon Kendra Gen AI Enterprise Edition index. Amazon Kendra will return a <code>ValidationException</code> error for a <code>Gen_AI_ENTERPRISE_EDITION</code> index.</p> </important>

        Args:
            index_id: <p>The identifier of the index to create an access control configuration for your documents.</p>
            name: <p>A name for the access control configuration.</p>
            description: <p>A description for the access control configuration.</p>
            access_control_list: <p>Information on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>
            hierarchical_access_control_list: <p>The list of <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html">principal</a> lists that define the hierarchy for which documents users should have access to.</p>
            client_token: <p>A token that you provide to identify the request to create an access control configuration. Multiple calls to the <code>CreateAccessControlConfiguration</code> API with the same client token will create only one access control configuration.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.create_access_control_configuration_request.CreateAccessControlConfigurationRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.create_access_control_configuration_response.CreateAccessControlConfigurationResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.create_access_control_configuration

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.create_access_control_configuration.create_access_control_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.create_access_control_configuration_request.CreateAccessControlConfigurationRequest = {
            "index_id": index_id,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if access_control_list is not None:
            input_["access_control_list"] = access_control_list
        if hierarchical_access_control_list is not None:
            input_["hierarchical_access_control_list"] = (
                hierarchical_access_control_list
            )
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

    def create_data_source(
        self,
        name: "capo_kendra.types.data_source_name.DataSourceName",
        index_id: "capo_kendra.types.index_id.IndexId",
        type: "capo_kendra.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        configuration: Optional[
            "capo_kendra.types.data_source_configuration.DataSourceConfiguration"
        ] = None,
        vpc_configuration: Optional[
            "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
        ] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        schedule: Optional["capo_kendra.types.scan_schedule.ScanSchedule"] = None,
        role_arn: Optional["capo_kendra.types.role_arn.RoleArn"] = None,
        tags: Optional["capo_kendra.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_kendra.types.client_token_name.ClientTokenName"
        ] = None,
        language_code: Optional["capo_kendra.types.language_code.LanguageCode"] = None,
        custom_document_enrichment_configuration: Optional[
            "capo_kendra.types.custom_document_enrichment_configuration.CustomDocumentEnrichmentConfiguration"
        ] = None,
    ) -> "capo_kendra.types.create_data_source_response.CreateDataSourceResponse":
        """<p>Creates a data source connector that you want to use with an Amazon Kendra index.</p> <p>You specify a name, data source connector type and description for your data source. You also specify configuration information for the data source connector.</p> <p> <code>CreateDataSource</code> is a synchronous operation. The operation returns 200 if the data source was successfully created. Otherwise, an exception is raised.</p> <p>For an example of creating an index and data source using the Python SDK, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/gs-python.html">Getting started with Python SDK</a>. For an example of creating an index and data source using the Java SDK, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/gs-java.html">Getting started with Java SDK</a>.</p>

        Args:
            name: <p>A name for the data source connector.</p>
            index_id: <p>The identifier of the index you want to use with the data source connector.</p>
            type: <p>The type of data source repository. For example, <code>SHAREPOINT</code>.</p>
            configuration: <p>Configuration information to connect to your data source repository.</p> <p>You can't specify the <code>Configuration</code> parameter when the <code>Type</code> parameter is set to <code>CUSTOM</code>. If you do, you receive a <code>ValidationException</code> exception.</p> <p>The <code>Configuration</code> parameter is required for all other data sources.</p>
            vpc_configuration: <p>Configuration information for an Amazon Virtual Private Cloud to connect to your data source. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html">Configuring a VPC</a>.</p>
            description: <p>A description for the data source connector.</p>
            schedule: <p>Sets the frequency for Amazon Kendra to check the documents in your data source repository and update the index. If you don't set a schedule Amazon Kendra will not periodically update the index. You can call the <code>StartDataSourceSyncJob</code> API to update the index.</p> <p>Specify a <code>cron-</code> format schedule string or an empty string to indicate that the index is updated on demand.</p> <p>You can't specify the <code>Schedule</code> parameter when the <code>Type</code> parameter is set to <code>CUSTOM</code>. If you do, you receive a <code>ValidationException</code> exception.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM access roles for Amazon Kendra.</a>.</p> <p>You can't specify the <code>RoleArn</code> parameter when the <code>Type</code> parameter is set to <code>CUSTOM</code>. If you do, you receive a <code>ValidationException</code> exception.</p> <p>The <code>RoleArn</code> parameter is required for all other data sources.</p>
            tags: <p>A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            client_token: <p>A token that you provide to identify the request to create a data source connector. Multiple calls to the <code>CreateDataSource</code> API with the same client token will create only one data source connector.</p>
            language_code: <p>The code for a language. This allows you to support a language for all documents when creating the data source connector. English is supported by default. For more information on supported languages, including their codes, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html">Adding documents in languages other than English</a>.</p>
            custom_document_enrichment_configuration: <p>Configuration information for altering document metadata and content during the document ingestion process.</p> <p>For more information on how to create, modify and delete document metadata, or make other content alterations when you ingest documents into Amazon Kendra, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html">Customizing document metadata during the ingestion process</a>.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_already_exist_exception.ResourceAlreadyExistException: <p>The resource you want to use already exists. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.create_data_source_request.CreateDataSourceRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.create_data_source_response.CreateDataSourceResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.create_data_source

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.create_data_source.create_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.create_data_source_request.CreateDataSourceRequest = {
            "name": name,
            "index_id": index_id,
            "type": type,
        }
        if configuration is not None:
            input_["configuration"] = configuration
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if description is not None:
            input_["description"] = description
        if schedule is not None:
            input_["schedule"] = schedule
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if language_code is not None:
            input_["language_code"] = language_code
        if custom_document_enrichment_configuration is not None:
            input_["custom_document_enrichment_configuration"] = (
                custom_document_enrichment_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_experience(
        self,
        name: "capo_kendra.types.experience_name.ExperienceName",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        role_arn: Optional["capo_kendra.types.role_arn.RoleArn"] = None,
        configuration: Optional[
            "capo_kendra.types.experience_configuration.ExperienceConfiguration"
        ] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        client_token: Optional[
            "capo_kendra.types.client_token_name.ClientTokenName"
        ] = None,
    ) -> "capo_kendra.types.create_experience_response.CreateExperienceResponse":
        """<p>Creates an Amazon Kendra experience such as a search application. For more information on creating a search application experience, including using the Python and Java SDKs, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html">Building a search experience with no code</a>.</p>

        Args:
            name: <p>A name for your Amazon Kendra experience.</p>
            index_id: <p>The identifier of the index for your Amazon Kendra experience.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access <code>Query</code> API, <code>GetQuerySuggestions</code> API, and other required APIs. The role also must include permission to access IAM Identity Center that stores your user and group information. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM access roles for Amazon Kendra</a>.</p>
            configuration: <p>Configuration information for your Amazon Kendra experience. This includes <code>ContentSourceConfiguration</code>, which specifies the data source IDs and/or FAQ IDs, and <code>UserIdentityConfiguration</code>, which specifies the user or group information to grant access to your Amazon Kendra experience.</p>
            description: <p>A description for your Amazon Kendra experience.</p>
            client_token: <p>A token that you provide to identify the request to create your Amazon Kendra experience. Multiple calls to the <code>CreateExperience</code> API with the same client token creates only one Amazon Kendra experience.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.create_experience_request.CreateExperienceRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.create_experience_response.CreateExperienceResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.create_experience

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.create_experience.create_experience(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.create_experience_request.CreateExperienceRequest = {
            "name": name,
            "index_id": index_id,
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if configuration is not None:
            input_["configuration"] = configuration
        if description is not None:
            input_["description"] = description
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

    def create_faq(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        name: "capo_kendra.types.faq_name.FaqName",
        s3_path: "capo_kendra.types.s3_path.S3Path",
        role_arn: "capo_kendra.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        tags: Optional["capo_kendra.types.tag_list.TagList"] = None,
        file_format: Optional["capo_kendra.types.faq_file_format.FaqFileFormat"] = None,
        client_token: Optional[
            "capo_kendra.types.client_token_name.ClientTokenName"
        ] = None,
        language_code: Optional["capo_kendra.types.language_code.LanguageCode"] = None,
    ) -> "capo_kendra.types.create_faq_response.CreateFaqResponse":
        """<p>Creates a set of frequently ask questions (FAQs) using a specified FAQ file stored in an Amazon S3 bucket.</p> <p>Adding FAQs to an index is an asynchronous operation.</p> <p>For an example of adding an FAQ to an index using Python and Java SDKs, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html#using-faq-file">Using your FAQ file</a>.</p>

        Args:
            index_id: <p>The identifier of the index for the FAQ.</p>
            name: <p>A name for the FAQ.</p>
            description: <p>A description for the FAQ.</p>
            s3_path: <p>The path to the FAQ file in S3.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access the S3 bucket that contains the FAQ file. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM access roles for Amazon Kendra</a>.</p>
            tags: <p>A list of key-value pairs that identify the FAQ. You can use the tags to identify and organize your resources and to control access to resources.</p>
            file_format: <p>The format of the FAQ input file. You can choose between a basic CSV format, a CSV format that includes customs attributes in a header, and a JSON format that includes custom attributes.</p> <p>The default format is CSV.</p> <p>The format must match the format of the file stored in the S3 bucket identified in the <code>S3Path</code> parameter.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html">Adding questions and answers</a>.</p>
            client_token: <p>A token that you provide to identify the request to create a FAQ. Multiple calls to the <code>CreateFaqRequest</code> API with the same client token will create only one FAQ. </p>
            language_code: <p>The code for a language. This allows you to support a language for the FAQ document. English is supported by default. For more information on supported languages, including their codes, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html">Adding documents in languages other than English</a>.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.create_faq_request.CreateFaqRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.create_faq_response.CreateFaqResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.create_faq

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.create_faq.create_faq(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.create_faq_request.CreateFaqRequest = {
            "index_id": index_id,
            "name": name,
            "s3_path": s3_path,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if file_format is not None:
            input_["file_format"] = file_format
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if language_code is not None:
            input_["language_code"] = language_code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_featured_results_set(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        featured_results_set_name: "capo_kendra.types.featured_results_set_name.FeaturedResultsSetName",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        description: Optional[
            "capo_kendra.types.featured_results_set_description.FeaturedResultsSetDescription"
        ] = None,
        client_token: Optional[
            "capo_kendra.types.client_token_name.ClientTokenName"
        ] = None,
        status: Optional[
            "capo_kendra.types.featured_results_set_status.FeaturedResultsSetStatus"
        ] = None,
        query_texts: Optional["capo_kendra.types.query_text_list.QueryTextList"] = None,
        featured_documents: Optional[
            "capo_kendra.types.featured_document_list.FeaturedDocumentList"
        ] = None,
        tags: Optional["capo_kendra.types.tag_list.TagList"] = None,
    ) -> "capo_kendra.types.create_featured_results_set_response.CreateFeaturedResultsSetResponse":
        """<p>Creates a set of featured results to display at the top of the search results page. Featured results are placed above all other results for certain queries. You map specific queries to specific documents for featuring in the results. If a query contains an exact match, then one or more specific documents are featured in the search results.</p> <p>You can create up to 50 sets of featured results per index. You can request to increase this limit by contacting <a href="http://aws.amazon.com/contact-us/">Support</a>.</p>

        Args:
            index_id: <p>The identifier of the index that you want to use for featuring results.</p>
            featured_results_set_name: <p>A name for the set of featured results.</p>
            description: <p>A description for the set of featured results.</p>
            client_token: <p>A token that you provide to identify the request to create a set of featured results. Multiple calls to the <code>CreateFeaturedResultsSet</code> API with the same client token will create only one featured results set.</p>
            status: <p>The current status of the set of featured results. When the value is <code>ACTIVE</code>, featured results are ready for use. You can still configure your settings before setting the status to <code>ACTIVE</code>. You can set the status to <code>ACTIVE</code> or <code>INACTIVE</code> using the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateFeaturedResultsSet.html">UpdateFeaturedResultsSet</a> API. The queries you specify for featured results must be unique per featured results set for each index, whether the status is <code>ACTIVE</code> or <code>INACTIVE</code>.</p>
            query_texts: <p>A list of queries for featuring results. For more information on the list of queries, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html">FeaturedResultsSet</a>.</p>
            featured_documents: <p>A list of document IDs for the documents you want to feature at the top of the search results page. For more information on the list of documents, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html">FeaturedResultsSet</a>.</p>
            tags: <p>A list of key-value pairs that identify or categorize the featured results set. You can also use tags to help control access to the featured results set. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols:_ . : / = + - @.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.featured_results_conflict_exception.FeaturedResultsConflictException: <p>An error message with a list of conflicting queries used across different sets of featured results. This occurred with the request for a new featured results set. Check that the queries you specified for featured results are unique per featured results set for each index.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.create_featured_results_set_request.CreateFeaturedResultsSetRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.create_featured_results_set_response.CreateFeaturedResultsSetResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.create_featured_results_set

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.create_featured_results_set.create_featured_results_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.create_featured_results_set_request.CreateFeaturedResultsSetRequest = {
            "index_id": index_id,
            "featured_results_set_name": featured_results_set_name,
        }
        if description is not None:
            input_["description"] = description
        if client_token is not None:
            input_["client_token"] = client_token
        if status is not None:
            input_["status"] = status
        if query_texts is not None:
            input_["query_texts"] = query_texts
        if featured_documents is not None:
            input_["featured_documents"] = featured_documents
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_index(
        self,
        name: "capo_kendra.types.index_name.IndexName",
        role_arn: "capo_kendra.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        edition: Optional["capo_kendra.types.index_edition.IndexEdition"] = None,
        server_side_encryption_configuration: Optional[
            "capo_kendra.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        client_token: Optional[
            "capo_kendra.types.client_token_name.ClientTokenName"
        ] = None,
        tags: Optional["capo_kendra.types.tag_list.TagList"] = None,
        user_token_configurations: Optional[
            "capo_kendra.types.user_token_configuration_list.UserTokenConfigurationList"
        ] = None,
        user_context_policy: Optional[
            "capo_kendra.types.user_context_policy.UserContextPolicy"
        ] = None,
        user_group_resolution_configuration: Optional[
            "capo_kendra.types.user_group_resolution_configuration.UserGroupResolutionConfiguration"
        ] = None,
    ) -> "capo_kendra.types.create_index_response.CreateIndexResponse":
        """<p>Creates an Amazon Kendra index. Index creation is an asynchronous API. To determine if index creation has completed, check the <code>Status</code> field returned from a call to <code>DescribeIndex</code>. The <code>Status</code> field is set to <code>ACTIVE</code> when the index is ready to use.</p> <p>Once the index is active, you can index your documents using the <code>BatchPutDocument</code> API or using one of the supported <a href="https://docs.aws.amazon.com/kendra/latest/dg/data-sources.html">data sources</a>.</p> <p>For an example of creating an index and data source using the Python SDK, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/gs-python.html">Getting started with Python SDK</a>. For an example of creating an index and data source using the Java SDK, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/gs-java.html">Getting started with Java SDK</a>.</p>

        Args:
            name: <p>A name for the index.</p>
            edition: <p>The Amazon Kendra edition to use for the index. Choose <code>DEVELOPER_EDITION</code> for indexes intended for development, testing, or proof of concept. Use <code>ENTERPRISE_EDITION</code> for production. Use <code>GEN_AI_ENTERPRISE_EDITION</code> for creating generative AI applications. Once you set the edition for an index, it can't be changed. </p> <p>The <code>Edition</code> parameter is optional. If you don't supply a value, the default is <code>ENTERPRISE_EDITION</code>.</p> <p>For more information on quota limits for Gen AI Enterprise Edition, Enterprise Edition, and Developer Edition indices, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access your Amazon CloudWatch logs and metrics. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM access roles for Amazon Kendra</a>.</p>
            server_side_encryption_configuration: <p>The identifier of the KMS customer managed key (CMK) that's used to encrypt data indexed by Amazon Kendra. Amazon Kendra doesn't support asymmetric CMKs.</p>
            description: <p>A description for the index.</p>
            client_token: <p>A token that you provide to identify the request to create an index. Multiple calls to the <code>CreateIndex</code> API with the same client token will create only one index.</p>
            tags: <p>A list of key-value pairs that identify or categorize the index. You can also use tags to help control access to the index. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            user_token_configurations: <p>The user token configuration.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>UserTokenConfigurations</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important>
            user_context_policy: <p>The user context policy.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, you can only use <code>ATTRIBUTE_FILTER</code> to filter search results by user context. If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>USER_TOKEN</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important> <dl> <dt>ATTRIBUTE_FILTER</dt> <dd> <p>All indexed content is searchable and displayable for all users. If you want to filter search results on user context, you can use the attribute filters of <code>_user_id</code> and <code>_group_ids</code> or you can provide user and group information in <code>UserContext</code>. </p> </dd> <dt>USER_TOKEN</dt> <dd> <p>Enables token-based user access control to filter search results on user context. All documents with no access control and all documents accessible to the user will be searchable and displayable. </p> </dd> </dl>
            user_group_resolution_configuration: <p>Gets users and groups from IAM Identity Center identity source. To configure this, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_UserGroupResolutionConfiguration.html">UserGroupResolutionConfiguration</a>. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, <code>UserGroupResolutionConfiguration</code> isn't supported.</p> </important>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_already_exist_exception.ResourceAlreadyExistException: <p>The resource you want to use already exists. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.create_index_request.CreateIndexRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.create_index_response.CreateIndexResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.create_index

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.create_index.create_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.create_index_request.CreateIndexRequest = {
            "name": name,
            "role_arn": role_arn,
        }
        if edition is not None:
            input_["edition"] = edition
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if user_token_configurations is not None:
            input_["user_token_configurations"] = user_token_configurations
        if user_context_policy is not None:
            input_["user_context_policy"] = user_context_policy
        if user_group_resolution_configuration is not None:
            input_["user_group_resolution_configuration"] = (
                user_group_resolution_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_query_suggestions_block_list(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        name: "capo_kendra.types.query_suggestions_block_list_name.QuerySuggestionsBlockListName",
        source_s3_path: "capo_kendra.types.s3_path.S3Path",
        role_arn: "capo_kendra.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        client_token: Optional[
            "capo_kendra.types.client_token_name.ClientTokenName"
        ] = None,
        tags: Optional["capo_kendra.types.tag_list.TagList"] = None,
    ) -> "capo_kendra.types.create_query_suggestions_block_list_response.CreateQuerySuggestionsBlockListResponse":
        """<p>Creates a block list to exlcude certain queries from suggestions.</p> <p>Any query that contains words or phrases specified in the block list is blocked or filtered out from being shown as a suggestion.</p> <p>You need to provide the file location of your block list text file in your S3 bucket. In your text file, enter each block word or phrase on a separate line.</p> <p>For information on the current quota limits for block lists, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas for Amazon Kendra</a>.</p> <p> <code>CreateQuerySuggestionsBlockList</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p> <p>For an example of creating a block list for query suggestions using the Python SDK, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions.html#query-suggestions-blocklist">Query suggestions block list</a>.</p>

        Args:
            index_id: <p>The identifier of the index you want to create a query suggestions block list for.</p>
            name: <p>A name for the block list.</p> <p>For example, the name 'offensive-words', which includes all offensive words that could appear in user queries and need to be blocked from suggestions.</p>
            description: <p>A description for the block list.</p> <p>For example, the description "List of all offensive words that can appear in user queries and need to be blocked from suggestions."</p>
            source_s3_path: <p>The S3 path to your block list text file in your S3 bucket.</p> <p>Each block word or phrase should be on a separate line in a text file.</p> <p>For information on the current quota limits for block lists, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas for Amazon Kendra</a>.</p>
            client_token: <p>A token that you provide to identify the request to create a query suggestions block list.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket that contains the block list text file. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM access roles for Amazon Kendra</a>.</p>
            tags: <p>A list of key-value pairs that identify or categorize the block list. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.create_query_suggestions_block_list_request.CreateQuerySuggestionsBlockListRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.create_query_suggestions_block_list_response.CreateQuerySuggestionsBlockListResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.create_query_suggestions_block_list

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.create_query_suggestions_block_list.create_query_suggestions_block_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.create_query_suggestions_block_list_request.CreateQuerySuggestionsBlockListRequest = {
            "index_id": index_id,
            "name": name,
            "source_s3_path": source_s3_path,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_thesaurus(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        name: "capo_kendra.types.thesaurus_name.ThesaurusName",
        role_arn: "capo_kendra.types.role_arn.RoleArn",
        source_s3_path: "capo_kendra.types.s3_path.S3Path",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        tags: Optional["capo_kendra.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_kendra.types.client_token_name.ClientTokenName"
        ] = None,
    ) -> "capo_kendra.types.create_thesaurus_response.CreateThesaurusResponse":
        """<p>Creates a thesaurus for an index. The thesaurus contains a list of synonyms in Solr format.</p> <p>For an example of adding a thesaurus file to an index, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/index-synonyms-adding-thesaurus-file.html">Adding custom synonyms to an index</a>.</p>

        Args:
            index_id: <p>The identifier of the index for the thesaurus.</p>
            name: <p>A name for the thesaurus.</p>
            description: <p>A description for the thesaurus.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket that contains the thesaurus file. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM access roles for Amazon Kendra</a>.</p>
            tags: <p>A list of key-value pairs that identify or categorize the thesaurus. You can also use tags to help control access to the thesaurus. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            source_s3_path: <p>The path to the thesaurus file in S3.</p>
            client_token: <p>A token that you provide to identify the request to create a thesaurus. Multiple calls to the <code>CreateThesaurus</code> API with the same client token will create only one thesaurus. </p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.create_thesaurus_request.CreateThesaurusRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.create_thesaurus_response.CreateThesaurusResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.create_thesaurus

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.create_thesaurus.create_thesaurus(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.create_thesaurus_request.CreateThesaurusRequest = {
            "index_id": index_id,
            "name": name,
            "role_arn": role_arn,
            "source_s3_path": source_s3_path,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
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

    def delete_access_control_configuration(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        id: "capo_kendra.types.access_control_configuration_id.AccessControlConfigurationId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.delete_access_control_configuration_response.DeleteAccessControlConfigurationResponse":
        """<p>Deletes an access control configuration that you created for your documents in an index. This includes user and group access information for your documents. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>

        Args:
            index_id: <p>The identifier of the index for an access control configuration.</p>
            id: <p>The identifier of the access control configuration you want to delete.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.delete_access_control_configuration_request.DeleteAccessControlConfigurationRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.delete_access_control_configuration_response.DeleteAccessControlConfigurationResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.delete_access_control_configuration

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.delete_access_control_configuration.delete_access_control_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.delete_access_control_configuration_request.DeleteAccessControlConfigurationRequest = {
            "index_id": index_id,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_source(
        self,
        id: "capo_kendra.types.data_source_id.DataSourceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> None:
        """<p>Deletes an Amazon Kendra data source connector. An exception is not thrown if the data source is already being deleted. While the data source is being deleted, the <code>Status</code> field returned by a call to the <code>DescribeDataSource</code> API is set to <code>DELETING</code>. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/delete-data-source.html">Deleting Data Sources</a>.</p> <p>Deleting an entire data source or re-syncing your index after deleting specific documents from a data source could take up to an hour or more, depending on the number of documents you want to delete.</p>

        Args:
            id: <p>The identifier of the data source connector you want to delete.</p>
            index_id: <p>The identifier of the index used with the data source connector.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.delete_data_source_request.DeleteDataSourceRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.delete_data_source

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.delete_data_source.delete_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.delete_data_source_request.DeleteDataSourceRequest = {
            "id": id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_experience(
        self,
        id: "capo_kendra.types.experience_id.ExperienceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.delete_experience_response.DeleteExperienceResponse":
        """<p>Deletes your Amazon Kendra experience such as a search application. For more information on creating a search application experience, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html">Building a search experience with no code</a>.</p>

        Args:
            id: <p>The identifier of your Amazon Kendra experience you want to delete.</p>
            index_id: <p>The identifier of the index for your Amazon Kendra experience.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.delete_experience_request.DeleteExperienceRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.delete_experience_response.DeleteExperienceResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.delete_experience

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.delete_experience.delete_experience(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.delete_experience_request.DeleteExperienceRequest = {
            "id": id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_faq(
        self,
        id: "capo_kendra.types.faq_id.FaqId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> None:
        """<p>Removes a FAQ from an index.</p>

        Args:
            id: <p>The identifier of the FAQ you want to remove.</p>
            index_id: <p>The identifier of the index for the FAQ.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.delete_faq_request.DeleteFaqRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.delete_faq

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.delete_faq.delete_faq(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.delete_faq_request.DeleteFaqRequest = {
            "id": id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_index(
        self,
        id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> None:
        """<p>Deletes an Amazon Kendra index. An exception is not thrown if the index is already being deleted. While the index is being deleted, the <code>Status</code> field returned by a call to the <code>DescribeIndex</code> API is set to <code>DELETING</code>.</p>

        Args:
            id: <p>The identifier of the index you want to delete.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.delete_index_request.DeleteIndexRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.delete_index

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.delete_index.delete_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.delete_index_request.DeleteIndexRequest = {"id": id}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_principal_mapping(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        group_id: "capo_kendra.types.group_id.GroupId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        data_source_id: Optional[
            "capo_kendra.types.data_source_id.DataSourceId"
        ] = None,
        ordering_id: Optional[
            "capo_kendra.types.principal_ordering_id.PrincipalOrderingId"
        ] = None,
    ) -> None:
        """<p>Deletes a group so that all users that belong to the group can no longer access documents only available to that group.</p> <p>For example, after deleting the group "Summer Interns", all interns who belonged to that group no longer see intern-only documents in their search results.</p> <p>If you want to delete or replace users or sub groups of a group, you need to use the <code>PutPrincipalMapping</code> operation. For example, if a user in the group "Engineering" leaves the engineering team and another user takes their place, you provide an updated list of users or sub groups that belong to the "Engineering" group when calling <code>PutPrincipalMapping</code>. You can update your internal list of users or sub groups and input this list when calling <code>PutPrincipalMapping</code>.</p> <p> <code>DeletePrincipalMapping</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p>The identifier of the index you want to delete a group from.</p>
            data_source_id: <p>The identifier of the data source you want to delete a group from.</p> <p>A group can be tied to multiple data sources. You can delete a group from accessing documents in a certain data source. For example, the groups "Research", "Engineering", and "Sales and Marketing" are all tied to the company's documents stored in the data sources Confluence and Salesforce. You want to delete "Research" and "Engineering" groups from Salesforce, so that these groups cannot access customer-related documents stored in Salesforce. Only "Sales and Marketing" should access documents in the Salesforce data source.</p>
            group_id: <p>The identifier of the group you want to delete.</p>
            ordering_id: <p>The timestamp identifier you specify to ensure Amazon Kendra does not override the latest <code>DELETE</code> action with previous actions. The highest number ID, which is the ordering ID, is the latest action you want to process and apply on top of other actions with lower number IDs. This prevents previous actions with lower number IDs from possibly overriding the latest action.</p> <p>The ordering ID can be the Unix time of the last update you made to a group members list. You would then provide this list when calling <code>PutPrincipalMapping</code>. This ensures your <code>DELETE</code> action for that updated group with the latest members list doesn't get overwritten by earlier <code>DELETE</code> actions for the same group which are yet to be processed.</p> <p>The default ordering ID is the current Unix time in milliseconds that the action was received by Amazon Kendra. </p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.delete_principal_mapping_request.DeletePrincipalMappingRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.delete_principal_mapping

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.delete_principal_mapping.delete_principal_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.delete_principal_mapping_request.DeletePrincipalMappingRequest = {
            "index_id": index_id,
            "group_id": group_id,
        }
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id
        if ordering_id is not None:
            input_["ordering_id"] = ordering_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_query_suggestions_block_list(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        id: "capo_kendra.types.query_suggestions_block_list_id.QuerySuggestionsBlockListId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> None:
        """<p>Deletes a block list used for query suggestions for an index.</p> <p>A deleted block list might not take effect right away. Amazon Kendra needs to refresh the entire suggestions list to add back the queries that were previously blocked.</p> <p> <code>DeleteQuerySuggestionsBlockList</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p>The identifier of the index for the block list.</p>
            id: <p>The identifier of the block list you want to delete.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.delete_query_suggestions_block_list_request.DeleteQuerySuggestionsBlockListRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.delete_query_suggestions_block_list

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.delete_query_suggestions_block_list.delete_query_suggestions_block_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.delete_query_suggestions_block_list_request.DeleteQuerySuggestionsBlockListRequest = {
            "index_id": index_id,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_thesaurus(
        self,
        id: "capo_kendra.types.thesaurus_id.ThesaurusId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> None:
        """<p>Deletes an Amazon Kendra thesaurus. </p>

        Args:
            id: <p>The identifier of the thesaurus you want to delete.</p>
            index_id: <p>The identifier of the index for the thesaurus.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.delete_thesaurus_request.DeleteThesaurusRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.delete_thesaurus

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.delete_thesaurus.delete_thesaurus(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.delete_thesaurus_request.DeleteThesaurusRequest = {
            "id": id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_access_control_configuration(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        id: "capo_kendra.types.access_control_configuration_id.AccessControlConfigurationId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.describe_access_control_configuration_response.DescribeAccessControlConfigurationResponse":
        """<p>Gets information about an access control configuration that you created for your documents in an index. This includes user and group access information for your documents. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>

        Args:
            index_id: <p>The identifier of the index for an access control configuration.</p>
            id: <p>The identifier of the access control configuration you want to get information on.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.describe_access_control_configuration_request.DescribeAccessControlConfigurationRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.describe_access_control_configuration_response.DescribeAccessControlConfigurationResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.describe_access_control_configuration

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.describe_access_control_configuration.describe_access_control_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.describe_access_control_configuration_request.DescribeAccessControlConfigurationRequest = {
            "index_id": index_id,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_data_source(
        self,
        id: "capo_kendra.types.data_source_id.DataSourceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.describe_data_source_response.DescribeDataSourceResponse":
        """<p>Gets information about an Amazon Kendra data source connector.</p>

        Args:
            id: <p>The identifier of the data source connector.</p>
            index_id: <p>The identifier of the index used with the data source connector.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.describe_data_source_request.DescribeDataSourceRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.describe_data_source_response.DescribeDataSourceResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.describe_data_source

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.describe_data_source.describe_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.describe_data_source_request.DescribeDataSourceRequest = {
            "id": id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_experience(
        self,
        id: "capo_kendra.types.experience_id.ExperienceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.describe_experience_response.DescribeExperienceResponse":
        """<p>Gets information about your Amazon Kendra experience such as a search application. For more information on creating a search application experience, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html">Building a search experience with no code</a>.</p>

        Args:
            id: <p>The identifier of your Amazon Kendra experience you want to get information on.</p>
            index_id: <p>The identifier of the index for your Amazon Kendra experience.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.describe_experience_request.DescribeExperienceRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.describe_experience_response.DescribeExperienceResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.describe_experience

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.describe_experience.describe_experience(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.describe_experience_request.DescribeExperienceRequest = {
            "id": id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_faq(
        self,
        id: "capo_kendra.types.faq_id.FaqId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.describe_faq_response.DescribeFaqResponse":
        """<p>Gets information about a FAQ.</p>

        Args:
            id: <p>The identifier of the FAQ you want to get information on.</p>
            index_id: <p>The identifier of the index for the FAQ.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.describe_faq_request.DescribeFaqRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.describe_faq_response.DescribeFaqResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.describe_faq

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.describe_faq.describe_faq(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.describe_faq_request.DescribeFaqRequest = {
            "id": id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_featured_results_set(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        featured_results_set_id: "capo_kendra.types.featured_results_set_id.FeaturedResultsSetId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.describe_featured_results_set_response.DescribeFeaturedResultsSetResponse":
        """<p>Gets information about a set of featured results. Features results are placed above all other results for certain queries. If there's an exact match of a query, then one or more specific documents are featured in the search results.</p>

        Args:
            index_id: <p>The identifier of the index used for featuring results.</p>
            featured_results_set_id: <p>The identifier of the set of featured results that you want to get information on.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.describe_featured_results_set_request.DescribeFeaturedResultsSetRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.describe_featured_results_set_response.DescribeFeaturedResultsSetResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.describe_featured_results_set

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.describe_featured_results_set.describe_featured_results_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.describe_featured_results_set_request.DescribeFeaturedResultsSetRequest = {
            "index_id": index_id,
            "featured_results_set_id": featured_results_set_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_index(
        self,
        id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.describe_index_response.DescribeIndexResponse":
        """<p>Gets information about an Amazon Kendra index.</p>

        Args:
            id: <p>The identifier of the index you want to get information on.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.describe_index_request.DescribeIndexRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.describe_index_response.DescribeIndexResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.describe_index

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.describe_index.describe_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.describe_index_request.DescribeIndexRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_principal_mapping(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        group_id: "capo_kendra.types.group_id.GroupId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        data_source_id: Optional[
            "capo_kendra.types.data_source_id.DataSourceId"
        ] = None,
    ) -> "capo_kendra.types.describe_principal_mapping_response.DescribePrincipalMappingResponse":
        """<p>Describes the processing of <code>PUT</code> and <code>DELETE</code> actions for mapping users to their groups. This includes information on the status of actions currently processing or yet to be processed, when actions were last updated, when actions were received by Amazon Kendra, the latest action that should process and apply after other actions, and useful error messages if an action could not be processed.</p> <p> <code>DescribePrincipalMapping</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p>The identifier of the index required to check the processing of <code>PUT</code> and <code>DELETE</code> actions for mapping users to their groups.</p>
            data_source_id: <p>The identifier of the data source to check the processing of <code>PUT</code> and <code>DELETE</code> actions for mapping users to their groups.</p>
            group_id: <p>The identifier of the group required to check the processing of <code>PUT</code> and <code>DELETE</code> actions for mapping users to their groups.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.describe_principal_mapping_request.DescribePrincipalMappingRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.describe_principal_mapping_response.DescribePrincipalMappingResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.describe_principal_mapping

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.describe_principal_mapping.describe_principal_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.describe_principal_mapping_request.DescribePrincipalMappingRequest = {
            "index_id": index_id,
            "group_id": group_id,
        }
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_query_suggestions_block_list(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        id: "capo_kendra.types.query_suggestions_block_list_id.QuerySuggestionsBlockListId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.describe_query_suggestions_block_list_response.DescribeQuerySuggestionsBlockListResponse":
        """<p>Gets information about a block list used for query suggestions for an index.</p> <p>This is used to check the current settings that are applied to a block list.</p> <p> <code>DescribeQuerySuggestionsBlockList</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p>The identifier of the index for the block list.</p>
            id: <p>The identifier of the block list you want to get information on.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.describe_query_suggestions_block_list_request.DescribeQuerySuggestionsBlockListRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.describe_query_suggestions_block_list_response.DescribeQuerySuggestionsBlockListResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.describe_query_suggestions_block_list

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.describe_query_suggestions_block_list.describe_query_suggestions_block_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.describe_query_suggestions_block_list_request.DescribeQuerySuggestionsBlockListRequest = {
            "index_id": index_id,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_query_suggestions_config(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.describe_query_suggestions_config_response.DescribeQuerySuggestionsConfigResponse":
        """<p>Gets information on the settings of query suggestions for an index.</p> <p>This is used to check the current settings applied to query suggestions.</p> <p> <code>DescribeQuerySuggestionsConfig</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p>The identifier of the index with query suggestions that you want to get information on.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.describe_query_suggestions_config_request.DescribeQuerySuggestionsConfigRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.describe_query_suggestions_config_response.DescribeQuerySuggestionsConfigResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.describe_query_suggestions_config

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.describe_query_suggestions_config.describe_query_suggestions_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.describe_query_suggestions_config_request.DescribeQuerySuggestionsConfigRequest = {
            "index_id": index_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_thesaurus(
        self,
        id: "capo_kendra.types.thesaurus_id.ThesaurusId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.describe_thesaurus_response.DescribeThesaurusResponse":
        """<p>Gets information about an Amazon Kendra thesaurus.</p>

        Args:
            id: <p>The identifier of the thesaurus you want to get information on.</p>
            index_id: <p>The identifier of the index for the thesaurus.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.describe_thesaurus_request.DescribeThesaurusRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.describe_thesaurus_response.DescribeThesaurusResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.describe_thesaurus

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.describe_thesaurus.describe_thesaurus(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.describe_thesaurus_request.DescribeThesaurusRequest = {
            "id": id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_entities_from_experience(
        self,
        id: "capo_kendra.types.experience_id.ExperienceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        entity_list: "capo_kendra.types.disassociate_entity_list.DisassociateEntityList",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.disassociate_entities_from_experience_response.DisassociateEntitiesFromExperienceResponse":
        """<p>Prevents users or groups in your IAM Identity Center identity source from accessing your Amazon Kendra experience. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html">Building a search experience with no code</a>.</p>

        Args:
            id: <p>The identifier of your Amazon Kendra experience.</p>
            index_id: <p>The identifier of the index for your Amazon Kendra experience.</p>
            entity_list: <p>Lists users or groups in your IAM Identity Center identity source.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.disassociate_entities_from_experience_request.DisassociateEntitiesFromExperienceRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.disassociate_entities_from_experience_response.DisassociateEntitiesFromExperienceResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.disassociate_entities_from_experience

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.disassociate_entities_from_experience.disassociate_entities_from_experience(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.disassociate_entities_from_experience_request.DisassociateEntitiesFromExperienceRequest = {
            "id": id,
            "index_id": index_id,
            "entity_list": entity_list,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_personas_from_entities(
        self,
        id: "capo_kendra.types.experience_id.ExperienceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        entity_ids: "capo_kendra.types.entity_ids_list.EntityIdsList",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.disassociate_personas_from_entities_response.DisassociatePersonasFromEntitiesResponse":
        """<p>Removes the specific permissions of users or groups in your IAM Identity Center identity source with access to your Amazon Kendra experience. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html">Building a search experience with no code</a>.</p>

        Args:
            id: <p>The identifier of your Amazon Kendra experience.</p>
            index_id: <p>The identifier of the index for your Amazon Kendra experience.</p>
            entity_ids: <p>The identifiers of users or groups in your IAM Identity Center identity source. For example, user IDs could be user emails.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.disassociate_personas_from_entities_request.DisassociatePersonasFromEntitiesRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.disassociate_personas_from_entities_response.DisassociatePersonasFromEntitiesResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.disassociate_personas_from_entities

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.disassociate_personas_from_entities.disassociate_personas_from_entities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.disassociate_personas_from_entities_request.DisassociatePersonasFromEntitiesRequest = {
            "id": id,
            "index_id": index_id,
            "entity_ids": entity_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_query_suggestions(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        query_text: "capo_kendra.types.suggestion_query_text.SuggestionQueryText",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        max_suggestions_count: Optional["capo_kendra.types.integer.Integer"] = None,
        suggestion_types: Optional[
            "capo_kendra.types.suggestion_types.SuggestionTypes"
        ] = None,
        attribute_suggestions_config: Optional[
            "capo_kendra.types.attribute_suggestions_get_config.AttributeSuggestionsGetConfig"
        ] = None,
    ) -> "capo_kendra.types.get_query_suggestions_response.GetQuerySuggestionsResponse":
        """<p>Fetches the queries that are suggested to your users.</p> <p> <code>GetQuerySuggestions</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p>The identifier of the index you want to get query suggestions from.</p>
            query_text: <p>The text of a user's query to generate query suggestions.</p> <p>A query is suggested if the query prefix matches what a user starts to type as their query.</p> <p>Amazon Kendra does not show any suggestions if a user types fewer than two characters or more than 60 characters. A query must also have at least one search result and contain at least one word of more than four characters.</p>
            max_suggestions_count: <p>The maximum number of query suggestions you want to show to your users.</p>
            suggestion_types: <p>The suggestions type to base query suggestions on. The suggestion types are query history or document fields/attributes. You can set one type or the other.</p> <p>If you set query history as your suggestions type, Amazon Kendra suggests queries relevant to your users based on popular queries in the query history.</p> <p>If you set document fields/attributes as your suggestions type, Amazon Kendra suggests queries relevant to your users based on the contents of document fields.</p>
            attribute_suggestions_config: <p>Configuration information for the document fields/attributes that you want to base query suggestions on.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.get_query_suggestions_request.GetQuerySuggestionsRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.get_query_suggestions_response.GetQuerySuggestionsResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.get_query_suggestions

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.get_query_suggestions.get_query_suggestions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.get_query_suggestions_request.GetQuerySuggestionsRequest = {
            "index_id": index_id,
            "query_text": query_text,
        }
        if max_suggestions_count is not None:
            input_["max_suggestions_count"] = max_suggestions_count
        if suggestion_types is not None:
            input_["suggestion_types"] = suggestion_types
        if attribute_suggestions_config is not None:
            input_["attribute_suggestions_config"] = attribute_suggestions_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_snapshots(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        interval: "capo_kendra.types.interval.Interval",
        metric_type: "capo_kendra.types.metric_type.MetricType",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional["capo_kendra.types.integer.Integer"] = None,
    ) -> "capo_kendra.types.get_snapshots_response.GetSnapshotsResponse":
        """<p>Retrieves search metrics data. The data provides a snapshot of how your users interact with your search application and how effective the application is.</p>

        Args:
            index_id: <p>The identifier of the index to get search metrics data.</p>
            interval: <p>The time interval or time window to get search metrics data. The time interval uses the time zone of your index. You can view data in the following time windows:</p> <ul> <li> <p> <code>THIS_WEEK</code>: The current week, starting on the Sunday and ending on the day before the current date.</p> </li> <li> <p> <code>ONE_WEEK_AGO</code>: The previous week, starting on the Sunday and ending on the following Saturday.</p> </li> <li> <p> <code>TWO_WEEKS_AGO</code>: The week before the previous week, starting on the Sunday and ending on the following Saturday.</p> </li> <li> <p> <code>THIS_MONTH</code>: The current month, starting on the first day of the month and ending on the day before the current date.</p> </li> <li> <p> <code>ONE_MONTH_AGO</code>: The previous month, starting on the first day of the month and ending on the last day of the month.</p> </li> <li> <p> <code>TWO_MONTHS_AGO</code>: The month before the previous month, starting on the first day of the month and ending on last day of the month.</p> </li> </ul>
            metric_type: <p>The metric you want to retrieve. You can specify only one metric per call.</p> <p>For more information about the metrics you can view, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/search-analytics.html">Gaining insights with search analytics</a>.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of search metrics data.</p>
            max_results: <p>The maximum number of returned data for the metric.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.invalid_request_exception.InvalidRequestException: <p>The input to the request is not valid. Please provide the correct input and try again.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.get_snapshots_request.GetSnapshotsRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.get_snapshots_response.GetSnapshotsResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.get_snapshots

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.get_snapshots.get_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.get_snapshots_request.GetSnapshotsRequest = {
            "index_id": index_id,
            "interval": interval,
            "metric_type": metric_type,
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

    def iter_get_snapshots(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        interval: "capo_kendra.types.interval.Interval",
        metric_type: "capo_kendra.types.metric_type.MetricType",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional["capo_kendra.types.integer.Integer"] = None,
    ) -> "Iterator[capo_kendra.types.get_snapshots_response.GetSnapshotsResponse]":
        _token = next_token
        while True:
            _response = self.get_snapshots(
                index_id,
                interval,
                metric_type,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_access_control_configurations(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.string.String"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_access_control_configurations_request.MaxResultsIntegerForListAccessControlConfigurationsRequest"
        ] = None,
    ) -> "capo_kendra.types.list_access_control_configurations_response.ListAccessControlConfigurationsResponse":
        """<p>Lists one or more access control configurations for an index. This includes user and group access information for your documents. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>

        Args:
            index_id: <p>The identifier of the index for the access control configuration.</p>
            next_token: <p>If the previous response was incomplete (because there's more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of access control configurations.</p>
            max_results: <p>The maximum number of access control configurations to return.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_access_control_configurations_request.ListAccessControlConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_access_control_configurations_response.ListAccessControlConfigurationsResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_access_control_configurations

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_access_control_configurations.list_access_control_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_access_control_configurations_request.ListAccessControlConfigurationsRequest = {
            "index_id": index_id
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

    def iter_list_access_control_configurations(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.string.String"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_access_control_configurations_request.MaxResultsIntegerForListAccessControlConfigurationsRequest"
        ] = None,
    ) -> "Iterator[capo_kendra.types.list_access_control_configurations_response.ListAccessControlConfigurationsResponse]":
        _token = next_token
        while True:
            _response = self.list_access_control_configurations(
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_sources(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_data_sources_request.MaxResultsIntegerForListDataSourcesRequest"
        ] = None,
    ) -> "capo_kendra.types.list_data_sources_response.ListDataSourcesResponse":
        """<p>Lists the data source connectors that you have created.</p>

        Args:
            index_id: <p>The identifier of the index used with one or more data source connectors.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of data source connectors. </p>
            max_results: <p>The maximum number of data source connectors to return.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_data_sources_request.ListDataSourcesRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_data_sources_response.ListDataSourcesResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_data_sources

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_data_sources.list_data_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_data_sources_request.ListDataSourcesRequest = {
            "index_id": index_id
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

    def iter_list_data_sources(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_data_sources_request.MaxResultsIntegerForListDataSourcesRequest"
        ] = None,
    ) -> (
        "Iterator[capo_kendra.types.list_data_sources_response.ListDataSourcesResponse]"
    ):
        _token = next_token
        while True:
            _response = self.list_data_sources(
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_source_sync_jobs(
        self,
        id: "capo_kendra.types.data_source_id.DataSourceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_data_source_sync_jobs_request.MaxResultsIntegerForListDataSourceSyncJobsRequest"
        ] = None,
        start_time_filter: Optional["capo_kendra.types.time_range.TimeRange"] = None,
        status_filter: Optional[
            "capo_kendra.types.data_source_sync_job_status.DataSourceSyncJobStatus"
        ] = None,
    ) -> "capo_kendra.types.list_data_source_sync_jobs_response.ListDataSourceSyncJobsResponse":
        """<p>Gets statistics about synchronizing a data source connector.</p>

        Args:
            id: <p>The identifier of the data source connector.</p>
            index_id: <p>The identifier of the index used with the data source connector.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of jobs.</p>
            max_results: <p>The maximum number of synchronization jobs to return in the response. If there are fewer results in the list, this response contains only the actual results.</p>
            start_time_filter: <p>When specified, the synchronization jobs returned in the list are limited to jobs between the specified dates.</p>
            status_filter: <p>Only returns synchronization jobs with the <code>Status</code> field equal to the specified status.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_data_source_sync_jobs_request.ListDataSourceSyncJobsRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_data_source_sync_jobs_response.ListDataSourceSyncJobsResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_data_source_sync_jobs

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_data_source_sync_jobs.list_data_source_sync_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_data_source_sync_jobs_request.ListDataSourceSyncJobsRequest = {
            "id": id,
            "index_id": index_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if start_time_filter is not None:
            input_["start_time_filter"] = start_time_filter
        if status_filter is not None:
            input_["status_filter"] = status_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_data_source_sync_jobs(
        self,
        id: "capo_kendra.types.data_source_id.DataSourceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_data_source_sync_jobs_request.MaxResultsIntegerForListDataSourceSyncJobsRequest"
        ] = None,
        start_time_filter: Optional["capo_kendra.types.time_range.TimeRange"] = None,
        status_filter: Optional[
            "capo_kendra.types.data_source_sync_job_status.DataSourceSyncJobStatus"
        ] = None,
    ) -> "Iterator[capo_kendra.types.list_data_source_sync_jobs_response.ListDataSourceSyncJobsResponse]":
        _token = next_token
        while True:
            _response = self.list_data_source_sync_jobs(
                id,
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                start_time_filter=start_time_filter,
                status_filter=status_filter,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_entity_personas(
        self,
        id: "capo_kendra.types.experience_id.ExperienceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_entity_personas_request.MaxResultsIntegerForListEntityPersonasRequest"
        ] = None,
    ) -> "capo_kendra.types.list_entity_personas_response.ListEntityPersonasResponse":
        """<p>Lists specific permissions of users and groups with access to your Amazon Kendra experience.</p>

        Args:
            id: <p>The identifier of your Amazon Kendra experience.</p>
            index_id: <p>The identifier of the index for your Amazon Kendra experience.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of users or groups.</p>
            max_results: <p>The maximum number of returned users or groups.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_entity_personas_request.ListEntityPersonasRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_entity_personas_response.ListEntityPersonasResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_entity_personas

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_entity_personas.list_entity_personas(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_entity_personas_request.ListEntityPersonasRequest = {
            "id": id,
            "index_id": index_id,
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

    def iter_list_entity_personas(
        self,
        id: "capo_kendra.types.experience_id.ExperienceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_entity_personas_request.MaxResultsIntegerForListEntityPersonasRequest"
        ] = None,
    ) -> "Iterator[capo_kendra.types.list_entity_personas_response.ListEntityPersonasResponse]":
        _token = next_token
        while True:
            _response = self.list_entity_personas(
                id,
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_experience_entities(
        self,
        id: "capo_kendra.types.experience_id.ExperienceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
    ) -> "capo_kendra.types.list_experience_entities_response.ListExperienceEntitiesResponse":
        """<p>Lists users or groups in your IAM Identity Center identity source that are granted access to your Amazon Kendra experience. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html">Building a search experience with no code</a>.</p>

        Args:
            id: <p>The identifier of your Amazon Kendra experience.</p>
            index_id: <p>The identifier of the index for your Amazon Kendra experience.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of users or groups.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_experience_entities_request.ListExperienceEntitiesRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_experience_entities_response.ListExperienceEntitiesResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_experience_entities

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_experience_entities.list_experience_entities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_experience_entities_request.ListExperienceEntitiesRequest = {
            "id": id,
            "index_id": index_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_experience_entities(
        self,
        id: "capo_kendra.types.experience_id.ExperienceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_kendra.types.list_experience_entities_response.ListExperienceEntitiesResponse]":
        _token = next_token
        while True:
            _response = self.list_experience_entities(
                id,
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_experiences(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_experiences_request.MaxResultsIntegerForListExperiencesRequest"
        ] = None,
    ) -> "capo_kendra.types.list_experiences_response.ListExperiencesResponse":
        """<p>Lists one or more Amazon Kendra experiences. You can create an Amazon Kendra experience such as a search application. For more information on creating a search application experience, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html">Building a search experience with no code</a>.</p>

        Args:
            index_id: <p>The identifier of the index for your Amazon Kendra experience.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Kendra experiences.</p>
            max_results: <p>The maximum number of returned Amazon Kendra experiences.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_experiences_request.ListExperiencesRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_experiences_response.ListExperiencesResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_experiences

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_experiences.list_experiences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_experiences_request.ListExperiencesRequest = {
            "index_id": index_id
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

    def iter_list_experiences(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_experiences_request.MaxResultsIntegerForListExperiencesRequest"
        ] = None,
    ) -> (
        "Iterator[capo_kendra.types.list_experiences_response.ListExperiencesResponse]"
    ):
        _token = next_token
        while True:
            _response = self.list_experiences(
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_faqs(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_faqs_request.MaxResultsIntegerForListFaqsRequest"
        ] = None,
    ) -> "capo_kendra.types.list_faqs_response.ListFaqsResponse":
        """<p>Gets a list of FAQs associated with an index.</p>

        Args:
            index_id: <p>The index for the FAQs.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of FAQs.</p>
            max_results: <p>The maximum number of FAQs to return in the response. If there are fewer results in the list, this response contains only the actual results.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_faqs_request.ListFaqsRequest]",
        ) -> OperationResponse["capo_kendra.types.list_faqs_response.ListFaqsResponse"]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_faqs

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_faqs.list_faqs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_faqs_request.ListFaqsRequest = {
            "index_id": index_id
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

    def iter_list_faqs(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_faqs_request.MaxResultsIntegerForListFaqsRequest"
        ] = None,
    ) -> "Iterator[capo_kendra.types.list_faqs_response.ListFaqsResponse]":
        _token = next_token
        while True:
            _response = self.list_faqs(
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_featured_results_sets(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_featured_results_sets_request.MaxResultsIntegerForListFeaturedResultsSetsRequest"
        ] = None,
    ) -> "capo_kendra.types.list_featured_results_sets_response.ListFeaturedResultsSetsResponse":
        """<p>Lists all your sets of featured results for a given index. Features results are placed above all other results for certain queries. If there's an exact match of a query, then one or more specific documents are featured in the search results.</p>

        Args:
            index_id: <p>The identifier of the index used for featuring results.</p>
            next_token: <p>If the response is truncated, Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of featured results sets.</p>
            max_results: <p>The maximum number of featured results sets to return.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_featured_results_sets_request.ListFeaturedResultsSetsRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_featured_results_sets_response.ListFeaturedResultsSetsResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_featured_results_sets

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_featured_results_sets.list_featured_results_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_featured_results_sets_request.ListFeaturedResultsSetsRequest = {
            "index_id": index_id
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

    def list_groups_older_than_ordering_id(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        ordering_id: "capo_kendra.types.principal_ordering_id.PrincipalOrderingId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        data_source_id: Optional[
            "capo_kendra.types.data_source_id.DataSourceId"
        ] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_principals_request.MaxResultsIntegerForListPrincipalsRequest"
        ] = None,
    ) -> "capo_kendra.types.list_groups_older_than_ordering_id_response.ListGroupsOlderThanOrderingIdResponse":
        """<p>Provides a list of groups that are mapped to users before a given ordering or timestamp identifier.</p> <p> <code>ListGroupsOlderThanOrderingId</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p>The identifier of the index for getting a list of groups mapped to users before a given ordering or timestamp identifier.</p>
            data_source_id: <p>The identifier of the data source for getting a list of groups mapped to users before a given ordering timestamp identifier.</p>
            ordering_id: <p>The timestamp identifier used for the latest <code>PUT</code> or <code>DELETE</code> action for mapping users to their groups.</p>
            next_token: <p> If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of groups that are mapped to users before a given ordering or timestamp identifier. </p>
            max_results: <p> The maximum number of returned groups that are mapped to users before a given ordering or timestamp identifier. </p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_groups_older_than_ordering_id_request.ListGroupsOlderThanOrderingIdRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_groups_older_than_ordering_id_response.ListGroupsOlderThanOrderingIdResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_groups_older_than_ordering_id

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_groups_older_than_ordering_id.list_groups_older_than_ordering_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_groups_older_than_ordering_id_request.ListGroupsOlderThanOrderingIdRequest = {
            "index_id": index_id,
            "ordering_id": ordering_id,
        }
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id
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

    def iter_list_groups_older_than_ordering_id(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        ordering_id: "capo_kendra.types.principal_ordering_id.PrincipalOrderingId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        data_source_id: Optional[
            "capo_kendra.types.data_source_id.DataSourceId"
        ] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_principals_request.MaxResultsIntegerForListPrincipalsRequest"
        ] = None,
    ) -> "Iterator[capo_kendra.types.list_groups_older_than_ordering_id_response.ListGroupsOlderThanOrderingIdResponse]":
        _token = next_token
        while True:
            _response = self.list_groups_older_than_ordering_id(
                index_id,
                ordering_id,
                config_overrides=config_overrides,
                data_source_id=data_source_id,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_indices(
        self,
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_indices_request.MaxResultsIntegerForListIndicesRequest"
        ] = None,
    ) -> "capo_kendra.types.list_indices_response.ListIndicesResponse":
        """<p>Lists the Amazon Kendra indexes that you created.</p>

        Args:
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of indexes. </p>
            max_results: <p>The maximum number of indices to return.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_indices_request.ListIndicesRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_indices_response.ListIndicesResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_indices

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_indices.list_indices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_indices_request.ListIndicesRequest = {}
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

    def iter_list_indices(
        self,
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_indices_request.MaxResultsIntegerForListIndicesRequest"
        ] = None,
    ) -> "Iterator[capo_kendra.types.list_indices_response.ListIndicesResponse]":
        _token = next_token
        while True:
            _response = self.list_indices(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_query_suggestions_block_lists(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_query_suggestions_block_lists.MaxResultsIntegerForListQuerySuggestionsBlockLists"
        ] = None,
    ) -> "capo_kendra.types.list_query_suggestions_block_lists_response.ListQuerySuggestionsBlockListsResponse":
        """<p>Lists the block lists used for query suggestions for an index.</p> <p>For information on the current quota limits for block lists, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas for Amazon Kendra</a>.</p> <p> <code>ListQuerySuggestionsBlockLists</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p>The identifier of the index for a list of all block lists that exist for that index.</p> <p>For information on the current quota limits for block lists, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas for Amazon Kendra</a>.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of block lists (<code>BlockListSummaryItems</code>).</p>
            max_results: <p>The maximum number of block lists to return.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_query_suggestions_block_lists_request.ListQuerySuggestionsBlockListsRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_query_suggestions_block_lists_response.ListQuerySuggestionsBlockListsResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_query_suggestions_block_lists

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_query_suggestions_block_lists.list_query_suggestions_block_lists(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_query_suggestions_block_lists_request.ListQuerySuggestionsBlockListsRequest = {
            "index_id": index_id
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

    def iter_list_query_suggestions_block_lists(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_query_suggestions_block_lists.MaxResultsIntegerForListQuerySuggestionsBlockLists"
        ] = None,
    ) -> "Iterator[capo_kendra.types.list_query_suggestions_block_lists_response.ListQuerySuggestionsBlockListsResponse]":
        _token = next_token
        while True:
            _response = self.list_query_suggestions_block_lists(
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_kendra.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> (
        "capo_kendra.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Gets a list of tags associated with a resource. Indexes, FAQs, data sources, and other resources can have tags associated with them.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the index, FAQ, data source, or other resource to get a list of tags for. For example, the ARN of an index is constructed as follows: <i>arn:aws:kendra:your-region:your-account-id:index/index-id</i> For information on how to construct an ARN for all types of Amazon Kendra resources, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkendra.html#amazonkendra-resources-for-iam-policies">Resource types</a>.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The resource you want to use isn't available. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_tags_for_resource

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_thesauri(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_thesauri_request.MaxResultsIntegerForListThesauriRequest"
        ] = None,
    ) -> "capo_kendra.types.list_thesauri_response.ListThesauriResponse":
        """<p>Lists the thesauri for an index.</p>

        Args:
            index_id: <p>The identifier of the index with one or more thesauri.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of thesauri (<code>ThesaurusSummaryItems</code>). </p>
            max_results: <p>The maximum number of thesauri to return.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.list_thesauri_request.ListThesauriRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.list_thesauri_response.ListThesauriResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.list_thesauri

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.list_thesauri.list_thesauri(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.list_thesauri_request.ListThesauriRequest = {
            "index_id": index_id
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

    def iter_list_thesauri(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        next_token: Optional["capo_kendra.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_kendra.types.max_results_integer_for_list_thesauri_request.MaxResultsIntegerForListThesauriRequest"
        ] = None,
    ) -> "Iterator[capo_kendra.types.list_thesauri_response.ListThesauriResponse]":
        _token = next_token
        while True:
            _response = self.list_thesauri(
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_principal_mapping(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        group_id: "capo_kendra.types.group_id.GroupId",
        group_members: "capo_kendra.types.group_members.GroupMembers",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        data_source_id: Optional[
            "capo_kendra.types.data_source_id.DataSourceId"
        ] = None,
        ordering_id: Optional[
            "capo_kendra.types.principal_ordering_id.PrincipalOrderingId"
        ] = None,
        role_arn: Optional["capo_kendra.types.role_arn.RoleArn"] = None,
    ) -> None:
        """<p>Maps users to their groups so that you only need to provide the user ID when you issue the query.</p> <p>You can also map sub groups to groups. For example, the group "Company Intellectual Property Teams" includes sub groups "Research" and "Engineering". These sub groups include their own list of users or people who work in these teams. Only users who work in research and engineering, and therefore belong in the intellectual property group, can see top-secret company documents in their search results.</p> <p>This is useful for user context filtering, where search results are filtered based on the user or their group access to documents. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html">Filtering on user context</a>.</p> <p>If more than five <code>PUT</code> actions for a group are currently processing, a validation exception is thrown.</p>

        Args:
            index_id: <p>The identifier of the index you want to map users to their groups.</p>
            data_source_id: <p>The identifier of the data source you want to map users to their groups.</p> <p>This is useful if a group is tied to multiple data sources, but you only want the group to access documents of a certain data source. For example, the groups "Research", "Engineering", and "Sales and Marketing" are all tied to the company's documents stored in the data sources Confluence and Salesforce. However, "Sales and Marketing" team only needs access to customer-related documents stored in Salesforce.</p>
            group_id: <p>The identifier of the group you want to map its users to.</p>
            group_members: <p>The list that contains your users that belong the same group. This can include sub groups that belong to a group.</p> <p>For example, the group "Company A" includes the user "CEO" and the sub groups "Research", "Engineering", and "Sales and Marketing".</p> <p>If you have more than 1000 users and/or sub groups for a single group, you need to provide the path to the S3 file that lists your users and sub groups for a group. Your sub groups can contain more than 1000 users, but the list of sub groups that belong to a group (and/or users) must be no more than 1000.</p>
            ordering_id: <p>The timestamp identifier you specify to ensure Amazon Kendra doesn't override the latest <code>PUT</code> action with previous actions. The highest number ID, which is the ordering ID, is the latest action you want to process and apply on top of other actions with lower number IDs. This prevents previous actions with lower number IDs from possibly overriding the latest action.</p> <p>The ordering ID can be the Unix time of the last update you made to a group members list. You would then provide this list when calling <code>PutPrincipalMapping</code>. This ensures your <code>PUT</code> action for that updated group with the latest members list doesn't get overwritten by earlier <code>PUT</code> actions for the same group which are yet to be processed.</p> <p>The default ordering ID is the current Unix time in milliseconds that the action was received by Amazon Kendra.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that has access to the S3 file that contains your list of users that belong to a group.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html#iam-roles-ds">IAM roles for Amazon Kendra</a>.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.put_principal_mapping_request.PutPrincipalMappingRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.put_principal_mapping

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.put_principal_mapping.put_principal_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.put_principal_mapping_request.PutPrincipalMappingRequest = {
            "index_id": index_id,
            "group_id": group_id,
            "group_members": group_members,
        }
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id
        if ordering_id is not None:
            input_["ordering_id"] = ordering_id
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def query(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        query_text: Optional["capo_kendra.types.query_text.QueryText"] = None,
        attribute_filter: Optional[
            "capo_kendra.types.attribute_filter.AttributeFilter"
        ] = None,
        facets: Optional["capo_kendra.types.facet_list.FacetList"] = None,
        requested_document_attributes: Optional[
            "capo_kendra.types.document_attribute_key_list.DocumentAttributeKeyList"
        ] = None,
        query_result_type_filter: Optional[
            "capo_kendra.types.query_result_type.QueryResultType"
        ] = None,
        document_relevance_override_configurations: Optional[
            "capo_kendra.types.document_relevance_override_configuration_list.DocumentRelevanceOverrideConfigurationList"
        ] = None,
        page_number: Optional["capo_kendra.types.integer.Integer"] = None,
        page_size: Optional["capo_kendra.types.integer.Integer"] = None,
        sorting_configuration: Optional[
            "capo_kendra.types.sorting_configuration.SortingConfiguration"
        ] = None,
        sorting_configurations: Optional[
            "capo_kendra.types.sorting_configuration_list.SortingConfigurationList"
        ] = None,
        user_context: Optional["capo_kendra.types.user_context.UserContext"] = None,
        visitor_id: Optional["capo_kendra.types.visitor_id.VisitorId"] = None,
        spell_correction_configuration: Optional[
            "capo_kendra.types.spell_correction_configuration.SpellCorrectionConfiguration"
        ] = None,
        collapse_configuration: Optional[
            "capo_kendra.types.collapse_configuration.CollapseConfiguration"
        ] = None,
    ) -> "capo_kendra.types.query_result.QueryResult":
        """<p>Searches an index given an input query.</p> <note> <p>If you are working with large language models (LLMs) or implementing retrieval augmented generation (RAG) systems, you can use Amazon Kendra's <a href="https://docs.aws.amazon.com/kendra/latest/APIReference/API_Retrieve.html">Retrieve</a> API, which can return longer semantically relevant passages. We recommend using the <code>Retrieve</code> API instead of filing a service limit increase to increase the <code>Query</code> API document excerpt length.</p> </note> <p>You can configure boosting or relevance tuning at the query level to override boosting at the index level, filter based on document fields/attributes and faceted search, and filter based on the user or their group access to documents. You can also include certain fields in the response that might provide useful additional information.</p> <p>A query response contains three types of results.</p> <ul> <li> <p>Relevant suggested answers. The answers can be either a text excerpt or table excerpt. The answer can be highlighted in the excerpt.</p> </li> <li> <p>Matching FAQs or questions-answer from your FAQ file.</p> </li> <li> <p>Relevant documents. This result type includes an excerpt of the document with the document title. The searched terms can be highlighted in the excerpt.</p> </li> </ul> <p>You can specify that the query return only one type of result using the <code>QueryResultTypeFilter</code> parameter. Each query returns the 100 most relevant results. If you filter result type to only question-answers, a maximum of four results are returned. If you filter result type to only answers, a maximum of three results are returned.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, you can only use <code>ATTRIBUTE_FILTER</code> to filter search results by user context. If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>USER_TOKEN</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important>

        Args:
            index_id: <p>The identifier of the index for the search.</p>
            query_text: <p>The input query text for the search. Amazon Kendra truncates queries at 30 token words, which excludes punctuation and stop words. Truncation still applies if you use Boolean or more advanced, complex queries. For example, <code>Timeoff AND October AND Category:HR</code> is counted as 3 tokens: <code>timeoff</code>, <code>october</code>, <code>hr</code>. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax">Searching with advanced query syntax</a> in the Amazon Kendra Developer Guide. </p>
            attribute_filter: <p>Filters search results by document fields/attributes. You can only provide one attribute filter; however, the <code>AndAllFilters</code>, <code>NotFilter</code>, and <code>OrAllFilters</code> parameters contain a list of other filters.</p> <p>The <code>AttributeFilter</code> parameter means you can create a set of filtering rules that a document must satisfy to be included in the query results.</p> <note> <p>For Amazon Kendra Gen AI Enterprise Edition indices use <code>AttributeFilter</code> to enable document filtering for end users using <code>_email_id</code> or include public documents (<code>_email_id=null</code>).</p> </note>
            facets: <p>An array of documents fields/attributes for faceted search. Amazon Kendra returns a count for each field key specified. This helps your users narrow their search.</p>
            requested_document_attributes: <p>An array of document fields/attributes to include in the response. You can limit the response to include certain document fields. By default, all document attributes are included in the response.</p>
            query_result_type_filter: <p>Sets the type of query result or response. Only results for the specified type are returned.</p>
            document_relevance_override_configurations: <p>Overrides relevance tuning configurations of fields/attributes set at the index level.</p> <p>If you use this API to override the relevance tuning configured at the index level, but there is no relevance tuning configured at the index level, then Amazon Kendra does not apply any relevance tuning.</p> <p>If there is relevance tuning configured for fields at the index level, and you use this API to override only some of these fields, then for the fields you did not override, the importance is set to 1.</p>
            page_number: <p>Query results are returned in pages the size of the <code>PageSize</code> parameter. By default, Amazon Kendra returns the first page of results. Use this parameter to get result pages after the first one.</p>
            page_size: <p>Sets the number of results that are returned in each page of results. The default page size is 10. The maximum number of results returned is 100. If you ask for more than 100 results, only 100 are returned.</p>
            sorting_configuration: <p>Provides information that determines how the results of the query are sorted. You can set the field that Amazon Kendra should sort the results on, and specify whether the results should be sorted in ascending or descending order. In the case of ties in sorting the results, the results are sorted by relevance.</p> <p>If you don't provide sorting configuration, the results are sorted by the relevance that Amazon Kendra determines for the result.</p>
            sorting_configurations: <p>Provides configuration information to determine how the results of a query are sorted.</p> <p>You can set upto 3 fields that Amazon Kendra should sort the results on, and specify whether the results should be sorted in ascending or descending order. The sort field quota can be increased.</p> <p>If you don't provide a sorting configuration, the results are sorted by the relevance that Amazon Kendra determines for the result. In the case of ties in sorting the results, the results are sorted by relevance. </p>
            user_context: <p>The user context token or user and group information.</p>
            visitor_id: <p>Provides an identifier for a specific user. The <code>VisitorId</code> should be a unique identifier, such as a GUID. Don't use personally identifiable information, such as the user's email address, as the <code>VisitorId</code>.</p>
            spell_correction_configuration: <p>Enables suggested spell corrections for queries.</p>
            collapse_configuration: <p>Provides configuration to determine how to group results by document attribute value, and how to display them (collapsed or expanded) under a designated primary document for each group.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.query_request.QueryRequest]",
        ) -> OperationResponse["capo_kendra.types.query_result.QueryResult"]:
            import capo_kendra._operations.aws_kendra_frontend_service.query

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.query.query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.query_request.QueryRequest = {"index_id": index_id}
        if query_text is not None:
            input_["query_text"] = query_text
        if attribute_filter is not None:
            input_["attribute_filter"] = attribute_filter
        if facets is not None:
            input_["facets"] = facets
        if requested_document_attributes is not None:
            input_["requested_document_attributes"] = requested_document_attributes
        if query_result_type_filter is not None:
            input_["query_result_type_filter"] = query_result_type_filter
        if document_relevance_override_configurations is not None:
            input_["document_relevance_override_configurations"] = (
                document_relevance_override_configurations
            )
        if page_number is not None:
            input_["page_number"] = page_number
        if page_size is not None:
            input_["page_size"] = page_size
        if sorting_configuration is not None:
            input_["sorting_configuration"] = sorting_configuration
        if sorting_configurations is not None:
            input_["sorting_configurations"] = sorting_configurations
        if user_context is not None:
            input_["user_context"] = user_context
        if visitor_id is not None:
            input_["visitor_id"] = visitor_id
        if spell_correction_configuration is not None:
            input_["spell_correction_configuration"] = spell_correction_configuration
        if collapse_configuration is not None:
            input_["collapse_configuration"] = collapse_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def retrieve(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        query_text: "capo_kendra.types.query_text.QueryText",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        attribute_filter: Optional[
            "capo_kendra.types.attribute_filter.AttributeFilter"
        ] = None,
        requested_document_attributes: Optional[
            "capo_kendra.types.document_attribute_key_list.DocumentAttributeKeyList"
        ] = None,
        document_relevance_override_configurations: Optional[
            "capo_kendra.types.document_relevance_override_configuration_list.DocumentRelevanceOverrideConfigurationList"
        ] = None,
        page_number: Optional["capo_kendra.types.integer.Integer"] = None,
        page_size: Optional["capo_kendra.types.integer.Integer"] = None,
        user_context: Optional["capo_kendra.types.user_context.UserContext"] = None,
    ) -> "capo_kendra.types.retrieve_result.RetrieveResult":
        """<p>Retrieves relevant passages or text excerpts given an input query.</p> <p>This API is similar to the <a href="https://docs.aws.amazon.com/kendra/latest/APIReference/API_Query.html">Query</a> API. However, by default, the <code>Query</code> API only returns excerpt passages of up to 100 token words. With the <code>Retrieve</code> API, you can retrieve longer passages of up to 200 token words and up to 100 semantically relevant passages. This doesn't include question-answer or FAQ type responses from your index. The passages are text excerpts that can be semantically extracted from multiple documents and multiple parts of the same document. If in extreme cases your documents produce zero passages using the <code>Retrieve</code> API, you can alternatively use the <code>Query</code> API and its types of responses.</p> <p>You can also do the following:</p> <ul> <li> <p>Override boosting at the index level</p> </li> <li> <p>Filter based on document fields or attributes</p> </li> <li> <p>Filter based on the user or their group access to documents</p> </li> <li> <p>View the confidence score bucket for a retrieved passage result. The confidence bucket provides a relative ranking that indicates how confident Amazon Kendra is that the response is relevant to the query.</p> <note> <p>Confidence score buckets are currently available only for English.</p> </note> </li> </ul> <p>You can also include certain fields in the response that might provide useful additional information.</p> <p>The <code>Retrieve</code> API shares the number of <a href="https://docs.aws.amazon.com/kendra/latest/APIReference/API_CapacityUnitsConfiguration.html">query capacity units</a> that you set for your index. For more information on what's included in a single capacity unit and the default base capacity for an index, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html">Adjusting capacity</a>.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, you can only use <code>ATTRIBUTE_FILTER</code> to filter search results by user context. If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>USER_TOKEN</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important>

        Args:
            index_id: <p>The identifier of the index to retrieve relevant passages for the search.</p>
            query_text: <p>The input query text to retrieve relevant passages for the search. Amazon Kendra truncates queries at 30 token words, which excludes punctuation and stop words. Truncation still applies if you use Boolean or more advanced, complex queries. For example, <code>Timeoff AND October AND Category:HR</code> is counted as 3 tokens: <code>timeoff</code>, <code>october</code>, <code>hr</code>. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/searching-example.html#searching-index-query-syntax">Searching with advanced query syntax</a> in the Amazon Kendra Developer Guide. </p>
            attribute_filter: <p>Filters search results by document fields/attributes. You can only provide one attribute filter; however, the <code>AndAllFilters</code>, <code>NotFilter</code>, and <code>OrAllFilters</code> parameters contain a list of other filters.</p> <p>The <code>AttributeFilter</code> parameter means you can create a set of filtering rules that a document must satisfy to be included in the query results.</p> <note> <p>For Amazon Kendra Gen AI Enterprise Edition indices use <code>AttributeFilter</code> to enable document filtering for end users using <code>_email_id</code> or include public documents (<code>_email_id=null</code>).</p> </note>
            requested_document_attributes: <p>A list of document fields/attributes to include in the response. You can limit the response to include certain document fields. By default, all document fields are included in the response.</p>
            document_relevance_override_configurations: <p>Overrides relevance tuning configurations of fields/attributes set at the index level.</p> <p>If you use this API to override the relevance tuning configured at the index level, but there is no relevance tuning configured at the index level, then Amazon Kendra does not apply any relevance tuning.</p> <p>If there is relevance tuning configured for fields at the index level, and you use this API to override only some of these fields, then for the fields you did not override, the importance is set to 1.</p>
            page_number: <p>Retrieved relevant passages are returned in pages the size of the <code>PageSize</code> parameter. By default, Amazon Kendra returns the first page of results. Use this parameter to get result pages after the first one.</p>
            page_size: <p>Sets the number of retrieved relevant passages that are returned in each page of results. The default page size is 10. The maximum number of results returned is 100. If you ask for more than 100 results, only 100 are returned.</p>
            user_context: <p>The user context token or user and group information.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.retrieve_request.RetrieveRequest]",
        ) -> OperationResponse["capo_kendra.types.retrieve_result.RetrieveResult"]:
            import capo_kendra._operations.aws_kendra_frontend_service.retrieve

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.retrieve.retrieve(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.retrieve_request.RetrieveRequest = {
            "index_id": index_id,
            "query_text": query_text,
        }
        if attribute_filter is not None:
            input_["attribute_filter"] = attribute_filter
        if requested_document_attributes is not None:
            input_["requested_document_attributes"] = requested_document_attributes
        if document_relevance_override_configurations is not None:
            input_["document_relevance_override_configurations"] = (
                document_relevance_override_configurations
            )
        if page_number is not None:
            input_["page_number"] = page_number
        if page_size is not None:
            input_["page_size"] = page_size
        if user_context is not None:
            input_["user_context"] = user_context

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_data_source_sync_job(
        self,
        id: "capo_kendra.types.data_source_id.DataSourceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.start_data_source_sync_job_response.StartDataSourceSyncJobResponse":
        """<p>Starts a synchronization job for a data source connector. If a synchronization job is already in progress, Amazon Kendra returns a <code>ResourceInUseException</code> exception.</p> <p>Re-syncing your data source with your index after modifying, adding, or deleting documents from your data source respository could take up to an hour or more, depending on the number of documents to sync.</p>

        Args:
            id: <p>The identifier of the data source connector to synchronize.</p>
            index_id: <p>The identifier of the index used with the data source connector.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_in_use_exception.ResourceInUseException: <p>The resource you want to use is currently in use. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.start_data_source_sync_job_request.StartDataSourceSyncJobRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.start_data_source_sync_job_response.StartDataSourceSyncJobResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.start_data_source_sync_job

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.start_data_source_sync_job.start_data_source_sync_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.start_data_source_sync_job_request.StartDataSourceSyncJobRequest = {
            "id": id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_data_source_sync_job(
        self,
        id: "capo_kendra.types.data_source_id.DataSourceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> None:
        """<p>Stops a synchronization job that is currently running. You can't stop a scheduled synchronization job.</p>

        Args:
            id: <p>The identifier of the data source connector for which to stop the synchronization jobs.</p>
            index_id: <p>The identifier of the index used with the data source connector.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.stop_data_source_sync_job_request.StopDataSourceSyncJobRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.stop_data_source_sync_job

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.stop_data_source_sync_job.stop_data_source_sync_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.stop_data_source_sync_job_request.StopDataSourceSyncJobRequest = {
            "id": id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def submit_feedback(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        query_id: "capo_kendra.types.query_id.QueryId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        click_feedback_items: Optional[
            "capo_kendra.types.click_feedback_list.ClickFeedbackList"
        ] = None,
        relevance_feedback_items: Optional[
            "capo_kendra.types.relevance_feedback_list.RelevanceFeedbackList"
        ] = None,
    ) -> None:
        """<p>Enables you to provide feedback to Amazon Kendra to improve the performance of your index.</p> <p> <code>SubmitFeedback</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p>The identifier of the index that was queried.</p>
            query_id: <p>The identifier of the specific query for which you are submitting feedback. The query ID is returned in the response to the <code>Query</code> API.</p>
            click_feedback_items: <p>Tells Amazon Kendra that a particular search result link was chosen by the user. </p>
            relevance_feedback_items: <p>Provides Amazon Kendra with relevant or not relevant feedback for whether a particular item was relevant to the search.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The resource you want to use isn't available. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.submit_feedback_request.SubmitFeedbackRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.submit_feedback

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.submit_feedback.submit_feedback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.submit_feedback_request.SubmitFeedbackRequest = {
            "index_id": index_id,
            "query_id": query_id,
        }
        if click_feedback_items is not None:
            input_["click_feedback_items"] = click_feedback_items
        if relevance_feedback_items is not None:
            input_["relevance_feedback_items"] = relevance_feedback_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_kendra.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_kendra.types.tag_list.TagList",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tag to the specified index, FAQ, data source, or other resource. If the tag already exists, the existing value is replaced with the new value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the index, FAQ, data source, or other resource to add a tag. For example, the ARN of an index is constructed as follows: <i>arn:aws:kendra:your-region:your-account-id:index/index-id</i> For information on how to construct an ARN for all types of Amazon Kendra resources, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkendra.html#amazonkendra-resources-for-iam-policies">Resource types</a>.</p>
            tags: <p>A list of tag keys to add to the index, FAQ, data source, or other resource. If a tag already exists, the existing value is replaced with the new value.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The resource you want to use isn't available. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.tag_resource

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_kendra.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_kendra.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
    ) -> "capo_kendra.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from an index, FAQ, data source, or other resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the index, FAQ, data source, or other resource to remove a tag. For example, the ARN of an index is constructed as follows: <i>arn:aws:kendra:your-region:your-account-id:index/index-id</i> For information on how to construct an ARN for all types of Amazon Kendra resources, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkendra.html#amazonkendra-resources-for-iam-policies">Resource types</a>.</p>
            tag_keys: <p>A list of tag keys to remove from the index, FAQ, data source, or other resource. If a tag key doesn't exist for the resource, it is ignored.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The resource you want to use isn't available. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.untag_resource

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_access_control_configuration(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        id: "capo_kendra.types.access_control_configuration_id.AccessControlConfigurationId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        name: Optional[
            "capo_kendra.types.access_control_configuration_name.AccessControlConfigurationName"
        ] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        access_control_list: Optional[
            "capo_kendra.types.principal_list.PrincipalList"
        ] = None,
        hierarchical_access_control_list: Optional[
            "capo_kendra.types.hierarchical_principal_list.HierarchicalPrincipalList"
        ] = None,
    ) -> "capo_kendra.types.update_access_control_configuration_response.UpdateAccessControlConfigurationResponse":
        """<p>Updates an access control configuration for your documents in an index. This includes user and group access information for your documents. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p> <p>You can update an access control configuration you created without indexing all of your documents again. For example, your index contains top-secret company documents that only certain employees or users should access. You created an 'allow' access control configuration for one user who recently joined the 'top-secret' team, switching from a team with 'deny' access to top-secret documents. However, the user suddenly returns to their previous team and should no longer have access to top secret documents. You can update the access control configuration to re-configure access control for your documents as circumstances change.</p> <p>You call the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html">BatchPutDocument</a> API to apply the updated access control configuration, with the <code>AccessControlConfigurationId</code> included in the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_Document.html">Document</a> object. If you use an S3 bucket as a data source, you synchronize your data source to apply the <code>AccessControlConfigurationId</code> in the <code>.metadata.json</code> file. Amazon Kendra currently only supports access control configuration for S3 data sources and documents indexed using the <code>BatchPutDocument</code> API.</p> <important> <p>You can't configure access control using <code>CreateAccessControlConfiguration</code> for an Amazon Kendra Gen AI Enterprise Edition index. Amazon Kendra will return a <code>ValidationException</code> error for a <code>Gen_AI_ENTERPRISE_EDITION</code> index.</p> </important>

        Args:
            index_id: <p>The identifier of the index for an access control configuration.</p>
            id: <p>The identifier of the access control configuration you want to update.</p>
            name: <p>A new name for the access control configuration.</p>
            description: <p>A new description for the access control configuration.</p>
            access_control_list: <p>Information you want to update on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>
            hierarchical_access_control_list: <p>The updated list of <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html">principal</a> lists that define the hierarchy for which documents users should have access to.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.update_access_control_configuration_request.UpdateAccessControlConfigurationRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.update_access_control_configuration_response.UpdateAccessControlConfigurationResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.update_access_control_configuration

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.update_access_control_configuration.update_access_control_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.update_access_control_configuration_request.UpdateAccessControlConfigurationRequest = {
            "index_id": index_id,
            "id": id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if access_control_list is not None:
            input_["access_control_list"] = access_control_list
        if hierarchical_access_control_list is not None:
            input_["hierarchical_access_control_list"] = (
                hierarchical_access_control_list
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_data_source(
        self,
        id: "capo_kendra.types.data_source_id.DataSourceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        name: Optional["capo_kendra.types.data_source_name.DataSourceName"] = None,
        configuration: Optional[
            "capo_kendra.types.data_source_configuration.DataSourceConfiguration"
        ] = None,
        vpc_configuration: Optional[
            "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
        ] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        schedule: Optional["capo_kendra.types.scan_schedule.ScanSchedule"] = None,
        role_arn: Optional["capo_kendra.types.role_arn.RoleArn"] = None,
        language_code: Optional["capo_kendra.types.language_code.LanguageCode"] = None,
        custom_document_enrichment_configuration: Optional[
            "capo_kendra.types.custom_document_enrichment_configuration.CustomDocumentEnrichmentConfiguration"
        ] = None,
    ) -> None:
        """<p>Updates an Amazon Kendra data source connector.</p>

        Args:
            id: <p>The identifier of the data source connector you want to update.</p>
            name: <p>A new name for the data source connector.</p>
            index_id: <p>The identifier of the index used with the data source connector.</p>
            configuration: <p>Configuration information you want to update for the data source connector.</p>
            vpc_configuration: <p>Configuration information for an Amazon Virtual Private Cloud to connect to your data source. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html">Configuring a VPC</a>.</p>
            description: <p>A new description for the data source connector.</p>
            schedule: <p>The sync schedule you want to update for the data source connector.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM roles for Amazon Kendra</a>.</p>
            language_code: <p>The code for a language you want to update for the data source connector. This allows you to support a language for all documents when updating the data source. English is supported by default. For more information on supported languages, including their codes, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html">Adding documents in languages other than English</a>.</p>
            custom_document_enrichment_configuration: <p>Configuration information you want to update for altering document metadata and content during the document ingestion process.</p> <p>For more information on how to create, modify and delete document metadata, or make other content alterations when you ingest documents into Amazon Kendra, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html">Customizing document metadata during the ingestion process</a>.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.update_data_source_request.UpdateDataSourceRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.update_data_source

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.update_data_source.update_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.update_data_source_request.UpdateDataSourceRequest = {
            "id": id,
            "index_id": index_id,
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if description is not None:
            input_["description"] = description
        if schedule is not None:
            input_["schedule"] = schedule
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if language_code is not None:
            input_["language_code"] = language_code
        if custom_document_enrichment_configuration is not None:
            input_["custom_document_enrichment_configuration"] = (
                custom_document_enrichment_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_experience(
        self,
        id: "capo_kendra.types.experience_id.ExperienceId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        name: Optional["capo_kendra.types.experience_name.ExperienceName"] = None,
        role_arn: Optional["capo_kendra.types.role_arn.RoleArn"] = None,
        configuration: Optional[
            "capo_kendra.types.experience_configuration.ExperienceConfiguration"
        ] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
    ) -> None:
        """<p>Updates your Amazon Kendra experience such as a search application. For more information on creating a search application experience, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html">Building a search experience with no code</a>.</p>

        Args:
            id: <p>The identifier of your Amazon Kendra experience you want to update.</p>
            name: <p>A new name for your Amazon Kendra experience.</p>
            index_id: <p>The identifier of the index for your Amazon Kendra experience.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access the <code>Query</code> API, <code>QuerySuggestions</code> API, <code>SubmitFeedback</code> API, and IAM Identity Center that stores your users and groups information. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM roles for Amazon Kendra</a>.</p>
            configuration: <p>Configuration information you want to update for your Amazon Kendra experience.</p>
            description: <p>A new description for your Amazon Kendra experience.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.update_experience_request.UpdateExperienceRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.update_experience

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.update_experience.update_experience(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.update_experience_request.UpdateExperienceRequest = {
            "id": id,
            "index_id": index_id,
        }
        if name is not None:
            input_["name"] = name
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if configuration is not None:
            input_["configuration"] = configuration
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_featured_results_set(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        featured_results_set_id: "capo_kendra.types.featured_results_set_id.FeaturedResultsSetId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        featured_results_set_name: Optional[
            "capo_kendra.types.featured_results_set_name.FeaturedResultsSetName"
        ] = None,
        description: Optional[
            "capo_kendra.types.featured_results_set_description.FeaturedResultsSetDescription"
        ] = None,
        status: Optional[
            "capo_kendra.types.featured_results_set_status.FeaturedResultsSetStatus"
        ] = None,
        query_texts: Optional["capo_kendra.types.query_text_list.QueryTextList"] = None,
        featured_documents: Optional[
            "capo_kendra.types.featured_document_list.FeaturedDocumentList"
        ] = None,
    ) -> "capo_kendra.types.update_featured_results_set_response.UpdateFeaturedResultsSetResponse":
        """<p>Updates a set of featured results. Features results are placed above all other results for certain queries. You map specific queries to specific documents for featuring in the results. If a query contains an exact match of a query, then one or more specific documents are featured in the search results.</p>

        Args:
            index_id: <p>The identifier of the index used for featuring results.</p>
            featured_results_set_id: <p>The identifier of the set of featured results that you want to update.</p>
            featured_results_set_name: <p>A new name for the set of featured results.</p>
            description: <p>A new description for the set of featured results.</p>
            status: <p>You can set the status to <code>ACTIVE</code> or <code>INACTIVE</code>. When the value is <code>ACTIVE</code>, featured results are ready for use. You can still configure your settings before setting the status to <code>ACTIVE</code>. The queries you specify for featured results must be unique per featured results set for each index, whether the status is <code>ACTIVE</code> or <code>INACTIVE</code>.</p>
            query_texts: <p>A list of queries for featuring results. For more information on the list of queries, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html">FeaturedResultsSet</a>.</p>
            featured_documents: <p>A list of document IDs for the documents you want to feature at the top of the search results page. For more information on the list of featured documents, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html">FeaturedResultsSet</a>.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.featured_results_conflict_exception.FeaturedResultsConflictException: <p>An error message with a list of conflicting queries used across different sets of featured results. This occurred with the request for a new featured results set. Check that the queries you specified for featured results are unique per featured results set for each index.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.update_featured_results_set_request.UpdateFeaturedResultsSetRequest]",
        ) -> OperationResponse[
            "capo_kendra.types.update_featured_results_set_response.UpdateFeaturedResultsSetResponse"
        ]:
            import capo_kendra._operations.aws_kendra_frontend_service.update_featured_results_set

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.update_featured_results_set.update_featured_results_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.update_featured_results_set_request.UpdateFeaturedResultsSetRequest = {
            "index_id": index_id,
            "featured_results_set_id": featured_results_set_id,
        }
        if featured_results_set_name is not None:
            input_["featured_results_set_name"] = featured_results_set_name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if query_texts is not None:
            input_["query_texts"] = query_texts
        if featured_documents is not None:
            input_["featured_documents"] = featured_documents

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_index(
        self,
        id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        name: Optional["capo_kendra.types.index_name.IndexName"] = None,
        role_arn: Optional["capo_kendra.types.role_arn.RoleArn"] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        document_metadata_configuration_updates: Optional[
            "capo_kendra.types.document_metadata_configuration_list.DocumentMetadataConfigurationList"
        ] = None,
        capacity_units: Optional[
            "capo_kendra.types.capacity_units_configuration.CapacityUnitsConfiguration"
        ] = None,
        user_token_configurations: Optional[
            "capo_kendra.types.user_token_configuration_list.UserTokenConfigurationList"
        ] = None,
        user_context_policy: Optional[
            "capo_kendra.types.user_context_policy.UserContextPolicy"
        ] = None,
        user_group_resolution_configuration: Optional[
            "capo_kendra.types.user_group_resolution_configuration.UserGroupResolutionConfiguration"
        ] = None,
    ) -> None:
        """<p>Updates an Amazon Kendra index.</p>

        Args:
            id: <p>The identifier of the index you want to update.</p>
            name: <p>A new name for the index.</p>
            role_arn: <p>An Identity and Access Management (IAM) role that gives Amazon Kendra permission to access Amazon CloudWatch logs and metrics.</p>
            description: <p>A new description for the index.</p>
            document_metadata_configuration_updates: <p>The document metadata configuration you want to update for the index. Document metadata are fields or attributes associated with your documents. For example, the company department name associated with each document.</p>
            capacity_units: <p>Sets the number of additional document storage and query capacity units that should be used by the index. You can change the capacity of the index up to 5 times per day, or make 5 API calls.</p> <p>If you are using extra storage units, you can't reduce the storage capacity below what is required to meet the storage needs for your index.</p>
            user_token_configurations: <p>The user token configuration.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>UserTokenConfigurations</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important>
            user_context_policy: <p>The user context policy.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, you can only use <code>ATTRIBUTE_FILTER</code> to filter search results by user context. If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>USER_TOKEN</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important>
            user_group_resolution_configuration: <p>Gets users and groups from IAM Identity Center identity source. To configure this, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_UserGroupResolutionConfiguration.html">UserGroupResolutionConfiguration</a>. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, <code>UserGroupResolutionConfiguration</code> isn't supported.</p> </important>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Kendra service. Please see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas</a> for more information, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> to inquire about an increase of limits.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.update_index_request.UpdateIndexRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.update_index

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.update_index.update_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.update_index_request.UpdateIndexRequest = {"id": id}
        if name is not None:
            input_["name"] = name
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if description is not None:
            input_["description"] = description
        if document_metadata_configuration_updates is not None:
            input_["document_metadata_configuration_updates"] = (
                document_metadata_configuration_updates
            )
        if capacity_units is not None:
            input_["capacity_units"] = capacity_units
        if user_token_configurations is not None:
            input_["user_token_configurations"] = user_token_configurations
        if user_context_policy is not None:
            input_["user_context_policy"] = user_context_policy
        if user_group_resolution_configuration is not None:
            input_["user_group_resolution_configuration"] = (
                user_group_resolution_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_query_suggestions_block_list(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        id: "capo_kendra.types.query_suggestions_block_list_id.QuerySuggestionsBlockListId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        name: Optional[
            "capo_kendra.types.query_suggestions_block_list_name.QuerySuggestionsBlockListName"
        ] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        source_s3_path: Optional["capo_kendra.types.s3_path.S3Path"] = None,
        role_arn: Optional["capo_kendra.types.role_arn.RoleArn"] = None,
    ) -> None:
        """<p>Updates a block list used for query suggestions for an index.</p> <p>Updates to a block list might not take effect right away. Amazon Kendra needs to refresh the entire suggestions list to apply any updates to the block list. Other changes not related to the block list apply immediately.</p> <p>If a block list is updating, then you need to wait for the first update to finish before submitting another update.</p> <p>Amazon Kendra supports partial updates, so you only need to provide the fields you want to update.</p> <p> <code>UpdateQuerySuggestionsBlockList</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p>The identifier of the index for the block list.</p>
            id: <p>The identifier of the block list you want to update.</p>
            name: <p>A new name for the block list.</p>
            description: <p>A new description for the block list.</p>
            source_s3_path: <p>The S3 path where your block list text file sits in S3.</p> <p>If you update your block list and provide the same path to the block list text file in S3, then Amazon Kendra reloads the file to refresh the block list. Amazon Kendra does not automatically refresh your block list. You need to call the <code>UpdateQuerySuggestionsBlockList</code> API to refresh you block list.</p> <p>If you update your block list, then Amazon Kendra asynchronously refreshes all query suggestions with the latest content in the S3 file. This means changes might not take effect immediately.</p>
            role_arn: <p>The IAM (Identity and Access Management) role used to access the block list text file in S3.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.update_query_suggestions_block_list_request.UpdateQuerySuggestionsBlockListRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.update_query_suggestions_block_list

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.update_query_suggestions_block_list.update_query_suggestions_block_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.update_query_suggestions_block_list_request.UpdateQuerySuggestionsBlockListRequest = {
            "index_id": index_id,
            "id": id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if source_s3_path is not None:
            input_["source_s3_path"] = source_s3_path
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_query_suggestions_config(
        self,
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        mode: Optional["capo_kendra.types.mode.Mode"] = None,
        query_log_look_back_window_in_days: Optional[
            "capo_kendra.types.integer.Integer"
        ] = None,
        include_queries_without_user_information: Optional[
            "capo_kendra.types.object_boolean.ObjectBoolean"
        ] = None,
        minimum_number_of_querying_users: Optional[
            "capo_kendra.types.minimum_number_of_querying_users.MinimumNumberOfQueryingUsers"
        ] = None,
        minimum_query_count: Optional[
            "capo_kendra.types.minimum_query_count.MinimumQueryCount"
        ] = None,
        attribute_suggestions_config: Optional[
            "capo_kendra.types.attribute_suggestions_update_config.AttributeSuggestionsUpdateConfig"
        ] = None,
    ) -> None:
        """<p>Updates the settings of query suggestions for an index.</p> <p>Amazon Kendra supports partial updates, so you only need to provide the fields you want to update.</p> <p>If an update is currently processing, you need to wait for the update to finish before making another update.</p> <p>Updates to query suggestions settings might not take effect right away. The time for your updated settings to take effect depends on the updates made and the number of search queries in your index.</p> <p>You can still enable/disable query suggestions at any time.</p> <p> <code>UpdateQuerySuggestionsConfig</code> is currently not supported in the Amazon Web Services GovCloud (US-West) region.</p>

        Args:
            index_id: <p> The identifier of the index with query suggestions you want to update.</p>
            mode: <p>Set the mode to <code>ENABLED</code> or <code>LEARN_ONLY</code>.</p> <p>By default, Amazon Kendra enables query suggestions. <code>LEARN_ONLY</code> mode allows you to turn off query suggestions. You can to update this at any time.</p> <p>In <code>LEARN_ONLY</code> mode, Amazon Kendra continues to learn from new queries to keep suggestions up to date for when you are ready to switch to ENABLED mode again.</p>
            query_log_look_back_window_in_days: <p>How recent your queries are in your query log time window.</p> <p>The time window is the number of days from current day to past days.</p> <p>By default, Amazon Kendra sets this to 180.</p>
            include_queries_without_user_information: <p> <code>TRUE</code> to include queries without user information (i.e. all queries, irrespective of the user), otherwise <code>FALSE</code> to only include queries with user information.</p> <p>If you pass user information to Amazon Kendra along with the queries, you can set this flag to <code>FALSE</code> and instruct Amazon Kendra to only consider queries with user information.</p> <p>If you set to <code>FALSE</code>, Amazon Kendra only considers queries searched at least <code>MinimumQueryCount</code> times across <code>MinimumNumberOfQueryingUsers</code> unique users for suggestions.</p> <p>If you set to <code>TRUE</code>, Amazon Kendra ignores all user information and learns from all queries.</p>
            minimum_number_of_querying_users: <p>The minimum number of unique users who must search a query in order for the query to be eligible to suggest to your users.</p> <p>Increasing this number might decrease the number of suggestions. However, this ensures a query is searched by many users and is truly popular to suggest to users.</p> <p>How you tune this setting depends on your specific needs.</p>
            minimum_query_count: <p>The the minimum number of times a query must be searched in order to be eligible to suggest to your users.</p> <p>Decreasing this number increases the number of suggestions. However, this affects the quality of suggestions as it sets a low bar for a query to be considered popular to suggest to users.</p> <p>How you tune this setting depends on your specific needs.</p>
            attribute_suggestions_config: <p>Configuration information for the document fields/attributes that you want to base query suggestions on.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.update_query_suggestions_config_request.UpdateQuerySuggestionsConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.update_query_suggestions_config

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.update_query_suggestions_config.update_query_suggestions_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.update_query_suggestions_config_request.UpdateQuerySuggestionsConfigRequest = {
            "index_id": index_id
        }
        if mode is not None:
            input_["mode"] = mode
        if query_log_look_back_window_in_days is not None:
            input_["query_log_look_back_window_in_days"] = (
                query_log_look_back_window_in_days
            )
        if include_queries_without_user_information is not None:
            input_["include_queries_without_user_information"] = (
                include_queries_without_user_information
            )
        if minimum_number_of_querying_users is not None:
            input_["minimum_number_of_querying_users"] = (
                minimum_number_of_querying_users
            )
        if minimum_query_count is not None:
            input_["minimum_query_count"] = minimum_query_count
        if attribute_suggestions_config is not None:
            input_["attribute_suggestions_config"] = attribute_suggestions_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_thesaurus(
        self,
        id: "capo_kendra.types.thesaurus_id.ThesaurusId",
        index_id: "capo_kendra.types.index_id.IndexId",
        *,
        config_overrides: Optional[kendraClientConfig] = None,
        name: Optional["capo_kendra.types.thesaurus_name.ThesaurusName"] = None,
        description: Optional["capo_kendra.types.description.Description"] = None,
        role_arn: Optional["capo_kendra.types.role_arn.RoleArn"] = None,
        source_s3_path: Optional["capo_kendra.types.s3_path.S3Path"] = None,
    ) -> None:
        """<p>Updates a thesaurus for an index.</p>

        Args:
            id: <p>The identifier of the thesaurus you want to update.</p>
            name: <p>A new name for the thesaurus.</p>
            index_id: <p>The identifier of the index for the thesaurus.</p>
            description: <p>A new description for the thesaurus.</p>
            role_arn: <p>An IAM role that gives Amazon Kendra permissions to access thesaurus file specified in <code>SourceS3Path</code>.</p>

        Raises:
            capo_kendra.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.</p>
            capo_kendra.errors.conflict_exception.ConflictException: <p>A conflict occurred with the request. Please fix any inconsistences with your resources and try again.</p>
            capo_kendra.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_kendra.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.</p>
            capo_kendra.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Please reduce the number of requests and try again.</p>
            capo_kendra.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.</p>
            capo_kendra.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_kendra.types.update_thesaurus_request.UpdateThesaurusRequest]",
        ) -> OperationResponse[None]:
            import capo_kendra._operations.aws_kendra_frontend_service.update_thesaurus

            output, http_response = (
                capo_kendra._operations.aws_kendra_frontend_service.update_thesaurus.update_thesaurus(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kendra.types.update_thesaurus_request.UpdateThesaurusRequest = {
            "id": id,
            "index_id": index_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if source_s3_path is not None:
            input_["source_s3_path"] = source_s3_path

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
