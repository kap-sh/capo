"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CustomerProfiles_20200815``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_customer_profiles._auth._signers
import capo_customer_profiles._auth._sigv4
from capo_customer_profiles._auth._identity import Credentials
from capo_customer_profiles._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_customer_profiles._auth._zapros_handler import AuthMiddleware
from capo_customer_profiles._pagination import resolve_path as _resolve_path
from capo_customer_profiles._services._aws_config import aws_config
from capo_customer_profiles._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_customer_profiles.types.action_type
    import capo_customer_profiles.types.add_profile_key_request
    import capo_customer_profiles.types.add_profile_key_response
    import capo_customer_profiles.types.additional_search_keys_list
    import capo_customer_profiles.types.address
    import capo_customer_profiles.types.associate_stream_for_segments_request
    import capo_customer_profiles.types.associate_stream_for_segments_response
    import capo_customer_profiles.types.attribute_details
    import capo_customer_profiles.types.attributes
    import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list
    import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_request
    import capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_response
    import capo_customer_profiles.types.batch_get_profile_id_list
    import capo_customer_profiles.types.batch_get_profile_request
    import capo_customer_profiles.types.batch_get_profile_response
    import capo_customer_profiles.types.batch_put_profile_object_request
    import capo_customer_profiles.types.batch_put_profile_object_request_item_list
    import capo_customer_profiles.types.batch_put_profile_object_response
    import capo_customer_profiles.types.boolean
    import capo_customer_profiles.types.candidate_id_list
    import capo_customer_profiles.types.condition_overrides
    import capo_customer_profiles.types.conditions
    import capo_customer_profiles.types.conflict_resolution
    import capo_customer_profiles.types.consolidation
    import capo_customer_profiles.types.create_calculated_attribute_definition_request
    import capo_customer_profiles.types.create_calculated_attribute_definition_response
    import capo_customer_profiles.types.create_domain_layout_request
    import capo_customer_profiles.types.create_domain_layout_response
    import capo_customer_profiles.types.create_domain_request
    import capo_customer_profiles.types.create_domain_response
    import capo_customer_profiles.types.create_event_stream_request
    import capo_customer_profiles.types.create_event_stream_response
    import capo_customer_profiles.types.create_event_trigger_request
    import capo_customer_profiles.types.create_event_trigger_response
    import capo_customer_profiles.types.create_integration_workflow_request
    import capo_customer_profiles.types.create_integration_workflow_response
    import capo_customer_profiles.types.create_profile_request
    import capo_customer_profiles.types.create_profile_response
    import capo_customer_profiles.types.create_recommender_filter_request
    import capo_customer_profiles.types.create_recommender_filter_response
    import capo_customer_profiles.types.create_recommender_request
    import capo_customer_profiles.types.create_recommender_response
    import capo_customer_profiles.types.create_recommender_schema_request
    import capo_customer_profiles.types.create_recommender_schema_response
    import capo_customer_profiles.types.create_segment_definition_request
    import capo_customer_profiles.types.create_segment_definition_response
    import capo_customer_profiles.types.create_segment_estimate_request
    import capo_customer_profiles.types.create_segment_estimate_response
    import capo_customer_profiles.types.create_segment_snapshot_request
    import capo_customer_profiles.types.create_segment_snapshot_response
    import capo_customer_profiles.types.create_upload_job_request
    import capo_customer_profiles.types.create_upload_job_response
    import capo_customer_profiles.types.data_format
    import capo_customer_profiles.types.data_store_request
    import capo_customer_profiles.types.delete_calculated_attribute_definition_request
    import capo_customer_profiles.types.delete_calculated_attribute_definition_response
    import capo_customer_profiles.types.delete_domain_layout_request
    import capo_customer_profiles.types.delete_domain_layout_response
    import capo_customer_profiles.types.delete_domain_object_type_request
    import capo_customer_profiles.types.delete_domain_object_type_response
    import capo_customer_profiles.types.delete_domain_request
    import capo_customer_profiles.types.delete_domain_response
    import capo_customer_profiles.types.delete_event_stream_request
    import capo_customer_profiles.types.delete_event_stream_response
    import capo_customer_profiles.types.delete_event_trigger_request
    import capo_customer_profiles.types.delete_event_trigger_response
    import capo_customer_profiles.types.delete_integration_request
    import capo_customer_profiles.types.delete_integration_response
    import capo_customer_profiles.types.delete_profile_key_request
    import capo_customer_profiles.types.delete_profile_key_response
    import capo_customer_profiles.types.delete_profile_object_request
    import capo_customer_profiles.types.delete_profile_object_response
    import capo_customer_profiles.types.delete_profile_object_type_request
    import capo_customer_profiles.types.delete_profile_object_type_response
    import capo_customer_profiles.types.delete_profile_request
    import capo_customer_profiles.types.delete_profile_response
    import capo_customer_profiles.types.delete_recommender_filter_request
    import capo_customer_profiles.types.delete_recommender_filter_response
    import capo_customer_profiles.types.delete_recommender_request
    import capo_customer_profiles.types.delete_recommender_response
    import capo_customer_profiles.types.delete_recommender_schema_request
    import capo_customer_profiles.types.delete_recommender_schema_response
    import capo_customer_profiles.types.delete_segment_definition_request
    import capo_customer_profiles.types.delete_segment_definition_response
    import capo_customer_profiles.types.delete_segment_subscription_request
    import capo_customer_profiles.types.delete_segment_subscription_response
    import capo_customer_profiles.types.delete_workflow_request
    import capo_customer_profiles.types.delete_workflow_response
    import capo_customer_profiles.types.destination_arn_string
    import capo_customer_profiles.types.destination_role_arn
    import capo_customer_profiles.types.detect_profile_object_type_request
    import capo_customer_profiles.types.detect_profile_object_type_response
    import capo_customer_profiles.types.disassociate_stream_for_segments_request
    import capo_customer_profiles.types.disassociate_stream_for_segments_response
    import capo_customer_profiles.types.display_name
    import capo_customer_profiles.types.domain_object_type_fields
    import capo_customer_profiles.types.domain_object_types_list_item
    import capo_customer_profiles.types.double0_to1
    import capo_customer_profiles.types.encryption_key
    import capo_customer_profiles.types.engagement_preferences
    import capo_customer_profiles.types.event_stream_summary
    import capo_customer_profiles.types.event_trigger_conditions
    import capo_customer_profiles.types.event_trigger_limits
    import capo_customer_profiles.types.event_trigger_names
    import capo_customer_profiles.types.event_trigger_summary_item
    import capo_customer_profiles.types.expiration_days_integer
    import capo_customer_profiles.types.field_map
    import capo_customer_profiles.types.field_source_profile_ids
    import capo_customer_profiles.types.filter
    import capo_customer_profiles.types.flow_definition
    import capo_customer_profiles.types.gender
    import capo_customer_profiles.types.get_auto_merging_preview_request
    import capo_customer_profiles.types.get_auto_merging_preview_response
    import capo_customer_profiles.types.get_calculated_attribute_definition_request
    import capo_customer_profiles.types.get_calculated_attribute_definition_response
    import capo_customer_profiles.types.get_calculated_attribute_for_profile_request
    import capo_customer_profiles.types.get_calculated_attribute_for_profile_response
    import capo_customer_profiles.types.get_domain_layout_request
    import capo_customer_profiles.types.get_domain_layout_response
    import capo_customer_profiles.types.get_domain_object_type_request
    import capo_customer_profiles.types.get_domain_object_type_response
    import capo_customer_profiles.types.get_domain_request
    import capo_customer_profiles.types.get_domain_response
    import capo_customer_profiles.types.get_event_stream_request
    import capo_customer_profiles.types.get_event_stream_response
    import capo_customer_profiles.types.get_event_trigger_request
    import capo_customer_profiles.types.get_event_trigger_response
    import capo_customer_profiles.types.get_identity_resolution_job_request
    import capo_customer_profiles.types.get_identity_resolution_job_response
    import capo_customer_profiles.types.get_integration_request
    import capo_customer_profiles.types.get_integration_response
    import capo_customer_profiles.types.get_matches_request
    import capo_customer_profiles.types.get_matches_response
    import capo_customer_profiles.types.get_object_type_attribute_statistics_request
    import capo_customer_profiles.types.get_object_type_attribute_statistics_response
    import capo_customer_profiles.types.get_profile_history_record_request
    import capo_customer_profiles.types.get_profile_history_record_response
    import capo_customer_profiles.types.get_profile_object_type_request
    import capo_customer_profiles.types.get_profile_object_type_response
    import capo_customer_profiles.types.get_profile_object_type_template_request
    import capo_customer_profiles.types.get_profile_object_type_template_response
    import capo_customer_profiles.types.get_profile_recommendations_request
    import capo_customer_profiles.types.get_profile_recommendations_response
    import capo_customer_profiles.types.get_recommender_filter_request
    import capo_customer_profiles.types.get_recommender_filter_response
    import capo_customer_profiles.types.get_recommender_request
    import capo_customer_profiles.types.get_recommender_request_training_metrics_count_integer
    import capo_customer_profiles.types.get_recommender_response
    import capo_customer_profiles.types.get_recommender_schema_request
    import capo_customer_profiles.types.get_recommender_schema_response
    import capo_customer_profiles.types.get_segment_definition_request
    import capo_customer_profiles.types.get_segment_definition_response
    import capo_customer_profiles.types.get_segment_estimate_request
    import capo_customer_profiles.types.get_segment_estimate_response
    import capo_customer_profiles.types.get_segment_membership_request
    import capo_customer_profiles.types.get_segment_membership_response
    import capo_customer_profiles.types.get_segment_snapshot_request
    import capo_customer_profiles.types.get_segment_snapshot_response
    import capo_customer_profiles.types.get_segment_subscription_request
    import capo_customer_profiles.types.get_segment_subscription_response
    import capo_customer_profiles.types.get_similar_profiles_request
    import capo_customer_profiles.types.get_similar_profiles_response
    import capo_customer_profiles.types.get_stream_for_segments_request
    import capo_customer_profiles.types.get_stream_for_segments_response
    import capo_customer_profiles.types.get_upload_job_path_request
    import capo_customer_profiles.types.get_upload_job_path_response
    import capo_customer_profiles.types.get_upload_job_request
    import capo_customer_profiles.types.get_upload_job_response
    import capo_customer_profiles.types.get_workflow_request
    import capo_customer_profiles.types.get_workflow_response
    import capo_customer_profiles.types.get_workflow_steps_request
    import capo_customer_profiles.types.get_workflow_steps_response
    import capo_customer_profiles.types.integration_config
    import capo_customer_profiles.types.key_map
    import capo_customer_profiles.types.key_values_list
    import capo_customer_profiles.types.layout_item
    import capo_customer_profiles.types.layout_type
    import capo_customer_profiles.types.list_account_integrations_request
    import capo_customer_profiles.types.list_account_integrations_response
    import capo_customer_profiles.types.list_calculated_attribute_definitions_request
    import capo_customer_profiles.types.list_calculated_attribute_definitions_response
    import capo_customer_profiles.types.list_calculated_attributes_for_profile_request
    import capo_customer_profiles.types.list_calculated_attributes_for_profile_response
    import capo_customer_profiles.types.list_domain_layouts_request
    import capo_customer_profiles.types.list_domain_layouts_response
    import capo_customer_profiles.types.list_domain_object_types_request
    import capo_customer_profiles.types.list_domain_object_types_response
    import capo_customer_profiles.types.list_domains_request
    import capo_customer_profiles.types.list_domains_response
    import capo_customer_profiles.types.list_event_streams_request
    import capo_customer_profiles.types.list_event_streams_response
    import capo_customer_profiles.types.list_event_triggers_request
    import capo_customer_profiles.types.list_event_triggers_response
    import capo_customer_profiles.types.list_identity_resolution_jobs_request
    import capo_customer_profiles.types.list_identity_resolution_jobs_response
    import capo_customer_profiles.types.list_integrations_request
    import capo_customer_profiles.types.list_integrations_response
    import capo_customer_profiles.types.list_object_type_attribute_item
    import capo_customer_profiles.types.list_object_type_attribute_values_request
    import capo_customer_profiles.types.list_object_type_attribute_values_response
    import capo_customer_profiles.types.list_object_type_attributes_request
    import capo_customer_profiles.types.list_object_type_attributes_response
    import capo_customer_profiles.types.list_profile_history_records_request
    import capo_customer_profiles.types.list_profile_history_records_response
    import capo_customer_profiles.types.list_profile_object_type_templates_request
    import capo_customer_profiles.types.list_profile_object_type_templates_response
    import capo_customer_profiles.types.list_profile_object_types_request
    import capo_customer_profiles.types.list_profile_object_types_response
    import capo_customer_profiles.types.list_profile_objects_request
    import capo_customer_profiles.types.list_profile_objects_response
    import capo_customer_profiles.types.list_recommender_filters_request
    import capo_customer_profiles.types.list_recommender_filters_response
    import capo_customer_profiles.types.list_recommender_recipes_request
    import capo_customer_profiles.types.list_recommender_recipes_request_max_results_integer
    import capo_customer_profiles.types.list_recommender_recipes_response
    import capo_customer_profiles.types.list_recommender_schemas_request
    import capo_customer_profiles.types.list_recommender_schemas_response
    import capo_customer_profiles.types.list_recommenders_request
    import capo_customer_profiles.types.list_recommenders_request_max_results_integer
    import capo_customer_profiles.types.list_recommenders_response
    import capo_customer_profiles.types.list_rule_based_matches_request
    import capo_customer_profiles.types.list_rule_based_matches_response
    import capo_customer_profiles.types.list_segment_definitions_request
    import capo_customer_profiles.types.list_segment_definitions_response
    import capo_customer_profiles.types.list_segment_subscription_events_request
    import capo_customer_profiles.types.list_segment_subscription_events_response
    import capo_customer_profiles.types.list_tags_for_resource_request
    import capo_customer_profiles.types.list_tags_for_resource_response
    import capo_customer_profiles.types.list_upload_jobs_request
    import capo_customer_profiles.types.list_upload_jobs_response
    import capo_customer_profiles.types.list_workflows_request
    import capo_customer_profiles.types.list_workflows_response
    import capo_customer_profiles.types.logical_operator
    import capo_customer_profiles.types.match_type
    import capo_customer_profiles.types.matching_request
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.max_size500
    import capo_customer_profiles.types.merge_profiles_request
    import capo_customer_profiles.types.merge_profiles_response
    import capo_customer_profiles.types.metadata_config
    import capo_customer_profiles.types.min_size1
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.object_filter
    import capo_customer_profiles.types.object_type_names
    import capo_customer_profiles.types.objects
    import capo_customer_profiles.types.optional_boolean
    import capo_customer_profiles.types.party_type
    import capo_customer_profiles.types.profile_attribute_values_request
    import capo_customer_profiles.types.profile_attribute_values_response
    import capo_customer_profiles.types.profile_id_to_be_merged_list
    import capo_customer_profiles.types.profile_ids
    import capo_customer_profiles.types.profile_type
    import capo_customer_profiles.types.put_domain_object_type_request
    import capo_customer_profiles.types.put_domain_object_type_response
    import capo_customer_profiles.types.put_integration_request
    import capo_customer_profiles.types.put_integration_response
    import capo_customer_profiles.types.put_profile_object_request
    import capo_customer_profiles.types.put_profile_object_response
    import capo_customer_profiles.types.put_profile_object_type_request
    import capo_customer_profiles.types.put_profile_object_type_response
    import capo_customer_profiles.types.put_segment_subscription_request
    import capo_customer_profiles.types.put_segment_subscription_response
    import capo_customer_profiles.types.recommendation_diversity_config
    import capo_customer_profiles.types.recommendation_metadata
    import capo_customer_profiles.types.recommender
    import capo_customer_profiles.types.recommender_config
    import capo_customer_profiles.types.recommender_context
    import capo_customer_profiles.types.recommender_filter_expression
    import capo_customer_profiles.types.recommender_filter_name
    import capo_customer_profiles.types.recommender_filter_summary
    import capo_customer_profiles.types.recommender_filters
    import capo_customer_profiles.types.recommender_promotional_filters
    import capo_customer_profiles.types.recommender_recipe
    import capo_customer_profiles.types.recommender_recipe_name
    import capo_customer_profiles.types.recommender_schema_fields
    import capo_customer_profiles.types.recommender_schema_summary
    import capo_customer_profiles.types.recommender_summary
    import capo_customer_profiles.types.recommender_version_name
    import capo_customer_profiles.types.request_value_list
    import capo_customer_profiles.types.role_arn
    import capo_customer_profiles.types.rule_based_matching_request
    import capo_customer_profiles.types.schedule_configuration
    import capo_customer_profiles.types.scope
    import capo_customer_profiles.types.search_profiles_request
    import capo_customer_profiles.types.search_profiles_response
    import capo_customer_profiles.types.search_recommendations_request
    import capo_customer_profiles.types.search_recommendations_response
    import capo_customer_profiles.types.segment_definition_item
    import capo_customer_profiles.types.segment_group
    import capo_customer_profiles.types.segment_group_structure
    import capo_customer_profiles.types.segment_sort
    import capo_customer_profiles.types.sensitive_string0_to255
    import capo_customer_profiles.types.sensitive_string0_to1000
    import capo_customer_profiles.types.sensitive_string1_to255
    import capo_customer_profiles.types.sensitive_string1_to1000
    import capo_customer_profiles.types.sensitive_string1_to4000
    import capo_customer_profiles.types.sensitive_string1_to10000
    import capo_customer_profiles.types.sensitive_string1_to50000
    import capo_customer_profiles.types.sensitive_string1_to2000000
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.sqs_queue_url
    import capo_customer_profiles.types.start_recommender_request
    import capo_customer_profiles.types.start_recommender_response
    import capo_customer_profiles.types.start_upload_job_request
    import capo_customer_profiles.types.start_upload_job_response
    import capo_customer_profiles.types.statistic
    import capo_customer_profiles.types.status
    import capo_customer_profiles.types.stop_recommender_request
    import capo_customer_profiles.types.stop_recommender_response
    import capo_customer_profiles.types.stop_upload_job_request
    import capo_customer_profiles.types.stop_upload_job_response
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.string1_to1000
    import capo_customer_profiles.types.stringified_json
    import capo_customer_profiles.types.subscription_event_item
    import capo_customer_profiles.types.tag_arn
    import capo_customer_profiles.types.tag_key_list
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.tag_resource_request
    import capo_customer_profiles.types.tag_resource_response
    import capo_customer_profiles.types.text
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.token
    import capo_customer_profiles.types.type_name
    import capo_customer_profiles.types.untag_resource_request
    import capo_customer_profiles.types.untag_resource_response
    import capo_customer_profiles.types.update_address
    import capo_customer_profiles.types.update_attributes
    import capo_customer_profiles.types.update_calculated_attribute_definition_request
    import capo_customer_profiles.types.update_calculated_attribute_definition_response
    import capo_customer_profiles.types.update_domain_layout_request
    import capo_customer_profiles.types.update_domain_layout_response
    import capo_customer_profiles.types.update_domain_request
    import capo_customer_profiles.types.update_domain_response
    import capo_customer_profiles.types.update_event_trigger_request
    import capo_customer_profiles.types.update_event_trigger_response
    import capo_customer_profiles.types.update_profile_request
    import capo_customer_profiles.types.update_profile_response
    import capo_customer_profiles.types.update_recommender_request
    import capo_customer_profiles.types.update_recommender_response
    import capo_customer_profiles.types.upload_job_item
    import capo_customer_profiles.types.uuid
    import capo_customer_profiles.types.workflow_type


class CustomerProfilesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class CustomerProfilesClient:
    """A client for the ``CustomerProfiles`` service.

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
        self._config = CustomerProfilesClientConfig(
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
        self, config_overrides: Optional[CustomerProfilesClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CustomerProfilesClientConfig = config_overrides or {}
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

    def add_profile_key(
        self,
        profile_id: "capo_customer_profiles.types.uuid.uuid",
        key_name: "capo_customer_profiles.types.name.name",
        values: "capo_customer_profiles.types.request_value_list.requestValueList",
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.add_profile_key_response.AddProfileKeyResponse":
        """<p>Associates a new key value with a specific profile, such as a Contact Record ContactId.</p> <p>A profile object can have a single unique key and any number of additional keys that can be used to identify the profile that it belongs to.</p>

        Args:
            profile_id: <p>The unique identifier of a customer profile.</p>
            key_name: <p>A searchable identifier of a customer profile. The predefined keys you can use include: _account, _profileId, _assetId, _caseId, _orderId, _fullName, _phone, _email, _ctrContactId, _marketoLeadId, _salesforceAccountId, _salesforceContactId, _salesforceAssetId, _zendeskUserId, _zendeskExternalId, _zendeskTicketId, _serviceNowSystemId, _serviceNowIncidentId, _segmentUserId, _shopifyCustomerId, _shopifyOrderId.</p>
            values: <p>A list of key values.</p>
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.add_profile_key_request.AddProfileKeyRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.add_profile_key_response.AddProfileKeyResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.add_profile_key

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.add_profile_key.add_profile_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.add_profile_key_request.AddProfileKeyRequest = {
            "profile_id": profile_id,
            "key_name": key_name,
            "values": values,
            "domain_name": domain_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_stream_for_segments(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        destination_arn: "capo_customer_profiles.types.destination_arn_string.DestinationArnString",
        destination_role_arn: "capo_customer_profiles.types.destination_role_arn.DestinationRoleArn",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.associate_stream_for_segments_response.AssociateStreamForSegmentsResponse":
        """<p>Associates an Amazon Kinesis data stream to receive segment membership events for a given domain. This is a domain-level configuration that applies to all segment subscriptions within the domain. A domain can have only one associated stream at a time. </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            destination_arn: <p>The Amazon Resource Name (ARN) of the Amazon Kinesis data stream to deliver segment membership events to. For example, <code>arn:aws:kinesis:region:account-id:stream/stream-name</code>. </p>
            destination_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that allows Customer Profiles service principal to assume the role for conducting AWS Key Management Service (KMS) and Amazon Kinesis operations. The role must grant the following Amazon Kinesis permissions to deliver segment membership events to the stream: </p> <ul> <li> <p> <code>kinesis:PutRecord</code> </p> </li> <li> <p> <code>kinesis:PutRecords</code> </p> </li> <li> <p> <code>kinesis:DescribeStream</code> </p> </li> </ul>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.associate_stream_for_segments_request.AssociateStreamForSegmentsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.associate_stream_for_segments_response.AssociateStreamForSegmentsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.associate_stream_for_segments

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.associate_stream_for_segments.associate_stream_for_segments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.associate_stream_for_segments_request.AssociateStreamForSegmentsRequest = {
            "domain_name": domain_name,
            "destination_arn": destination_arn,
            "destination_role_arn": destination_role_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_calculated_attribute_for_profile(
        self,
        calculated_attribute_name: "capo_customer_profiles.types.type_name.typeName",
        domain_name: "capo_customer_profiles.types.name.name",
        profile_ids: "capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_id_list.BatchGetCalculatedAttributeForProfileIdList",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        condition_overrides: Optional[
            "capo_customer_profiles.types.condition_overrides.ConditionOverrides"
        ] = None,
    ) -> "capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_response.BatchGetCalculatedAttributeForProfileResponse":
        """<p>Fetch the possible attribute values given the attribute name.</p>

        Args:
            calculated_attribute_name: <p>The unique name of the calculated attribute.</p>
            domain_name: <p>The unique name of the domain.</p>
            profile_ids: <p>List of unique identifiers for customer profiles to retrieve.</p>
            condition_overrides: <p>Overrides the condition block within the original calculated attribute definition.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_request.BatchGetCalculatedAttributeForProfileRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_response.BatchGetCalculatedAttributeForProfileResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.batch_get_calculated_attribute_for_profile

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.batch_get_calculated_attribute_for_profile.batch_get_calculated_attribute_for_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.batch_get_calculated_attribute_for_profile_request.BatchGetCalculatedAttributeForProfileRequest = {
            "calculated_attribute_name": calculated_attribute_name,
            "domain_name": domain_name,
            "profile_ids": profile_ids,
        }
        if condition_overrides is not None:
            input_["condition_overrides"] = condition_overrides

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_profile(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        profile_ids: "capo_customer_profiles.types.batch_get_profile_id_list.BatchGetProfileIdList",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.batch_get_profile_response.BatchGetProfileResponse":
        """<p>Get a batch of profiles.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            profile_ids: <p>List of unique identifiers for customer profiles to retrieve.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.batch_get_profile_request.BatchGetProfileRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.batch_get_profile_response.BatchGetProfileResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.batch_get_profile

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.batch_get_profile.batch_get_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.batch_get_profile_request.BatchGetProfileRequest = {
            "domain_name": domain_name,
            "profile_ids": profile_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_put_profile_object(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        items: "capo_customer_profiles.types.batch_put_profile_object_request_item_list.BatchPutProfileObjectRequestItemList",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.batch_put_profile_object_response.BatchPutProfileObjectResponse":
        """<p>Adds multiple profile objects to a domain of a given ObjectType in a single API call.</p> <p>When adding a specific profile object, like a Contact Record, an inferred profile can get created if it is not mapped to an existing profile. The resulting profile will only have a phone number populated in the standard ProfileObject. Any additional Contact Records with the same phone number will be mapped to the same inferred profile.</p> <p>When a ProfileObject is created and if a ProfileObjectType already exists for the ProfileObject, it will provide data to a standard profile depending on the ProfileObjectType definition.</p> <p>BatchPutProfileObject needs an ObjectType, which can be created using PutProfileObjectType.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            object_type_name: <p>The name of the profile object type.</p>
            items: <p>A list of items to add to the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.batch_put_profile_object_request.BatchPutProfileObjectRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.batch_put_profile_object_response.BatchPutProfileObjectResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.batch_put_profile_object

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.batch_put_profile_object.batch_put_profile_object(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.batch_put_profile_object_request.BatchPutProfileObjectRequest = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
            "items": items,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_calculated_attribute_definition(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        calculated_attribute_name: "capo_customer_profiles.types.type_name.typeName",
        attribute_details: "capo_customer_profiles.types.attribute_details.AttributeDetails",
        statistic: "capo_customer_profiles.types.statistic.Statistic",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        display_name: Optional[
            "capo_customer_profiles.types.display_name.displayName"
        ] = None,
        description: Optional[
            "capo_customer_profiles.types.sensitive_text.sensitiveText"
        ] = None,
        conditions: Optional[
            "capo_customer_profiles.types.conditions.Conditions"
        ] = None,
        filter: Optional["capo_customer_profiles.types.filter.Filter"] = None,
        use_historical_data: Optional[
            "capo_customer_profiles.types.optional_boolean.optionalBoolean"
        ] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.create_calculated_attribute_definition_response.CreateCalculatedAttributeDefinitionResponse":
        """<p>Creates a new calculated attribute definition. After creation, new object data ingested into Customer Profiles will be included in the calculated attribute, which can be retrieved for a profile using the <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetCalculatedAttributeForProfile.html">GetCalculatedAttributeForProfile</a> API. Defining a calculated attribute makes it available for all profiles within a domain. Each calculated attribute can only reference one <code>ObjectType</code> and at most, two fields from that <code>ObjectType</code>.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            calculated_attribute_name: <p>The unique name of the calculated attribute.</p>
            display_name: <p>The display name of the calculated attribute.</p>
            description: <p>The description of the calculated attribute.</p>
            attribute_details: <p>Mathematical expression and a list of attribute items specified in that expression.</p>
            conditions: <p>The conditions including range, object count, and threshold for the calculated attribute.</p>
            filter: <p>Defines how to filter incoming objects to include part of the Calculated Attribute.</p>
            statistic: <p>The aggregation operation to perform for the calculated attribute.</p>
            use_historical_data: <p>Whether historical data ingested before the Calculated Attribute was created should be included in calculations.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_calculated_attribute_definition_request.CreateCalculatedAttributeDefinitionRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_calculated_attribute_definition_response.CreateCalculatedAttributeDefinitionResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_calculated_attribute_definition

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_calculated_attribute_definition.create_calculated_attribute_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_calculated_attribute_definition_request.CreateCalculatedAttributeDefinitionRequest = {
            "domain_name": domain_name,
            "calculated_attribute_name": calculated_attribute_name,
            "attribute_details": attribute_details,
            "statistic": statistic,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if conditions is not None:
            input_["conditions"] = conditions
        if filter is not None:
            input_["filter"] = filter
        if use_historical_data is not None:
            input_["use_historical_data"] = use_historical_data
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_domain(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        default_expiration_days: "capo_customer_profiles.types.expiration_days_integer.expirationDaysInteger",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        default_encryption_key: Optional[
            "capo_customer_profiles.types.encryption_key.encryptionKey"
        ] = None,
        dead_letter_queue_url: Optional[
            "capo_customer_profiles.types.sqs_queue_url.sqsQueueUrl"
        ] = None,
        matching: Optional[
            "capo_customer_profiles.types.matching_request.MatchingRequest"
        ] = None,
        rule_based_matching: Optional[
            "capo_customer_profiles.types.rule_based_matching_request.RuleBasedMatchingRequest"
        ] = None,
        data_store: Optional[
            "capo_customer_profiles.types.data_store_request.DataStoreRequest"
        ] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.create_domain_response.CreateDomainResponse":
        """<p>Creates a domain, which is a container for all customer data, such as customer profile attributes, object types, profile keys, and encryption keys. You can create multiple domains, and each domain can have multiple third-party integrations.</p> <p>Each Connect Customer instance can be associated with only one domain. Multiple Connect Customer instances can be associated with one domain.</p> <p>Use this API or <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html">UpdateDomain</a> to enable <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html">identity resolution</a>: set <code>Matching</code> to true.</p> <p>To prevent cross-service impersonation when you call this API, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html">Cross-service confused deputy prevention</a> for sample policies that you should apply. </p> <note> <p>It is not possible to associate a Customer Profiles domain with an Amazon Connect Instance directly from the API. If you would like to create a domain and associate a Customer Profiles domain, use the Amazon Connect admin website. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-customer-profiles.html#enable-customer-profiles-step1">Enable Customer Profiles</a>.</p> <p>Each Amazon Connect instance can be associated with only one domain. Multiple Amazon Connect instances can be associated with one domain.</p> </note>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            default_expiration_days: <p>The default number of days until the data within the domain expires.</p>
            default_encryption_key: <p>The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage.</p>
            dead_letter_queue_url: <p>The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications. You must set up a policy on the DeadLetterQueue for the SendMessage operation to enable Amazon Connect Customer Profiles to send messages to the DeadLetterQueue.</p>
            matching: <p>The process of matching duplicate profiles. If <code>Matching</code> = <code>true</code>, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains. </p> <p>After the Identity Resolution Job completes, use the <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html">GetMatches</a> API to return and review the results. Or, if you have configured <code>ExportingConfig</code> in the <code>MatchingRequest</code>, you can download the results from S3.</p>
            rule_based_matching: <p>The process of matching duplicate profiles using the Rule-Based matching. If <code>RuleBasedMatching</code> = true, Connect Customer Customer Profiles will start to match and merge your profiles according to your configuration in the <code>RuleBasedMatchingRequest</code>. You can use the <code>ListRuleBasedMatches</code> and <code>GetSimilarProfiles</code> API to return and review the results. Also, if you have configured <code>ExportingConfig</code> in the <code>RuleBasedMatchingRequest</code>, you can download the results from S3.</p>
            data_store: <p>Set to true to enabled data store for this domain.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_domain_request.CreateDomainRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_domain_response.CreateDomainResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_domain

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_domain.create_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_domain_request.CreateDomainRequest = {
            "domain_name": domain_name,
            "default_expiration_days": default_expiration_days,
        }
        if default_encryption_key is not None:
            input_["default_encryption_key"] = default_encryption_key
        if dead_letter_queue_url is not None:
            input_["dead_letter_queue_url"] = dead_letter_queue_url
        if matching is not None:
            input_["matching"] = matching
        if rule_based_matching is not None:
            input_["rule_based_matching"] = rule_based_matching
        if data_store is not None:
            input_["data_store"] = data_store
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_domain_layout(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        layout_definition_name: "capo_customer_profiles.types.name.name",
        description: "capo_customer_profiles.types.sensitive_text.sensitiveText",
        display_name: "capo_customer_profiles.types.display_name.displayName",
        layout_type: "capo_customer_profiles.types.layout_type.LayoutType",
        layout: "capo_customer_profiles.types.sensitive_string1_to2000000.sensitiveString1To2000000",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        is_default: Optional["capo_customer_profiles.types.boolean.boolean"] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.create_domain_layout_response.CreateDomainLayoutResponse":
        """<p>Creates the layout to view data for a specific domain. This API can only be invoked from the Amazon Connect admin website.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            layout_definition_name: <p>The unique name of the layout.</p>
            description: <p>The description of the layout</p>
            display_name: <p>The display name of the layout</p>
            is_default: <p>If set to true for a layout, this layout will be used by default to view data. If set to false, then the layout will not be used by default, but it can be used to view data by explicitly selecting it in the console.</p>
            layout_type: <p>The type of layout that can be used to view data under a Customer Profiles domain.</p>
            layout: <p>A customizable layout that can be used to view data under a Customer Profiles domain.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_domain_layout_request.CreateDomainLayoutRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_domain_layout_response.CreateDomainLayoutResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_domain_layout

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_domain_layout.create_domain_layout(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_domain_layout_request.CreateDomainLayoutRequest = {
            "domain_name": domain_name,
            "layout_definition_name": layout_definition_name,
            "description": description,
            "display_name": display_name,
            "layout_type": layout_type,
            "layout": layout,
        }
        if is_default is not None:
            input_["is_default"] = is_default
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_event_stream(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        uri: "capo_customer_profiles.types.string1_to255.string1To255",
        event_stream_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.create_event_stream_response.CreateEventStreamResponse":
        """<p>Creates an event stream, which is a subscription to real-time events, such as when profiles are created and updated through Connect Customer Customer Profiles.</p> <p>Each event stream can be associated with only one Kinesis Data Stream destination in the same region and Amazon Web Services account as the customer profiles domain</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            uri: <p>The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name</p>
            event_stream_name: <p>The name of the event stream.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_event_stream_request.CreateEventStreamRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_event_stream_response.CreateEventStreamResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_event_stream

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_event_stream.create_event_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_event_stream_request.CreateEventStreamRequest = {
            "domain_name": domain_name,
            "uri": uri,
            "event_stream_name": event_stream_name,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_event_trigger(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        event_trigger_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        event_trigger_conditions: "capo_customer_profiles.types.event_trigger_conditions.EventTriggerConditions",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        description: Optional[
            "capo_customer_profiles.types.sensitive_text.sensitiveText"
        ] = None,
        segment_filter: Optional["capo_customer_profiles.types.name.name"] = None,
        event_trigger_limits: Optional[
            "capo_customer_profiles.types.event_trigger_limits.EventTriggerLimits"
        ] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.create_event_trigger_response.CreateEventTriggerResponse":
        """<p>Creates an event trigger, which specifies the rules when to perform action based on customer's ingested data.</p> <p>Each event stream can be associated with only one integration in the same region and AWS account as the event stream. </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            event_trigger_name: <p>The unique name of the event trigger.</p>
            object_type_name: <p>The unique name of the object type.</p>
            description: <p>The description of the event trigger.</p>
            event_trigger_conditions: <p>A list of conditions that determine when an event should trigger the destination.</p>
            segment_filter: <p>The destination is triggered only for profiles that meet the criteria of a segment definition.</p>
            event_trigger_limits: <p>Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.</p>
            tags: <p>An array of key-value pairs to apply to this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_event_trigger_request.CreateEventTriggerRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_event_trigger_response.CreateEventTriggerResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_event_trigger

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_event_trigger.create_event_trigger(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_event_trigger_request.CreateEventTriggerRequest = {
            "domain_name": domain_name,
            "event_trigger_name": event_trigger_name,
            "object_type_name": object_type_name,
            "event_trigger_conditions": event_trigger_conditions,
        }
        if description is not None:
            input_["description"] = description
        if segment_filter is not None:
            input_["segment_filter"] = segment_filter
        if event_trigger_limits is not None:
            input_["event_trigger_limits"] = event_trigger_limits
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_integration_workflow(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        workflow_type: "capo_customer_profiles.types.workflow_type.WorkflowType",
        integration_config: "capo_customer_profiles.types.integration_config.IntegrationConfig",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        role_arn: "capo_customer_profiles.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.create_integration_workflow_response.CreateIntegrationWorkflowResponse":
        """<p> Creates an integration workflow. An integration workflow is an async process which ingests historic data and sets up an integration for ongoing updates. The supported Amazon AppFlow sources are Salesforce, ServiceNow, and Marketo. </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            workflow_type: <p>The type of workflow. The only supported value is APPFLOW_INTEGRATION.</p>
            integration_config: <p>Configuration data for integration workflow.</p>
            object_type_name: <p>The name of the profile object type.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role. Customer Profiles assumes this role to create resources on your behalf as part of workflow execution.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_integration_workflow_request.CreateIntegrationWorkflowRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_integration_workflow_response.CreateIntegrationWorkflowResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_integration_workflow

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_integration_workflow.create_integration_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_integration_workflow_request.CreateIntegrationWorkflowRequest = {
            "domain_name": domain_name,
            "workflow_type": workflow_type,
            "integration_config": integration_config,
            "object_type_name": object_type_name,
            "role_arn": role_arn,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_profile(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        account_number: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        additional_information: Optional[
            "capo_customer_profiles.types.sensitive_string1_to1000.sensitiveString1To1000"
        ] = None,
        party_type: Optional[
            "capo_customer_profiles.types.party_type.PartyType"
        ] = None,
        business_name: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        first_name: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        middle_name: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        last_name: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        birth_date: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        gender: Optional["capo_customer_profiles.types.gender.Gender"] = None,
        phone_number: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        mobile_phone_number: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        home_phone_number: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        business_phone_number: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        email_address: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        personal_email_address: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        business_email_address: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        address: Optional["capo_customer_profiles.types.address.Address"] = None,
        shipping_address: Optional[
            "capo_customer_profiles.types.address.Address"
        ] = None,
        mailing_address: Optional[
            "capo_customer_profiles.types.address.Address"
        ] = None,
        billing_address: Optional[
            "capo_customer_profiles.types.address.Address"
        ] = None,
        attributes: Optional[
            "capo_customer_profiles.types.attributes.Attributes"
        ] = None,
        party_type_string: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        gender_string: Optional[
            "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
        ] = None,
        profile_type: Optional[
            "capo_customer_profiles.types.profile_type.ProfileType"
        ] = None,
        engagement_preferences: Optional[
            "capo_customer_profiles.types.engagement_preferences.EngagementPreferences"
        ] = None,
    ) -> "capo_customer_profiles.types.create_profile_response.CreateProfileResponse":
        """<p>Creates a standard profile.</p> <p>A standard profile represents the following attributes for a customer profile in a domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            account_number: <p>An account number that you have assigned to the customer.</p>
            additional_information: <p>Any additional information relevant to the customer’s profile.</p>
            party_type: <p>The type of profile used to describe the customer.</p>
            business_name: <p>The name of the customer’s business.</p>
            first_name: <p>The customer’s first name.</p>
            middle_name: <p>The customer’s middle name.</p>
            last_name: <p>The customer’s last name.</p>
            birth_date: <p>The customer’s birth date. </p>
            gender: <p>The gender with which the customer identifies. </p>
            phone_number: <p>The customer’s phone number, which has not been specified as a mobile, home, or business number. </p>
            mobile_phone_number: <p>The customer’s mobile phone number.</p>
            home_phone_number: <p>The customer’s home phone number.</p>
            business_phone_number: <p>The customer’s business phone number.</p>
            email_address: <p>The customer’s email address, which has not been specified as a personal or business address. </p>
            personal_email_address: <p>The customer’s personal email address.</p>
            business_email_address: <p>The customer’s business email address.</p>
            address: <p>A generic address associated with the customer that is not mailing, shipping, or billing.</p>
            shipping_address: <p>The customer’s shipping address.</p>
            mailing_address: <p>The customer’s mailing address.</p>
            billing_address: <p>The customer’s billing address.</p>
            attributes: <p>A key value pair of attributes of a customer profile.</p>
            party_type_string: <p>An alternative to <code>PartyType</code> which accepts any string as input.</p>
            gender_string: <p>An alternative to <code>Gender</code> which accepts any string as input.</p>
            profile_type: <p>The type of the profile.</p>
            engagement_preferences: <p>Object that defines the preferred methods of engagement, per channel.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_profile_request.CreateProfileRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_profile_response.CreateProfileResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_profile

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_profile.create_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_profile_request.CreateProfileRequest = {
            "domain_name": domain_name
        }
        if account_number is not None:
            input_["account_number"] = account_number
        if additional_information is not None:
            input_["additional_information"] = additional_information
        if party_type is not None:
            input_["party_type"] = party_type
        if business_name is not None:
            input_["business_name"] = business_name
        if first_name is not None:
            input_["first_name"] = first_name
        if middle_name is not None:
            input_["middle_name"] = middle_name
        if last_name is not None:
            input_["last_name"] = last_name
        if birth_date is not None:
            input_["birth_date"] = birth_date
        if gender is not None:
            input_["gender"] = gender
        if phone_number is not None:
            input_["phone_number"] = phone_number
        if mobile_phone_number is not None:
            input_["mobile_phone_number"] = mobile_phone_number
        if home_phone_number is not None:
            input_["home_phone_number"] = home_phone_number
        if business_phone_number is not None:
            input_["business_phone_number"] = business_phone_number
        if email_address is not None:
            input_["email_address"] = email_address
        if personal_email_address is not None:
            input_["personal_email_address"] = personal_email_address
        if business_email_address is not None:
            input_["business_email_address"] = business_email_address
        if address is not None:
            input_["address"] = address
        if shipping_address is not None:
            input_["shipping_address"] = shipping_address
        if mailing_address is not None:
            input_["mailing_address"] = mailing_address
        if billing_address is not None:
            input_["billing_address"] = billing_address
        if attributes is not None:
            input_["attributes"] = attributes
        if party_type_string is not None:
            input_["party_type_string"] = party_type_string
        if gender_string is not None:
            input_["gender_string"] = gender_string
        if profile_type is not None:
            input_["profile_type"] = profile_type
        if engagement_preferences is not None:
            input_["engagement_preferences"] = engagement_preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_recommender(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_name: "capo_customer_profiles.types.name.name",
        recommender_recipe_name: "capo_customer_profiles.types.recommender_recipe_name.RecommenderRecipeName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        recommender_config: Optional[
            "capo_customer_profiles.types.recommender_config.RecommenderConfig"
        ] = None,
        description: Optional[
            "capo_customer_profiles.types.sensitive_text.sensitiveText"
        ] = None,
        recommender_schema_name: Optional[
            "capo_customer_profiles.types.name.name"
        ] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.create_recommender_response.CreateRecommenderResponse":
        """<p>Creates a recommender</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_name: <p>The name of the recommender.</p>
            recommender_recipe_name: <p>The name of the recommeder recipe.</p>
            recommender_config: <p>The recommender configuration.</p>
            description: <p>The description of the domain object type.</p>
            recommender_schema_name: <p>The name of the recommender schema to use for this recommender. If not specified, the default schema is used.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_recommender_request.CreateRecommenderRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_recommender_response.CreateRecommenderResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_recommender

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_recommender.create_recommender(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_recommender_request.CreateRecommenderRequest = {
            "domain_name": domain_name,
            "recommender_name": recommender_name,
            "recommender_recipe_name": recommender_recipe_name,
        }
        if recommender_config is not None:
            input_["recommender_config"] = recommender_config
        if description is not None:
            input_["description"] = description
        if recommender_schema_name is not None:
            input_["recommender_schema_name"] = recommender_schema_name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_recommender_filter(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_filter_name: "capo_customer_profiles.types.recommender_filter_name.RecommenderFilterName",
        recommender_filter_expression: "capo_customer_profiles.types.recommender_filter_expression.RecommenderFilterExpression",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        recommender_schema_name: Optional[
            "capo_customer_profiles.types.name.name"
        ] = None,
        description: Optional[
            "capo_customer_profiles.types.sensitive_text.sensitiveText"
        ] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.create_recommender_filter_response.CreateRecommenderFilterResponse":
        """<p>Creates a recommender filter. A recommender filter specifies which items to include or exclude from recommendations.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_filter_name: <p>The name of the recommender filter. The name must be unique within the domain.</p>
            recommender_filter_expression: <p>The filter expression that defines which items to include or exclude from recommendations.</p>
            recommender_schema_name: <p>The name of the recommender schema to use for this recommender filter. If not specified, the default schema is used.</p>
            description: <p>A description of the recommender filter.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_recommender_filter_request.CreateRecommenderFilterRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_recommender_filter_response.CreateRecommenderFilterResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_recommender_filter

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_recommender_filter.create_recommender_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_recommender_filter_request.CreateRecommenderFilterRequest = {
            "domain_name": domain_name,
            "recommender_filter_name": recommender_filter_name,
            "recommender_filter_expression": recommender_filter_expression,
        }
        if recommender_schema_name is not None:
            input_["recommender_schema_name"] = recommender_schema_name
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

    def create_recommender_schema(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_schema_name: "capo_customer_profiles.types.name.name",
        fields: "capo_customer_profiles.types.recommender_schema_fields.RecommenderSchemaFields",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.create_recommender_schema_response.CreateRecommenderSchemaResponse":
        """<p>Creates a recommender schema. A recommender schema defines the set of data columns available for training recommenders and filters under a domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_schema_name: <p>The name of the recommender schema. The name must be unique within the domain.</p>
            fields: <p>A map of dataset type to column definitions that specifies which data columns to include in the schema. The <code>_webAnalytics</code> and <code>_catalogItem</code> keys are supported.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_recommender_schema_request.CreateRecommenderSchemaRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_recommender_schema_response.CreateRecommenderSchemaResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_recommender_schema

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_recommender_schema.create_recommender_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_recommender_schema_request.CreateRecommenderSchemaRequest = {
            "domain_name": domain_name,
            "recommender_schema_name": recommender_schema_name,
            "fields": fields,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_segment_definition(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        segment_definition_name: "capo_customer_profiles.types.name.name",
        display_name: "capo_customer_profiles.types.string1_to255.string1To255",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        description: Optional[
            "capo_customer_profiles.types.sensitive_string1_to4000.sensitiveString1To4000"
        ] = None,
        segment_groups: Optional[
            "capo_customer_profiles.types.segment_group.SegmentGroup"
        ] = None,
        segment_sql_query: Optional[
            "capo_customer_profiles.types.sensitive_string1_to50000.sensitiveString1To50000"
        ] = None,
        segment_sort: Optional[
            "capo_customer_profiles.types.segment_sort.SegmentSort"
        ] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.create_segment_definition_response.CreateSegmentDefinitionResponse":
        """<p>Creates a segment definition associated to the given domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            segment_definition_name: <p>The unique name of the segment definition.</p>
            display_name: <p>The display name of the segment definition.</p>
            description: <p>The description of the segment definition.</p>
            segment_groups: <p>Specifies the base segments and dimensions for a segment definition along with their respective relationship.</p>
            segment_sql_query: <p>The segment SQL query.</p>
            segment_sort: <p>The segment sort.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_segment_definition_request.CreateSegmentDefinitionRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_segment_definition_response.CreateSegmentDefinitionResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_segment_definition

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_segment_definition.create_segment_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_segment_definition_request.CreateSegmentDefinitionRequest = {
            "domain_name": domain_name,
            "segment_definition_name": segment_definition_name,
            "display_name": display_name,
        }
        if description is not None:
            input_["description"] = description
        if segment_groups is not None:
            input_["segment_groups"] = segment_groups
        if segment_sql_query is not None:
            input_["segment_sql_query"] = segment_sql_query
        if segment_sort is not None:
            input_["segment_sort"] = segment_sort
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_segment_estimate(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        segment_query: Optional[
            "capo_customer_profiles.types.segment_group_structure.SegmentGroupStructure"
        ] = None,
        segment_sql_query: Optional[
            "capo_customer_profiles.types.sensitive_string1_to50000.sensitiveString1To50000"
        ] = None,
    ) -> "capo_customer_profiles.types.create_segment_estimate_response.CreateSegmentEstimateResponse":
        """<p>Creates a segment estimate query.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            segment_query: <p>The segment query for calculating a segment estimate.</p>
            segment_sql_query: <p>The segment SQL query.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_segment_estimate_request.CreateSegmentEstimateRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_segment_estimate_response.CreateSegmentEstimateResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_segment_estimate

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_segment_estimate.create_segment_estimate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_segment_estimate_request.CreateSegmentEstimateRequest = {
            "domain_name": domain_name
        }
        if segment_query is not None:
            input_["segment_query"] = segment_query
        if segment_sql_query is not None:
            input_["segment_sql_query"] = segment_sql_query

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_segment_snapshot(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        segment_definition_name: "capo_customer_profiles.types.name.name",
        data_format: "capo_customer_profiles.types.data_format.DataFormat",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        encryption_key: Optional[
            "capo_customer_profiles.types.encryption_key.encryptionKey"
        ] = None,
        role_arn: Optional["capo_customer_profiles.types.role_arn.RoleArn"] = None,
        destination_uri: Optional[
            "capo_customer_profiles.types.string1_to255.string1To255"
        ] = None,
    ) -> "capo_customer_profiles.types.create_segment_snapshot_response.CreateSegmentSnapshotResponse":
        """<p>Triggers a job to export a segment to a specified destination.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            segment_definition_name: <p>The name of the segment definition used in this snapshot request.</p>
            data_format: <p>The format in which the segment will be exported.</p>
            encryption_key: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the exported segment.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that allows Customer Profiles service principal to assume the role for conducting KMS and S3 operations.</p>
            destination_uri: <p>The destination to which the segment will be exported. This field must be provided if the request is not submitted from the Connect Customer Admin Website.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_segment_snapshot_request.CreateSegmentSnapshotRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_segment_snapshot_response.CreateSegmentSnapshotResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_segment_snapshot

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_segment_snapshot.create_segment_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_segment_snapshot_request.CreateSegmentSnapshotRequest = {
            "domain_name": domain_name,
            "segment_definition_name": segment_definition_name,
            "data_format": data_format,
        }
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if destination_uri is not None:
            input_["destination_uri"] = destination_uri

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_upload_job(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        display_name: "capo_customer_profiles.types.string1_to255.string1To255",
        fields: "capo_customer_profiles.types.field_map.FieldMap",
        unique_key: "capo_customer_profiles.types.text.text",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        data_expiry: Optional[
            "capo_customer_profiles.types.expiration_days_integer.expirationDaysInteger"
        ] = None,
    ) -> "capo_customer_profiles.types.create_upload_job_response.CreateUploadJobResponse":
        """<p>Creates an Upload job to ingest data for segment imports. The metadata is created for the job with the provided field mapping and unique key. </p>

        Args:
            domain_name: <p>The unique name of the domain. Domain should be exists for the upload job to be created. </p>
            display_name: <p>The unique name of the upload job. Could be a file name to identify the upload job.</p>
            fields: <p>The mapping between CSV Columns and Profile Object attributes. A map of the name and ObjectType field.</p>
            unique_key: <p>The unique key columns for de-duping the profiles used to map data to the profile. </p>
            data_expiry: <p>The expiry duration for the profiles ingested with the job. If not provided, the system default of 2 weeks is used. </p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.create_upload_job_request.CreateUploadJobRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.create_upload_job_response.CreateUploadJobResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.create_upload_job

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.create_upload_job.create_upload_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.create_upload_job_request.CreateUploadJobRequest = {
            "domain_name": domain_name,
            "display_name": display_name,
            "fields": fields,
            "unique_key": unique_key,
        }
        if data_expiry is not None:
            input_["data_expiry"] = data_expiry

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_calculated_attribute_definition(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        calculated_attribute_name: "capo_customer_profiles.types.type_name.typeName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_calculated_attribute_definition_response.DeleteCalculatedAttributeDefinitionResponse":
        """<p>Deletes an existing calculated attribute definition. Note that deleting a default calculated attribute is possible, however once deleted, you will be unable to undo that action and will need to recreate it on your own using the CreateCalculatedAttributeDefinition API if you want it back.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            calculated_attribute_name: <p>The unique name of the calculated attribute.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_calculated_attribute_definition_request.DeleteCalculatedAttributeDefinitionRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_calculated_attribute_definition_response.DeleteCalculatedAttributeDefinitionResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_calculated_attribute_definition

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_calculated_attribute_definition.delete_calculated_attribute_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_calculated_attribute_definition_request.DeleteCalculatedAttributeDefinitionRequest = {
            "domain_name": domain_name,
            "calculated_attribute_name": calculated_attribute_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_domain(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_domain_response.DeleteDomainResponse":
        """<p>Deletes a specific domain and all of its customer data, such as customer profile attributes and their related objects.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_domain_request.DeleteDomainRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_domain_response.DeleteDomainResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_domain

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_domain.delete_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_domain_request.DeleteDomainRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_domain_layout(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        layout_definition_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_domain_layout_response.DeleteDomainLayoutResponse":
        """<p>Deletes the layout used to view data for a specific domain. This API can only be invoked from the Amazon Connect admin website.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            layout_definition_name: <p>The unique name of the layout.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_domain_layout_request.DeleteDomainLayoutRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_domain_layout_response.DeleteDomainLayoutResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_domain_layout

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_domain_layout.delete_domain_layout(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_domain_layout_request.DeleteDomainLayoutRequest = {
            "domain_name": domain_name,
            "layout_definition_name": layout_definition_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_domain_object_type(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_domain_object_type_response.DeleteDomainObjectTypeResponse":
        """<p>Delete a DomainObjectType for the given Domain and ObjectType name.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            object_type_name: <p>The unique name of the domain object type.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_domain_object_type_request.DeleteDomainObjectTypeRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_domain_object_type_response.DeleteDomainObjectTypeResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_domain_object_type

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_domain_object_type.delete_domain_object_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_domain_object_type_request.DeleteDomainObjectTypeRequest = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event_stream(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        event_stream_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_event_stream_response.DeleteEventStreamResponse":
        """<p>Disables and deletes the specified event stream.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            event_stream_name: <p>The name of the event stream</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_event_stream_request.DeleteEventStreamRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_event_stream_response.DeleteEventStreamResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_event_stream

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_event_stream.delete_event_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_event_stream_request.DeleteEventStreamRequest = {
            "domain_name": domain_name,
            "event_stream_name": event_stream_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event_trigger(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        event_trigger_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_event_trigger_response.DeleteEventTriggerResponse":
        """<p>Disable and deletes the Event Trigger.</p> <note> <p>You cannot delete an Event Trigger with an active Integration associated.</p> </note>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            event_trigger_name: <p>The unique name of the event trigger.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_event_trigger_request.DeleteEventTriggerRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_event_trigger_response.DeleteEventTriggerResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_event_trigger

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_event_trigger.delete_event_trigger(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_event_trigger_request.DeleteEventTriggerRequest = {
            "domain_name": domain_name,
            "event_trigger_name": event_trigger_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_integration(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        uri: "capo_customer_profiles.types.string1_to255.string1To255",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_integration_response.DeleteIntegrationResponse":
        """<p>Removes an integration from a specific domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            uri: <p>The URI of the S3 bucket or any other type of data source.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_integration_request.DeleteIntegrationRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_integration_response.DeleteIntegrationResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_integration

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_integration.delete_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_integration_request.DeleteIntegrationRequest = {
            "domain_name": domain_name,
            "uri": uri,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_profile(
        self,
        profile_id: "capo_customer_profiles.types.uuid.uuid",
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_profile_response.DeleteProfileResponse":
        """<p>Deletes the standard customer profile and all data pertaining to the profile.</p>

        Args:
            profile_id: <p>The unique identifier of a customer profile.</p>
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_profile_request.DeleteProfileRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_profile_response.DeleteProfileResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_profile

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_profile.delete_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_profile_request.DeleteProfileRequest = {
            "profile_id": profile_id,
            "domain_name": domain_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_profile_key(
        self,
        profile_id: "capo_customer_profiles.types.uuid.uuid",
        key_name: "capo_customer_profiles.types.name.name",
        values: "capo_customer_profiles.types.request_value_list.requestValueList",
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_profile_key_response.DeleteProfileKeyResponse":
        """<p>Removes a searchable key from a customer profile.</p>

        Args:
            profile_id: <p>The unique identifier of a customer profile.</p>
            key_name: <p>A searchable identifier of a customer profile.</p>
            values: <p>A list of key values.</p>
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_profile_key_request.DeleteProfileKeyRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_profile_key_response.DeleteProfileKeyResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_profile_key

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_profile_key.delete_profile_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_profile_key_request.DeleteProfileKeyRequest = {
            "profile_id": profile_id,
            "key_name": key_name,
            "values": values,
            "domain_name": domain_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_profile_object(
        self,
        profile_id: "capo_customer_profiles.types.uuid.uuid",
        profile_object_unique_key: "capo_customer_profiles.types.string1_to255.string1To255",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_profile_object_response.DeleteProfileObjectResponse":
        """<p>Removes an object associated with a profile of a given ProfileObjectType.</p>

        Args:
            profile_id: <p>The unique identifier of a customer profile.</p>
            profile_object_unique_key: <p>The unique identifier of the profile object generated by the service.</p>
            object_type_name: <p>The name of the profile object type.</p>
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_profile_object_request.DeleteProfileObjectRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_profile_object_response.DeleteProfileObjectResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_profile_object

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_profile_object.delete_profile_object(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_profile_object_request.DeleteProfileObjectRequest = {
            "profile_id": profile_id,
            "profile_object_unique_key": profile_object_unique_key,
            "object_type_name": object_type_name,
            "domain_name": domain_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_profile_object_type(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_profile_object_type_response.DeleteProfileObjectTypeResponse":
        """<p>Removes a ProfileObjectType from a specific domain as well as removes all the ProfileObjects of that type. It also disables integrations from this specific ProfileObjectType. In addition, it scrubs all of the fields of the standard profile that were populated from this ProfileObjectType.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            object_type_name: <p>The name of the profile object type.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_profile_object_type_request.DeleteProfileObjectTypeRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_profile_object_type_response.DeleteProfileObjectTypeResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_profile_object_type

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_profile_object_type.delete_profile_object_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_profile_object_type_request.DeleteProfileObjectTypeRequest = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_recommender(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_recommender_response.DeleteRecommenderResponse":
        """<p>Deletes a recommender.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_name: <p>The recommender name.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_recommender_request.DeleteRecommenderRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_recommender_response.DeleteRecommenderResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_recommender

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_recommender.delete_recommender(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_recommender_request.DeleteRecommenderRequest = {
            "domain_name": domain_name,
            "recommender_name": recommender_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_recommender_filter(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_filter_name: "capo_customer_profiles.types.recommender_filter_name.RecommenderFilterName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_recommender_filter_response.DeleteRecommenderFilterResponse":
        """<p>Deletes a recommender filter from a domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_filter_name: <p>The name of the recommender filter to delete.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_recommender_filter_request.DeleteRecommenderFilterRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_recommender_filter_response.DeleteRecommenderFilterResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_recommender_filter

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_recommender_filter.delete_recommender_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_recommender_filter_request.DeleteRecommenderFilterRequest = {
            "domain_name": domain_name,
            "recommender_filter_name": recommender_filter_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_recommender_schema(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_schema_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_recommender_schema_response.DeleteRecommenderSchemaResponse":
        """<p>Deletes a recommender schema from a domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_schema_name: <p>The name of the recommender schema to delete.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_recommender_schema_request.DeleteRecommenderSchemaRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_recommender_schema_response.DeleteRecommenderSchemaResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_recommender_schema

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_recommender_schema.delete_recommender_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_recommender_schema_request.DeleteRecommenderSchemaRequest = {
            "domain_name": domain_name,
            "recommender_schema_name": recommender_schema_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_segment_definition(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        segment_definition_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_segment_definition_response.DeleteSegmentDefinitionResponse":
        """<p>Deletes a segment definition from the domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            segment_definition_name: <p>The unique name of the segment definition.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_segment_definition_request.DeleteSegmentDefinitionRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_segment_definition_response.DeleteSegmentDefinitionResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_segment_definition

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_segment_definition.delete_segment_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_segment_definition_request.DeleteSegmentDefinitionRequest = {
            "domain_name": domain_name,
            "segment_definition_name": segment_definition_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_segment_subscription(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        segment_definition_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_segment_subscription_response.DeleteSegmentSubscriptionResponse":
        """<p>Deletes a segment subscription for membership events. All active event notifications for this segment are stopped. </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            segment_definition_name: <p>The unique name of the segment definition. </p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_segment_subscription_request.DeleteSegmentSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_segment_subscription_response.DeleteSegmentSubscriptionResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_segment_subscription

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_segment_subscription.delete_segment_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_segment_subscription_request.DeleteSegmentSubscriptionRequest = {
            "domain_name": domain_name,
            "segment_definition_name": segment_definition_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workflow(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        workflow_id: "capo_customer_profiles.types.string1_to255.string1To255",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.delete_workflow_response.DeleteWorkflowResponse":
        """<p>Deletes the specified workflow and all its corresponding resources. This is an async process.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            workflow_id: <p>Unique identifier for the workflow.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.delete_workflow_response.DeleteWorkflowResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.delete_workflow

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.delete_workflow.delete_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.delete_workflow_request.DeleteWorkflowRequest = {
            "domain_name": domain_name,
            "workflow_id": workflow_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detect_profile_object_type(
        self,
        objects: "capo_customer_profiles.types.objects.Objects",
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.detect_profile_object_type_response.DetectProfileObjectTypeResponse":
        """<p>The process of detecting profile object type mapping by using given objects.</p>

        Args:
            objects: <p>A string that is serialized from a JSON object.</p>
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.detect_profile_object_type_request.DetectProfileObjectTypeRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.detect_profile_object_type_response.DetectProfileObjectTypeResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.detect_profile_object_type

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.detect_profile_object_type.detect_profile_object_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.detect_profile_object_type_request.DetectProfileObjectTypeRequest = {
            "objects": objects,
            "domain_name": domain_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_stream_for_segments(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.disassociate_stream_for_segments_response.DisassociateStreamForSegmentsResponse":
        """<p>Disassociates the Amazon Kinesis data stream configured for segment membership events. All active segment subscriptions delivering events to this stream are eventually stopped. </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.disassociate_stream_for_segments_request.DisassociateStreamForSegmentsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.disassociate_stream_for_segments_response.DisassociateStreamForSegmentsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.disassociate_stream_for_segments

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.disassociate_stream_for_segments.disassociate_stream_for_segments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.disassociate_stream_for_segments_request.DisassociateStreamForSegmentsRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_auto_merging_preview(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        consolidation: "capo_customer_profiles.types.consolidation.Consolidation",
        conflict_resolution: "capo_customer_profiles.types.conflict_resolution.ConflictResolution",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        min_allowed_confidence_score_for_merging: Optional[
            "capo_customer_profiles.types.double0_to1.Double0To1"
        ] = None,
    ) -> "capo_customer_profiles.types.get_auto_merging_preview_response.GetAutoMergingPreviewResponse":
        """<p>Tests the auto-merging settings of your Identity Resolution Job without merging your data. It randomly selects a sample of matching groups from the existing matching results, and applies the automerging settings that you provided. You can then view the number of profiles in the sample, the number of matches, and the number of profiles identified to be merged. This enables you to evaluate the accuracy of the attributes in your matching list. </p> <p>You can't view which profiles are matched and would be merged.</p> <important> <p>We strongly recommend you use this API to do a dry run of the automerging process before running the Identity Resolution Job. Include <b>at least</b> two matching attributes. If your matching list includes too few attributes (such as only <code>FirstName</code> or only <code>LastName</code>), there may be a large number of matches. This increases the chances of erroneous merges.</p> </important>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            consolidation: <p>A list of matching attributes that represent matching criteria.</p>
            conflict_resolution: <p>How the auto-merging process should resolve conflicts between different profiles.</p>
            min_allowed_confidence_score_for_merging: <p>Minimum confidence score required for profiles within a matching group to be merged during the auto-merge process.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_auto_merging_preview_request.GetAutoMergingPreviewRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_auto_merging_preview_response.GetAutoMergingPreviewResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_auto_merging_preview

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_auto_merging_preview.get_auto_merging_preview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_auto_merging_preview_request.GetAutoMergingPreviewRequest = {
            "domain_name": domain_name,
            "consolidation": consolidation,
            "conflict_resolution": conflict_resolution,
        }
        if min_allowed_confidence_score_for_merging is not None:
            input_["min_allowed_confidence_score_for_merging"] = (
                min_allowed_confidence_score_for_merging
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_calculated_attribute_definition(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        calculated_attribute_name: "capo_customer_profiles.types.type_name.typeName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_calculated_attribute_definition_response.GetCalculatedAttributeDefinitionResponse":
        """<p>Provides more information on a calculated attribute definition for Customer Profiles.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            calculated_attribute_name: <p>The unique name of the calculated attribute.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_calculated_attribute_definition_request.GetCalculatedAttributeDefinitionRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_calculated_attribute_definition_response.GetCalculatedAttributeDefinitionResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_calculated_attribute_definition

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_calculated_attribute_definition.get_calculated_attribute_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_calculated_attribute_definition_request.GetCalculatedAttributeDefinitionRequest = {
            "domain_name": domain_name,
            "calculated_attribute_name": calculated_attribute_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_calculated_attribute_for_profile(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        profile_id: "capo_customer_profiles.types.uuid.uuid",
        calculated_attribute_name: "capo_customer_profiles.types.type_name.typeName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_calculated_attribute_for_profile_response.GetCalculatedAttributeForProfileResponse":
        """<p>Retrieve a calculated attribute for a customer profile.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            profile_id: <p>The unique identifier of a customer profile.</p>
            calculated_attribute_name: <p>The unique name of the calculated attribute.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_calculated_attribute_for_profile_request.GetCalculatedAttributeForProfileRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_calculated_attribute_for_profile_response.GetCalculatedAttributeForProfileResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_calculated_attribute_for_profile

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_calculated_attribute_for_profile.get_calculated_attribute_for_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_calculated_attribute_for_profile_request.GetCalculatedAttributeForProfileRequest = {
            "domain_name": domain_name,
            "profile_id": profile_id,
            "calculated_attribute_name": calculated_attribute_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_domain(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_domain_response.GetDomainResponse":
        """<p>Returns information about a specific domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_domain_request.GetDomainRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_domain_response.GetDomainResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_domain

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_domain.get_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_domain_request.GetDomainRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_domain_layout(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        layout_definition_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_domain_layout_response.GetDomainLayoutResponse":
        """<p>Gets the layout to view data for a specific domain. This API can only be invoked from the Amazon Connect admin website.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            layout_definition_name: <p>The unique name of the layout.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_domain_layout_request.GetDomainLayoutRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_domain_layout_response.GetDomainLayoutResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_domain_layout

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_domain_layout.get_domain_layout(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_domain_layout_request.GetDomainLayoutRequest = {
            "domain_name": domain_name,
            "layout_definition_name": layout_definition_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_domain_object_type(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_domain_object_type_response.GetDomainObjectTypeResponse":
        """<p>Return a DomainObjectType for the input Domain and ObjectType names. </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            object_type_name: <p>The unique name of the domain object type.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_domain_object_type_request.GetDomainObjectTypeRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_domain_object_type_response.GetDomainObjectTypeResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_domain_object_type

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_domain_object_type.get_domain_object_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_domain_object_type_request.GetDomainObjectTypeRequest = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_stream(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        event_stream_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> (
        "capo_customer_profiles.types.get_event_stream_response.GetEventStreamResponse"
    ):
        """<p>Returns information about the specified event stream in a specific domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            event_stream_name: <p>The name of the event stream provided during create operations.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_event_stream_request.GetEventStreamRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_event_stream_response.GetEventStreamResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_event_stream

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_event_stream.get_event_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_event_stream_request.GetEventStreamRequest = {
            "domain_name": domain_name,
            "event_stream_name": event_stream_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_trigger(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        event_trigger_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_event_trigger_response.GetEventTriggerResponse":
        """<p>Get a specific Event Trigger from the domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            event_trigger_name: <p>The unique name of the event trigger.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_event_trigger_request.GetEventTriggerRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_event_trigger_response.GetEventTriggerResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_event_trigger

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_event_trigger.get_event_trigger(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_event_trigger_request.GetEventTriggerRequest = {
            "domain_name": domain_name,
            "event_trigger_name": event_trigger_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_identity_resolution_job(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        job_id: "capo_customer_profiles.types.uuid.uuid",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_identity_resolution_job_response.GetIdentityResolutionJobResponse":
        """<p>Returns information about an Identity Resolution Job in a specific domain. </p> <p>Identity Resolution Jobs are set up using the Amazon Connect admin console. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/use-identity-resolution.html">Use Identity Resolution to consolidate similar profiles</a>.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            job_id: <p>The unique identifier of the Identity Resolution Job.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_identity_resolution_job_request.GetIdentityResolutionJobRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_identity_resolution_job_response.GetIdentityResolutionJobResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_identity_resolution_job

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_identity_resolution_job.get_identity_resolution_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_identity_resolution_job_request.GetIdentityResolutionJobRequest = {
            "domain_name": domain_name,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_integration(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        uri: "capo_customer_profiles.types.string1_to255.string1To255",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_integration_response.GetIntegrationResponse":
        """<p>Returns an integration for a domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            uri: <p>The URI of the S3 bucket or any other type of data source.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_integration_request.GetIntegrationRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_integration_response.GetIntegrationResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_integration

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_integration.get_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_integration_request.GetIntegrationRequest = {
            "domain_name": domain_name,
            "uri": uri,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_matches(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.get_matches_response.GetMatchesResponse":
        """<p>Before calling this API, use <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html">CreateDomain</a> or <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html">UpdateDomain</a> to enable identity resolution: set <code>Matching</code> to true.</p> <p>GetMatches returns potentially matching profiles, based on the results of the latest run of a machine learning process. </p> <important> <p>The process of matching duplicate profiles. If <code>Matching</code> = <code>true</code>, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains. </p> <p>After the Identity Resolution Job completes, use the <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html">GetMatches</a> API to return and review the results. Or, if you have configured <code>ExportingConfig</code> in the <code>MatchingRequest</code>, you can download the results from S3.</p> </important> <p>Amazon Connect uses the following profile attributes to identify matches:</p> <ul> <li> <p>PhoneNumber</p> </li> <li> <p>HomePhoneNumber</p> </li> <li> <p>BusinessPhoneNumber</p> </li> <li> <p>MobilePhoneNumber</p> </li> <li> <p>EmailAddress</p> </li> <li> <p>PersonalEmailAddress</p> </li> <li> <p>BusinessEmailAddress</p> </li> <li> <p>FullName</p> </li> </ul> <p>For example, two or more profiles—with spelling mistakes such as <b>John Doe</b> and <b>Jhn Doe</b>, or different casing email addresses such as <b>JOHN_DOE@ANYCOMPANY.COM</b> and <b>johndoe@anycompany.com</b>, or different phone number formats such as <b>555-010-0000</b> and <b>+1-555-010-0000</b>—can be detected as belonging to the same customer <b>John Doe</b> and merged into a unified profile.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_matches_request.GetMatchesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_matches_response.GetMatchesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_matches

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_matches.get_matches(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_matches_request.GetMatchesRequest = {
            "domain_name": domain_name
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

    def get_object_type_attribute_statistics(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        attribute_name: "capo_customer_profiles.types.string1_to1000.string1To1000",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_object_type_attribute_statistics_response.GetObjectTypeAttributeStatisticsResponse":
        """<p>The GetObjectTypeAttributeValues API delivers statistical insights about attributes within a specific object type, but is exclusively available for domains with data store enabled. This API performs daily calculations to provide statistical information about your attribute values, helping you understand patterns and trends in your data. The statistical calculations are performed once per day, providing a consistent snapshot of your attribute data characteristics.</p> <note> <p>You'll receive null values in two scenarios: </p> <p>During the first period after enabling data vault (unless a calculation cycle occurs, which happens once daily).</p> <p>For attributes that don't contain numeric values. </p> </note>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            object_type_name: <p>The unique name of the domain object type.</p>
            attribute_name: <p>The attribute name.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_object_type_attribute_statistics_request.GetObjectTypeAttributeStatisticsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_object_type_attribute_statistics_response.GetObjectTypeAttributeStatisticsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_object_type_attribute_statistics

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_object_type_attribute_statistics.get_object_type_attribute_statistics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_object_type_attribute_statistics_request.GetObjectTypeAttributeStatisticsRequest = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
            "attribute_name": attribute_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_profile_history_record(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        profile_id: "capo_customer_profiles.types.uuid.uuid",
        id: "capo_customer_profiles.types.uuid.uuid",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_profile_history_record_response.GetProfileHistoryRecordResponse":
        """<p>Returns a history record for a specific profile, for a specific domain.</p>

        Args:
            domain_name: <p>The unique name of the domain for which to return a profile history record.</p>
            profile_id: <p>The unique identifier of the profile for which to return a history record.</p>
            id: <p>The unique identifier of the profile history record to return.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_profile_history_record_request.GetProfileHistoryRecordRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_profile_history_record_response.GetProfileHistoryRecordResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_profile_history_record

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_profile_history_record.get_profile_history_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_profile_history_record_request.GetProfileHistoryRecordRequest = {
            "domain_name": domain_name,
            "profile_id": profile_id,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_profile_object_type(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_profile_object_type_response.GetProfileObjectTypeResponse":
        """<p>Returns the object types for a specific domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            object_type_name: <p>The name of the profile object type.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_profile_object_type_request.GetProfileObjectTypeRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_profile_object_type_response.GetProfileObjectTypeResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_profile_object_type

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_profile_object_type.get_profile_object_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_profile_object_type_request.GetProfileObjectTypeRequest = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_profile_object_type_template(
        self,
        template_id: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_profile_object_type_template_response.GetProfileObjectTypeTemplateResponse":
        """<p>Returns the template information for a specific object type.</p> <p>A template is a predefined ProfileObjectType, such as “Salesforce-Account” or “Salesforce-Contact.” When a user sends a ProfileObject, using the PutProfileObject API, with an ObjectTypeName that matches one of the TemplateIds, it uses the mappings from the template.</p>

        Args:
            template_id: <p>A unique identifier for the object template.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_profile_object_type_template_request.GetProfileObjectTypeTemplateRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_profile_object_type_template_response.GetProfileObjectTypeTemplateResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_profile_object_type_template

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_profile_object_type_template.get_profile_object_type_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_profile_object_type_template_request.GetProfileObjectTypeTemplateRequest = {
            "template_id": template_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_profile_recommendations(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        profile_id: "capo_customer_profiles.types.uuid.uuid",
        recommender_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        context: Optional[
            "capo_customer_profiles.types.recommender_context.RecommenderContext"
        ] = None,
        recommender_filters: Optional[
            "capo_customer_profiles.types.recommender_filters.RecommenderFilters"
        ] = None,
        recommender_promotional_filters: Optional[
            "capo_customer_profiles.types.recommender_promotional_filters.RecommenderPromotionalFilters"
        ] = None,
        candidate_ids: Optional[
            "capo_customer_profiles.types.candidate_id_list.CandidateIdList"
        ] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size500.MaxSize500"
        ] = None,
        metadata_config: Optional[
            "capo_customer_profiles.types.metadata_config.MetadataConfig"
        ] = None,
        diversity_config: Optional[
            "capo_customer_profiles.types.recommendation_diversity_config.RecommendationDiversityConfig"
        ] = None,
    ) -> "capo_customer_profiles.types.get_profile_recommendations_response.GetProfileRecommendationsResponse":
        """<p>Fetches the recommendations for a profile in the input Customer Profiles domain. Fetches all the profile recommendations </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            profile_id: <p>The unique identifier of the profile for which to retrieve recommendations.</p>
            recommender_name: <p>The unique name of the recommender.</p>
            context: <p>The contextual metadata used to provide dynamic runtime information to tailor recommendations.</p>
            recommender_filters: <p>A list of filters to apply to the returned recommendations. Filters define criteria for including or excluding items from the recommendation results.</p>
            recommender_promotional_filters: <p>A list of promotional filters to apply to the recommendations. Promotional filters allow you to promote specific items within a configurable subset of recommendation results.</p>
            candidate_ids: <p>A list of item IDs to rank for the user. Use this when you want to re-rank a specific set of items rather than getting recommendations from the full item catalog. Required for personalized-ranking use cases.</p>
            max_results: <p>The maximum number of recommendations to return. The default value is 10.</p>
            metadata_config: <p>Configuration for including item metadata in the recommendation response. Use this to specify which metadata columns to return alongside recommended items.</p>
            diversity_config: <p>Runtime diversity configuration for this request. Enables diversity-aware recommendations and optionally supplies values for placeholder-based diversity caps configured on the recommender.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_profile_recommendations_request.GetProfileRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_profile_recommendations_response.GetProfileRecommendationsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_profile_recommendations

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_profile_recommendations.get_profile_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_profile_recommendations_request.GetProfileRecommendationsRequest = {
            "domain_name": domain_name,
            "profile_id": profile_id,
            "recommender_name": recommender_name,
        }
        if context is not None:
            input_["context"] = context
        if recommender_filters is not None:
            input_["recommender_filters"] = recommender_filters
        if recommender_promotional_filters is not None:
            input_["recommender_promotional_filters"] = recommender_promotional_filters
        if candidate_ids is not None:
            input_["candidate_ids"] = candidate_ids
        if max_results is not None:
            input_["max_results"] = max_results
        if metadata_config is not None:
            input_["metadata_config"] = metadata_config
        if diversity_config is not None:
            input_["diversity_config"] = diversity_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recommender(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        training_metrics_count: Optional[
            "capo_customer_profiles.types.get_recommender_request_training_metrics_count_integer.GetRecommenderRequestTrainingMetricsCountInteger"
        ] = None,
    ) -> "capo_customer_profiles.types.get_recommender_response.GetRecommenderResponse":
        """<p>Retrieves a recommender.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_name: <p>The name of the recommender.</p>
            training_metrics_count: <p>The number of training metrics to retrieve for the recommender.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_recommender_request.GetRecommenderRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_recommender_response.GetRecommenderResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_recommender

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_recommender.get_recommender(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_recommender_request.GetRecommenderRequest = {
            "domain_name": domain_name,
            "recommender_name": recommender_name,
        }
        if training_metrics_count is not None:
            input_["training_metrics_count"] = training_metrics_count

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recommender_filter(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_filter_name: "capo_customer_profiles.types.recommender_filter_name.RecommenderFilterName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_recommender_filter_response.GetRecommenderFilterResponse":
        """<p>Retrieves information about a specific recommender filter in a domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_filter_name: <p>The name of the recommender filter to retrieve.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_recommender_filter_request.GetRecommenderFilterRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_recommender_filter_response.GetRecommenderFilterResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_recommender_filter

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_recommender_filter.get_recommender_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_recommender_filter_request.GetRecommenderFilterRequest = {
            "domain_name": domain_name,
            "recommender_filter_name": recommender_filter_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recommender_schema(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_schema_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_recommender_schema_response.GetRecommenderSchemaResponse":
        """<p>Retrieves information about a specific recommender schema in a domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_schema_name: <p>The name of the recommender schema to retrieve.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_recommender_schema_request.GetRecommenderSchemaRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_recommender_schema_response.GetRecommenderSchemaResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_recommender_schema

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_recommender_schema.get_recommender_schema(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_recommender_schema_request.GetRecommenderSchemaRequest = {
            "domain_name": domain_name,
            "recommender_schema_name": recommender_schema_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_segment_definition(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        segment_definition_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_segment_definition_response.GetSegmentDefinitionResponse":
        """<p>Gets a segment definition from the domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            segment_definition_name: <p>The unique name of the segment definition.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_segment_definition_request.GetSegmentDefinitionRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_segment_definition_response.GetSegmentDefinitionResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_segment_definition

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_segment_definition.get_segment_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_segment_definition_request.GetSegmentDefinitionRequest = {
            "domain_name": domain_name,
            "segment_definition_name": segment_definition_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_segment_estimate(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        estimate_id: "capo_customer_profiles.types.string1_to255.string1To255",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_segment_estimate_response.GetSegmentEstimateResponse":
        """<p>Gets the result of a segment estimate query.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            estimate_id: <p>The query Id passed by a previous <code>CreateSegmentEstimate</code> operation.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_segment_estimate_request.GetSegmentEstimateRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_segment_estimate_response.GetSegmentEstimateResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_segment_estimate

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_segment_estimate.get_segment_estimate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_segment_estimate_request.GetSegmentEstimateRequest = {
            "domain_name": domain_name,
            "estimate_id": estimate_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_segment_membership(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        segment_definition_name: "capo_customer_profiles.types.name.name",
        profile_ids: "capo_customer_profiles.types.profile_ids.ProfileIds",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_segment_membership_response.GetSegmentMembershipResponse":
        """<p>Determines if the given profiles are within a segment.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            segment_definition_name: <p>The Id of the wanted segment. Needs to be a valid, and existing segment Id.</p>
            profile_ids: <p>The list of profile IDs to query for.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_segment_membership_request.GetSegmentMembershipRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_segment_membership_response.GetSegmentMembershipResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_segment_membership

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_segment_membership.get_segment_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_segment_membership_request.GetSegmentMembershipRequest = {
            "domain_name": domain_name,
            "segment_definition_name": segment_definition_name,
            "profile_ids": profile_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_segment_snapshot(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        segment_definition_name: "capo_customer_profiles.types.name.name",
        snapshot_id: "capo_customer_profiles.types.uuid.uuid",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_segment_snapshot_response.GetSegmentSnapshotResponse":
        """<p>Retrieve the latest status of a segment snapshot.</p>

        Args:
            domain_name: <p>The unique identifier of the domain.</p>
            segment_definition_name: <p>The unique name of the segment definition.</p>
            snapshot_id: <p>The unique identifier of the segment snapshot.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_segment_snapshot_request.GetSegmentSnapshotRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_segment_snapshot_response.GetSegmentSnapshotResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_segment_snapshot

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_segment_snapshot.get_segment_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_segment_snapshot_request.GetSegmentSnapshotRequest = {
            "domain_name": domain_name,
            "segment_definition_name": segment_definition_name,
            "snapshot_id": snapshot_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_segment_subscription(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        segment_definition_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_segment_subscription_response.GetSegmentSubscriptionResponse":
        """<p>Returns the current subscription configuration, execution schedule, and status for segment membership events. </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            segment_definition_name: <p>The unique name of the segment definition. </p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_segment_subscription_request.GetSegmentSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_segment_subscription_response.GetSegmentSubscriptionResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_segment_subscription

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_segment_subscription.get_segment_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_segment_subscription_request.GetSegmentSubscriptionRequest = {
            "domain_name": domain_name,
            "segment_definition_name": segment_definition_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_similar_profiles(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        match_type: "capo_customer_profiles.types.match_type.MatchType",
        search_key: "capo_customer_profiles.types.string1_to255.string1To255",
        search_value: "capo_customer_profiles.types.string1_to255.string1To255",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.get_similar_profiles_response.GetSimilarProfilesResponse":
        """<p>Returns a set of profiles that belong to the same matching group using the <code>matchId</code> or <code>profileId</code>. You can also specify the type of matching that you want for finding similar profiles using either <code>RULE_BASED_MATCHING</code> or <code>ML_BASED_MATCHING</code>.</p>

        Args:
            next_token: <p>The pagination token from the previous <code>GetSimilarProfiles</code> API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p>
            domain_name: <p>The unique name of the domain.</p>
            match_type: <p>Specify the type of matching to get similar profiles for.</p>
            search_key: <p>The string indicating the search key to be used.</p>
            search_value: <p>The string based on <code>SearchKey</code> to be searched for similar profiles.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_similar_profiles_request.GetSimilarProfilesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_similar_profiles_response.GetSimilarProfilesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_similar_profiles

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_similar_profiles.get_similar_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_similar_profiles_request.GetSimilarProfilesRequest = {
            "domain_name": domain_name,
            "match_type": match_type,
            "search_key": search_key,
            "search_value": search_value,
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

    def iter_get_similar_profiles(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        match_type: "capo_customer_profiles.types.match_type.MatchType",
        search_key: "capo_customer_profiles.types.string1_to255.string1To255",
        search_value: "capo_customer_profiles.types.string1_to255.string1To255",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "Iterator[capo_customer_profiles.types.uuid.uuid]":
        _token = next_token
        while True:
            _response = self.get_similar_profiles(
                domain_name,
                match_type,
                search_key,
                search_value,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("profile_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_stream_for_segments(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_stream_for_segments_response.GetStreamForSegmentsResponse":
        """<p>Returns information about the segment membership event stream configured for a specific domain, including the stream state and associated segments. </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_stream_for_segments_request.GetStreamForSegmentsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_stream_for_segments_response.GetStreamForSegmentsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_stream_for_segments

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_stream_for_segments.get_stream_for_segments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_stream_for_segments_request.GetStreamForSegmentsRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_upload_job(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        job_id: "capo_customer_profiles.types.uuid.uuid",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_upload_job_response.GetUploadJobResponse":
        """<p>This API retrieves the details of a specific upload job. </p>

        Args:
            domain_name: <p>The unique name of the domain containing the upload job. </p>
            job_id: <p>The unique identifier of the upload job to retrieve. </p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_upload_job_request.GetUploadJobRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_upload_job_response.GetUploadJobResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_upload_job

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_upload_job.get_upload_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_upload_job_request.GetUploadJobRequest = {
            "domain_name": domain_name,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_upload_job_path(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        job_id: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_upload_job_path_response.GetUploadJobPathResponse":
        """<p>This API retrieves the pre-signed URL and client token for uploading the file associated with the upload job. </p>

        Args:
            domain_name: <p>The unique name of the domain containing the upload job. </p>
            job_id: <p>The unique identifier of the upload job to retrieve the upload path for. This is generated from the CreateUploadJob API. </p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_upload_job_path_request.GetUploadJobPathRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_upload_job_path_response.GetUploadJobPathResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_upload_job_path

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_upload_job_path.get_upload_job_path(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_upload_job_path_request.GetUploadJobPathRequest = {
            "domain_name": domain_name,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workflow(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        workflow_id: "capo_customer_profiles.types.uuid.uuid",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.get_workflow_response.GetWorkflowResponse":
        """<p>Get details of specified workflow.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            workflow_id: <p>Unique identifier for the workflow.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_workflow_request.GetWorkflowRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_workflow_response.GetWorkflowResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_workflow

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_workflow.get_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_workflow_request.GetWorkflowRequest = {
            "domain_name": domain_name,
            "workflow_id": workflow_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workflow_steps(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        workflow_id: "capo_customer_profiles.types.uuid.uuid",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.get_workflow_steps_response.GetWorkflowStepsResponse":
        """<p>Get granular list of steps in workflow.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            workflow_id: <p>Unique identifier for the workflow.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.get_workflow_steps_request.GetWorkflowStepsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.get_workflow_steps_response.GetWorkflowStepsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.get_workflow_steps

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.get_workflow_steps.get_workflow_steps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.get_workflow_steps_request.GetWorkflowStepsRequest = {
            "domain_name": domain_name,
            "workflow_id": workflow_id,
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

    def list_account_integrations(
        self,
        uri: "capo_customer_profiles.types.string1_to255.string1To255",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        include_hidden: Optional[
            "capo_customer_profiles.types.optional_boolean.optionalBoolean"
        ] = None,
    ) -> "capo_customer_profiles.types.list_account_integrations_response.ListAccountIntegrationsResponse":
        """<p>Lists all of the integrations associated to a specific URI in the AWS account.</p>

        Args:
            uri: <p>The URI of the S3 bucket or any other type of data source.</p>
            next_token: <p>The pagination token from the previous ListAccountIntegrations API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p>
            include_hidden: <p>Boolean to indicate if hidden integration should be returned. Defaults to <code>False</code>.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_account_integrations_request.ListAccountIntegrationsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_account_integrations_response.ListAccountIntegrationsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_account_integrations

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_account_integrations.list_account_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_account_integrations_request.ListAccountIntegrationsRequest = {
            "uri": uri
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if include_hidden is not None:
            input_["include_hidden"] = include_hidden

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_calculated_attribute_definitions(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_calculated_attribute_definitions_response.ListCalculatedAttributeDefinitionsResponse":
        """<p>Lists calculated attribute definitions for Customer Profiles</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            next_token: <p>The pagination token from the previous call to ListCalculatedAttributeDefinitions.</p>
            max_results: <p>The maximum number of calculated attribute definitions returned per page.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_calculated_attribute_definitions_request.ListCalculatedAttributeDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_calculated_attribute_definitions_response.ListCalculatedAttributeDefinitionsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_calculated_attribute_definitions

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_calculated_attribute_definitions.list_calculated_attribute_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_calculated_attribute_definitions_request.ListCalculatedAttributeDefinitionsRequest = {
            "domain_name": domain_name
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

    def list_calculated_attributes_for_profile(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        profile_id: "capo_customer_profiles.types.uuid.uuid",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_calculated_attributes_for_profile_response.ListCalculatedAttributesForProfileResponse":
        """<p>Retrieve a list of calculated attributes for a customer profile.</p>

        Args:
            next_token: <p>The pagination token from the previous call to ListCalculatedAttributesForProfile.</p>
            max_results: <p>The maximum number of calculated attributes returned per page.</p>
            domain_name: <p>The unique name of the domain.</p>
            profile_id: <p>The unique identifier of a customer profile.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_calculated_attributes_for_profile_request.ListCalculatedAttributesForProfileRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_calculated_attributes_for_profile_response.ListCalculatedAttributesForProfileResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_calculated_attributes_for_profile

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_calculated_attributes_for_profile.list_calculated_attributes_for_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_calculated_attributes_for_profile_request.ListCalculatedAttributesForProfileRequest = {
            "domain_name": domain_name,
            "profile_id": profile_id,
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

    def list_domain_layouts(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_domain_layouts_response.ListDomainLayoutsResponse":
        """<p>Lists the existing layouts that can be used to view data for a specific domain. This API can only be invoked from the Amazon Connect admin website.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of objects returned per page.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_domain_layouts_request.ListDomainLayoutsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_domain_layouts_response.ListDomainLayoutsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_domain_layouts

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_domain_layouts.list_domain_layouts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_domain_layouts_request.ListDomainLayoutsRequest = {
            "domain_name": domain_name
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

    def iter_list_domain_layouts(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "Iterator[capo_customer_profiles.types.layout_item.LayoutItem]":
        _token = next_token
        while True:
            _response = self.list_domain_layouts(
                domain_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_domain_object_types(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "capo_customer_profiles.types.list_domain_object_types_response.ListDomainObjectTypesResponse":
        """<p>List all DomainObjectType(s) in a Customer Profiles domain. </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            max_results: <p>The maximum number of domain object types returned per page.</p>
            next_token: <p>The pagination token from the previous call to ListDomainObjectTypes.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_domain_object_types_request.ListDomainObjectTypesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_domain_object_types_response.ListDomainObjectTypesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_domain_object_types

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_domain_object_types.list_domain_object_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_domain_object_types_request.ListDomainObjectTypesRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_domain_object_types(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "Iterator[capo_customer_profiles.types.domain_object_types_list_item.DomainObjectTypesListItem]":
        _token = next_token
        while True:
            _response = self.list_domain_object_types(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_domains(
        self,
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_domains_response.ListDomainsResponse":
        """<p>Returns a list of all the domains for an AWS account that have been created.</p>

        Args:
            next_token: <p>The pagination token from the previous ListDomain API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_domains_request.ListDomainsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_domains_response.ListDomainsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_domains

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_domains.list_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_domains_request.ListDomainsRequest = {}
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

    def list_event_streams(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_event_streams_response.ListEventStreamsResponse":
        """<p>Returns a list of all the event streams in a specific domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of objects returned per page.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_event_streams_request.ListEventStreamsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_event_streams_response.ListEventStreamsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_event_streams

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_event_streams.list_event_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_event_streams_request.ListEventStreamsRequest = {
            "domain_name": domain_name
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

    def iter_list_event_streams(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> (
        "Iterator[capo_customer_profiles.types.event_stream_summary.EventStreamSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_event_streams(
                domain_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_event_triggers(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_event_triggers_response.ListEventTriggersResponse":
        """<p>List all Event Triggers under a domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            next_token: <p>The pagination token to use with ListEventTriggers.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_event_triggers_request.ListEventTriggersRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_event_triggers_response.ListEventTriggersResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_event_triggers

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_event_triggers.list_event_triggers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_event_triggers_request.ListEventTriggersRequest = {
            "domain_name": domain_name
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

    def iter_list_event_triggers(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "Iterator[capo_customer_profiles.types.event_trigger_summary_item.EventTriggerSummaryItem]":
        _token = next_token
        while True:
            _response = self.list_event_triggers(
                domain_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_identity_resolution_jobs(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_identity_resolution_jobs_response.ListIdentityResolutionJobsResponse":
        """<p>Lists all of the Identity Resolution Jobs in your domain. The response sorts the list by <code>JobStartTime</code>.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_identity_resolution_jobs_request.ListIdentityResolutionJobsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_identity_resolution_jobs_response.ListIdentityResolutionJobsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_identity_resolution_jobs

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_identity_resolution_jobs.list_identity_resolution_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_identity_resolution_jobs_request.ListIdentityResolutionJobsRequest = {
            "domain_name": domain_name
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

    def list_integrations(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        include_hidden: Optional[
            "capo_customer_profiles.types.optional_boolean.optionalBoolean"
        ] = None,
    ) -> "capo_customer_profiles.types.list_integrations_response.ListIntegrationsResponse":
        """<p>Lists all of the integrations in your domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            next_token: <p>The pagination token from the previous ListIntegrations API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p>
            include_hidden: <p>Boolean to indicate if hidden integration should be returned. Defaults to <code>False</code>.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_integrations_request.ListIntegrationsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_integrations_response.ListIntegrationsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_integrations

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_integrations.list_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_integrations_request.ListIntegrationsRequest = {
            "domain_name": domain_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if include_hidden is not None:
            input_["include_hidden"] = include_hidden

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_object_type_attributes(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_object_type_attributes_response.ListObjectTypeAttributesResponse":
        """<p>Fetch the possible attribute values given the attribute name.</p>

        Args:
            next_token: <p>The pagination token from the previous call. </p>
            max_results: <p>The maximum number of objects returned per page.</p>
            domain_name: <p>The unique identifier of the domain.</p>
            object_type_name: <p>The name of the profile object type.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_object_type_attributes_request.ListObjectTypeAttributesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_object_type_attributes_response.ListObjectTypeAttributesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_object_type_attributes

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_object_type_attributes.list_object_type_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_object_type_attributes_request.ListObjectTypeAttributesRequest = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
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

    def iter_list_object_type_attributes(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "Iterator[capo_customer_profiles.types.list_object_type_attribute_item.ListObjectTypeAttributeItem]":
        _token = next_token
        while True:
            _response = self.list_object_type_attributes(
                domain_name,
                object_type_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_object_type_attribute_values(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        attribute_name: "capo_customer_profiles.types.string1_to1000.string1To1000",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_object_type_attribute_values_response.ListObjectTypeAttributeValuesResponse":
        """<p>The ListObjectTypeAttributeValues API provides access to the most recent distinct values for any specified attribute, making it valuable for real-time data validation and consistency checks within your object types. This API works across domain, supporting both custom and standard object types. The API accepts the object type name, attribute name, and domain name as input parameters and returns values up to the storage limit of approximately 350KB.</p>

        Args:
            next_token: <p>The pagination token from the previous call.</p>
            max_results: <p>The maximum number of objects returned per page. Valid Range: Minimum value of 1. Maximum value of 100. If not provided default as 100.</p>
            domain_name: <p>The unique name of the domain.</p>
            object_type_name: <p>The unique name of the domain object type.</p>
            attribute_name: <p>The attribute name.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_object_type_attribute_values_request.ListObjectTypeAttributeValuesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_object_type_attribute_values_response.ListObjectTypeAttributeValuesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_object_type_attribute_values

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_object_type_attribute_values.list_object_type_attribute_values(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_object_type_attribute_values_request.ListObjectTypeAttributeValuesRequest = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
            "attribute_name": attribute_name,
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

    def list_profile_attribute_values(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        attribute_name: "capo_customer_profiles.types.string1_to255.string1To255",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.profile_attribute_values_response.ProfileAttributeValuesResponse":
        """<p>Fetch the possible attribute values given the attribute name.</p>

        Args:
            domain_name: <p>The unique identifier of the domain.</p>
            attribute_name: <p>The attribute name.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.profile_attribute_values_request.ProfileAttributeValuesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.profile_attribute_values_response.ProfileAttributeValuesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_profile_attribute_values

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_profile_attribute_values.list_profile_attribute_values(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.profile_attribute_values_request.ProfileAttributeValuesRequest = {
            "domain_name": domain_name,
            "attribute_name": attribute_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_profile_history_records(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        profile_id: "capo_customer_profiles.types.uuid.uuid",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        object_type_name: Optional[
            "capo_customer_profiles.types.type_name.typeName"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        action_type: Optional[
            "capo_customer_profiles.types.action_type.ActionType"
        ] = None,
        performed_by: Optional[
            "capo_customer_profiles.types.string1_to255.string1To255"
        ] = None,
    ) -> "capo_customer_profiles.types.list_profile_history_records_response.ListProfileHistoryRecordsResponse":
        """<p>Returns a list of history records for a specific profile, for a specific domain.</p>

        Args:
            domain_name: <p>The unique name of the domain for which to return profile history records.</p>
            profile_id: <p>The identifier of the profile to be taken.</p>
            object_type_name: <p>Applies a filter to include profile history records only with the specified <code>ObjectTypeName</code> value in the response.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            action_type: <p>Applies a filter to include profile history records only with the specified <code>ActionType</code> value in the response.</p>
            performed_by: <p>Applies a filter to include profile history records only with the specified <code>PerformedBy</code> value in the response. The <code>PerformedBy</code> value can be the Amazon Resource Name (ARN) of the person or service principal who performed the action.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_profile_history_records_request.ListProfileHistoryRecordsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_profile_history_records_response.ListProfileHistoryRecordsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_profile_history_records

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_profile_history_records.list_profile_history_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_profile_history_records_request.ListProfileHistoryRecordsRequest = {
            "domain_name": domain_name,
            "profile_id": profile_id,
        }
        if object_type_name is not None:
            input_["object_type_name"] = object_type_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if action_type is not None:
            input_["action_type"] = action_type
        if performed_by is not None:
            input_["performed_by"] = performed_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_profile_objects(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        profile_id: "capo_customer_profiles.types.uuid.uuid",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        object_filter: Optional[
            "capo_customer_profiles.types.object_filter.ObjectFilter"
        ] = None,
    ) -> "capo_customer_profiles.types.list_profile_objects_response.ListProfileObjectsResponse":
        """<p>Returns a list of objects associated with a profile of a given ProfileObjectType.</p>

        Args:
            next_token: <p>The pagination token from the previous call to ListProfileObjects.</p>
            max_results: <p>The maximum number of objects returned per page.</p>
            domain_name: <p>The unique name of the domain.</p>
            object_type_name: <p>The name of the profile object type.</p>
            profile_id: <p>The unique identifier of a customer profile.</p>
            object_filter: <p>Applies a filter to the response to include profile objects with the specified index values.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_profile_objects_request.ListProfileObjectsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_profile_objects_response.ListProfileObjectsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_profile_objects

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_profile_objects.list_profile_objects(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_profile_objects_request.ListProfileObjectsRequest = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
            "profile_id": profile_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if object_filter is not None:
            input_["object_filter"] = object_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_profile_object_types(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_profile_object_types_response.ListProfileObjectTypesResponse":
        """<p>Lists all of the templates available within the service.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of objects returned per page.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_profile_object_types_request.ListProfileObjectTypesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_profile_object_types_response.ListProfileObjectTypesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_profile_object_types

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_profile_object_types.list_profile_object_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_profile_object_types_request.ListProfileObjectTypesRequest = {
            "domain_name": domain_name
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

    def list_profile_object_type_templates(
        self,
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_profile_object_type_templates_response.ListProfileObjectTypeTemplatesResponse":
        """<p>Lists all of the template information for object types.</p>

        Args:
            next_token: <p>The pagination token from the previous ListObjectTypeTemplates API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_profile_object_type_templates_request.ListProfileObjectTypeTemplatesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_profile_object_type_templates_response.ListProfileObjectTypeTemplatesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_profile_object_type_templates

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_profile_object_type_templates.list_profile_object_type_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_profile_object_type_templates_request.ListProfileObjectTypeTemplatesRequest = {}
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

    def list_recommender_filters(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "capo_customer_profiles.types.list_recommender_filters_response.ListRecommenderFiltersResponse":
        """<p>Returns a list of recommender filters in the specified domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            max_results: <p>The maximum number of recommender filters to return in the response. The default value is 100.</p>
            next_token: <p>A token received from a previous ListRecommenderFilters call to retrieve the next page of results.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_recommender_filters_request.ListRecommenderFiltersRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_recommender_filters_response.ListRecommenderFiltersResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_recommender_filters

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_recommender_filters.list_recommender_filters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_recommender_filters_request.ListRecommenderFiltersRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_recommender_filters(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "Iterator[capo_customer_profiles.types.recommender_filter_summary.RecommenderFilterSummary]":
        _token = next_token
        while True:
            _response = self.list_recommender_filters(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recommender_filters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recommender_recipes(
        self,
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.list_recommender_recipes_request_max_results_integer.ListRecommenderRecipesRequestMaxResultsInteger"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "capo_customer_profiles.types.list_recommender_recipes_response.ListRecommenderRecipesResponse":
        """<p>Returns a list of available recommender recipes that can be used to create recommenders.</p>

        Args:
            max_results: <p>The maximum number of recommender recipes to return in the response. The default value is 100.</p>
            next_token: <p>A token received from a previous ListRecommenderRecipes call to retrieve the next page of results.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_recommender_recipes_request.ListRecommenderRecipesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_recommender_recipes_response.ListRecommenderRecipesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_recommender_recipes

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_recommender_recipes.list_recommender_recipes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_recommender_recipes_request.ListRecommenderRecipesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_recommender_recipes(
        self,
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.list_recommender_recipes_request_max_results_integer.ListRecommenderRecipesRequestMaxResultsInteger"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "Iterator[capo_customer_profiles.types.recommender_recipe.RecommenderRecipe]":
        _token = next_token
        while True:
            _response = self.list_recommender_recipes(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recommender_recipes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recommenders(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.list_recommenders_request_max_results_integer.ListRecommendersRequestMaxResultsInteger"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "capo_customer_profiles.types.list_recommenders_response.ListRecommendersResponse":
        """<p>Returns a list of recommenders in the specified domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            max_results: <p>The maximum number of recommenders to return in the response. The default value is 100.</p>
            next_token: <p>A token received from a previous ListRecommenders call to retrieve the next page of results.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_recommenders_request.ListRecommendersRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_recommenders_response.ListRecommendersResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_recommenders

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_recommenders.list_recommenders(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_recommenders_request.ListRecommendersRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_recommenders(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.list_recommenders_request_max_results_integer.ListRecommendersRequestMaxResultsInteger"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> (
        "Iterator[capo_customer_profiles.types.recommender_summary.RecommenderSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_recommenders(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recommenders",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recommender_schemas(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "capo_customer_profiles.types.list_recommender_schemas_response.ListRecommenderSchemasResponse":
        """<p>Returns a list of recommender schemas in the specified domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            max_results: <p>The maximum number of recommender schemas to return in the response. The default value is 100.</p>
            next_token: <p>A token received from a previous ListRecommenderSchemas call to retrieve the next page of results.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_recommender_schemas_request.ListRecommenderSchemasRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_recommender_schemas_response.ListRecommenderSchemasResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_recommender_schemas

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_recommender_schemas.list_recommender_schemas(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_recommender_schemas_request.ListRecommenderSchemasRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_recommender_schemas(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "Iterator[capo_customer_profiles.types.recommender_schema_summary.RecommenderSchemaSummary]":
        _token = next_token
        while True:
            _response = self.list_recommender_schemas(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recommender_schemas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_rule_based_matches(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_rule_based_matches_response.ListRuleBasedMatchesResponse":
        """<p>Returns a set of <code>MatchIds</code> that belong to the given domain.</p>

        Args:
            next_token: <p>The pagination token from the previous <code>ListRuleBasedMatches</code> API call.</p>
            max_results: <p>The maximum number of <code>MatchIds</code> returned per page.</p>
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_rule_based_matches_request.ListRuleBasedMatchesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_rule_based_matches_response.ListRuleBasedMatchesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_rule_based_matches

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_rule_based_matches.list_rule_based_matches(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_rule_based_matches_request.ListRuleBasedMatchesRequest = {
            "domain_name": domain_name
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

    def iter_list_rule_based_matches(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "Iterator[capo_customer_profiles.types.string1_to255.string1To255]":
        _token = next_token
        while True:
            _response = self.list_rule_based_matches(
                domain_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("match_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_segment_definitions(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size500.MaxSize500"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "capo_customer_profiles.types.list_segment_definitions_response.ListSegmentDefinitionsResponse":
        """<p>Lists all segment definitions under a domain.</p>

        Args:
            domain_name: <p>The unique identifier of the domain.</p>
            max_results: <p>The maximum number of objects returned per page.</p>
            next_token: <p>The pagination token from the previous call. </p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_segment_definitions_request.ListSegmentDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_segment_definitions_response.ListSegmentDefinitionsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_segment_definitions

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_segment_definitions.list_segment_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_segment_definitions_request.ListSegmentDefinitionsRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_segment_definitions(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size500.MaxSize500"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "Iterator[capo_customer_profiles.types.segment_definition_item.SegmentDefinitionItem]":
        _token = next_token
        while True:
            _response = self.list_segment_definitions(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_segment_subscription_events(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        segment_definition_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "capo_customer_profiles.types.list_segment_subscription_events_response.ListSegmentSubscriptionEventsResponse":
        """<p>Returns the most recent membership events for a segment. Each event represents a profile that entered or exited the segment. </p> <p>This operation is paginated. </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            segment_definition_name: <p>The unique name of the segment definition. </p>
            max_results: <p>The maximum number of events to return per page. </p>
            next_token: <p>The pagination token from the previous call to retrieve the next page of results. </p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_segment_subscription_events_request.ListSegmentSubscriptionEventsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_segment_subscription_events_response.ListSegmentSubscriptionEventsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_segment_subscription_events

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_segment_subscription_events.list_segment_subscription_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_segment_subscription_events_request.ListSegmentSubscriptionEventsRequest = {
            "domain_name": domain_name,
            "segment_definition_name": segment_definition_name,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_segment_subscription_events(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        segment_definition_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "Iterator[capo_customer_profiles.types.subscription_event_item.SubscriptionEventItem]":
        _token = next_token
        while True:
            _response = self.list_segment_subscription_events(
                domain_name,
                segment_definition_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_customer_profiles.types.tag_arn.TagArn",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Displays the tags associated with an Amazon Connect Customer Profiles resource. In Connect Customer Profiles, domains, profile object types, and integrations can be tagged.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which you want to view tags.</p>

        Raises:
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_tags_for_resource

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_upload_jobs(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size500.MaxSize500"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> (
        "capo_customer_profiles.types.list_upload_jobs_response.ListUploadJobsResponse"
    ):
        """<p>This API retrieves a list of upload jobs for the specified domain. </p>

        Args:
            domain_name: <p>The unique name of the domain to list upload jobs for. </p>
            max_results: <p>The maximum number of upload jobs to return per page. </p>
            next_token: <p>The pagination token from the previous call to retrieve the next page of results. </p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_upload_jobs_request.ListUploadJobsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_upload_jobs_response.ListUploadJobsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_upload_jobs

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_upload_jobs.list_upload_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_upload_jobs_request.ListUploadJobsRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_upload_jobs(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size500.MaxSize500"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
    ) -> "Iterator[capo_customer_profiles.types.upload_job_item.UploadJobItem]":
        _token = next_token
        while True:
            _response = self.list_upload_jobs(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_workflows(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        workflow_type: Optional[
            "capo_customer_profiles.types.workflow_type.WorkflowType"
        ] = None,
        status: Optional["capo_customer_profiles.types.status.Status"] = None,
        query_start_date: Optional[
            "capo_customer_profiles.types.timestamp.timestamp"
        ] = None,
        query_end_date: Optional[
            "capo_customer_profiles.types.timestamp.timestamp"
        ] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
    ) -> "capo_customer_profiles.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Query to list all workflows.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            workflow_type: <p>The type of workflow. The only supported value is APPFLOW_INTEGRATION.</p>
            status: <p>Status of workflow execution.</p>
            query_start_date: <p>Retrieve workflows started after timestamp.</p>
            query_end_date: <p>Retrieve workflows ended after timestamp.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.list_workflows

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.list_workflows.list_workflows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.list_workflows_request.ListWorkflowsRequest = {
            "domain_name": domain_name
        }
        if workflow_type is not None:
            input_["workflow_type"] = workflow_type
        if status is not None:
            input_["status"] = status
        if query_start_date is not None:
            input_["query_start_date"] = query_start_date
        if query_end_date is not None:
            input_["query_end_date"] = query_end_date
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

    def merge_profiles(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        main_profile_id: "capo_customer_profiles.types.uuid.uuid",
        profile_ids_to_be_merged: "capo_customer_profiles.types.profile_id_to_be_merged_list.ProfileIdToBeMergedList",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        field_source_profile_ids: Optional[
            "capo_customer_profiles.types.field_source_profile_ids.FieldSourceProfileIds"
        ] = None,
    ) -> "capo_customer_profiles.types.merge_profiles_response.MergeProfilesResponse":
        """<p>Runs an AWS Lambda job that does the following:</p> <ol> <li> <p>All the profileKeys in the <code>ProfileToBeMerged</code> will be moved to the main profile.</p> </li> <li> <p>All the objects in the <code>ProfileToBeMerged</code> will be moved to the main profile.</p> </li> <li> <p>All the <code>ProfileToBeMerged</code> will be deleted at the end.</p> </li> <li> <p>All the profileKeys in the <code>ProfileIdsToBeMerged</code> will be moved to the main profile.</p> </li> <li> <p>Standard fields are merged as follows:</p> <ol> <li> <p>Fields are always "union"-ed if there are no conflicts in standard fields or attributeKeys.</p> </li> <li> <p>When there are conflicting fields:</p> <ol> <li> <p>If no <code>SourceProfileIds</code> entry is specified, the main Profile value is always taken. </p> </li> <li> <p>If a <code>SourceProfileIds</code> entry is specified, the specified profileId is always taken, even if it is a NULL value.</p> </li> </ol> </li> </ol> </li> </ol> <p>You can use MergeProfiles together with <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html">GetMatches</a>, which returns potentially matching profiles, or use it with the results of another matching system. After profiles have been merged, they cannot be separated (unmerged).</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            main_profile_id: <p>The identifier of the profile to be taken.</p>
            profile_ids_to_be_merged: <p>The identifier of the profile to be merged into MainProfileId.</p>
            field_source_profile_ids: <p>The identifiers of the fields in the profile that has the information you want to apply to the merge. For example, say you want to merge EmailAddress from Profile1 into MainProfile. This would be the identifier of the EmailAddress field in Profile1. </p>

        Raises:
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.merge_profiles_request.MergeProfilesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.merge_profiles_response.MergeProfilesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.merge_profiles

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.merge_profiles.merge_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.merge_profiles_request.MergeProfilesRequest = {
            "domain_name": domain_name,
            "main_profile_id": main_profile_id,
            "profile_ids_to_be_merged": profile_ids_to_be_merged,
        }
        if field_source_profile_ids is not None:
            input_["field_source_profile_ids"] = field_source_profile_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_domain_object_type(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        fields: "capo_customer_profiles.types.domain_object_type_fields.DomainObjectTypeFields",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        description: Optional[
            "capo_customer_profiles.types.sensitive_string1_to10000.sensitiveString1To10000"
        ] = None,
        encryption_key: Optional[
            "capo_customer_profiles.types.encryption_key.encryptionKey"
        ] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.put_domain_object_type_response.PutDomainObjectTypeResponse":
        """<p>Create/Update a DomainObjectType in a Customer Profiles domain. To create a new DomainObjectType, Data Store needs to be enabled on the Domain.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            object_type_name: <p>The unique name of the domain object type.</p>
            description: <p>The description of the domain object type.</p>
            encryption_key: <p>The customer provided KMS key used to encrypt this type of domain object.</p>
            fields: <p>A map of field names to their corresponding domain object type field definitions.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.put_domain_object_type_request.PutDomainObjectTypeRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.put_domain_object_type_response.PutDomainObjectTypeResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.put_domain_object_type

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.put_domain_object_type.put_domain_object_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.put_domain_object_type_request.PutDomainObjectTypeRequest = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
            "fields": fields,
        }
        if description is not None:
            input_["description"] = description
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_integration(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        uri: Optional["capo_customer_profiles.types.string1_to255.string1To255"] = None,
        object_type_name: Optional[
            "capo_customer_profiles.types.type_name.typeName"
        ] = None,
        object_type_names: Optional[
            "capo_customer_profiles.types.object_type_names.ObjectTypeNames"
        ] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
        flow_definition: Optional[
            "capo_customer_profiles.types.flow_definition.FlowDefinition"
        ] = None,
        role_arn: Optional["capo_customer_profiles.types.role_arn.RoleArn"] = None,
        event_trigger_names: Optional[
            "capo_customer_profiles.types.event_trigger_names.EventTriggerNames"
        ] = None,
        scope: Optional["capo_customer_profiles.types.scope.Scope"] = None,
    ) -> "capo_customer_profiles.types.put_integration_response.PutIntegrationResponse":
        """<p>Adds an integration between the service and a third-party service, which includes Amazon AppFlow and Amazon Connect.</p> <p>An integration can belong to only one domain.</p> <p>To add or remove tags on an existing Integration, see <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html"> TagResource </a>/<a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html"> UntagResource</a>.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            uri: <p>The URI of the S3 bucket or any other type of data source.</p>
            object_type_name: <p>The name of the profile object type.</p>
            object_type_names: <p>A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an <code>ObjectTypeName</code> (template) used to ingest the event. It supports the following event types: <code>SegmentIdentify</code>, <code>ShopifyCreateCustomers</code>, <code>ShopifyUpdateCustomers</code>, <code>ShopifyCreateDraftOrders</code>, <code>ShopifyUpdateDraftOrders</code>, <code>ShopifyCreateOrders</code>, and <code>ShopifyUpdatedOrders</code>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            flow_definition: <p>The configuration that controls how Customer Profiles retrieves data from the source.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role. The Integration uses this role to make Customer Profiles requests on your behalf.</p>
            event_trigger_names: <p>A list of unique names for active event triggers associated with the integration.</p>
            scope: <p>Specifies whether the integration applies to profile level data (associated with profiles) or domain level data (not associated with any specific profile). The default value is PROFILE.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.put_integration_request.PutIntegrationRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.put_integration_response.PutIntegrationResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.put_integration

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.put_integration.put_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.put_integration_request.PutIntegrationRequest = {
            "domain_name": domain_name
        }
        if uri is not None:
            input_["uri"] = uri
        if object_type_name is not None:
            input_["object_type_name"] = object_type_name
        if object_type_names is not None:
            input_["object_type_names"] = object_type_names
        if tags is not None:
            input_["tags"] = tags
        if flow_definition is not None:
            input_["flow_definition"] = flow_definition
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if event_trigger_names is not None:
            input_["event_trigger_names"] = event_trigger_names
        if scope is not None:
            input_["scope"] = scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_profile_object(
        self,
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        object: "capo_customer_profiles.types.stringified_json.stringifiedJson",
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.put_profile_object_response.PutProfileObjectResponse":
        """<p>Adds additional objects to customer profiles of a given ObjectType.</p> <p>When adding a specific profile object, like a Contact Record, an inferred profile can get created if it is not mapped to an existing profile. The resulting profile will only have a phone number populated in the standard ProfileObject. Any additional Contact Records with the same phone number will be mapped to the same inferred profile.</p> <p>When a ProfileObject is created and if a ProfileObjectType already exists for the ProfileObject, it will provide data to a standard profile depending on the ProfileObjectType definition.</p> <p>PutProfileObject needs an ObjectType, which can be created using PutProfileObjectType.</p>

        Args:
            object_type_name: <p>The name of the profile object type.</p>
            object: <p>A string that is serialized from a JSON object.</p>
            domain_name: <p>The unique name of the domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.put_profile_object_request.PutProfileObjectRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.put_profile_object_response.PutProfileObjectResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.put_profile_object

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.put_profile_object.put_profile_object(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.put_profile_object_request.PutProfileObjectRequest = {
            "object_type_name": object_type_name,
            "object": object,
            "domain_name": domain_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_profile_object_type(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        object_type_name: "capo_customer_profiles.types.type_name.typeName",
        description: "capo_customer_profiles.types.sensitive_text.sensitiveText",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        template_id: Optional["capo_customer_profiles.types.name.name"] = None,
        expiration_days: Optional[
            "capo_customer_profiles.types.expiration_days_integer.expirationDaysInteger"
        ] = None,
        encryption_key: Optional[
            "capo_customer_profiles.types.encryption_key.encryptionKey"
        ] = None,
        allow_profile_creation: Optional[
            "capo_customer_profiles.types.boolean.boolean"
        ] = None,
        source_last_updated_timestamp_format: Optional[
            "capo_customer_profiles.types.string1_to255.string1To255"
        ] = None,
        max_profile_object_count: Optional[
            "capo_customer_profiles.types.min_size1.minSize1"
        ] = None,
        source_priority: Optional[
            "capo_customer_profiles.types.min_size1.minSize1"
        ] = None,
        fields: Optional["capo_customer_profiles.types.field_map.FieldMap"] = None,
        keys: Optional["capo_customer_profiles.types.key_map.KeyMap"] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.put_profile_object_type_response.PutProfileObjectTypeResponse":
        """<p>Defines a ProfileObjectType.</p> <p>To add or remove tags on an existing ObjectType, see <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html"> TagResource</a>/<a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html">UntagResource</a>.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            object_type_name: <p>The name of the profile object type.</p>
            description: <p>Description of the profile object type.</p>
            template_id: <p>A unique identifier for the object template. For some attributes in the request, the service will use the default value from the object template when TemplateId is present. If these attributes are present in the request, the service may return a <code>BadRequestException</code>. These attributes include: AllowProfileCreation, SourceLastUpdatedTimestampFormat, Fields, and Keys. For example, if AllowProfileCreation is set to true when TemplateId is set, the service may return a <code>BadRequestException</code>.</p>
            expiration_days: <p>The number of days until the data in the object expires.</p>
            encryption_key: <p>The customer-provided key to encrypt the profile object that will be created in this profile object type.</p>
            allow_profile_creation: <p>Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is <code>FALSE</code>. If the AllowProfileCreation flag is set to <code>FALSE</code>, then the service tries to fetch a standard profile and associate this object with the profile. If it is set to <code>TRUE</code>, and if no match is found, then the service creates a new standard profile.</p>
            source_last_updated_timestamp_format: <p>The format of your <code>sourceLastUpdatedTimestamp</code> that was previously set up. </p>
            max_profile_object_count: <p>The amount of profile object max count assigned to the object type</p>
            source_priority: <p>An integer that determines the priority of this object type when data from multiple sources is ingested. Lower values take priority. Object types without a specified source priority default to the lowest priority.</p>
            fields: <p>A map of the name and ObjectType field.</p>
            keys: <p>A list of unique keys that can be used to map data to the profile.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.put_profile_object_type_request.PutProfileObjectTypeRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.put_profile_object_type_response.PutProfileObjectTypeResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.put_profile_object_type

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.put_profile_object_type.put_profile_object_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.put_profile_object_type_request.PutProfileObjectTypeRequest = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
            "description": description,
        }
        if template_id is not None:
            input_["template_id"] = template_id
        if expiration_days is not None:
            input_["expiration_days"] = expiration_days
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if allow_profile_creation is not None:
            input_["allow_profile_creation"] = allow_profile_creation
        if source_last_updated_timestamp_format is not None:
            input_["source_last_updated_timestamp_format"] = (
                source_last_updated_timestamp_format
            )
        if max_profile_object_count is not None:
            input_["max_profile_object_count"] = max_profile_object_count
        if source_priority is not None:
            input_["source_priority"] = source_priority
        if fields is not None:
            input_["fields"] = fields
        if keys is not None:
            input_["keys"] = keys
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_segment_subscription(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        segment_definition_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        schedule_configuration: Optional[
            "capo_customer_profiles.types.schedule_configuration.ScheduleConfiguration"
        ] = None,
    ) -> "capo_customer_profiles.types.put_segment_subscription_response.PutSegmentSubscriptionResponse":
        """<p>Creates or updates a segment subscription for membership events. When a subscription is created, an initial snapshot is taken and the system begins monitoring for membership changes. </p> <p>You can optionally set a schedule configuration interval to control how often membership snapshots are run. The interval can be from 1 to 24 hours. If not set, the interval defaults to 24 hours. Scheduled snapshots run on a best-effort basis. If a scheduled snapshot takes longer than the configured interval, the next scheduled run does not start until the in-progress snapshot completes, so a run might be delayed or skipped and is not guaranteed to occur at exactly the requested time. </p> <p>For Classic segments, membership events are generated from these scheduled snapshots and also in near real-time as profile attribute changes occur. For SQL segments, membership events are generated only from the scheduled snapshots. </p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            segment_definition_name: <p>The unique name of the segment definition. </p>
            schedule_configuration: <p>The optional schedule configuration that controls how often membership snapshots are run. If not provided, the subscription defaults to a 24-hour interval. </p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.put_segment_subscription_request.PutSegmentSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.put_segment_subscription_response.PutSegmentSubscriptionResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.put_segment_subscription

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.put_segment_subscription.put_segment_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.put_segment_subscription_request.PutSegmentSubscriptionRequest = {
            "domain_name": domain_name,
            "segment_definition_name": segment_definition_name,
        }
        if schedule_configuration is not None:
            input_["schedule_configuration"] = schedule_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_profiles(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        key_name: "capo_customer_profiles.types.name.name",
        values: "capo_customer_profiles.types.request_value_list.requestValueList",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        next_token: Optional["capo_customer_profiles.types.token.token"] = None,
        max_results: Optional[
            "capo_customer_profiles.types.max_size100.maxSize100"
        ] = None,
        additional_search_keys: Optional[
            "capo_customer_profiles.types.additional_search_keys_list.additionalSearchKeysList"
        ] = None,
        logical_operator: Optional[
            "capo_customer_profiles.types.logical_operator.logicalOperator"
        ] = None,
    ) -> "capo_customer_profiles.types.search_profiles_response.SearchProfilesResponse":
        """<p>Searches for profiles within a specific domain using one or more predefined search keys (e.g., _fullName, _phone, _email, _account, etc.) and/or custom-defined search keys. A search key is a data type pair that consists of a <code>KeyName</code> and <code>Values</code> list.</p> <p>This operation supports searching for profiles with a minimum of 1 key-value(s) pair and up to 5 key-value(s) pairs using either <code>AND</code> or <code>OR</code> logic.</p>

        Args:
            next_token: <p>The pagination token from the previous SearchProfiles API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p> <p>The default is 20 if this parameter is not included in the request.</p>
            domain_name: <p>The unique name of the domain.</p>
            key_name: <p>A searchable identifier of a customer profile. The predefined keys you can use to search include: _account, _profileId, _assetId, _caseId, _orderId, _fullName, _phone, _email, _ctrContactId, _marketoLeadId, _salesforceAccountId, _salesforceContactId, _salesforceAssetId, _zendeskUserId, _zendeskExternalId, _zendeskTicketId, _serviceNowSystemId, _serviceNowIncidentId, _segmentUserId, _shopifyCustomerId, _shopifyOrderId.</p>
            values: <p>A list of key values.</p>
            additional_search_keys: <p>A list of <code>AdditionalSearchKey</code> objects that are each searchable identifiers of a profile. Each <code>AdditionalSearchKey</code> object contains a <code>KeyName</code> and a list of <code>Values</code> associated with that specific key (i.e., a key-value(s) pair). These additional search keys will be used in conjunction with the <code>LogicalOperator</code> and the required <code>KeyName</code> and <code>Values</code> parameters to search for profiles that satisfy the search criteria. </p>
            logical_operator: <p>Relationship between all specified search keys that will be used to search for profiles. This includes the required <code>KeyName</code> and <code>Values</code> parameters as well as any key-value(s) pairs specified in the <code>AdditionalSearchKeys</code> list.</p> <p>This parameter influences which profiles will be returned in the response in the following manner:</p> <ul> <li> <p> <code>AND</code> - The response only includes profiles that match all of the search keys.</p> </li> <li> <p> <code>OR</code> - The response includes profiles that match at least one of the search keys.</p> </li> </ul> <p>The <code>OR</code> relationship is the default behavior if this parameter is not included in the request.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.search_profiles_request.SearchProfilesRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.search_profiles_response.SearchProfilesResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.search_profiles

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.search_profiles.search_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.search_profiles_request.SearchProfilesRequest = {
            "domain_name": domain_name,
            "key_name": key_name,
            "values": values,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if additional_search_keys is not None:
            input_["additional_search_keys"] = additional_search_keys
        if logical_operator is not None:
            input_["logical_operator"] = logical_operator

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_recommendations(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        key_name: "capo_customer_profiles.types.name.name",
        key_values: "capo_customer_profiles.types.key_values_list.KeyValuesList",
        recommender: "capo_customer_profiles.types.recommender.Recommender",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        candidate_ids: Optional[
            "capo_customer_profiles.types.candidate_id_list.CandidateIdList"
        ] = None,
        context: Optional[
            "capo_customer_profiles.types.recommender_context.RecommenderContext"
        ] = None,
        diversity: Optional[
            "capo_customer_profiles.types.recommendation_diversity_config.RecommendationDiversityConfig"
        ] = None,
        metadata: Optional[
            "capo_customer_profiles.types.recommendation_metadata.RecommendationMetadata"
        ] = None,
        max_recommendations: Optional[
            "capo_customer_profiles.types.max_size500.MaxSize500"
        ] = None,
    ) -> "capo_customer_profiles.types.search_recommendations_response.SearchRecommendationsResponse":
        """<p>Retrieves recommendations for a profile in a specific domain. The profile is identified using a search key, which consists of a <code>KeyName</code> and a <code>KeyValues</code> list. The <code>KeyName</code> can be a predefined key (for example, <code>_profileId</code>, <code>_phone</code>, <code>_email</code>) or a custom-defined key.</p> <p>The search key must match exactly one profile. If no profile matches the search key, the operation returns a <code>ResourceNotFoundException</code>. If more than one profile matches the search key, the operation returns a <code>BadRequestException</code>. You can use the SearchProfiles API to review the matching profiles.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            key_name: <p>A searchable identifier of a customer profile. You can use a predefined key, such as <code>_profileId</code>, <code>_phone</code>, or <code>_email</code>, or a custom-defined key.</p>
            key_values: <p>A list of key values. Provide one value for each field of the search key.</p>
            recommender: <p>The recommender used to generate the recommendations.</p>
            candidate_ids: <p>A list of item IDs to rank for the user. Use this when you want to re-rank a specific set of items rather than getting recommendations from the full item catalog. Required for personalized-ranking use cases.</p>
            context: <p>The contextual metadata used to provide dynamic runtime information to tailor recommendations.</p>
            diversity: <p>Runtime diversity configuration for this request. Enables diversity-aware recommendations and optionally supplies values for placeholder-based diversity caps configured on the recommender.</p>
            metadata: <p>Configuration for metadata to include in recommendation responses.</p>
            max_recommendations: <p>The maximum number of recommendations to return. The default value is 5.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.search_recommendations_request.SearchRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.search_recommendations_response.SearchRecommendationsResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.search_recommendations

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.search_recommendations.search_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.search_recommendations_request.SearchRecommendationsRequest = {
            "domain_name": domain_name,
            "key_name": key_name,
            "key_values": key_values,
            "recommender": recommender,
        }
        if candidate_ids is not None:
            input_["candidate_ids"] = candidate_ids
        if context is not None:
            input_["context"] = context
        if diversity is not None:
            input_["diversity"] = diversity
        if metadata is not None:
            input_["metadata"] = metadata
        if max_recommendations is not None:
            input_["max_recommendations"] = max_recommendations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_recommender(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.start_recommender_response.StartRecommenderResponse":
        """<p>Starts a recommender that was previously stopped. Starting a recommender resumes its ability to generate recommendations.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_name: <p>The name of the recommender to start.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.start_recommender_request.StartRecommenderRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.start_recommender_response.StartRecommenderResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.start_recommender

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.start_recommender.start_recommender(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.start_recommender_request.StartRecommenderRequest = {
            "domain_name": domain_name,
            "recommender_name": recommender_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_upload_job(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        job_id: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> (
        "capo_customer_profiles.types.start_upload_job_response.StartUploadJobResponse"
    ):
        """<p>This API starts the processing of an upload job to ingest profile data. </p>

        Args:
            domain_name: <p>The unique name of the domain containing the upload job to start. </p>
            job_id: <p>The unique identifier of the upload job to start. </p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.start_upload_job_request.StartUploadJobRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.start_upload_job_response.StartUploadJobResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.start_upload_job

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.start_upload_job.start_upload_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.start_upload_job_request.StartUploadJobRequest = {
            "domain_name": domain_name,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_recommender(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> (
        "capo_customer_profiles.types.stop_recommender_response.StopRecommenderResponse"
    ):
        """<p>Stops a recommender, suspending its ability to generate recommendations. The recommender can be restarted later using StartRecommender.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_name: <p>The name of the recommender to stop.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.stop_recommender_request.StopRecommenderRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.stop_recommender_response.StopRecommenderResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.stop_recommender

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.stop_recommender.stop_recommender(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.stop_recommender_request.StopRecommenderRequest = {
            "domain_name": domain_name,
            "recommender_name": recommender_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_upload_job(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        job_id: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.stop_upload_job_response.StopUploadJobResponse":
        """<p>This API stops the processing of an upload job. </p>

        Args:
            domain_name: <p>The unique name of the domain containing the upload job to stop. </p>
            job_id: <p>The unique identifier of the upload job to stop. </p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.stop_upload_job_request.StopUploadJobRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.stop_upload_job_response.StopUploadJobResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.stop_upload_job

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.stop_upload_job.stop_upload_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.stop_upload_job_request.StopUploadJobRequest = {
            "domain_name": domain_name,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_customer_profiles.types.tag_arn.TagArn",
        tags: "capo_customer_profiles.types.tag_map.TagMap",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified Amazon Connect Customer Profiles resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In Connect Customer Profiles, domains, profile object types, and integrations can be tagged.</p> <p>Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.</p> <p>You can use the TagResource action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource that you're adding tags to.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.tag_resource

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_customer_profiles.types.tag_arn.TagArn",
        tag_keys: "capo_customer_profiles.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
    ) -> "capo_customer_profiles.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified Amazon Connect Customer Profiles resource. In Connect Customer Profiles, domains, profile object types, and integrations can be tagged.</p>

        Args:
            resource_arn: <p>The ARN of the resource from which you are removing tags.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.untag_resource

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.untag_resource_request.UntagResourceRequest = {
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

    def update_calculated_attribute_definition(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        calculated_attribute_name: "capo_customer_profiles.types.type_name.typeName",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        display_name: Optional[
            "capo_customer_profiles.types.display_name.displayName"
        ] = None,
        description: Optional[
            "capo_customer_profiles.types.sensitive_text.sensitiveText"
        ] = None,
        conditions: Optional[
            "capo_customer_profiles.types.conditions.Conditions"
        ] = None,
    ) -> "capo_customer_profiles.types.update_calculated_attribute_definition_response.UpdateCalculatedAttributeDefinitionResponse":
        """<p>Updates an existing calculated attribute definition. When updating the Conditions, note that increasing the date range of a calculated attribute will not trigger inclusion of historical data greater than the current date range.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            calculated_attribute_name: <p>The unique name of the calculated attribute.</p>
            display_name: <p>The display name of the calculated attribute.</p>
            description: <p>The description of the calculated attribute.</p>
            conditions: <p>The conditions including range, object count, and threshold for the calculated attribute.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.update_calculated_attribute_definition_request.UpdateCalculatedAttributeDefinitionRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.update_calculated_attribute_definition_response.UpdateCalculatedAttributeDefinitionResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.update_calculated_attribute_definition

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.update_calculated_attribute_definition.update_calculated_attribute_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.update_calculated_attribute_definition_request.UpdateCalculatedAttributeDefinitionRequest = {
            "domain_name": domain_name,
            "calculated_attribute_name": calculated_attribute_name,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if conditions is not None:
            input_["conditions"] = conditions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_domain(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        default_expiration_days: Optional[
            "capo_customer_profiles.types.expiration_days_integer.expirationDaysInteger"
        ] = None,
        default_encryption_key: Optional[
            "capo_customer_profiles.types.encryption_key.encryptionKey"
        ] = None,
        dead_letter_queue_url: Optional[
            "capo_customer_profiles.types.sqs_queue_url.sqsQueueUrl"
        ] = None,
        matching: Optional[
            "capo_customer_profiles.types.matching_request.MatchingRequest"
        ] = None,
        rule_based_matching: Optional[
            "capo_customer_profiles.types.rule_based_matching_request.RuleBasedMatchingRequest"
        ] = None,
        data_store: Optional[
            "capo_customer_profiles.types.data_store_request.DataStoreRequest"
        ] = None,
        tags: Optional["capo_customer_profiles.types.tag_map.TagMap"] = None,
    ) -> "capo_customer_profiles.types.update_domain_response.UpdateDomainResponse":
        """<p>Updates the properties of a domain, including creating or selecting a dead letter queue or an encryption key.</p> <p>After a domain is created, the name can’t be changed.</p> <p>Use this API or <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html">CreateDomain</a> to enable <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html">identity resolution</a>: set <code>Matching</code> to true.</p> <p>To prevent cross-service impersonation when you call this API, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html">Cross-service confused deputy prevention</a> for sample policies that you should apply. </p> <p>To add or remove tags on an existing Domain, see <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html">TagResource</a>/<a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html">UntagResource</a>.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            default_expiration_days: <p>The default number of days until the data within the domain expires.</p>
            default_encryption_key: <p>The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage. If specified as an empty string, it will clear any existing value.</p>
            dead_letter_queue_url: <p>The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications. If specified as an empty string, it will clear any existing value. You must set up a policy on the DeadLetterQueue for the SendMessage operation to enable Amazon Connect Customer Profiles to send messages to the DeadLetterQueue.</p>
            matching: <p>The process of matching duplicate profiles. If <code>Matching</code> = <code>true</code>, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains. </p> <p>After the Identity Resolution Job completes, use the <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html">GetMatches</a> API to return and review the results. Or, if you have configured <code>ExportingConfig</code> in the <code>MatchingRequest</code>, you can download the results from S3.</p>
            rule_based_matching: <p>The process of matching duplicate profiles using the rule-Based matching. If <code>RuleBasedMatching</code> = true, Connect Customer Customer Profiles will start to match and merge your profiles according to your configuration in the <code>RuleBasedMatchingRequest</code>. You can use the <code>ListRuleBasedMatches</code> and <code>GetSimilarProfiles</code> API to return and review the results. Also, if you have configured <code>ExportingConfig</code> in the <code>RuleBasedMatchingRequest</code>, you can download the results from S3.</p>
            data_store: <p>Set to true to enabled data store for this domain.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.update_domain_request.UpdateDomainRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.update_domain_response.UpdateDomainResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.update_domain

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.update_domain.update_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.update_domain_request.UpdateDomainRequest = {
            "domain_name": domain_name
        }
        if default_expiration_days is not None:
            input_["default_expiration_days"] = default_expiration_days
        if default_encryption_key is not None:
            input_["default_encryption_key"] = default_encryption_key
        if dead_letter_queue_url is not None:
            input_["dead_letter_queue_url"] = dead_letter_queue_url
        if matching is not None:
            input_["matching"] = matching
        if rule_based_matching is not None:
            input_["rule_based_matching"] = rule_based_matching
        if data_store is not None:
            input_["data_store"] = data_store
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_domain_layout(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        layout_definition_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        description: Optional[
            "capo_customer_profiles.types.sensitive_text.sensitiveText"
        ] = None,
        display_name: Optional[
            "capo_customer_profiles.types.display_name.displayName"
        ] = None,
        is_default: Optional["capo_customer_profiles.types.boolean.boolean"] = None,
        layout_type: Optional[
            "capo_customer_profiles.types.layout_type.LayoutType"
        ] = None,
        layout: Optional[
            "capo_customer_profiles.types.sensitive_string1_to2000000.sensitiveString1To2000000"
        ] = None,
    ) -> "capo_customer_profiles.types.update_domain_layout_response.UpdateDomainLayoutResponse":
        """<p>Updates the layout used to view data for a specific domain. This API can only be invoked from the Amazon Connect admin website.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            layout_definition_name: <p>The unique name of the layout.</p>
            description: <p>The description of the layout</p>
            display_name: <p>The display name of the layout</p>
            is_default: <p>If set to true for a layout, this layout will be used by default to view data. If set to false, then the layout will not be used by default, but it can be used to view data by explicitly selecting it in the console.</p>
            layout_type: <p>The type of layout that can be used to view data under a Customer Profiles domain.</p>
            layout: <p>A customizable layout that can be used to view data under a Customer Profiles domain.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.update_domain_layout_request.UpdateDomainLayoutRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.update_domain_layout_response.UpdateDomainLayoutResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.update_domain_layout

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.update_domain_layout.update_domain_layout(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.update_domain_layout_request.UpdateDomainLayoutRequest = {
            "domain_name": domain_name,
            "layout_definition_name": layout_definition_name,
        }
        if description is not None:
            input_["description"] = description
        if display_name is not None:
            input_["display_name"] = display_name
        if is_default is not None:
            input_["is_default"] = is_default
        if layout_type is not None:
            input_["layout_type"] = layout_type
        if layout is not None:
            input_["layout"] = layout

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_event_trigger(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        event_trigger_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        object_type_name: Optional[
            "capo_customer_profiles.types.type_name.typeName"
        ] = None,
        description: Optional[
            "capo_customer_profiles.types.sensitive_text.sensitiveText"
        ] = None,
        event_trigger_conditions: Optional[
            "capo_customer_profiles.types.event_trigger_conditions.EventTriggerConditions"
        ] = None,
        segment_filter: Optional["capo_customer_profiles.types.name.name"] = None,
        event_trigger_limits: Optional[
            "capo_customer_profiles.types.event_trigger_limits.EventTriggerLimits"
        ] = None,
    ) -> "capo_customer_profiles.types.update_event_trigger_response.UpdateEventTriggerResponse":
        """<p>Update the properties of an Event Trigger.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            event_trigger_name: <p>The unique name of the event trigger.</p>
            object_type_name: <p>The unique name of the object type.</p>
            description: <p>The description of the event trigger.</p>
            event_trigger_conditions: <p>A list of conditions that determine when an event should trigger the destination.</p>
            segment_filter: <p>The destination is triggered only for profiles that meet the criteria of a segment definition.</p>
            event_trigger_limits: <p>Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.update_event_trigger_request.UpdateEventTriggerRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.update_event_trigger_response.UpdateEventTriggerResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.update_event_trigger

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.update_event_trigger.update_event_trigger(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.update_event_trigger_request.UpdateEventTriggerRequest = {
            "domain_name": domain_name,
            "event_trigger_name": event_trigger_name,
        }
        if object_type_name is not None:
            input_["object_type_name"] = object_type_name
        if description is not None:
            input_["description"] = description
        if event_trigger_conditions is not None:
            input_["event_trigger_conditions"] = event_trigger_conditions
        if segment_filter is not None:
            input_["segment_filter"] = segment_filter
        if event_trigger_limits is not None:
            input_["event_trigger_limits"] = event_trigger_limits

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_profile(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        profile_id: "capo_customer_profiles.types.uuid.uuid",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        additional_information: Optional[
            "capo_customer_profiles.types.sensitive_string0_to1000.sensitiveString0To1000"
        ] = None,
        account_number: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        party_type: Optional[
            "capo_customer_profiles.types.party_type.PartyType"
        ] = None,
        business_name: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        first_name: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        middle_name: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        last_name: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        birth_date: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        gender: Optional["capo_customer_profiles.types.gender.Gender"] = None,
        phone_number: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        mobile_phone_number: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        home_phone_number: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        business_phone_number: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        email_address: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        personal_email_address: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        business_email_address: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        address: Optional[
            "capo_customer_profiles.types.update_address.UpdateAddress"
        ] = None,
        shipping_address: Optional[
            "capo_customer_profiles.types.update_address.UpdateAddress"
        ] = None,
        mailing_address: Optional[
            "capo_customer_profiles.types.update_address.UpdateAddress"
        ] = None,
        billing_address: Optional[
            "capo_customer_profiles.types.update_address.UpdateAddress"
        ] = None,
        attributes: Optional[
            "capo_customer_profiles.types.update_attributes.UpdateAttributes"
        ] = None,
        party_type_string: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        gender_string: Optional[
            "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
        ] = None,
        profile_type: Optional[
            "capo_customer_profiles.types.profile_type.ProfileType"
        ] = None,
        engagement_preferences: Optional[
            "capo_customer_profiles.types.engagement_preferences.EngagementPreferences"
        ] = None,
    ) -> "capo_customer_profiles.types.update_profile_response.UpdateProfileResponse":
        """<p>Updates the properties of a profile. The ProfileId is required for updating a customer profile.</p> <p>When calling the UpdateProfile API, specifying an empty string value means that any existing value will be removed. Not specifying a string value means that any value already there will be kept.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            profile_id: <p>The unique identifier of a customer profile.</p>
            additional_information: <p>Any additional information relevant to the customer’s profile.</p>
            account_number: <p>An account number that you have assigned to the customer.</p>
            party_type: <p>The type of profile used to describe the customer.</p>
            business_name: <p>The name of the customer’s business.</p>
            first_name: <p>The customer’s first name.</p>
            middle_name: <p>The customer’s middle name.</p>
            last_name: <p>The customer’s last name.</p>
            birth_date: <p>The customer’s birth date. </p>
            gender: <p>The gender with which the customer identifies. </p>
            phone_number: <p>The customer’s phone number, which has not been specified as a mobile, home, or business number. </p>
            mobile_phone_number: <p>The customer’s mobile phone number.</p>
            home_phone_number: <p>The customer’s home phone number.</p>
            business_phone_number: <p>The customer’s business phone number.</p>
            email_address: <p>The customer’s email address, which has not been specified as a personal or business address. </p>
            personal_email_address: <p>The customer’s personal email address.</p>
            business_email_address: <p>The customer’s business email address.</p>
            address: <p>A generic address associated with the customer that is not mailing, shipping, or billing.</p>
            shipping_address: <p>The customer’s shipping address.</p>
            mailing_address: <p>The customer’s mailing address.</p>
            billing_address: <p>The customer’s billing address.</p>
            attributes: <p>A key value pair of attributes of a customer profile.</p>
            party_type_string: <p>An alternative to <code>PartyType</code> which accepts any string as input.</p>
            gender_string: <p>An alternative to <code>Gender</code> which accepts any string as input.</p>
            profile_type: <p>Determines the type of the profile.</p>
            engagement_preferences: <p>Object that defines users preferred methods of engagement.</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.update_profile_request.UpdateProfileRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.update_profile_response.UpdateProfileResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.update_profile

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.update_profile.update_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.update_profile_request.UpdateProfileRequest = {
            "domain_name": domain_name,
            "profile_id": profile_id,
        }
        if additional_information is not None:
            input_["additional_information"] = additional_information
        if account_number is not None:
            input_["account_number"] = account_number
        if party_type is not None:
            input_["party_type"] = party_type
        if business_name is not None:
            input_["business_name"] = business_name
        if first_name is not None:
            input_["first_name"] = first_name
        if middle_name is not None:
            input_["middle_name"] = middle_name
        if last_name is not None:
            input_["last_name"] = last_name
        if birth_date is not None:
            input_["birth_date"] = birth_date
        if gender is not None:
            input_["gender"] = gender
        if phone_number is not None:
            input_["phone_number"] = phone_number
        if mobile_phone_number is not None:
            input_["mobile_phone_number"] = mobile_phone_number
        if home_phone_number is not None:
            input_["home_phone_number"] = home_phone_number
        if business_phone_number is not None:
            input_["business_phone_number"] = business_phone_number
        if email_address is not None:
            input_["email_address"] = email_address
        if personal_email_address is not None:
            input_["personal_email_address"] = personal_email_address
        if business_email_address is not None:
            input_["business_email_address"] = business_email_address
        if address is not None:
            input_["address"] = address
        if shipping_address is not None:
            input_["shipping_address"] = shipping_address
        if mailing_address is not None:
            input_["mailing_address"] = mailing_address
        if billing_address is not None:
            input_["billing_address"] = billing_address
        if attributes is not None:
            input_["attributes"] = attributes
        if party_type_string is not None:
            input_["party_type_string"] = party_type_string
        if gender_string is not None:
            input_["gender_string"] = gender_string
        if profile_type is not None:
            input_["profile_type"] = profile_type
        if engagement_preferences is not None:
            input_["engagement_preferences"] = engagement_preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_recommender(
        self,
        domain_name: "capo_customer_profiles.types.name.name",
        recommender_name: "capo_customer_profiles.types.name.name",
        *,
        config_overrides: Optional[CustomerProfilesClientConfig] = None,
        description: Optional[
            "capo_customer_profiles.types.sensitive_text.sensitiveText"
        ] = None,
        recommender_config: Optional[
            "capo_customer_profiles.types.recommender_config.RecommenderConfig"
        ] = None,
        recommender_version_name: Optional[
            "capo_customer_profiles.types.recommender_version_name.RecommenderVersionName"
        ] = None,
    ) -> "capo_customer_profiles.types.update_recommender_response.UpdateRecommenderResponse":
        """<p>Updates the properties of an existing recommender, allowing you to modify its configuration and description.</p>

        Args:
            domain_name: <p>The unique name of the domain.</p>
            recommender_name: <p>The name of the recommender to update.</p>
            description: <p>The new description to assign to the recommender.</p>
            recommender_config: <p>The new configuration settings to apply to the recommender, including updated parameters and settings that define its behavior.</p>
            recommender_version_name: <p>The name of a specific recommender version to activate as part of this update (for example, to roll back to a previously trained version).</p>

        Raises:
            capo_customer_profiles.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_customer_profiles.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_customer_profiles.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred.</p>
            capo_customer_profiles.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_customer_profiles.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_customer_profiles.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_customer_profiles.types.update_recommender_request.UpdateRecommenderRequest]",
        ) -> OperationResponse[
            "capo_customer_profiles.types.update_recommender_response.UpdateRecommenderResponse"
        ]:
            import capo_customer_profiles._operations.customer_profiles_20200815.update_recommender

            output, http_response = (
                capo_customer_profiles._operations.customer_profiles_20200815.update_recommender.update_recommender(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_customer_profiles.types.update_recommender_request.UpdateRecommenderRequest = {
            "domain_name": domain_name,
            "recommender_name": recommender_name,
        }
        if description is not None:
            input_["description"] = description
        if recommender_config is not None:
            input_["recommender_config"] = recommender_config
        if recommender_version_name is not None:
            input_["recommender_version_name"] = recommender_version_name

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
