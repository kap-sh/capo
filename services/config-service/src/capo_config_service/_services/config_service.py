"""Generated from Smithy shape ``com.amazonaws.configservice#StarlingDoveService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_config_service._auth._signers
import capo_config_service._auth._sigv4
from capo_config_service._auth._identity import Credentials
from capo_config_service._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_config_service._auth._zapros_handler import AuthMiddleware
from capo_config_service._pagination import resolve_path as _resolve_path
from capo_config_service._services._aws_config import aws_config
from capo_config_service._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_config_service.types.account_aggregation_source_list
    import capo_config_service.types.account_id
    import capo_config_service.types.aggregate_compliance_by_conformance_pack
    import capo_config_service.types.aggregate_conformance_pack_compliance_filters
    import capo_config_service.types.aggregate_conformance_pack_compliance_summary_filters
    import capo_config_service.types.aggregate_conformance_pack_compliance_summary_group_key
    import capo_config_service.types.aggregate_evaluation_result
    import capo_config_service.types.aggregate_resource_identifier
    import capo_config_service.types.aggregated_source_status
    import capo_config_service.types.aggregated_source_status_type_list
    import capo_config_service.types.aggregation_authorization
    import capo_config_service.types.aggregator_filters
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.associate_resource_types_request
    import capo_config_service.types.associate_resource_types_response
    import capo_config_service.types.aws_region
    import capo_config_service.types.base_resource_id
    import capo_config_service.types.batch_get_aggregate_resource_config_request
    import capo_config_service.types.batch_get_aggregate_resource_config_response
    import capo_config_service.types.batch_get_resource_config_request
    import capo_config_service.types.batch_get_resource_config_response
    import capo_config_service.types.boolean
    import capo_config_service.types.channel_name
    import capo_config_service.types.chronological_order
    import capo_config_service.types.client_token
    import capo_config_service.types.compliance_by_config_rule
    import capo_config_service.types.compliance_by_resource
    import capo_config_service.types.compliance_type
    import capo_config_service.types.compliance_types
    import capo_config_service.types.config_rule
    import capo_config_service.types.config_rule_compliance_filters
    import capo_config_service.types.config_rule_compliance_summary_filters
    import capo_config_service.types.config_rule_compliance_summary_group_key
    import capo_config_service.types.config_rule_evaluation_status
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.config_rule_names
    import capo_config_service.types.configuration
    import capo_config_service.types.configuration_aggregator
    import capo_config_service.types.configuration_aggregator_name
    import capo_config_service.types.configuration_aggregator_name_list
    import capo_config_service.types.configuration_item
    import capo_config_service.types.configuration_recorder
    import capo_config_service.types.configuration_recorder_filter_list
    import capo_config_service.types.configuration_recorder_name_list
    import capo_config_service.types.configuration_recorder_summary
    import capo_config_service.types.conformance_pack_compliance_filters
    import capo_config_service.types.conformance_pack_compliance_scores_filters
    import capo_config_service.types.conformance_pack_compliance_summary
    import capo_config_service.types.conformance_pack_detail
    import capo_config_service.types.conformance_pack_evaluation_filters
    import capo_config_service.types.conformance_pack_input_parameters
    import capo_config_service.types.conformance_pack_name
    import capo_config_service.types.conformance_pack_names_list
    import capo_config_service.types.conformance_pack_names_to_summarize_list
    import capo_config_service.types.conformance_pack_rule_compliance
    import capo_config_service.types.conformance_pack_status_detail
    import capo_config_service.types.connector_configuration
    import capo_config_service.types.connector_filter_list
    import capo_config_service.types.connector_summary
    import capo_config_service.types.cosmos_page_limit
    import capo_config_service.types.date
    import capo_config_service.types.delete_aggregation_authorization_request
    import capo_config_service.types.delete_config_rule_request
    import capo_config_service.types.delete_configuration_aggregator_request
    import capo_config_service.types.delete_configuration_recorder_request
    import capo_config_service.types.delete_conformance_pack_request
    import capo_config_service.types.delete_connector_request
    import capo_config_service.types.delete_delivery_channel_request
    import capo_config_service.types.delete_evaluation_results_request
    import capo_config_service.types.delete_evaluation_results_response
    import capo_config_service.types.delete_organization_config_rule_request
    import capo_config_service.types.delete_organization_conformance_pack_request
    import capo_config_service.types.delete_pending_aggregation_request_request
    import capo_config_service.types.delete_remediation_configuration_request
    import capo_config_service.types.delete_remediation_configuration_response
    import capo_config_service.types.delete_remediation_exceptions_request
    import capo_config_service.types.delete_remediation_exceptions_response
    import capo_config_service.types.delete_resource_config_request
    import capo_config_service.types.delete_retention_configuration_request
    import capo_config_service.types.delete_service_linked_configuration_recorder_request
    import capo_config_service.types.delete_service_linked_configuration_recorder_response
    import capo_config_service.types.delete_stored_query_request
    import capo_config_service.types.delete_stored_query_response
    import capo_config_service.types.deliver_config_snapshot_request
    import capo_config_service.types.deliver_config_snapshot_response
    import capo_config_service.types.delivery_channel
    import capo_config_service.types.delivery_channel_name_list
    import capo_config_service.types.delivery_s3_bucket
    import capo_config_service.types.delivery_s3_key_prefix
    import capo_config_service.types.describe_aggregate_compliance_by_config_rules_request
    import capo_config_service.types.describe_aggregate_compliance_by_config_rules_response
    import capo_config_service.types.describe_aggregate_compliance_by_conformance_packs_request
    import capo_config_service.types.describe_aggregate_compliance_by_conformance_packs_response
    import capo_config_service.types.describe_aggregation_authorizations_request
    import capo_config_service.types.describe_aggregation_authorizations_response
    import capo_config_service.types.describe_compliance_by_config_rule_request
    import capo_config_service.types.describe_compliance_by_config_rule_response
    import capo_config_service.types.describe_compliance_by_resource_request
    import capo_config_service.types.describe_compliance_by_resource_response
    import capo_config_service.types.describe_config_rule_evaluation_status_request
    import capo_config_service.types.describe_config_rule_evaluation_status_response
    import capo_config_service.types.describe_config_rules_filters
    import capo_config_service.types.describe_config_rules_request
    import capo_config_service.types.describe_config_rules_response
    import capo_config_service.types.describe_configuration_aggregator_sources_status_request
    import capo_config_service.types.describe_configuration_aggregator_sources_status_response
    import capo_config_service.types.describe_configuration_aggregators_request
    import capo_config_service.types.describe_configuration_aggregators_response
    import capo_config_service.types.describe_configuration_recorder_status_request
    import capo_config_service.types.describe_configuration_recorder_status_response
    import capo_config_service.types.describe_configuration_recorders_request
    import capo_config_service.types.describe_configuration_recorders_response
    import capo_config_service.types.describe_conformance_pack_compliance_limit
    import capo_config_service.types.describe_conformance_pack_compliance_request
    import capo_config_service.types.describe_conformance_pack_compliance_response
    import capo_config_service.types.describe_conformance_pack_status_request
    import capo_config_service.types.describe_conformance_pack_status_response
    import capo_config_service.types.describe_conformance_packs_request
    import capo_config_service.types.describe_conformance_packs_response
    import capo_config_service.types.describe_delivery_channel_status_request
    import capo_config_service.types.describe_delivery_channel_status_response
    import capo_config_service.types.describe_delivery_channels_request
    import capo_config_service.types.describe_delivery_channels_response
    import capo_config_service.types.describe_organization_config_rule_statuses_request
    import capo_config_service.types.describe_organization_config_rule_statuses_response
    import capo_config_service.types.describe_organization_config_rules_request
    import capo_config_service.types.describe_organization_config_rules_response
    import capo_config_service.types.describe_organization_conformance_pack_statuses_request
    import capo_config_service.types.describe_organization_conformance_pack_statuses_response
    import capo_config_service.types.describe_organization_conformance_packs_request
    import capo_config_service.types.describe_organization_conformance_packs_response
    import capo_config_service.types.describe_pending_aggregation_requests_limit
    import capo_config_service.types.describe_pending_aggregation_requests_request
    import capo_config_service.types.describe_pending_aggregation_requests_response
    import capo_config_service.types.describe_remediation_configurations_request
    import capo_config_service.types.describe_remediation_configurations_response
    import capo_config_service.types.describe_remediation_exceptions_request
    import capo_config_service.types.describe_remediation_exceptions_response
    import capo_config_service.types.describe_remediation_execution_status_request
    import capo_config_service.types.describe_remediation_execution_status_response
    import capo_config_service.types.describe_retention_configurations_request
    import capo_config_service.types.describe_retention_configurations_response
    import capo_config_service.types.disassociate_resource_types_request
    import capo_config_service.types.disassociate_resource_types_response
    import capo_config_service.types.earlier_time
    import capo_config_service.types.evaluation_context
    import capo_config_service.types.evaluation_mode
    import capo_config_service.types.evaluation_result
    import capo_config_service.types.evaluation_timeout
    import capo_config_service.types.evaluations
    import capo_config_service.types.excluded_accounts
    import capo_config_service.types.expression
    import capo_config_service.types.external_evaluation
    import capo_config_service.types.get_aggregate_compliance_details_by_config_rule_request
    import capo_config_service.types.get_aggregate_compliance_details_by_config_rule_response
    import capo_config_service.types.get_aggregate_config_rule_compliance_summary_request
    import capo_config_service.types.get_aggregate_config_rule_compliance_summary_response
    import capo_config_service.types.get_aggregate_conformance_pack_compliance_summary_request
    import capo_config_service.types.get_aggregate_conformance_pack_compliance_summary_response
    import capo_config_service.types.get_aggregate_discovered_resource_counts_request
    import capo_config_service.types.get_aggregate_discovered_resource_counts_response
    import capo_config_service.types.get_aggregate_resource_config_request
    import capo_config_service.types.get_aggregate_resource_config_response
    import capo_config_service.types.get_compliance_details_by_config_rule_request
    import capo_config_service.types.get_compliance_details_by_config_rule_response
    import capo_config_service.types.get_compliance_details_by_resource_request
    import capo_config_service.types.get_compliance_details_by_resource_response
    import capo_config_service.types.get_compliance_summary_by_config_rule_response
    import capo_config_service.types.get_compliance_summary_by_resource_type_request
    import capo_config_service.types.get_compliance_summary_by_resource_type_response
    import capo_config_service.types.get_conformance_pack_compliance_details_limit
    import capo_config_service.types.get_conformance_pack_compliance_details_request
    import capo_config_service.types.get_conformance_pack_compliance_details_response
    import capo_config_service.types.get_conformance_pack_compliance_summary_request
    import capo_config_service.types.get_conformance_pack_compliance_summary_response
    import capo_config_service.types.get_connector_request
    import capo_config_service.types.get_connector_response
    import capo_config_service.types.get_custom_rule_policy_request
    import capo_config_service.types.get_custom_rule_policy_response
    import capo_config_service.types.get_discovered_resource_counts_request
    import capo_config_service.types.get_discovered_resource_counts_response
    import capo_config_service.types.get_organization_config_rule_detailed_status_request
    import capo_config_service.types.get_organization_config_rule_detailed_status_response
    import capo_config_service.types.get_organization_conformance_pack_detailed_status_request
    import capo_config_service.types.get_organization_conformance_pack_detailed_status_response
    import capo_config_service.types.get_organization_custom_rule_policy_request
    import capo_config_service.types.get_organization_custom_rule_policy_response
    import capo_config_service.types.get_resource_config_history_request
    import capo_config_service.types.get_resource_config_history_response
    import capo_config_service.types.get_resource_evaluation_summary_request
    import capo_config_service.types.get_resource_evaluation_summary_response
    import capo_config_service.types.get_stored_query_request
    import capo_config_service.types.get_stored_query_response
    import capo_config_service.types.group_by_api_limit
    import capo_config_service.types.later_time
    import capo_config_service.types.limit
    import capo_config_service.types.list_aggregate_discovered_resources_request
    import capo_config_service.types.list_aggregate_discovered_resources_response
    import capo_config_service.types.list_configuration_recorders_request
    import capo_config_service.types.list_configuration_recorders_response
    import capo_config_service.types.list_conformance_pack_compliance_scores_request
    import capo_config_service.types.list_conformance_pack_compliance_scores_response
    import capo_config_service.types.list_connectors_max_results
    import capo_config_service.types.list_connectors_request
    import capo_config_service.types.list_connectors_response
    import capo_config_service.types.list_discovered_resources_request
    import capo_config_service.types.list_discovered_resources_response
    import capo_config_service.types.list_resource_evaluations_page_item_limit
    import capo_config_service.types.list_resource_evaluations_request
    import capo_config_service.types.list_resource_evaluations_response
    import capo_config_service.types.list_stored_queries_request
    import capo_config_service.types.list_stored_queries_response
    import capo_config_service.types.list_tags_for_resource_request
    import capo_config_service.types.list_tags_for_resource_response
    import capo_config_service.types.max_results
    import capo_config_service.types.member_account_status
    import capo_config_service.types.next_token
    import capo_config_service.types.organization_aggregation_source
    import capo_config_service.types.organization_config_rule
    import capo_config_service.types.organization_config_rule_name
    import capo_config_service.types.organization_config_rule_names
    import capo_config_service.types.organization_config_rule_status
    import capo_config_service.types.organization_conformance_pack
    import capo_config_service.types.organization_conformance_pack_detailed_status
    import capo_config_service.types.organization_conformance_pack_name
    import capo_config_service.types.organization_conformance_pack_names
    import capo_config_service.types.organization_conformance_pack_status
    import capo_config_service.types.organization_custom_policy_rule_metadata
    import capo_config_service.types.organization_custom_rule_metadata
    import capo_config_service.types.organization_managed_rule_metadata
    import capo_config_service.types.organization_resource_detailed_status_filters
    import capo_config_service.types.page_size_limit
    import capo_config_service.types.pending_aggregation_request
    import capo_config_service.types.put_aggregation_authorization_request
    import capo_config_service.types.put_aggregation_authorization_response
    import capo_config_service.types.put_config_rule_request
    import capo_config_service.types.put_configuration_aggregator_request
    import capo_config_service.types.put_configuration_aggregator_response
    import capo_config_service.types.put_configuration_recorder_request
    import capo_config_service.types.put_conformance_pack_request
    import capo_config_service.types.put_conformance_pack_response
    import capo_config_service.types.put_connector_request
    import capo_config_service.types.put_connector_response
    import capo_config_service.types.put_delivery_channel_request
    import capo_config_service.types.put_evaluations_request
    import capo_config_service.types.put_evaluations_response
    import capo_config_service.types.put_external_evaluation_request
    import capo_config_service.types.put_external_evaluation_response
    import capo_config_service.types.put_organization_config_rule_request
    import capo_config_service.types.put_organization_config_rule_response
    import capo_config_service.types.put_organization_conformance_pack_request
    import capo_config_service.types.put_organization_conformance_pack_response
    import capo_config_service.types.put_remediation_configurations_request
    import capo_config_service.types.put_remediation_configurations_response
    import capo_config_service.types.put_remediation_exceptions_request
    import capo_config_service.types.put_remediation_exceptions_response
    import capo_config_service.types.put_resource_config_request
    import capo_config_service.types.put_retention_configuration_request
    import capo_config_service.types.put_retention_configuration_response
    import capo_config_service.types.put_service_linked_configuration_recorder_request
    import capo_config_service.types.put_service_linked_configuration_recorder_response
    import capo_config_service.types.put_stored_query_request
    import capo_config_service.types.put_stored_query_response
    import capo_config_service.types.put_third_party_service_linked_configuration_recorder_request
    import capo_config_service.types.put_third_party_service_linked_configuration_recorder_response
    import capo_config_service.types.query_name
    import capo_config_service.types.recorder_name
    import capo_config_service.types.reevaluate_config_rule_names
    import capo_config_service.types.remediation_configurations
    import capo_config_service.types.remediation_exception_resource_keys
    import capo_config_service.types.remediation_execution_status
    import capo_config_service.types.resource_count_filters
    import capo_config_service.types.resource_count_group_key
    import capo_config_service.types.resource_details
    import capo_config_service.types.resource_evaluation
    import capo_config_service.types.resource_evaluation_filters
    import capo_config_service.types.resource_evaluation_id
    import capo_config_service.types.resource_filters
    import capo_config_service.types.resource_id
    import capo_config_service.types.resource_id_list
    import capo_config_service.types.resource_identifier
    import capo_config_service.types.resource_identifiers_list
    import capo_config_service.types.resource_keys
    import capo_config_service.types.resource_name
    import capo_config_service.types.resource_type
    import capo_config_service.types.resource_type_list
    import capo_config_service.types.resource_type_string
    import capo_config_service.types.resource_types
    import capo_config_service.types.retention_configuration
    import capo_config_service.types.retention_configuration_name
    import capo_config_service.types.retention_configuration_name_list
    import capo_config_service.types.retention_period_in_days
    import capo_config_service.types.rule_limit
    import capo_config_service.types.schema_version_id
    import capo_config_service.types.scope_configuration
    import capo_config_service.types.select_aggregate_resource_config_request
    import capo_config_service.types.select_aggregate_resource_config_response
    import capo_config_service.types.select_resource_config_request
    import capo_config_service.types.select_resource_config_response
    import capo_config_service.types.service_principal
    import capo_config_service.types.sort_by
    import capo_config_service.types.sort_order
    import capo_config_service.types.start_config_rules_evaluation_request
    import capo_config_service.types.start_config_rules_evaluation_response
    import capo_config_service.types.start_configuration_recorder_request
    import capo_config_service.types.start_remediation_execution_request
    import capo_config_service.types.start_remediation_execution_response
    import capo_config_service.types.start_resource_evaluation_request
    import capo_config_service.types.start_resource_evaluation_response
    import capo_config_service.types.status_detail_filters
    import capo_config_service.types.stop_configuration_recorder_request
    import capo_config_service.types.stored_query
    import capo_config_service.types.string
    import capo_config_service.types.string_with_char_limit64
    import capo_config_service.types.string_with_char_limit256
    import capo_config_service.types.string_with_char_limit1024
    import capo_config_service.types.tag
    import capo_config_service.types.tag_key_list
    import capo_config_service.types.tag_list
    import capo_config_service.types.tag_resource_request
    import capo_config_service.types.tags
    import capo_config_service.types.tags_list
    import capo_config_service.types.template_body
    import capo_config_service.types.template_s3_uri
    import capo_config_service.types.template_ssm_document_details
    import capo_config_service.types.untag_resource_request


class ConfigServiceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ConfigServiceClient:
    """A client for the ``ConfigService`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
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
        anonymous: bool | None = None,
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
        self._config = ConfigServiceClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[ConfigServiceClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ConfigServiceClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def associate_resource_types(
        self,
        configuration_recorder_arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName",
        resource_types: "capo_config_service.types.resource_type_list.ResourceTypeList",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.associate_resource_types_response.AssociateResourceTypesResponse":
        """<p>Adds all resource types specified in the <code>ResourceTypes</code> list to the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html">RecordingGroup</a> of specified configuration recorder and includes those resource types when recording.</p> <p>For this operation, the specified configuration recorder must use a <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html">RecordingStrategy</a> that is either <code>INCLUSION_BY_RESOURCE_TYPES</code> or <code>EXCLUSION_BY_RESOURCE_TYPES</code>.</p>

        Args:
            configuration_recorder_arn: <p>The Amazon Resource Name (ARN) of the specified configuration recorder.</p>
            resource_types: <p>The list of resource types you want to add to the recording group of the specified configuration recorder.</p>

        Raises:
            capo_config_service.errors.conflict_exception.ConflictException: <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because a service-linked recorder already exists for the specified service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because the specified service principal does not support multiple configuration recorders and one already exists.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector or service principal. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, you cannot create a connector because a connector already exists for the specified connector configuration.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, you cannot delete the service-linked recorder because it is currently in use by the linked Amazon Web Services service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConnector.html">DeleteConnector</a>, another in-progress operation is currently referencing the connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteDeliveryChannel.html">DeleteDeliveryChannel</a>, you cannot delete the specified delivery channel because the customer managed configuration recorder is running. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html">StopConfigurationRecorder</a> operation to stop the customer managed configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>For service-linked configuration recorders, the configuration recorder is not in use by the service. No association or dissociation of resource types is permitted.</p> </li> <li> <p>For service-linked configuration recorders, your requested change to the configuration recorder has been denied by its linked Amazon Web Services service.</p> </li> </ul>
            capo_config_service.errors.no_such_configuration_recorder_exception.NoSuchConfigurationRecorderException: <p>You have specified a configuration recorder that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.associate_resource_types_request.AssociateResourceTypesRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.associate_resource_types_response.AssociateResourceTypesResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.associate_resource_types

            output, http_response = (
                capo_config_service._operations.starling_dove_service.associate_resource_types.associate_resource_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.associate_resource_types_request.AssociateResourceTypesRequest = {
            "configuration_recorder_arn": configuration_recorder_arn,
            "resource_types": resource_types,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_aggregate_resource_config(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        resource_identifiers: "capo_config_service.types.resource_identifiers_list.ResourceIdentifiersList",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.batch_get_aggregate_resource_config_response.BatchGetAggregateResourceConfigResponse":
        """<p>Returns the current configuration items for resources that are present in your Config aggregator. The operation also returns a list of resources that are not processed in the current request. If there are no unprocessed resources, the operation returns an empty <code>unprocessedResourceIdentifiers</code> list. </p> <note> <ul> <li> <p>The API does not return results for deleted resources.</p> </li> <li> <p> The API does not return tags and relationships.</p> </li> </ul> </note>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>
            resource_identifiers: <p>A list of aggregate ResourceIdentifiers objects. </p>

        Raises:
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.batch_get_aggregate_resource_config_request.BatchGetAggregateResourceConfigRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.batch_get_aggregate_resource_config_response.BatchGetAggregateResourceConfigResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.batch_get_aggregate_resource_config

            output, http_response = (
                capo_config_service._operations.starling_dove_service.batch_get_aggregate_resource_config.batch_get_aggregate_resource_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.batch_get_aggregate_resource_config_request.BatchGetAggregateResourceConfigRequest = {
            "configuration_aggregator_name": configuration_aggregator_name,
            "resource_identifiers": resource_identifiers,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_resource_config(
        self,
        resource_keys: "capo_config_service.types.resource_keys.ResourceKeys",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.batch_get_resource_config_response.BatchGetResourceConfigResponse":
        """<p>Returns the <code>BaseConfigurationItem</code> for one or more requested resources. The operation also returns a list of resources that are not processed in the current request. If there are no unprocessed resources, the operation returns an empty unprocessedResourceKeys list. </p> <note> <ul> <li> <p>The API does not return results for deleted resources.</p> </li> <li> <p> The API does not return any tags for the requested resources. This information is filtered out of the supplementaryConfiguration section of the API response.</p> </li> </ul> </note>

        Args:
            resource_keys: <p>A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.</p>

        Raises:
            capo_config_service.errors.no_available_configuration_recorder_exception.NoAvailableConfigurationRecorderException: <p>There are no customer managed configuration recorders available to record your resources. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html">PutConfigurationRecorder</a> operation to create the customer managed configuration recorder.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.batch_get_resource_config_request.BatchGetResourceConfigRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.batch_get_resource_config_response.BatchGetResourceConfigResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.batch_get_resource_config

            output, http_response = (
                capo_config_service._operations.starling_dove_service.batch_get_resource_config.batch_get_resource_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.batch_get_resource_config_request.BatchGetResourceConfigRequest = {
            "resource_keys": resource_keys
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_aggregation_authorization(
        self,
        authorized_account_id: "capo_config_service.types.account_id.AccountId",
        authorized_aws_region: "capo_config_service.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the authorization granted to the specified configuration aggregator account in a specified region.</p>

        Args:
            authorized_account_id: <p>The 12-digit account ID of the account authorized to aggregate data.</p>
            authorized_aws_region: <p>The region authorized to collect aggregated data.</p>

        Raises:
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_aggregation_authorization_request.DeleteAggregationAuthorizationRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_aggregation_authorization

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_aggregation_authorization.delete_aggregation_authorization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_aggregation_authorization_request.DeleteAggregationAuthorizationRequest = {
            "authorized_account_id": authorized_account_id,
            "authorized_aws_region": authorized_aws_region,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_config_rule(
        self,
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified Config rule and all of its evaluation results.</p> <p>Config sets the state of a rule to <code>DELETING</code> until the deletion is complete. You cannot update a rule while it is in this state. If you make a <code>PutConfigRule</code> or <code>DeleteConfigRule</code> request for the rule, you will receive a <code>ResourceInUseException</code>.</p> <p>You can check the state of a rule by using the <code>DescribeConfigRules</code> request.</p> <note> <p> <b>Recommendation: Consider excluding the <code>AWS::Config::ResourceCompliance</code> resource type from recording before deleting rules</b> </p> <p>Deleting rules creates configuration items (CIs) for <code>AWS::Config::ResourceCompliance</code> that can affect your costs for the configuration recorder. If you are deleting rules which evaluate a large number of resource types, this can lead to a spike in the number of CIs recorded.</p> <p>To avoid the associated costs, you can opt to disable recording for the <code>AWS::Config::ResourceCompliance</code> resource type before deleting rules, and re-enable recording after the rules have been deleted.</p> <p>However, since deleting rules is an asynchronous process, it might take an hour or more to complete. During the time when recording is disabled for <code>AWS::Config::ResourceCompliance</code>, rule evaluations will not be recorded in the associated resource’s history.</p> </note>

        Args:
            config_rule_name: <p>The name of the Config rule that you want to delete.</p>

        Raises:
            capo_config_service.errors.no_such_config_rule_exception.NoSuchConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.resource_in_use_exception.ResourceInUseException: <p>You see this exception in the following cases: </p> <ul> <li> <p>For DeleteConfigRule, Config is deleting this rule. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, a remediation action is associated with the rule and Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.</p> </li> <li> <p>For PutConfigOrganizationRule, organization Config rule deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteOrganizationConfigRule, organization Config rule creation is in progress. Try your request again later.</p> </li> <li> <p>For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_config_rule_request.DeleteConfigRuleRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_config_rule

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_config_rule.delete_config_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_config_rule_request.DeleteConfigRuleRequest = {
            "config_rule_name": config_rule_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_configuration_aggregator(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified configuration aggregator and the aggregated data associated with the aggregator.</p>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>

        Raises:
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_configuration_aggregator_request.DeleteConfigurationAggregatorRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_configuration_aggregator

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_configuration_aggregator.delete_configuration_aggregator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_configuration_aggregator_request.DeleteConfigurationAggregatorRequest = {
            "configuration_aggregator_name": configuration_aggregator_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_configuration_recorder(
        self,
        configuration_recorder_name: "capo_config_service.types.recorder_name.RecorderName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the customer managed configuration recorder.</p> <p>This operation does not delete the configuration information that was previously recorded. You will be able to access the previously recorded information by using the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceConfigHistory.html">GetResourceConfigHistory</a> operation, but you will not be able to access this information in the Config console until you have created a new customer managed configuration recorder.</p>

        Args:
            configuration_recorder_name: <p>The name of the customer managed configuration recorder that you want to delete. You can retrieve the name of your configuration recorders by using the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> operation.</p>

        Raises:
            capo_config_service.errors.no_such_configuration_recorder_exception.NoSuchConfigurationRecorderException: <p>You have specified a configuration recorder that does not exist.</p>
            capo_config_service.errors.unmodifiable_entity_exception.UnmodifiableEntityException: <p>The requested operation is not valid.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html">PutConfigurationRecorder</a>, you will see this exception because you cannot use this operation to create a service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a> operation to create a service-linked configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigurationRecorder.html">DeleteConfigurationRecorder</a>, you will see this exception because you cannot use this operation to delete a service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a> operation to delete a service-linked configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigurationRecorder.html">StartConfigurationRecorder</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html">StopConfigurationRecorder</a>, you will see this exception because these operations do not affect service-linked configuration recorders. Service-linked configuration recorders are always recording. To stop recording, you must delete the service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a> operation to delete a service-linked configuration recorder.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_configuration_recorder_request.DeleteConfigurationRecorderRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_configuration_recorder

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_configuration_recorder.delete_configuration_recorder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_configuration_recorder_request.DeleteConfigurationRecorderRequest = {
            "configuration_recorder_name": configuration_recorder_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_conformance_pack(
        self,
        conformance_pack_name: "capo_config_service.types.conformance_pack_name.ConformancePackName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified conformance pack and all the Config rules, remediation actions, and all evaluation results within that conformance pack.</p> <p>Config sets the conformance pack to <code>DELETE_IN_PROGRESS</code> until the deletion is complete. You cannot update a conformance pack while it is in this state.</p> <note> <p> <b>Recommendation: Consider excluding the <code>AWS::Config::ResourceCompliance</code> resource type from recording before deleting rules</b> </p> <p>Deleting rules creates configuration items (CIs) for <code>AWS::Config::ResourceCompliance</code> that can affect your costs for the configuration recorder. If you are deleting rules which evaluate a large number of resource types, this can lead to a spike in the number of CIs recorded.</p> <p>To avoid the associated costs, you can opt to disable recording for the <code>AWS::Config::ResourceCompliance</code> resource type before deleting rules, and re-enable recording after the rules have been deleted.</p> <p>However, since deleting rules is an asynchronous process, it might take an hour or more to complete. During the time when recording is disabled for <code>AWS::Config::ResourceCompliance</code>, rule evaluations will not be recorded in the associated resource’s history.</p> </note>

        Args:
            conformance_pack_name: <p>Name of the conformance pack you want to delete.</p>

        Raises:
            capo_config_service.errors.no_such_conformance_pack_exception.NoSuchConformancePackException: <p>You specified one or more conformance packs that do not exist.</p>
            capo_config_service.errors.resource_in_use_exception.ResourceInUseException: <p>You see this exception in the following cases: </p> <ul> <li> <p>For DeleteConfigRule, Config is deleting this rule. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, a remediation action is associated with the rule and Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.</p> </li> <li> <p>For PutConfigOrganizationRule, organization Config rule deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteOrganizationConfigRule, organization Config rule creation is in progress. Try your request again later.</p> </li> <li> <p>For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_conformance_pack_request.DeleteConformancePackRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_conformance_pack

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_conformance_pack.delete_conformance_pack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_conformance_pack_request.DeleteConformancePackRequest = {
            "conformance_pack_name": conformance_pack_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_connector(
        self,
        arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified connector.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the connector that you want to delete.</p>

        Raises:
            capo_config_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>You have specified a resource that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_connector

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_connector.delete_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_connector_request.DeleteConnectorRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_delivery_channel(
        self,
        delivery_channel_name: "capo_config_service.types.channel_name.ChannelName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the delivery channel.</p> <p>Before you can delete the delivery channel, you must stop the customer managed configuration recorder. You can use the <a>StopConfigurationRecorder</a> operation to stop the customer managed configuration recorder.</p>

        Args:
            delivery_channel_name: <p>The name of the delivery channel that you want to delete.</p>

        Raises:
            capo_config_service.errors.last_delivery_channel_delete_failed_exception.LastDeliveryChannelDeleteFailedException: <p>You cannot delete the delivery channel you specified because the customer managed configuration recorder is running.</p>
            capo_config_service.errors.no_such_delivery_channel_exception.NoSuchDeliveryChannelException: <p>You have specified a delivery channel that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_delivery_channel_request.DeleteDeliveryChannelRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_delivery_channel

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_delivery_channel.delete_delivery_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_delivery_channel_request.DeleteDeliveryChannelRequest = {
            "delivery_channel_name": delivery_channel_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_evaluation_results(
        self,
        config_rule_name: "capo_config_service.types.string_with_char_limit64.StringWithCharLimit64",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.delete_evaluation_results_response.DeleteEvaluationResultsResponse":
        """<p>Deletes the evaluation results for the specified Config rule. You can specify one Config rule per request. After you delete the evaluation results, you can call the <a>StartConfigRulesEvaluation</a> API to start evaluating your Amazon Web Services resources against the rule.</p>

        Args:
            config_rule_name: <p>The name of the Config rule for which you want to delete the evaluation results.</p>

        Raises:
            capo_config_service.errors.no_such_config_rule_exception.NoSuchConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.resource_in_use_exception.ResourceInUseException: <p>You see this exception in the following cases: </p> <ul> <li> <p>For DeleteConfigRule, Config is deleting this rule. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, a remediation action is associated with the rule and Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.</p> </li> <li> <p>For PutConfigOrganizationRule, organization Config rule deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteOrganizationConfigRule, organization Config rule creation is in progress. Try your request again later.</p> </li> <li> <p>For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_evaluation_results_request.DeleteEvaluationResultsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.delete_evaluation_results_response.DeleteEvaluationResultsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.delete_evaluation_results

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_evaluation_results.delete_evaluation_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_evaluation_results_request.DeleteEvaluationResultsRequest = {
            "config_rule_name": config_rule_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_organization_config_rule(
        self,
        organization_config_rule_name: "capo_config_service.types.organization_config_rule_name.OrganizationConfigRuleName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified organization Config rule and all of its evaluation results from all member accounts in that organization. </p> <p>Only a management account and a delegated administrator account can delete an organization Config rule. When calling this API with a delegated administrator, you must ensure Organizations <code>ListDelegatedAdministrator</code> permissions are added.</p> <p>Config sets the state of a rule to DELETE_IN_PROGRESS until the deletion is complete. You cannot update a rule while it is in this state.</p> <note> <p> <b>Recommendation: Consider excluding the <code>AWS::Config::ResourceCompliance</code> resource type from recording before deleting rules</b> </p> <p>Deleting rules creates configuration items (CIs) for <code>AWS::Config::ResourceCompliance</code> that can affect your costs for the configuration recorder. If you are deleting rules which evaluate a large number of resource types, this can lead to a spike in the number of CIs recorded.</p> <p>To avoid the associated costs, you can opt to disable recording for the <code>AWS::Config::ResourceCompliance</code> resource type before deleting rules, and re-enable recording after the rules have been deleted.</p> <p>However, since deleting rules is an asynchronous process, it might take an hour or more to complete. During the time when recording is disabled for <code>AWS::Config::ResourceCompliance</code>, rule evaluations will not be recorded in the associated resource’s history.</p> </note>

        Args:
            organization_config_rule_name: <p>The name of organization Config rule that you want to delete.</p>

        Raises:
            capo_config_service.errors.no_such_organization_config_rule_exception.NoSuchOrganizationConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an organization Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.resource_in_use_exception.ResourceInUseException: <p>You see this exception in the following cases: </p> <ul> <li> <p>For DeleteConfigRule, Config is deleting this rule. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, a remediation action is associated with the rule and Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.</p> </li> <li> <p>For PutConfigOrganizationRule, organization Config rule deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteOrganizationConfigRule, organization Config rule creation is in progress. Try your request again later.</p> </li> <li> <p>For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_organization_config_rule_request.DeleteOrganizationConfigRuleRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_organization_config_rule

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_organization_config_rule.delete_organization_config_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_organization_config_rule_request.DeleteOrganizationConfigRuleRequest = {
            "organization_config_rule_name": organization_config_rule_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_organization_conformance_pack(
        self,
        organization_conformance_pack_name: "capo_config_service.types.organization_conformance_pack_name.OrganizationConformancePackName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified organization conformance pack and all of the Config rules and remediation actions from all member accounts in that organization. </p> <p> Only a management account or a delegated administrator account can delete an organization conformance pack. When calling this API with a delegated administrator, you must ensure Organizations <code>ListDelegatedAdministrator</code> permissions are added.</p> <p>Config sets the state of a conformance pack to DELETE_IN_PROGRESS until the deletion is complete. You cannot update a conformance pack while it is in this state. </p> <note> <p> <b>Recommendation: Consider excluding the <code>AWS::Config::ResourceCompliance</code> resource type from recording before deleting rules</b> </p> <p>Deleting rules creates configuration items (CIs) for <code>AWS::Config::ResourceCompliance</code> that can affect your costs for the configuration recorder. If you are deleting rules which evaluate a large number of resource types, this can lead to a spike in the number of CIs recorded.</p> <p>To avoid the associated costs, you can opt to disable recording for the <code>AWS::Config::ResourceCompliance</code> resource type before deleting rules, and re-enable recording after the rules have been deleted.</p> <p>However, since deleting rules is an asynchronous process, it might take an hour or more to complete. During the time when recording is disabled for <code>AWS::Config::ResourceCompliance</code>, rule evaluations will not be recorded in the associated resource’s history.</p> </note>

        Args:
            organization_conformance_pack_name: <p>The name of organization conformance pack that you want to delete.</p>

        Raises:
            capo_config_service.errors.no_such_organization_conformance_pack_exception.NoSuchOrganizationConformancePackException: <p>Config organization conformance pack that you passed in the filter does not exist.</p> <p>For DeleteOrganizationConformancePack, you tried to delete an organization conformance pack that does not exist.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.resource_in_use_exception.ResourceInUseException: <p>You see this exception in the following cases: </p> <ul> <li> <p>For DeleteConfigRule, Config is deleting this rule. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, a remediation action is associated with the rule and Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.</p> </li> <li> <p>For PutConfigOrganizationRule, organization Config rule deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteOrganizationConfigRule, organization Config rule creation is in progress. Try your request again later.</p> </li> <li> <p>For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_organization_conformance_pack_request.DeleteOrganizationConformancePackRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_organization_conformance_pack

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_organization_conformance_pack.delete_organization_conformance_pack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_organization_conformance_pack_request.DeleteOrganizationConformancePackRequest = {
            "organization_conformance_pack_name": organization_conformance_pack_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_pending_aggregation_request(
        self,
        requester_account_id: "capo_config_service.types.account_id.AccountId",
        requester_aws_region: "capo_config_service.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes pending authorization requests for a specified aggregator account in a specified region.</p>

        Args:
            requester_account_id: <p>The 12-digit account ID of the account requesting to aggregate data.</p>
            requester_aws_region: <p>The region requesting to aggregate data.</p>

        Raises:
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_pending_aggregation_request_request.DeletePendingAggregationRequestRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_pending_aggregation_request

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_pending_aggregation_request.delete_pending_aggregation_request(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_pending_aggregation_request_request.DeletePendingAggregationRequestRequest = {
            "requester_account_id": requester_account_id,
            "requester_aws_region": requester_aws_region,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_remediation_configuration(
        self,
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_type: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.delete_remediation_configuration_response.DeleteRemediationConfigurationResponse":
        """<p>Deletes the remediation configuration.</p>

        Args:
            config_rule_name: <p>The name of the Config rule for which you want to delete remediation configuration.</p>
            resource_type: <p>The type of a resource.</p>

        Raises:
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_remediation_configuration_exception.NoSuchRemediationConfigurationException: <p>You specified an Config rule without a remediation configuration.</p>
            capo_config_service.errors.remediation_in_progress_exception.RemediationInProgressException: <p>Remediation action is in progress. You can either cancel execution in Amazon Web Services Systems Manager or wait and try again later. </p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_remediation_configuration_request.DeleteRemediationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.delete_remediation_configuration_response.DeleteRemediationConfigurationResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.delete_remediation_configuration

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_remediation_configuration.delete_remediation_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_remediation_configuration_request.DeleteRemediationConfigurationRequest = {
            "config_rule_name": config_rule_name
        }
        if resource_type is not None:
            input_["resource_type"] = resource_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_remediation_exceptions(
        self,
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        resource_keys: "capo_config_service.types.remediation_exception_resource_keys.RemediationExceptionResourceKeys",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.delete_remediation_exceptions_response.DeleteRemediationExceptionsResponse":
        """<p>Deletes one or more remediation exceptions mentioned in the resource keys.</p> <note> <p>Config generates a remediation exception when a problem occurs executing a remediation action to a specific resource. Remediation exceptions blocks auto-remediation until the exception is cleared.</p> </note>

        Args:
            config_rule_name: <p>The name of the Config rule for which you want to delete remediation exception configuration.</p>
            resource_keys: <p>An exception list of resource exception keys to be processed with the current request. Config adds exception for each resource key. For example, Config adds 3 exceptions for 3 resource keys. </p>

        Raises:
            capo_config_service.errors.no_such_remediation_exception_exception.NoSuchRemediationExceptionException: <p>You tried to delete a remediation exception that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_remediation_exceptions_request.DeleteRemediationExceptionsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.delete_remediation_exceptions_response.DeleteRemediationExceptionsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.delete_remediation_exceptions

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_remediation_exceptions.delete_remediation_exceptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_remediation_exceptions_request.DeleteRemediationExceptionsRequest = {
            "config_rule_name": config_rule_name,
            "resource_keys": resource_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_config(
        self,
        resource_type: "capo_config_service.types.resource_type_string.ResourceTypeString",
        resource_id: "capo_config_service.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Records the configuration state for a custom resource that has been deleted. This API records a new ConfigurationItem with a ResourceDeleted status. You can retrieve the ConfigurationItems recorded for this resource in your Config History. </p>

        Args:
            resource_type: <p>The type of the resource.</p>
            resource_id: <p>Unique identifier of the resource.</p>

        Raises:
            capo_config_service.errors.no_running_configuration_recorder_exception.NoRunningConfigurationRecorderException: <p>There is no configuration recorder running.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_resource_config_request.DeleteResourceConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_resource_config

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_resource_config.delete_resource_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_resource_config_request.DeleteResourceConfigRequest = {
            "resource_type": resource_type,
            "resource_id": resource_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_retention_configuration(
        self,
        retention_configuration_name: "capo_config_service.types.retention_configuration_name.RetentionConfigurationName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the retention configuration.</p>

        Args:
            retention_configuration_name: <p>The name of the retention configuration to delete.</p>

        Raises:
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_retention_configuration_exception.NoSuchRetentionConfigurationException: <p>You have specified a retention configuration that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_retention_configuration_request.DeleteRetentionConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.delete_retention_configuration

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_retention_configuration.delete_retention_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_retention_configuration_request.DeleteRetentionConfigurationRequest = {
            "retention_configuration_name": retention_configuration_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service_linked_configuration_recorder(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        service_principal: Optional[
            "capo_config_service.types.service_principal.ServicePrincipal"
        ] = None,
        arn: Optional[
            "capo_config_service.types.amazon_resource_name.AmazonResourceName"
        ] = None,
    ) -> "capo_config_service.types.delete_service_linked_configuration_recorder_response.DeleteServiceLinkedConfigurationRecorderResponse":
        """<p>Deletes an existing service-linked configuration recorder.</p> <p>This operation does not delete the configuration information that was previously recorded. You will be able to access the previously recorded information by using the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceConfigHistory.html">GetResourceConfigHistory</a> operation, but you will not be able to access this information in the Config console until you have created a new service-linked configuration recorder for the same service.</p> <note> <p> <b>The recording scope determines if you receive configuration items</b> </p> <p>The recording scope is set by the service that is linked to the configuration recorder and determines whether you receive configuration items (CIs) in the delivery channel. If the recording scope is internal, you will not receive CIs in the delivery channel.</p> </note>

        Args:
            service_principal: <p>The service principal of the Amazon Web Services service for the service-linked configuration recorder that you want to delete. This field is only supported for Amazon Web Services service principals. For third-party service-linked configuration recorders, use <code>Arn</code> instead.</p>
            arn: <p>The Amazon Resource Name (ARN) of the service-linked configuration recorder that you want to delete. For third-party service-linked configuration recorders, you must use <code>Arn</code>. You must specify exactly one of <code>Arn</code> or <code>ServicePrincipal</code>.</p>

        Raises:
            capo_config_service.errors.conflict_exception.ConflictException: <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because a service-linked recorder already exists for the specified service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because the specified service principal does not support multiple configuration recorders and one already exists.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector or service principal. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, you cannot create a connector because a connector already exists for the specified connector configuration.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, you cannot delete the service-linked recorder because it is currently in use by the linked Amazon Web Services service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConnector.html">DeleteConnector</a>, another in-progress operation is currently referencing the connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteDeliveryChannel.html">DeleteDeliveryChannel</a>, you cannot delete the specified delivery channel because the customer managed configuration recorder is running. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html">StopConfigurationRecorder</a> operation to stop the customer managed configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>For service-linked configuration recorders, the configuration recorder is not in use by the service. No association or dissociation of resource types is permitted.</p> </li> <li> <p>For service-linked configuration recorders, your requested change to the configuration recorder has been denied by its linked Amazon Web Services service.</p> </li> </ul>
            capo_config_service.errors.no_such_configuration_recorder_exception.NoSuchConfigurationRecorderException: <p>You have specified a configuration recorder that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_service_linked_configuration_recorder_request.DeleteServiceLinkedConfigurationRecorderRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.delete_service_linked_configuration_recorder_response.DeleteServiceLinkedConfigurationRecorderResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.delete_service_linked_configuration_recorder

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_service_linked_configuration_recorder.delete_service_linked_configuration_recorder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_service_linked_configuration_recorder_request.DeleteServiceLinkedConfigurationRecorderRequest = {}
        if service_principal is not None:
            input_["service_principal"] = service_principal
        if arn is not None:
            input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_stored_query(
        self,
        query_name: "capo_config_service.types.query_name.QueryName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.delete_stored_query_response.DeleteStoredQueryResponse":
        """<p>Deletes the stored query for a single Amazon Web Services account and a single Amazon Web Services Region.</p>

        Args:
            query_name: <p>The name of the query that you want to delete.</p>

        Raises:
            capo_config_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>You have specified a resource that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.delete_stored_query_request.DeleteStoredQueryRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.delete_stored_query_response.DeleteStoredQueryResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.delete_stored_query

            output, http_response = (
                capo_config_service._operations.starling_dove_service.delete_stored_query.delete_stored_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.delete_stored_query_request.DeleteStoredQueryRequest = {
            "query_name": query_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deliver_config_snapshot(
        self,
        delivery_channel_name: "capo_config_service.types.channel_name.ChannelName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.deliver_config_snapshot_response.DeliverConfigSnapshotResponse":
        """<p>Schedules delivery of a configuration snapshot to the Amazon S3 bucket in the specified delivery channel. After the delivery has started, Config sends the following notifications using an Amazon SNS topic that you have specified.</p> <ul> <li> <p>Notification of the start of the delivery.</p> </li> <li> <p>Notification of the completion of the delivery, if the delivery was successfully completed.</p> </li> <li> <p>Notification of delivery failure, if the delivery failed.</p> </li> </ul>

        Args:
            delivery_channel_name: <p>The name of the delivery channel through which the snapshot is delivered.</p>

        Raises:
            capo_config_service.errors.no_available_configuration_recorder_exception.NoAvailableConfigurationRecorderException: <p>There are no customer managed configuration recorders available to record your resources. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html">PutConfigurationRecorder</a> operation to create the customer managed configuration recorder.</p>
            capo_config_service.errors.no_running_configuration_recorder_exception.NoRunningConfigurationRecorderException: <p>There is no configuration recorder running.</p>
            capo_config_service.errors.no_such_delivery_channel_exception.NoSuchDeliveryChannelException: <p>You have specified a delivery channel that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.deliver_config_snapshot_request.DeliverConfigSnapshotRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.deliver_config_snapshot_response.DeliverConfigSnapshotResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.deliver_config_snapshot

            output, http_response = (
                capo_config_service._operations.starling_dove_service.deliver_config_snapshot.deliver_config_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.deliver_config_snapshot_request.DeliverConfigSnapshotRequest = {
            "delivery_channel_name": delivery_channel_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_aggregate_compliance_by_config_rules(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.config_rule_compliance_filters.ConfigRuleComplianceFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.group_by_api_limit.GroupByAPILimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.describe_aggregate_compliance_by_config_rules_response.DescribeAggregateComplianceByConfigRulesResponse":
        """<p>Returns a list of compliant and noncompliant rules with the number of resources for compliant and noncompliant rules. Does not display rules that do not have compliance results. </p> <note> <p>The results can return an empty result page, but if you have a <code>nextToken</code>, the results are displayed on the next page.</p> </note>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>
            filters: <p>Filters the results by ConfigRuleComplianceFilters object. </p>
            limit: <p>The maximum number of evaluation results returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_aggregate_compliance_by_config_rules_request.DescribeAggregateComplianceByConfigRulesRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_aggregate_compliance_by_config_rules_response.DescribeAggregateComplianceByConfigRulesResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_aggregate_compliance_by_config_rules

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_aggregate_compliance_by_config_rules.describe_aggregate_compliance_by_config_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_aggregate_compliance_by_config_rules_request.DescribeAggregateComplianceByConfigRulesRequest = {
            "configuration_aggregator_name": configuration_aggregator_name
        }
        if filters is not None:
            input_["filters"] = filters
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_aggregate_compliance_by_config_rules(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.config_rule_compliance_filters.ConfigRuleComplianceFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.group_by_api_limit.GroupByAPILimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.describe_aggregate_compliance_by_config_rules_response.DescribeAggregateComplianceByConfigRulesResponse]":
        _token = next_token
        while True:
            _response = self.describe_aggregate_compliance_by_config_rules(
                configuration_aggregator_name,
                config_overrides=config_overrides,
                filters=filters,
                limit=limit,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_aggregate_compliance_by_conformance_packs(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.aggregate_conformance_pack_compliance_filters.AggregateConformancePackComplianceFilters"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.describe_aggregate_compliance_by_conformance_packs_response.DescribeAggregateComplianceByConformancePacksResponse":
        """<p>Returns a list of the existing and deleted conformance packs and their associated compliance status with the count of compliant and noncompliant Config rules within each conformance pack. Also returns the total rule count which includes compliant rules, noncompliant rules, and rules that cannot be evaluated due to insufficient data.</p> <note> <p>The results can return an empty result page, but if you have a <code>nextToken</code>, the results are displayed on the next page.</p> </note>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>
            filters: <p>Filters the result by <code>AggregateConformancePackComplianceFilters</code> object.</p>
            limit: <p>The maximum number of conformance packs compliance details returned on each page. The default is maximum. If you specify 0, Config uses the default. </p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_aggregate_compliance_by_conformance_packs_request.DescribeAggregateComplianceByConformancePacksRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_aggregate_compliance_by_conformance_packs_response.DescribeAggregateComplianceByConformancePacksResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_aggregate_compliance_by_conformance_packs

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_aggregate_compliance_by_conformance_packs.describe_aggregate_compliance_by_conformance_packs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_aggregate_compliance_by_conformance_packs_request.DescribeAggregateComplianceByConformancePacksRequest = {
            "configuration_aggregator_name": configuration_aggregator_name
        }
        if filters is not None:
            input_["filters"] = filters
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_aggregate_compliance_by_conformance_packs(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.aggregate_conformance_pack_compliance_filters.AggregateConformancePackComplianceFilters"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.aggregate_compliance_by_conformance_pack.AggregateComplianceByConformancePack]":
        _token = next_token
        while True:
            _response = self.describe_aggregate_compliance_by_conformance_packs(
                configuration_aggregator_name,
                config_overrides=config_overrides,
                filters=filters,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("aggregate_compliance_by_conformance_packs",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_aggregation_authorizations(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.describe_aggregation_authorizations_response.DescribeAggregationAuthorizationsResponse":
        """<p>Returns a list of authorizations granted to various aggregator accounts and regions.</p>

        Args:
            limit: <p>The maximum number of AggregationAuthorizations returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_aggregation_authorizations_request.DescribeAggregationAuthorizationsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_aggregation_authorizations_response.DescribeAggregationAuthorizationsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_aggregation_authorizations

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_aggregation_authorizations.describe_aggregation_authorizations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_aggregation_authorizations_request.DescribeAggregationAuthorizationsRequest = {}
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_aggregation_authorizations(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.aggregation_authorization.AggregationAuthorization]":
        _token = next_token
        while True:
            _response = self.describe_aggregation_authorizations(
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("aggregation_authorizations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_compliance_by_config_rule(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        config_rule_names: Optional[
            "capo_config_service.types.config_rule_names.ConfigRuleNames"
        ] = None,
        compliance_types: Optional[
            "capo_config_service.types.compliance_types.ComplianceTypes"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.describe_compliance_by_config_rule_response.DescribeComplianceByConfigRuleResponse":
        """<p>Indicates whether the specified Config rules are compliant. If a rule is noncompliant, this operation returns the number of Amazon Web Services resources that do not comply with the rule.</p> <p>A rule is compliant if all of the evaluated resources comply with it. It is noncompliant if any of these resources do not comply.</p> <p>If Config has no current evaluation results for the rule, it returns <code>INSUFFICIENT_DATA</code>. This result might indicate one of the following conditions:</p> <ul> <li> <p>Config has never invoked an evaluation for the rule. To check whether it has, use the <code>DescribeConfigRuleEvaluationStatus</code> action to get the <code>LastSuccessfulInvocationTime</code> and <code>LastFailedInvocationTime</code>.</p> </li> <li> <p>The rule's Lambda function is failing to send evaluation results to Config. Verify that the role you assigned to your configuration recorder includes the <code>config:PutEvaluations</code> permission. If the rule is a custom rule, verify that the Lambda execution role includes the <code>config:PutEvaluations</code> permission.</p> </li> <li> <p>The rule's Lambda function has returned <code>NOT_APPLICABLE</code> for all evaluation results. This can occur if the resources were deleted or removed from the rule's scope.</p> </li> </ul>

        Args:
            config_rule_names: <p>Specify one or more Config rule names to filter the results by rule.</p>
            compliance_types: <p>Filters the results by compliance.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_config_rule_exception.NoSuchConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_compliance_by_config_rule_request.DescribeComplianceByConfigRuleRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_compliance_by_config_rule_response.DescribeComplianceByConfigRuleResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_compliance_by_config_rule

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_compliance_by_config_rule.describe_compliance_by_config_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_compliance_by_config_rule_request.DescribeComplianceByConfigRuleRequest = {}
        if config_rule_names is not None:
            input_["config_rule_names"] = config_rule_names
        if compliance_types is not None:
            input_["compliance_types"] = compliance_types
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_compliance_by_config_rule(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        config_rule_names: Optional[
            "capo_config_service.types.config_rule_names.ConfigRuleNames"
        ] = None,
        compliance_types: Optional[
            "capo_config_service.types.compliance_types.ComplianceTypes"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.compliance_by_config_rule.ComplianceByConfigRule]":
        _token = next_token
        while True:
            _response = self.describe_compliance_by_config_rule(
                config_overrides=config_overrides,
                config_rule_names=config_rule_names,
                compliance_types=compliance_types,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("compliance_by_config_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_compliance_by_resource(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_type: Optional[
            "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
        ] = None,
        resource_id: Optional[
            "capo_config_service.types.base_resource_id.BaseResourceId"
        ] = None,
        compliance_types: Optional[
            "capo_config_service.types.compliance_types.ComplianceTypes"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.describe_compliance_by_resource_response.DescribeComplianceByResourceResponse":
        """<p>Indicates whether the specified Amazon Web Services resources are compliant. If a resource is noncompliant, this operation returns the number of Config rules that the resource does not comply with.</p> <p>A resource is compliant if it complies with all the Config rules that evaluate it. It is noncompliant if it does not comply with one or more of these rules.</p> <p>If Config has no current evaluation results for the resource, it returns <code>INSUFFICIENT_DATA</code>. This result might indicate one of the following conditions about the rules that evaluate the resource:</p> <ul> <li> <p>Config has never invoked an evaluation for the rule. To check whether it has, use the <code>DescribeConfigRuleEvaluationStatus</code> action to get the <code>LastSuccessfulInvocationTime</code> and <code>LastFailedInvocationTime</code>.</p> </li> <li> <p>The rule's Lambda function is failing to send evaluation results to Config. Verify that the role that you assigned to your configuration recorder includes the <code>config:PutEvaluations</code> permission. If the rule is a custom rule, verify that the Lambda execution role includes the <code>config:PutEvaluations</code> permission.</p> </li> <li> <p>The rule's Lambda function has returned <code>NOT_APPLICABLE</code> for all evaluation results. This can occur if the resources were deleted or removed from the rule's scope.</p> </li> </ul>

        Args:
            resource_type: <p>The types of Amazon Web Services resources for which you want compliance information (for example, <code>AWS::EC2::Instance</code>). For this operation, you can specify that the resource type is an Amazon Web Services account by specifying <code>AWS::::Account</code>.</p>
            resource_id: <p>The ID of the Amazon Web Services resource for which you want compliance information. You can specify only one resource ID. If you specify a resource ID, you must also specify a type for <code>ResourceType</code>.</p>
            compliance_types: <p>Filters the results by compliance.</p>
            limit: <p>The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_compliance_by_resource_request.DescribeComplianceByResourceRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_compliance_by_resource_response.DescribeComplianceByResourceResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_compliance_by_resource

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_compliance_by_resource.describe_compliance_by_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_compliance_by_resource_request.DescribeComplianceByResourceRequest = {}
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if compliance_types is not None:
            input_["compliance_types"] = compliance_types
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_compliance_by_resource(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_type: Optional[
            "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
        ] = None,
        resource_id: Optional[
            "capo_config_service.types.base_resource_id.BaseResourceId"
        ] = None,
        compliance_types: Optional[
            "capo_config_service.types.compliance_types.ComplianceTypes"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.compliance_by_resource.ComplianceByResource]":
        _token = next_token
        while True:
            _response = self.describe_compliance_by_resource(
                config_overrides=config_overrides,
                resource_type=resource_type,
                resource_id=resource_id,
                compliance_types=compliance_types,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("compliance_by_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_config_rule_evaluation_status(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        config_rule_names: Optional[
            "capo_config_service.types.config_rule_names.ConfigRuleNames"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        limit: Optional["capo_config_service.types.rule_limit.RuleLimit"] = None,
    ) -> "capo_config_service.types.describe_config_rule_evaluation_status_response.DescribeConfigRuleEvaluationStatusResponse":
        """<p>Returns status information for each of your Config managed rules. The status includes information such as the last time Config invoked the rule, the last time Config failed to invoke the rule, and the related error for the last failure.</p>

        Args:
            config_rule_names: <p>The name of the Config managed rules for which you want status information. If you do not specify any names, Config returns status information for all Config managed rules that you use.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>
            limit: <p>The number of rule evaluation results that you want returned.</p> <p>This parameter is required if the rule limit for your account is more than the default of 1000 rules.</p> <p>For information about requesting a rule limit increase, see <a href="http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_config">Config Limits</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>

        Raises:
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_config_rule_exception.NoSuchConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_config_rule_evaluation_status_request.DescribeConfigRuleEvaluationStatusRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_config_rule_evaluation_status_response.DescribeConfigRuleEvaluationStatusResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_config_rule_evaluation_status

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_config_rule_evaluation_status.describe_config_rule_evaluation_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_config_rule_evaluation_status_request.DescribeConfigRuleEvaluationStatusRequest = {}
        if config_rule_names is not None:
            input_["config_rule_names"] = config_rule_names
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_config_rule_evaluation_status(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        config_rule_names: Optional[
            "capo_config_service.types.config_rule_names.ConfigRuleNames"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        limit: Optional["capo_config_service.types.rule_limit.RuleLimit"] = None,
    ) -> "Iterator[capo_config_service.types.config_rule_evaluation_status.ConfigRuleEvaluationStatus]":
        _token = next_token
        while True:
            _response = self.describe_config_rule_evaluation_status(
                config_overrides=config_overrides,
                config_rule_names=config_rule_names,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("config_rules_evaluation_status",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_config_rules(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        config_rule_names: Optional[
            "capo_config_service.types.config_rule_names.ConfigRuleNames"
        ] = None,
        filters: Optional[
            "capo_config_service.types.describe_config_rules_filters.DescribeConfigRulesFilters"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.describe_config_rules_response.DescribeConfigRulesResponse":
        """<p>Returns details about your Config rules.</p>

        Args:
            config_rule_names: <p>The names of the Config rules for which you want details. If you do not specify any names, Config returns details for all your rules.</p>
            filters: <p>Returns a list of Detective or Proactive Config rules. By default, this API returns an unfiltered list. For more information on Detective or Proactive Config rules, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html"> <b>Evaluation Mode</b> </a> in the <i>Config Developer Guide</i>.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_config_rule_exception.NoSuchConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_config_rules_request.DescribeConfigRulesRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_config_rules_response.DescribeConfigRulesResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_config_rules

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_config_rules.describe_config_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_config_rules_request.DescribeConfigRulesRequest = {}
        if config_rule_names is not None:
            input_["config_rule_names"] = config_rule_names
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_config_rules(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        config_rule_names: Optional[
            "capo_config_service.types.config_rule_names.ConfigRuleNames"
        ] = None,
        filters: Optional[
            "capo_config_service.types.describe_config_rules_filters.DescribeConfigRulesFilters"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.config_rule.ConfigRule]":
        _token = next_token
        while True:
            _response = self.describe_config_rules(
                config_overrides=config_overrides,
                config_rule_names=config_rule_names,
                filters=filters,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("config_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_configuration_aggregators(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        configuration_aggregator_names: Optional[
            "capo_config_service.types.configuration_aggregator_name_list.ConfigurationAggregatorNameList"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
    ) -> "capo_config_service.types.describe_configuration_aggregators_response.DescribeConfigurationAggregatorsResponse":
        """<p>Returns the details of one or more configuration aggregators. If the configuration aggregator is not specified, this operation returns the details for all the configuration aggregators associated with the account. </p>

        Args:
            configuration_aggregator_names: <p>The name of the configuration aggregators.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>
            limit: <p>The maximum number of configuration aggregators returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_configuration_aggregators_request.DescribeConfigurationAggregatorsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_configuration_aggregators_response.DescribeConfigurationAggregatorsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_configuration_aggregators

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_configuration_aggregators.describe_configuration_aggregators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_configuration_aggregators_request.DescribeConfigurationAggregatorsRequest = {}
        if configuration_aggregator_names is not None:
            input_["configuration_aggregator_names"] = configuration_aggregator_names
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_configuration_aggregators(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        configuration_aggregator_names: Optional[
            "capo_config_service.types.configuration_aggregator_name_list.ConfigurationAggregatorNameList"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
    ) -> "Iterator[capo_config_service.types.configuration_aggregator.ConfigurationAggregator]":
        _token = next_token
        while True:
            _response = self.describe_configuration_aggregators(
                config_overrides=config_overrides,
                configuration_aggregator_names=configuration_aggregator_names,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("configuration_aggregators",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_configuration_aggregator_sources_status(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        update_status: Optional[
            "capo_config_service.types.aggregated_source_status_type_list.AggregatedSourceStatusTypeList"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
    ) -> "capo_config_service.types.describe_configuration_aggregator_sources_status_response.DescribeConfigurationAggregatorSourcesStatusResponse":
        """<p>Returns status information for sources within an aggregator. The status includes information about the last time Config verified authorization between the source account and an aggregator account. In case of a failure, the status contains the related error code or message. </p>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>
            update_status: <p>Filters the status type.</p> <ul> <li> <p>Valid value FAILED indicates errors while moving data.</p> </li> <li> <p>Valid value SUCCEEDED indicates the data was successfully moved.</p> </li> <li> <p>Valid value OUTDATED indicates the data is not the most recent.</p> </li> </ul>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>
            limit: <p>The maximum number of AggregatorSourceStatus returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_configuration_aggregator_sources_status_request.DescribeConfigurationAggregatorSourcesStatusRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_configuration_aggregator_sources_status_response.DescribeConfigurationAggregatorSourcesStatusResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_configuration_aggregator_sources_status

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_configuration_aggregator_sources_status.describe_configuration_aggregator_sources_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_configuration_aggregator_sources_status_request.DescribeConfigurationAggregatorSourcesStatusRequest = {
            "configuration_aggregator_name": configuration_aggregator_name
        }
        if update_status is not None:
            input_["update_status"] = update_status
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_configuration_aggregator_sources_status(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        update_status: Optional[
            "capo_config_service.types.aggregated_source_status_type_list.AggregatedSourceStatusTypeList"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
    ) -> "Iterator[capo_config_service.types.aggregated_source_status.AggregatedSourceStatus]":
        _token = next_token
        while True:
            _response = self.describe_configuration_aggregator_sources_status(
                configuration_aggregator_name,
                config_overrides=config_overrides,
                update_status=update_status,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("aggregated_source_status_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_configuration_recorders(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        configuration_recorder_names: Optional[
            "capo_config_service.types.configuration_recorder_name_list.ConfigurationRecorderNameList"
        ] = None,
        service_principal: Optional[
            "capo_config_service.types.service_principal.ServicePrincipal"
        ] = None,
        arn: Optional[
            "capo_config_service.types.amazon_resource_name.AmazonResourceName"
        ] = None,
    ) -> "capo_config_service.types.describe_configuration_recorders_response.DescribeConfigurationRecordersResponse":
        """<p>Returns details for the configuration recorder you specify.</p> <p>If a configuration recorder is not specified, this operation returns details for the customer managed configuration recorder configured for the account, if applicable.</p> <note> <p>When making a request to this operation, you can only specify one configuration recorder.</p> </note>

        Args:
            configuration_recorder_names: <p>A list of names of the configuration recorders that you want to specify.</p> <note> <p>When making a request to this operation, you can only specify one configuration recorder.</p> </note>
            service_principal: <p>For service-linked configuration recorders, you can use the service principal of the linked Amazon Web Services service to specify the configuration recorder. This field is only supported for Amazon Web Services service principals. For third-party service-linked configuration recorders, use <code>Arn</code> instead.</p>
            arn: <p>The Amazon Resource Name (ARN) of the configuration recorder that you want to specify.</p>

        Raises:
            capo_config_service.errors.no_such_configuration_recorder_exception.NoSuchConfigurationRecorderException: <p>You have specified a configuration recorder that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_configuration_recorders_request.DescribeConfigurationRecordersRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_configuration_recorders_response.DescribeConfigurationRecordersResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_configuration_recorders

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_configuration_recorders.describe_configuration_recorders(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_configuration_recorders_request.DescribeConfigurationRecordersRequest = {}
        if configuration_recorder_names is not None:
            input_["configuration_recorder_names"] = configuration_recorder_names
        if service_principal is not None:
            input_["service_principal"] = service_principal
        if arn is not None:
            input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_configuration_recorder_status(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        configuration_recorder_names: Optional[
            "capo_config_service.types.configuration_recorder_name_list.ConfigurationRecorderNameList"
        ] = None,
        service_principal: Optional[
            "capo_config_service.types.service_principal.ServicePrincipal"
        ] = None,
        arn: Optional[
            "capo_config_service.types.amazon_resource_name.AmazonResourceName"
        ] = None,
    ) -> "capo_config_service.types.describe_configuration_recorder_status_response.DescribeConfigurationRecorderStatusResponse":
        """<p>Returns the current status of the configuration recorder you specify as well as the status of the last recording event for the configuration recorders.</p> <p>For a detailed status of recording events over time, add your Config events to Amazon CloudWatch metrics and use CloudWatch metrics.</p> <p>If a configuration recorder is not specified, this operation returns the status for the customer managed configuration recorder configured for the account, if applicable.</p> <note> <p>When making a request to this operation, you can only specify one configuration recorder.</p> </note>

        Args:
            configuration_recorder_names: <p>The name of the configuration recorder. If the name is not specified, the operation returns the status for the customer managed configuration recorder configured for the account, if applicable.</p> <note> <p>When making a request to this operation, you can only specify one configuration recorder.</p> </note>
            service_principal: <p>For service-linked configuration recorders, you can use the service principal of the linked Amazon Web Services service to specify the configuration recorder. This field is only supported for Amazon Web Services service principals. For third-party service-linked configuration recorders, use <code>Arn</code> instead.</p>
            arn: <p>The Amazon Resource Name (ARN) of the configuration recorder that you want to specify.</p>

        Raises:
            capo_config_service.errors.no_such_configuration_recorder_exception.NoSuchConfigurationRecorderException: <p>You have specified a configuration recorder that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_configuration_recorder_status_request.DescribeConfigurationRecorderStatusRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_configuration_recorder_status_response.DescribeConfigurationRecorderStatusResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_configuration_recorder_status

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_configuration_recorder_status.describe_configuration_recorder_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_configuration_recorder_status_request.DescribeConfigurationRecorderStatusRequest = {}
        if configuration_recorder_names is not None:
            input_["configuration_recorder_names"] = configuration_recorder_names
        if service_principal is not None:
            input_["service_principal"] = service_principal
        if arn is not None:
            input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_conformance_pack_compliance(
        self,
        conformance_pack_name: "capo_config_service.types.conformance_pack_name.ConformancePackName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.conformance_pack_compliance_filters.ConformancePackComplianceFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.describe_conformance_pack_compliance_limit.DescribeConformancePackComplianceLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.describe_conformance_pack_compliance_response.DescribeConformancePackComplianceResponse":
        """<p>Returns compliance details for each rule in that conformance pack.</p> <note> <p>You must provide exact rule names.</p> </note>

        Args:
            conformance_pack_name: <p>Name of the conformance pack.</p>
            filters: <p>A <code>ConformancePackComplianceFilters</code> object.</p>
            limit: <p>The maximum number of Config rules within a conformance pack are returned on each page.</p>
            next_token: <p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_config_rule_in_conformance_pack_exception.NoSuchConfigRuleInConformancePackException: <p>Config rule that you passed in the filter does not exist.</p>
            capo_config_service.errors.no_such_conformance_pack_exception.NoSuchConformancePackException: <p>You specified one or more conformance packs that do not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_conformance_pack_compliance_request.DescribeConformancePackComplianceRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_conformance_pack_compliance_response.DescribeConformancePackComplianceResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_conformance_pack_compliance

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_conformance_pack_compliance.describe_conformance_pack_compliance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_conformance_pack_compliance_request.DescribeConformancePackComplianceRequest = {
            "conformance_pack_name": conformance_pack_name
        }
        if filters is not None:
            input_["filters"] = filters
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_conformance_pack_compliance(
        self,
        conformance_pack_name: "capo_config_service.types.conformance_pack_name.ConformancePackName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.conformance_pack_compliance_filters.ConformancePackComplianceFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.describe_conformance_pack_compliance_limit.DescribeConformancePackComplianceLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.conformance_pack_rule_compliance.ConformancePackRuleCompliance]":
        _token = next_token
        while True:
            _response = self.describe_conformance_pack_compliance(
                conformance_pack_name,
                config_overrides=config_overrides,
                filters=filters,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("conformance_pack_rule_compliance_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_conformance_packs(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        conformance_pack_names: Optional[
            "capo_config_service.types.conformance_pack_names_list.ConformancePackNamesList"
        ] = None,
        limit: Optional[
            "capo_config_service.types.page_size_limit.PageSizeLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.describe_conformance_packs_response.DescribeConformancePacksResponse":
        """<p>Returns a list of one or more conformance packs.</p>

        Args:
            conformance_pack_names: <p>Comma-separated list of conformance pack names for which you want details. If you do not specify any names, Config returns details for all your conformance packs. </p>
            limit: <p>The maximum number of conformance packs returned on each page.</p>
            next_token: <p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_conformance_pack_exception.NoSuchConformancePackException: <p>You specified one or more conformance packs that do not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_conformance_packs_request.DescribeConformancePacksRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_conformance_packs_response.DescribeConformancePacksResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_conformance_packs

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_conformance_packs.describe_conformance_packs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_conformance_packs_request.DescribeConformancePacksRequest = {}
        if conformance_pack_names is not None:
            input_["conformance_pack_names"] = conformance_pack_names
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_conformance_packs(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        conformance_pack_names: Optional[
            "capo_config_service.types.conformance_pack_names_list.ConformancePackNamesList"
        ] = None,
        limit: Optional[
            "capo_config_service.types.page_size_limit.PageSizeLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.conformance_pack_detail.ConformancePackDetail]":
        _token = next_token
        while True:
            _response = self.describe_conformance_packs(
                config_overrides=config_overrides,
                conformance_pack_names=conformance_pack_names,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("conformance_pack_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_conformance_pack_status(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        conformance_pack_names: Optional[
            "capo_config_service.types.conformance_pack_names_list.ConformancePackNamesList"
        ] = None,
        limit: Optional[
            "capo_config_service.types.page_size_limit.PageSizeLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.describe_conformance_pack_status_response.DescribeConformancePackStatusResponse":
        """<p>Provides one or more conformance packs deployment status.</p> <note> <p>If there are no conformance packs then you will see an empty result.</p> </note>

        Args:
            conformance_pack_names: <p>Comma-separated list of conformance pack names.</p>
            limit: <p>The maximum number of conformance packs status returned on each page.</p>
            next_token: <p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_conformance_pack_status_request.DescribeConformancePackStatusRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_conformance_pack_status_response.DescribeConformancePackStatusResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_conformance_pack_status

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_conformance_pack_status.describe_conformance_pack_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_conformance_pack_status_request.DescribeConformancePackStatusRequest = {}
        if conformance_pack_names is not None:
            input_["conformance_pack_names"] = conformance_pack_names
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_conformance_pack_status(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        conformance_pack_names: Optional[
            "capo_config_service.types.conformance_pack_names_list.ConformancePackNamesList"
        ] = None,
        limit: Optional[
            "capo_config_service.types.page_size_limit.PageSizeLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.conformance_pack_status_detail.ConformancePackStatusDetail]":
        _token = next_token
        while True:
            _response = self.describe_conformance_pack_status(
                config_overrides=config_overrides,
                conformance_pack_names=conformance_pack_names,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("conformance_pack_status_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_delivery_channels(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        delivery_channel_names: Optional[
            "capo_config_service.types.delivery_channel_name_list.DeliveryChannelNameList"
        ] = None,
    ) -> "capo_config_service.types.describe_delivery_channels_response.DescribeDeliveryChannelsResponse":
        """<p>Returns details about the specified delivery channel. If a delivery channel is not specified, this operation returns the details of all delivery channels associated with the account.</p> <note> <p>Currently, you can specify only one delivery channel per region in your account.</p> </note>

        Args:
            delivery_channel_names: <p>A list of delivery channel names.</p>

        Raises:
            capo_config_service.errors.no_such_delivery_channel_exception.NoSuchDeliveryChannelException: <p>You have specified a delivery channel that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_delivery_channels_request.DescribeDeliveryChannelsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_delivery_channels_response.DescribeDeliveryChannelsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_delivery_channels

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_delivery_channels.describe_delivery_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_delivery_channels_request.DescribeDeliveryChannelsRequest = {}
        if delivery_channel_names is not None:
            input_["delivery_channel_names"] = delivery_channel_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_delivery_channel_status(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        delivery_channel_names: Optional[
            "capo_config_service.types.delivery_channel_name_list.DeliveryChannelNameList"
        ] = None,
    ) -> "capo_config_service.types.describe_delivery_channel_status_response.DescribeDeliveryChannelStatusResponse":
        """<p>Returns the current status of the specified delivery channel. If a delivery channel is not specified, this operation returns the current status of all delivery channels associated with the account.</p> <note> <p>Currently, you can specify only one delivery channel per region in your account.</p> </note>

        Args:
            delivery_channel_names: <p>A list of delivery channel names.</p>

        Raises:
            capo_config_service.errors.no_such_delivery_channel_exception.NoSuchDeliveryChannelException: <p>You have specified a delivery channel that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_delivery_channel_status_request.DescribeDeliveryChannelStatusRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_delivery_channel_status_response.DescribeDeliveryChannelStatusResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_delivery_channel_status

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_delivery_channel_status.describe_delivery_channel_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_delivery_channel_status_request.DescribeDeliveryChannelStatusRequest = {}
        if delivery_channel_names is not None:
            input_["delivery_channel_names"] = delivery_channel_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_organization_config_rules(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        organization_config_rule_names: Optional[
            "capo_config_service.types.organization_config_rule_names.OrganizationConfigRuleNames"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.describe_organization_config_rules_response.DescribeOrganizationConfigRulesResponse":
        """<p>Returns a list of organization Config rules. </p> <note> <p>When you specify the limit and the next token, you receive a paginated response.</p> <p>Limit and next token are not applicable if you specify organization Config rule names. It is only applicable, when you request all the organization Config rules.</p> <p> <i>For accounts within an organization</i> </p> <p>If you deploy an organizational rule or conformance pack in an organization administrator account, and then establish a delegated administrator and deploy an organizational rule or conformance pack in the delegated administrator account, you won't be able to see the organizational rule or conformance pack in the organization administrator account from the delegated administrator account or see the organizational rule or conformance pack in the delegated administrator account from organization administrator account. The <code>DescribeOrganizationConfigRules</code> and <code>DescribeOrganizationConformancePacks</code> APIs can only see and interact with the organization-related resource that were deployed from within the account calling those APIs.</p> </note>

        Args:
            organization_config_rule_names: <p>The names of organization Config rules for which you want details. If you do not specify any names, Config returns details for all your organization Config rules.</p>
            limit: <p>The maximum number of organization Config rules returned on each page. If you do no specify a number, Config uses the default. The default is 100.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_organization_config_rule_exception.NoSuchOrganizationConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an organization Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_organization_config_rules_request.DescribeOrganizationConfigRulesRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_organization_config_rules_response.DescribeOrganizationConfigRulesResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_organization_config_rules

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_organization_config_rules.describe_organization_config_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_organization_config_rules_request.DescribeOrganizationConfigRulesRequest = {}
        if organization_config_rule_names is not None:
            input_["organization_config_rule_names"] = organization_config_rule_names
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_organization_config_rules(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        organization_config_rule_names: Optional[
            "capo_config_service.types.organization_config_rule_names.OrganizationConfigRuleNames"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.organization_config_rule.OrganizationConfigRule]":
        _token = next_token
        while True:
            _response = self.describe_organization_config_rules(
                config_overrides=config_overrides,
                organization_config_rule_names=organization_config_rule_names,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("organization_config_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_organization_config_rule_statuses(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        organization_config_rule_names: Optional[
            "capo_config_service.types.organization_config_rule_names.OrganizationConfigRuleNames"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.describe_organization_config_rule_statuses_response.DescribeOrganizationConfigRuleStatusesResponse":
        """<p>Provides organization Config rule deployment status for an organization.</p> <note> <p>The status is not considered successful until organization Config rule is successfully deployed in all the member accounts with an exception of excluded accounts.</p> <p>When you specify the limit and the next token, you receive a paginated response. Limit and next token are not applicable if you specify organization Config rule names. It is only applicable, when you request all the organization Config rules.</p> </note>

        Args:
            organization_config_rule_names: <p>The names of organization Config rules for which you want status details. If you do not specify any names, Config returns details for all your organization Config rules.</p>
            limit: <p>The maximum number of <code>OrganizationConfigRuleStatuses</code> returned on each page. If you do no specify a number, Config uses the default. The default is 100.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_organization_config_rule_exception.NoSuchOrganizationConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an organization Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_organization_config_rule_statuses_request.DescribeOrganizationConfigRuleStatusesRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_organization_config_rule_statuses_response.DescribeOrganizationConfigRuleStatusesResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_organization_config_rule_statuses

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_organization_config_rule_statuses.describe_organization_config_rule_statuses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_organization_config_rule_statuses_request.DescribeOrganizationConfigRuleStatusesRequest = {}
        if organization_config_rule_names is not None:
            input_["organization_config_rule_names"] = organization_config_rule_names
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_organization_config_rule_statuses(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        organization_config_rule_names: Optional[
            "capo_config_service.types.organization_config_rule_names.OrganizationConfigRuleNames"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.organization_config_rule_status.OrganizationConfigRuleStatus]":
        _token = next_token
        while True:
            _response = self.describe_organization_config_rule_statuses(
                config_overrides=config_overrides,
                organization_config_rule_names=organization_config_rule_names,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("organization_config_rule_statuses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_organization_conformance_packs(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        organization_conformance_pack_names: Optional[
            "capo_config_service.types.organization_conformance_pack_names.OrganizationConformancePackNames"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.describe_organization_conformance_packs_response.DescribeOrganizationConformancePacksResponse":
        """<p>Returns a list of organization conformance packs. </p> <note> <p>When you specify the limit and the next token, you receive a paginated response. </p> <p>Limit and next token are not applicable if you specify organization conformance packs names. They are only applicable, when you request all the organization conformance packs. </p> <p> <i>For accounts within an organization</i> </p> <p>If you deploy an organizational rule or conformance pack in an organization administrator account, and then establish a delegated administrator and deploy an organizational rule or conformance pack in the delegated administrator account, you won't be able to see the organizational rule or conformance pack in the organization administrator account from the delegated administrator account or see the organizational rule or conformance pack in the delegated administrator account from organization administrator account. The <code>DescribeOrganizationConfigRules</code> and <code>DescribeOrganizationConformancePacks</code> APIs can only see and interact with the organization-related resource that were deployed from within the account calling those APIs.</p> </note>

        Args:
            organization_conformance_pack_names: <p>The name that you assign to an organization conformance pack.</p>
            limit: <p>The maximum number of organization config packs returned on each page. If you do no specify a number, Config uses the default. The default is 100.</p>
            next_token: <p>The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_organization_conformance_pack_exception.NoSuchOrganizationConformancePackException: <p>Config organization conformance pack that you passed in the filter does not exist.</p> <p>For DeleteOrganizationConformancePack, you tried to delete an organization conformance pack that does not exist.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_organization_conformance_packs_request.DescribeOrganizationConformancePacksRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_organization_conformance_packs_response.DescribeOrganizationConformancePacksResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_organization_conformance_packs

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_organization_conformance_packs.describe_organization_conformance_packs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_organization_conformance_packs_request.DescribeOrganizationConformancePacksRequest = {}
        if organization_conformance_pack_names is not None:
            input_["organization_conformance_pack_names"] = (
                organization_conformance_pack_names
            )
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_organization_conformance_packs(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        organization_conformance_pack_names: Optional[
            "capo_config_service.types.organization_conformance_pack_names.OrganizationConformancePackNames"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.organization_conformance_pack.OrganizationConformancePack]":
        _token = next_token
        while True:
            _response = self.describe_organization_conformance_packs(
                config_overrides=config_overrides,
                organization_conformance_pack_names=organization_conformance_pack_names,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("organization_conformance_packs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_organization_conformance_pack_statuses(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        organization_conformance_pack_names: Optional[
            "capo_config_service.types.organization_conformance_pack_names.OrganizationConformancePackNames"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.describe_organization_conformance_pack_statuses_response.DescribeOrganizationConformancePackStatusesResponse":
        """<p>Provides organization conformance pack deployment status for an organization. </p> <note> <p>The status is not considered successful until organization conformance pack is successfully deployed in all the member accounts with an exception of excluded accounts.</p> <p>When you specify the limit and the next token, you receive a paginated response. Limit and next token are not applicable if you specify organization conformance pack names. They are only applicable, when you request all the organization conformance packs.</p> </note>

        Args:
            organization_conformance_pack_names: <p>The names of organization conformance packs for which you want status details. If you do not specify any names, Config returns details for all your organization conformance packs. </p>
            limit: <p>The maximum number of OrganizationConformancePackStatuses returned on each page. If you do no specify a number, Config uses the default. The default is 100. </p>
            next_token: <p>The nextToken string returned on a previous page that you use to get the next page of results in a paginated response. </p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_organization_conformance_pack_exception.NoSuchOrganizationConformancePackException: <p>Config organization conformance pack that you passed in the filter does not exist.</p> <p>For DeleteOrganizationConformancePack, you tried to delete an organization conformance pack that does not exist.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_organization_conformance_pack_statuses_request.DescribeOrganizationConformancePackStatusesRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_organization_conformance_pack_statuses_response.DescribeOrganizationConformancePackStatusesResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_organization_conformance_pack_statuses

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_organization_conformance_pack_statuses.describe_organization_conformance_pack_statuses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_organization_conformance_pack_statuses_request.DescribeOrganizationConformancePackStatusesRequest = {}
        if organization_conformance_pack_names is not None:
            input_["organization_conformance_pack_names"] = (
                organization_conformance_pack_names
            )
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_organization_conformance_pack_statuses(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        organization_conformance_pack_names: Optional[
            "capo_config_service.types.organization_conformance_pack_names.OrganizationConformancePackNames"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.organization_conformance_pack_status.OrganizationConformancePackStatus]":
        _token = next_token
        while True:
            _response = self.describe_organization_conformance_pack_statuses(
                config_overrides=config_overrides,
                organization_conformance_pack_names=organization_conformance_pack_names,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("organization_conformance_pack_statuses",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_pending_aggregation_requests(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional[
            "capo_config_service.types.describe_pending_aggregation_requests_limit.DescribePendingAggregationRequestsLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.describe_pending_aggregation_requests_response.DescribePendingAggregationRequestsResponse":
        """<p>Returns a list of all pending aggregation requests.</p>

        Args:
            limit: <p>The maximum number of evaluation results returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_pending_aggregation_requests_request.DescribePendingAggregationRequestsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_pending_aggregation_requests_response.DescribePendingAggregationRequestsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_pending_aggregation_requests

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_pending_aggregation_requests.describe_pending_aggregation_requests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_pending_aggregation_requests_request.DescribePendingAggregationRequestsRequest = {}
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_pending_aggregation_requests(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional[
            "capo_config_service.types.describe_pending_aggregation_requests_limit.DescribePendingAggregationRequestsLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.pending_aggregation_request.PendingAggregationRequest]":
        _token = next_token
        while True:
            _response = self.describe_pending_aggregation_requests(
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pending_aggregation_requests",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_remediation_configurations(
        self,
        config_rule_names: "capo_config_service.types.config_rule_names.ConfigRuleNames",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.describe_remediation_configurations_response.DescribeRemediationConfigurationsResponse":
        """<p>Returns the details of one or more remediation configurations.</p>

        Args:
            config_rule_names: <p>A list of Config rule names of remediation configurations for which you want details. </p>

        Raises:
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_remediation_configurations_request.DescribeRemediationConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_remediation_configurations_response.DescribeRemediationConfigurationsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_remediation_configurations

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_remediation_configurations.describe_remediation_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_remediation_configurations_request.DescribeRemediationConfigurationsRequest = {
            "config_rule_names": config_rule_names
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_remediation_exceptions(
        self,
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_keys: Optional[
            "capo_config_service.types.remediation_exception_resource_keys.RemediationExceptionResourceKeys"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.describe_remediation_exceptions_response.DescribeRemediationExceptionsResponse":
        """<p>Returns the details of one or more remediation exceptions. A detailed view of a remediation exception for a set of resources that includes an explanation of an exception and the time when the exception will be deleted. When you specify the limit and the next token, you receive a paginated response. </p> <note> <p>Config generates a remediation exception when a problem occurs executing a remediation action to a specific resource. Remediation exceptions blocks auto-remediation until the exception is cleared.</p> <p>When you specify the limit and the next token, you receive a paginated response. </p> <p>Limit and next token are not applicable if you request resources in batch. It is only applicable, when you request all resources.</p> </note>

        Args:
            config_rule_name: <p>The name of the Config rule.</p>
            resource_keys: <p>An exception list of resource exception keys to be processed with the current request. Config adds exception for each resource key. For example, Config adds 3 exceptions for 3 resource keys. </p>
            limit: <p>The maximum number of RemediationExceptionResourceKey returned on each page. The default is 25. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_remediation_exceptions_request.DescribeRemediationExceptionsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_remediation_exceptions_response.DescribeRemediationExceptionsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_remediation_exceptions

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_remediation_exceptions.describe_remediation_exceptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_remediation_exceptions_request.DescribeRemediationExceptionsRequest = {
            "config_rule_name": config_rule_name
        }
        if resource_keys is not None:
            input_["resource_keys"] = resource_keys
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_remediation_exceptions(
        self,
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_keys: Optional[
            "capo_config_service.types.remediation_exception_resource_keys.RemediationExceptionResourceKeys"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.describe_remediation_exceptions_response.DescribeRemediationExceptionsResponse]":
        _token = next_token
        while True:
            _response = self.describe_remediation_exceptions(
                config_rule_name,
                config_overrides=config_overrides,
                resource_keys=resource_keys,
                limit=limit,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_remediation_execution_status(
        self,
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_keys: Optional[
            "capo_config_service.types.resource_keys.ResourceKeys"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.describe_remediation_execution_status_response.DescribeRemediationExecutionStatusResponse":
        """<p>Provides a detailed view of a Remediation Execution for a set of resources including state, timestamps for when steps for the remediation execution occur, and any error messages for steps that have failed. When you specify the limit and the next token, you receive a paginated response.</p>

        Args:
            config_rule_name: <p>The name of the Config rule.</p>
            resource_keys: <p>A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID. </p>
            limit: <p>The maximum number of RemediationExecutionStatuses returned on each page. The default is maximum. If you specify 0, Config uses the default. </p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_remediation_configuration_exception.NoSuchRemediationConfigurationException: <p>You specified an Config rule without a remediation configuration.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_remediation_execution_status_request.DescribeRemediationExecutionStatusRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_remediation_execution_status_response.DescribeRemediationExecutionStatusResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_remediation_execution_status

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_remediation_execution_status.describe_remediation_execution_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_remediation_execution_status_request.DescribeRemediationExecutionStatusRequest = {
            "config_rule_name": config_rule_name
        }
        if resource_keys is not None:
            input_["resource_keys"] = resource_keys
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_remediation_execution_status(
        self,
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_keys: Optional[
            "capo_config_service.types.resource_keys.ResourceKeys"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.remediation_execution_status.RemediationExecutionStatus]":
        _token = next_token
        while True:
            _response = self.describe_remediation_execution_status(
                config_rule_name,
                config_overrides=config_overrides,
                resource_keys=resource_keys,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("remediation_execution_statuses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_retention_configurations(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        retention_configuration_names: Optional[
            "capo_config_service.types.retention_configuration_name_list.RetentionConfigurationNameList"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.describe_retention_configurations_response.DescribeRetentionConfigurationsResponse":
        """<p>Returns the details of one or more retention configurations. If the retention configuration name is not specified, this operation returns the details for all the retention configurations for that account.</p> <note> <p>Currently, Config supports only one retention configuration per region in your account.</p> </note>

        Args:
            retention_configuration_names: <p>A list of names of retention configurations for which you want details. If you do not specify a name, Config returns details for all the retention configurations for that account.</p> <note> <p>Currently, Config supports only one retention configuration per region in your account.</p> </note>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>

        Raises:
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_retention_configuration_exception.NoSuchRetentionConfigurationException: <p>You have specified a retention configuration that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.describe_retention_configurations_request.DescribeRetentionConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.describe_retention_configurations_response.DescribeRetentionConfigurationsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.describe_retention_configurations

            output, http_response = (
                capo_config_service._operations.starling_dove_service.describe_retention_configurations.describe_retention_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.describe_retention_configurations_request.DescribeRetentionConfigurationsRequest = {}
        if retention_configuration_names is not None:
            input_["retention_configuration_names"] = retention_configuration_names
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_retention_configurations(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        retention_configuration_names: Optional[
            "capo_config_service.types.retention_configuration_name_list.RetentionConfigurationNameList"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.retention_configuration.RetentionConfiguration]":
        _token = next_token
        while True:
            _response = self.describe_retention_configurations(
                config_overrides=config_overrides,
                retention_configuration_names=retention_configuration_names,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("retention_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def disassociate_resource_types(
        self,
        configuration_recorder_arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName",
        resource_types: "capo_config_service.types.resource_type_list.ResourceTypeList",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.disassociate_resource_types_response.DisassociateResourceTypesResponse":
        """<p>Removes all resource types specified in the <code>ResourceTypes</code> list from the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html">RecordingGroup</a> of configuration recorder and excludes these resource types when recording.</p> <p>For this operation, the configuration recorder must use a <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html">RecordingStrategy</a> that is either <code>INCLUSION_BY_RESOURCE_TYPES</code> or <code>EXCLUSION_BY_RESOURCE_TYPES</code>.</p>

        Args:
            configuration_recorder_arn: <p>The Amazon Resource Name (ARN) of the specified configuration recorder.</p>
            resource_types: <p>The list of resource types you want to remove from the recording group of the specified configuration recorder.</p>

        Raises:
            capo_config_service.errors.conflict_exception.ConflictException: <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because a service-linked recorder already exists for the specified service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because the specified service principal does not support multiple configuration recorders and one already exists.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector or service principal. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, you cannot create a connector because a connector already exists for the specified connector configuration.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, you cannot delete the service-linked recorder because it is currently in use by the linked Amazon Web Services service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConnector.html">DeleteConnector</a>, another in-progress operation is currently referencing the connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteDeliveryChannel.html">DeleteDeliveryChannel</a>, you cannot delete the specified delivery channel because the customer managed configuration recorder is running. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html">StopConfigurationRecorder</a> operation to stop the customer managed configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>For service-linked configuration recorders, the configuration recorder is not in use by the service. No association or dissociation of resource types is permitted.</p> </li> <li> <p>For service-linked configuration recorders, your requested change to the configuration recorder has been denied by its linked Amazon Web Services service.</p> </li> </ul>
            capo_config_service.errors.no_such_configuration_recorder_exception.NoSuchConfigurationRecorderException: <p>You have specified a configuration recorder that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.disassociate_resource_types_request.DisassociateResourceTypesRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.disassociate_resource_types_response.DisassociateResourceTypesResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.disassociate_resource_types

            output, http_response = (
                capo_config_service._operations.starling_dove_service.disassociate_resource_types.disassociate_resource_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.disassociate_resource_types_request.DisassociateResourceTypesRequest = {
            "configuration_recorder_arn": configuration_recorder_arn,
            "resource_types": resource_types,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_aggregate_compliance_details_by_config_rule(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        account_id: "capo_config_service.types.account_id.AccountId",
        aws_region: "capo_config_service.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        compliance_type: Optional[
            "capo_config_service.types.compliance_type.ComplianceType"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.get_aggregate_compliance_details_by_config_rule_response.GetAggregateComplianceDetailsByConfigRuleResponse":
        """<p>Returns the evaluation results for the specified Config rule for a specific resource in a rule. The results indicate which Amazon Web Services resources were evaluated by the rule, when each resource was last evaluated, and whether each resource complies with the rule. </p> <note> <p>The results can return an empty result page. But if you have a <code>nextToken</code>, the results are displayed on the next page.</p> </note>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>
            config_rule_name: <p>The name of the Config rule for which you want compliance information.</p>
            account_id: <p>The 12-digit account ID of the source account.</p>
            aws_region: <p>The source region from where the data is aggregated.</p>
            compliance_type: <p>The resource compliance status.</p> <note> <p>For the <code>GetAggregateComplianceDetailsByConfigRuleRequest</code> data type, Config supports only the <code>COMPLIANT</code> and <code>NON_COMPLIANT</code>. Config does not support the <code>NOT_APPLICABLE</code> and <code>INSUFFICIENT_DATA</code> values.</p> </note>
            limit: <p>The maximum number of evaluation results returned on each page. The default is 50. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_aggregate_compliance_details_by_config_rule_request.GetAggregateComplianceDetailsByConfigRuleRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_aggregate_compliance_details_by_config_rule_response.GetAggregateComplianceDetailsByConfigRuleResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_aggregate_compliance_details_by_config_rule

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_aggregate_compliance_details_by_config_rule.get_aggregate_compliance_details_by_config_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_aggregate_compliance_details_by_config_rule_request.GetAggregateComplianceDetailsByConfigRuleRequest = {
            "configuration_aggregator_name": configuration_aggregator_name,
            "config_rule_name": config_rule_name,
            "account_id": account_id,
            "aws_region": aws_region,
        }
        if compliance_type is not None:
            input_["compliance_type"] = compliance_type
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_aggregate_compliance_details_by_config_rule(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        account_id: "capo_config_service.types.account_id.AccountId",
        aws_region: "capo_config_service.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        compliance_type: Optional[
            "capo_config_service.types.compliance_type.ComplianceType"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.aggregate_evaluation_result.AggregateEvaluationResult]":
        _token = next_token
        while True:
            _response = self.get_aggregate_compliance_details_by_config_rule(
                configuration_aggregator_name,
                config_rule_name,
                account_id,
                aws_region,
                config_overrides=config_overrides,
                compliance_type=compliance_type,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("aggregate_evaluation_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_aggregate_config_rule_compliance_summary(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.config_rule_compliance_summary_filters.ConfigRuleComplianceSummaryFilters"
        ] = None,
        group_by_key: Optional[
            "capo_config_service.types.config_rule_compliance_summary_group_key.ConfigRuleComplianceSummaryGroupKey"
        ] = None,
        limit: Optional[
            "capo_config_service.types.group_by_api_limit.GroupByAPILimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.get_aggregate_config_rule_compliance_summary_response.GetAggregateConfigRuleComplianceSummaryResponse":
        """<p>Returns the number of compliant and noncompliant rules for one or more accounts and regions in an aggregator.</p> <note> <p>The results can return an empty result page, but if you have a nextToken, the results are displayed on the next page.</p> </note>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>
            filters: <p>Filters the results based on the ConfigRuleComplianceSummaryFilters object.</p>
            group_by_key: <p>Groups the result based on ACCOUNT_ID or AWS_REGION.</p>
            limit: <p>The maximum number of evaluation results returned on each page. The default is 1000. You cannot specify a number greater than 1000. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_aggregate_config_rule_compliance_summary_request.GetAggregateConfigRuleComplianceSummaryRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_aggregate_config_rule_compliance_summary_response.GetAggregateConfigRuleComplianceSummaryResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_aggregate_config_rule_compliance_summary

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_aggregate_config_rule_compliance_summary.get_aggregate_config_rule_compliance_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_aggregate_config_rule_compliance_summary_request.GetAggregateConfigRuleComplianceSummaryRequest = {
            "configuration_aggregator_name": configuration_aggregator_name
        }
        if filters is not None:
            input_["filters"] = filters
        if group_by_key is not None:
            input_["group_by_key"] = group_by_key
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_aggregate_config_rule_compliance_summary(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.config_rule_compliance_summary_filters.ConfigRuleComplianceSummaryFilters"
        ] = None,
        group_by_key: Optional[
            "capo_config_service.types.config_rule_compliance_summary_group_key.ConfigRuleComplianceSummaryGroupKey"
        ] = None,
        limit: Optional[
            "capo_config_service.types.group_by_api_limit.GroupByAPILimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.get_aggregate_config_rule_compliance_summary_response.GetAggregateConfigRuleComplianceSummaryResponse]":
        _token = next_token
        while True:
            _response = self.get_aggregate_config_rule_compliance_summary(
                configuration_aggregator_name,
                config_overrides=config_overrides,
                filters=filters,
                group_by_key=group_by_key,
                limit=limit,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_aggregate_conformance_pack_compliance_summary(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.aggregate_conformance_pack_compliance_summary_filters.AggregateConformancePackComplianceSummaryFilters"
        ] = None,
        group_by_key: Optional[
            "capo_config_service.types.aggregate_conformance_pack_compliance_summary_group_key.AggregateConformancePackComplianceSummaryGroupKey"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.get_aggregate_conformance_pack_compliance_summary_response.GetAggregateConformancePackComplianceSummaryResponse":
        """<p>Returns the count of compliant and noncompliant conformance packs across all Amazon Web Services accounts and Amazon Web Services Regions in an aggregator. You can filter based on Amazon Web Services account ID or Amazon Web Services Region.</p> <note> <p>The results can return an empty result page, but if you have a nextToken, the results are displayed on the next page.</p> </note>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>
            filters: <p>Filters the results based on the <code>AggregateConformancePackComplianceSummaryFilters</code> object.</p>
            group_by_key: <p>Groups the result based on Amazon Web Services account ID or Amazon Web Services Region.</p>
            limit: <p>The maximum number of results returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_aggregate_conformance_pack_compliance_summary_request.GetAggregateConformancePackComplianceSummaryRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_aggregate_conformance_pack_compliance_summary_response.GetAggregateConformancePackComplianceSummaryResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_aggregate_conformance_pack_compliance_summary

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_aggregate_conformance_pack_compliance_summary.get_aggregate_conformance_pack_compliance_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_aggregate_conformance_pack_compliance_summary_request.GetAggregateConformancePackComplianceSummaryRequest = {
            "configuration_aggregator_name": configuration_aggregator_name
        }
        if filters is not None:
            input_["filters"] = filters
        if group_by_key is not None:
            input_["group_by_key"] = group_by_key
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_aggregate_conformance_pack_compliance_summary(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.aggregate_conformance_pack_compliance_summary_filters.AggregateConformancePackComplianceSummaryFilters"
        ] = None,
        group_by_key: Optional[
            "capo_config_service.types.aggregate_conformance_pack_compliance_summary_group_key.AggregateConformancePackComplianceSummaryGroupKey"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.get_aggregate_conformance_pack_compliance_summary_response.GetAggregateConformancePackComplianceSummaryResponse]":
        _token = next_token
        while True:
            _response = self.get_aggregate_conformance_pack_compliance_summary(
                configuration_aggregator_name,
                config_overrides=config_overrides,
                filters=filters,
                group_by_key=group_by_key,
                limit=limit,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_aggregate_discovered_resource_counts(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.resource_count_filters.ResourceCountFilters"
        ] = None,
        group_by_key: Optional[
            "capo_config_service.types.resource_count_group_key.ResourceCountGroupKey"
        ] = None,
        limit: Optional[
            "capo_config_service.types.group_by_api_limit.GroupByAPILimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.get_aggregate_discovered_resource_counts_response.GetAggregateDiscoveredResourceCountsResponse":
        """<p>Returns the resource counts across accounts and regions that are present in your Config aggregator. You can request the resource counts by providing filters and GroupByKey.</p> <p>For example, if the input contains accountID 12345678910 and region us-east-1 in filters, the API returns the count of resources in account ID 12345678910 and region us-east-1. If the input contains ACCOUNT_ID as a GroupByKey, the API returns resource counts for all source accounts that are present in your aggregator.</p>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>
            filters: <p>Filters the results based on the <code>ResourceCountFilters</code> object.</p>
            group_by_key: <p>The key to group the resource counts.</p>
            limit: <p>The maximum number of <a>GroupedResourceCount</a> objects returned on each page. The default is 1000. You cannot specify a number greater than 1000. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_aggregate_discovered_resource_counts_request.GetAggregateDiscoveredResourceCountsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_aggregate_discovered_resource_counts_response.GetAggregateDiscoveredResourceCountsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_aggregate_discovered_resource_counts

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_aggregate_discovered_resource_counts.get_aggregate_discovered_resource_counts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_aggregate_discovered_resource_counts_request.GetAggregateDiscoveredResourceCountsRequest = {
            "configuration_aggregator_name": configuration_aggregator_name
        }
        if filters is not None:
            input_["filters"] = filters
        if group_by_key is not None:
            input_["group_by_key"] = group_by_key
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_aggregate_discovered_resource_counts(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.resource_count_filters.ResourceCountFilters"
        ] = None,
        group_by_key: Optional[
            "capo_config_service.types.resource_count_group_key.ResourceCountGroupKey"
        ] = None,
        limit: Optional[
            "capo_config_service.types.group_by_api_limit.GroupByAPILimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.get_aggregate_discovered_resource_counts_response.GetAggregateDiscoveredResourceCountsResponse]":
        _token = next_token
        while True:
            _response = self.get_aggregate_discovered_resource_counts(
                configuration_aggregator_name,
                config_overrides=config_overrides,
                filters=filters,
                group_by_key=group_by_key,
                limit=limit,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_aggregate_resource_config(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        resource_identifier: "capo_config_service.types.aggregate_resource_identifier.AggregateResourceIdentifier",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.get_aggregate_resource_config_response.GetAggregateResourceConfigResponse":
        """<p>Returns configuration item that is aggregated for your specific resource in a specific source account and region.</p> <note> <p>The API does not return results for deleted resources.</p> </note>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>
            resource_identifier: <p>An object that identifies aggregate resource.</p>

        Raises:
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.oversized_configuration_item_exception.OversizedConfigurationItemException: <p>The configuration item size is outside the allowable range.</p>
            capo_config_service.errors.resource_not_discovered_exception.ResourceNotDiscoveredException: <p>You have specified a resource that is either unknown or has not been discovered.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_aggregate_resource_config_request.GetAggregateResourceConfigRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_aggregate_resource_config_response.GetAggregateResourceConfigResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_aggregate_resource_config

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_aggregate_resource_config.get_aggregate_resource_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_aggregate_resource_config_request.GetAggregateResourceConfigRequest = {
            "configuration_aggregator_name": configuration_aggregator_name,
            "resource_identifier": resource_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_compliance_details_by_config_rule(
        self,
        config_rule_name: "capo_config_service.types.string_with_char_limit64.StringWithCharLimit64",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        compliance_types: Optional[
            "capo_config_service.types.compliance_types.ComplianceTypes"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.get_compliance_details_by_config_rule_response.GetComplianceDetailsByConfigRuleResponse":
        """<p>Returns the evaluation results for the specified Config rule. The results indicate which Amazon Web Services resources were evaluated by the rule, when each resource was last evaluated, and whether each resource complies with the rule.</p>

        Args:
            config_rule_name: <p>The name of the Config rule for which you want compliance information.</p>
            compliance_types: <p>Filters the results by compliance.</p> <p> <code>INSUFFICIENT_DATA</code> is a valid <code>ComplianceType</code> that is returned when an Config rule cannot be evaluated. However, <code>INSUFFICIENT_DATA</code> cannot be used as a <code>ComplianceType</code> for filtering results.</p>
            limit: <p>The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_config_rule_exception.NoSuchConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_compliance_details_by_config_rule_request.GetComplianceDetailsByConfigRuleRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_compliance_details_by_config_rule_response.GetComplianceDetailsByConfigRuleResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_compliance_details_by_config_rule

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_compliance_details_by_config_rule.get_compliance_details_by_config_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_compliance_details_by_config_rule_request.GetComplianceDetailsByConfigRuleRequest = {
            "config_rule_name": config_rule_name
        }
        if compliance_types is not None:
            input_["compliance_types"] = compliance_types
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_compliance_details_by_config_rule(
        self,
        config_rule_name: "capo_config_service.types.string_with_char_limit64.StringWithCharLimit64",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        compliance_types: Optional[
            "capo_config_service.types.compliance_types.ComplianceTypes"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.evaluation_result.EvaluationResult]":
        _token = next_token
        while True:
            _response = self.get_compliance_details_by_config_rule(
                config_rule_name,
                config_overrides=config_overrides,
                compliance_types=compliance_types,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("evaluation_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_compliance_details_by_resource(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_type: Optional[
            "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
        ] = None,
        resource_id: Optional[
            "capo_config_service.types.base_resource_id.BaseResourceId"
        ] = None,
        compliance_types: Optional[
            "capo_config_service.types.compliance_types.ComplianceTypes"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        resource_evaluation_id: Optional[
            "capo_config_service.types.resource_evaluation_id.ResourceEvaluationId"
        ] = None,
    ) -> "capo_config_service.types.get_compliance_details_by_resource_response.GetComplianceDetailsByResourceResponse":
        """<p>Returns the evaluation results for the specified Amazon Web Services resource. The results indicate which Config rules were used to evaluate the resource, when each rule was last invoked, and whether the resource complies with each rule.</p>

        Args:
            resource_type: <p>The type of the Amazon Web Services resource for which you want compliance information.</p>
            resource_id: <p>The ID of the Amazon Web Services resource for which you want compliance information.</p>
            compliance_types: <p>Filters the results by compliance.</p> <p> <code>INSUFFICIENT_DATA</code> is a valid <code>ComplianceType</code> that is returned when an Config rule cannot be evaluated. However, <code>INSUFFICIENT_DATA</code> cannot be used as a <code>ComplianceType</code> for filtering results.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>
            resource_evaluation_id: <p>The unique ID of Amazon Web Services resource execution for which you want to retrieve evaluation results. </p> <note> <p>You need to only provide either a <code>ResourceEvaluationID</code> or a <code>ResourceID </code>and <code>ResourceType</code>.</p> </note>

        Raises:
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_compliance_details_by_resource_request.GetComplianceDetailsByResourceRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_compliance_details_by_resource_response.GetComplianceDetailsByResourceResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_compliance_details_by_resource

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_compliance_details_by_resource.get_compliance_details_by_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_compliance_details_by_resource_request.GetComplianceDetailsByResourceRequest = {}
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if compliance_types is not None:
            input_["compliance_types"] = compliance_types
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_evaluation_id is not None:
            input_["resource_evaluation_id"] = resource_evaluation_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_compliance_details_by_resource(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_type: Optional[
            "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
        ] = None,
        resource_id: Optional[
            "capo_config_service.types.base_resource_id.BaseResourceId"
        ] = None,
        compliance_types: Optional[
            "capo_config_service.types.compliance_types.ComplianceTypes"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        resource_evaluation_id: Optional[
            "capo_config_service.types.resource_evaluation_id.ResourceEvaluationId"
        ] = None,
    ) -> "Iterator[capo_config_service.types.evaluation_result.EvaluationResult]":
        _token = next_token
        while True:
            _response = self.get_compliance_details_by_resource(
                config_overrides=config_overrides,
                resource_type=resource_type,
                resource_id=resource_id,
                compliance_types=compliance_types,
                next_token=_token,
                resource_evaluation_id=resource_evaluation_id,
            )
            _page = _resolve_path(_response, ("evaluation_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_compliance_summary_by_config_rule(
        self, *, config_overrides: Optional[ConfigServiceClientConfig] = None
    ) -> "capo_config_service.types.get_compliance_summary_by_config_rule_response.GetComplianceSummaryByConfigRuleResponse":
        """<p>Returns the number of Config rules that are compliant and noncompliant, up to a maximum of 25 for each.</p>

        Raises:
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_config_service.types.get_compliance_summary_by_config_rule_response.GetComplianceSummaryByConfigRuleResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_compliance_summary_by_config_rule

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_compliance_summary_by_config_rule.get_compliance_summary_by_config_rule(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_compliance_summary_by_resource_type(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_types: Optional[
            "capo_config_service.types.resource_types.ResourceTypes"
        ] = None,
    ) -> "capo_config_service.types.get_compliance_summary_by_resource_type_response.GetComplianceSummaryByResourceTypeResponse":
        """<p>Returns the number of resources that are compliant and the number that are noncompliant. You can specify one or more resource types to get these numbers for each resource type. The maximum number returned is 100.</p>

        Args:
            resource_types: <p>Specify one or more resource types to get the number of resources that are compliant and the number that are noncompliant for each resource type.</p> <p>For this request, you can specify an Amazon Web Services resource type such as <code>AWS::EC2::Instance</code>. You can specify that the resource type is an Amazon Web Services account by specifying <code>AWS::::Account</code>.</p>

        Raises:
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_compliance_summary_by_resource_type_request.GetComplianceSummaryByResourceTypeRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_compliance_summary_by_resource_type_response.GetComplianceSummaryByResourceTypeResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_compliance_summary_by_resource_type

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_compliance_summary_by_resource_type.get_compliance_summary_by_resource_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_compliance_summary_by_resource_type_request.GetComplianceSummaryByResourceTypeRequest = {}
        if resource_types is not None:
            input_["resource_types"] = resource_types

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_conformance_pack_compliance_details(
        self,
        conformance_pack_name: "capo_config_service.types.conformance_pack_name.ConformancePackName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.conformance_pack_evaluation_filters.ConformancePackEvaluationFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.get_conformance_pack_compliance_details_limit.GetConformancePackComplianceDetailsLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.get_conformance_pack_compliance_details_response.GetConformancePackComplianceDetailsResponse":
        """<p>Returns compliance details of a conformance pack for all Amazon Web Services resources that are monitered by conformance pack.</p>

        Args:
            conformance_pack_name: <p>Name of the conformance pack.</p>
            filters: <p>A <code>ConformancePackEvaluationFilters</code> object.</p>
            limit: <p>The maximum number of evaluation results returned on each page. If you do no specify a number, Config uses the default. The default is 100.</p>
            next_token: <p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_config_rule_in_conformance_pack_exception.NoSuchConfigRuleInConformancePackException: <p>Config rule that you passed in the filter does not exist.</p>
            capo_config_service.errors.no_such_conformance_pack_exception.NoSuchConformancePackException: <p>You specified one or more conformance packs that do not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_conformance_pack_compliance_details_request.GetConformancePackComplianceDetailsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_conformance_pack_compliance_details_response.GetConformancePackComplianceDetailsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_conformance_pack_compliance_details

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_conformance_pack_compliance_details.get_conformance_pack_compliance_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_conformance_pack_compliance_details_request.GetConformancePackComplianceDetailsRequest = {
            "conformance_pack_name": conformance_pack_name
        }
        if filters is not None:
            input_["filters"] = filters
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_conformance_pack_compliance_details(
        self,
        conformance_pack_name: "capo_config_service.types.conformance_pack_name.ConformancePackName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.conformance_pack_evaluation_filters.ConformancePackEvaluationFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.get_conformance_pack_compliance_details_limit.GetConformancePackComplianceDetailsLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.get_conformance_pack_compliance_details_response.GetConformancePackComplianceDetailsResponse]":
        _token = next_token
        while True:
            _response = self.get_conformance_pack_compliance_details(
                conformance_pack_name,
                config_overrides=config_overrides,
                filters=filters,
                limit=limit,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_conformance_pack_compliance_summary(
        self,
        conformance_pack_names: "capo_config_service.types.conformance_pack_names_to_summarize_list.ConformancePackNamesToSummarizeList",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional[
            "capo_config_service.types.page_size_limit.PageSizeLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.get_conformance_pack_compliance_summary_response.GetConformancePackComplianceSummaryResponse":
        """<p>Returns compliance details for the conformance pack based on the cumulative compliance results of all the rules in that conformance pack.</p>

        Args:
            conformance_pack_names: <p>Names of conformance packs.</p>
            limit: <p>The maximum number of conformance packs returned on each page.</p>
            next_token: <p>The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_conformance_pack_exception.NoSuchConformancePackException: <p>You specified one or more conformance packs that do not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_conformance_pack_compliance_summary_request.GetConformancePackComplianceSummaryRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_conformance_pack_compliance_summary_response.GetConformancePackComplianceSummaryResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_conformance_pack_compliance_summary

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_conformance_pack_compliance_summary.get_conformance_pack_compliance_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_conformance_pack_compliance_summary_request.GetConformancePackComplianceSummaryRequest = {
            "conformance_pack_names": conformance_pack_names
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_conformance_pack_compliance_summary(
        self,
        conformance_pack_names: "capo_config_service.types.conformance_pack_names_to_summarize_list.ConformancePackNamesToSummarizeList",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional[
            "capo_config_service.types.page_size_limit.PageSizeLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.conformance_pack_compliance_summary.ConformancePackComplianceSummary]":
        _token = next_token
        while True:
            _response = self.get_conformance_pack_compliance_summary(
                conformance_pack_names,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("conformance_pack_compliance_summary_list",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_connector(
        self,
        arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.get_connector_response.GetConnectorResponse":
        """<p>Returns the details of the specified connector.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the connector.</p>

        Raises:
            capo_config_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>You have specified a resource that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_connector_request.GetConnectorRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_connector_response.GetConnectorResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_connector

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_connector.get_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_connector_request.GetConnectorRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_custom_rule_policy(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        config_rule_name: Optional[
            "capo_config_service.types.config_rule_name.ConfigRuleName"
        ] = None,
    ) -> "capo_config_service.types.get_custom_rule_policy_response.GetCustomRulePolicyResponse":
        """<p>Returns the policy definition containing the logic for your Config Custom Policy rule.</p>

        Args:
            config_rule_name: <p>The name of your Config Custom Policy rule.</p>

        Raises:
            capo_config_service.errors.no_such_config_rule_exception.NoSuchConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_custom_rule_policy_request.GetCustomRulePolicyRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_custom_rule_policy_response.GetCustomRulePolicyResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_custom_rule_policy

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_custom_rule_policy.get_custom_rule_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_custom_rule_policy_request.GetCustomRulePolicyRequest = {}
        if config_rule_name is not None:
            input_["config_rule_name"] = config_rule_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_discovered_resource_counts(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_types: Optional[
            "capo_config_service.types.resource_types.ResourceTypes"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.get_discovered_resource_counts_response.GetDiscoveredResourceCountsResponse":
        """<p>Returns the resource types, the number of each resource type, and the total number of resources that Config is recording in this region for your Amazon Web Services account. </p> <p class="title"> <b>Example</b> </p> <ol> <li> <p>Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets.</p> </li> <li> <p>You make a call to the <code>GetDiscoveredResourceCounts</code> action and specify that you want all resource types. </p> </li> <li> <p>Config returns the following:</p> <ul> <li> <p>The resource types (EC2 instances, IAM users, and S3 buckets).</p> </li> <li> <p>The number of each resource type (25, 20, and 15).</p> </li> <li> <p>The total number of all resources (60).</p> </li> </ul> </li> </ol> <p>The response is paginated. By default, Config lists 100 <a>ResourceCount</a> objects on each page. You can customize this number with the <code>limit</code> parameter. The response includes a <code>nextToken</code> string. To get the next page of results, run the request again and specify the string for the <code>nextToken</code> parameter.</p> <note> <p>If you make a call to the <a>GetDiscoveredResourceCounts</a> action, you might not immediately receive resource counts in the following situations:</p> <ul> <li> <p>You are a new Config customer.</p> </li> <li> <p>You just enabled resource recording.</p> </li> </ul> <p>It might take a few minutes for Config to record and count your resources. Wait a few minutes and then retry the <a>GetDiscoveredResourceCounts</a> action. </p> </note>

        Args:
            resource_types: <p>The comma-separated list that specifies the resource types that you want Config to return (for example, <code>"AWS::EC2::Instance"</code>, <code>"AWS::IAM::User"</code>).</p> <p>If a value for <code>resourceTypes</code> is not specified, Config returns all resource types that Config is recording in the region for your account.</p> <note> <p>If the configuration recorder is turned off, Config returns an empty list of <a>ResourceCount</a> objects. If the configuration recorder is not recording a specific resource type (for example, S3 buckets), that resource type is not returned in the list of <a>ResourceCount</a> objects.</p> </note>
            limit: <p>The maximum number of <a>ResourceCount</a> objects returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_discovered_resource_counts_request.GetDiscoveredResourceCountsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_discovered_resource_counts_response.GetDiscoveredResourceCountsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_discovered_resource_counts

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_discovered_resource_counts.get_discovered_resource_counts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_discovered_resource_counts_request.GetDiscoveredResourceCountsRequest = {}
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_discovered_resource_counts(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_types: Optional[
            "capo_config_service.types.resource_types.ResourceTypes"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.get_discovered_resource_counts_response.GetDiscoveredResourceCountsResponse]":
        _token = next_token
        while True:
            _response = self.get_discovered_resource_counts(
                config_overrides=config_overrides,
                resource_types=resource_types,
                limit=limit,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_organization_config_rule_detailed_status(
        self,
        organization_config_rule_name: "capo_config_service.types.organization_config_rule_name.OrganizationConfigRuleName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.status_detail_filters.StatusDetailFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.get_organization_config_rule_detailed_status_response.GetOrganizationConfigRuleDetailedStatusResponse":
        """<p>Returns detailed status for each member account within an organization for a given organization Config rule.</p>

        Args:
            organization_config_rule_name: <p>The name of your organization Config rule for which you want status details for member accounts.</p>
            filters: <p>A <code>StatusDetailFilters</code> object.</p>
            limit: <p>The maximum number of <code>OrganizationConfigRuleDetailedStatus</code> returned on each page. If you do not specify a number, Config uses the default. The default is 100.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_organization_config_rule_exception.NoSuchOrganizationConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an organization Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_organization_config_rule_detailed_status_request.GetOrganizationConfigRuleDetailedStatusRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_organization_config_rule_detailed_status_response.GetOrganizationConfigRuleDetailedStatusResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_organization_config_rule_detailed_status

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_organization_config_rule_detailed_status.get_organization_config_rule_detailed_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_organization_config_rule_detailed_status_request.GetOrganizationConfigRuleDetailedStatusRequest = {
            "organization_config_rule_name": organization_config_rule_name
        }
        if filters is not None:
            input_["filters"] = filters
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_organization_config_rule_detailed_status(
        self,
        organization_config_rule_name: "capo_config_service.types.organization_config_rule_name.OrganizationConfigRuleName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.status_detail_filters.StatusDetailFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> (
        "Iterator[capo_config_service.types.member_account_status.MemberAccountStatus]"
    ):
        _token = next_token
        while True:
            _response = self.get_organization_config_rule_detailed_status(
                organization_config_rule_name,
                config_overrides=config_overrides,
                filters=filters,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("organization_config_rule_detailed_status",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_organization_conformance_pack_detailed_status(
        self,
        organization_conformance_pack_name: "capo_config_service.types.organization_conformance_pack_name.OrganizationConformancePackName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.organization_resource_detailed_status_filters.OrganizationResourceDetailedStatusFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.get_organization_conformance_pack_detailed_status_response.GetOrganizationConformancePackDetailedStatusResponse":
        """<p>Returns detailed status for each member account within an organization for a given organization conformance pack.</p>

        Args:
            organization_conformance_pack_name: <p>The name of organization conformance pack for which you want status details for member accounts.</p>
            filters: <p>An <code>OrganizationResourceDetailedStatusFilters</code> object.</p>
            limit: <p>The maximum number of <code>OrganizationConformancePackDetailedStatuses</code> returned on each page. If you do not specify a number, Config uses the default. The default is 100. </p>
            next_token: <p>The nextToken string returned on a previous page that you use to get the next page of results in a paginated response. </p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_organization_conformance_pack_exception.NoSuchOrganizationConformancePackException: <p>Config organization conformance pack that you passed in the filter does not exist.</p> <p>For DeleteOrganizationConformancePack, you tried to delete an organization conformance pack that does not exist.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_organization_conformance_pack_detailed_status_request.GetOrganizationConformancePackDetailedStatusRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_organization_conformance_pack_detailed_status_response.GetOrganizationConformancePackDetailedStatusResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_organization_conformance_pack_detailed_status

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_organization_conformance_pack_detailed_status.get_organization_conformance_pack_detailed_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_organization_conformance_pack_detailed_status_request.GetOrganizationConformancePackDetailedStatusRequest = {
            "organization_conformance_pack_name": organization_conformance_pack_name
        }
        if filters is not None:
            input_["filters"] = filters
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_organization_conformance_pack_detailed_status(
        self,
        organization_conformance_pack_name: "capo_config_service.types.organization_conformance_pack_name.OrganizationConformancePackName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.organization_resource_detailed_status_filters.OrganizationResourceDetailedStatusFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.cosmos_page_limit.CosmosPageLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.organization_conformance_pack_detailed_status.OrganizationConformancePackDetailedStatus]":
        _token = next_token
        while True:
            _response = self.get_organization_conformance_pack_detailed_status(
                organization_conformance_pack_name,
                config_overrides=config_overrides,
                filters=filters,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(
                _response, ("organization_conformance_pack_detailed_statuses",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_organization_custom_rule_policy(
        self,
        organization_config_rule_name: "capo_config_service.types.organization_config_rule_name.OrganizationConfigRuleName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.get_organization_custom_rule_policy_response.GetOrganizationCustomRulePolicyResponse":
        """<p>Returns the policy definition containing the logic for your organization Config Custom Policy rule.</p>

        Args:
            organization_config_rule_name: <p>The name of your organization Config Custom Policy rule. </p>

        Raises:
            capo_config_service.errors.no_such_organization_config_rule_exception.NoSuchOrganizationConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an organization Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_organization_custom_rule_policy_request.GetOrganizationCustomRulePolicyRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_organization_custom_rule_policy_response.GetOrganizationCustomRulePolicyResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_organization_custom_rule_policy

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_organization_custom_rule_policy.get_organization_custom_rule_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_organization_custom_rule_policy_request.GetOrganizationCustomRulePolicyRequest = {
            "organization_config_rule_name": organization_config_rule_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_config_history(
        self,
        resource_type: "capo_config_service.types.resource_type.ResourceType",
        resource_id: "capo_config_service.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        later_time: Optional["capo_config_service.types.later_time.LaterTime"] = None,
        earlier_time: Optional[
            "capo_config_service.types.earlier_time.EarlierTime"
        ] = None,
        chronological_order: Optional[
            "capo_config_service.types.chronological_order.ChronologicalOrder"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.get_resource_config_history_response.GetResourceConfigHistoryResponse":
        """<important> <p>For accurate reporting on the compliance status, you must record the <code>AWS::Config::ResourceCompliance</code> resource type.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html">Recording Amazon Web Services Resources</a> in the <i>Config Resources Developer Guide</i>.</p> </important> <p>Returns a list of configurations items (CIs) for the specified resource.</p> <p> <b>Contents</b> </p> <p>The list contains details about each state of the resource during the specified time interval. If you specified a retention period to retain your CIs between a minimum of 30 days and a maximum of 7 years (2557 days), Config returns the CIs for the specified retention period. </p> <p> <b>Pagination</b> </p> <p>The response is paginated. By default, Config returns a limit of 10 configuration items per page. You can customize this number with the <code>limit</code> parameter. The response includes a <code>nextToken</code> string. To get the next page of results, run the request again and specify the string for the <code>nextToken</code> parameter.</p> <note> <p>Each call to the API is limited to span a duration of seven days. It is likely that the number of records returned is smaller than the specified <code>limit</code>. In such cases, you can make another call, using the <code>nextToken</code>.</p> </note>

        Args:
            resource_type: <p>The resource type.</p>
            resource_id: <p>The ID of the resource (for example., <code>sg-xxxxxx</code>).</p>
            later_time: <p>The chronologically latest time in the time range for which the history requested. If not specified, current time is taken.</p>
            earlier_time: <p>The chronologically earliest time in the time range for which the history requested. If not specified, the action returns paginated results that contain configuration items that start when the first configuration item was recorded.</p>
            chronological_order: <p>The chronological order for configuration items listed. By default, the results are listed in reverse chronological order.</p>
            limit: <p>The maximum number of configuration items returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_time_range_exception.InvalidTimeRangeException: <p>The specified time range is not valid. The earlier time is not chronologically before the later time.</p>
            capo_config_service.errors.no_available_configuration_recorder_exception.NoAvailableConfigurationRecorderException: <p>There are no customer managed configuration recorders available to record your resources. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html">PutConfigurationRecorder</a> operation to create the customer managed configuration recorder.</p>
            capo_config_service.errors.resource_not_discovered_exception.ResourceNotDiscoveredException: <p>You have specified a resource that is either unknown or has not been discovered.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_resource_config_history_request.GetResourceConfigHistoryRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_resource_config_history_response.GetResourceConfigHistoryResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_resource_config_history

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_resource_config_history.get_resource_config_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_resource_config_history_request.GetResourceConfigHistoryRequest = {
            "resource_type": resource_type,
            "resource_id": resource_id,
        }
        if later_time is not None:
            input_["later_time"] = later_time
        if earlier_time is not None:
            input_["earlier_time"] = earlier_time
        if chronological_order is not None:
            input_["chronological_order"] = chronological_order
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_resource_config_history(
        self,
        resource_type: "capo_config_service.types.resource_type.ResourceType",
        resource_id: "capo_config_service.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        later_time: Optional["capo_config_service.types.later_time.LaterTime"] = None,
        earlier_time: Optional[
            "capo_config_service.types.earlier_time.EarlierTime"
        ] = None,
        chronological_order: Optional[
            "capo_config_service.types.chronological_order.ChronologicalOrder"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.configuration_item.ConfigurationItem]":
        _token = next_token
        while True:
            _response = self.get_resource_config_history(
                resource_type,
                resource_id,
                config_overrides=config_overrides,
                later_time=later_time,
                earlier_time=earlier_time,
                chronological_order=chronological_order,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("configuration_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_resource_evaluation_summary(
        self,
        resource_evaluation_id: "capo_config_service.types.resource_evaluation_id.ResourceEvaluationId",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.get_resource_evaluation_summary_response.GetResourceEvaluationSummaryResponse":
        """<p>Returns a summary of resource evaluation for the specified resource evaluation ID from the proactive rules that were run. The results indicate which evaluation context was used to evaluate the rules, which resource details were evaluated, the evaluation mode that was run, and whether the resource details comply with the configuration of the proactive rules. </p> <note> <p>To see additional information about the evaluation result, such as which rule flagged a resource as NON_COMPLIANT, use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceDetailsByResource.html">GetComplianceDetailsByResource</a> API. For more information, see the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceEvaluationSummary.html#API_GetResourceEvaluationSummary_Examples">Examples</a> section.</p> </note>

        Args:
            resource_evaluation_id: <p>The unique <code>ResourceEvaluationId</code> of Amazon Web Services resource execution for which you want to retrieve the evaluation summary.</p>

        Raises:
            capo_config_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>You have specified a resource that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_resource_evaluation_summary_request.GetResourceEvaluationSummaryRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_resource_evaluation_summary_response.GetResourceEvaluationSummaryResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_resource_evaluation_summary

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_resource_evaluation_summary.get_resource_evaluation_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_resource_evaluation_summary_request.GetResourceEvaluationSummaryRequest = {
            "resource_evaluation_id": resource_evaluation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_stored_query(
        self,
        query_name: "capo_config_service.types.query_name.QueryName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.get_stored_query_response.GetStoredQueryResponse":
        """<p>Returns the details of a specific stored query.</p>

        Args:
            query_name: <p>The name of the query.</p>

        Raises:
            capo_config_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>You have specified a resource that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.get_stored_query_request.GetStoredQueryRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.get_stored_query_response.GetStoredQueryResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.get_stored_query

            output, http_response = (
                capo_config_service._operations.starling_dove_service.get_stored_query.get_stored_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.get_stored_query_request.GetStoredQueryRequest = {
            "query_name": query_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_aggregate_discovered_resources(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        resource_type: "capo_config_service.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.resource_filters.ResourceFilters"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.list_aggregate_discovered_resources_response.ListAggregateDiscoveredResourcesResponse":
        """<p>Accepts a resource type and returns a list of resource identifiers that are aggregated for a specific resource type across accounts and regions. A resource identifier includes the resource type, ID, (if available) the custom resource name, source account, and source region. You can narrow the results to include only resources that have specific resource IDs, or a resource name, or source account ID, or source region.</p> <p>For example, if the input consists of accountID 12345678910 and the region is us-east-1 for resource type <code>AWS::EC2::Instance</code> then the API returns all the EC2 instance identifiers of accountID 12345678910 and region us-east-1.</p>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator. </p>
            resource_type: <p>The type of resources that you want Config to list in the response.</p>
            filters: <p>Filters the results based on the <code>ResourceFilters</code> object.</p>
            limit: <p>The maximum number of resource identifiers returned on each page. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.list_aggregate_discovered_resources_request.ListAggregateDiscoveredResourcesRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.list_aggregate_discovered_resources_response.ListAggregateDiscoveredResourcesResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.list_aggregate_discovered_resources

            output, http_response = (
                capo_config_service._operations.starling_dove_service.list_aggregate_discovered_resources.list_aggregate_discovered_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.list_aggregate_discovered_resources_request.ListAggregateDiscoveredResourcesRequest = {
            "configuration_aggregator_name": configuration_aggregator_name,
            "resource_type": resource_type,
        }
        if filters is not None:
            input_["filters"] = filters
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_aggregate_discovered_resources(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        resource_type: "capo_config_service.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.resource_filters.ResourceFilters"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.aggregate_resource_identifier.AggregateResourceIdentifier]":
        _token = next_token
        while True:
            _response = self.list_aggregate_discovered_resources(
                configuration_aggregator_name,
                resource_type,
                config_overrides=config_overrides,
                filters=filters,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_identifiers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_configuration_recorders(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.configuration_recorder_filter_list.ConfigurationRecorderFilterList"
        ] = None,
        max_results: Optional[
            "capo_config_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.list_configuration_recorders_response.ListConfigurationRecordersResponse":
        """<p>Returns a list of configuration recorders depending on the filters you specify.</p>

        Args:
            filters: <p>Filters the results based on a list of <code>ConfigurationRecorderFilter</code> objects that you specify.</p>
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The <code>NextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.list_configuration_recorders_request.ListConfigurationRecordersRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.list_configuration_recorders_response.ListConfigurationRecordersResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.list_configuration_recorders

            output, http_response = (
                capo_config_service._operations.starling_dove_service.list_configuration_recorders.list_configuration_recorders(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.list_configuration_recorders_request.ListConfigurationRecordersRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_configuration_recorders(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.configuration_recorder_filter_list.ConfigurationRecorderFilterList"
        ] = None,
        max_results: Optional[
            "capo_config_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.configuration_recorder_summary.ConfigurationRecorderSummary]":
        _token = next_token
        while True:
            _response = self.list_configuration_recorders(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("configuration_recorder_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_conformance_pack_compliance_scores(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.conformance_pack_compliance_scores_filters.ConformancePackComplianceScoresFilters"
        ] = None,
        sort_order: Optional["capo_config_service.types.sort_order.SortOrder"] = None,
        sort_by: Optional["capo_config_service.types.sort_by.SortBy"] = None,
        limit: Optional[
            "capo_config_service.types.page_size_limit.PageSizeLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.list_conformance_pack_compliance_scores_response.ListConformancePackComplianceScoresResponse":
        """<p>Returns a list of conformance pack compliance scores. A compliance score is the percentage of the number of compliant rule-resource combinations in a conformance pack compared to the number of total possible rule-resource combinations in the conformance pack. This metric provides you with a high-level view of the compliance state of your conformance packs. You can use it to identify, investigate, and understand the level of compliance in your conformance packs.</p> <note> <p>Conformance packs with no evaluation results will have a compliance score of <code>INSUFFICIENT_DATA</code>.</p> </note>

        Args:
            filters: <p>Filters the results based on the <code>ConformancePackComplianceScoresFilters</code>.</p>
            sort_order: <p>Determines the order in which conformance pack compliance scores are sorted. Either in ascending or descending order.</p> <p>By default, conformance pack compliance scores are sorted in alphabetical order by name of the conformance pack. Conformance pack compliance scores are sorted in reverse alphabetical order if you enter <code>DESCENDING</code>.</p> <p>You can sort conformance pack compliance scores by the numerical value of the compliance score by entering <code>SCORE</code> in the <code>SortBy</code> action. When compliance scores are sorted by <code>SCORE</code>, conformance packs with a compliance score of <code>INSUFFICIENT_DATA</code> will be last when sorting by ascending order and first when sorting by descending order.</p>
            sort_by: <p>Sorts your conformance pack compliance scores in either ascending or descending order, depending on <code>SortOrder</code>.</p> <p>By default, conformance pack compliance scores are sorted in alphabetical order by name of the conformance pack. Enter <code>SCORE</code>, to sort conformance pack compliance scores by the numerical value of the compliance score.</p>
            limit: <p>The maximum number of conformance pack compliance scores returned on each page.</p>
            next_token: <p>The <code>nextToken</code> string in a prior request that you can use to get the paginated response for the next set of conformance pack compliance scores.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.list_conformance_pack_compliance_scores_request.ListConformancePackComplianceScoresRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.list_conformance_pack_compliance_scores_response.ListConformancePackComplianceScoresResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.list_conformance_pack_compliance_scores

            output, http_response = (
                capo_config_service._operations.starling_dove_service.list_conformance_pack_compliance_scores.list_conformance_pack_compliance_scores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.list_conformance_pack_compliance_scores_request.ListConformancePackComplianceScoresRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_conformance_pack_compliance_scores(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.conformance_pack_compliance_scores_filters.ConformancePackComplianceScoresFilters"
        ] = None,
        sort_order: Optional["capo_config_service.types.sort_order.SortOrder"] = None,
        sort_by: Optional["capo_config_service.types.sort_by.SortBy"] = None,
        limit: Optional[
            "capo_config_service.types.page_size_limit.PageSizeLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.list_conformance_pack_compliance_scores_response.ListConformancePackComplianceScoresResponse]":
        _token = next_token
        while True:
            _response = self.list_conformance_pack_compliance_scores(
                config_overrides=config_overrides,
                filters=filters,
                sort_order=sort_order,
                sort_by=sort_by,
                limit=limit,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_connectors(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        max_results: Optional[
            "capo_config_service.types.list_connectors_max_results.ListConnectorsMaxResults"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        filters: Optional[
            "capo_config_service.types.connector_filter_list.ConnectorFilterList"
        ] = None,
    ) -> "capo_config_service.types.list_connectors_response.ListConnectorsResponse":
        """<p>Returns a list of connectors depending on the filters you specify.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The <code>NextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>
            filters: <p>Filters the results based on a list of <code>ConnectorFilter</code> objects that you specify.</p>

        Raises:
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.list_connectors_request.ListConnectorsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.list_connectors

            output, http_response = (
                capo_config_service._operations.starling_dove_service.list_connectors.list_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.list_connectors_request.ListConnectorsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_connectors(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        max_results: Optional[
            "capo_config_service.types.list_connectors_max_results.ListConnectorsMaxResults"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        filters: Optional[
            "capo_config_service.types.connector_filter_list.ConnectorFilterList"
        ] = None,
    ) -> "Iterator[capo_config_service.types.connector_summary.ConnectorSummary]":
        _token = next_token
        while True:
            _response = self.list_connectors(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("connector_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_discovered_resources(
        self,
        resource_type: "capo_config_service.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_ids: Optional[
            "capo_config_service.types.resource_id_list.ResourceIdList"
        ] = None,
        resource_name: Optional[
            "capo_config_service.types.resource_name.ResourceName"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        include_deleted_resources: Optional[
            "capo_config_service.types.boolean.Boolean"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.list_discovered_resources_response.ListDiscoveredResourcesResponse":
        """<p>Returns a list of resource resource identifiers for the specified resource types for the resources of that type. A <i>resource identifier</i> includes the resource type, ID, and (if available) the custom resource name.</p> <p>The results consist of resources that Config has <i>discovered</i>, including those that Config is not currently recording. You can narrow the results to include only resources that have specific resource IDs or a resource name.</p> <note> <p>You can specify either resource IDs or a resource name, but not both, in the same request.</p> </note> <important> <p> <i>CloudFormation stack recording behavior in Config</i> </p> <p>When a CloudFormation stack fails to create (for example, it enters the <code>ROLLBACK_FAILED</code> state), Config does not record a configuration item (CI) for that stack. Configuration items are only recorded for stacks that reach the following states:</p> <ul> <li> <p> <code>CREATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_ROLLBACK_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_ROLLBACK_FAILED</code> </p> </li> <li> <p> <code>DELETE_FAILED</code> </p> </li> <li> <p> <code>DELETE_COMPLETE</code> </p> </li> </ul> <p>Because no CI is created for a failed stack creation, you won't see configuration history for that stack in Config, even after the stack is deleted. This helps make sure that Config only tracks resources that were successfully provisioned.</p> </important>

        Args:
            resource_type: <p>The type of resources that you want Config to list in the response.</p>
            resource_ids: <p>The IDs of only those resources that you want Config to list in the response. If you do not specify this parameter, Config lists all resources of the specified type that it has discovered. You can list a minimum of 1 resourceID and a maximum of 20 resourceIds.</p>
            resource_name: <p>The custom name of only those resources that you want Config to list in the response. If you do not specify this parameter, Config lists all resources of the specified type that it has discovered.</p>
            limit: <p>The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>
            include_deleted_resources: <p>Specifies whether Config includes deleted resources in the results. By default, deleted resources are not included.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_available_configuration_recorder_exception.NoAvailableConfigurationRecorderException: <p>There are no customer managed configuration recorders available to record your resources. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html">PutConfigurationRecorder</a> operation to create the customer managed configuration recorder.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.list_discovered_resources_request.ListDiscoveredResourcesRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.list_discovered_resources_response.ListDiscoveredResourcesResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.list_discovered_resources

            output, http_response = (
                capo_config_service._operations.starling_dove_service.list_discovered_resources.list_discovered_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.list_discovered_resources_request.ListDiscoveredResourcesRequest = {
            "resource_type": resource_type
        }
        if resource_ids is not None:
            input_["resource_ids"] = resource_ids
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if limit is not None:
            input_["limit"] = limit
        if include_deleted_resources is not None:
            input_["include_deleted_resources"] = include_deleted_resources
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_discovered_resources(
        self,
        resource_type: "capo_config_service.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_ids: Optional[
            "capo_config_service.types.resource_id_list.ResourceIdList"
        ] = None,
        resource_name: Optional[
            "capo_config_service.types.resource_name.ResourceName"
        ] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        include_deleted_resources: Optional[
            "capo_config_service.types.boolean.Boolean"
        ] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.resource_identifier.ResourceIdentifier]":
        _token = next_token
        while True:
            _response = self.list_discovered_resources(
                resource_type,
                config_overrides=config_overrides,
                resource_ids=resource_ids,
                resource_name=resource_name,
                limit=limit,
                include_deleted_resources=include_deleted_resources,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_identifiers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_evaluations(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.resource_evaluation_filters.ResourceEvaluationFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.list_resource_evaluations_page_item_limit.ListResourceEvaluationsPageItemLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "capo_config_service.types.list_resource_evaluations_response.ListResourceEvaluationsResponse":
        """<p>Returns a list of proactive resource evaluations.</p>

        Args:
            filters: <p>Returns a <code>ResourceEvaluationFilters</code> object.</p>
            limit: <p>The maximum number of evaluations returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>

        Raises:
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.invalid_time_range_exception.InvalidTimeRangeException: <p>The specified time range is not valid. The earlier time is not chronologically before the later time.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.list_resource_evaluations_request.ListResourceEvaluationsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.list_resource_evaluations_response.ListResourceEvaluationsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.list_resource_evaluations

            output, http_response = (
                capo_config_service._operations.starling_dove_service.list_resource_evaluations.list_resource_evaluations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.list_resource_evaluations_request.ListResourceEvaluationsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_resource_evaluations(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        filters: Optional[
            "capo_config_service.types.resource_evaluation_filters.ResourceEvaluationFilters"
        ] = None,
        limit: Optional[
            "capo_config_service.types.list_resource_evaluations_page_item_limit.ListResourceEvaluationsPageItemLimit"
        ] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
    ) -> "Iterator[capo_config_service.types.resource_evaluation.ResourceEvaluation]":
        _token = next_token
        while True:
            _response = self.list_resource_evaluations(
                config_overrides=config_overrides,
                filters=filters,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_evaluations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stored_queries(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        max_results: Optional["capo_config_service.types.limit.Limit"] = None,
    ) -> "capo_config_service.types.list_stored_queries_response.ListStoredQueriesResponse":
        """<p>Lists the stored queries for a single Amazon Web Services account and a single Amazon Web Services Region. The default is 100. </p>

        Args:
            next_token: <p>The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.</p>
            max_results: <p>The maximum number of results to be returned with a single call.</p>

        Raises:
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.list_stored_queries_request.ListStoredQueriesRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.list_stored_queries_response.ListStoredQueriesResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.list_stored_queries

            output, http_response = (
                capo_config_service._operations.starling_dove_service.list_stored_queries.list_stored_queries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.list_stored_queries_request.ListStoredQueriesRequest = {}
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

    def iter_list_stored_queries(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        next_token: Optional["capo_config_service.types.string.String"] = None,
        max_results: Optional["capo_config_service.types.limit.Limit"] = None,
    ) -> "Iterator[capo_config_service.types.list_stored_queries_response.ListStoredQueriesResponse]":
        _token = next_token
        while True:
            _response = self.list_stored_queries(
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
        resource_arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List the tags for Config resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. The following resources are supported:</p> <ul> <li> <p> <code>ConfigurationRecorder</code> </p> </li> <li> <p> <code>ConfigRule</code> </p> </li> <li> <p> <code>OrganizationConfigRule</code> </p> </li> <li> <p> <code>ConformancePack</code> </p> </li> <li> <p> <code>OrganizationConformancePack</code> </p> </li> <li> <p> <code>ConfigurationAggregator</code> </p> </li> <li> <p> <code>AggregationAuthorization</code> </p> </li> <li> <p> <code>StoredQuery</code> </p> </li> <li> <p> <code>Connector</code> </p> </li> </ul>
            limit: <p>The maximum number of tags returned on each page. The limit maximum is 50. You cannot specify a number greater than 50. If you specify 0, Config uses the default. </p>
            next_token: <p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>

        Raises:
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>You have specified a resource that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.list_tags_for_resource

            output, http_response = (
                capo_config_service._operations.starling_dove_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.tag.Tag]":
        _token = next_token
        while True:
            _response = self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_aggregation_authorization(
        self,
        authorized_account_id: "capo_config_service.types.account_id.AccountId",
        authorized_aws_region: "capo_config_service.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        tags: Optional["capo_config_service.types.tags_list.TagsList"] = None,
    ) -> "capo_config_service.types.put_aggregation_authorization_response.PutAggregationAuthorizationResponse":
        """<p>Authorizes the aggregator account and region to collect data from the source account and region. </p> <note> <p> <b>Tags are added at creation and cannot be updated with this operation</b> </p> <p> <code>PutAggregationAuthorization</code> is an idempotent API. Subsequent requests won’t create a duplicate resource if one was already created. If a following request has different <code>tags</code> values, Config will ignore these differences and treat it as an idempotent request of the previous. In this case, <code>tags</code> will not be updated, even if they are different.</p> <p>Use <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html">TagResource</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html">UntagResource</a> to update tags after creation.</p> </note>

        Args:
            authorized_account_id: <p>The 12-digit account ID of the account authorized to aggregate data.</p>
            authorized_aws_region: <p>The region authorized to collect aggregated data.</p>
            tags: <p>An array of tag object.</p>

        Raises:
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_aggregation_authorization_request.PutAggregationAuthorizationRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_aggregation_authorization_response.PutAggregationAuthorizationResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_aggregation_authorization

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_aggregation_authorization.put_aggregation_authorization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_aggregation_authorization_request.PutAggregationAuthorizationRequest = {
            "authorized_account_id": authorized_account_id,
            "authorized_aws_region": authorized_aws_region,
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

    def put_config_rule(
        self,
        config_rule: "capo_config_service.types.config_rule.ConfigRule",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        tags: Optional["capo_config_service.types.tags_list.TagsList"] = None,
    ) -> None:
        """<p>Adds or updates an Config rule to evaluate if your Amazon Web Services resources comply with your desired configurations. For information on how many Config rules you can have per account, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html"> <b>Service Limits</b> </a> in the <i>Config Developer Guide</i>.</p> <p>There are two types of rules: <i>Config Managed Rules</i> and <i>Config Custom Rules</i>. You can use <code>PutConfigRule</code> to create both Config Managed Rules and Config Custom Rules.</p> <p>Config Managed Rules are predefined, customizable rules created by Config. For a list of managed rules, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html">List of Config Managed Rules</a>. If you are adding an Config managed rule, you must specify the rule's identifier for the <code>SourceIdentifier</code> key.</p> <p>Config Custom Rules are rules that you create from scratch. There are two ways to create Config custom rules: with Lambda functions (<a href="https://docs.aws.amazon.com/config/latest/developerguide/gettingstarted-concepts.html#gettingstarted-concepts-function"> Lambda Developer Guide</a>) and with Guard (<a href="https://github.com/aws-cloudformation/cloudformation-guard">Guard GitHub Repository</a>), a policy-as-code language. Config custom rules created with Lambda are called <i>Config Custom Lambda Rules</i> and Config custom rules created with Guard are called <i>Config Custom Policy Rules</i>.</p> <p>If you are adding a new Config Custom Lambda rule, you first need to create an Lambda function that the rule invokes to evaluate your resources. When you use <code>PutConfigRule</code> to add a Custom Lambda rule to Config, you must specify the Amazon Resource Name (ARN) that Lambda assigns to the function. You specify the ARN in the <code>SourceIdentifier</code> key. This key is part of the <code>Source</code> object, which is part of the <code>ConfigRule</code> object. </p> <p>For any new Config rule that you add, specify the <code>ConfigRuleName</code> in the <code>ConfigRule</code> object. Do not specify the <code>ConfigRuleArn</code> or the <code>ConfigRuleId</code>. These values are generated by Config for new rules.</p> <p>If you are updating a rule that you added previously, you can specify the rule by <code>ConfigRuleName</code>, <code>ConfigRuleId</code>, or <code>ConfigRuleArn</code> in the <code>ConfigRule</code> data type that you use in this request.</p> <p>For more information about developing and using Config rules, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html">Evaluating Resources with Config Rules</a> in the <i>Config Developer Guide</i>.</p> <note> <p> <b>Tags are added at creation and cannot be updated with this operation</b> </p> <p> <code>PutConfigRule</code> is an idempotent API. Subsequent requests won’t create a duplicate resource if one was already created. If a following request has different <code>tags</code> values, Config will ignore these differences and treat it as an idempotent request of the previous. In this case, <code>tags</code> will not be updated, even if they are different.</p> <p>Use <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html">TagResource</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html">UntagResource</a> to update tags after creation.</p> </note>

        Args:
            config_rule: <p>The rule that you want to add to your account.</p>
            tags: <p>An array of tag object.</p>

        Raises:
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.max_number_of_config_rules_exceeded_exception.MaxNumberOfConfigRulesExceededException: <p>Failed to add the Config rule because the account already contains the maximum number of 1000 rules. Consider deleting any deactivated rules before you add new rules.</p>
            capo_config_service.errors.no_available_configuration_recorder_exception.NoAvailableConfigurationRecorderException: <p>There are no customer managed configuration recorders available to record your resources. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html">PutConfigurationRecorder</a> operation to create the customer managed configuration recorder.</p>
            capo_config_service.errors.resource_in_use_exception.ResourceInUseException: <p>You see this exception in the following cases: </p> <ul> <li> <p>For DeleteConfigRule, Config is deleting this rule. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, a remediation action is associated with the rule and Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.</p> </li> <li> <p>For PutConfigOrganizationRule, organization Config rule deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteOrganizationConfigRule, organization Config rule creation is in progress. Try your request again later.</p> </li> <li> <p>For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_config_rule_request.PutConfigRuleRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.put_config_rule

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_config_rule.put_config_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_config_rule_request.PutConfigRuleRequest = {
            "config_rule": config_rule
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

    def put_configuration_aggregator(
        self,
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        account_aggregation_sources: Optional[
            "capo_config_service.types.account_aggregation_source_list.AccountAggregationSourceList"
        ] = None,
        organization_aggregation_source: Optional[
            "capo_config_service.types.organization_aggregation_source.OrganizationAggregationSource"
        ] = None,
        tags: Optional["capo_config_service.types.tags_list.TagsList"] = None,
        aggregator_filters: Optional[
            "capo_config_service.types.aggregator_filters.AggregatorFilters"
        ] = None,
    ) -> "capo_config_service.types.put_configuration_aggregator_response.PutConfigurationAggregatorResponse":
        """<p>Creates and updates the configuration aggregator with the selected source accounts and regions. The source account can be individual account(s) or an organization.</p> <p> <code>accountIds</code> that are passed will be replaced with existing accounts. If you want to add additional accounts into the aggregator, call <code>DescribeConfigurationAggregators</code> to get the previous accounts and then append new ones.</p> <note> <p>Config should be enabled in source accounts and regions you want to aggregate.</p> <p>If your source type is an organization, you must be signed in to the management account or a registered delegated administrator and all the features must be enabled in your organization. If the caller is a management account, Config calls <code>EnableAwsServiceAccess</code> API to enable integration between Config and Organizations. If the caller is a registered delegated administrator, Config calls <code>ListDelegatedAdministrators</code> API to verify whether the caller is a valid delegated administrator.</p> <p>To register a delegated administrator, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/set-up-aggregator-cli.html#register-a-delegated-administrator-cli">Register a Delegated Administrator</a> in the <i>Config developer guide</i>. </p> </note> <note> <p> <b>Tags are added at creation and cannot be updated with this operation</b> </p> <p> <code>PutConfigurationAggregator</code> is an idempotent API. Subsequent requests won’t create a duplicate resource if one was already created. If a following request has different <code>tags</code> values, Config will ignore these differences and treat it as an idempotent request of the previous. In this case, <code>tags</code> will not be updated, even if they are different.</p> <p>Use <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html">TagResource</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html">UntagResource</a> to update tags after creation.</p> </note>

        Args:
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>
            account_aggregation_sources: <p>A list of AccountAggregationSource object. </p>
            organization_aggregation_source: <p>An OrganizationAggregationSource object.</p>
            tags: <p>An array of tag object.</p>
            aggregator_filters: <p>An object to filter configuration recorders in an aggregator. Either <code>ResourceType</code> or <code>ServicePrincipal</code> is required.</p>

        Raises:
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.invalid_role_exception.InvalidRoleException: <p>You have provided a null or empty Amazon Resource Name (ARN) for the IAM role assumed by Config and used by the customer managed configuration recorder.</p>
            capo_config_service.errors.limit_exceeded_exception.LimitExceededException: <p>For <code>PutServiceLinkedConfigurationRecorder</code> API, this exception is thrown if the number of service-linked roles in the account exceeds the limit.</p> <p>For <code>StartConfigRulesEvaluation</code> API, this exception is thrown if an evaluation is in progress or if you call the <a>StartConfigRulesEvaluation</a> API more than once per minute.</p> <p>For <code>PutConfigurationAggregator</code> API, this exception is thrown if the number of accounts and aggregators exceeds the limit.</p>
            capo_config_service.errors.no_available_organization_exception.NoAvailableOrganizationException: <p>Organization is no longer available.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.organization_all_features_not_enabled_exception.OrganizationAllFeaturesNotEnabledException: <p>Config resource cannot be created because your organization does not have all features enabled.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_configuration_aggregator_request.PutConfigurationAggregatorRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_configuration_aggregator_response.PutConfigurationAggregatorResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_configuration_aggregator

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_configuration_aggregator.put_configuration_aggregator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_configuration_aggregator_request.PutConfigurationAggregatorRequest = {
            "configuration_aggregator_name": configuration_aggregator_name
        }
        if account_aggregation_sources is not None:
            input_["account_aggregation_sources"] = account_aggregation_sources
        if organization_aggregation_source is not None:
            input_["organization_aggregation_source"] = organization_aggregation_source
        if tags is not None:
            input_["tags"] = tags
        if aggregator_filters is not None:
            input_["aggregator_filters"] = aggregator_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_configuration_recorder(
        self,
        configuration_recorder: "capo_config_service.types.configuration_recorder.ConfigurationRecorder",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        tags: Optional["capo_config_service.types.tags_list.TagsList"] = None,
    ) -> None:
        """<p>Creates or updates the customer managed configuration recorder.</p> <p>You can use this operation to create a new customer managed configuration recorder or to update the <code>roleARN</code> and the <code>recordingGroup</code> for an existing customer managed configuration recorder.</p> <p>To start the customer managed configuration recorder and begin recording configuration changes for the resource types you specify, use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigurationRecorder.html">StartConfigurationRecorder</a> operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html"> <b>Working with the Configuration Recorder</b> </a> in the <i>Config Developer Guide</i>.</p> <note> <p> <b>One customer managed configuration recorder per account per Region</b> </p> <p>You can create only one customer managed configuration recorder for each account for each Amazon Web Services Region.</p> <p> <b>Default is to record all supported resource types, excluding the global IAM resource types</b> </p> <p>If you have not specified values for the <code>recordingGroup</code> field, the default for the customer managed configuration recorder is to record all supported resource types, excluding the global IAM resource types: <code>AWS::IAM::Group</code>, <code>AWS::IAM::Policy</code>, <code>AWS::IAM::Role</code>, and <code>AWS::IAM::User</code>.</p> <p> <b>Tags are added at creation and cannot be updated</b> </p> <p> <code>PutConfigurationRecorder</code> is an idempotent API. Subsequent requests won’t create a duplicate resource if one was already created. If a following request has different tags values, Config will ignore these differences and treat it as an idempotent request of the previous. In this case, tags will not be updated, even if they are different.</p> <p>Use <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html">TagResource</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html">UntagResource</a> to update tags after creation.</p> </note>

        Args:
            configuration_recorder: <p>An object for the configuration recorder. A configuration recorder records configuration changes for the resource types in scope.</p>
            tags: <p>The tags for the customer managed configuration recorder. Each tag consists of a key and an optional value, both of which you define.</p>

        Raises:
            capo_config_service.errors.invalid_configuration_recorder_name_exception.InvalidConfigurationRecorderNameException: <p>The configuration recorder name is not valid. The prefix "<code>AWSConfigurationRecorderFor</code>" is reserved for service-linked configuration recorders.</p>
            capo_config_service.errors.invalid_recording_group_exception.InvalidRecordingGroupException: <p>One of the following errors:</p> <ul> <li> <p>You have provided a combination of parameter values that is not valid. For example:</p> <ul> <li> <p>Setting the <code>allSupported</code> field of <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html">RecordingGroup</a> to <code>true</code>, but providing a non-empty list for the <code>resourceTypes</code>field of <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html">RecordingGroup</a>.</p> </li> <li> <p>Setting the <code>allSupported</code> field of <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html">RecordingGroup</a> to <code>true</code>, but also setting the <code>useOnly</code> field of <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html">RecordingStrategy</a> to <code>EXCLUSION_BY_RESOURCE_TYPES</code>.</p> </li> </ul> </li> <li> <p>Every parameter is either null, false, or empty.</p> </li> <li> <p>You have reached the limit of the number of resource types you can provide for the recording group.</p> </li> <li> <p>You have provided resource types or a recording strategy that are not valid.</p> </li> </ul>
            capo_config_service.errors.invalid_role_exception.InvalidRoleException: <p>You have provided a null or empty Amazon Resource Name (ARN) for the IAM role assumed by Config and used by the customer managed configuration recorder.</p>
            capo_config_service.errors.max_number_of_configuration_recorders_exceeded_exception.MaxNumberOfConfigurationRecordersExceededException: <p>You have reached the limit of the number of configuration recorders you can create.</p>
            capo_config_service.errors.unmodifiable_entity_exception.UnmodifiableEntityException: <p>The requested operation is not valid.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html">PutConfigurationRecorder</a>, you will see this exception because you cannot use this operation to create a service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a> operation to create a service-linked configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigurationRecorder.html">DeleteConfigurationRecorder</a>, you will see this exception because you cannot use this operation to delete a service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a> operation to delete a service-linked configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigurationRecorder.html">StartConfigurationRecorder</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html">StopConfigurationRecorder</a>, you will see this exception because these operations do not affect service-linked configuration recorders. Service-linked configuration recorders are always recording. To stop recording, you must delete the service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a> operation to delete a service-linked configuration recorder.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_configuration_recorder_request.PutConfigurationRecorderRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.put_configuration_recorder

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_configuration_recorder.put_configuration_recorder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_configuration_recorder_request.PutConfigurationRecorderRequest = {
            "configuration_recorder": configuration_recorder
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

    def put_conformance_pack(
        self,
        conformance_pack_name: "capo_config_service.types.conformance_pack_name.ConformancePackName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        template_s3_uri: Optional[
            "capo_config_service.types.template_s3_uri.TemplateS3Uri"
        ] = None,
        template_body: Optional[
            "capo_config_service.types.template_body.TemplateBody"
        ] = None,
        delivery_s3_bucket: Optional[
            "capo_config_service.types.delivery_s3_bucket.DeliveryS3Bucket"
        ] = None,
        delivery_s3_key_prefix: Optional[
            "capo_config_service.types.delivery_s3_key_prefix.DeliveryS3KeyPrefix"
        ] = None,
        conformance_pack_input_parameters: Optional[
            "capo_config_service.types.conformance_pack_input_parameters.ConformancePackInputParameters"
        ] = None,
        template_ssm_document_details: Optional[
            "capo_config_service.types.template_ssm_document_details.TemplateSSMDocumentDetails"
        ] = None,
        tags: Optional["capo_config_service.types.tags_list.TagsList"] = None,
    ) -> "capo_config_service.types.put_conformance_pack_response.PutConformancePackResponse":
        """<p>Creates or updates a conformance pack. A conformance pack is a collection of Config rules that can be easily deployed in an account and a region and across an organization. For information on how many conformance packs you can have per account, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html"> <b>Service Limits</b> </a> in the <i>Config Developer Guide</i>.</p> <important> <p>When you use <code>PutConformancePack</code> to deploy conformance packs in your account, the operation can create Config rules and remediation actions without requiring <code>config:PutConfigRule</code> or <code>config:PutRemediationConfigurations</code> permissions in your account IAM policies.</p> <p>This API uses the <code>AWSServiceRoleForConfigConforms</code> service-linked role in your account to create conformance pack resources. This service-linked role includes the permissions to create Config rules and remediation configurations, even if your account IAM policies explicitly deny these actions.</p> </important> <p>This API creates a service-linked role <code>AWSServiceRoleForConfigConforms</code> in your account. The service-linked role is created only when the role does not exist in your account. </p> <note> <p>You must specify only one of the follow parameters: <code>TemplateS3Uri</code>, <code>TemplateBody</code> or <code>TemplateSSMDocumentDetails</code>.</p> </note> <note> <p> <b>Tags are added at creation and cannot be updated with this operation</b> </p> <p> <code>PutConformancePack</code> is an idempotent API. Subsequent requests won't create a duplicate resource if one was already created. If a following request has different <code>tags</code> values, Config will ignore these differences and treat it as an idempotent request of the previous. In this case, <code>tags</code> will not be updated, even if they are different.</p> <p>Use <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html">TagResource</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html">UntagResource</a> to update tags after creation.</p> </note>

        Args:
            conformance_pack_name: <p>The unique name of the conformance pack you want to deploy.</p>
            template_s3_uri: <p>The location of the file containing the template body (<code>s3://bucketname/prefix</code>). The uri must point to a conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket in the same Region as the conformance pack. </p> <note> <p>You must have access to read Amazon S3 bucket. In addition, in order to ensure a successful deployment, the template object must not be in an <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html">archived storage class</a> if this parameter is passed.</p> </note>
            template_body: <p>A string that contains the full conformance pack template body. The structure containing the template body has a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <note> <p>You can use a YAML template with two resource types: Config rule (<code>AWS::Config::ConfigRule</code>) and remediation action (<code>AWS::Config::RemediationConfiguration</code>).</p> </note>
            delivery_s3_bucket: <p>The name of the Amazon S3 bucket where Config stores conformance pack templates.</p> <note> <p>This field is optional.</p> </note>
            delivery_s3_key_prefix: <p>The prefix for the Amazon S3 bucket. </p> <note> <p>This field is optional.</p> </note>
            conformance_pack_input_parameters: <p>A list of <code>ConformancePackInputParameter</code> objects.</p>
            template_ssm_document_details: <p>An object of type <code>TemplateSSMDocumentDetails</code>, which contains the name or the Amazon Resource Name (ARN) of the Amazon Web Services Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.</p>
            tags: <p>The tags for the conformance pack. Each tag consists of a key and an optional value, both of which you define.</p>

        Raises:
            capo_config_service.errors.conformance_pack_template_validation_exception.ConformancePackTemplateValidationException: <p>You have specified a template that is not valid or supported.</p>
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.max_number_of_conformance_packs_exceeded_exception.MaxNumberOfConformancePacksExceededException: <p>You have reached the limit of the number of conformance packs you can create in an account. For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html"> <b>Service Limits</b> </a> in the <i>Config Developer Guide</i>.</p>
            capo_config_service.errors.resource_in_use_exception.ResourceInUseException: <p>You see this exception in the following cases: </p> <ul> <li> <p>For DeleteConfigRule, Config is deleting this rule. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, a remediation action is associated with the rule and Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.</p> </li> <li> <p>For PutConfigOrganizationRule, organization Config rule deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteOrganizationConfigRule, organization Config rule creation is in progress. Try your request again later.</p> </li> <li> <p>For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_conformance_pack_request.PutConformancePackRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_conformance_pack_response.PutConformancePackResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_conformance_pack

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_conformance_pack.put_conformance_pack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_conformance_pack_request.PutConformancePackRequest = {
            "conformance_pack_name": conformance_pack_name
        }
        if template_s3_uri is not None:
            input_["template_s3_uri"] = template_s3_uri
        if template_body is not None:
            input_["template_body"] = template_body
        if delivery_s3_bucket is not None:
            input_["delivery_s3_bucket"] = delivery_s3_bucket
        if delivery_s3_key_prefix is not None:
            input_["delivery_s3_key_prefix"] = delivery_s3_key_prefix
        if conformance_pack_input_parameters is not None:
            input_["conformance_pack_input_parameters"] = (
                conformance_pack_input_parameters
            )
        if template_ssm_document_details is not None:
            input_["template_ssm_document_details"] = template_ssm_document_details
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_connector(
        self,
        connector_configuration: "capo_config_service.types.connector_configuration.ConnectorConfiguration",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        tags: Optional["capo_config_service.types.tags_list.TagsList"] = None,
    ) -> "capo_config_service.types.put_connector_response.PutConnectorResponse":
        """<p>Creates a connector that specifies the connection between a third-party cloud service provider and Config.</p> <p>A connector is required to create a service-linked configuration recorder for a third-party cloud service provider using the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a> operation.</p> <p>This API creates a service-linked role <code>AWSServiceRoleForConfigThirdParty</code> in your account. The service-linked role is created only when the role does not exist in your account.</p> <note> <p> <b>Connectors cannot be updated</b> </p> <p>To update the connector configuration, you must delete all associated configuration recorders, delete the connector, and recreate it with the updated configuration.</p> </note> <note> <p> <b>Tags are added at creation and cannot be updated with this operation</b> </p> <p>Use <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html">TagResource</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html">UntagResource</a> to update tags after creation.</p> </note>

        Args:
            connector_configuration: <p>The provider-specific configuration for connecting to the third-party cloud service provider.</p>
            tags: <p>The tags for the connector. Each tag consists of a key and an optional value, both of which you define.</p>

        Raises:
            capo_config_service.errors.conflict_exception.ConflictException: <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because a service-linked recorder already exists for the specified service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because the specified service principal does not support multiple configuration recorders and one already exists.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector or service principal. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, you cannot create a connector because a connector already exists for the specified connector configuration.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, you cannot delete the service-linked recorder because it is currently in use by the linked Amazon Web Services service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConnector.html">DeleteConnector</a>, another in-progress operation is currently referencing the connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteDeliveryChannel.html">DeleteDeliveryChannel</a>, you cannot delete the specified delivery channel because the customer managed configuration recorder is running. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html">StopConfigurationRecorder</a> operation to stop the customer managed configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>For service-linked configuration recorders, the configuration recorder is not in use by the service. No association or dissociation of resource types is permitted.</p> </li> <li> <p>For service-linked configuration recorders, your requested change to the configuration recorder has been denied by its linked Amazon Web Services service.</p> </li> </ul>
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.max_number_of_connectors_exceeded_exception.MaxNumberOfConnectorsExceededException: <p>You have reached the limit of the number of connectors in your account.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_connector_request.PutConnectorRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_connector_response.PutConnectorResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_connector

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_connector.put_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_connector_request.PutConnectorRequest = {
            "connector_configuration": connector_configuration
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

    def put_delivery_channel(
        self,
        delivery_channel: "capo_config_service.types.delivery_channel.DeliveryChannel",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Creates or updates a delivery channel to deliver configuration information and other compliance information.</p> <p>You can use this operation to create a new delivery channel or to update the Amazon S3 bucket and the Amazon SNS topic of an existing delivery channel.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html"> <b>Working with the Delivery Channel</b> </a> in the <i>Config Developer Guide.</i> </p> <note> <p> <b>One delivery channel per account per Region</b> </p> <p>You can have only one delivery channel for each account for each Amazon Web Services Region.</p> </note>

        Args:
            delivery_channel: <p>An object for the delivery channel. A delivery channel sends notifications and updated configuration states. </p>

        Raises:
            capo_config_service.errors.insufficient_delivery_policy_exception.InsufficientDeliveryPolicyException: <p>Your Amazon S3 bucket policy does not allow Config to write to it.</p>
            capo_config_service.errors.invalid_delivery_channel_name_exception.InvalidDeliveryChannelNameException: <p>The specified delivery channel name is not valid.</p>
            capo_config_service.errors.invalid_s3_key_prefix_exception.InvalidS3KeyPrefixException: <p>The specified Amazon S3 key prefix is not valid.</p>
            capo_config_service.errors.invalid_s3_kms_key_arn_exception.InvalidS3KmsKeyArnException: <p>The specified Amazon KMS Key ARN is not valid.</p>
            capo_config_service.errors.invalid_sns_topic_arn_exception.InvalidSNSTopicARNException: <p>The specified Amazon SNS topic does not exist.</p>
            capo_config_service.errors.max_number_of_delivery_channels_exceeded_exception.MaxNumberOfDeliveryChannelsExceededException: <p>You have reached the limit of the number of delivery channels you can create.</p>
            capo_config_service.errors.no_available_configuration_recorder_exception.NoAvailableConfigurationRecorderException: <p>There are no customer managed configuration recorders available to record your resources. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html">PutConfigurationRecorder</a> operation to create the customer managed configuration recorder.</p>
            capo_config_service.errors.no_such_bucket_exception.NoSuchBucketException: <p>The specified Amazon S3 bucket does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_delivery_channel_request.PutDeliveryChannelRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.put_delivery_channel

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_delivery_channel.put_delivery_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_delivery_channel_request.PutDeliveryChannelRequest = {
            "delivery_channel": delivery_channel
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_evaluations(
        self,
        result_token: "capo_config_service.types.string.String",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        evaluations: Optional[
            "capo_config_service.types.evaluations.Evaluations"
        ] = None,
        test_mode: Optional["capo_config_service.types.boolean.Boolean"] = None,
    ) -> "capo_config_service.types.put_evaluations_response.PutEvaluationsResponse":
        """<p>Used by an Lambda function to deliver evaluation results to Config. This operation is required in every Lambda function that is invoked by an Config rule.</p>

        Args:
            evaluations: <p>The assessments that the Lambda function performs. Each evaluation identifies an Amazon Web Services resource and indicates whether it complies with the Config rule that invokes the Lambda function.</p>
            result_token: <p>An encrypted token that associates an evaluation with an Config rule. Identifies the rule and the event that triggered the evaluation.</p>
            test_mode: <p>Use this parameter to specify a test run for <code>PutEvaluations</code>. You can verify whether your Lambda function will deliver evaluation results to Config. No updates occur to your existing evaluations, and evaluation results are not sent to Config.</p> <note> <p>When <code>TestMode</code> is <code>true</code>, <code>PutEvaluations</code> doesn't require a valid value for the <code>ResultToken</code> parameter, but the value cannot be null.</p> </note>

        Raises:
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.invalid_result_token_exception.InvalidResultTokenException: <p>The specified <code>ResultToken</code> is not valid.</p>
            capo_config_service.errors.no_such_config_rule_exception.NoSuchConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_evaluations_request.PutEvaluationsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_evaluations_response.PutEvaluationsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_evaluations

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_evaluations.put_evaluations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_evaluations_request.PutEvaluationsRequest = {
            "result_token": result_token
        }
        if evaluations is not None:
            input_["evaluations"] = evaluations
        if test_mode is not None:
            input_["test_mode"] = test_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_external_evaluation(
        self,
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        external_evaluation: "capo_config_service.types.external_evaluation.ExternalEvaluation",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.put_external_evaluation_response.PutExternalEvaluationResponse":
        """<p>Add or updates the evaluations for process checks. This API checks if the rule is a process check when the name of the Config rule is provided.</p>

        Args:
            config_rule_name: <p>The name of the Config rule.</p>
            external_evaluation: <p>An <code>ExternalEvaluation</code> object that provides details about compliance.</p>

        Raises:
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_config_rule_exception.NoSuchConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_external_evaluation_request.PutExternalEvaluationRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_external_evaluation_response.PutExternalEvaluationResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_external_evaluation

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_external_evaluation.put_external_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_external_evaluation_request.PutExternalEvaluationRequest = {
            "config_rule_name": config_rule_name,
            "external_evaluation": external_evaluation,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_organization_config_rule(
        self,
        organization_config_rule_name: "capo_config_service.types.organization_config_rule_name.OrganizationConfigRuleName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        organization_managed_rule_metadata: Optional[
            "capo_config_service.types.organization_managed_rule_metadata.OrganizationManagedRuleMetadata"
        ] = None,
        organization_custom_rule_metadata: Optional[
            "capo_config_service.types.organization_custom_rule_metadata.OrganizationCustomRuleMetadata"
        ] = None,
        excluded_accounts: Optional[
            "capo_config_service.types.excluded_accounts.ExcludedAccounts"
        ] = None,
        organization_custom_policy_rule_metadata: Optional[
            "capo_config_service.types.organization_custom_policy_rule_metadata.OrganizationCustomPolicyRuleMetadata"
        ] = None,
        tags: Optional["capo_config_service.types.tags_list.TagsList"] = None,
    ) -> "capo_config_service.types.put_organization_config_rule_response.PutOrganizationConfigRuleResponse":
        """<p>Adds or updates an Config rule for your entire organization to evaluate if your Amazon Web Services resources comply with your desired configurations. For information on how many organization Config rules you can have per account, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html"> <b>Service Limits</b> </a> in the <i>Config Developer Guide</i>.</p> <p> Only a management account and a delegated administrator can create or update an organization Config rule. When calling this API with a delegated administrator, you must ensure Organizations <code>ListDelegatedAdministrator</code> permissions are added. An organization can have up to 3 delegated administrators.</p> <p>This API enables organization service access through the <code>EnableAWSServiceAccess</code> action and creates a service-linked role <code>AWSServiceRoleForConfigMultiAccountSetup</code> in the management or delegated administrator account of your organization. The service-linked role is created only when the role does not exist in the caller account. Config verifies the existence of role with <code>GetRole</code> action.</p> <p>To use this API with delegated administrator, register a delegated administrator by calling Amazon Web Services Organization <code>register-delegated-administrator</code> for <code>config-multiaccountsetup.amazonaws.com</code>. </p> <p>There are two types of rules: <i>Config Managed Rules</i> and <i>Config Custom Rules</i>. You can use <code>PutOrganizationConfigRule</code> to create both Config Managed Rules and Config Custom Rules.</p> <p>Config Managed Rules are predefined, customizable rules created by Config. For a list of managed rules, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html">List of Config Managed Rules</a>. If you are adding an Config managed rule, you must specify the rule's identifier for the <code>RuleIdentifier</code> key.</p> <p>Config Custom Rules are rules that you create from scratch. There are two ways to create Config custom rules: with Lambda functions (<a href="https://docs.aws.amazon.com/config/latest/developerguide/gettingstarted-concepts.html#gettingstarted-concepts-function"> Lambda Developer Guide</a>) and with Guard (<a href="https://github.com/aws-cloudformation/cloudformation-guard">Guard GitHub Repository</a>), a policy-as-code language. Config custom rules created with Lambda are called <i>Config Custom Lambda Rules</i> and Config custom rules created with Guard are called <i>Config Custom Policy Rules</i>.</p> <p>If you are adding a new Config Custom Lambda rule, you first need to create an Lambda function in the management account or a delegated administrator that the rule invokes to evaluate your resources. You also need to create an IAM role in the managed account that can be assumed by the Lambda function. When you use <code>PutOrganizationConfigRule</code> to add a Custom Lambda rule to Config, you must specify the Amazon Resource Name (ARN) that Lambda assigns to the function.</p> <note> <p>Prerequisite: Ensure you call <code>EnableAllFeatures</code> API to enable all features in an organization.</p> <p>Make sure to specify one of either <code>OrganizationCustomPolicyRuleMetadata</code> for Custom Policy rules, <code>OrganizationCustomRuleMetadata</code> for Custom Lambda rules, or <code>OrganizationManagedRuleMetadata</code> for managed rules.</p> </note>

        Args:
            organization_config_rule_name: <p>The name that you assign to an organization Config rule.</p>
            organization_managed_rule_metadata: <p>An <code>OrganizationManagedRuleMetadata</code> object. This object specifies organization managed rule metadata such as resource type and ID of Amazon Web Services resource along with the rule identifier. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.</p>
            organization_custom_rule_metadata: <p>An <code>OrganizationCustomRuleMetadata</code> object. This object specifies organization custom rule metadata such as resource type, resource ID of Amazon Web Services resource, Lambda function ARN, and organization trigger types that trigger Config to evaluate your Amazon Web Services resources against a rule. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.</p>
            excluded_accounts: <p>A comma-separated list of accounts that you want to exclude from an organization Config rule.</p>
            organization_custom_policy_rule_metadata: <p>An <code>OrganizationCustomPolicyRuleMetadata</code> object. This object specifies metadata for your organization's Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of Amazon Web Services resource, and organization trigger types that initiate Config to evaluate Amazon Web Services resources against a rule.</p>
            tags: <p>The tags for the organization Config rule. Each tag consists of a key and an optional value, both of which you define.</p>

        Raises:
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.max_number_of_organization_config_rules_exceeded_exception.MaxNumberOfOrganizationConfigRulesExceededException: <p>You have reached the limit of the number of organization Config rules you can create. For more information, see see <a href="https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html"> <b>Service Limits</b> </a> in the <i>Config Developer Guide</i>.</p>
            capo_config_service.errors.no_available_organization_exception.NoAvailableOrganizationException: <p>Organization is no longer available.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.organization_all_features_not_enabled_exception.OrganizationAllFeaturesNotEnabledException: <p>Config resource cannot be created because your organization does not have all features enabled.</p>
            capo_config_service.errors.resource_in_use_exception.ResourceInUseException: <p>You see this exception in the following cases: </p> <ul> <li> <p>For DeleteConfigRule, Config is deleting this rule. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, a remediation action is associated with the rule and Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.</p> </li> <li> <p>For PutConfigOrganizationRule, organization Config rule deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteOrganizationConfigRule, organization Config rule creation is in progress. Try your request again later.</p> </li> <li> <p>For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> </ul>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_organization_config_rule_request.PutOrganizationConfigRuleRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_organization_config_rule_response.PutOrganizationConfigRuleResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_organization_config_rule

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_organization_config_rule.put_organization_config_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_organization_config_rule_request.PutOrganizationConfigRuleRequest = {
            "organization_config_rule_name": organization_config_rule_name
        }
        if organization_managed_rule_metadata is not None:
            input_["organization_managed_rule_metadata"] = (
                organization_managed_rule_metadata
            )
        if organization_custom_rule_metadata is not None:
            input_["organization_custom_rule_metadata"] = (
                organization_custom_rule_metadata
            )
        if excluded_accounts is not None:
            input_["excluded_accounts"] = excluded_accounts
        if organization_custom_policy_rule_metadata is not None:
            input_["organization_custom_policy_rule_metadata"] = (
                organization_custom_policy_rule_metadata
            )
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_organization_conformance_pack(
        self,
        organization_conformance_pack_name: "capo_config_service.types.organization_conformance_pack_name.OrganizationConformancePackName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        template_s3_uri: Optional[
            "capo_config_service.types.template_s3_uri.TemplateS3Uri"
        ] = None,
        template_body: Optional[
            "capo_config_service.types.template_body.TemplateBody"
        ] = None,
        delivery_s3_bucket: Optional[
            "capo_config_service.types.delivery_s3_bucket.DeliveryS3Bucket"
        ] = None,
        delivery_s3_key_prefix: Optional[
            "capo_config_service.types.delivery_s3_key_prefix.DeliveryS3KeyPrefix"
        ] = None,
        conformance_pack_input_parameters: Optional[
            "capo_config_service.types.conformance_pack_input_parameters.ConformancePackInputParameters"
        ] = None,
        excluded_accounts: Optional[
            "capo_config_service.types.excluded_accounts.ExcludedAccounts"
        ] = None,
        tags: Optional["capo_config_service.types.tags_list.TagsList"] = None,
    ) -> "capo_config_service.types.put_organization_conformance_pack_response.PutOrganizationConformancePackResponse":
        """<p>Deploys conformance packs across member accounts in an Amazon Web Services Organization. For information on how many organization conformance packs and how many Config rules you can have per account, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html"> <b>Service Limits</b> </a> in the <i>Config Developer Guide</i>.</p> <p>Only a management account and a delegated administrator can call this API. When calling this API with a delegated administrator, you must ensure Organizations <code>ListDelegatedAdministrator</code> permissions are added. An organization can have up to 3 delegated administrators.</p> <important> <p>When you use <code>PutOrganizationConformancePack</code> to deploy conformance packs across member accounts, the operation can create Config rules and remediation actions without requiring <code>config:PutConfigRule</code> or <code>config:PutRemediationConfigurations</code> permissions in member account IAM policies.</p> <p>This API uses the <code>AWSServiceRoleForConfigConforms</code> service-linked role in each member account to create conformance pack resources. This service-linked role includes the permissions to create Config rules and remediation configurations, even if member account IAM policies explicitly deny these actions.</p> </important> <p>This API enables organization service access for <code>config-multiaccountsetup.amazonaws.com</code> through the <code>EnableAWSServiceAccess</code> action and creates a service-linked role <code>AWSServiceRoleForConfigMultiAccountSetup</code> in the management or delegated administrator account of your organization. The service-linked role is created only when the role does not exist in the caller account. To use this API with delegated administrator, register a delegated administrator by calling Amazon Web Services Organization <code>register-delegate-admin</code> for <code>config-multiaccountsetup.amazonaws.com</code>.</p> <note> <p>Prerequisite: Ensure you call <code>EnableAllFeatures</code> API to enable all features in an organization.</p> <p>You must specify either the <code>TemplateS3Uri</code> or the <code>TemplateBody</code> parameter, but not both. If you provide both Config uses the <code>TemplateS3Uri</code> parameter and ignores the <code>TemplateBody</code> parameter.</p> <p>Config sets the state of a conformance pack to CREATE_IN_PROGRESS and UPDATE_IN_PROGRESS until the conformance pack is created or updated. You cannot update a conformance pack while it is in this state.</p> </note>

        Args:
            organization_conformance_pack_name: <p>Name of the organization conformance pack you want to create.</p>
            template_s3_uri: <p>Location of file containing the template body. The uri must point to the conformance pack template (max size: 300 KB).</p> <note> <p>You must have access to read Amazon S3 bucket. In addition, in order to ensure a successful deployment, the template object must not be in an <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html">archived storage class</a> if this parameter is passed.</p> </note>
            template_body: <p>A string that contains the full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p>
            delivery_s3_bucket: <p>The name of the Amazon S3 bucket where Config stores conformance pack templates.</p> <note> <p>This field is optional. If used, it must be prefixed with <code>awsconfigconforms</code>.</p> </note>
            delivery_s3_key_prefix: <p>The prefix for the Amazon S3 bucket.</p> <note> <p>This field is optional.</p> </note>
            conformance_pack_input_parameters: <p>A list of <code>ConformancePackInputParameter</code> objects.</p>
            excluded_accounts: <p>A list of Amazon Web Services accounts to be excluded from an organization conformance pack while deploying a conformance pack.</p>
            tags: <p>The tags for the organization conformance pack. Each tag consists of a key and an optional value, both of which you define.</p>

        Raises:
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.max_number_of_organization_conformance_packs_exceeded_exception.MaxNumberOfOrganizationConformancePacksExceededException: <p>You have reached the limit of the number of organization conformance packs you can create in an account. For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html"> <b>Service Limits</b> </a> in the <i>Config Developer Guide</i>.</p>
            capo_config_service.errors.no_available_organization_exception.NoAvailableOrganizationException: <p>Organization is no longer available.</p>
            capo_config_service.errors.organization_access_denied_exception.OrganizationAccessDeniedException: <p>For <code>PutConfigurationAggregator</code> API, you can see this exception for the following reasons:</p> <ul> <li> <p>No permission to call <code>EnableAWSServiceAccess</code> API</p> </li> <li> <p>The configuration aggregator cannot be updated because your Amazon Web Services Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>The configuration aggregator is associated with a previous Amazon Web Services Organization and Config cannot aggregate data with current Amazon Web Services Organization. Delete this aggregator and create a new one with the current Amazon Web Services Organization.</p> </li> <li> <p>You are not a registered delegated administrator for Config with permissions to call <code>ListDelegatedAdministrators</code> API. Ensure that the management account registers delagated administrator for Config service principal name before the delegated administrator creates an aggregator.</p> </li> </ul> <p>For all <code>OrganizationConfigRule</code> and <code>OrganizationConformancePack</code> APIs, Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.</p>
            capo_config_service.errors.organization_all_features_not_enabled_exception.OrganizationAllFeaturesNotEnabledException: <p>Config resource cannot be created because your organization does not have all features enabled.</p>
            capo_config_service.errors.organization_conformance_pack_template_validation_exception.OrganizationConformancePackTemplateValidationException: <p>You have specified a template that is not valid or supported.</p>
            capo_config_service.errors.resource_in_use_exception.ResourceInUseException: <p>You see this exception in the following cases: </p> <ul> <li> <p>For DeleteConfigRule, Config is deleting this rule. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, a remediation action is associated with the rule and Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.</p> </li> <li> <p>For PutConfigOrganizationRule, organization Config rule deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteOrganizationConfigRule, organization Config rule creation is in progress. Try your request again later.</p> </li> <li> <p>For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> </ul>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_organization_conformance_pack_request.PutOrganizationConformancePackRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_organization_conformance_pack_response.PutOrganizationConformancePackResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_organization_conformance_pack

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_organization_conformance_pack.put_organization_conformance_pack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_organization_conformance_pack_request.PutOrganizationConformancePackRequest = {
            "organization_conformance_pack_name": organization_conformance_pack_name
        }
        if template_s3_uri is not None:
            input_["template_s3_uri"] = template_s3_uri
        if template_body is not None:
            input_["template_body"] = template_body
        if delivery_s3_bucket is not None:
            input_["delivery_s3_bucket"] = delivery_s3_bucket
        if delivery_s3_key_prefix is not None:
            input_["delivery_s3_key_prefix"] = delivery_s3_key_prefix
        if conformance_pack_input_parameters is not None:
            input_["conformance_pack_input_parameters"] = (
                conformance_pack_input_parameters
            )
        if excluded_accounts is not None:
            input_["excluded_accounts"] = excluded_accounts
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_remediation_configurations(
        self,
        remediation_configurations: "capo_config_service.types.remediation_configurations.RemediationConfigurations",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.put_remediation_configurations_response.PutRemediationConfigurationsResponse":
        """<p>Adds or updates the remediation configuration with a specific Config rule with the selected target or action. The API creates the <code>RemediationConfiguration</code> object for the Config rule. The Config rule must already exist for you to add a remediation configuration. The target (SSM document) must exist and have permissions to use the target. </p> <note> <p> <b>Be aware of backward incompatible changes</b> </p> <p>If you make backward incompatible changes to the SSM document, you must call this again to ensure the remediations can run.</p> <p>This API does not support adding remediation configurations for service-linked Config Rules such as Organization Config rules, the rules deployed by conformance packs, and rules deployed by Amazon Web Services Security Hub.</p> </note> <note> <p> <b>Required fields</b> </p> <p>For manual remediation configuration, you need to provide a value for <code>automationAssumeRole</code> or use a value in the <code>assumeRole</code>field to remediate your resources. The SSM automation document can use either as long as it maps to a valid parameter.</p> <p>However, for automatic remediation configuration, the only valid <code>assumeRole</code> field value is <code>AutomationAssumeRole</code> and you need to provide a value for <code>AutomationAssumeRole</code> to remediate your resources.</p> </note> <note> <p> <b>Auto remediation can be initiated even for compliant resources</b> </p> <p>If you enable auto remediation for a specific Config rule using the <a href="https://docs.aws.amazon.com/config/latest/APIReference/emAPI_PutRemediationConfigurations.html">PutRemediationConfigurations</a> API or the Config console, it initiates the remediation process for all non-compliant resources for that specific rule. The auto remediation process relies on the compliance data snapshot which is captured on a periodic basis. Any non-compliant resource that is updated between the snapshot schedule will continue to be remediated based on the last known compliance data snapshot.</p> <p>This means that in some cases auto remediation can be initiated even for compliant resources, since the bootstrap processor uses a database that can have stale evaluation results based on the last known compliance data snapshot.</p> </note>

        Args:
            remediation_configurations: <p>A list of remediation configuration objects.</p>

        Raises:
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_remediation_configurations_request.PutRemediationConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_remediation_configurations_response.PutRemediationConfigurationsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_remediation_configurations

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_remediation_configurations.put_remediation_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_remediation_configurations_request.PutRemediationConfigurationsRequest = {
            "remediation_configurations": remediation_configurations
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_remediation_exceptions(
        self,
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        resource_keys: "capo_config_service.types.remediation_exception_resource_keys.RemediationExceptionResourceKeys",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        message: Optional[
            "capo_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
        ] = None,
        expiration_time: Optional["capo_config_service.types.date.Date"] = None,
    ) -> "capo_config_service.types.put_remediation_exceptions_response.PutRemediationExceptionsResponse":
        """<p>A remediation exception is when a specified resource is no longer considered for auto-remediation. This API adds a new exception or updates an existing exception for a specified resource with a specified Config rule. </p> <note> <p> <b>Exceptions block auto remediation</b> </p> <p>Config generates a remediation exception when a problem occurs running a remediation action for a specified resource. Remediation exceptions blocks auto-remediation until the exception is cleared.</p> </note> <note> <p> <b>Manual remediation is recommended when placing an exception</b> </p> <p>When placing an exception on an Amazon Web Services resource, it is recommended that remediation is set as manual remediation until the given Config rule for the specified resource evaluates the resource as <code>NON_COMPLIANT</code>. Once the resource has been evaluated as <code>NON_COMPLIANT</code>, you can add remediation exceptions and change the remediation type back from Manual to Auto if you want to use auto-remediation. Otherwise, using auto-remediation before a <code>NON_COMPLIANT</code> evaluation result can delete resources before the exception is applied.</p> </note> <note> <p> <b>Exceptions can only be performed on non-compliant resources</b> </p> <p>Placing an exception can only be performed on resources that are <code>NON_COMPLIANT</code>. If you use this API for <code>COMPLIANT</code> resources or resources that are <code>NOT_APPLICABLE</code>, a remediation exception will not be generated. For more information on the conditions that initiate the possible Config evaluation results, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#aws-config-rules">Concepts | Config Rules</a> in the <i>Config Developer Guide</i>.</p> </note> <note> <p> <b>Exceptions cannot be placed on service-linked remediation actions</b> </p> <p>You cannot place an exception on service-linked remediation actions, such as remediation actions put by an organizational conformance pack.</p> </note> <note> <p> <b>Auto remediation can be initiated even for compliant resources</b> </p> <p>If you enable auto remediation for a specific Config rule using the <a href="https://docs.aws.amazon.com/config/latest/APIReference/emAPI_PutRemediationConfigurations.html">PutRemediationConfigurations</a> API or the Config console, it initiates the remediation process for all non-compliant resources for that specific rule. The auto remediation process relies on the compliance data snapshot which is captured on a periodic basis. Any non-compliant resource that is updated between the snapshot schedule will continue to be remediated based on the last known compliance data snapshot.</p> <p>This means that in some cases auto remediation can be initiated even for compliant resources, since the bootstrap processor uses a database that can have stale evaluation results based on the last known compliance data snapshot.</p> </note>

        Args:
            config_rule_name: <p>The name of the Config rule for which you want to create remediation exception.</p>
            resource_keys: <p>An exception list of resource exception keys to be processed with the current request. Config adds exception for each resource key. For example, Config adds 3 exceptions for 3 resource keys. </p>
            message: <p>The message contains an explanation of the exception.</p>
            expiration_time: <p>The exception is automatically deleted after the expiration date.</p>

        Raises:
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_remediation_exceptions_request.PutRemediationExceptionsRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_remediation_exceptions_response.PutRemediationExceptionsResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_remediation_exceptions

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_remediation_exceptions.put_remediation_exceptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_remediation_exceptions_request.PutRemediationExceptionsRequest = {
            "config_rule_name": config_rule_name,
            "resource_keys": resource_keys,
        }
        if message is not None:
            input_["message"] = message
        if expiration_time is not None:
            input_["expiration_time"] = expiration_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_config(
        self,
        resource_type: "capo_config_service.types.resource_type_string.ResourceTypeString",
        schema_version_id: "capo_config_service.types.schema_version_id.SchemaVersionId",
        resource_id: "capo_config_service.types.resource_id.ResourceId",
        configuration: "capo_config_service.types.configuration.Configuration",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        resource_name: Optional[
            "capo_config_service.types.resource_name.ResourceName"
        ] = None,
        tags: Optional["capo_config_service.types.tags.Tags"] = None,
    ) -> None:
        """<p>Records the configuration state for the resource provided in the request. The configuration state of a resource is represented in Config as Configuration Items. Once this API records the configuration item, you can retrieve the list of configuration items for the custom resource type using existing Config APIs. </p> <note> <p>The custom resource type must be registered with CloudFormation. This API accepts the configuration item registered with CloudFormation.</p> <p>When you call this API, Config only stores configuration state of the resource provided in the request. This API does not change or remediate the configuration of the resource. </p> <p>Write-only schema properites are not recorded as part of the published configuration item.</p> </note>

        Args:
            resource_type: <p>The type of the resource. The custom resource type must be registered with CloudFormation. </p> <note> <p>You cannot use the organization names “amzn”, “amazon”, “alexa”, “custom” with custom resource types. It is the first part of the ResourceType up to the first ::.</p> </note>
            schema_version_id: <p>Version of the schema registered for the ResourceType in CloudFormation.</p>
            resource_id: <p>Unique identifier of the resource.</p>
            resource_name: <p>Name of the resource.</p>
            configuration: <p>The configuration object of the resource in valid JSON format. It must match the schema registered with CloudFormation.</p> <note> <p>The configuration JSON must not exceed 64 KB.</p> </note>
            tags: <p>Tags associated with the resource.</p> <note> <p>This field is not to be confused with the Amazon Web Services-wide tag feature for Amazon Web Services resources. Tags for <code>PutResourceConfig</code> are tags that you supply for the configuration items of your custom resources.</p> </note>

        Raises:
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.max_active_resources_exceeded_exception.MaxActiveResourcesExceededException: <p>You have reached the limit of active custom resource types in your account. There is a limit of 100,000. Delete unused resources using <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteResourceConfig.html">DeleteResourceConfig</a> <code></code>.</p>
            capo_config_service.errors.no_running_configuration_recorder_exception.NoRunningConfigurationRecorderException: <p>There is no configuration recorder running.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_resource_config_request.PutResourceConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.put_resource_config

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_resource_config.put_resource_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_resource_config_request.PutResourceConfigRequest = {
            "resource_type": resource_type,
            "schema_version_id": schema_version_id,
            "resource_id": resource_id,
            "configuration": configuration,
        }
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_retention_configuration(
        self,
        retention_period_in_days: "capo_config_service.types.retention_period_in_days.RetentionPeriodInDays",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.put_retention_configuration_response.PutRetentionConfigurationResponse":
        """<p>Creates and updates the retention configuration with details about retention period (number of days) that Config stores your historical information. The API creates the <code>RetentionConfiguration</code> object and names the object as <b>default</b>. When you have a <code>RetentionConfiguration</code> object named <b>default</b>, calling the API modifies the default object. </p> <note> <p>Currently, Config supports only one retention configuration per region in your account.</p> </note>

        Args:
            retention_period_in_days: <p>Number of days Config stores your historical information.</p> <note> <p>Currently, only applicable to the configuration item history.</p> </note>

        Raises:
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.max_number_of_retention_configurations_exceeded_exception.MaxNumberOfRetentionConfigurationsExceededException: <p>Failed to add the retention configuration because a retention configuration with that name already exists.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_retention_configuration_request.PutRetentionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_retention_configuration_response.PutRetentionConfigurationResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_retention_configuration

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_retention_configuration.put_retention_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_retention_configuration_request.PutRetentionConfigurationRequest = {
            "retention_period_in_days": retention_period_in_days
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_service_linked_configuration_recorder(
        self,
        service_principal: "capo_config_service.types.service_principal.ServicePrincipal",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        tags: Optional["capo_config_service.types.tags_list.TagsList"] = None,
    ) -> "capo_config_service.types.put_service_linked_configuration_recorder_response.PutServiceLinkedConfigurationRecorderResponse":
        """<p>Creates a service-linked configuration recorder that is linked to a specific Amazon Web Services service based on the <code>ServicePrincipal</code> you specify.</p> <p>The configuration recorder's <code>name</code>, <code>recordingGroup</code>, <code>recordingMode</code>, and <code>recordingScope</code> is set by the service that is linked to the configuration recorder.</p> <p>For more information and a list of supported services/service principals, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html"> <b>Working with the Configuration Recorder</b> </a> in the <i>Config Developer Guide</i>.</p> <p>This API creates a service-linked role <code>AWSServiceRoleForConfig</code> in your account. The service-linked role is created only when the role does not exist in your account.</p> <note> <p> <b>The recording scope determines if you receive configuration items</b> </p> <p>The recording scope is set by the service that is linked to the configuration recorder and determines whether you receive configuration items (CIs) in the delivery channel. If the recording scope is internal, you will not receive CIs in the delivery channel.</p> <p> <b>Tags are added at creation and cannot be updated with this operation</b> </p> <p>Use <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html">TagResource</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html">UntagResource</a> to update tags after creation.</p> </note>

        Args:
            service_principal: <p>The service principal of the Amazon Web Services service for the service-linked configuration recorder that you want to create.</p>
            tags: <p>The tags for a service-linked configuration recorder. Each tag consists of a key and an optional value, both of which you define.</p>

        Raises:
            capo_config_service.errors.conflict_exception.ConflictException: <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because a service-linked recorder already exists for the specified service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because the specified service principal does not support multiple configuration recorders and one already exists.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector or service principal. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, you cannot create a connector because a connector already exists for the specified connector configuration.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, you cannot delete the service-linked recorder because it is currently in use by the linked Amazon Web Services service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConnector.html">DeleteConnector</a>, another in-progress operation is currently referencing the connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteDeliveryChannel.html">DeleteDeliveryChannel</a>, you cannot delete the specified delivery channel because the customer managed configuration recorder is running. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html">StopConfigurationRecorder</a> operation to stop the customer managed configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>For service-linked configuration recorders, the configuration recorder is not in use by the service. No association or dissociation of resource types is permitted.</p> </li> <li> <p>For service-linked configuration recorders, your requested change to the configuration recorder has been denied by its linked Amazon Web Services service.</p> </li> </ul>
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.limit_exceeded_exception.LimitExceededException: <p>For <code>PutServiceLinkedConfigurationRecorder</code> API, this exception is thrown if the number of service-linked roles in the account exceeds the limit.</p> <p>For <code>StartConfigRulesEvaluation</code> API, this exception is thrown if an evaluation is in progress or if you call the <a>StartConfigRulesEvaluation</a> API more than once per minute.</p> <p>For <code>PutConfigurationAggregator</code> API, this exception is thrown if the number of accounts and aggregators exceeds the limit.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_service_linked_configuration_recorder_request.PutServiceLinkedConfigurationRecorderRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_service_linked_configuration_recorder_response.PutServiceLinkedConfigurationRecorderResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_service_linked_configuration_recorder

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_service_linked_configuration_recorder.put_service_linked_configuration_recorder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_service_linked_configuration_recorder_request.PutServiceLinkedConfigurationRecorderRequest = {
            "service_principal": service_principal
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

    def put_stored_query(
        self,
        stored_query: "capo_config_service.types.stored_query.StoredQuery",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        tags: Optional["capo_config_service.types.tags_list.TagsList"] = None,
    ) -> "capo_config_service.types.put_stored_query_response.PutStoredQueryResponse":
        """<p>Saves a new query or updates an existing saved query. The <code>QueryName</code> must be unique for a single Amazon Web Services account and a single Amazon Web Services Region. You can create upto 300 queries in a single Amazon Web Services account and a single Amazon Web Services Region.</p> <note> <p> <b>Tags are added at creation and cannot be updated</b> </p> <p> <code>PutStoredQuery</code> is an idempotent API. Subsequent requests won’t create a duplicate resource if one was already created. If a following request has different <code>tags</code> values, Config will ignore these differences and treat it as an idempotent request of the previous. In this case, <code>tags</code> will not be updated, even if they are different.</p> </note>

        Args:
            stored_query: <p>A list of <code>StoredQuery</code> objects. The mandatory fields are <code>QueryName</code> and <code>Expression</code>.</p> <note> <p>When you are creating a query, you must provide a query name and an expression. When you are updating a query, you must provide a query name but updating the description is optional.</p> </note>
            tags: <p>A list of <code>Tags</code> object.</p>

        Raises:
            capo_config_service.errors.resource_concurrent_modification_exception.ResourceConcurrentModificationException: <p>Two users are trying to modify the same query at the same time. Wait for a moment and try again.</p>
            capo_config_service.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit of the number of tags you can use. For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html"> <b>Service Limits</b> </a> in the <i>Config Developer Guide</i>.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_stored_query_request.PutStoredQueryRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_stored_query_response.PutStoredQueryResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_stored_query

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_stored_query.put_stored_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_stored_query_request.PutStoredQueryRequest = {
            "stored_query": stored_query
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

    def put_third_party_service_linked_configuration_recorder(
        self,
        service_principal: "capo_config_service.types.service_principal.ServicePrincipal",
        connector_arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName",
        scope_configuration: "capo_config_service.types.scope_configuration.ScopeConfiguration",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        tags: Optional["capo_config_service.types.tags_list.TagsList"] = None,
    ) -> "capo_config_service.types.put_third_party_service_linked_configuration_recorder_response.PutThirdPartyServiceLinkedConfigurationRecorderResponse":
        """<p>Creates or updates a service-linked configuration recorder that is linked to a third-party cloud service provider based on the <code>ConnectorArn</code> you specify.</p> <p>The configuration recorder's <code>name</code>, <code>recordingGroup</code>, <code>recordingMode</code>, and <code>recordingScope</code> is set by the service that is linked to the configuration recorder.</p> <p>If a service-linked configuration recorder already exists for the specified service principal and connector, calling this operation again updates the <code>ScopeConfiguration</code>.</p> <note> <p> <b>This operation can only be called by the Amazon Web Services service linked to the configuration recorder</b> </p> <p>Customers cannot call this operation directly. Only the linked Amazon Web Services service can create or update the service-linked configuration recorder.</p> </note> <note> <p> <b>Tags are added at creation and cannot be updated with this operation</b> </p> <p>Use <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html">TagResource</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html">UntagResource</a> to update tags after creation.</p> </note>

        Args:
            service_principal: <p>The service principal of the Amazon Web Services service for the service-linked configuration recorder that you want to create.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector that specifies the connection between the third-party cloud service provider and Config. The specified connector must exist.</p>
            scope_configuration: <p>Specifies the scope of resources to record from the third-party cloud service provider.</p>
            tags: <p>The tags for a service-linked configuration recorder. Each tag consists of a key and an optional value, both of which you define.</p>

        Raises:
            capo_config_service.errors.conflict_exception.ConflictException: <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because a service-linked recorder already exists for the specified service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, you cannot create a service-linked recorder because the specified service principal does not support multiple configuration recorders and one already exists.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutThirdPartyServiceLinkedConfigurationRecorder.html">PutThirdPartyServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector or service principal. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, you cannot create a connector because a connector already exists for the specified connector configuration.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, you cannot delete the service-linked recorder because it is currently in use by the linked Amazon Web Services service.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, another in-progress operation is currently referencing the same connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConnector.html">DeleteConnector</a>, another in-progress operation is currently referencing the connector. Please try again later.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteDeliveryChannel.html">DeleteDeliveryChannel</a>, you cannot delete the specified delivery channel because the customer managed configuration recorder is running. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html">StopConfigurationRecorder</a> operation to stop the customer managed configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>For service-linked configuration recorders, the configuration recorder is not in use by the service. No association or dissociation of resource types is permitted.</p> </li> <li> <p>For service-linked configuration recorders, your requested change to the configuration recorder has been denied by its linked Amazon Web Services service.</p> </li> </ul>
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.put_third_party_service_linked_configuration_recorder_request.PutThirdPartyServiceLinkedConfigurationRecorderRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.put_third_party_service_linked_configuration_recorder_response.PutThirdPartyServiceLinkedConfigurationRecorderResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.put_third_party_service_linked_configuration_recorder

            output, http_response = (
                capo_config_service._operations.starling_dove_service.put_third_party_service_linked_configuration_recorder.put_third_party_service_linked_configuration_recorder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.put_third_party_service_linked_configuration_recorder_request.PutThirdPartyServiceLinkedConfigurationRecorderRequest = {
            "service_principal": service_principal,
            "connector_arn": connector_arn,
            "scope_configuration": scope_configuration,
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

    def select_aggregate_resource_config(
        self,
        expression: "capo_config_service.types.expression.Expression",
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        max_results: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.select_aggregate_resource_config_response.SelectAggregateResourceConfigResponse":
        """<p>Accepts a structured query language (SQL) SELECT command and an aggregator to query configuration state of Amazon Web Services resources across multiple accounts and regions, performs the corresponding search, and returns resource configurations matching the properties.</p> <p>For more information about query components, see the <a href="https://docs.aws.amazon.com/config/latest/developerguide/query-components.html"> <b>Query Components</b> </a> section in the <i>Config Developer Guide</i>.</p> <note> <p>If you run an aggregation query (i.e., using <code>GROUP BY</code> or using aggregate functions such as <code>COUNT</code>; e.g., <code>SELECT resourceId, COUNT(*) WHERE resourceType = 'AWS::IAM::Role' GROUP BY resourceId</code>) and do not specify the <code>MaxResults</code> or the <code>Limit</code> query parameters, the default page size is set to 500.</p> <p>If you run a non-aggregation query (i.e., not using <code>GROUP BY</code> or aggregate function; e.g., <code>SELECT * WHERE resourceType = 'AWS::IAM::Role'</code>) and do not specify the <code>MaxResults</code> or the <code>Limit</code> query parameters, the default page size is set to 25.</p> </note>

        Args:
            expression: <p>The SQL query SELECT command. </p>
            configuration_aggregator_name: <p>The name of the configuration aggregator.</p>
            limit: <p>The maximum number of query results returned on each page. </p>
            max_results: <p>The maximum number of query results returned on each page. Config also allows the Limit request parameter.</p>
            next_token: <p>The nextToken string returned in a previous request that you use to request the next page of results in a paginated response. </p>

        Raises:
            capo_config_service.errors.invalid_expression_exception.InvalidExpressionException: <p>The syntax of the query is incorrect.</p>
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.no_such_configuration_aggregator_exception.NoSuchConfigurationAggregatorException: <p>You have specified a configuration aggregator that does not exist.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.select_aggregate_resource_config_request.SelectAggregateResourceConfigRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.select_aggregate_resource_config_response.SelectAggregateResourceConfigResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.select_aggregate_resource_config

            output, http_response = (
                capo_config_service._operations.starling_dove_service.select_aggregate_resource_config.select_aggregate_resource_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.select_aggregate_resource_config_request.SelectAggregateResourceConfigRequest = {
            "expression": expression,
            "configuration_aggregator_name": configuration_aggregator_name,
        }
        if limit is not None:
            input_["limit"] = limit
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

    def iter_select_aggregate_resource_config(
        self,
        expression: "capo_config_service.types.expression.Expression",
        configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        max_results: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.string.String]":
        _token = next_token
        while True:
            _response = self.select_aggregate_resource_config(
                expression,
                configuration_aggregator_name,
                config_overrides=config_overrides,
                limit=limit,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def select_resource_config(
        self,
        expression: "capo_config_service.types.expression.Expression",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "capo_config_service.types.select_resource_config_response.SelectResourceConfigResponse":
        """<p>Accepts a structured query language (SQL) <code>SELECT</code> command, performs the corresponding search, and returns resource configurations matching the properties.</p> <p>For more information about query components, see the <a href="https://docs.aws.amazon.com/config/latest/developerguide/query-components.html"> <b>Query Components</b> </a> section in the <i>Config Developer Guide</i>.</p>

        Args:
            expression: <p>The SQL query <code>SELECT</code> command.</p>
            limit: <p>The maximum number of query results returned on each page. </p>
            next_token: <p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response. </p>

        Raises:
            capo_config_service.errors.invalid_expression_exception.InvalidExpressionException: <p>The syntax of the query is incorrect.</p>
            capo_config_service.errors.invalid_limit_exception.InvalidLimitException: <p>The specified limit is outside the allowable range.</p>
            capo_config_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified next token is not valid. Specify the <code>nextToken</code> string that was returned in the previous response to get the next page of results.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.select_resource_config_request.SelectResourceConfigRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.select_resource_config_response.SelectResourceConfigResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.select_resource_config

            output, http_response = (
                capo_config_service._operations.starling_dove_service.select_resource_config.select_resource_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.select_resource_config_request.SelectResourceConfigRequest = {
            "expression": expression
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_select_resource_config(
        self,
        expression: "capo_config_service.types.expression.Expression",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        limit: Optional["capo_config_service.types.limit.Limit"] = None,
        next_token: Optional["capo_config_service.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_config_service.types.string.String]":
        _token = next_token
        while True:
            _response = self.select_resource_config(
                expression,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_config_rules_evaluation(
        self,
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        config_rule_names: Optional[
            "capo_config_service.types.reevaluate_config_rule_names.ReevaluateConfigRuleNames"
        ] = None,
    ) -> "capo_config_service.types.start_config_rules_evaluation_response.StartConfigRulesEvaluationResponse":
        """<p>Runs an on-demand evaluation for the specified Config rules against the last known configuration state of the resources. Use <code>StartConfigRulesEvaluation</code> when you want to test that a rule you updated is working as expected. <code>StartConfigRulesEvaluation</code> does not re-record the latest configuration state for your resources. It re-runs an evaluation against the last known state of your resources. </p> <p>You can specify up to 25 Config rules per request. </p> <p>An existing <code>StartConfigRulesEvaluation</code> call for the specified rules must complete before you can call the API again. If you chose to have Config stream to an Amazon SNS topic, you will receive a <code>ConfigRuleEvaluationStarted</code> notification when the evaluation starts.</p> <note> <p>You don't need to call the <code>StartConfigRulesEvaluation</code> API to run an evaluation for a new rule. When you create a rule, Config evaluates your resources against the rule automatically. </p> </note> <p>The <code>StartConfigRulesEvaluation</code> API is useful if you want to run on-demand evaluations, such as the following example:</p> <ol> <li> <p>You have a custom rule that evaluates your IAM resources every 24 hours.</p> </li> <li> <p>You update your Lambda function to add additional conditions to your rule.</p> </li> <li> <p>Instead of waiting for the next periodic evaluation, you call the <code>StartConfigRulesEvaluation</code> API.</p> </li> <li> <p>Config invokes your Lambda function and evaluates your IAM resources.</p> </li> <li> <p>Your custom rule will still run periodic evaluations every 24 hours.</p> </li> </ol>

        Args:
            config_rule_names: <p>The list of names of Config rules that you want to run evaluations for.</p>

        Raises:
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.limit_exceeded_exception.LimitExceededException: <p>For <code>PutServiceLinkedConfigurationRecorder</code> API, this exception is thrown if the number of service-linked roles in the account exceeds the limit.</p> <p>For <code>StartConfigRulesEvaluation</code> API, this exception is thrown if an evaluation is in progress or if you call the <a>StartConfigRulesEvaluation</a> API more than once per minute.</p> <p>For <code>PutConfigurationAggregator</code> API, this exception is thrown if the number of accounts and aggregators exceeds the limit.</p>
            capo_config_service.errors.no_such_config_rule_exception.NoSuchConfigRuleException: <p>The Config rule in the request is not valid. Verify that the rule is an Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.</p>
            capo_config_service.errors.resource_in_use_exception.ResourceInUseException: <p>You see this exception in the following cases: </p> <ul> <li> <p>For DeleteConfigRule, Config is deleting this rule. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.</p> </li> <li> <p>For DeleteConfigRule, a remediation action is associated with the rule and Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.</p> </li> <li> <p>For PutConfigOrganizationRule, organization Config rule deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteOrganizationConfigRule, organization Config rule creation is in progress. Try your request again later.</p> </li> <li> <p>For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> <li> <p>For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.start_config_rules_evaluation_request.StartConfigRulesEvaluationRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.start_config_rules_evaluation_response.StartConfigRulesEvaluationResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.start_config_rules_evaluation

            output, http_response = (
                capo_config_service._operations.starling_dove_service.start_config_rules_evaluation.start_config_rules_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.start_config_rules_evaluation_request.StartConfigRulesEvaluationRequest = {}
        if config_rule_names is not None:
            input_["config_rule_names"] = config_rule_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_configuration_recorder(
        self,
        configuration_recorder_name: "capo_config_service.types.recorder_name.RecorderName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Starts the customer managed configuration recorder. The customer managed configuration recorder will begin recording configuration changes for the resource types you specify.</p> <p>You must have created a delivery channel to successfully start the customer managed configuration recorder. You can use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutDeliveryChannel.html">PutDeliveryChannel</a> operation to create a delivery channel.</p>

        Args:
            configuration_recorder_name: <p>The name of the customer managed configuration recorder that you want to start.</p>

        Raises:
            capo_config_service.errors.no_available_delivery_channel_exception.NoAvailableDeliveryChannelException: <p>There is no delivery channel available to record configurations.</p>
            capo_config_service.errors.no_such_configuration_recorder_exception.NoSuchConfigurationRecorderException: <p>You have specified a configuration recorder that does not exist.</p>
            capo_config_service.errors.unmodifiable_entity_exception.UnmodifiableEntityException: <p>The requested operation is not valid.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html">PutConfigurationRecorder</a>, you will see this exception because you cannot use this operation to create a service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a> operation to create a service-linked configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigurationRecorder.html">DeleteConfigurationRecorder</a>, you will see this exception because you cannot use this operation to delete a service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a> operation to delete a service-linked configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigurationRecorder.html">StartConfigurationRecorder</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html">StopConfigurationRecorder</a>, you will see this exception because these operations do not affect service-linked configuration recorders. Service-linked configuration recorders are always recording. To stop recording, you must delete the service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a> operation to delete a service-linked configuration recorder.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.start_configuration_recorder_request.StartConfigurationRecorderRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.start_configuration_recorder

            output, http_response = (
                capo_config_service._operations.starling_dove_service.start_configuration_recorder.start_configuration_recorder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.start_configuration_recorder_request.StartConfigurationRecorderRequest = {
            "configuration_recorder_name": configuration_recorder_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_remediation_execution(
        self,
        config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName",
        resource_keys: "capo_config_service.types.resource_keys.ResourceKeys",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> "capo_config_service.types.start_remediation_execution_response.StartRemediationExecutionResponse":
        """<p>Runs an on-demand remediation for the specified Config rules against the last known remediation configuration. It runs an execution against the current state of your resources. Remediation execution is asynchronous.</p> <p>You can specify up to 100 resource keys per request. An existing StartRemediationExecution call for the specified resource keys must complete before you can call the API again.</p>

        Args:
            config_rule_name: <p>The list of names of Config rules that you want to run remediation execution for.</p>
            resource_keys: <p>A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID. </p>

        Raises:
            capo_config_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>Indicates one of the following errors:</p> <ul> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the rule cannot be created because the IAM role assigned to Config lacks permissions to perform the config:Put* action.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html">PutConfigRule</a>, the Lambda function cannot be invoked. Check the function ARN, and check the function's permissions.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html">PutOrganizationConfigRule</a>, organization Config rule cannot be created because you do not have permissions to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConformancePack.html">PutOrganizationConformancePack</a>, a conformance pack cannot be created because you do not have the following permissions: </p> <ul> <li> <p>You do not have permission to call IAM <code>GetRole</code> action or create a service-linked role.</p> </li> <li> <p>You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.</p> </li> </ul> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a>, a service-linked configuration recorder cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConnector.html">PutConnector</a>, a connector cannot be created because you do not have the following permissions: IAM <code>CreateServiceLinkedRole</code>.</p> </li> </ul>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.no_such_remediation_configuration_exception.NoSuchRemediationConfigurationException: <p>You specified an Config rule without a remediation configuration.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.start_remediation_execution_request.StartRemediationExecutionRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.start_remediation_execution_response.StartRemediationExecutionResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.start_remediation_execution

            output, http_response = (
                capo_config_service._operations.starling_dove_service.start_remediation_execution.start_remediation_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.start_remediation_execution_request.StartRemediationExecutionRequest = {
            "config_rule_name": config_rule_name,
            "resource_keys": resource_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_resource_evaluation(
        self,
        resource_details: "capo_config_service.types.resource_details.ResourceDetails",
        evaluation_mode: "capo_config_service.types.evaluation_mode.EvaluationMode",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
        evaluation_context: Optional[
            "capo_config_service.types.evaluation_context.EvaluationContext"
        ] = None,
        evaluation_timeout: Optional[
            "capo_config_service.types.evaluation_timeout.EvaluationTimeout"
        ] = None,
        client_token: Optional[
            "capo_config_service.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_config_service.types.start_resource_evaluation_response.StartResourceEvaluationResponse":
        """<p>Runs an on-demand evaluation for the specified resource to determine whether the resource details will comply with configured Config rules. You can also use it for evaluation purposes. Config recommends using an evaluation context. It runs an execution against the resource details with all of the Config rules in your account that match with the specified proactive mode and resource type.</p> <note> <p>Ensure you have the <code>cloudformation:DescribeType</code> role setup to validate the resource type schema.</p> <p>You can find the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">Resource type schema</a> in "<i>Amazon Web Services public extensions</i>" within the CloudFormation registry or with the following CLI commmand: <code>aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type RESOURCE</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html#registry-view">Managing extensions through the CloudFormation registry</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services resource and property types reference</a> in the CloudFormation User Guide.</p> </note>

        Args:
            resource_details: <p>Returns a <code>ResourceDetails</code> object.</p>
            evaluation_context: <p>Returns an <code>EvaluationContext</code> object.</p>
            evaluation_mode: <p>The mode of an evaluation.</p> <note> <p>The only valid value for this API is <code>PROACTIVE</code>.</p> </note>
            evaluation_timeout: <p>The timeout for an evaluation. The default is 900 seconds. You cannot specify a number greater than 3600. If you specify 0, Config uses the default.</p>
            client_token: <p>A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request.</p> <note> <p>Avoid reusing the same client token for other API requests. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, other than the Region or Availability Zone, the retry fails with an IdempotentParameterMismatch error.</p> </note>

        Raises:
            capo_config_service.errors.idempotent_parameter_mismatch.IdempotentParameterMismatch: <p>Using the same client token with one or more different parameters. Specify a new client token with the parameter changes and try again.</p>
            capo_config_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.start_resource_evaluation_request.StartResourceEvaluationRequest]",
        ) -> OperationResponse[
            "capo_config_service.types.start_resource_evaluation_response.StartResourceEvaluationResponse"
        ]:
            import capo_config_service._operations.starling_dove_service.start_resource_evaluation

            output, http_response = (
                capo_config_service._operations.starling_dove_service.start_resource_evaluation.start_resource_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.start_resource_evaluation_request.StartResourceEvaluationRequest = {
            "resource_details": resource_details,
            "evaluation_mode": evaluation_mode,
        }
        if evaluation_context is not None:
            input_["evaluation_context"] = evaluation_context
        if evaluation_timeout is not None:
            input_["evaluation_timeout"] = evaluation_timeout
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_configuration_recorder(
        self,
        configuration_recorder_name: "capo_config_service.types.recorder_name.RecorderName",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Stops the customer managed configuration recorder. The customer managed configuration recorder will stop recording configuration changes for the resource types you have specified.</p>

        Args:
            configuration_recorder_name: <p>The name of the customer managed configuration recorder that you want to stop.</p>

        Raises:
            capo_config_service.errors.no_such_configuration_recorder_exception.NoSuchConfigurationRecorderException: <p>You have specified a configuration recorder that does not exist.</p>
            capo_config_service.errors.unmodifiable_entity_exception.UnmodifiableEntityException: <p>The requested operation is not valid.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html">PutConfigurationRecorder</a>, you will see this exception because you cannot use this operation to create a service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutServiceLinkedConfigurationRecorder.html">PutServiceLinkedConfigurationRecorder</a> operation to create a service-linked configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigurationRecorder.html">DeleteConfigurationRecorder</a>, you will see this exception because you cannot use this operation to delete a service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a> operation to delete a service-linked configuration recorder.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigurationRecorder.html">StartConfigurationRecorder</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html">StopConfigurationRecorder</a>, you will see this exception because these operations do not affect service-linked configuration recorders. Service-linked configuration recorders are always recording. To stop recording, you must delete the service-linked configuration recorder. Use the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a> operation to delete a service-linked configuration recorder.</p>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.stop_configuration_recorder_request.StopConfigurationRecorderRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.stop_configuration_recorder

            output, http_response = (
                capo_config_service._operations.starling_dove_service.stop_configuration_recorder.stop_configuration_recorder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.stop_configuration_recorder_request.StopConfigurationRecorderRequest = {
            "configuration_recorder_name": configuration_recorder_name
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
        resource_arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_config_service.types.tag_list.TagList",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Associates the specified tags to a resource with the specified <code>ResourceArn</code>. If existing tags on a resource are not specified in the request parameters, they are not changed. If existing tags are specified, however, then their values will be updated. When a resource is deleted, the tags associated with that resource are deleted as well.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. The following resources are supported:</p> <ul> <li> <p> <code>ConfigurationRecorder</code> </p> </li> <li> <p> <code>ConfigRule</code> </p> </li> <li> <p> <code>OrganizationConfigRule</code> </p> </li> <li> <p> <code>ConformancePack</code> </p> </li> <li> <p> <code>OrganizationConformancePack</code> </p> </li> <li> <p> <code>ConfigurationAggregator</code> </p> </li> <li> <p> <code>AggregationAuthorization</code> </p> </li> <li> <p> <code>StoredQuery</code> </p> </li> <li> <p> <code>Connector</code> </p> </li> </ul>
            tags: <p>An array of tag object.</p>

        Raises:
            capo_config_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>You have specified a resource that does not exist.</p>
            capo_config_service.errors.too_many_tags_exception.TooManyTagsException: <p>You have reached the limit of the number of tags you can use. For more information, see <a href="https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html"> <b>Service Limits</b> </a> in the <i>Config Developer Guide</i>.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.tag_resource

            output, http_response = (
                capo_config_service._operations.starling_dove_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_config_service.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ConfigServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. The following resources are supported:</p> <ul> <li> <p> <code>ConfigurationRecorder</code> </p> </li> <li> <p> <code>ConfigRule</code> </p> </li> <li> <p> <code>OrganizationConfigRule</code> </p> </li> <li> <p> <code>ConformancePack</code> </p> </li> <li> <p> <code>OrganizationConformancePack</code> </p> </li> <li> <p> <code>ConfigurationAggregator</code> </p> </li> <li> <p> <code>AggregationAuthorization</code> </p> </li> <li> <p> <code>StoredQuery</code> </p> </li> <li> <p> <code>Connector</code> </p> </li> </ul>
            tag_keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_config_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>You have specified a resource that does not exist.</p>
            capo_config_service.errors.validation_exception.ValidationException: <p>The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.</p> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html">PutStoredQuery</a>, one of the following errors:</p> <ul> <li> <p>There are missing required fields.</p> </li> <li> <p>The input value fails the validation.</p> </li> <li> <p>You are trying to create more than 300 queries.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html">DescribeConfigurationRecorders</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html">DescribeConfigurationRecorderStatus</a>, one of the following errors:</p> <ul> <li> <p>You have specified more than one configuration recorder.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html">AssociateResourceTypes</a> and <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html">DisassociateResourceTypes</a>, one of the following errors:</p> <ul> <li> <p>Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.</p> </li> <li> <p>One or more of the specified resource types are already associated or disassociated with the configuration recorder.</p> </li> <li> <p>For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.</p> </li> </ul> <p>For <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html">DeleteServiceLinkedConfigurationRecorder</a>, one of the following errors:</p> <ul> <li> <p>You have provided both <code>Arn</code> and <code>ServicePrincipal</code>. Only one of <code>Arn</code> or <code>ServicePrincipal</code> can be specified.</p> </li> <li> <p>You have provided a service principal for service-linked configuration recorder that is not valid.</p> </li> </ul>
            capo_config_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_config_service.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_config_service._operations.starling_dove_service.untag_resource

            output, http_response = (
                capo_config_service._operations.starling_dove_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_config_service.types.untag_resource_request.UntagResourceRequest = {
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
