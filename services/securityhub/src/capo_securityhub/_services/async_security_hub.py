"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityHubAPIService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_securityhub._auth._signers
import capo_securityhub._auth._sigv4
from capo_securityhub._auth._identity import Credentials
from capo_securityhub._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_securityhub._auth._zapros_handler import AuthMiddleware
from capo_securityhub._pagination import resolve_path as _resolve_path
from capo_securityhub._services._aws_config import aaws_config
from capo_securityhub._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_securityhub.types.accept_administrator_invitation_request
    import capo_securityhub.types.accept_administrator_invitation_response
    import capo_securityhub.types.accept_invitation_request
    import capo_securityhub.types.accept_invitation_response
    import capo_securityhub.types.account_details_list
    import capo_securityhub.types.account_free_trial_status
    import capo_securityhub.types.account_id_list
    import capo_securityhub.types.action_list
    import capo_securityhub.types.action_target
    import capo_securityhub.types.admin_account
    import capo_securityhub.types.admins_max_results
    import capo_securityhub.types.aggregator_v2
    import capo_securityhub.types.alpha_numeric_non_empty_string
    import capo_securityhub.types.arn_list
    import capo_securityhub.types.association_filters
    import capo_securityhub.types.auto_enable_standards
    import capo_securityhub.types.automation_rules_action_list_v2
    import capo_securityhub.types.automation_rules_arns_list
    import capo_securityhub.types.automation_rules_finding_filters
    import capo_securityhub.types.aws_security_finding
    import capo_securityhub.types.aws_security_finding_filters
    import capo_securityhub.types.aws_security_finding_identifier
    import capo_securityhub.types.aws_security_finding_identifier_list
    import capo_securityhub.types.batch_delete_automation_rules_request
    import capo_securityhub.types.batch_delete_automation_rules_response
    import capo_securityhub.types.batch_disable_standards_request
    import capo_securityhub.types.batch_disable_standards_response
    import capo_securityhub.types.batch_enable_standards_request
    import capo_securityhub.types.batch_enable_standards_response
    import capo_securityhub.types.batch_get_automation_rules_request
    import capo_securityhub.types.batch_get_automation_rules_response
    import capo_securityhub.types.batch_get_configuration_policy_associations_request
    import capo_securityhub.types.batch_get_configuration_policy_associations_response
    import capo_securityhub.types.batch_get_security_controls_request
    import capo_securityhub.types.batch_get_security_controls_response
    import capo_securityhub.types.batch_get_standards_control_associations_request
    import capo_securityhub.types.batch_get_standards_control_associations_response
    import capo_securityhub.types.batch_import_findings_request
    import capo_securityhub.types.batch_import_findings_request_finding_list
    import capo_securityhub.types.batch_import_findings_response
    import capo_securityhub.types.batch_update_automation_rules_request
    import capo_securityhub.types.batch_update_automation_rules_response
    import capo_securityhub.types.batch_update_findings_request
    import capo_securityhub.types.batch_update_findings_response
    import capo_securityhub.types.batch_update_findings_v2_request
    import capo_securityhub.types.batch_update_findings_v2_response
    import capo_securityhub.types.batch_update_standards_control_associations_request
    import capo_securityhub.types.batch_update_standards_control_associations_response
    import capo_securityhub.types.boolean
    import capo_securityhub.types.client_token
    import capo_securityhub.types.configuration_policy_association_summary
    import capo_securityhub.types.configuration_policy_associations_list
    import capo_securityhub.types.configuration_policy_summary
    import capo_securityhub.types.connector_provider_name
    import capo_securityhub.types.connector_status
    import capo_securityhub.types.control_finding_generator
    import capo_securityhub.types.control_status
    import capo_securityhub.types.create_action_target_request
    import capo_securityhub.types.create_action_target_response
    import capo_securityhub.types.create_aggregator_v2_request
    import capo_securityhub.types.create_aggregator_v2_response
    import capo_securityhub.types.create_automation_rule_request
    import capo_securityhub.types.create_automation_rule_response
    import capo_securityhub.types.create_automation_rule_v2_request
    import capo_securityhub.types.create_automation_rule_v2_response
    import capo_securityhub.types.create_configuration_policy_request
    import capo_securityhub.types.create_configuration_policy_response
    import capo_securityhub.types.create_connector_request
    import capo_securityhub.types.create_connector_response
    import capo_securityhub.types.create_connector_v2_request
    import capo_securityhub.types.create_connector_v2_response
    import capo_securityhub.types.create_finding_aggregator_request
    import capo_securityhub.types.create_finding_aggregator_response
    import capo_securityhub.types.create_insight_request
    import capo_securityhub.types.create_insight_response
    import capo_securityhub.types.create_members_request
    import capo_securityhub.types.create_members_response
    import capo_securityhub.types.create_ticket_v2_request
    import capo_securityhub.types.create_ticket_v2_response
    import capo_securityhub.types.criteria
    import capo_securityhub.types.cross_account_max_results
    import capo_securityhub.types.cspm_connector_provider_name
    import capo_securityhub.types.cspm_connector_status
    import capo_securityhub.types.cspm_enablement_status
    import capo_securityhub.types.cspm_provider_configuration
    import capo_securityhub.types.cspm_provider_update_configuration
    import capo_securityhub.types.decline_invitations_request
    import capo_securityhub.types.decline_invitations_response
    import capo_securityhub.types.delete_action_target_request
    import capo_securityhub.types.delete_action_target_response
    import capo_securityhub.types.delete_aggregator_v2_request
    import capo_securityhub.types.delete_aggregator_v2_response
    import capo_securityhub.types.delete_automation_rule_v2_request
    import capo_securityhub.types.delete_automation_rule_v2_response
    import capo_securityhub.types.delete_configuration_policy_request
    import capo_securityhub.types.delete_configuration_policy_response
    import capo_securityhub.types.delete_connector_request
    import capo_securityhub.types.delete_connector_response
    import capo_securityhub.types.delete_connector_v2_request
    import capo_securityhub.types.delete_connector_v2_response
    import capo_securityhub.types.delete_finding_aggregator_request
    import capo_securityhub.types.delete_finding_aggregator_response
    import capo_securityhub.types.delete_insight_request
    import capo_securityhub.types.delete_insight_response
    import capo_securityhub.types.delete_invitations_request
    import capo_securityhub.types.delete_invitations_response
    import capo_securityhub.types.delete_members_request
    import capo_securityhub.types.delete_members_response
    import capo_securityhub.types.describe_action_targets_request
    import capo_securityhub.types.describe_action_targets_response
    import capo_securityhub.types.describe_hub_request
    import capo_securityhub.types.describe_hub_response
    import capo_securityhub.types.describe_organization_configuration_request
    import capo_securityhub.types.describe_organization_configuration_response
    import capo_securityhub.types.describe_products_request
    import capo_securityhub.types.describe_products_response
    import capo_securityhub.types.describe_products_v2_request
    import capo_securityhub.types.describe_products_v2_response
    import capo_securityhub.types.describe_security_hub_v2_request
    import capo_securityhub.types.describe_security_hub_v2_response
    import capo_securityhub.types.describe_standards_controls_request
    import capo_securityhub.types.describe_standards_controls_response
    import capo_securityhub.types.describe_standards_request
    import capo_securityhub.types.describe_standards_response
    import capo_securityhub.types.disable_import_findings_for_product_request
    import capo_securityhub.types.disable_import_findings_for_product_response
    import capo_securityhub.types.disable_organization_admin_account_request
    import capo_securityhub.types.disable_organization_admin_account_response
    import capo_securityhub.types.disable_security_hub_feature_v2_request
    import capo_securityhub.types.disable_security_hub_feature_v2_response
    import capo_securityhub.types.disable_security_hub_request
    import capo_securityhub.types.disable_security_hub_response
    import capo_securityhub.types.disable_security_hub_v2_request
    import capo_securityhub.types.disable_security_hub_v2_response
    import capo_securityhub.types.disassociate_from_administrator_account_request
    import capo_securityhub.types.disassociate_from_administrator_account_response
    import capo_securityhub.types.disassociate_from_master_account_request
    import capo_securityhub.types.disassociate_from_master_account_response
    import capo_securityhub.types.disassociate_members_request
    import capo_securityhub.types.disassociate_members_response
    import capo_securityhub.types.enable_import_findings_for_product_request
    import capo_securityhub.types.enable_import_findings_for_product_response
    import capo_securityhub.types.enable_organization_admin_account_request
    import capo_securityhub.types.enable_organization_admin_account_response
    import capo_securityhub.types.enable_security_hub_feature_v2_request
    import capo_securityhub.types.enable_security_hub_feature_v2_response
    import capo_securityhub.types.enable_security_hub_request
    import capo_securityhub.types.enable_security_hub_response
    import capo_securityhub.types.enable_security_hub_v2_request
    import capo_securityhub.types.enable_security_hub_v2_response
    import capo_securityhub.types.enablement_status
    import capo_securityhub.types.feature_name
    import capo_securityhub.types.field_map
    import capo_securityhub.types.finding_aggregator
    import capo_securityhub.types.finding_history_record
    import capo_securityhub.types.finding_scopes
    import capo_securityhub.types.findings_trends_filters
    import capo_securityhub.types.free_trial_account_id_list
    import capo_securityhub.types.free_trial_status_value_list
    import capo_securityhub.types.generate_recommended_policy_v2_request
    import capo_securityhub.types.generate_recommended_policy_v2_response
    import capo_securityhub.types.get_administrator_account_request
    import capo_securityhub.types.get_administrator_account_response
    import capo_securityhub.types.get_aggregator_v2_request
    import capo_securityhub.types.get_aggregator_v2_response
    import capo_securityhub.types.get_automation_rule_v2_request
    import capo_securityhub.types.get_automation_rule_v2_response
    import capo_securityhub.types.get_configuration_policy_association_request
    import capo_securityhub.types.get_configuration_policy_association_response
    import capo_securityhub.types.get_configuration_policy_request
    import capo_securityhub.types.get_configuration_policy_response
    import capo_securityhub.types.get_connector_request
    import capo_securityhub.types.get_connector_response
    import capo_securityhub.types.get_connector_v2_request
    import capo_securityhub.types.get_connector_v2_response
    import capo_securityhub.types.get_enabled_standards_request
    import capo_securityhub.types.get_enabled_standards_response
    import capo_securityhub.types.get_finding_aggregator_request
    import capo_securityhub.types.get_finding_aggregator_response
    import capo_securityhub.types.get_finding_history_request
    import capo_securityhub.types.get_finding_history_response
    import capo_securityhub.types.get_finding_statistics_v2_request
    import capo_securityhub.types.get_finding_statistics_v2_response
    import capo_securityhub.types.get_findings_request
    import capo_securityhub.types.get_findings_response
    import capo_securityhub.types.get_findings_trends_v2_request
    import capo_securityhub.types.get_findings_trends_v2_response
    import capo_securityhub.types.get_findings_v2_request
    import capo_securityhub.types.get_findings_v2_response
    import capo_securityhub.types.get_insight_results_request
    import capo_securityhub.types.get_insight_results_response
    import capo_securityhub.types.get_insights_request
    import capo_securityhub.types.get_insights_response
    import capo_securityhub.types.get_invitations_count_request
    import capo_securityhub.types.get_invitations_count_response
    import capo_securityhub.types.get_master_account_request
    import capo_securityhub.types.get_master_account_response
    import capo_securityhub.types.get_members_request
    import capo_securityhub.types.get_members_response
    import capo_securityhub.types.get_recommended_policy_v2_request
    import capo_securityhub.types.get_recommended_policy_v2_response
    import capo_securityhub.types.get_resources_statistics_v2_request
    import capo_securityhub.types.get_resources_statistics_v2_response
    import capo_securityhub.types.get_resources_trends_v2_request
    import capo_securityhub.types.get_resources_trends_v2_response
    import capo_securityhub.types.get_resources_v2_request
    import capo_securityhub.types.get_resources_v2_response
    import capo_securityhub.types.get_security_control_definition_request
    import capo_securityhub.types.get_security_control_definition_response
    import capo_securityhub.types.group_by_rules
    import capo_securityhub.types.insight
    import capo_securityhub.types.integer
    import capo_securityhub.types.invitation
    import capo_securityhub.types.invite_members_request
    import capo_securityhub.types.invite_members_response
    import capo_securityhub.types.list_aggregators_v2_request
    import capo_securityhub.types.list_aggregators_v2_response
    import capo_securityhub.types.list_automation_rules_request
    import capo_securityhub.types.list_automation_rules_response
    import capo_securityhub.types.list_automation_rules_v2_request
    import capo_securityhub.types.list_automation_rules_v2_response
    import capo_securityhub.types.list_configuration_policies_request
    import capo_securityhub.types.list_configuration_policies_response
    import capo_securityhub.types.list_configuration_policy_associations_request
    import capo_securityhub.types.list_configuration_policy_associations_response
    import capo_securityhub.types.list_connectors_request
    import capo_securityhub.types.list_connectors_response
    import capo_securityhub.types.list_connectors_v2_request
    import capo_securityhub.types.list_connectors_v2_response
    import capo_securityhub.types.list_enabled_products_for_import_request
    import capo_securityhub.types.list_enabled_products_for_import_response
    import capo_securityhub.types.list_finding_aggregators_request
    import capo_securityhub.types.list_finding_aggregators_response
    import capo_securityhub.types.list_free_trial_statuses_v2_request
    import capo_securityhub.types.list_free_trial_statuses_v2_response
    import capo_securityhub.types.list_invitations_request
    import capo_securityhub.types.list_invitations_response
    import capo_securityhub.types.list_members_request
    import capo_securityhub.types.list_members_response
    import capo_securityhub.types.list_organization_admin_accounts_request
    import capo_securityhub.types.list_organization_admin_accounts_response
    import capo_securityhub.types.list_security_control_definitions_request
    import capo_securityhub.types.list_security_control_definitions_response
    import capo_securityhub.types.list_standards_control_associations_request
    import capo_securityhub.types.list_standards_control_associations_response
    import capo_securityhub.types.list_tags_for_resource_request
    import capo_securityhub.types.list_tags_for_resource_response
    import capo_securityhub.types.max_results
    import capo_securityhub.types.max_statistic_results
    import capo_securityhub.types.member
    import capo_securityhub.types.metadata_uid_list
    import capo_securityhub.types.next_token
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.note_update
    import capo_securityhub.types.ocsf_finding
    import capo_securityhub.types.ocsf_finding_filters
    import capo_securityhub.types.ocsf_finding_identifier_list
    import capo_securityhub.types.organization_configuration
    import capo_securityhub.types.parameters
    import capo_securityhub.types.policy
    import capo_securityhub.types.product
    import capo_securityhub.types.product_v2
    import capo_securityhub.types.provider_configuration
    import capo_securityhub.types.provider_update_configuration
    import capo_securityhub.types.ratio_scale
    import capo_securityhub.types.recommendation_step
    import capo_securityhub.types.record_state
    import capo_securityhub.types.register_connector_v2_request
    import capo_securityhub.types.register_connector_v2_response
    import capo_securityhub.types.related_finding_list
    import capo_securityhub.types.resource_arn
    import capo_securityhub.types.resource_group_by_rules
    import capo_securityhub.types.resource_result
    import capo_securityhub.types.resource_scopes
    import capo_securityhub.types.resources_filters
    import capo_securityhub.types.resources_trends_filters
    import capo_securityhub.types.resources_trends_metrics_result
    import capo_securityhub.types.rule_order_value
    import capo_securityhub.types.rule_order_value_v2
    import capo_securityhub.types.rule_status
    import capo_securityhub.types.rule_status_v2
    import capo_securityhub.types.security_control_definition
    import capo_securityhub.types.security_controls_providers
    import capo_securityhub.types.security_hub_feature
    import capo_securityhub.types.severity_update
    import capo_securityhub.types.sort_criteria
    import capo_securityhub.types.sort_order
    import capo_securityhub.types.standard
    import capo_securityhub.types.standards_control
    import capo_securityhub.types.standards_control_association_ids
    import capo_securityhub.types.standards_control_association_summary
    import capo_securityhub.types.standards_control_association_updates
    import capo_securityhub.types.standards_providers
    import capo_securityhub.types.standards_subscription
    import capo_securityhub.types.standards_subscription_arns
    import capo_securityhub.types.standards_subscription_requests
    import capo_securityhub.types.start_configuration_policy_association_request
    import capo_securityhub.types.start_configuration_policy_association_response
    import capo_securityhub.types.start_configuration_policy_disassociation_request
    import capo_securityhub.types.start_configuration_policy_disassociation_response
    import capo_securityhub.types.string_list
    import capo_securityhub.types.tag_key_list
    import capo_securityhub.types.tag_map
    import capo_securityhub.types.tag_resource_request
    import capo_securityhub.types.tag_resource_response
    import capo_securityhub.types.target
    import capo_securityhub.types.ticket_creation_mode
    import capo_securityhub.types.timestamp
    import capo_securityhub.types.trends_metrics_result
    import capo_securityhub.types.type_list
    import capo_securityhub.types.untag_resource_request
    import capo_securityhub.types.untag_resource_response
    import capo_securityhub.types.update_action_target_request
    import capo_securityhub.types.update_action_target_response
    import capo_securityhub.types.update_aggregator_v2_request
    import capo_securityhub.types.update_aggregator_v2_response
    import capo_securityhub.types.update_automation_rule_v2_request
    import capo_securityhub.types.update_automation_rule_v2_response
    import capo_securityhub.types.update_automation_rules_request_items_list
    import capo_securityhub.types.update_configuration_policy_request
    import capo_securityhub.types.update_configuration_policy_response
    import capo_securityhub.types.update_connector_request
    import capo_securityhub.types.update_connector_response
    import capo_securityhub.types.update_connector_v2_request
    import capo_securityhub.types.update_connector_v2_response
    import capo_securityhub.types.update_finding_aggregator_request
    import capo_securityhub.types.update_finding_aggregator_response
    import capo_securityhub.types.update_findings_request
    import capo_securityhub.types.update_findings_response
    import capo_securityhub.types.update_insight_request
    import capo_securityhub.types.update_insight_response
    import capo_securityhub.types.update_organization_configuration_request
    import capo_securityhub.types.update_organization_configuration_response
    import capo_securityhub.types.update_security_control_request
    import capo_securityhub.types.update_security_control_response
    import capo_securityhub.types.update_security_hub_configuration_request
    import capo_securityhub.types.update_security_hub_configuration_response
    import capo_securityhub.types.update_standards_control_request
    import capo_securityhub.types.update_standards_control_response
    import capo_securityhub.types.verification_state
    import capo_securityhub.types.workflow_update


class AsyncSecurityHubClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSecurityHubClient:
    """A client for the ``SecurityHub`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncSecurityHubClientConfig(
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
        self, config_overrides: Optional[AsyncSecurityHubClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSecurityHubClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def accept_administrator_invitation(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        administrator_id: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        invitation_id: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.accept_administrator_invitation_response.AcceptAdministratorInvitationResponse":
        """<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Accepts the invitation to be a member account and be monitored by the Security Hub CSPM administrator account that the invitation was sent from.</p> <p>This operation is only used by member accounts that are not added through Organizations.</p> <p>When the member account accepts the invitation, permission is granted to the administrator account to view findings generated in the member account.</p>

        Args:
            administrator_id: <p>The account ID of the Security Hub CSPM administrator account that sent the invitation.</p>
            invitation_id: <p>The identifier of the invitation sent from the Security Hub CSPM administrator account.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To accept an invitation be a member account
            The following example demonstrates how an account can accept an invitation from the Security Hub administrator account to be a member account. This operation is applicable only to member accounts that are not added through AWS Organizations.

            >>> await client.accept_administrator_invitation(administrator_id='123456789012', invitation_id='7ab938c5d52d7904ad09f9e7c20cc4eb')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.accept_administrator_invitation_request.AcceptAdministratorInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.accept_administrator_invitation_response.AcceptAdministratorInvitationResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.accept_administrator_invitation

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.accept_administrator_invitation.async_accept_administrator_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.accept_administrator_invitation_request.AcceptAdministratorInvitationRequest = {}
        if administrator_id is not None:
            input_["administrator_id"] = administrator_id
        if invitation_id is not None:
            input_["invitation_id"] = invitation_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def accept_invitation(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        master_id: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        invitation_id: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.accept_invitation_response.AcceptInvitationResponse":
        """<p>This method is deprecated. Instead, use <code>AcceptAdministratorInvitation</code>.</p> <p>The Security Hub CSPM console continues to use <code>AcceptInvitation</code>. It will eventually change to use <code>AcceptAdministratorInvitation</code>. Any IAM policies that specifically control access to this function must continue to use <code>AcceptInvitation</code>. You should also add <code>AcceptAdministratorInvitation</code> to your policies to ensure that the correct permissions are in place after the console begins to use <code>AcceptAdministratorInvitation</code>.</p> <p>Accepts the invitation to be a member account and be monitored by the Security Hub CSPM administrator account that the invitation was sent from.</p> <p>This operation is only used by member accounts that are not added through Organizations.</p> <p>When the member account accepts the invitation, permission is granted to the administrator account to view findings generated in the member account.</p>

        Args:
            master_id: <p>The account ID of the Security Hub CSPM administrator account that sent the invitation.</p>
            invitation_id: <p>The identifier of the invitation sent from the Security Hub CSPM administrator account.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.accept_invitation_request.AcceptInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.accept_invitation_response.AcceptInvitationResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.accept_invitation

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.accept_invitation.async_accept_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.accept_invitation_request.AcceptInvitationRequest = {}
        if master_id is not None:
            input_["master_id"] = master_id
        if invitation_id is not None:
            input_["invitation_id"] = invitation_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_automation_rules(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        automation_rules_arns: Optional[
            "capo_securityhub.types.automation_rules_arns_list.AutomationRulesArnsList"
        ] = None,
    ) -> "capo_securityhub.types.batch_delete_automation_rules_response.BatchDeleteAutomationRulesResponse":
        """<p> Deletes one or more automation rules. </p>

        Args:
            automation_rules_arns: <p> A list of Amazon Resource Names (ARNs) for the rules that are to be deleted. </p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete one or more automation rules
            The following example deletes the specified automation rules.

            >>> await client.batch_delete_automation_rules(automation_rules_arns=['arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_delete_automation_rules_request.BatchDeleteAutomationRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_delete_automation_rules_response.BatchDeleteAutomationRulesResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_delete_automation_rules

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_delete_automation_rules.async_batch_delete_automation_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_delete_automation_rules_request.BatchDeleteAutomationRulesRequest = {}
        if automation_rules_arns is not None:
            input_["automation_rules_arns"] = automation_rules_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_disable_standards(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        standards_subscription_arns: Optional[
            "capo_securityhub.types.standards_subscription_arns.StandardsSubscriptionArns"
        ] = None,
    ) -> "capo_securityhub.types.batch_disable_standards_response.BatchDisableStandardsResponse":
        """<p>Disables the standards specified by the provided <code>StandardsSubscriptionArns</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html">Security Standards</a> section of the <i>Security Hub CSPM User Guide</i>.</p>

        Args:
            standards_subscription_arns: <p>The ARNs of the standards subscriptions to disable.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disable one or more security standards
            The following example disables a security standard in Security Hub.

            >>> await client.batch_disable_standards(standards_subscription_arns=['arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_disable_standards_request.BatchDisableStandardsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_disable_standards_response.BatchDisableStandardsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_disable_standards

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_disable_standards.async_batch_disable_standards(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_disable_standards_request.BatchDisableStandardsRequest = {}
        if standards_subscription_arns is not None:
            input_["standards_subscription_arns"] = standards_subscription_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_enable_standards(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        standards_subscription_requests: Optional[
            "capo_securityhub.types.standards_subscription_requests.StandardsSubscriptionRequests"
        ] = None,
    ) -> "capo_securityhub.types.batch_enable_standards_response.BatchEnableStandardsResponse":
        """<p>Enables the standards specified by the provided <code>StandardsArn</code>. To obtain the ARN for a standard, use the <code>DescribeStandards</code> operation.</p> <p>For more information, see the <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html">Security Standards</a> section of the <i>Security Hub CSPM User Guide</i>.</p>

        Args:
            standards_subscription_requests: <p>The list of standards checks to enable.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable security standards
            The following example enables the security standard specified by the StandardArn. You can use this operation to enable one or more Security Hub standards.

            >>> await client.batch_enable_standards(standards_subscription_requests=[{'StandardsArn': 'arn:aws:securityhub:us-west-1::standards/pci-dss/v/3.2.1'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_enable_standards_request.BatchEnableStandardsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_enable_standards_response.BatchEnableStandardsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_enable_standards

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_enable_standards.async_batch_enable_standards(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_enable_standards_request.BatchEnableStandardsRequest = {}
        if standards_subscription_requests is not None:
            input_["standards_subscription_requests"] = standards_subscription_requests

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_automation_rules(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        automation_rules_arns: Optional[
            "capo_securityhub.types.automation_rules_arns_list.AutomationRulesArnsList"
        ] = None,
    ) -> "capo_securityhub.types.batch_get_automation_rules_response.BatchGetAutomationRulesResponse":
        """<p> Retrieves a list of details for automation rules based on rule Amazon Resource Names (ARNs). </p>

        Args:
            automation_rules_arns: <p> A list of rule ARNs to get details for. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update one ore more automation rules
            The following example updates the specified automation rules.

            >>> await client.batch_get_automation_rules(automation_rules_arns=['arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_get_automation_rules_request.BatchGetAutomationRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_get_automation_rules_response.BatchGetAutomationRulesResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_get_automation_rules

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_get_automation_rules.async_batch_get_automation_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_get_automation_rules_request.BatchGetAutomationRulesRequest = {}
        if automation_rules_arns is not None:
            input_["automation_rules_arns"] = automation_rules_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_configuration_policy_associations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        configuration_policy_association_identifiers: Optional[
            "capo_securityhub.types.configuration_policy_associations_list.ConfigurationPolicyAssociationsList"
        ] = None,
    ) -> "capo_securityhub.types.batch_get_configuration_policy_associations_response.BatchGetConfigurationPolicyAssociationsResponse":
        """<p> Returns associations between an Security Hub CSPM configuration and a batch of target accounts, organizational units, or the root. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. A configuration can refer to a configuration policy or to a self-managed configuration. </p>

        Args:
            configuration_policy_association_identifiers: <p> Specifies one or more target account IDs, organizational unit (OU) IDs, or the root ID to retrieve associations for. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get configuration associations for a batch of targets
            This operation provides details about configuration associations for a batch of target accounts, organizational units, or the root.

            >>> await client.batch_get_configuration_policy_associations(configuration_policy_association_identifiers=[{'Target': {'AccountId': '111122223333'}}, {'Target': {'RootId': 'r-f6g7h8i9j0example'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_get_configuration_policy_associations_request.BatchGetConfigurationPolicyAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_get_configuration_policy_associations_response.BatchGetConfigurationPolicyAssociationsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_get_configuration_policy_associations

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_get_configuration_policy_associations.async_batch_get_configuration_policy_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_get_configuration_policy_associations_request.BatchGetConfigurationPolicyAssociationsRequest = {}
        if configuration_policy_association_identifiers is not None:
            input_["configuration_policy_association_identifiers"] = (
                configuration_policy_association_identifiers
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_security_controls(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        security_control_ids: Optional[
            "capo_securityhub.types.string_list.StringList"
        ] = None,
    ) -> "capo_securityhub.types.batch_get_security_controls_response.BatchGetSecurityControlsResponse":
        """<p> Provides details about a batch of security controls for the current Amazon Web Services account and Amazon Web Services Region. </p>

        Args:
            security_control_ids: <p> A list of security controls (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters). The security control ID or Amazon Resource Name (ARN) is the same across standards. </p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get security control details
            The following example gets details for the specified controls in the current AWS account and AWS Region.

            >>> await client.batch_get_security_controls(security_control_ids=['ACM.1', 'APIGateway.1'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_get_security_controls_request.BatchGetSecurityControlsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_get_security_controls_response.BatchGetSecurityControlsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_get_security_controls

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_get_security_controls.async_batch_get_security_controls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_get_security_controls_request.BatchGetSecurityControlsRequest = {}
        if security_control_ids is not None:
            input_["security_control_ids"] = security_control_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_standards_control_associations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        standards_control_association_ids: Optional[
            "capo_securityhub.types.standards_control_association_ids.StandardsControlAssociationIds"
        ] = None,
    ) -> "capo_securityhub.types.batch_get_standards_control_associations_response.BatchGetStandardsControlAssociationsResponse":
        """<p> For a batch of security controls and standards, identifies whether each control is currently enabled or disabled in a standard. </p> <p> Calls to this operation return a <code>RESOURCE_NOT_FOUND_EXCEPTION</code> error when the standard subscription for the association has a <code>NOT_READY_FOR_UPDATES</code> value for <code>StandardsControlsUpdatable</code>. </p>

        Args:
            standards_control_association_ids: <p> An array with one or more objects that includes a security control (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) and the Amazon Resource Name (ARN) of a standard. This field is used to query the enablement status of a control in a specified standard. The security control ID or ARN is the same across standards. </p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_get_standards_control_associations_request.BatchGetStandardsControlAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_get_standards_control_associations_response.BatchGetStandardsControlAssociationsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_get_standards_control_associations

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_get_standards_control_associations.async_batch_get_standards_control_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_get_standards_control_associations_request.BatchGetStandardsControlAssociationsRequest = {}
        if standards_control_association_ids is not None:
            input_["standards_control_association_ids"] = (
                standards_control_association_ids
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_import_findings(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        findings: Optional[
            "capo_securityhub.types.batch_import_findings_request_finding_list.BatchImportFindingsRequestFindingList"
        ] = None,
    ) -> "capo_securityhub.types.batch_import_findings_response.BatchImportFindingsResponse":
        """<p>Imports security findings generated by a finding provider into Security Hub CSPM. This action is requested by the finding provider to import its findings into Security Hub CSPM.</p> <p> <code>BatchImportFindings</code> must be called by one of the following:</p> <ul> <li> <p>The Amazon Web Services account that is associated with a finding if you are using the <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-custom-providers.html#securityhub-custom-providers-bfi-reqs">default product ARN</a> or are a partner sending findings from within a customer's Amazon Web Services account. In these cases, the identifier of the account that you are calling <code>BatchImportFindings</code> from needs to be the same as the <code>AwsAccountId</code> attribute for the finding.</p> </li> <li> <p>An Amazon Web Services account that Security Hub CSPM has allow-listed for an official partner integration. In this case, you can call <code>BatchImportFindings</code> from the allow-listed account and send findings from different customer accounts in the same batch.</p> </li> </ul> <p>The maximum allowed size for a finding is 240 Kb. An error is returned for any finding larger than 240 Kb.</p> <p>After a finding is created, <code>BatchImportFindings</code> cannot be used to update the following finding fields and objects, which Security Hub CSPM customers use to manage their investigation workflow.</p> <ul> <li> <p> <code>Note</code> </p> </li> <li> <p> <code>UserDefinedFields</code> </p> </li> <li> <p> <code>VerificationState</code> </p> </li> <li> <p> <code>Workflow</code> </p> </li> </ul> <p>Finding providers also should not use <code>BatchImportFindings</code> to update the following attributes.</p> <ul> <li> <p> <code>Confidence</code> </p> </li> <li> <p> <code>Criticality</code> </p> </li> <li> <p> <code>RelatedFindings</code> </p> </li> <li> <p> <code>Severity</code> </p> </li> <li> <p> <code>Types</code> </p> </li> </ul> <p>Instead, finding providers use <code>FindingProviderFields</code> to provide values for these attributes.</p>

        Args:
            findings: <p>A list of findings to import. To successfully import a finding, it must follow the <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html">Amazon Web Services Security Finding Format</a>. Maximum of 100 findings per request.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To import security findings from a third party provider to Security Hub
            The following example imports findings from a third party provider to Security Hub.

            >>> await client.batch_import_findings(findings=[{'AwsAccountId': '123456789012', 'CreatedAt': '2020-05-27T17:05:54.832Z', 'Description': 'Vulnerability in a CloudTrail trail', 'FindingProviderFields': {'Severity': {'Label': 'LOW', 'Original': '10'}, 'Types': ['Software and Configuration Checks/Vulnerabilities/CVE']}, 'GeneratorId': 'TestGeneratorId', 'Id': 'Id1', 'ProductArn': 'arn:aws:securityhub:us-west-1:123456789012:product/123456789012/default', 'Resources': [{'Id': 'arn:aws:cloudtrail:us-west-1:123456789012:trail/TrailName', 'Partition': 'aws', 'Region': 'us-west-1', 'Type': 'AwsCloudTrailTrail'}], 'SchemaVersion': '2018-10-08', 'Title': 'CloudTrail trail vulnerability', 'UpdatedAt': '2020-06-02T16:05:54.832Z'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_import_findings_request.BatchImportFindingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_import_findings_response.BatchImportFindingsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_import_findings

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_import_findings.async_batch_import_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_import_findings_request.BatchImportFindingsRequest = {}
        if findings is not None:
            input_["findings"] = findings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_automation_rules(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        update_automation_rules_request_items: Optional[
            "capo_securityhub.types.update_automation_rules_request_items_list.UpdateAutomationRulesRequestItemsList"
        ] = None,
    ) -> "capo_securityhub.types.batch_update_automation_rules_response.BatchUpdateAutomationRulesResponse":
        """<p> Updates one or more automation rules based on rule Amazon Resource Names (ARNs) and input parameters. </p>

        Args:
            update_automation_rules_request_items: <p> An array of ARNs for the rules that are to be updated. Optionally, you can also include <code>RuleStatus</code> and <code>RuleOrder</code>. </p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update one ore more automation rules
            The following example updates the specified automation rules.

            >>> await client.batch_update_automation_rules(update_automation_rules_request_items=[{'RuleArn': 'arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'RuleStatus': 'ENABLED', 'RuleOrder': 15}, {'RuleArn': 'arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222', 'RuleStatus': 'DISABLED'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_update_automation_rules_request.BatchUpdateAutomationRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_update_automation_rules_response.BatchUpdateAutomationRulesResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_update_automation_rules

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_update_automation_rules.async_batch_update_automation_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_update_automation_rules_request.BatchUpdateAutomationRulesRequest = {}
        if update_automation_rules_request_items is not None:
            input_["update_automation_rules_request_items"] = (
                update_automation_rules_request_items
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_findings(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        finding_identifiers: Optional[
            "capo_securityhub.types.aws_security_finding_identifier_list.AwsSecurityFindingIdentifierList"
        ] = None,
        note: Optional["capo_securityhub.types.note_update.NoteUpdate"] = None,
        severity: Optional[
            "capo_securityhub.types.severity_update.SeverityUpdate"
        ] = None,
        verification_state: Optional[
            "capo_securityhub.types.verification_state.VerificationState"
        ] = None,
        confidence: Optional["capo_securityhub.types.ratio_scale.RatioScale"] = None,
        criticality: Optional["capo_securityhub.types.ratio_scale.RatioScale"] = None,
        types: Optional["capo_securityhub.types.type_list.TypeList"] = None,
        user_defined_fields: Optional[
            "capo_securityhub.types.field_map.FieldMap"
        ] = None,
        workflow: Optional[
            "capo_securityhub.types.workflow_update.WorkflowUpdate"
        ] = None,
        related_findings: Optional[
            "capo_securityhub.types.related_finding_list.RelatedFindingList"
        ] = None,
    ) -> "capo_securityhub.types.batch_update_findings_response.BatchUpdateFindingsResponse":
        """<p> Used by Security Hub CSPM customers to update information about their investigation into one or more findings. Requested by administrator accounts or member accounts. Administrator accounts can update findings for their account and their member accounts. A member account can update findings only for their own account. Administrator and member accounts can use this operation to update the following fields and objects for one or more findings: </p> <ul> <li> <p> <code>Confidence</code> </p> </li> <li> <p> <code>Criticality</code> </p> </li> <li> <p> <code>Note</code> </p> </li> <li> <p> <code>RelatedFindings</code> </p> </li> <li> <p> <code>Severity</code> </p> </li> <li> <p> <code>Types</code> </p> </li> <li> <p> <code>UserDefinedFields</code> </p> </li> <li> <p> <code>VerificationState</code> </p> </li> <li> <p> <code>Workflow</code> </p> </li> </ul> <p> If you use this operation to update a finding, your updates don’t affect the value for the <code>UpdatedAt</code> field of the finding. Also note that it can take several minutes for Security Hub CSPM to process your request and update each finding specified in the request. </p> <p> You can configure IAM policies to restrict access to fields and field values. For example, you might not want member accounts to be able to suppress findings or change the finding severity. For more information see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/finding-update-batchupdatefindings.html#batchupdatefindings-configure-access">Configuring access to BatchUpdateFindings</a> in the <i>Security Hub CSPM User Guide</i>. </p>

        Args:
            finding_identifiers: <p>The list of findings to update. <code>BatchUpdateFindings</code> can be used to update up to 100 findings at a time.</p> <p>For each finding, the list provides the finding identifier and the ARN of the finding provider.</p>
            severity: <p>Used to update the finding severity.</p>
            verification_state: <p>Indicates the veracity of a finding.</p> <p>The available values for <code>VerificationState</code> are as follows.</p> <ul> <li> <p> <code>UNKNOWN</code> – The default disposition of a security finding</p> </li> <li> <p> <code>TRUE_POSITIVE</code> – The security finding is confirmed</p> </li> <li> <p> <code>FALSE_POSITIVE</code> – The security finding was determined to be a false alarm</p> </li> <li> <p> <code>BENIGN_POSITIVE</code> – A special case of <code>TRUE_POSITIVE</code> where the finding doesn't pose any threat, is expected, or both</p> </li> </ul>
            confidence: <p>The updated value for the finding confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.</p> <p>Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.</p>
            criticality: <p>The updated value for the level of importance assigned to the resources associated with the findings.</p> <p>A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources. </p>
            types: <p>One or more finding types in the format of namespace/category/classifier that classify a finding.</p> <p>Valid namespace values are as follows.</p> <ul> <li> <p>Software and Configuration Checks</p> </li> <li> <p>TTPs</p> </li> <li> <p>Effects</p> </li> <li> <p>Unusual Behaviors</p> </li> <li> <p>Sensitive Data Identifications </p> </li> </ul>
            user_defined_fields: <p>A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.</p>
            workflow: <p>Used to update the workflow status of a finding.</p> <p>The workflow status indicates the progress of the investigation into the finding. </p>
            related_findings: <p>A list of findings that are related to the updated findings.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update Security Hub findings
            The following example updates Security Hub findings. The finding identifier parameter specifies which findings to update. Only specific finding fields can be updated with this operation.

            >>> await client.batch_update_findings(finding_identifiers=[{'Id': 'arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'ProductArn': 'arn:aws:securityhub:us-west-1::product/aws/securityhub'}, {'Id': 'arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222', 'ProductArn': 'arn:aws:securityhub:us-west-1::product/aws/securityhub'}], note={'Text': 'Known issue that is not a risk.', 'UpdatedBy': 'user1'}, severity={'Label': 'LOW'}, verification_state='TRUE_POSITIVE', confidence=80, criticality=80, types=['Software and Configuration Checks/Vulnerabilities/CVE'], user_defined_fields={'reviewedByCio': 'true'}, workflow={'Status': 'RESOLVED'}, related_findings=[{'Id': 'arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333', 'ProductArn': 'arn:aws:securityhub:us-west-1::product/aws/securityhub'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_update_findings_request.BatchUpdateFindingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_update_findings_response.BatchUpdateFindingsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_update_findings

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_update_findings.async_batch_update_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_update_findings_request.BatchUpdateFindingsRequest = {}
        if finding_identifiers is not None:
            input_["finding_identifiers"] = finding_identifiers
        if note is not None:
            input_["note"] = note
        if severity is not None:
            input_["severity"] = severity
        if verification_state is not None:
            input_["verification_state"] = verification_state
        if confidence is not None:
            input_["confidence"] = confidence
        if criticality is not None:
            input_["criticality"] = criticality
        if types is not None:
            input_["types"] = types
        if user_defined_fields is not None:
            input_["user_defined_fields"] = user_defined_fields
        if workflow is not None:
            input_["workflow"] = workflow
        if related_findings is not None:
            input_["related_findings"] = related_findings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_findings_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        metadata_uids: Optional[
            "capo_securityhub.types.metadata_uid_list.MetadataUidList"
        ] = None,
        finding_identifiers: Optional[
            "capo_securityhub.types.ocsf_finding_identifier_list.OcsfFindingIdentifierList"
        ] = None,
        comment: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        severity_id: Optional["capo_securityhub.types.integer.Integer"] = None,
        status_id: Optional["capo_securityhub.types.integer.Integer"] = None,
    ) -> "capo_securityhub.types.batch_update_findings_v2_response.BatchUpdateFindingsV2Response":
        """<p>Updates information about a customer's investigation into a finding. Delegated administrator accounts can update findings for their account and their member accounts. Member accounts can update findings for their own account.</p> <p> <code>BatchUpdateFindings</code> and <code>BatchUpdateFindingsV2</code> both use <code>securityhub:BatchUpdateFindings</code> in the <code>Action</code> element of an IAM policy statement. You must have permission to perform the <code>securityhub:BatchUpdateFindings</code> action. You can configure IAM policies to restrict access to specific finding fields or field values by using the <code>securityhub:OCSFSyntaxPath/<fieldName></code> condition key, where <code><fieldName></code> is one of the following supported fields: <code>SeverityId</code>, <code>StatusId</code>, or <code>Comment</code>.</p> <p>To prevent a user from updating a specific field, use a <code>Null</code> condition with <code>securityhub:OCSFSyntaxPath/<fieldName></code> set to <code>"false"</code>. To prevent a user from setting a field to a specific value, use a <code>StringEquals</code> condition with <code>securityhub:OCSFSyntaxPath/<fieldName></code> set to the disallowed value or list of values.</p> <p>Updates from <code>BatchUpdateFindingsV2</code> don't affect the value of <code>finding_info.modified_time</code>, <code>finding_info.modified_time_dt</code>, <code>time</code>, or <code>time_dt</code> for a finding.</p>

        Args:
            metadata_uids: <p>The list of finding <code>metadata.uid</code> to indicate findings to update. Finding <code>metadata.uid</code> is a globally unique identifier associated with the finding. Customers cannot use <code>MetadataUids</code> together with <code>FindingIdentifiers</code>.</p>
            finding_identifiers: <p>Provides information to identify a specific V2 finding.</p>
            comment: <p>The updated value for a user provided comment about the finding. Minimum character length 1. Maximum character length 512.</p>
            severity_id: <p>The updated value for the normalized severity identifier. The severity ID is an integer with the allowed enum values [0, 1, 2, 3, 4, 5, 6, 99]. When customer provides the updated severity ID, the string sibling severity will automatically be updated in the finding.</p>
            status_id: <p>The updated value for the normalized status identifier. The status ID is an integer with the allowed enum values [0, 1, 2, 3, 4, 5, 99]. When customer provides the updated status ID, the string sibling status will automatically be updated in the finding.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_update_findings_v2_request.BatchUpdateFindingsV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_update_findings_v2_response.BatchUpdateFindingsV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_update_findings_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_update_findings_v2.async_batch_update_findings_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_update_findings_v2_request.BatchUpdateFindingsV2Request = {}
        if metadata_uids is not None:
            input_["metadata_uids"] = metadata_uids
        if finding_identifiers is not None:
            input_["finding_identifiers"] = finding_identifiers
        if comment is not None:
            input_["comment"] = comment
        if severity_id is not None:
            input_["severity_id"] = severity_id
        if status_id is not None:
            input_["status_id"] = status_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_standards_control_associations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        standards_control_association_updates: Optional[
            "capo_securityhub.types.standards_control_association_updates.StandardsControlAssociationUpdates"
        ] = None,
    ) -> "capo_securityhub.types.batch_update_standards_control_associations_response.BatchUpdateStandardsControlAssociationsResponse":
        """<p> For a batch of security controls and standards, this operation updates the enablement status of a control in a standard. </p>

        Args:
            standards_control_association_updates: <p> Updates the enablement status of a security control in a specified standard. </p> <p> Calls to this operation return a <code>RESOURCE_NOT_FOUND_EXCEPTION</code> error when the standard subscription for the control has <code>StandardsControlsUpdatable</code> value <code>NOT_READY_FOR_UPDATES</code>. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update enablement status of a batch of controls
            The following example disables CloudWatch.12 in CIS AWS Foundations Benchmark v1.2.0. The example returns an error for CloudTrail.1 because an invalid standard ARN is provided.

            >>> await client.batch_update_standards_control_associations(standards_control_association_updates=[{'SecurityControlId': 'CloudTrail.1', 'StandardsArn': 'arn:aws:securityhub:::ruleset/sample-standard/v/1.1.0', 'AssociationStatus': 'DISABLED', 'UpdatedReason': 'Not relevant to environment'}, {'SecurityControlId': 'CloudWatch.12', 'StandardsArn': 'arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0', 'AssociationStatus': 'DISABLED', 'UpdatedReason': 'Not relevant to environment'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.batch_update_standards_control_associations_request.BatchUpdateStandardsControlAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.batch_update_standards_control_associations_response.BatchUpdateStandardsControlAssociationsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.batch_update_standards_control_associations

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.batch_update_standards_control_associations.async_batch_update_standards_control_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.batch_update_standards_control_associations_request.BatchUpdateStandardsControlAssociationsRequest = {}
        if standards_control_association_updates is not None:
            input_["standards_control_association_updates"] = (
                standards_control_association_updates
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_action_target(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        name: Optional["capo_securityhub.types.non_empty_string.NonEmptyString"] = None,
        description: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        id: Optional["capo_securityhub.types.non_empty_string.NonEmptyString"] = None,
    ) -> "capo_securityhub.types.create_action_target_response.CreateActionTargetResponse":
        """<p>Creates a custom action target in Security Hub CSPM.</p> <p>You can use custom actions on findings and insights in Security Hub CSPM to trigger target actions in Amazon CloudWatch Events.</p>

        Args:
            name: <p>The name of the custom action target. Can contain up to 20 characters.</p>
            description: <p>The description for the custom action target.</p>
            id: <p>The ID for the custom action target. Can contain up to 20 alphanumeric characters.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a custom action target
            The following example creates a custom action target in Security Hub. Custom actions on findings and insights automatically trigger actions in Amazon CloudWatch Events.

            >>> await client.create_action_target(name='Send to remediation', description='Action to send the finding for remediation tracking', id='Remediation')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.create_action_target_request.CreateActionTargetRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.create_action_target_response.CreateActionTargetResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.create_action_target

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.create_action_target.async_create_action_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.create_action_target_request.CreateActionTargetRequest = {}
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if id is not None:
            input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_aggregator_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        region_linking_mode: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        linked_regions: Optional[
            "capo_securityhub.types.string_list.StringList"
        ] = None,
        tags: Optional["capo_securityhub.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_securityhub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_securityhub.types.create_aggregator_v2_response.CreateAggregatorV2Response":
        """<p>Enables aggregation across Amazon Web Services Regions.</p>

        Args:
            region_linking_mode: <p>Determines how Regions are linked to an Aggregator V2.</p>
            linked_regions: <p>The list of Regions that are linked to the aggregation Region.</p>
            tags: <p>A list of key-value pairs to be applied to the AggregatorV2.</p>
            client_token: <p>A unique identifier used to ensure idempotency.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed the service quota limit.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.create_aggregator_v2_request.CreateAggregatorV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.create_aggregator_v2_response.CreateAggregatorV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.create_aggregator_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.create_aggregator_v2.async_create_aggregator_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.create_aggregator_v2_request.CreateAggregatorV2Request = {}
        if region_linking_mode is not None:
            input_["region_linking_mode"] = region_linking_mode
        if linked_regions is not None:
            input_["linked_regions"] = linked_regions
        if tags is not None:
            input_["tags"] = tags
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

    async def create_automation_rule(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        tags: Optional["capo_securityhub.types.tag_map.TagMap"] = None,
        rule_status: Optional["capo_securityhub.types.rule_status.RuleStatus"] = None,
        rule_order: Optional[
            "capo_securityhub.types.rule_order_value.RuleOrderValue"
        ] = None,
        rule_name: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        is_terminal: Optional["capo_securityhub.types.boolean.Boolean"] = None,
        criteria: Optional[
            "capo_securityhub.types.automation_rules_finding_filters.AutomationRulesFindingFilters"
        ] = None,
        actions: Optional["capo_securityhub.types.action_list.ActionList"] = None,
    ) -> "capo_securityhub.types.create_automation_rule_response.CreateAutomationRuleResponse":
        """<p> Creates an automation rule based on input parameters. </p>

        Args:
            tags: <p> User-defined tags associated with an automation rule. </p>
            rule_status: <p> Whether the rule is active after it is created. If this parameter is equal to <code>ENABLED</code>, Security Hub CSPM starts applying the rule to findings and finding updates after the rule is created. To change the value of this parameter after creating a rule, use <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateAutomationRules.html"> <code>BatchUpdateAutomationRules</code> </a>. </p>
            rule_order: <p>An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub CSPM applies rules with lower values for this parameter first. </p>
            rule_name: <p> The name of the rule. </p>
            description: <p> A description of the rule. </p>
            is_terminal: <p>Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub CSPM applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal. </p>
            criteria: <p> A set of ASFF finding field attributes and corresponding expected values that Security Hub CSPM uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub CSPM applies the rule action to the finding. </p>
            actions: <p> One or more actions to update finding fields if a finding matches the conditions specified in <code>Criteria</code>. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an automation rule
            The following example creates an automation rule.

            >>> await client.create_automation_rule(tags={'important-resources-rule': 's3-bucket'}, rule_status='ENABLED', rule_order=1, rule_name='Elevate severity for important resources', description='Elevate finding severity to Critical for important resources', is_terminal=False, criteria={'ProductName': [{'Value': 'Security Hub', 'Comparison': 'EQUALS'}], 'ComplianceStatus': [{'Value': 'FAILED', 'Comparison': 'EQUALS'}], 'RecordState': [{'Value': 'ACTIVE', 'Comparison': 'EQUALS'}], 'WorkflowStatus': [{'Value': 'NEW', 'Comparison': 'EQUALS'}], 'ResourceId': [{'Value': 'arn:aws:s3:::examplebucket/developers/design_info.doc', 'Comparison': 'EQUALS'}]}, actions=[{'Type': 'FINDING_FIELDS_UPDATE', 'FindingFieldsUpdate': {'Severity': {'Label': 'CRITICAL'}, 'Note': {'Text': 'This is a critical S3 bucket, please look into this ASAP', 'UpdatedBy': 'test-user'}}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.create_automation_rule_request.CreateAutomationRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.create_automation_rule_response.CreateAutomationRuleResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.create_automation_rule

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.create_automation_rule.async_create_automation_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.create_automation_rule_request.CreateAutomationRuleRequest = {}
        if tags is not None:
            input_["tags"] = tags
        if rule_status is not None:
            input_["rule_status"] = rule_status
        if rule_order is not None:
            input_["rule_order"] = rule_order
        if rule_name is not None:
            input_["rule_name"] = rule_name
        if description is not None:
            input_["description"] = description
        if is_terminal is not None:
            input_["is_terminal"] = is_terminal
        if criteria is not None:
            input_["criteria"] = criteria
        if actions is not None:
            input_["actions"] = actions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_automation_rule_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        rule_name: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        rule_status: Optional[
            "capo_securityhub.types.rule_status_v2.RuleStatusV2"
        ] = None,
        description: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        rule_order: Optional[
            "capo_securityhub.types.rule_order_value_v2.RuleOrderValueV2"
        ] = None,
        criteria: Optional["capo_securityhub.types.criteria.Criteria"] = None,
        actions: Optional[
            "capo_securityhub.types.automation_rules_action_list_v2.AutomationRulesActionListV2"
        ] = None,
        tags: Optional["capo_securityhub.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_securityhub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_securityhub.types.create_automation_rule_v2_response.CreateAutomationRuleV2Response":
        """<p>Creates a V2 automation rule.</p>

        Args:
            rule_name: <p>The name of the V2 automation rule.</p>
            rule_status: <p>The status of the V2 automation rule.</p>
            description: <p>A description of the V2 automation rule.</p>
            rule_order: <p>The value for the rule priority.</p>
            criteria: <p>The filtering type and configuration of the automation rule.</p>
            actions: <p>A list of actions to be performed when the rule criteria is met.</p>
            tags: <p>A list of key-value pairs associated with the V2 automation rule.</p>
            client_token: <p>A unique identifier used to ensure idempotency.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed the service quota limit.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.create_automation_rule_v2_request.CreateAutomationRuleV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.create_automation_rule_v2_response.CreateAutomationRuleV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.create_automation_rule_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.create_automation_rule_v2.async_create_automation_rule_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.create_automation_rule_v2_request.CreateAutomationRuleV2Request = {}
        if rule_name is not None:
            input_["rule_name"] = rule_name
        if rule_status is not None:
            input_["rule_status"] = rule_status
        if description is not None:
            input_["description"] = description
        if rule_order is not None:
            input_["rule_order"] = rule_order
        if criteria is not None:
            input_["criteria"] = criteria
        if actions is not None:
            input_["actions"] = actions
        if tags is not None:
            input_["tags"] = tags
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

    async def create_configuration_policy(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        name: Optional["capo_securityhub.types.non_empty_string.NonEmptyString"] = None,
        description: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        configuration_policy: Optional["capo_securityhub.types.policy.Policy"] = None,
        tags: Optional["capo_securityhub.types.tag_map.TagMap"] = None,
    ) -> "capo_securityhub.types.create_configuration_policy_response.CreateConfigurationPolicyResponse":
        """<p> Creates a configuration policy with the defined configuration. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            name: <p> The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: <code>-, ., !, *, /</code>. </p>
            description: <p> The description of the configuration policy. </p>
            configuration_policy: <p> An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls). </p>
            tags: <p> User-defined tags associated with a configuration policy. For more information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/tagging-resources.html">Tagging Security Hub CSPM resources</a> in the <i>Security Hub CSPM user guide</i>. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a configuration policy
            This operation creates a configuration policy in Security Hub.

            >>> await client.create_configuration_policy(name='TestConfigurationPolicy', description='Configuration policy for testing FSBP and CIS', configuration_policy={'SecurityHub': {'ServiceEnabled': True, 'EnabledStandardIdentifiers': ['arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0', 'arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0'], 'SecurityControlsConfiguration': {'DisabledSecurityControlIdentifiers': ['CloudWatch.1'], 'SecurityControlCustomParameters': [{'SecurityControlId': 'ACM.1', 'Parameters': {'daysToExpiration': {'ValueType': 'CUSTOM', 'Value': {'Integer': 14}}}}]}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.create_configuration_policy_request.CreateConfigurationPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.create_configuration_policy_response.CreateConfigurationPolicyResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.create_configuration_policy

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.create_configuration_policy.async_create_configuration_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.create_configuration_policy_request.CreateConfigurationPolicyRequest = {}
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if configuration_policy is not None:
            input_["configuration_policy"] = configuration_policy
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_connector(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        name: Optional["capo_securityhub.types.non_empty_string.NonEmptyString"] = None,
        description: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        provider: Optional[
            "capo_securityhub.types.cspm_provider_configuration.CspmProviderConfiguration"
        ] = None,
        tags: Optional["capo_securityhub.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_securityhub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_securityhub.types.create_connector_response.CreateConnectorResponse":
        """<p>Creates a connector to a third-party cloud provider in Security Hub CSPM. A connector establishes a connection between Security Hub CSPM and a third-party cloud provider, enabling Security Hub CSPM to ingest security findings and resource data from the connected environment.</p>

        Args:
            name: <p>The name of the connector. Must be unique within the account.</p>
            description: <p>The description of the connector.</p>
            provider: <p>The configuration for the cloud provider to connect to. Currently supports Azure.</p>
            tags: <p>The tags to add to the connector resource.</p>
            client_token: <p>A unique identifier used to ensure idempotency of the request.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed the service quota limit.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a CSPM connector
            This operation creates a CSPM connector to connect Security Hub to an Azure environment.

            >>> await client.create_connector(name='MyAzureConnector', description='Connector for Azure tenant monitoring', provider={'Azure': {'AWSConfigConnectorArn': 'arn:aws:config:us-east-1:123456789012:connector/azure-connector-1234', 'ScopeConfiguration': {'ScopeType': 'TENANT'}, 'AzureRegions': ['eastus', 'westus2']}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.create_connector_request.CreateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.create_connector_response.CreateConnectorResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.create_connector

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.create_connector.async_create_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.create_connector_request.CreateConnectorRequest = {}
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if provider is not None:
            input_["provider"] = provider
        if tags is not None:
            input_["tags"] = tags
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

    async def create_connector_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        name: Optional["capo_securityhub.types.non_empty_string.NonEmptyString"] = None,
        description: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        provider: Optional[
            "capo_securityhub.types.provider_configuration.ProviderConfiguration"
        ] = None,
        kms_key_arn: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_securityhub.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_securityhub.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_securityhub.types.create_connector_v2_response.CreateConnectorV2Response"
    ):
        """<p>Grants permission to create a connectorV2 based on input parameters.</p>

        Args:
            name: <p>The unique name of the connectorV2.</p>
            description: <p>The description of the connectorV2.</p>
            provider: <p>The third-party provider’s service configuration.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of KMS key used to encrypt secrets for the connectorV2.</p>
            tags: <p>The tags to add to the connectorV2 when you create.</p>
            client_token: <p>A unique identifier used to ensure idempotency.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed the service quota limit.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.create_connector_v2_request.CreateConnectorV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.create_connector_v2_response.CreateConnectorV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.create_connector_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.create_connector_v2.async_create_connector_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.create_connector_v2_request.CreateConnectorV2Request = {}
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if provider is not None:
            input_["provider"] = provider
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
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

    async def create_finding_aggregator(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        region_linking_mode: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        regions: Optional["capo_securityhub.types.string_list.StringList"] = None,
    ) -> "capo_securityhub.types.create_finding_aggregator_response.CreateFindingAggregatorResponse":
        """<note> <p>The <i>aggregation Region</i> is now called the <i>home Region</i>.</p> </note> <p>Used to enable cross-Region aggregation. This operation can be invoked from the home Region only.</p> <p>For information about how cross-Region aggregation works, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html">Understanding cross-Region aggregation in Security Hub CSPM</a> in the <i>Security Hub CSPM User Guide</i>. </p>

        Args:
            region_linking_mode: <p>Indicates whether to aggregate findings from all of the available Regions in the current partition. Also determines whether to automatically aggregate findings from new Regions as Security Hub CSPM supports them and you opt into them.</p> <p>The selected option also determines how to use the Regions provided in the Regions list.</p> <p>The options are as follows:</p> <ul> <li> <p> <code>ALL_REGIONS</code> - Aggregates findings from all of the Regions where Security Hub CSPM is enabled. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them. </p> </li> <li> <p> <code>ALL_REGIONS_EXCEPT_SPECIFIED</code> - Aggregates findings from all of the Regions where Security Hub CSPM is enabled, except for the Regions listed in the <code>Regions</code> parameter. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them. </p> </li> <li> <p> <code>SPECIFIED_REGIONS</code> - Aggregates findings only from the Regions listed in the <code>Regions</code> parameter. Security Hub CSPM does not automatically aggregate findings from new Regions. </p> </li> <li> <p> <code>NO_REGIONS</code> - Aggregates no data because no Regions are selected as linked Regions. </p> </li> </ul>
            regions: <p>If <code>RegionLinkingMode</code> is <code>ALL_REGIONS_EXCEPT_SPECIFIED</code>, then this is a space-separated list of Regions that don't replicate and send findings to the home Region.</p> <p>If <code>RegionLinkingMode</code> is <code>SPECIFIED_REGIONS</code>, then this is a space-separated list of Regions that do replicate and send findings to the home Region. </p> <p>An <code>InvalidInputException</code> error results if you populate this field while <code>RegionLinkingMode</code> is <code>NO_REGIONS</code>.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable cross-Region aggregation
            The following example creates a finding aggregator. This is required to enable cross-Region aggregation.

            >>> await client.create_finding_aggregator(region_linking_mode='SPECIFIED_REGIONS', regions=['us-west-1', 'us-west-2'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.create_finding_aggregator_request.CreateFindingAggregatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.create_finding_aggregator_response.CreateFindingAggregatorResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.create_finding_aggregator

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.create_finding_aggregator.async_create_finding_aggregator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.create_finding_aggregator_request.CreateFindingAggregatorRequest = {}
        if region_linking_mode is not None:
            input_["region_linking_mode"] = region_linking_mode
        if regions is not None:
            input_["regions"] = regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_insight(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        name: Optional["capo_securityhub.types.non_empty_string.NonEmptyString"] = None,
        filters: Optional[
            "capo_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
        ] = None,
        group_by_attribute: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.create_insight_response.CreateInsightResponse":
        """<p>Creates a custom insight in Security Hub CSPM. An insight is a consolidation of findings that relate to a security issue that requires attention or remediation.</p> <p>To group the related findings in the insight, use the <code>GroupByAttribute</code>.</p>

        Args:
            name: <p>The name of the custom insight to create.</p>
            filters: <p>One or more attributes used to filter the findings included in the insight. The insight only includes findings that match the criteria defined in the filters.</p>
            group_by_attribute: <p>The attribute used to group the findings for the insight. The grouping attribute identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a custom insight
            The following example creates a custom insight in Security Hub. An insight is a collection of findings that relate to a security issue.

            >>> await client.create_insight(name='Critical role findings', filters={'ResourceType': [{'Comparison': 'EQUALS', 'Value': 'AwsIamRole'}], 'SeverityLabel': [{'Comparison': 'EQUALS', 'Value': 'CRITICAL'}]}, group_by_attribute='ResourceId')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.create_insight_request.CreateInsightRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.create_insight_response.CreateInsightResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.create_insight

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.create_insight.async_create_insight(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.create_insight_request.CreateInsightRequest = {}
        if name is not None:
            input_["name"] = name
        if filters is not None:
            input_["filters"] = filters
        if group_by_attribute is not None:
            input_["group_by_attribute"] = group_by_attribute

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_members(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        account_details: Optional[
            "capo_securityhub.types.account_details_list.AccountDetailsList"
        ] = None,
    ) -> "capo_securityhub.types.create_members_response.CreateMembersResponse":
        """<p>Creates a member association in Security Hub CSPM between the specified accounts and the account used to make the request, which is the administrator account. If you are integrated with Organizations, then the administrator account is designated by the organization management account.</p> <p> <code>CreateMembers</code> is always used to add accounts that are not organization members.</p> <p>For accounts that are managed using Organizations, <code>CreateMembers</code> is only used in the following cases:</p> <ul> <li> <p>Security Hub CSPM is not configured to automatically add new organization accounts.</p> </li> <li> <p>The account was disassociated or deleted in Security Hub CSPM.</p> </li> </ul> <p>This action can only be used by an account that has Security Hub CSPM enabled. To enable Security Hub CSPM, you can use the <code>EnableSecurityHub</code> operation.</p> <p>For accounts that are not organization members, you create the account association and then send an invitation to the member account. To send the invitation, you use the <code>InviteMembers</code> operation. If the account owner accepts the invitation, the account becomes a member account in Security Hub CSPM.</p> <p>Accounts that are managed using Organizations don't receive an invitation. They automatically become a member account in Security Hub CSPM.</p> <ul> <li> <p>If the organization account does not have Security Hub CSPM enabled, then Security Hub CSPM and the default standards are automatically enabled. Note that Security Hub CSPM cannot be enabled automatically for the organization management account. The organization management account must enable Security Hub CSPM before the administrator account enables it as a member account.</p> </li> <li> <p>For organization accounts that already have Security Hub CSPM enabled, Security Hub CSPM does not make any other changes to those accounts. It does not change their enabled standards or controls.</p> </li> </ul> <p>A permissions policy is added that permits the administrator account to view the findings generated in the member account.</p> <p>To remove the association between the administrator and member accounts, use the <code>DisassociateFromMasterAccount</code> or <code>DisassociateMembers</code> operation.</p>

        Args:
            account_details: <p>The list of accounts to associate with the Security Hub CSPM administrator account. For each account, the list includes the account ID and optionally the email address.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add a member account
            The following example creates a member association between the specified accounts and the administrator account (the account that makes the request). This operation is used to add accounts that aren't part of an organization.

            >>> await client.create_members(account_details=[{'AccountId': '123456789012'}, {'AccountId': '111122223333'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.create_members_request.CreateMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.create_members_response.CreateMembersResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.create_members

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.create_members.async_create_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.create_members_request.CreateMembersRequest = {}
        if account_details is not None:
            input_["account_details"] = account_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_ticket_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        connector_id: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        finding_metadata_uid: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        client_token: Optional[
            "capo_securityhub.types.client_token.ClientToken"
        ] = None,
        mode: Optional[
            "capo_securityhub.types.ticket_creation_mode.TicketCreationMode"
        ] = None,
    ) -> "capo_securityhub.types.create_ticket_v2_response.CreateTicketV2Response":
        """<p>Grants permission to create a ticket in the chosen ITSM based on finding information for the provided finding metadata UID.</p>

        Args:
            connector_id: <p>The UUID of the connectorV2 to identify connectorV2 resource.</p>
            finding_metadata_uid: <p>The the unique ID for the finding.</p>
            client_token: <p>The client idempotency token.</p>
            mode: <p>The mode for ticket creation. When set to DRYRUN, the ticket is created using a Security Hub owned template test finding to verify the integration is working correctly.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.create_ticket_v2_request.CreateTicketV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.create_ticket_v2_response.CreateTicketV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.create_ticket_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.create_ticket_v2.async_create_ticket_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.create_ticket_v2_request.CreateTicketV2Request = {}
        if connector_id is not None:
            input_["connector_id"] = connector_id
        if finding_metadata_uid is not None:
            input_["finding_metadata_uid"] = finding_metadata_uid
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mode is not None:
            input_["mode"] = mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def decline_invitations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        account_ids: Optional[
            "capo_securityhub.types.account_id_list.AccountIdList"
        ] = None,
    ) -> (
        "capo_securityhub.types.decline_invitations_response.DeclineInvitationsResponse"
    ):
        """<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Declines invitations to become a Security Hub CSPM member account.</p> <p>A prospective member account uses this operation to decline an invitation to become a member.</p> <p>Only member accounts that aren't part of an Amazon Web Services organization should use this operation. Organization accounts don't receive invitations.</p>

        Args:
            account_ids: <p>The list of prospective member account IDs for which to decline an invitation.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To decline invitation to become a member account
            The following example declines an invitation from the Security Hub administrator account to become a member account. The invited account makes the request.

            >>> await client.decline_invitations(account_ids=['123456789012', '111122223333'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.decline_invitations_request.DeclineInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.decline_invitations_response.DeclineInvitationsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.decline_invitations

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.decline_invitations.async_decline_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.decline_invitations_request.DeclineInvitationsRequest = {}
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_action_target(
        self,
        action_target_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.delete_action_target_response.DeleteActionTargetResponse":
        """<p>Deletes a custom action target from Security Hub CSPM.</p> <p>Deleting a custom action target does not affect any findings or insights that were already sent to Amazon CloudWatch Events using the custom action.</p>

        Args:
            action_target_arn: <p>The Amazon Resource Name (ARN) of the custom action target to delete.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a custom action target
            The following example deletes a custom action target that triggers target actions in Amazon CloudWatch Events. Deleting a custom action target doesn't affect findings or insights that were already sent to CloudWatch Events based on the custom action.

            >>> await client.delete_action_target(action_target_arn='arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.delete_action_target_request.DeleteActionTargetRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.delete_action_target_response.DeleteActionTargetResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.delete_action_target

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.delete_action_target.async_delete_action_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.delete_action_target_request.DeleteActionTargetRequest = {
            "action_target_arn": action_target_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_aggregator_v2(
        self,
        aggregator_v2_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.delete_aggregator_v2_response.DeleteAggregatorV2Response":
        """<p>Deletes the Aggregator V2.</p>

        Args:
            aggregator_v2_arn: <p>The ARN of the Aggregator V2.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.delete_aggregator_v2_request.DeleteAggregatorV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.delete_aggregator_v2_response.DeleteAggregatorV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.delete_aggregator_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.delete_aggregator_v2.async_delete_aggregator_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.delete_aggregator_v2_request.DeleteAggregatorV2Request = {
            "aggregator_v2_arn": aggregator_v2_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_automation_rule_v2(
        self,
        identifier: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.delete_automation_rule_v2_response.DeleteAutomationRuleV2Response":
        """<p>Deletes a V2 automation rule.</p>

        Args:
            identifier: <p>The ARN of the V2 automation rule.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.delete_automation_rule_v2_request.DeleteAutomationRuleV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.delete_automation_rule_v2_response.DeleteAutomationRuleV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.delete_automation_rule_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.delete_automation_rule_v2.async_delete_automation_rule_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.delete_automation_rule_v2_request.DeleteAutomationRuleV2Request = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_policy(
        self,
        identifier: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.delete_configuration_policy_response.DeleteConfigurationPolicyResponse":
        """<p> Deletes a configuration policy. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. For the deletion to succeed, you must first disassociate a configuration policy from target accounts, organizational units, or the root by invoking the <code>StartConfigurationPolicyDisassociation</code> operation. </p>

        Args:
            identifier: <p> The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a configuration policy
            This operation deletes the specified configuration policy.

            >>> await client.delete_configuration_policy(identifier='arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.delete_configuration_policy_request.DeleteConfigurationPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.delete_configuration_policy_response.DeleteConfigurationPolicyResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.delete_configuration_policy

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.delete_configuration_policy.async_delete_configuration_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.delete_configuration_policy_request.DeleteConfigurationPolicyRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connector(
        self,
        connector_id: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.delete_connector_response.DeleteConnectorResponse":
        """<p>Deletes a CSPM connector. When you delete a connector, Security Hub CSPM stops ingesting findings and resource data from the connected cloud provider environment.</p>

        Args:
            connector_id: <p>The unique identifier of the connector to delete.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a CSPM connector
            This operation deletes a CSPM connector.

            >>> await client.delete_connector(connector_id='cspm-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.delete_connector_response.DeleteConnectorResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.delete_connector

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.delete_connector.async_delete_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.delete_connector_request.DeleteConnectorRequest = {
            "connector_id": connector_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connector_v2(
        self,
        connector_id: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> (
        "capo_securityhub.types.delete_connector_v2_response.DeleteConnectorV2Response"
    ):
        """<p>Grants permission to delete a connectorV2.</p>

        Args:
            connector_id: <p>The UUID of the connectorV2 to identify connectorV2 resource.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.delete_connector_v2_request.DeleteConnectorV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.delete_connector_v2_response.DeleteConnectorV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.delete_connector_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.delete_connector_v2.async_delete_connector_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.delete_connector_v2_request.DeleteConnectorV2Request = {
            "connector_id": connector_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_finding_aggregator(
        self,
        finding_aggregator_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.delete_finding_aggregator_response.DeleteFindingAggregatorResponse":
        """<note> <p>The <i>aggregation Region</i> is now called the <i>home Region</i>.</p> </note> <p>Deletes a finding aggregator. When you delete the finding aggregator, you stop cross-Region aggregation. Finding replication stops occurring from the linked Regions to the home Region.</p> <p>When you stop cross-Region aggregation, findings that were already replicated and sent to the home Region are still visible from the home Region. However, new findings and finding updates are no longer replicated and sent to the home Region. </p>

        Args:
            finding_aggregator_arn: <p>The ARN of the finding aggregator to delete. To obtain the ARN, use <code>ListFindingAggregators</code>.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a finding aggregator
            The following example deletes a finding aggregator in Security Hub. Deleting the finding aggregator stops cross-Region aggregation. This operation produces no output.

            >>> await client.delete_finding_aggregator(finding_aggregator_arn='arn:aws:securityhub:us-east-1:123456789012:finding-aggregator/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.delete_finding_aggregator_request.DeleteFindingAggregatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.delete_finding_aggregator_response.DeleteFindingAggregatorResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.delete_finding_aggregator

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.delete_finding_aggregator.async_delete_finding_aggregator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.delete_finding_aggregator_request.DeleteFindingAggregatorRequest = {
            "finding_aggregator_arn": finding_aggregator_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_insight(
        self,
        insight_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.delete_insight_response.DeleteInsightResponse":
        """<p>Deletes the insight specified by the <code>InsightArn</code>.</p>

        Args:
            insight_arn: <p>The ARN of the insight to delete.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a custom insight
            The following example deletes a custom insight in Security Hub.

            >>> await client.delete_insight(insight_arn='arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.delete_insight_request.DeleteInsightRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.delete_insight_response.DeleteInsightResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.delete_insight

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.delete_insight.async_delete_insight(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.delete_insight_request.DeleteInsightRequest = {
            "insight_arn": insight_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_invitations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        account_ids: Optional[
            "capo_securityhub.types.account_id_list.AccountIdList"
        ] = None,
    ) -> "capo_securityhub.types.delete_invitations_response.DeleteInvitationsResponse":
        """<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Deletes invitations to become a Security Hub CSPM member account.</p> <p>A Security Hub CSPM administrator account can use this operation to delete invitations sent to one or more prospective member accounts.</p> <p>This operation is only used to delete invitations that are sent to prospective member accounts that aren't part of an Amazon Web Services organization. Organization accounts don't receive invitations.</p>

        Args:
            account_ids: <p>The list of member account IDs that received the invitations you want to delete.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a custom insight
            The following example deletes an invitation sent by the Security Hub administrator account to a prospective member account. This operation is used only for invitations sent to accounts that aren't part of an organization. Organization accounts don't receive invitations.

            >>> await client.delete_invitations(account_ids=['123456789012'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.delete_invitations_request.DeleteInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.delete_invitations_response.DeleteInvitationsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.delete_invitations

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.delete_invitations.async_delete_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.delete_invitations_request.DeleteInvitationsRequest = {}
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_members(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        account_ids: Optional[
            "capo_securityhub.types.account_id_list.AccountIdList"
        ] = None,
    ) -> "capo_securityhub.types.delete_members_response.DeleteMembersResponse":
        """<p>Deletes the specified member accounts from Security Hub CSPM.</p> <p>You can invoke this API only to delete accounts that became members through invitation. You can't invoke this API to delete accounts that belong to an Organizations organization.</p>

        Args:
            account_ids: <p>The list of account IDs for the member accounts to delete.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a member account
            The following example deletes the specified member account from Security Hub. This operation can be used to delete member accounts that are part of an organization or that were invited manually.

            >>> await client.delete_members(account_ids=['123456789111', '123456789222'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.delete_members_request.DeleteMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.delete_members_response.DeleteMembersResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.delete_members

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.delete_members.async_delete_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.delete_members_request.DeleteMembersRequest = {}
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_action_targets(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        action_target_arns: Optional["capo_securityhub.types.arn_list.ArnList"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.describe_action_targets_response.DescribeActionTargetsResponse":
        """<p>Returns a list of the custom action targets in Security Hub CSPM in your account.</p>

        Args:
            action_target_arns: <p>A list of custom action target ARNs for the custom action targets to retrieve.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>DescribeActionTargets</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To return custom action targets
            The following example returns a list of custom action targets. You use custom actions on findings and insights in Security Hub to trigger target actions in Amazon CloudWatch Events.

            >>> await client.describe_action_targets(action_target_arns=['arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.describe_action_targets_request.DescribeActionTargetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.describe_action_targets_response.DescribeActionTargetsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.describe_action_targets

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.describe_action_targets.async_describe_action_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.describe_action_targets_request.DescribeActionTargetsRequest = {}
        if action_target_arns is not None:
            input_["action_target_arns"] = action_target_arns
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

    async def iter_describe_action_targets(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        action_target_arns: Optional["capo_securityhub.types.arn_list.ArnList"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.action_target.ActionTarget]":
        _token = next_token
        while True:
            _response = await self.describe_action_targets(
                config_overrides=config_overrides,
                action_target_arns=action_target_arns,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("action_targets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_hub(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        hub_arn: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.describe_hub_response.DescribeHubResponse":
        """<p>Returns details about the Hub resource in your account, including the <code>HubArn</code> and the time when you enabled Security Hub CSPM.</p>

        Args:
            hub_arn: <p>The ARN of the Hub resource to retrieve.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To return details about Hub resource
            The following example returns details about the Hub resource in the calling account. The Hub resource represents the implementation of  the AWS Security Hub service in the calling account.

            >>> await client.describe_hub(hub_arn='arn:aws:securityhub:us-west-1:123456789012:hub/default')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.describe_hub_request.DescribeHubRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.describe_hub_response.DescribeHubResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.describe_hub

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.describe_hub.async_describe_hub(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.describe_hub_request.DescribeHubRequest = {}
        if hub_arn is not None:
            input_["hub_arn"] = hub_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_organization_configuration(
        self, *, config_overrides: Optional[AsyncSecurityHubClientConfig] = None
    ) -> "capo_securityhub.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse":
        """<p>Returns information about the way your organization is configured in Security Hub CSPM. Only the Security Hub CSPM administrator account can invoke this operation.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about organization configuration
            This operation provides information about the way your organization is configured in Security Hub. Only a Security Hub administrator account can invoke this operation.

            >>> await client.describe_organization_configuration()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.describe_organization_configuration

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.describe_organization_configuration.async_describe_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_products(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        product_arn: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.describe_products_response.DescribeProductsResponse":
        """<p>Returns information about product integrations in Security Hub CSPM.</p> <p>You can optionally provide an integration ARN. If you provide an integration ARN, then the results only include that integration.</p> <p>If you don't provide an integration ARN, then the results include all of the available product integrations. </p>

        Args:
            next_token: <p>The token that is required for pagination. On your first call to the <code>DescribeProducts</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>
            product_arn: <p>The ARN of the integration to return.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about Security Hub integrations
            The following example returns details about AWS services and third-party products that Security Hub integrates with.

            >>> await client.describe_products(next_token='NULL', max_results=1, product_arn='arn:aws:securityhub:us-east-1:517716713836:product/crowdstrike/crowdstrike-falcon')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.describe_products_request.DescribeProductsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.describe_products_response.DescribeProductsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.describe_products

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.describe_products.async_describe_products(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.describe_products_request.DescribeProductsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if product_arn is not None:
            input_["product_arn"] = product_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_products(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        product_arn: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "AsyncIterator[capo_securityhub.types.product.Product]":
        _token = next_token
        while True:
            _response = await self.describe_products(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                product_arn=product_arn,
            )
            _page = _resolve_path(_response, ("products",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_products_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.describe_products_v2_response.DescribeProductsV2Response":
        """<p>Gets information about the product integration.</p>

        Args:
            next_token: <p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.describe_products_v2_request.DescribeProductsV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.describe_products_v2_response.DescribeProductsV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.describe_products_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.describe_products_v2.async_describe_products_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.describe_products_v2_request.DescribeProductsV2Request = {}
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

    async def iter_describe_products_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.product_v2.ProductV2]":
        _token = next_token
        while True:
            _response = await self.describe_products_v2(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("products_v2",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_security_hub_v2(
        self, *, config_overrides: Optional[AsyncSecurityHubClientConfig] = None
    ) -> "capo_securityhub.types.describe_security_hub_v2_response.DescribeSecurityHubV2Response":
        """<p>Returns details about the service resource in your account.</p>

        Raises:
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.describe_security_hub_v2_request.DescribeSecurityHubV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.describe_security_hub_v2_response.DescribeSecurityHubV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.describe_security_hub_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.describe_security_hub_v2.async_describe_security_hub_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.describe_security_hub_v2_request.DescribeSecurityHubV2Request = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_standards(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        providers: Optional[
            "capo_securityhub.types.standards_providers.StandardsProviders"
        ] = None,
    ) -> "capo_securityhub.types.describe_standards_response.DescribeStandardsResponse":
        """<p>Returns a list of the available standards in Security Hub CSPM.</p> <p>For each standard, the results include the standard ARN, the name, and a description. </p>

        Args:
            next_token: <p>The token that is required for pagination. On your first call to the <code>DescribeStandards</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of standards to return.</p>
            providers: <p>A list of cloud providers to filter the standards by. For example, specify <code>Azure</code> to return only standards that evaluate Azure resources.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get available Azure security standards
            The following example returns a list of available security standards from a specified provider.

            >>> await client.describe_standards(providers=['Azure'])
            To get available Security Hub standards
            The following example returns a list of available security standards in Security Hub.

            >>> await client.describe_standards()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.describe_standards_request.DescribeStandardsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.describe_standards_response.DescribeStandardsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.describe_standards

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.describe_standards.async_describe_standards(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.describe_standards_request.DescribeStandardsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if providers is not None:
            input_["providers"] = providers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_standards(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        providers: Optional[
            "capo_securityhub.types.standards_providers.StandardsProviders"
        ] = None,
    ) -> "AsyncIterator[capo_securityhub.types.standard.Standard]":
        _token = next_token
        while True:
            _response = await self.describe_standards(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                providers=providers,
            )
            _page = _resolve_path(_response, ("standards",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_standards_controls(
        self,
        standards_subscription_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.describe_standards_controls_response.DescribeStandardsControlsResponse":
        """<p>Returns a list of security standards controls.</p> <p>For each control, the results include information about whether it is currently enabled, the severity, and a link to remediation information.</p> <p>This operation returns an empty list for standard subscriptions where <code>StandardsControlsUpdatable</code> has value <code>NOT_READY_FOR_UPDATES</code>.</p>

        Args:
            standards_subscription_arn: <p>The ARN of a resource that represents your subscription to a supported standard. To get the subscription ARNs of the standards you have enabled, use the <code>GetEnabledStandards</code> operation.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>DescribeStandardsControls</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of security standard controls to return.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.describe_standards_controls_request.DescribeStandardsControlsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.describe_standards_controls_response.DescribeStandardsControlsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.describe_standards_controls

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.describe_standards_controls.async_describe_standards_controls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.describe_standards_controls_request.DescribeStandardsControlsRequest = {
            "standards_subscription_arn": standards_subscription_arn
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

    async def iter_describe_standards_controls(
        self,
        standards_subscription_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.standards_control.StandardsControl]":
        _token = next_token
        while True:
            _response = await self.describe_standards_controls(
                standards_subscription_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("controls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disable_import_findings_for_product(
        self,
        product_subscription_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.disable_import_findings_for_product_response.DisableImportFindingsForProductResponse":
        """<p>Disables the integration of the specified product with Security Hub CSPM. After the integration is disabled, findings from that product are no longer sent to Security Hub CSPM.</p>

        Args:
            product_subscription_arn: <p>The ARN of the integrated product to disable the integration for.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To end a Security Hub integration
            The following example ends an integration between Security Hub and the specified product that sends findings to Security Hub. After the integration ends, the product no longer sends findings to Security  Hub.

            >>> await client.disable_import_findings_for_product(product_subscription_arn='arn:aws:securityhub:us-east-1:517716713836:product/crowdstrike/crowdstrike-falcon')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.disable_import_findings_for_product_request.DisableImportFindingsForProductRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.disable_import_findings_for_product_response.DisableImportFindingsForProductResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.disable_import_findings_for_product

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.disable_import_findings_for_product.async_disable_import_findings_for_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.disable_import_findings_for_product_request.DisableImportFindingsForProductRequest = {
            "product_subscription_arn": product_subscription_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_organization_admin_account(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        admin_account_id: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        feature: Optional[
            "capo_securityhub.types.security_hub_feature.SecurityHubFeature"
        ] = None,
    ) -> "capo_securityhub.types.disable_organization_admin_account_response.DisableOrganizationAdminAccountResponse":
        """<p>Disables a Security Hub CSPM administrator account. Can only be called by the organization management account.</p>

        Args:
            admin_account_id: <p>The Amazon Web Services account identifier of the Security Hub CSPM administrator account.</p>
            feature: <p>The feature for which the delegated admin account is disabled. Defaults to Security Hub CSPM if not specified.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove a Security Hub administrator account
            The following example removes the Security Hub administrator account in the Region from which the operation was executed. This operation doesn't remove the delegated administrator account in AWS Organizations.

            >>> await client.disable_organization_admin_account(admin_account_id='123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.disable_organization_admin_account_request.DisableOrganizationAdminAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.disable_organization_admin_account_response.DisableOrganizationAdminAccountResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.disable_organization_admin_account

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.disable_organization_admin_account.async_disable_organization_admin_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.disable_organization_admin_account_request.DisableOrganizationAdminAccountRequest = {}
        if admin_account_id is not None:
            input_["admin_account_id"] = admin_account_id
        if feature is not None:
            input_["feature"] = feature

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_security_hub(
        self, *, config_overrides: Optional[AsyncSecurityHubClientConfig] = None
    ) -> "capo_securityhub.types.disable_security_hub_response.DisableSecurityHubResponse":
        """<p>Disables Security Hub CSPM in your account only in the current Amazon Web Services Region. To disable Security Hub CSPM in all Regions, you must submit one request per Region where you have enabled Security Hub CSPM.</p> <p>You can't disable Security Hub CSPM in an account that is currently the Security Hub CSPM administrator.</p> <p>When you disable Security Hub CSPM, your existing findings and insights and any Security Hub CSPM configuration settings are deleted after 90 days and cannot be recovered. Any standards that were enabled are disabled, and your administrator and member account associations are removed.</p> <p>If you want to save your existing findings, you must export them before you disable Security Hub CSPM.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To deactivate Security Hub
            The following example deactivates Security Hub for the current account and Region.

            >>> await client.disable_security_hub()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.disable_security_hub_request.DisableSecurityHubRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.disable_security_hub_response.DisableSecurityHubResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.disable_security_hub

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.disable_security_hub.async_disable_security_hub(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.disable_security_hub_request.DisableSecurityHubRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_security_hub_feature_v2(
        self,
        feature_name: "capo_securityhub.types.feature_name.FeatureName",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.disable_security_hub_feature_v2_response.DisableSecurityHubFeatureV2Response":
        """<p>Disables an opt-in feature for the calling account in the current Amazon Web Services Region. The operation is idempotent. If the feature is already disabled, no changes are made. You cannot disable a feature that is managed by an organization policy.</p>

        Args:
            feature_name: <p>The name of the feature to disable.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.disable_security_hub_feature_v2_request.DisableSecurityHubFeatureV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.disable_security_hub_feature_v2_response.DisableSecurityHubFeatureV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.disable_security_hub_feature_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.disable_security_hub_feature_v2.async_disable_security_hub_feature_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.disable_security_hub_feature_v2_request.DisableSecurityHubFeatureV2Request = {
            "feature_name": feature_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_security_hub_v2(
        self, *, config_overrides: Optional[AsyncSecurityHubClientConfig] = None
    ) -> "capo_securityhub.types.disable_security_hub_v2_response.DisableSecurityHubV2Response":
        """<p>Disable the service for the current Amazon Web Services Region or specified Amazon Web Services Region. Disabling the service also disables all opt-in features that are currently enabled in that Region.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.disable_security_hub_v2_request.DisableSecurityHubV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.disable_security_hub_v2_response.DisableSecurityHubV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.disable_security_hub_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.disable_security_hub_v2.async_disable_security_hub_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.disable_security_hub_v2_request.DisableSecurityHubV2Request = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_from_administrator_account(
        self, *, config_overrides: Optional[AsyncSecurityHubClientConfig] = None
    ) -> "capo_securityhub.types.disassociate_from_administrator_account_response.DisassociateFromAdministratorAccountResponse":
        """<p>Disassociates the current Security Hub CSPM member account from the associated administrator account.</p> <p>This operation is only used by accounts that are not part of an organization. For organization accounts, only the administrator account can disassociate a member account.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disassociate requesting account from administrator account
            The following example dissociates the requesting account from its associated administrator account.

            >>> await client.disassociate_from_administrator_account()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.disassociate_from_administrator_account_request.DisassociateFromAdministratorAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.disassociate_from_administrator_account_response.DisassociateFromAdministratorAccountResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.disassociate_from_administrator_account

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.disassociate_from_administrator_account.async_disassociate_from_administrator_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.disassociate_from_administrator_account_request.DisassociateFromAdministratorAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_from_master_account(
        self, *, config_overrides: Optional[AsyncSecurityHubClientConfig] = None
    ) -> "capo_securityhub.types.disassociate_from_master_account_response.DisassociateFromMasterAccountResponse":
        """<p>This method is deprecated. Instead, use <code>DisassociateFromAdministratorAccount</code>.</p> <p>The Security Hub CSPM console continues to use <code>DisassociateFromMasterAccount</code>. It will eventually change to use <code>DisassociateFromAdministratorAccount</code>. Any IAM policies that specifically control access to this function must continue to use <code>DisassociateFromMasterAccount</code>. You should also add <code>DisassociateFromAdministratorAccount</code> to your policies to ensure that the correct permissions are in place after the console begins to use <code>DisassociateFromAdministratorAccount</code>.</p> <p>Disassociates the current Security Hub CSPM member account from the associated administrator account.</p> <p>This operation is only used by accounts that are not part of an organization. For organization accounts, only the administrator account can disassociate a member account.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.disassociate_from_master_account_request.DisassociateFromMasterAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.disassociate_from_master_account_response.DisassociateFromMasterAccountResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.disassociate_from_master_account

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.disassociate_from_master_account.async_disassociate_from_master_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.disassociate_from_master_account_request.DisassociateFromMasterAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_members(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        account_ids: Optional[
            "capo_securityhub.types.account_id_list.AccountIdList"
        ] = None,
    ) -> "capo_securityhub.types.disassociate_members_response.DisassociateMembersResponse":
        """<p>Disassociates the specified member accounts from the associated administrator account.</p> <p>Can be used to disassociate both accounts that are managed using Organizations and accounts that were invited manually.</p>

        Args:
            account_ids: <p>The account IDs of the member accounts to disassociate from the administrator account.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disassociate member accounts from administrator account
            The following example dissociates the specified member accounts from the associated administrator account.

            >>> await client.disassociate_members(account_ids=['123456789012', '111122223333'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.disassociate_members_request.DisassociateMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.disassociate_members_response.DisassociateMembersResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.disassociate_members

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.disassociate_members.async_disassociate_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.disassociate_members_request.DisassociateMembersRequest = {}
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_import_findings_for_product(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        product_arn: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.enable_import_findings_for_product_response.EnableImportFindingsForProductResponse":
        """<p>Enables the integration of a partner product with Security Hub CSPM. Integrated products send findings to Security Hub CSPM.</p> <p>When you enable a product integration, a permissions policy that grants permission for the product to send findings to Security Hub CSPM is applied.</p>

        Args:
            product_arn: <p>The ARN of the product to enable the integration for.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To activate an integration
            The following example activates an integration between Security Hub and a third party partner product that sends findings to Security Hub.

            >>> await client.enable_import_findings_for_product(product_arn='arn:aws:securityhub:us-east-1:517716713836:product/crowdstrike/crowdstrike-falcon')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.enable_import_findings_for_product_request.EnableImportFindingsForProductRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.enable_import_findings_for_product_response.EnableImportFindingsForProductResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.enable_import_findings_for_product

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.enable_import_findings_for_product.async_enable_import_findings_for_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.enable_import_findings_for_product_request.EnableImportFindingsForProductRequest = {}
        if product_arn is not None:
            input_["product_arn"] = product_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_organization_admin_account(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        admin_account_id: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        feature: Optional[
            "capo_securityhub.types.security_hub_feature.SecurityHubFeature"
        ] = None,
    ) -> "capo_securityhub.types.enable_organization_admin_account_response.EnableOrganizationAdminAccountResponse":
        """<p>Designates the Security Hub CSPM administrator account for an organization. Can only be called by the organization management account.</p>

        Args:
            admin_account_id: <p>The Amazon Web Services account identifier of the account to designate as the Security Hub CSPM administrator account.</p>
            feature: <p>The feature for which the delegated admin account is enabled. Defaults to Security Hub CSPM if not specified.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To designate a Security Hub administrator
            The following example designates the specified account as the Security Hub administrator account. The requesting account must be the organization management account.

            >>> await client.enable_organization_admin_account(admin_account_id='123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.enable_organization_admin_account_response.EnableOrganizationAdminAccountResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.enable_organization_admin_account

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.enable_organization_admin_account.async_enable_organization_admin_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest = {}
        if admin_account_id is not None:
            input_["admin_account_id"] = admin_account_id
        if feature is not None:
            input_["feature"] = feature

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_security_hub(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        tags: Optional["capo_securityhub.types.tag_map.TagMap"] = None,
        enable_default_standards: Optional[
            "capo_securityhub.types.boolean.Boolean"
        ] = None,
        control_finding_generator: Optional[
            "capo_securityhub.types.control_finding_generator.ControlFindingGenerator"
        ] = None,
    ) -> (
        "capo_securityhub.types.enable_security_hub_response.EnableSecurityHubResponse"
    ):
        """<p>Enables Security Hub CSPM for your account in the current Region or the Region you specify in the request.</p> <p>When you enable Security Hub CSPM, you grant to Security Hub CSPM the permissions necessary to gather findings from other services that are integrated with Security Hub CSPM.</p> <p>When you use the <code>EnableSecurityHub</code> operation to enable Security Hub CSPM, you also automatically enable the following standards:</p> <ul> <li> <p>Center for Internet Security (CIS) Amazon Web Services Foundations Benchmark v1.2.0</p> </li> <li> <p>Amazon Web Services Foundational Security Best Practices</p> </li> </ul> <p>Other standards are not automatically enabled. </p> <p>To opt out of automatically enabled standards, set <code>EnableDefaultStandards</code> to <code>false</code>.</p> <p>After you enable Security Hub CSPM, to enable a standard, use the <code>BatchEnableStandards</code> operation. To disable a standard, use the <code>BatchDisableStandards</code> operation.</p> <p>To learn more, see the <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html">setup information</a> in the <i>Security Hub CSPM User Guide</i>.</p>

        Args:
            tags: <p>The tags to add to the hub resource when you enable Security Hub CSPM.</p>
            enable_default_standards: <p>Whether to enable the security standards that Security Hub CSPM has designated as automatically enabled. If you don't provide a value for <code>EnableDefaultStandards</code>, it is set to <code>true</code>. To not enable the automatically enabled standards, set <code>EnableDefaultStandards</code> to <code>false</code>.</p>
            control_finding_generator: <p>This field, used when enabling Security Hub CSPM, specifies whether the calling account has consolidated control findings turned on. If the value for this field is set to <code>SECURITY_CONTROL</code>, Security Hub CSPM generates a single finding for a control check even when the check applies to multiple enabled standards.</p> <p>If the value for this field is set to <code>STANDARD_CONTROL</code>, Security Hub CSPM generates separate findings for a control check when the check applies to multiple enabled standards.</p> <p>The value for this field in a member account matches the value in the administrator account. For accounts that aren't part of an organization, the default value of this field is <code>SECURITY_CONTROL</code> if you enabled Security Hub CSPM on or after February 23, 2023.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To activate Security Hub
            The following example activates the Security Hub service in the requesting AWS account. The service is activated in the current AWS Region or the Region that you specify in the request. Some standards are automatically turned on in your account unless you opt out. To determine which standards are automatically turned on, see the Security Hub documentation.

            >>> await client.enable_security_hub(tags={'Department': 'Security'}, enable_default_standards=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.enable_security_hub_request.EnableSecurityHubRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.enable_security_hub_response.EnableSecurityHubResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.enable_security_hub

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.enable_security_hub.async_enable_security_hub(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.enable_security_hub_request.EnableSecurityHubRequest = {}
        if tags is not None:
            input_["tags"] = tags
        if enable_default_standards is not None:
            input_["enable_default_standards"] = enable_default_standards
        if control_finding_generator is not None:
            input_["control_finding_generator"] = control_finding_generator

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_security_hub_feature_v2(
        self,
        feature_name: "capo_securityhub.types.feature_name.FeatureName",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.enable_security_hub_feature_v2_response.EnableSecurityHubFeatureV2Response":
        """<p>Enables an opt-in feature for the calling account in the current Amazon Web Services Region. The service must be enabled before you can enable a feature. The operation is idempotent. If the feature is already enabled, no changes are made. You cannot enable a feature that is managed by an organization policy.</p>

        Args:
            feature_name: <p>The name of the feature to enable.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.enable_security_hub_feature_v2_request.EnableSecurityHubFeatureV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.enable_security_hub_feature_v2_response.EnableSecurityHubFeatureV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.enable_security_hub_feature_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.enable_security_hub_feature_v2.async_enable_security_hub_feature_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.enable_security_hub_feature_v2_request.EnableSecurityHubFeatureV2Request = {
            "feature_name": feature_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_security_hub_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        tags: Optional["capo_securityhub.types.tag_map.TagMap"] = None,
    ) -> "capo_securityhub.types.enable_security_hub_v2_response.EnableSecurityHubV2Response":
        """<p>Enables the service in account for the current Amazon Web Services Region or specified Amazon Web Services Region.</p>

        Args:
            tags: <p>The tags to add to the hub V2 resource when you enable Security Hub.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.enable_security_hub_v2_request.EnableSecurityHubV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.enable_security_hub_v2_response.EnableSecurityHubV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.enable_security_hub_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.enable_security_hub_v2.async_enable_security_hub_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.enable_security_hub_v2_request.EnableSecurityHubV2Request = {}
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def generate_recommended_policy_v2(
        self,
        metadata_uid: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.generate_recommended_policy_v2_response.GenerateRecommendedPolicyV2Response":
        """<p>Begins the recommended policy generation to remediate a Security Hub finding. <code>GenerateRecommendedPolicyV2</code> only supports findings for unused permissions.</p>

        Args:
            metadata_uid: <p>The unique identifier (ID) of Security Hub OCSF findings found under the <code>metadata.uid</code> field of the finding.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.generate_recommended_policy_v2_request.GenerateRecommendedPolicyV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.generate_recommended_policy_v2_response.GenerateRecommendedPolicyV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.generate_recommended_policy_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.generate_recommended_policy_v2.async_generate_recommended_policy_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.generate_recommended_policy_v2_request.GenerateRecommendedPolicyV2Request = {
            "metadata_uid": metadata_uid
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_administrator_account(
        self, *, config_overrides: Optional[AsyncSecurityHubClientConfig] = None
    ) -> "capo_securityhub.types.get_administrator_account_response.GetAdministratorAccountResponse":
        """<p>Provides the details for the Security Hub CSPM administrator account for the current member account.</p> <p>Can be used by both member accounts that are managed using Organizations and accounts that were invited manually.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_administrator_account_request.GetAdministratorAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_administrator_account_response.GetAdministratorAccountResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_administrator_account

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_administrator_account.async_get_administrator_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_administrator_account_request.GetAdministratorAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_aggregator_v2(
        self,
        aggregator_v2_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.get_aggregator_v2_response.GetAggregatorV2Response":
        """<p>Returns the configuration of the specified Aggregator V2.</p>

        Args:
            aggregator_v2_arn: <p>The ARN of the Aggregator V2.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_aggregator_v2_request.GetAggregatorV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_aggregator_v2_response.GetAggregatorV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_aggregator_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_aggregator_v2.async_get_aggregator_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_aggregator_v2_request.GetAggregatorV2Request = {
            "aggregator_v2_arn": aggregator_v2_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automation_rule_v2(
        self,
        identifier: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.get_automation_rule_v2_response.GetAutomationRuleV2Response":
        """<p>Returns an automation rule for the V2 service.</p>

        Args:
            identifier: <p>The ARN of the V2 automation rule.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_automation_rule_v2_request.GetAutomationRuleV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_automation_rule_v2_response.GetAutomationRuleV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_automation_rule_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_automation_rule_v2.async_get_automation_rule_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_automation_rule_v2_request.GetAutomationRuleV2Request = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configuration_policy(
        self,
        identifier: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.get_configuration_policy_response.GetConfigurationPolicyResponse":
        """<p> Provides information about a configuration policy. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            identifier: <p> The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get details about a configuration policy
            This operation provides details about the specified configuration policy.

            >>> await client.get_configuration_policy(identifier='arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_configuration_policy_request.GetConfigurationPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_configuration_policy_response.GetConfigurationPolicyResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_configuration_policy

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_configuration_policy.async_get_configuration_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_configuration_policy_request.GetConfigurationPolicyRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configuration_policy_association(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        target: Optional["capo_securityhub.types.target.Target"] = None,
    ) -> "capo_securityhub.types.get_configuration_policy_association_response.GetConfigurationPolicyAssociationResponse":
        """<p> Returns the association between a configuration and a target account, organizational unit, or the root. The configuration can be a configuration policy or self-managed behavior. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            target: <p> The target account ID, organizational unit ID, or the root ID to retrieve the association for. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get details about a configuration association
            This operation provides details about configuration associations for a specific target account, organizational unit, or the root.

            >>> await client.get_configuration_policy_association(target={'AccountId': '111122223333'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_configuration_policy_association_request.GetConfigurationPolicyAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_configuration_policy_association_response.GetConfigurationPolicyAssociationResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_configuration_policy_association

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_configuration_policy_association.async_get_configuration_policy_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_configuration_policy_association_request.GetConfigurationPolicyAssociationRequest = {}
        if target is not None:
            input_["target"] = target

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connector(
        self,
        connector_id: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.get_connector_response.GetConnectorResponse":
        """<p>Retrieves details for a CSPM connector based on the connector ID.</p>

        Args:
            connector_id: <p>The unique identifier of the connector to retrieve.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get details of a CSPM connector
            This operation retrieves details for a CSPM connector.

            >>> await client.get_connector(connector_id='cspm-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_connector_request.GetConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_connector_response.GetConnectorResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_connector

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_connector.async_get_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_connector_request.GetConnectorRequest = {
            "connector_id": connector_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connector_v2(
        self,
        connector_id: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.get_connector_v2_response.GetConnectorV2Response":
        """<p>Grants permission to retrieve details for a connectorV2 based on connector id.</p>

        Args:
            connector_id: <p>The UUID of the connectorV2 to identify connectorV2 resource.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_connector_v2_request.GetConnectorV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_connector_v2_response.GetConnectorV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_connector_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_connector_v2.async_get_connector_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_connector_v2_request.GetConnectorV2Request = {
            "connector_id": connector_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_enabled_standards(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        standards_subscription_arns: Optional[
            "capo_securityhub.types.standards_subscription_arns.StandardsSubscriptionArns"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        providers: Optional[
            "capo_securityhub.types.standards_providers.StandardsProviders"
        ] = None,
    ) -> "capo_securityhub.types.get_enabled_standards_response.GetEnabledStandardsResponse":
        """<p>Returns a list of the standards that are currently enabled.</p>

        Args:
            standards_subscription_arns: <p>The list of the standards subscription ARNs for the standards to retrieve.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>GetEnabledStandards</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            providers: <p>A list of cloud providers to filter the enabled standards by. For example, specify <code>Azure</code> to return only enabled standards that evaluate Azure resources.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To return a list of enabled standards
            The following example returns a list of Security Hub standards that are currently enabled in your account.

            >>> await client.get_enabled_standards(standards_subscription_arns=['arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_enabled_standards_request.GetEnabledStandardsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_enabled_standards_response.GetEnabledStandardsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_enabled_standards

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_enabled_standards.async_get_enabled_standards(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_enabled_standards_request.GetEnabledStandardsRequest = {}
        if standards_subscription_arns is not None:
            input_["standards_subscription_arns"] = standards_subscription_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if providers is not None:
            input_["providers"] = providers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_enabled_standards(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        standards_subscription_arns: Optional[
            "capo_securityhub.types.standards_subscription_arns.StandardsSubscriptionArns"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        providers: Optional[
            "capo_securityhub.types.standards_providers.StandardsProviders"
        ] = None,
    ) -> "AsyncIterator[capo_securityhub.types.standards_subscription.StandardsSubscription]":
        _token = next_token
        while True:
            _response = await self.get_enabled_standards(
                config_overrides=config_overrides,
                standards_subscription_arns=standards_subscription_arns,
                next_token=_token,
                max_results=max_results,
                providers=providers,
            )
            _page = _resolve_path(_response, ("standards_subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_finding_aggregator(
        self,
        finding_aggregator_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.get_finding_aggregator_response.GetFindingAggregatorResponse":
        """<note> <p>The <i>aggregation Region</i> is now called the <i>home Region</i>.</p> </note> <p>Returns the current configuration in the calling account for cross-Region aggregation. A finding aggregator is a resource that establishes the home Region and any linked Regions.</p>

        Args:
            finding_aggregator_arn: <p>The ARN of the finding aggregator to return details for. To obtain the ARN, use <code>ListFindingAggregators</code>.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get cross-Region aggregation details
            The following example returns cross-Region aggregation details for the requesting account.

            >>> await client.get_finding_aggregator(finding_aggregator_arn='arn:aws:securityhub:us-east-1:123456789012:finding-aggregator/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_finding_aggregator_request.GetFindingAggregatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_finding_aggregator_response.GetFindingAggregatorResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_finding_aggregator

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_finding_aggregator.async_get_finding_aggregator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_finding_aggregator_request.GetFindingAggregatorRequest = {
            "finding_aggregator_arn": finding_aggregator_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_finding_history(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        finding_identifier: Optional[
            "capo_securityhub.types.aws_security_finding_identifier.AwsSecurityFindingIdentifier"
        ] = None,
        start_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_securityhub.types.get_finding_history_response.GetFindingHistoryResponse"
    ):
        """<p> Returns the history of a Security Hub CSPM finding. The history includes changes made to any fields in the Amazon Web Services Security Finding Format (ASFF) except top-level timestamp fields, such as the <code>CreatedAt</code> and <code>UpdatedAt</code> fields. </p> <p>This operation might return fewer results than the maximum number of results (<code>MaxResults</code>) specified in a request, even when more results are available. If this occurs, the response includes a <code>NextToken</code> value, which you should use to retrieve the next set of results in the response. The presence of a <code>NextToken</code> value in a response doesn't necessarily indicate that the results are incomplete. However, you should continue to specify a <code>NextToken</code> value until you receive a response that doesn't include this value.</p>

        Args:
            start_time: <p>A timestamp that indicates the start time of the requested finding history.</p> <p>If you provide values for both <code>StartTime</code> and <code>EndTime</code>, Security Hub CSPM returns finding history for the specified time period. If you provide a value for <code>StartTime</code> but not for <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>StartTime</code> to the time at which the API is called. If you provide a value for <code>EndTime</code> but not for <code>StartTime</code>, Security Hub CSPM returns finding history from the <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html#securityhub-Type-AwsSecurityFindingFilters-CreatedAt">CreatedAt</a> timestamp of the finding to the <code>EndTime</code>. If you provide neither <code>StartTime</code> nor <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>CreatedAt</code> timestamp of the finding to the time at which the API is called. In all of these scenarios, the response is limited to 100 results.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>
            end_time: <p> An ISO 8601-formatted timestamp that indicates the end time of the requested finding history.</p> <p>If you provide values for both <code>StartTime</code> and <code>EndTime</code>, Security Hub CSPM returns finding history for the specified time period. If you provide a value for <code>StartTime</code> but not for <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>StartTime</code> to the time at which the API is called. If you provide a value for <code>EndTime</code> but not for <code>StartTime</code>, Security Hub CSPM returns finding history from the <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html#securityhub-Type-AwsSecurityFindingFilters-CreatedAt">CreatedAt</a> timestamp of the finding to the <code>EndTime</code>. If you provide neither <code>StartTime</code> nor <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>CreatedAt</code> timestamp of the finding to the time at which the API is called. In all of these scenarios, the response is limited to 100 results.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>
            next_token: <p> A token for pagination purposes. Provide <code>NULL</code> as the initial value. In subsequent requests, provide the token included in the response to get up to an additional 100 results of finding history. If you don’t provide <code>NextToken</code>, Security Hub CSPM returns up to 100 results of finding history for each request. </p>
            max_results: <p> The maximum number of results to be returned. If you don’t provide it, Security Hub CSPM returns up to 100 results of finding history. </p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_finding_history_request.GetFindingHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_finding_history_response.GetFindingHistoryResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_finding_history

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_finding_history.async_get_finding_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_finding_history_request.GetFindingHistoryRequest = {}
        if finding_identifier is not None:
            input_["finding_identifier"] = finding_identifier
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
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

    async def iter_get_finding_history(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        finding_identifier: Optional[
            "capo_securityhub.types.aws_security_finding_identifier.AwsSecurityFindingIdentifier"
        ] = None,
        start_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.finding_history_record.FindingHistoryRecord]":
        _token = next_token
        while True:
            _response = await self.get_finding_history(
                config_overrides=config_overrides,
                finding_identifier=finding_identifier,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_findings(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        filters: Optional[
            "capo_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
        ] = None,
        sort_criteria: Optional[
            "capo_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.get_findings_response.GetFindingsResponse":
        """<p>Returns a list of findings that match the specified criteria.</p> <p>If cross-Region aggregation is enabled, then when you call <code>GetFindings</code> from the home Region, the results include all of the matching findings from both the home Region and linked Regions.</p>

        Args:
            filters: <p>The finding attributes used to define a condition to filter the returned findings.</p> <p>You can filter by up to 10 finding attributes. For each attribute, you can provide up to 20 filter values.</p> <p>Note that in the available filter fields, <code>WorkflowState</code> is deprecated. To search for a finding based on its workflow status, use <code>WorkflowStatus</code>.</p>
            sort_criteria: <p>The finding attributes used to sort the list of returned findings.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>GetFindings</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of findings to return.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of findings
            The following example returns a filtered and sorted list of Security Hub findings.

            >>> await client.get_findings(filters={'AwsAccountId': [{'Value': '123456789012', 'Comparison': 'PREFIX'}]}, max_results=1)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_findings_request.GetFindingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_findings_response.GetFindingsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_findings

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_findings.async_get_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_findings_request.GetFindingsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria
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

    async def iter_get_findings(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        filters: Optional[
            "capo_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
        ] = None,
        sort_criteria: Optional[
            "capo_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[capo_securityhub.types.aws_security_finding.AwsSecurityFinding]"
    ):
        _token = next_token
        while True:
            _response = await self.get_findings(
                config_overrides=config_overrides,
                filters=filters,
                sort_criteria=sort_criteria,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("findings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_finding_statistics_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        group_by_rules: Optional[
            "capo_securityhub.types.group_by_rules.GroupByRules"
        ] = None,
        scopes: Optional["capo_securityhub.types.finding_scopes.FindingScopes"] = None,
        sort_order: Optional["capo_securityhub.types.sort_order.SortOrder"] = None,
        max_statistic_results: Optional[
            "capo_securityhub.types.max_statistic_results.MaxStatisticResults"
        ] = None,
    ) -> "capo_securityhub.types.get_finding_statistics_v2_response.GetFindingStatisticsV2Response":
        """<p>Returns aggregated statistical data about findings.</p> <p>You can use the <code>Scopes</code> parameter to define the data boundary for the query. Currently, <code>Scopes</code> supports <code>AwsOrganizations</code>, which lets you aggregate findings from your entire organization or from specific organizational units. Only the delegated administrator account can use <code>Scopes</code>.</p> <p> <code>GetFindingStatisticsV2</code> uses <code>securityhub:GetAdhocInsightResults</code> in the <code>Action</code> element of an IAM policy statement. You must have permission to perform the <code>securityhub:GetAdhocInsightResults</code> action.</p>

        Args:
            group_by_rules: <p>Specifies how security findings should be aggregated and organized in the statistical analysis. It can accept up to 5 <code>groupBy</code> fields in a single call.</p>
            scopes: <p>Limits the results to findings from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees statistics from all accounts across the entire organization. Other accounts see only statistics for their own findings.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>
            sort_order: <p>Orders the aggregation count in descending or ascending order. Descending order is the default.</p>
            max_statistic_results: <p>The maximum number of results to be returned.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.organizational_unit_not_found_exception.OrganizationalUnitNotFoundException: <p>The request failed because one or more organizational units specified in the request don't exist within the caller's organization.</p>
            capo_securityhub.errors.organization_not_found_exception.OrganizationNotFoundException: <p>The request failed because one or more organizations specified in the request don't exist or don't belong to the caller's organization.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_finding_statistics_v2_request.GetFindingStatisticsV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_finding_statistics_v2_response.GetFindingStatisticsV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_finding_statistics_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_finding_statistics_v2.async_get_finding_statistics_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_finding_statistics_v2_request.GetFindingStatisticsV2Request = {}
        if group_by_rules is not None:
            input_["group_by_rules"] = group_by_rules
        if scopes is not None:
            input_["scopes"] = scopes
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_statistic_results is not None:
            input_["max_statistic_results"] = max_statistic_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_findings_trends_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        filters: Optional[
            "capo_securityhub.types.findings_trends_filters.FindingsTrendsFilters"
        ] = None,
        start_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.get_findings_trends_v2_response.GetFindingsTrendsV2Response":
        """<p>Returns findings trend data based on the specified criteria. This operation helps you analyze patterns and changes in findings over time.</p>

        Args:
            filters: <p>The filters to apply to the findings trend data.</p>
            start_time: <p>The starting timestamp for the time period to analyze findings trends, in ISO 8601 format.</p>
            end_time: <p>The ending timestamp for the time period to analyze findings trends, in ISO 8601 format.</p>
            next_token: <p>The token to use for paginating results. This value is returned in the response if more results are available.</p>
            max_results: <p>The maximum number of trend data points to return in a single response.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_findings_trends_v2_request.GetFindingsTrendsV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_findings_trends_v2_response.GetFindingsTrendsV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_findings_trends_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_findings_trends_v2.async_get_findings_trends_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_findings_trends_v2_request.GetFindingsTrendsV2Request = {}
        if filters is not None:
            input_["filters"] = filters
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
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

    async def iter_get_findings_trends_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        filters: Optional[
            "capo_securityhub.types.findings_trends_filters.FindingsTrendsFilters"
        ] = None,
        start_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.trends_metrics_result.TrendsMetricsResult]":
        _token = next_token
        while True:
            _response = await self.get_findings_trends_v2(
                config_overrides=config_overrides,
                filters=filters,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("trends_metrics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_findings_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        filters: Optional[
            "capo_securityhub.types.ocsf_finding_filters.OcsfFindingFilters"
        ] = None,
        scopes: Optional["capo_securityhub.types.finding_scopes.FindingScopes"] = None,
        sort_criteria: Optional[
            "capo_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.get_findings_v2_response.GetFindingsV2Response":
        """<p>Returns a list of findings that match the specified criteria.</p> <p>You can use the <code>Scopes</code> parameter to define the data boundary for the query. Currently, <code>Scopes</code> supports <code>AwsOrganizations</code>, which lets you retrieve findings from your entire organization or from specific organizational units. Only the delegated administrator account can use <code>Scopes</code>.</p> <p>You can use the <code>Filters</code> parameter to refine results based on finding attributes. You can use <code>Scopes</code> and <code>Filters</code> independently or together. When both are provided, <code>Scopes</code> narrows the data set first, and then <code>Filters</code> refines results within that scoped data set.</p> <p> <code>GetFindings</code> and <code>GetFindingsV2</code> both use <code>securityhub:GetFindings</code> in the <code>Action</code> element of an IAM policy statement. You must have permission to perform the <code>securityhub:GetFindings</code> action.</p>

        Args:
            filters: <p>The finding attributes used to define a condition to filter the returned OCSF findings. You can filter up to 10 composite filters. For each filter type inside of a composite filter, you can provide up to 20 filters.</p>
            scopes: <p>Limits the results to findings from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees findings from all accounts across the entire organization. Other accounts see only their own findings.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>
            sort_criteria: <p>The finding attributes used to sort the list of returned findings.</p>
            next_token: <p> The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.organizational_unit_not_found_exception.OrganizationalUnitNotFoundException: <p>The request failed because one or more organizational units specified in the request don't exist within the caller's organization.</p>
            capo_securityhub.errors.organization_not_found_exception.OrganizationNotFoundException: <p>The request failed because one or more organizations specified in the request don't exist or don't belong to the caller's organization.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_findings_v2_request.GetFindingsV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_findings_v2_response.GetFindingsV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_findings_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_findings_v2.async_get_findings_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_findings_v2_request.GetFindingsV2Request = {}
        if filters is not None:
            input_["filters"] = filters
        if scopes is not None:
            input_["scopes"] = scopes
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria
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

    async def iter_get_findings_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        filters: Optional[
            "capo_securityhub.types.ocsf_finding_filters.OcsfFindingFilters"
        ] = None,
        scopes: Optional["capo_securityhub.types.finding_scopes.FindingScopes"] = None,
        sort_criteria: Optional[
            "capo_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.ocsf_finding.OcsfFinding]":
        _token = next_token
        while True:
            _response = await self.get_findings_v2(
                config_overrides=config_overrides,
                filters=filters,
                scopes=scopes,
                sort_criteria=sort_criteria,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("findings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_insight_results(
        self,
        insight_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> (
        "capo_securityhub.types.get_insight_results_response.GetInsightResultsResponse"
    ):
        """<p>Lists the results of the Security Hub CSPM insight specified by the insight ARN.</p>

        Args:
            insight_arn: <p>The ARN of the insight for which to return results.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the results of a Security Hub insight
            The following example returns the results of the Security Hub insight specified by the insight ARN.

            >>> await client.get_insight_results(insight_arn='arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_insight_results_request.GetInsightResultsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_insight_results_response.GetInsightResultsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_insight_results

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_insight_results.async_get_insight_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_insight_results_request.GetInsightResultsRequest = {
            "insight_arn": insight_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_insights(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        insight_arns: Optional["capo_securityhub.types.arn_list.ArnList"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.get_insights_response.GetInsightsResponse":
        """<p>Lists and describes insights for the specified insight ARNs.</p>

        Args:
            insight_arns: <p>The ARNs of the insights to describe. If you don't provide any insight ARNs, then <code>GetInsights</code> returns all of your custom insights. It does not return any managed insights.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>GetInsights</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of items to return in the response.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get details of a Security Hub insight
            The following example returns details of the Security Hub insight with the specified ARN.

            >>> await client.get_insights(insight_arns=['arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_insights_request.GetInsightsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_insights_response.GetInsightsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_insights

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_insights.async_get_insights(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_insights_request.GetInsightsRequest = {}
        if insight_arns is not None:
            input_["insight_arns"] = insight_arns
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

    async def iter_get_insights(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        insight_arns: Optional["capo_securityhub.types.arn_list.ArnList"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.insight.Insight]":
        _token = next_token
        while True:
            _response = await self.get_insights(
                config_overrides=config_overrides,
                insight_arns=insight_arns,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("insights",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_invitations_count(
        self, *, config_overrides: Optional[AsyncSecurityHubClientConfig] = None
    ) -> "capo_securityhub.types.get_invitations_count_response.GetInvitationsCountResponse":
        """<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Returns the count of all Security Hub CSPM membership invitations that were sent to the calling member account, not including the currently accepted invitation. </p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a count of membership invitations
            The following example returns a count of invitations that the Security Hub administrator sent to the current member account, not including the currently accepted invitation.



            >>> await client.get_invitations_count()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_invitations_count_request.GetInvitationsCountRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_invitations_count_response.GetInvitationsCountResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_invitations_count

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_invitations_count.async_get_invitations_count(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_invitations_count_request.GetInvitationsCountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_master_account(
        self, *, config_overrides: Optional[AsyncSecurityHubClientConfig] = None
    ) -> "capo_securityhub.types.get_master_account_response.GetMasterAccountResponse":
        """<p>This method is deprecated. Instead, use <code>GetAdministratorAccount</code>.</p> <p>The Security Hub CSPM console continues to use <code>GetMasterAccount</code>. It will eventually change to use <code>GetAdministratorAccount</code>. Any IAM policies that specifically control access to this function must continue to use <code>GetMasterAccount</code>. You should also add <code>GetAdministratorAccount</code> to your policies to ensure that the correct permissions are in place after the console begins to use <code>GetAdministratorAccount</code>.</p> <p>Provides the details for the Security Hub CSPM administrator account for the current member account.</p> <p>Can be used by both member accounts that are managed using Organizations and accounts that were invited manually.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_master_account_request.GetMasterAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_master_account_response.GetMasterAccountResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_master_account

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_master_account.async_get_master_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_master_account_request.GetMasterAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_members(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        account_ids: Optional[
            "capo_securityhub.types.account_id_list.AccountIdList"
        ] = None,
    ) -> "capo_securityhub.types.get_members_response.GetMembersResponse":
        """<p>Returns the details for the Security Hub CSPM member accounts for the specified account IDs.</p> <p>An administrator account can be either the delegated Security Hub CSPM administrator account for an organization or an administrator account that enabled Security Hub CSPM manually.</p> <p>The results include both member accounts that are managed using Organizations and accounts that were invited manually.</p>

        Args:
            account_ids: <p>The list of account IDs for the Security Hub CSPM member accounts to return the details for. </p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_members_request.GetMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_members_response.GetMembersResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_members

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_members.async_get_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_members_request.GetMembersRequest = {}
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_recommended_policy_v2(
        self,
        metadata_uid: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.get_recommended_policy_v2_response.GetRecommendedPolicyV2Response":
        """<p>Retrieves the recommended policy to remediate a Security Hub finding. <code>GetRecommendedPolicyV2</code> only supports findings for unused permissions.</p>

        Args:
            metadata_uid: <p>The unique identifier (ID) of Security Hub OCSF findings found under the <code>metadata.uid</code> field of the finding.</p>
            next_token: <p>The token used to paginate the <code>RecommendationSteps</code> list returned. On your first call to <code>GetRecommendedPolicyV2</code>, omit this parameter or set it to <code>NULL</code>. For subsequent calls, use the <code>NextToken</code> value returned in the previous response to retrieve the next page of results.</p>
            max_results: <p>The maximum number of recommendation steps to return.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_recommended_policy_v2_request.GetRecommendedPolicyV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_recommended_policy_v2_response.GetRecommendedPolicyV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_recommended_policy_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_recommended_policy_v2.async_get_recommended_policy_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_recommended_policy_v2_request.GetRecommendedPolicyV2Request = {
            "metadata_uid": metadata_uid
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

    async def iter_get_recommended_policy_v2(
        self,
        metadata_uid: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.recommendation_step.RecommendationStep]":
        _token = next_token
        while True:
            _response = await self.get_recommended_policy_v2(
                metadata_uid,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("recommendation_steps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_resources_statistics_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        group_by_rules: Optional[
            "capo_securityhub.types.resource_group_by_rules.ResourceGroupByRules"
        ] = None,
        scopes: Optional[
            "capo_securityhub.types.resource_scopes.ResourceScopes"
        ] = None,
        sort_order: Optional["capo_securityhub.types.sort_order.SortOrder"] = None,
        max_statistic_results: Optional[
            "capo_securityhub.types.max_statistic_results.MaxStatisticResults"
        ] = None,
    ) -> "capo_securityhub.types.get_resources_statistics_v2_response.GetResourcesStatisticsV2Response":
        """<p>Retrieves statistical information about Amazon Web Services resources and their associated security findings.</p> <p>You can use the <code>Scopes</code> parameter to define the data boundary for the query. Currently, <code>Scopes</code> supports <code>AwsOrganizations</code>, which lets you aggregate resources from your entire organization or from specific organizational units. Only the delegated administrator account can use <code>Scopes</code>.</p> <p>If you set <code>GroupByField</code> to <code>ResourceSubCategory</code>, <code>ResourceInfo.AIDetails.HostResourceType</code>, or <code>ResourceInfo.AIDetails.CanonicalId</code>, you must include a <code>ResourceCategory</code> string filter with comparison set to <code>EQUALS</code> and value <code>AI/ML</code> in the corresponding <code>ResourceGroupByRule</code>.</p>

        Args:
            group_by_rules: <p>How resource statistics should be aggregated and organized in the response.</p>
            scopes: <p>Limits the results to resources from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees statistics from all accounts across the entire organization. Other accounts see only statistics for their own resources.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>
            sort_order: <p>Sorts aggregated statistics.</p>
            max_statistic_results: <p>The maximum number of results to be returned.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.organizational_unit_not_found_exception.OrganizationalUnitNotFoundException: <p>The request failed because one or more organizational units specified in the request don't exist within the caller's organization.</p>
            capo_securityhub.errors.organization_not_found_exception.OrganizationNotFoundException: <p>The request failed because one or more organizations specified in the request don't exist or don't belong to the caller's organization.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_resources_statistics_v2_request.GetResourcesStatisticsV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_resources_statistics_v2_response.GetResourcesStatisticsV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_resources_statistics_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_resources_statistics_v2.async_get_resources_statistics_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_resources_statistics_v2_request.GetResourcesStatisticsV2Request = {}
        if group_by_rules is not None:
            input_["group_by_rules"] = group_by_rules
        if scopes is not None:
            input_["scopes"] = scopes
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_statistic_results is not None:
            input_["max_statistic_results"] = max_statistic_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resources_trends_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        filters: Optional[
            "capo_securityhub.types.resources_trends_filters.ResourcesTrendsFilters"
        ] = None,
        start_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.get_resources_trends_v2_response.GetResourcesTrendsV2Response":
        """<p>Returns resource trend data based on the specified criteria. This operation helps you analyze patterns and changes in resource compliance over time.</p>

        Args:
            filters: <p>The filters to apply to the resources trend data.</p>
            start_time: <p>The starting timestamp for the time period to analyze resources trends, in ISO 8601 format.</p>
            end_time: <p>The ending timestamp for the time period to analyze resources trends, in ISO 8601 format.</p>
            next_token: <p>The token to use for paginating results. This value is returned in the response if more results are available.</p>
            max_results: <p>The maximum number of trend data points to return in a single response.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_resources_trends_v2_request.GetResourcesTrendsV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_resources_trends_v2_response.GetResourcesTrendsV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_resources_trends_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_resources_trends_v2.async_get_resources_trends_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_resources_trends_v2_request.GetResourcesTrendsV2Request = {}
        if filters is not None:
            input_["filters"] = filters
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
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

    async def iter_get_resources_trends_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        filters: Optional[
            "capo_securityhub.types.resources_trends_filters.ResourcesTrendsFilters"
        ] = None,
        start_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_securityhub.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.resources_trends_metrics_result.ResourcesTrendsMetricsResult]":
        _token = next_token
        while True:
            _response = await self.get_resources_trends_v2(
                config_overrides=config_overrides,
                filters=filters,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("trends_metrics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_resources_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        filters: Optional[
            "capo_securityhub.types.resources_filters.ResourcesFilters"
        ] = None,
        scopes: Optional[
            "capo_securityhub.types.resource_scopes.ResourceScopes"
        ] = None,
        sort_criteria: Optional[
            "capo_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.get_resources_v2_response.GetResourcesV2Response":
        """<p>Returns a list of resources.</p> <p>You can use the <code>Scopes</code> parameter to define the data boundary for the query. Currently, <code>Scopes</code> supports <code>AwsOrganizations</code>, which lets you retrieve resources from your entire organization or from specific organizational units. Only the delegated administrator account can use <code>Scopes</code>.</p> <p>You can use the <code>Filters</code> parameter to refine results based on resource attributes. You can use <code>Scopes</code> and <code>Filters</code> independently or together. When both are provided, <code>Scopes</code> narrows the data set first, and then <code>Filters</code> refines results within that scoped data set.</p> <p>For AI/ML resources, the response includes the <code>ResourceSubCategory</code> field. For self-hosted AI resources and their host resources, the response also includes <code>ResourceInfo</code> with AI-specific details. Self-hosted AI resources use a <code>ResourceType</code> with the <code>SelfHosted::AI::</code> prefix, such as <code>SelfHosted::AI::Model</code>, <code>SelfHosted::AI::Agent</code>, <code>SelfHosted::AI::InferenceEndpoint</code>, and <code>SelfHosted::AI::ExternalEndpoint</code>.</p> <p>If you filter by <code>ResourceSubCategory</code>, you must also include a <code>ResourceCategory</code> string filter with comparison set to <code>EQUALS</code> and value <code>AI/ML</code> in the same request.</p>

        Args:
            filters: <p>Filters resources based on a set of criteria.</p>
            scopes: <p>Limits the results to resources from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees resources from all accounts across the entire organization. Other accounts see only their own resources.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>
            sort_criteria: <p>The resource attributes used to sort the list of returned resources.</p>
            next_token: <p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.organizational_unit_not_found_exception.OrganizationalUnitNotFoundException: <p>The request failed because one or more organizational units specified in the request don't exist within the caller's organization.</p>
            capo_securityhub.errors.organization_not_found_exception.OrganizationNotFoundException: <p>The request failed because one or more organizations specified in the request don't exist or don't belong to the caller's organization.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_resources_v2_request.GetResourcesV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_resources_v2_response.GetResourcesV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_resources_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_resources_v2.async_get_resources_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_resources_v2_request.GetResourcesV2Request = {}
        if filters is not None:
            input_["filters"] = filters
        if scopes is not None:
            input_["scopes"] = scopes
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria
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

    async def iter_get_resources_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        filters: Optional[
            "capo_securityhub.types.resources_filters.ResourcesFilters"
        ] = None,
        scopes: Optional[
            "capo_securityhub.types.resource_scopes.ResourceScopes"
        ] = None,
        sort_criteria: Optional[
            "capo_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.resource_result.ResourceResult]":
        _token = next_token
        while True:
            _response = await self.get_resources_v2(
                config_overrides=config_overrides,
                filters=filters,
                scopes=scopes,
                sort_criteria=sort_criteria,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_security_control_definition(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        security_control_id: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.get_security_control_definition_response.GetSecurityControlDefinitionResponse":
        """<p> Retrieves the definition of a security control. The definition includes the control title, description, Region availability, parameter definitions, and other details. </p>

        Args:
            security_control_id: <p> The ID of the security control to retrieve the definition for. This field doesn’t accept an Amazon Resource Name (ARN). </p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the definition of a security control.
            The following example retrieves definition details for the specified security control.

            >>> await client.get_security_control_definition(security_control_id='EC2.4')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.get_security_control_definition_request.GetSecurityControlDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.get_security_control_definition_response.GetSecurityControlDefinitionResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.get_security_control_definition

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.get_security_control_definition.async_get_security_control_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.get_security_control_definition_request.GetSecurityControlDefinitionRequest = {}
        if security_control_id is not None:
            input_["security_control_id"] = security_control_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def invite_members(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        account_ids: Optional[
            "capo_securityhub.types.account_id_list.AccountIdList"
        ] = None,
    ) -> "capo_securityhub.types.invite_members_response.InviteMembersResponse":
        """<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Invites other Amazon Web Services accounts to become member accounts for the Security Hub CSPM administrator account that the invitation is sent from.</p> <p>This operation is only used to invite accounts that don't belong to an Amazon Web Services organization. Organization accounts don't receive invitations.</p> <p>Before you can use this action to invite a member, you must first use the <code>CreateMembers</code> action to create the member account in Security Hub CSPM.</p> <p>When the account owner enables Security Hub CSPM and accepts the invitation to become a member account, the administrator account can view the findings generated in the member account.</p>

        Args:
            account_ids: <p>The list of account IDs of the Amazon Web Services accounts to invite to Security Hub CSPM as members. </p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To invite accounts to become members
            The following example invites the specified AWS accounts to become member accounts associated with the calling Security Hub administrator account. You only use this operation to invite accounts that don't belong to an AWS Organizations organization.

            >>> await client.invite_members(account_ids=['111122223333', '444455556666'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.invite_members_request.InviteMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.invite_members_response.InviteMembersResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.invite_members

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.invite_members.async_invite_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.invite_members_request.InviteMembersRequest = {}
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_aggregators_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_securityhub.types.list_aggregators_v2_response.ListAggregatorsV2Response"
    ):
        """<p>Retrieves a list of V2 aggregators.</p>

        Args:
            next_token: <p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_aggregators_v2_request.ListAggregatorsV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_aggregators_v2_response.ListAggregatorsV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_aggregators_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_aggregators_v2.async_list_aggregators_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_aggregators_v2_request.ListAggregatorsV2Request = {}
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

    async def iter_list_aggregators_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.aggregator_v2.AggregatorV2]":
        _token = next_token
        while True:
            _response = await self.list_aggregators_v2(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("aggregators_v2",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_automation_rules(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.list_automation_rules_response.ListAutomationRulesResponse":
        """<p> A list of automation rules and their metadata for the calling account. </p>

        Args:
            next_token: <p> A token to specify where to start paginating the response. This is the <code>NextToken</code> from a previously truncated response. On your first call to the <code>ListAutomationRules</code> API, set the value of this parameter to <code>NULL</code>. </p>
            max_results: <p> The maximum number of rules to return in the response. This currently ranges from 1 to 100. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list automation rules
            The following example lists automation rules and rule metadata in the calling account.

            >>> await client.list_automation_rules(next_token='example-token', max_results=2)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_automation_rules_request.ListAutomationRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_automation_rules_response.ListAutomationRulesResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_automation_rules

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_automation_rules.async_list_automation_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_automation_rules_request.ListAutomationRulesRequest = {}
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

    async def list_automation_rules_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.list_automation_rules_v2_response.ListAutomationRulesV2Response":
        """<p>Returns a list of automation rules and metadata for the calling account.</p>

        Args:
            next_token: <p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_automation_rules_v2_request.ListAutomationRulesV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_automation_rules_v2_response.ListAutomationRulesV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_automation_rules_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_automation_rules_v2.async_list_automation_rules_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_automation_rules_v2_request.ListAutomationRulesV2Request = {}
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

    async def list_configuration_policies(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.list_configuration_policies_response.ListConfigurationPoliciesResponse":
        """<p> Lists the configuration policies that the Security Hub CSPM delegated administrator has created for your organization. Only the delegated administrator can invoke this operation from the home Region. </p>

        Args:
            next_token: <p> The NextToken value that's returned from a previous paginated <code>ListConfigurationPolicies</code> request where <code>MaxResults</code> was used but the results exceeded the value of that parameter. Pagination continues from the <code>MaxResults</code> was used but the results exceeded the value of that parameter. Pagination continues from the end of the previous response that returned the <code>NextToken</code> value. This value is <code>null</code> when there are no more results to return. </p>
            max_results: <p> The maximum number of results that's returned by <code>ListConfigurationPolicies</code> in each page of the response. When this parameter is used, <code>ListConfigurationPolicies</code> returns the specified number of results in a single page and a <code>NextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListConfigurationPolicies</code> request with the returned <code>NextToken</code> value. A valid range for <code>MaxResults</code> is between 1 and 100. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view a list of configuration policies
            This operation provides a list of your configuration policies, including metadata for each policy.

            >>> await client.list_configuration_policies(next_token='U1FsdGVkX19nBV2zoh+Gou9NgnulLJHWpn9xnG4hqSOhvw3o2JqjI86QDxdf', max_results=1)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_configuration_policies_request.ListConfigurationPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_configuration_policies_response.ListConfigurationPoliciesResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_configuration_policies

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_configuration_policies.async_list_configuration_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_configuration_policies_request.ListConfigurationPoliciesRequest = {}
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

    async def iter_list_configuration_policies(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.configuration_policy_summary.ConfigurationPolicySummary]":
        _token = next_token
        while True:
            _response = await self.list_configuration_policies(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("configuration_policy_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_configuration_policy_associations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        filters: Optional[
            "capo_securityhub.types.association_filters.AssociationFilters"
        ] = None,
    ) -> "capo_securityhub.types.list_configuration_policy_associations_response.ListConfigurationPolicyAssociationsResponse":
        """<p> Provides information about the associations for your configuration policies and self-managed behavior. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            next_token: <p> The <code>NextToken</code> value that's returned from a previous paginated <code>ListConfigurationPolicyAssociations</code> request where <code>MaxResults</code> was used but the results exceeded the value of that parameter. Pagination continues from the end of the previous response that returned the <code>NextToken</code> value. This value is <code>null</code> when there are no more results to return. </p>
            max_results: <p> The maximum number of results that's returned by <code>ListConfigurationPolicies</code> in each page of the response. When this parameter is used, <code>ListConfigurationPolicyAssociations</code> returns the specified number of results in a single page and a <code>NextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListConfigurationPolicyAssociations</code> request with the returned <code>NextToken</code> value. A valid range for <code>MaxResults</code> is between 1 and 100. </p>
            filters: <p> Options for filtering the <code>ListConfigurationPolicyAssociations</code> response. You can filter by the Amazon Resource Name (ARN) or universally unique identifier (UUID) of a configuration, <code>AssociationType</code>, or <code>AssociationStatus</code>. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list configuration associations
            This operation lists all of the associations between targets and configuration policies or self-managed behavior. Targets can include accounts, organizational units, or the root.

            >>> await client.list_configuration_policy_associations(next_token='U1FsdGVkX19nBV2zoh+Gou9NgnulLJHWpn9xnG4hqSOhvw3o2JqjI86QDxdf', max_results=1, filters={'AssociationType': 'APPLIED'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_configuration_policy_associations_request.ListConfigurationPolicyAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_configuration_policy_associations_response.ListConfigurationPolicyAssociationsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_configuration_policy_associations

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_configuration_policy_associations.async_list_configuration_policy_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_configuration_policy_associations_request.ListConfigurationPolicyAssociationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_configuration_policy_associations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        filters: Optional[
            "capo_securityhub.types.association_filters.AssociationFilters"
        ] = None,
    ) -> "AsyncIterator[capo_securityhub.types.configuration_policy_association_summary.ConfigurationPolicyAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_configuration_policy_associations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(
                _response, ("configuration_policy_association_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_connectors(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        provider_name: Optional[
            "capo_securityhub.types.cspm_connector_provider_name.CspmConnectorProviderName"
        ] = None,
        connector_status: Optional[
            "capo_securityhub.types.cspm_connector_status.CspmConnectorStatus"
        ] = None,
        enablement_status: Optional[
            "capo_securityhub.types.cspm_enablement_status.CspmEnablementStatus"
        ] = None,
    ) -> "capo_securityhub.types.list_connectors_response.ListConnectorsResponse":
        """<p>Lists the CSPM connectors and their metadata for the calling account.</p>

        Args:
            next_token: <p>The pagination token to request the next page of results.</p>
            max_results: <p>The maximum number of results to return.</p>
            provider_name: <p>The name of the cloud provider to filter connectors by.</p>
            connector_status: <p>The connectivity status to filter connectors by.</p>
            enablement_status: <p>The enablement status to filter connectors by.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list CSPM connectors
            This operation lists the CSPM connectors for the calling account.

            >>> await client.list_connectors(max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_connectors_request.ListConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_connectors

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_connectors.async_list_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_connectors_request.ListConnectorsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if connector_status is not None:
            input_["connector_status"] = connector_status
        if enablement_status is not None:
            input_["enablement_status"] = enablement_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_connectors_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        provider_name: Optional[
            "capo_securityhub.types.connector_provider_name.ConnectorProviderName"
        ] = None,
        connector_status: Optional[
            "capo_securityhub.types.connector_status.ConnectorStatus"
        ] = None,
        enablement_status: Optional[
            "capo_securityhub.types.enablement_status.EnablementStatus"
        ] = None,
    ) -> "capo_securityhub.types.list_connectors_v2_response.ListConnectorsV2Response":
        """<p>Grants permission to retrieve a list of connectorsV2 and their metadata for the calling account.</p>

        Args:
            next_token: <p>The pagination token per the Amazon Web Services Pagination standard</p>
            max_results: <p>The maximum number of results to be returned.</p>
            provider_name: <p>The name of the third-party provider.</p>
            connector_status: <p>The status for the connectorV2.</p>
            enablement_status: <p>The enablement status to filter connectors by.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_connectors_v2_request.ListConnectorsV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_connectors_v2_response.ListConnectorsV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_connectors_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_connectors_v2.async_list_connectors_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_connectors_v2_request.ListConnectorsV2Request = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if connector_status is not None:
            input_["connector_status"] = connector_status
        if enablement_status is not None:
            input_["enablement_status"] = enablement_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_enabled_products_for_import(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.list_enabled_products_for_import_response.ListEnabledProductsForImportResponse":
        """<p>Lists all findings-generating solutions (products) that you are subscribed to receive findings from in Security Hub CSPM.</p>

        Args:
            next_token: <p>The token that is required for pagination. On your first call to the <code>ListEnabledProductsForImport</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of items to return in the response.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list ARNs for enabled integrations
            The following example returns a list of subscription Amazon Resource Names (ARNs) for the product integrations that you have currently enabled in Security Hub.

            >>> await client.list_enabled_products_for_import()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_enabled_products_for_import_request.ListEnabledProductsForImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_enabled_products_for_import_response.ListEnabledProductsForImportResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_enabled_products_for_import

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_enabled_products_for_import.async_list_enabled_products_for_import(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_enabled_products_for_import_request.ListEnabledProductsForImportRequest = {}
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

    async def iter_list_enabled_products_for_import(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_enabled_products_for_import(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("product_subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_finding_aggregators(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.list_finding_aggregators_response.ListFindingAggregatorsResponse":
        """<p>If cross-Region aggregation is enabled, then <code>ListFindingAggregators</code> returns the Amazon Resource Name (ARN) of the finding aggregator. You can run this operation from any Amazon Web Services Region.</p>

        Args:
            next_token: <p>The token returned with the previous set of results. Identifies the next set of results to return.</p>
            max_results: <p>The maximum number of results to return. This operation currently only returns a single result.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update the enablement status of a standard control
            The following example disables the specified control in the specified security standard.

            >>> await client.list_finding_aggregators()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_finding_aggregators_request.ListFindingAggregatorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_finding_aggregators_response.ListFindingAggregatorsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_finding_aggregators

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_finding_aggregators.async_list_finding_aggregators(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_finding_aggregators_request.ListFindingAggregatorsRequest = {}
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

    async def iter_list_finding_aggregators(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.finding_aggregator.FindingAggregator]":
        _token = next_token
        while True:
            _response = await self.list_finding_aggregators(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("finding_aggregators",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_free_trial_statuses_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        account_ids: Optional[
            "capo_securityhub.types.free_trial_account_id_list.FreeTrialAccountIdList"
        ] = None,
        statuses: Optional[
            "capo_securityhub.types.free_trial_status_value_list.FreeTrialStatusValueList"
        ] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
    ) -> "capo_securityhub.types.list_free_trial_statuses_v2_response.ListFreeTrialStatusesV2Response":
        """<p>Lists the free trial status of Security Hub features. A delegated Security Hub administrator can list the status for accounts in its organization. Any other account can list the status only for itself. Free trial status remains available after a feature is disabled.</p>

        Args:
            account_ids: <p>The Amazon Web Services account identifiers to list free trial status for. You can specify accounts other than your own only if you are a delegated Security Hub administrator.</p>
            statuses: <p>The free trial statuses to filter the results by. Valid values:</p> <ul> <li> <p> <code>ACTIVE</code> returns only features with an ongoing free trial period.</p> </li> <li> <p> <code>INACTIVE</code> returns only features whose free trial period has ended, or that never started.</p> </li> </ul>
            max_results: <p>The maximum number of results to return. If you don't specify a value, Security Hub returns up to 100 results.</p>
            next_token: <p>The pagination token to request the next page of results.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_free_trial_statuses_v2_request.ListFreeTrialStatusesV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_free_trial_statuses_v2_response.ListFreeTrialStatusesV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_free_trial_statuses_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_free_trial_statuses_v2.async_list_free_trial_statuses_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_free_trial_statuses_v2_request.ListFreeTrialStatusesV2Request = {}
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if statuses is not None:
            input_["statuses"] = statuses
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_free_trial_statuses_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        account_ids: Optional[
            "capo_securityhub.types.free_trial_account_id_list.FreeTrialAccountIdList"
        ] = None,
        statuses: Optional[
            "capo_securityhub.types.free_trial_status_value_list.FreeTrialStatusValueList"
        ] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.account_free_trial_status.AccountFreeTrialStatus]":
        _token = next_token
        while True:
            _response = await self.list_free_trial_statuses_v2(
                config_overrides=config_overrides,
                account_ids=account_ids,
                statuses=statuses,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("account_free_trial_statuses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_invitations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        max_results: Optional[
            "capo_securityhub.types.cross_account_max_results.CrossAccountMaxResults"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
    ) -> "capo_securityhub.types.list_invitations_response.ListInvitationsResponse":
        """<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Lists all Security Hub CSPM membership invitations that were sent to the calling account.</p> <p>Only accounts that are managed by invitation can use this operation. Accounts that are managed using the integration with Organizations don't receive invitations.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. </p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>ListInvitations</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_invitations_request.ListInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_invitations_response.ListInvitationsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_invitations

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_invitations.async_list_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_invitations_request.ListInvitationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_invitations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        max_results: Optional[
            "capo_securityhub.types.cross_account_max_results.CrossAccountMaxResults"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.invitation.Invitation]":
        _token = next_token
        while True:
            _response = await self.list_invitations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("invitations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_members(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        only_associated: Optional["capo_securityhub.types.boolean.Boolean"] = None,
        max_results: Optional[
            "capo_securityhub.types.cross_account_max_results.CrossAccountMaxResults"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
    ) -> "capo_securityhub.types.list_members_response.ListMembersResponse":
        """<p>Lists details about all member accounts for the current Security Hub CSPM administrator account.</p> <p>The results include both member accounts that belong to an organization and member accounts that were invited manually.</p>

        Args:
            only_associated: <p>Specifies which member accounts to include in the response based on their relationship status with the administrator account. The default value is <code>TRUE</code>.</p> <p>If <code>OnlyAssociated</code> is set to <code>TRUE</code>, the response includes member accounts whose relationship status with the administrator account is set to <code>ENABLED</code>.</p> <p>If <code>OnlyAssociated</code> is set to <code>FALSE</code>, the response includes all existing member accounts. </p>
            max_results: <p>The maximum number of items to return in the response. </p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>ListMembers</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_members_request.ListMembersRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_members_response.ListMembersResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_members

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_members.async_list_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_members_request.ListMembersRequest = {}
        if only_associated is not None:
            input_["only_associated"] = only_associated
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_members(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        only_associated: Optional["capo_securityhub.types.boolean.Boolean"] = None,
        max_results: Optional[
            "capo_securityhub.types.cross_account_max_results.CrossAccountMaxResults"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.member.Member]":
        _token = next_token
        while True:
            _response = await self.list_members(
                config_overrides=config_overrides,
                only_associated=only_associated,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("members",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_organization_admin_accounts(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        max_results: Optional[
            "capo_securityhub.types.admins_max_results.AdminsMaxResults"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        feature: Optional[
            "capo_securityhub.types.security_hub_feature.SecurityHubFeature"
        ] = None,
    ) -> "capo_securityhub.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse":
        """<p>Lists the Security Hub CSPM administrator accounts. Can only be called by the organization management account.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>ListOrganizationAdminAccounts</code> operation, set the value of this parameter to <code>NULL</code>. For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response. </p>
            feature: <p>The feature where the delegated administrator account is listed. Defaults to Security Hub CSPM if not specified.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list administrator acccounts for an organization
            The following example lists the Security  Hub administrator accounts for an organization. Only the organization management account can call this operation.

            >>> await client.list_organization_admin_accounts()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_organization_admin_accounts

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_organization_admin_accounts.async_list_organization_admin_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if feature is not None:
            input_["feature"] = feature

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_organization_admin_accounts(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        max_results: Optional[
            "capo_securityhub.types.admins_max_results.AdminsMaxResults"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        feature: Optional[
            "capo_securityhub.types.security_hub_feature.SecurityHubFeature"
        ] = None,
    ) -> "AsyncIterator[capo_securityhub.types.admin_account.AdminAccount]":
        _token = next_token
        while True:
            _response = await self.list_organization_admin_accounts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                feature=feature,
            )
            _page = _resolve_path(_response, ("admin_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_security_control_definitions(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        standards_arn: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        providers: Optional[
            "capo_securityhub.types.security_controls_providers.SecurityControlsProviders"
        ] = None,
    ) -> "capo_securityhub.types.list_security_control_definitions_response.ListSecurityControlDefinitionsResponse":
        """<p> Lists all of the security controls that apply to a specified standard. </p>

        Args:
            standards_arn: <p> The Amazon Resource Name (ARN) of the standard that you want to view controls for. </p>
            next_token: <p> Optional pagination parameter. </p>
            max_results: <p> An optional parameter that limits the total results of the API response to the specified number. If this parameter isn't provided in the request, the results include the first 25 security controls that apply to the specified standard. The results also include a <code>NextToken</code> parameter that you can use in a subsequent API call to get the next 25 controls. This repeats until all controls for the standard are returned. </p>
            providers: <p>A list of cloud providers to filter the security control definitions by. For example, specify <code>Azure</code> to return only controls that evaluate Azure resources.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list Azure security control definitions
            The following example lists security control definitions for a specified provider.

            >>> await client.list_security_control_definitions(providers=['Azure'], max_results=3)
            To list security controls that apply to a standard
            The following example lists security controls that apply to a specified Security Hub standard.

            >>> await client.list_security_control_definitions(standards_arn='arn:aws:securityhub:::standards/aws-foundational-security-best-practices/v/1.0.0', next_token='NULL', max_results=3)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_security_control_definitions_request.ListSecurityControlDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_security_control_definitions_response.ListSecurityControlDefinitionsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_security_control_definitions

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_security_control_definitions.async_list_security_control_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_security_control_definitions_request.ListSecurityControlDefinitionsRequest = {}
        if standards_arn is not None:
            input_["standards_arn"] = standards_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if providers is not None:
            input_["providers"] = providers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_security_control_definitions(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        standards_arn: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
        providers: Optional[
            "capo_securityhub.types.security_controls_providers.SecurityControlsProviders"
        ] = None,
    ) -> "AsyncIterator[capo_securityhub.types.security_control_definition.SecurityControlDefinition]":
        _token = next_token
        while True:
            _response = await self.list_security_control_definitions(
                config_overrides=config_overrides,
                standards_arn=standards_arn,
                next_token=_token,
                max_results=max_results,
                providers=providers,
            )
            _page = _resolve_path(_response, ("security_control_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_standards_control_associations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        security_control_id: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "capo_securityhub.types.list_standards_control_associations_response.ListStandardsControlAssociationsResponse":
        """<p> Specifies whether a control is currently enabled or disabled in each enabled standard in the calling account. </p> <p>This operation omits standards control associations for standard subscriptions where <code>StandardsControlsUpdatable</code> has value <code>NOT_READY_FOR_UPDATES</code>.</p>

        Args:
            security_control_id: <p> The identifier of the control (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) that you want to determine the enablement status of in each enabled standard. </p>
            next_token: <p> Optional pagination parameter. </p>
            max_results: <p> An optional parameter that limits the total results of the API response to the specified number. If this parameter isn't provided in the request, the results include the first 25 standard and control associations. The results also include a <code>NextToken</code> parameter that you can use in a subsequent API call to get the next 25 associations. This repeats until all associations for the specified control are returned. The number of results is limited by the number of supported Security Hub CSPM standards that you've enabled in the calling account. </p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_standards_control_associations_request.ListStandardsControlAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_standards_control_associations_response.ListStandardsControlAssociationsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_standards_control_associations

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_standards_control_associations.async_list_standards_control_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_standards_control_associations_request.ListStandardsControlAssociationsRequest = {}
        if security_control_id is not None:
            input_["security_control_id"] = security_control_id
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

    async def iter_list_standards_control_associations(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        security_control_id: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        next_token: Optional["capo_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityhub.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_securityhub.types.standards_control_association_summary.StandardsControlAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_standards_control_associations(
                config_overrides=config_overrides,
                security_control_id=security_control_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("standards_control_association_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_securityhub.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
    ) -> "capo_securityhub.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags associated with a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to retrieve tags for.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of tags for a resource
            The following example returns a list of tags associated with the specified resource.

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:securityhub:us-west-1:123456789012:hub/default')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_connector_v2(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        auth_code: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        auth_state: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.register_connector_v2_response.RegisterConnectorV2Response":
        """<p>Grants permission to complete the authorization based on input parameters.</p>

        Args:
            auth_code: <p>The authCode retrieved from authUrl to complete the OAuth 2.0 authorization code flow.</p>
            auth_state: <p>The authState retrieved from authUrl to complete the OAuth 2.0 authorization code flow.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.register_connector_v2_request.RegisterConnectorV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.register_connector_v2_response.RegisterConnectorV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.register_connector_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.register_connector_v2.async_register_connector_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.register_connector_v2_request.RegisterConnectorV2Request = {}
        if auth_code is not None:
            input_["auth_code"] = auth_code
        if auth_state is not None:
            input_["auth_state"] = auth_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_configuration_policy_association(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        configuration_policy_identifier: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        target: Optional["capo_securityhub.types.target.Target"] = None,
    ) -> "capo_securityhub.types.start_configuration_policy_association_response.StartConfigurationPolicyAssociationResponse":
        """<p> Associates a target account, organizational unit, or the root with a specified configuration. The target can be associated with a configuration policy or self-managed behavior. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            configuration_policy_identifier: <p> The Amazon Resource Name (ARN) of a configuration policy, the universally unique identifier (UUID) of a configuration policy, or a value of <code>SELF_MANAGED_SECURITY_HUB</code> for a self-managed configuration. </p>
            target: <p> The identifier of the target account, organizational unit, or the root to associate with the specified configuration. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To associate a configuration with a target
            This operation associates a configuration policy or self-managed behavior with the target account, organizational unit, or the root.

            >>> await client.start_configuration_policy_association(configuration_policy_identifier='arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', target={'AccountId': '111122223333'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.start_configuration_policy_association_request.StartConfigurationPolicyAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.start_configuration_policy_association_response.StartConfigurationPolicyAssociationResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.start_configuration_policy_association

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.start_configuration_policy_association.async_start_configuration_policy_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.start_configuration_policy_association_request.StartConfigurationPolicyAssociationRequest = {}
        if configuration_policy_identifier is not None:
            input_["configuration_policy_identifier"] = configuration_policy_identifier
        if target is not None:
            input_["target"] = target

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_configuration_policy_disassociation(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        target: Optional["capo_securityhub.types.target.Target"] = None,
        configuration_policy_identifier: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.start_configuration_policy_disassociation_response.StartConfigurationPolicyDisassociationResponse":
        """<p> Disassociates a target account, organizational unit, or the root from a specified configuration. When you disassociate a configuration from its target, the target inherits the configuration of the closest parent. If there’s no configuration to inherit, the target retains its settings but becomes a self-managed account. A target can be disassociated from a configuration policy or self-managed behavior. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            target: <p> The identifier of the target account, organizational unit, or the root to disassociate from the specified configuration. </p>
            configuration_policy_identifier: <p> The Amazon Resource Name (ARN) of a configuration policy, the universally unique identifier (UUID) of a configuration policy, or a value of <code>SELF_MANAGED_SECURITY_HUB</code> for a self-managed configuration. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disassociate a configuration from a target
            This operation disassociates a configuration policy or self-managed behavior from the target account, organizational unit, or the root.

            >>> await client.start_configuration_policy_disassociation(target={'RootId': 'r-f6g7h8i9j0example'}, configuration_policy_identifier='SELF_MANAGED_SECURITY_HUB')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.start_configuration_policy_disassociation_request.StartConfigurationPolicyDisassociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.start_configuration_policy_disassociation_response.StartConfigurationPolicyDisassociationResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.start_configuration_policy_disassociation

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.start_configuration_policy_disassociation.async_start_configuration_policy_disassociation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.start_configuration_policy_disassociation_request.StartConfigurationPolicyDisassociationRequest = {}
        if target is not None:
            input_["target"] = target
        if configuration_policy_identifier is not None:
            input_["configuration_policy_identifier"] = configuration_policy_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_securityhub.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        tags: Optional["capo_securityhub.types.tag_map.TagMap"] = None,
    ) -> "capo_securityhub.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to apply the tags to.</p>
            tags: <p>The tags to add to the resource. You can add up to 50 tags at a time. The tag keys can be no longer than 128 characters. The tag values can be no longer than 256 characters.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To tag a resource
            The following example adds the 'Department' and 'Area' tags to the specified resource.

            >>> await client.tag_resource(resource_arn='arn:aws:securityhub:us-west-1:123456789012:hub/default', tags={'Department': 'Operations', 'Area': 'USMidwest'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_securityhub.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        tag_keys: Optional["capo_securityhub.types.tag_key_list.TagKeyList"] = None,
    ) -> "capo_securityhub.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to remove the tags from.</p>
            tag_keys: <p>The tag keys associated with the tags to remove from the resource. You can remove up to 50 tags at a time.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove tags from a resource
            The following example removes the 'Department' tag from the specified resource.

            >>> await client.untag_resource(resource_arn='arn:aws:securityhub:us-west-1:123456789012:hub/default', tag_keys=['Department'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_action_target(
        self,
        action_target_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        name: Optional["capo_securityhub.types.non_empty_string.NonEmptyString"] = None,
        description: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.update_action_target_response.UpdateActionTargetResponse":
        """<p>Updates the name and description of a custom action target in Security Hub CSPM.</p>

        Args:
            action_target_arn: <p>The ARN of the custom action target to update.</p>
            name: <p>The updated name of the custom action target.</p>
            description: <p>The updated description for the custom action target.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update the name and description of a custom action target
            The following example updates the name and description of a custom action target in Security Hub. You can create custom actions to automatically respond to Security Hub findings using Amazon EventBridge.

            >>> await client.update_action_target(action_target_arn='arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation', name='Chat custom action', description='Sends specified findings to customer service chat')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_action_target_request.UpdateActionTargetRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_action_target_response.UpdateActionTargetResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_action_target

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_action_target.async_update_action_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_action_target_request.UpdateActionTargetRequest = {
            "action_target_arn": action_target_arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_aggregator_v2(
        self,
        aggregator_v2_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        region_linking_mode: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        linked_regions: Optional[
            "capo_securityhub.types.string_list.StringList"
        ] = None,
    ) -> "capo_securityhub.types.update_aggregator_v2_response.UpdateAggregatorV2Response":
        """<p>Udpates the configuration for the Aggregator V2.</p>

        Args:
            aggregator_v2_arn: <p>The ARN of the Aggregator V2.</p>
            region_linking_mode: <p>Determines how Amazon Web Services Regions should be linked to the Aggregator V2.</p>
            linked_regions: <p>A list of Amazon Web Services Regions linked to the aggegation Region.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_aggregator_v2_request.UpdateAggregatorV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_aggregator_v2_response.UpdateAggregatorV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_aggregator_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_aggregator_v2.async_update_aggregator_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_aggregator_v2_request.UpdateAggregatorV2Request = {
            "aggregator_v2_arn": aggregator_v2_arn
        }
        if region_linking_mode is not None:
            input_["region_linking_mode"] = region_linking_mode
        if linked_regions is not None:
            input_["linked_regions"] = linked_regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_automation_rule_v2(
        self,
        identifier: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        rule_status: Optional[
            "capo_securityhub.types.rule_status_v2.RuleStatusV2"
        ] = None,
        rule_order: Optional[
            "capo_securityhub.types.rule_order_value_v2.RuleOrderValueV2"
        ] = None,
        description: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        rule_name: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        criteria: Optional["capo_securityhub.types.criteria.Criteria"] = None,
        actions: Optional[
            "capo_securityhub.types.automation_rules_action_list_v2.AutomationRulesActionListV2"
        ] = None,
    ) -> "capo_securityhub.types.update_automation_rule_v2_response.UpdateAutomationRuleV2Response":
        """<p>Updates a V2 automation rule.</p>

        Args:
            identifier: <p>The ARN of the automation rule.</p>
            rule_status: <p>The status of the automation rule.</p>
            rule_order: <p>Represents a value for the rule priority.</p>
            description: <p>A description of the automation rule.</p>
            rule_name: <p>The name of the automation rule.</p>
            criteria: <p>The filtering type and configuration of the automation rule.</p>
            actions: <p>A list of actions to be performed when the rule criteria is met.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_automation_rule_v2_request.UpdateAutomationRuleV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_automation_rule_v2_response.UpdateAutomationRuleV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_automation_rule_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_automation_rule_v2.async_update_automation_rule_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_automation_rule_v2_request.UpdateAutomationRuleV2Request = {
            "identifier": identifier
        }
        if rule_status is not None:
            input_["rule_status"] = rule_status
        if rule_order is not None:
            input_["rule_order"] = rule_order
        if description is not None:
            input_["description"] = description
        if rule_name is not None:
            input_["rule_name"] = rule_name
        if criteria is not None:
            input_["criteria"] = criteria
        if actions is not None:
            input_["actions"] = actions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configuration_policy(
        self,
        identifier: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        name: Optional["capo_securityhub.types.non_empty_string.NonEmptyString"] = None,
        description: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        updated_reason: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        configuration_policy: Optional["capo_securityhub.types.policy.Policy"] = None,
    ) -> "capo_securityhub.types.update_configuration_policy_response.UpdateConfigurationPolicyResponse":
        """<p> Updates a configuration policy. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            identifier: <p> The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy. </p>
            name: <p> The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: <code>-, ., !, *, /</code>. </p>
            description: <p> The description of the configuration policy. </p>
            updated_reason: <p> The reason for updating the configuration policy. </p>
            configuration_policy: <p> An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls). </p> <p>When updating a configuration policy, provide a complete list of standards that you want to enable and a complete list of controls that you want to enable or disable. The updated configuration replaces the current configuration.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a configuration policy
            This operation updates the specified configuration policy.

            >>> await client.update_configuration_policy(identifier='arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', name='TestConfigurationPolicy', description='Updated configuration policy for testing FSBP and CIS', updated_reason='Enabling ACM.2', configuration_policy={'SecurityHub': {'ServiceEnabled': True, 'EnabledStandardIdentifiers': ['arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0', 'arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0'], 'SecurityControlsConfiguration': {'DisabledSecurityControlIdentifiers': ['CloudWatch.1', 'CloudWatch.2'], 'SecurityControlCustomParameters': [{'SecurityControlId': 'ACM.1', 'Parameters': {'daysToExpiration': {'ValueType': 'CUSTOM', 'Value': {'Integer': 21}}}}]}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_configuration_policy_request.UpdateConfigurationPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_configuration_policy_response.UpdateConfigurationPolicyResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_configuration_policy

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_configuration_policy.async_update_configuration_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_configuration_policy_request.UpdateConfigurationPolicyRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if updated_reason is not None:
            input_["updated_reason"] = updated_reason
        if configuration_policy is not None:
            input_["configuration_policy"] = configuration_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connector(
        self,
        connector_id: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        description: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        provider: Optional[
            "capo_securityhub.types.cspm_provider_update_configuration.CspmProviderUpdateConfiguration"
        ] = None,
    ) -> "capo_securityhub.types.update_connector_response.UpdateConnectorResponse":
        """<p>Updates a CSPM connector's configuration, such as the scope or regions for the connected cloud provider.</p>

        Args:
            connector_id: <p>The unique identifier of the connector to update.</p>
            description: <p>The updated description of the connector.</p>
            provider: <p>The updated cloud provider configuration for the connector.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a CSPM connector
            This operation updates the configuration of a CSPM connector.

            >>> await client.update_connector(connector_id='cspm-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', description='Updated connector description', provider={'Azure': {'ScopeConfiguration': {'ScopeType': 'SUBSCRIPTION', 'ScopeValues': ['sub-1234-5678-abcd', 'sub-9012-3456-efgh']}, 'AzureRegions': ['eastus', 'westus2', 'northeurope']}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_connector_request.UpdateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_connector_response.UpdateConnectorResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_connector

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_connector.async_update_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_connector_request.UpdateConnectorRequest = {
            "connector_id": connector_id
        }
        if description is not None:
            input_["description"] = description
        if provider is not None:
            input_["provider"] = provider

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connector_v2(
        self,
        connector_id: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        description: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        provider: Optional[
            "capo_securityhub.types.provider_update_configuration.ProviderUpdateConfiguration"
        ] = None,
    ) -> (
        "capo_securityhub.types.update_connector_v2_response.UpdateConnectorV2Response"
    ):
        """<p>Grants permission to update a connectorV2 based on its id and input parameters.</p>

        Args:
            connector_id: <p>The UUID of the connectorV2 to identify connectorV2 resource.</p>
            description: <p>The description of the connectorV2.</p>
            provider: <p>The third-party provider’s service configuration.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.conflict_exception.ConflictException: <p>The request causes conflict with the current state of the service resource.</p>
            capo_securityhub.errors.internal_server_exception.InternalServerException: <p> The request has failed due to an internal failure of the service. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.throttling_exception.ThrottlingException: <p> The limit on the number of requests per second was exceeded. </p>
            capo_securityhub.errors.validation_exception.ValidationException: <p>The request has failed validation because it's missing required fields or has invalid inputs.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_connector_v2_request.UpdateConnectorV2Request]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_connector_v2_response.UpdateConnectorV2Response"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_connector_v2

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_connector_v2.async_update_connector_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_connector_v2_request.UpdateConnectorV2Request = {
            "connector_id": connector_id
        }
        if description is not None:
            input_["description"] = description
        if provider is not None:
            input_["provider"] = provider

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_finding_aggregator(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        finding_aggregator_arn: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        region_linking_mode: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        regions: Optional["capo_securityhub.types.string_list.StringList"] = None,
    ) -> "capo_securityhub.types.update_finding_aggregator_response.UpdateFindingAggregatorResponse":
        """<note> <p>The <i>aggregation Region</i> is now called the <i>home Region</i>.</p> </note> <p>Updates cross-Region aggregation settings. You can use this operation to update the Region linking mode and the list of included or excluded Amazon Web Services Regions. However, you can't use this operation to change the home Region.</p> <p>You can invoke this operation from the current home Region only. </p>

        Args:
            finding_aggregator_arn: <p>The ARN of the finding aggregator. To obtain the ARN, use <code>ListFindingAggregators</code>.</p>
            region_linking_mode: <p>Indicates whether to aggregate findings from all of the available Regions in the current partition. Also determines whether to automatically aggregate findings from new Regions as Security Hub CSPM supports them and you opt into them.</p> <p>The selected option also determines how to use the Regions provided in the Regions list.</p> <p>The options are as follows:</p> <ul> <li> <p> <code>ALL_REGIONS</code> - Aggregates findings from all of the Regions where Security Hub CSPM is enabled. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them. </p> </li> <li> <p> <code>ALL_REGIONS_EXCEPT_SPECIFIED</code> - Aggregates findings from all of the Regions where Security Hub CSPM is enabled, except for the Regions listed in the <code>Regions</code> parameter. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them. </p> </li> <li> <p> <code>SPECIFIED_REGIONS</code> - Aggregates findings only from the Regions listed in the <code>Regions</code> parameter. Security Hub CSPM does not automatically aggregate findings from new Regions. </p> </li> <li> <p> <code>NO_REGIONS</code> - Aggregates no data because no Regions are selected as linked Regions. </p> </li> </ul>
            regions: <p>If <code>RegionLinkingMode</code> is <code>ALL_REGIONS_EXCEPT_SPECIFIED</code>, then this is a space-separated list of Regions that don't replicate and send findings to the home Region.</p> <p>If <code>RegionLinkingMode</code> is <code>SPECIFIED_REGIONS</code>, then this is a space-separated list of Regions that do replicate and send findings to the home Region.</p> <p>An <code>InvalidInputException</code> error results if you populate this field while <code>RegionLinkingMode</code> is <code>NO_REGIONS</code>.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update cross-Region aggregation settings
            The following example updates the cross-Region aggregation configuration. You use this operation to change the list of linked Regions and the treatment of new Regions. However, you cannot use this operation to change the aggregation Region.

            >>> await client.update_finding_aggregator(finding_aggregator_arn='arn:aws:securityhub:us-east-1:123456789012:finding-aggregator/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', region_linking_mode='SPECIFIED_REGIONS', regions=['us-west-1', 'us-west-2'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_finding_aggregator_request.UpdateFindingAggregatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_finding_aggregator_response.UpdateFindingAggregatorResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_finding_aggregator

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_finding_aggregator.async_update_finding_aggregator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_finding_aggregator_request.UpdateFindingAggregatorRequest = {}
        if finding_aggregator_arn is not None:
            input_["finding_aggregator_arn"] = finding_aggregator_arn
        if region_linking_mode is not None:
            input_["region_linking_mode"] = region_linking_mode
        if regions is not None:
            input_["regions"] = regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_findings(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        filters: Optional[
            "capo_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
        ] = None,
        note: Optional["capo_securityhub.types.note_update.NoteUpdate"] = None,
        record_state: Optional[
            "capo_securityhub.types.record_state.RecordState"
        ] = None,
    ) -> "capo_securityhub.types.update_findings_response.UpdateFindingsResponse":
        """<p> <code>UpdateFindings</code> is a deprecated operation. Instead of <code>UpdateFindings</code>, use the <code>BatchUpdateFindings</code> operation.</p> <p>The <code>UpdateFindings</code> operation updates the <code>Note</code> and <code>RecordState</code> of the Security Hub CSPM aggregated findings that the filter attributes specify. Any member account that can view the finding can also see the update to the finding.</p> <p>Finding updates made with <code>UpdateFindings</code> aren't persisted if the same finding is later updated by the finding provider through the <code>BatchImportFindings</code> operation. In addition, Security Hub CSPM doesn't record updates made with <code>UpdateFindings</code> in the finding history.</p>

        Args:
            filters: <p>A collection of attributes that specify which findings you want to update.</p>
            note: <p>The updated note for the finding.</p>
            record_state: <p>The updated record state for the finding.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_findings_request.UpdateFindingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_findings_response.UpdateFindingsResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_findings

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_findings.async_update_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_findings_request.UpdateFindingsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if note is not None:
            input_["note"] = note
        if record_state is not None:
            input_["record_state"] = record_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_insight(
        self,
        insight_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        name: Optional["capo_securityhub.types.non_empty_string.NonEmptyString"] = None,
        filters: Optional[
            "capo_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
        ] = None,
        group_by_attribute: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.update_insight_response.UpdateInsightResponse":
        """<p>Updates the Security Hub CSPM insight identified by the specified insight ARN.</p>

        Args:
            insight_arn: <p>The ARN of the insight that you want to update.</p>
            name: <p>The updated name for the insight.</p>
            filters: <p>The updated filters that define this insight.</p>
            group_by_attribute: <p>The updated <code>GroupBy</code> attribute that defines this insight.</p>

        Raises:
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an insight
            The following example updates the specified Security Hub insight.

            >>> await client.update_insight(insight_arn='arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', name='High severity role findings', filters={'ResourceType': [{'Comparison': 'EQUALS', 'Value': 'AwsIamRole'}], 'SeverityLabel': [{'Comparison': 'EQUALS', 'Value': 'HIGH'}]})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_insight_request.UpdateInsightRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_insight_response.UpdateInsightResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_insight

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_insight.async_update_insight(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_insight_request.UpdateInsightRequest = {
            "insight_arn": insight_arn
        }
        if name is not None:
            input_["name"] = name
        if filters is not None:
            input_["filters"] = filters
        if group_by_attribute is not None:
            input_["group_by_attribute"] = group_by_attribute

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_organization_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        auto_enable: Optional["capo_securityhub.types.boolean.Boolean"] = None,
        auto_enable_standards: Optional[
            "capo_securityhub.types.auto_enable_standards.AutoEnableStandards"
        ] = None,
        organization_configuration: Optional[
            "capo_securityhub.types.organization_configuration.OrganizationConfiguration"
        ] = None,
    ) -> "capo_securityhub.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse":
        """<p>Updates the configuration of your organization in Security Hub CSPM. Only the Security Hub CSPM administrator account can invoke this operation.</p>

        Args:
            auto_enable: <p>Whether to automatically enable Security Hub CSPM in new member accounts when they join the organization.</p> <p>If set to <code>true</code>, then Security Hub CSPM is automatically enabled in new accounts. If set to <code>false</code>, then Security Hub CSPM isn't enabled in new accounts automatically. The default value is <code>false</code>.</p> <p>If the <code>ConfigurationType</code> of your organization is set to <code>CENTRAL</code>, then this field is set to <code>false</code> and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which Security Hub CSPM is enabled and associate the policy with new organization accounts.</p>
            auto_enable_standards: <p>Whether to automatically enable Security Hub CSPM <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html">default standards</a> in new member accounts when they join the organization.</p> <p>The default value of this parameter is equal to <code>DEFAULT</code>.</p> <p>If equal to <code>DEFAULT</code>, then Security Hub CSPM default standards are automatically enabled for new member accounts. If equal to <code>NONE</code>, then default standards are not automatically enabled for new member accounts.</p> <p>If the <code>ConfigurationType</code> of your organization is set to <code>CENTRAL</code>, then this field is set to <code>NONE</code> and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which specific security standards are enabled and associate the policy with new organization accounts.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update organization configuration
            This operation updates the way your organization is configured in Security Hub. Only a Security Hub administrator account can invoke this operation.

            >>> await client.update_organization_configuration(auto_enable=False, auto_enable_standards='NONE', organization_configuration={'ConfigurationType': 'CENTRAL'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_organization_configuration

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_organization_configuration.async_update_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest = {}
        if auto_enable is not None:
            input_["auto_enable"] = auto_enable
        if auto_enable_standards is not None:
            input_["auto_enable_standards"] = auto_enable_standards
        if organization_configuration is not None:
            input_["organization_configuration"] = organization_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_security_control(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        security_control_id: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        parameters: Optional["capo_securityhub.types.parameters.Parameters"] = None,
        last_update_reason: Optional[
            "capo_securityhub.types.alpha_numeric_non_empty_string.AlphaNumericNonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.update_security_control_response.UpdateSecurityControlResponse":
        """<p> Updates the properties of a security control. </p>

        Args:
            security_control_id: <p> The Amazon Resource Name (ARN) or ID of the control to update. </p>
            parameters: <p> An object that specifies which security control parameters to update. </p>
            last_update_reason: <p> The most recent reason for updating the properties of the security control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores. </p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_in_use_exception.ResourceInUseException: <p> The request was rejected because it conflicts with the resource's availability. For example, you tried to update a security control that's currently in the <code>UPDATING</code> state. </p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update security control properties
            The following example updates the specified security control. Specifically, this example updates control parameters.

            >>> await client.update_security_control(security_control_id='ACM.1', parameters={'maxCredentialUsageAge': {'ValueType': 'CUSTOM', 'Value': {'Integer': 15}}}, last_update_reason='Comply with internal requirements')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_security_control_request.UpdateSecurityControlRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_security_control_response.UpdateSecurityControlResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_security_control

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_security_control.async_update_security_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_security_control_request.UpdateSecurityControlRequest = {}
        if security_control_id is not None:
            input_["security_control_id"] = security_control_id
        if parameters is not None:
            input_["parameters"] = parameters
        if last_update_reason is not None:
            input_["last_update_reason"] = last_update_reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_security_hub_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        auto_enable_controls: Optional["capo_securityhub.types.boolean.Boolean"] = None,
        control_finding_generator: Optional[
            "capo_securityhub.types.control_finding_generator.ControlFindingGenerator"
        ] = None,
    ) -> "capo_securityhub.types.update_security_hub_configuration_response.UpdateSecurityHubConfigurationResponse":
        """<p>Updates configuration options for Security Hub CSPM.</p>

        Args:
            auto_enable_controls: <p>Whether to automatically enable new controls when they are added to standards that are enabled.</p> <p>By default, this is set to <code>true</code>, and new controls are enabled automatically. To not automatically enable new controls, set this to <code>false</code>. </p> <p>When you automatically enable new controls, you can interact with the controls in the console and programmatically immediately after release. However, automatically enabled controls have a temporary default status of <code>DISABLED</code>. It can take up to several days for Security Hub CSPM to process the control release and designate the control as <code>ENABLED</code> in your account. During the processing period, you can manually enable or disable a control, and Security Hub CSPM will maintain that designation regardless of whether you have <code>AutoEnableControls</code> set to <code>true</code>.</p>
            control_finding_generator: <p>Updates whether the calling account has consolidated control findings turned on. If the value for this field is set to <code>SECURITY_CONTROL</code>, Security Hub CSPM generates a single finding for a control check even when the check applies to multiple enabled standards.</p> <p>If the value for this field is set to <code>STANDARD_CONTROL</code>, Security Hub CSPM generates separate findings for a control check when the check applies to multiple enabled standards.</p> <p>For accounts that are part of an organization, this value can only be updated in the administrator account.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current Amazon Web Services account or throttling limits. The error code describes the limit exceeded.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update Security Hub settings
            The following example updates Security Hub settings to turn on consolidated control findings, and to automatically enable new controls in enabled standards.

            >>> await client.update_security_hub_configuration(auto_enable_controls=True, control_finding_generator='SECURITY_CONTROL')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_security_hub_configuration_request.UpdateSecurityHubConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_security_hub_configuration_response.UpdateSecurityHubConfigurationResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_security_hub_configuration

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_security_hub_configuration.async_update_security_hub_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_security_hub_configuration_request.UpdateSecurityHubConfigurationRequest = {}
        if auto_enable_controls is not None:
            input_["auto_enable_controls"] = auto_enable_controls
        if control_finding_generator is not None:
            input_["control_finding_generator"] = control_finding_generator

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_standards_control(
        self,
        standards_control_arn: "capo_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncSecurityHubClientConfig] = None,
        control_status: Optional[
            "capo_securityhub.types.control_status.ControlStatus"
        ] = None,
        disabled_reason: Optional[
            "capo_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_securityhub.types.update_standards_control_response.UpdateStandardsControlResponse":
        """<p>Used to control whether an individual security standard control is enabled or disabled.</p> <p>Calls to this operation return a <code>RESOURCE_NOT_FOUND_EXCEPTION</code> error when the standard subscription for the control has <code>StandardsControlsUpdatable</code> value <code>NOT_READY_FOR_UPDATES</code>.</p>

        Args:
            standards_control_arn: <p>The ARN of the security standard control to enable or disable.</p>
            control_status: <p>The updated status of the security standard control.</p>
            disabled_reason: <p>A description of the reason why you are disabling a security standard control. If you are disabling a control, then this is required.</p>

        Raises:
            capo_securityhub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action specified in the request.</p>
            capo_securityhub.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_securityhub.errors.invalid_access_exception.InvalidAccessException: <p>The account doesn't have permission to perform this action.</p>
            capo_securityhub.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because you supplied an invalid or out-of-range value for an input parameter.</p>
            capo_securityhub.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because we can't find the specified resource.</p>
            capo_securityhub.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update the enablement status of a standard control
            The following example disables the specified control in the specified security standard.

            >>> await client.update_standards_control(standards_control_arn='arn:aws:securityhub:us-west-1:123456789012:control/pci-dss/v/3.2.1/PCI.AutoScaling.1', control_status='DISABLED', disabled_reason='Not applicable to my service')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityhub.types.update_standards_control_request.UpdateStandardsControlRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityhub.types.update_standards_control_response.UpdateStandardsControlResponse"
        ]:
            import capo_securityhub._operations.security_hub_api_service.update_standards_control

            (
                output,
                http_response,
            ) = await capo_securityhub._operations.security_hub_api_service.update_standards_control.async_update_standards_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securityhub.types.update_standards_control_request.UpdateStandardsControlRequest = {
            "standards_control_arn": standards_control_arn
        }
        if control_status is not None:
            input_["control_status"] = control_status
        if disabled_reason is not None:
            input_["disabled_reason"] = disabled_reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
