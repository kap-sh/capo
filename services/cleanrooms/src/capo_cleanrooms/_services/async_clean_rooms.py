"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AWSBastionControlPlaneServiceLambda``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_cleanrooms._auth._signers
import capo_cleanrooms._auth._sigv4
from capo_cleanrooms._auth._identity import Credentials
from capo_cleanrooms._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cleanrooms._auth._zapros_handler import AuthMiddleware
from capo_cleanrooms._pagination import resolve_path as _resolve_path
from capo_cleanrooms._resources.aws_bastion_control_plane_service_lambda.analysis_template_resource import (
    AsyncAnalysisTemplateResource,
)
from capo_cleanrooms._resources.aws_bastion_control_plane_service_lambda.collaboration_resource import (
    AsyncCollaborationResource,
)
from capo_cleanrooms._resources.aws_bastion_control_plane_service_lambda.configured_audience_model_association_resource import (
    AsyncConfiguredAudienceModelAssociationResource,
)
from capo_cleanrooms._resources.aws_bastion_control_plane_service_lambda.configured_table_association_resource import (
    AsyncConfiguredTableAssociationResource,
)
from capo_cleanrooms._resources.aws_bastion_control_plane_service_lambda.configured_table_resource import (
    AsyncConfiguredTableResource,
)
from capo_cleanrooms._resources.aws_bastion_control_plane_service_lambda.id_mapping_table_resource import (
    AsyncIdMappingTableResource,
)
from capo_cleanrooms._resources.aws_bastion_control_plane_service_lambda.id_namespace_association_resource import (
    AsyncIdNamespaceAssociationResource,
)
from capo_cleanrooms._resources.aws_bastion_control_plane_service_lambda.intermediate_table_resource import (
    AsyncIntermediateTableResource,
)
from capo_cleanrooms._resources.aws_bastion_control_plane_service_lambda.membership_resource import (
    AsyncMembershipResource,
)
from capo_cleanrooms._resources.aws_bastion_control_plane_service_lambda.privacy_budget_template_resource import (
    AsyncPrivacyBudgetTemplateResource,
)
from capo_cleanrooms._services._aws_config import aaws_config
from capo_cleanrooms._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.allowed_column_list
    import capo_cleanrooms.types.allowed_result_regions
    import capo_cleanrooms.types.analysis_format
    import capo_cleanrooms.types.analysis_log_export_identifier
    import capo_cleanrooms.types.analysis_log_export_result_configuration
    import capo_cleanrooms.types.analysis_log_export_status
    import capo_cleanrooms.types.analysis_log_export_summary
    import capo_cleanrooms.types.analysis_method
    import capo_cleanrooms.types.analysis_parameter_list
    import capo_cleanrooms.types.analysis_rule_type
    import capo_cleanrooms.types.analysis_schema
    import capo_cleanrooms.types.analysis_source
    import capo_cleanrooms.types.analysis_template_arn
    import capo_cleanrooms.types.analysis_template_arn_list
    import capo_cleanrooms.types.analysis_template_identifier
    import capo_cleanrooms.types.analytics_engine
    import capo_cleanrooms.types.auto_approved_change_type_list
    import capo_cleanrooms.types.batch_get_collaboration_analysis_template_input
    import capo_cleanrooms.types.batch_get_collaboration_analysis_template_output
    import capo_cleanrooms.types.batch_get_schema_analysis_rule_input
    import capo_cleanrooms.types.batch_get_schema_analysis_rule_output
    import capo_cleanrooms.types.batch_get_schema_input
    import capo_cleanrooms.types.batch_get_schema_output
    import capo_cleanrooms.types.budgeted_resource_arn
    import capo_cleanrooms.types.change_input_list
    import capo_cleanrooms.types.change_request_action
    import capo_cleanrooms.types.change_request_status
    import capo_cleanrooms.types.cleanrooms_arn
    import capo_cleanrooms.types.collaboration_change_request_identifier
    import capo_cleanrooms.types.collaboration_change_request_summary
    import capo_cleanrooms.types.collaboration_configured_audience_model_association_summary
    import capo_cleanrooms.types.collaboration_description
    import capo_cleanrooms.types.collaboration_id_namespace_association_summary
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.collaboration_job_log_status
    import capo_cleanrooms.types.collaboration_name
    import capo_cleanrooms.types.collaboration_privacy_budget_summary
    import capo_cleanrooms.types.collaboration_privacy_budget_template_summary
    import capo_cleanrooms.types.collaboration_query_log_status
    import capo_cleanrooms.types.compute_configuration
    import capo_cleanrooms.types.configured_audience_model_arn
    import capo_cleanrooms.types.configured_audience_model_association_identifier
    import capo_cleanrooms.types.configured_audience_model_association_name
    import capo_cleanrooms.types.configured_audience_model_association_summary
    import capo_cleanrooms.types.configured_table_analysis_rule_policy
    import capo_cleanrooms.types.configured_table_analysis_rule_type
    import capo_cleanrooms.types.configured_table_association_analysis_rule_policy
    import capo_cleanrooms.types.configured_table_association_analysis_rule_type
    import capo_cleanrooms.types.configured_table_association_identifier
    import capo_cleanrooms.types.configured_table_identifier
    import capo_cleanrooms.types.create_analysis_template_input
    import capo_cleanrooms.types.create_analysis_template_output
    import capo_cleanrooms.types.create_collaboration_change_request_input
    import capo_cleanrooms.types.create_collaboration_change_request_output
    import capo_cleanrooms.types.create_collaboration_input
    import capo_cleanrooms.types.create_collaboration_output
    import capo_cleanrooms.types.create_configured_audience_model_association_input
    import capo_cleanrooms.types.create_configured_audience_model_association_output
    import capo_cleanrooms.types.create_configured_table_analysis_rule_input
    import capo_cleanrooms.types.create_configured_table_analysis_rule_output
    import capo_cleanrooms.types.create_configured_table_association_analysis_rule_input
    import capo_cleanrooms.types.create_configured_table_association_analysis_rule_output
    import capo_cleanrooms.types.create_configured_table_association_input
    import capo_cleanrooms.types.create_configured_table_association_output
    import capo_cleanrooms.types.create_configured_table_input
    import capo_cleanrooms.types.create_configured_table_output
    import capo_cleanrooms.types.create_id_mapping_table_input
    import capo_cleanrooms.types.create_id_mapping_table_output
    import capo_cleanrooms.types.create_id_namespace_association_input
    import capo_cleanrooms.types.create_id_namespace_association_output
    import capo_cleanrooms.types.create_intermediate_table_analysis_rule_input
    import capo_cleanrooms.types.create_intermediate_table_analysis_rule_output
    import capo_cleanrooms.types.create_intermediate_table_input
    import capo_cleanrooms.types.create_intermediate_table_output
    import capo_cleanrooms.types.create_membership_input
    import capo_cleanrooms.types.create_membership_output
    import capo_cleanrooms.types.create_privacy_budget_template_input
    import capo_cleanrooms.types.create_privacy_budget_template_output
    import capo_cleanrooms.types.data_encryption_metadata
    import capo_cleanrooms.types.delete_analysis_template_input
    import capo_cleanrooms.types.delete_analysis_template_output
    import capo_cleanrooms.types.delete_collaboration_input
    import capo_cleanrooms.types.delete_collaboration_output
    import capo_cleanrooms.types.delete_configured_audience_model_association_input
    import capo_cleanrooms.types.delete_configured_audience_model_association_output
    import capo_cleanrooms.types.delete_configured_table_analysis_rule_input
    import capo_cleanrooms.types.delete_configured_table_analysis_rule_output
    import capo_cleanrooms.types.delete_configured_table_association_analysis_rule_input
    import capo_cleanrooms.types.delete_configured_table_association_analysis_rule_output
    import capo_cleanrooms.types.delete_configured_table_association_input
    import capo_cleanrooms.types.delete_configured_table_association_output
    import capo_cleanrooms.types.delete_configured_table_input
    import capo_cleanrooms.types.delete_configured_table_output
    import capo_cleanrooms.types.delete_id_mapping_table_input
    import capo_cleanrooms.types.delete_id_mapping_table_output
    import capo_cleanrooms.types.delete_id_namespace_association_input
    import capo_cleanrooms.types.delete_id_namespace_association_output
    import capo_cleanrooms.types.delete_intermediate_table_analysis_rule_input
    import capo_cleanrooms.types.delete_intermediate_table_analysis_rule_output
    import capo_cleanrooms.types.delete_intermediate_table_input
    import capo_cleanrooms.types.delete_intermediate_table_output
    import capo_cleanrooms.types.delete_member_input
    import capo_cleanrooms.types.delete_member_output
    import capo_cleanrooms.types.delete_membership_input
    import capo_cleanrooms.types.delete_membership_output
    import capo_cleanrooms.types.delete_privacy_budget_template_input
    import capo_cleanrooms.types.delete_privacy_budget_template_output
    import capo_cleanrooms.types.disallow_intermediate_table_input
    import capo_cleanrooms.types.disallow_intermediate_table_output
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.error_message_configuration
    import capo_cleanrooms.types.filterable_member_status
    import capo_cleanrooms.types.generic_resource_name
    import capo_cleanrooms.types.get_analysis_log_export_input
    import capo_cleanrooms.types.get_analysis_log_export_output
    import capo_cleanrooms.types.get_analysis_template_input
    import capo_cleanrooms.types.get_analysis_template_output
    import capo_cleanrooms.types.get_collaboration_analysis_template_input
    import capo_cleanrooms.types.get_collaboration_analysis_template_output
    import capo_cleanrooms.types.get_collaboration_change_request_input
    import capo_cleanrooms.types.get_collaboration_change_request_output
    import capo_cleanrooms.types.get_collaboration_configured_audience_model_association_input
    import capo_cleanrooms.types.get_collaboration_configured_audience_model_association_output
    import capo_cleanrooms.types.get_collaboration_id_namespace_association_input
    import capo_cleanrooms.types.get_collaboration_id_namespace_association_output
    import capo_cleanrooms.types.get_collaboration_input
    import capo_cleanrooms.types.get_collaboration_output
    import capo_cleanrooms.types.get_collaboration_privacy_budget_template_input
    import capo_cleanrooms.types.get_collaboration_privacy_budget_template_output
    import capo_cleanrooms.types.get_configured_audience_model_association_input
    import capo_cleanrooms.types.get_configured_audience_model_association_output
    import capo_cleanrooms.types.get_configured_table_analysis_rule_input
    import capo_cleanrooms.types.get_configured_table_analysis_rule_output
    import capo_cleanrooms.types.get_configured_table_association_analysis_rule_input
    import capo_cleanrooms.types.get_configured_table_association_analysis_rule_output
    import capo_cleanrooms.types.get_configured_table_association_input
    import capo_cleanrooms.types.get_configured_table_association_output
    import capo_cleanrooms.types.get_configured_table_input
    import capo_cleanrooms.types.get_configured_table_output
    import capo_cleanrooms.types.get_id_mapping_table_input
    import capo_cleanrooms.types.get_id_mapping_table_output
    import capo_cleanrooms.types.get_id_namespace_association_input
    import capo_cleanrooms.types.get_id_namespace_association_output
    import capo_cleanrooms.types.get_intermediate_table_analysis_rule_input
    import capo_cleanrooms.types.get_intermediate_table_analysis_rule_output
    import capo_cleanrooms.types.get_intermediate_table_input
    import capo_cleanrooms.types.get_intermediate_table_output
    import capo_cleanrooms.types.get_membership_input
    import capo_cleanrooms.types.get_membership_output
    import capo_cleanrooms.types.get_privacy_budget_template_input
    import capo_cleanrooms.types.get_privacy_budget_template_output
    import capo_cleanrooms.types.get_protected_job_input
    import capo_cleanrooms.types.get_protected_job_output
    import capo_cleanrooms.types.get_protected_query_input
    import capo_cleanrooms.types.get_protected_query_output
    import capo_cleanrooms.types.get_schema_analysis_rule_input
    import capo_cleanrooms.types.get_schema_analysis_rule_output
    import capo_cleanrooms.types.get_schema_input
    import capo_cleanrooms.types.get_schema_output
    import capo_cleanrooms.types.id_mapping_config
    import capo_cleanrooms.types.id_mapping_table_input_reference_config
    import capo_cleanrooms.types.id_mapping_table_summary
    import capo_cleanrooms.types.id_namespace_association_identifier
    import capo_cleanrooms.types.id_namespace_association_input_reference_config
    import capo_cleanrooms.types.id_namespace_association_summary
    import capo_cleanrooms.types.intermediate_table_analysis_rule_policy
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type
    import capo_cleanrooms.types.intermediate_table_column_list
    import capo_cleanrooms.types.intermediate_table_compute_configuration
    import capo_cleanrooms.types.intermediate_table_identifier
    import capo_cleanrooms.types.intermediate_table_summary
    import capo_cleanrooms.types.intermediate_table_version_summary
    import capo_cleanrooms.types.job_type
    import capo_cleanrooms.types.kms_key_arn
    import capo_cleanrooms.types.list_analysis_log_exports_input
    import capo_cleanrooms.types.list_analysis_log_exports_output
    import capo_cleanrooms.types.list_analysis_templates_input
    import capo_cleanrooms.types.list_analysis_templates_output
    import capo_cleanrooms.types.list_collaboration_analysis_templates_input
    import capo_cleanrooms.types.list_collaboration_analysis_templates_output
    import capo_cleanrooms.types.list_collaboration_change_requests_input
    import capo_cleanrooms.types.list_collaboration_change_requests_output
    import capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_input
    import capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_output
    import capo_cleanrooms.types.list_collaboration_id_namespace_associations_input
    import capo_cleanrooms.types.list_collaboration_id_namespace_associations_output
    import capo_cleanrooms.types.list_collaboration_privacy_budget_templates_input
    import capo_cleanrooms.types.list_collaboration_privacy_budget_templates_output
    import capo_cleanrooms.types.list_collaboration_privacy_budgets_input
    import capo_cleanrooms.types.list_collaboration_privacy_budgets_output
    import capo_cleanrooms.types.list_collaborations_input
    import capo_cleanrooms.types.list_collaborations_output
    import capo_cleanrooms.types.list_configured_audience_model_associations_input
    import capo_cleanrooms.types.list_configured_audience_model_associations_output
    import capo_cleanrooms.types.list_configured_table_associations_input
    import capo_cleanrooms.types.list_configured_table_associations_output
    import capo_cleanrooms.types.list_configured_tables_input
    import capo_cleanrooms.types.list_configured_tables_output
    import capo_cleanrooms.types.list_id_mapping_tables_input
    import capo_cleanrooms.types.list_id_mapping_tables_output
    import capo_cleanrooms.types.list_id_namespace_associations_input
    import capo_cleanrooms.types.list_id_namespace_associations_output
    import capo_cleanrooms.types.list_intermediate_table_versions_input
    import capo_cleanrooms.types.list_intermediate_table_versions_output
    import capo_cleanrooms.types.list_intermediate_tables_input
    import capo_cleanrooms.types.list_intermediate_tables_output
    import capo_cleanrooms.types.list_members_input
    import capo_cleanrooms.types.list_members_output
    import capo_cleanrooms.types.list_memberships_input
    import capo_cleanrooms.types.list_memberships_output
    import capo_cleanrooms.types.list_privacy_budget_templates_input
    import capo_cleanrooms.types.list_privacy_budget_templates_output
    import capo_cleanrooms.types.list_privacy_budgets_input
    import capo_cleanrooms.types.list_privacy_budgets_output
    import capo_cleanrooms.types.list_protected_jobs_input
    import capo_cleanrooms.types.list_protected_jobs_output
    import capo_cleanrooms.types.list_protected_queries_input
    import capo_cleanrooms.types.list_protected_queries_output
    import capo_cleanrooms.types.list_schemas_input
    import capo_cleanrooms.types.list_schemas_output
    import capo_cleanrooms.types.list_tags_for_resource_input
    import capo_cleanrooms.types.list_tags_for_resource_output
    import capo_cleanrooms.types.log_export_analysis_type
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.member_abilities
    import capo_cleanrooms.types.member_list
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.membership_job_log_status
    import capo_cleanrooms.types.membership_payment_configuration
    import capo_cleanrooms.types.membership_protected_job_result_configuration
    import capo_cleanrooms.types.membership_protected_query_result_configuration
    import capo_cleanrooms.types.membership_query_log_status
    import capo_cleanrooms.types.membership_status
    import capo_cleanrooms.types.ml_member_abilities
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.parameter_map
    import capo_cleanrooms.types.payment_configuration
    import capo_cleanrooms.types.populate_id_mapping_table_input
    import capo_cleanrooms.types.populate_id_mapping_table_output
    import capo_cleanrooms.types.populate_intermediate_table_input
    import capo_cleanrooms.types.populate_intermediate_table_output
    import capo_cleanrooms.types.population_analysis_configuration
    import capo_cleanrooms.types.preview_privacy_impact_input
    import capo_cleanrooms.types.preview_privacy_impact_output
    import capo_cleanrooms.types.preview_privacy_impact_parameters_input
    import capo_cleanrooms.types.privacy_budget_summary
    import capo_cleanrooms.types.privacy_budget_template_auto_refresh
    import capo_cleanrooms.types.privacy_budget_template_identifier
    import capo_cleanrooms.types.privacy_budget_template_parameters_input
    import capo_cleanrooms.types.privacy_budget_template_summary
    import capo_cleanrooms.types.privacy_budget_template_update_parameters
    import capo_cleanrooms.types.privacy_budget_type
    import capo_cleanrooms.types.protected_job_compute_configuration
    import capo_cleanrooms.types.protected_job_identifier
    import capo_cleanrooms.types.protected_job_parameters
    import capo_cleanrooms.types.protected_job_result_configuration_input
    import capo_cleanrooms.types.protected_job_status
    import capo_cleanrooms.types.protected_job_summary
    import capo_cleanrooms.types.protected_job_type
    import capo_cleanrooms.types.protected_query_identifier
    import capo_cleanrooms.types.protected_query_result_configuration
    import capo_cleanrooms.types.protected_query_sql_parameters
    import capo_cleanrooms.types.protected_query_status
    import capo_cleanrooms.types.protected_query_summary
    import capo_cleanrooms.types.protected_query_type
    import capo_cleanrooms.types.resource_alias
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.role_arn
    import capo_cleanrooms.types.schema_analysis_rule_request_list
    import capo_cleanrooms.types.schema_type
    import capo_cleanrooms.types.selected_analysis_methods
    import capo_cleanrooms.types.start_analysis_log_export_input
    import capo_cleanrooms.types.start_analysis_log_export_output
    import capo_cleanrooms.types.start_protected_job_input
    import capo_cleanrooms.types.start_protected_job_output
    import capo_cleanrooms.types.start_protected_query_input
    import capo_cleanrooms.types.start_protected_query_output
    import capo_cleanrooms.types.synthetic_data_parameters
    import capo_cleanrooms.types.table_alias
    import capo_cleanrooms.types.table_alias_list
    import capo_cleanrooms.types.table_description
    import capo_cleanrooms.types.table_reference
    import capo_cleanrooms.types.tag_keys
    import capo_cleanrooms.types.tag_map
    import capo_cleanrooms.types.tag_resource_input
    import capo_cleanrooms.types.tag_resource_output
    import capo_cleanrooms.types.target_protected_job_status
    import capo_cleanrooms.types.target_protected_query_status
    import capo_cleanrooms.types.untag_resource_input
    import capo_cleanrooms.types.untag_resource_output
    import capo_cleanrooms.types.update_analysis_template_input
    import capo_cleanrooms.types.update_analysis_template_output
    import capo_cleanrooms.types.update_collaboration_change_request_input
    import capo_cleanrooms.types.update_collaboration_change_request_output
    import capo_cleanrooms.types.update_collaboration_input
    import capo_cleanrooms.types.update_collaboration_output
    import capo_cleanrooms.types.update_configured_audience_model_association_input
    import capo_cleanrooms.types.update_configured_audience_model_association_output
    import capo_cleanrooms.types.update_configured_table_analysis_rule_input
    import capo_cleanrooms.types.update_configured_table_analysis_rule_output
    import capo_cleanrooms.types.update_configured_table_association_analysis_rule_input
    import capo_cleanrooms.types.update_configured_table_association_analysis_rule_output
    import capo_cleanrooms.types.update_configured_table_association_input
    import capo_cleanrooms.types.update_configured_table_association_output
    import capo_cleanrooms.types.update_configured_table_input
    import capo_cleanrooms.types.update_configured_table_output
    import capo_cleanrooms.types.update_id_mapping_table_input
    import capo_cleanrooms.types.update_id_mapping_table_output
    import capo_cleanrooms.types.update_id_namespace_association_input
    import capo_cleanrooms.types.update_id_namespace_association_output
    import capo_cleanrooms.types.update_intermediate_table_analysis_rule_input
    import capo_cleanrooms.types.update_intermediate_table_analysis_rule_output
    import capo_cleanrooms.types.update_intermediate_table_input
    import capo_cleanrooms.types.update_intermediate_table_output
    import capo_cleanrooms.types.update_membership_input
    import capo_cleanrooms.types.update_membership_output
    import capo_cleanrooms.types.update_membership_payment_configuration
    import capo_cleanrooms.types.update_privacy_budget_template_input
    import capo_cleanrooms.types.update_privacy_budget_template_output
    import capo_cleanrooms.types.update_protected_job_input
    import capo_cleanrooms.types.update_protected_job_output
    import capo_cleanrooms.types.update_protected_query_input
    import capo_cleanrooms.types.update_protected_query_output
    import capo_cleanrooms.types.uuid


class AsyncCleanRoomsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncCleanRoomsClient:
    """A client for the ``CleanRooms`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = AsyncCleanRoomsClientConfig(
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

        # resources
        self.analysis_template_resource = AsyncAnalysisTemplateResource(self)
        self.collaboration_resource = AsyncCollaborationResource(self)
        self.configured_audience_model_association_resource = (
            AsyncConfiguredAudienceModelAssociationResource(self)
        )
        self.configured_table_association_resource = (
            AsyncConfiguredTableAssociationResource(self)
        )
        self.configured_table_resource = AsyncConfiguredTableResource(self)
        self.id_mapping_table_resource = AsyncIdMappingTableResource(self)
        self.id_namespace_association_resource = AsyncIdNamespaceAssociationResource(
            self
        )
        self.intermediate_table_resource = AsyncIntermediateTableResource(self)
        self.membership_resource = AsyncMembershipResource(self)
        self.privacy_budget_template_resource = AsyncPrivacyBudgetTemplateResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncCleanRoomsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCleanRoomsClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_cleanrooms.types.cleanrooms_arn.CleanroomsArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> (
        "capo_cleanrooms.types.list_tags_for_resource_output.ListTagsForResourceOutput"
    ):
        """<p>Lists all of the tags that have been added to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource you want to list tags on.</p>

        Raises:
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_cleanrooms.types.cleanrooms_arn.CleanroomsArn",
        tags: "capo_cleanrooms.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.tag_resource_output.TagResourceOutput":
        """<p>Tags a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource you want to tag.</p>
            tags: <p>A map of objects specifying each key name and value.</p>

        Raises:
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.tag_resource

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.tag_resource_input.TagResourceInput = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_cleanrooms.types.cleanrooms_arn.CleanroomsArn",
        tag_keys: "capo_cleanrooms.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a tag or list of tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource you want to remove the tag from.</p>
            tag_keys: <p>A list of key names of tags to be removed.</p>

        Raises:
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.untag_resource

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.untag_resource_input.UntagResourceInput = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_analysis_template(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        format: "capo_cleanrooms.types.analysis_format.AnalysisFormat",
        source: "capo_cleanrooms.types.analysis_source.AnalysisSource",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        analysis_parameters: Optional[
            "capo_cleanrooms.types.analysis_parameter_list.AnalysisParameterList"
        ] = None,
        schema: Optional["capo_cleanrooms.types.analysis_schema.AnalysisSchema"] = None,
        error_message_configuration: Optional[
            "capo_cleanrooms.types.error_message_configuration.ErrorMessageConfiguration"
        ] = None,
        synthetic_data_parameters: Optional[
            "capo_cleanrooms.types.synthetic_data_parameters.SyntheticDataParameters"
        ] = None,
    ) -> "capo_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput":
        """<p>Creates a new analysis template.</p>

        Args:
            description: <p>The description of the analysis template.</p>
            membership_identifier: <p>The identifier for a membership resource.</p>
            name: <p>The name of the analysis template.</p>
            format: <p>The format of the analysis template.</p>
            source: <p>The information in the analysis template.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            analysis_parameters: <p>The parameters of the analysis template.</p>
            error_message_configuration: <p>The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to <code>DETAILED</code>, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.</p>
            synthetic_data_parameters: <p>The parameters for generating synthetic data when running the analysis template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_analysis_template.async_create_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "name": name,
            "format": format,
            "source": source,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if analysis_parameters is not None:
            input_["analysis_parameters"] = analysis_parameters
        if schema is not None:
            input_["schema"] = schema
        if error_message_configuration is not None:
            input_["error_message_configuration"] = error_message_configuration
        if synthetic_data_parameters is not None:
            input_["synthetic_data_parameters"] = synthetic_data_parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_analysis_template(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput":
        """<p>Retrieves an analysis template.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_analysis_template_input.GetAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_template.async_get_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_analysis_template_input.GetAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "analysis_template_identifier": analysis_template_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_analysis_template(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput":
        """<p>Updates the analysis template metadata.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>
            description: <p>A new description for the analysis template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_analysis_template_input.UpdateAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_analysis_template.async_update_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_analysis_template_input.UpdateAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "analysis_template_identifier": analysis_template_identifier,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_analysis_template(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_analysis_template_output.DeleteAnalysisTemplateOutput":
        """<p>Deletes an analysis template.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_analysis_template_input.DeleteAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_analysis_template_output.DeleteAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_analysis_template.async_delete_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_analysis_template_input.DeleteAnalysisTemplateInput = {
            "membership_identifier": membership_identifier,
            "analysis_template_identifier": analysis_template_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_analysis_templates(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_analysis_templates_output.ListAnalysisTemplatesOutput":
        """<p>Lists analysis templates that the caller owns.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_analysis_templates_input.ListAnalysisTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_analysis_templates_output.ListAnalysisTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_templates

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_templates.async_list_analysis_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_analysis_templates_input.ListAnalysisTemplatesInput = {
            "membership_identifier": membership_identifier
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

    async def create_collaboration(
        self,
        members: "capo_cleanrooms.types.member_list.MemberList",
        name: "capo_cleanrooms.types.collaboration_name.CollaborationName",
        creator_member_abilities: "capo_cleanrooms.types.member_abilities.MemberAbilities",
        creator_display_name: "capo_cleanrooms.types.display_name.DisplayName",
        query_log_status: "capo_cleanrooms.types.collaboration_query_log_status.CollaborationQueryLogStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.collaboration_description.CollaborationDescription"
        ] = None,
        creator_ml_member_abilities: Optional[
            "capo_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
        ] = None,
        data_encryption_metadata: Optional[
            "capo_cleanrooms.types.data_encryption_metadata.DataEncryptionMetadata"
        ] = None,
        job_log_status: Optional[
            "capo_cleanrooms.types.collaboration_job_log_status.CollaborationJobLogStatus"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        creator_payment_configuration: Optional[
            "capo_cleanrooms.types.payment_configuration.PaymentConfiguration"
        ] = None,
        analytics_engine: Optional[
            "capo_cleanrooms.types.analytics_engine.AnalyticsEngine"
        ] = None,
        auto_approved_change_request_types: Optional[
            "capo_cleanrooms.types.auto_approved_change_type_list.AutoApprovedChangeTypeList"
        ] = None,
        allowed_result_regions: Optional[
            "capo_cleanrooms.types.allowed_result_regions.AllowedResultRegions"
        ] = None,
        is_metrics_enabled: Optional[bool] = None,
    ) -> "capo_cleanrooms.types.create_collaboration_output.CreateCollaborationOutput":
        """<p>Creates a new collaboration.</p>

        Args:
            members: <p>A list of initial members, not including the creator. This list is immutable.</p>
            name: <p>The display name for a collaboration.</p>
            description: <p>A description of the collaboration provided by the collaboration owner.</p>
            creator_member_abilities: <p>The abilities granted to the collaboration creator.</p>
            creator_ml_member_abilities: <p>The ML abilities granted to the collaboration creator.</p>
            creator_display_name: <p>The display name of the collaboration creator.</p>
            data_encryption_metadata: <p>The settings for client-side encryption with Cryptographic Computing for Clean Rooms.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the collaboration.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>Specifies whether job logs are enabled for this collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration; those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            creator_payment_configuration: <p>The collaboration creator's payment responsibilities set by the collaboration creator. </p> <p>If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer.</p>
            analytics_engine: <p> The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>
            auto_approved_change_request_types: <p>The types of change requests that are automatically approved for this collaboration.</p>
            allowed_result_regions: <p>The Amazon Web Services Regions where collaboration query results can be stored. When specified, results can only be written to these Regions. This parameter enables you to meet your compliance and data governance requirements, and implement regional data governance policies.</p>
            is_metrics_enabled: <p>An indicator as to whether metrics have been enabled or disabled for the collaboration.</p> <p>When <code>true</code>, collaboration members can opt in to Amazon CloudWatch metrics for their membership queries. The default value is <code>false</code>.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_collaboration_input.CreateCollaborationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_collaboration_output.CreateCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration.async_create_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_collaboration_input.CreateCollaborationInput = {
            "members": members,
            "name": name,
            "creator_member_abilities": creator_member_abilities,
            "creator_display_name": creator_display_name,
            "query_log_status": query_log_status,
        }
        if description is not None:
            input_["description"] = description
        if creator_ml_member_abilities is not None:
            input_["creator_ml_member_abilities"] = creator_ml_member_abilities
        if data_encryption_metadata is not None:
            input_["data_encryption_metadata"] = data_encryption_metadata
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if tags is not None:
            input_["tags"] = tags
        if creator_payment_configuration is not None:
            input_["creator_payment_configuration"] = creator_payment_configuration
        if analytics_engine is not None:
            input_["analytics_engine"] = analytics_engine
        if auto_approved_change_request_types is not None:
            input_["auto_approved_change_request_types"] = (
                auto_approved_change_request_types
            )
        if allowed_result_regions is not None:
            input_["allowed_result_regions"] = allowed_result_regions
        if is_metrics_enabled is not None:
            input_["is_metrics_enabled"] = is_metrics_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_output.GetCollaborationOutput":
        """<p>Returns metadata about a collaboration.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_input.GetCollaborationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_output.GetCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration.async_get_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_collaboration_input.GetCollaborationInput = {
            "collaboration_identifier": collaboration_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_collaboration(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        name: Optional[
            "capo_cleanrooms.types.collaboration_name.CollaborationName"
        ] = None,
        description: Optional[
            "capo_cleanrooms.types.collaboration_description.CollaborationDescription"
        ] = None,
        analytics_engine: Optional[
            "capo_cleanrooms.types.analytics_engine.AnalyticsEngine"
        ] = None,
    ) -> "capo_cleanrooms.types.update_collaboration_output.UpdateCollaborationOutput":
        """<p>Updates collaboration metadata and can only be called by the collaboration owner.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>
            name: <p>A human-readable identifier provided by the collaboration owner. Display names are not unique.</p>
            description: <p>A description of the collaboration.</p>
            analytics_engine: <p>The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_collaboration_input.UpdateCollaborationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_collaboration_output.UpdateCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration.async_update_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_collaboration_input.UpdateCollaborationInput = {
            "collaboration_identifier": collaboration_identifier
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if analytics_engine is not None:
            input_["analytics_engine"] = analytics_engine

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_collaboration(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_collaboration_output.DeleteCollaborationOutput":
        """<p>Deletes a collaboration. It can only be called by the collaboration owner.</p>

        Args:
            collaboration_identifier: <p>The identifier for the collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_collaboration_input.DeleteCollaborationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_collaboration_output.DeleteCollaborationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_collaboration

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_collaboration.async_delete_collaboration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_collaboration_input.DeleteCollaborationInput = {
            "collaboration_identifier": collaboration_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_collaborations(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        member_status: Optional[
            "capo_cleanrooms.types.filterable_member_status.FilterableMemberStatus"
        ] = None,
    ) -> "capo_cleanrooms.types.list_collaborations_output.ListCollaborationsOutput":
        """<p>Lists collaborations the caller owns, is active in, or has been invited to.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            member_status: <p>The caller's status in a collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaborations_input.ListCollaborationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaborations_output.ListCollaborationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaborations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaborations.async_list_collaborations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_collaborations_input.ListCollaborationsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if member_status is not None:
            input_["member_status"] = member_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_collaboration_analysis_template(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        analysis_template_arns: "capo_cleanrooms.types.analysis_template_arn_list.AnalysisTemplateArnList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput":
        """<p>Retrieves multiple analysis templates within a collaboration by their Amazon Resource Names (ARNs).</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            analysis_template_arns: <p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.batch_get_collaboration_analysis_template_input.BatchGetCollaborationAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.batch_get_collaboration_analysis_template_output.BatchGetCollaborationAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_collaboration_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_collaboration_analysis_template.async_batch_get_collaboration_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.batch_get_collaboration_analysis_template_input.BatchGetCollaborationAnalysisTemplateInput = {
            "collaboration_identifier": collaboration_identifier,
            "analysis_template_arns": analysis_template_arns,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_schema(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        names: "capo_cleanrooms.types.table_alias_list.TableAliasList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.batch_get_schema_output.BatchGetSchemaOutput":
        """<p>Retrieves multiple schemas by their identifiers.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schemas belong to. Currently accepts collaboration ID.</p>
            names: <p>The names for the schema objects to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.batch_get_schema_input.BatchGetSchemaInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.batch_get_schema_output.BatchGetSchemaOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema.async_batch_get_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.batch_get_schema_input.BatchGetSchemaInput = {
            "collaboration_identifier": collaboration_identifier,
            "names": names,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_schema_analysis_rule(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        schema_analysis_rule_requests: "capo_cleanrooms.types.schema_analysis_rule_request_list.SchemaAnalysisRuleRequestList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.batch_get_schema_analysis_rule_output.BatchGetSchemaAnalysisRuleOutput":
        """<p>Retrieves multiple analysis rule schemas.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the schema analysis rule.</p>
            schema_analysis_rule_requests: <p>The information that's necessary to retrieve a schema analysis rule.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.batch_get_schema_analysis_rule_input.BatchGetSchemaAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.batch_get_schema_analysis_rule_output.BatchGetSchemaAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.batch_get_schema_analysis_rule.async_batch_get_schema_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.batch_get_schema_analysis_rule_input.BatchGetSchemaAnalysisRuleInput = {
            "collaboration_identifier": collaboration_identifier,
            "schema_analysis_rule_requests": schema_analysis_rule_requests,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_collaboration_change_request(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        changes: "capo_cleanrooms.types.change_input_list.ChangeInputList",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_collaboration_change_request_output.CreateCollaborationChangeRequestOutput":
        """<p>Creates a new change request to modify an existing collaboration. This enables post-creation modifications to collaborations through a structured API-driven approach.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            changes: <p>The list of changes to apply to the collaboration. Each change specifies the type of modification and the details of what should be changed.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_collaboration_change_request_input.CreateCollaborationChangeRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_collaboration_change_request_output.CreateCollaborationChangeRequestOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration_change_request

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_collaboration_change_request.async_create_collaboration_change_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_collaboration_change_request_input.CreateCollaborationChangeRequestInput = {
            "collaboration_identifier": collaboration_identifier,
            "changes": changes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_member(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        account_id: "capo_cleanrooms.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_member_output.DeleteMemberOutput":
        """<p>Removes the specified member from a collaboration. The removed member is placed in the Removed status and can't interact with the collaboration. The removed member's data is inaccessible to active members of the collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier for the associated collaboration.</p>
            account_id: <p>The account ID of the member to remove.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_member_input.DeleteMemberInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_member_output.DeleteMemberOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_member

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_member.async_delete_member(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_member_input.DeleteMemberInput = {
            "collaboration_identifier": collaboration_identifier,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration_analysis_template(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        analysis_template_arn: "capo_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput":
        """<p>Retrieves an analysis template within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            analysis_template_arn: <p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_analysis_template_input.GetCollaborationAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_analysis_template_output.GetCollaborationAnalysisTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_analysis_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_analysis_template.async_get_collaboration_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_collaboration_analysis_template_input.GetCollaborationAnalysisTemplateInput = {
            "collaboration_identifier": collaboration_identifier,
            "analysis_template_arn": analysis_template_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration_change_request(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        change_request_identifier: "capo_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_change_request_output.GetCollaborationChangeRequestOutput":
        """<p>Retrieves detailed information about a specific collaboration change request.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            change_request_identifier: <p>A unique identifier for the change request to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_change_request_input.GetCollaborationChangeRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_change_request_output.GetCollaborationChangeRequestOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_change_request

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_change_request.async_get_collaboration_change_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_collaboration_change_request_input.GetCollaborationChangeRequestInput = {
            "collaboration_identifier": collaboration_identifier,
            "change_request_identifier": change_request_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration_configured_audience_model_association(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_configured_audience_model_association_output.GetCollaborationConfiguredAudienceModelAssociationOutput":
        """<p>Retrieves a configured audience model association within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.</p>
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_configured_audience_model_association_input.GetCollaborationConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_configured_audience_model_association_output.GetCollaborationConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_configured_audience_model_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_configured_audience_model_association.async_get_collaboration_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_collaboration_configured_audience_model_association_input.GetCollaborationConfiguredAudienceModelAssociationInput = {
            "collaboration_identifier": collaboration_identifier,
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration_id_namespace_association(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_id_namespace_association_output.GetCollaborationIdNamespaceAssociationOutput":
        """<p>Retrieves an ID namespace association from a specific collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the ID namespace association that you want to retrieve.</p>
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_id_namespace_association_input.GetCollaborationIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_id_namespace_association_output.GetCollaborationIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_id_namespace_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_id_namespace_association.async_get_collaboration_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_collaboration_id_namespace_association_input.GetCollaborationIdNamespaceAssociationInput = {
            "collaboration_identifier": collaboration_identifier,
            "id_namespace_association_identifier": id_namespace_association_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration_privacy_budget_template(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_collaboration_privacy_budget_template_output.GetCollaborationPrivacyBudgetTemplateOutput":
        """<p>Returns details about a specified privacy budget template.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            privacy_budget_template_identifier: <p>A unique identifier for one of your privacy budget templates.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_collaboration_privacy_budget_template_input.GetCollaborationPrivacyBudgetTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_collaboration_privacy_budget_template_output.GetCollaborationPrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_privacy_budget_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_collaboration_privacy_budget_template.async_get_collaboration_privacy_budget_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_collaboration_privacy_budget_template_input.GetCollaborationPrivacyBudgetTemplateInput = {
            "collaboration_identifier": collaboration_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_schema(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_schema_output.GetSchemaOutput":
        """<p>Retrieves the schema for a relation within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            name: <p>The name of the relation to retrieve the schema for.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_schema_input.GetSchemaInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_schema_output.GetSchemaOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema.async_get_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_schema_input.GetSchemaInput = {
            "collaboration_identifier": collaboration_identifier,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_schema_analysis_rule(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        type: "capo_cleanrooms.types.analysis_rule_type.AnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_schema_analysis_rule_output.GetSchemaAnalysisRuleOutput":
        """<p>Retrieves a schema analysis rule.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            name: <p>The name of the schema to retrieve the analysis rule for.</p>
            type: <p>The type of the schema analysis rule to retrieve. Schema analysis rules are uniquely identified by a combination of the collaboration, the schema name, and their type.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_schema_analysis_rule_input.GetSchemaAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_schema_analysis_rule_output.GetSchemaAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_schema_analysis_rule.async_get_schema_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_schema_analysis_rule_input.GetSchemaAnalysisRuleInput = {
            "collaboration_identifier": collaboration_identifier,
            "name": name,
            "type": type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_collaboration_analysis_templates(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_analysis_templates_output.ListCollaborationAnalysisTemplatesOutput":
        """<p>Lists analysis templates within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_analysis_templates_input.ListCollaborationAnalysisTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_analysis_templates_output.ListCollaborationAnalysisTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_analysis_templates

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_analysis_templates.async_list_collaboration_analysis_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_collaboration_analysis_templates_input.ListCollaborationAnalysisTemplatesInput = {
            "collaboration_identifier": collaboration_identifier
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

    async def list_collaboration_change_requests(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.change_request_status.ChangeRequestStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_change_requests_output.ListCollaborationChangeRequestsOutput":
        """<p>Lists all change requests for a collaboration with pagination support. Returns change requests sorted by creation time.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration that the change request is made against.</p>
            status: <p>A filter to only return change requests with the specified status.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_change_requests_input.ListCollaborationChangeRequestsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_change_requests_output.ListCollaborationChangeRequestsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_change_requests

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_change_requests.async_list_collaboration_change_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_collaboration_change_requests_input.ListCollaborationChangeRequestsInput = {
            "collaboration_identifier": collaboration_identifier
        }
        if status is not None:
            input_["status"] = status
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

    async def iter_list_collaboration_change_requests(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.change_request_status.ChangeRequestStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.collaboration_change_request_summary.CollaborationChangeRequestSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_change_requests(
                collaboration_identifier,
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("collaboration_change_request_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_configured_audience_model_associations(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_output.ListCollaborationConfiguredAudienceModelAssociationsOutput":
        """<p>Lists configured audience model associations within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_input.ListCollaborationConfiguredAudienceModelAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_output.ListCollaborationConfiguredAudienceModelAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_configured_audience_model_associations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_configured_audience_model_associations.async_list_collaboration_configured_audience_model_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_collaboration_configured_audience_model_associations_input.ListCollaborationConfiguredAudienceModelAssociationsInput = {
            "collaboration_identifier": collaboration_identifier
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

    async def iter_list_collaboration_configured_audience_model_associations(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.collaboration_configured_audience_model_association_summary.CollaborationConfiguredAudienceModelAssociationSummary]":
        _token = next_token
        while True:
            _response = (
                await self.list_collaboration_configured_audience_model_associations(
                    collaboration_identifier,
                    config_overrides=config_overrides,
                    next_token=_token,
                    max_results=max_results,
                )
            )
            _page = _resolve_path(
                _response,
                ("collaboration_configured_audience_model_association_summaries",),
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_id_namespace_associations(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_id_namespace_associations_output.ListCollaborationIdNamespaceAssociationsOutput":
        """<p>Returns a list of the ID namespace associations in a collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the ID namespace associations that you want to retrieve.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.&gt;</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_id_namespace_associations_input.ListCollaborationIdNamespaceAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_id_namespace_associations_output.ListCollaborationIdNamespaceAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_id_namespace_associations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_id_namespace_associations.async_list_collaboration_id_namespace_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_collaboration_id_namespace_associations_input.ListCollaborationIdNamespaceAssociationsInput = {
            "collaboration_identifier": collaboration_identifier
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

    async def iter_list_collaboration_id_namespace_associations(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.collaboration_id_namespace_association_summary.CollaborationIdNamespaceAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_id_namespace_associations(
                collaboration_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("collaboration_id_namespace_association_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_privacy_budgets(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        access_budget_resource_arn: Optional[
            "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_privacy_budgets_output.ListCollaborationPrivacyBudgetsOutput":
        """<p>Returns an array that summarizes each privacy budget in a specified collaboration. The summary includes the collaboration ARN, creation time, creating account, and privacy budget details.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            privacy_budget_type: <p>Specifies the type of the privacy budget.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            access_budget_resource_arn: <p>The Amazon Resource Name (ARN) of the Configured Table Association (ConfiguredTableAssociation) used to filter privacy budgets.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_privacy_budgets_input.ListCollaborationPrivacyBudgetsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_privacy_budgets_output.ListCollaborationPrivacyBudgetsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budgets

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budgets.async_list_collaboration_privacy_budgets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_collaboration_privacy_budgets_input.ListCollaborationPrivacyBudgetsInput = {
            "collaboration_identifier": collaboration_identifier,
            "privacy_budget_type": privacy_budget_type,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if access_budget_resource_arn is not None:
            input_["access_budget_resource_arn"] = access_budget_resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_collaboration_privacy_budgets(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        access_budget_resource_arn: Optional[
            "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.collaboration_privacy_budget_summary.CollaborationPrivacyBudgetSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_privacy_budgets(
                collaboration_identifier,
                privacy_budget_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                access_budget_resource_arn=access_budget_resource_arn,
            )
            _page = _resolve_path(
                _response, ("collaboration_privacy_budget_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_privacy_budget_templates(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_collaboration_privacy_budget_templates_output.ListCollaborationPrivacyBudgetTemplatesOutput":
        """<p>Returns an array that summarizes each privacy budget template in a specified collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for one of your collaborations.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_collaboration_privacy_budget_templates_input.ListCollaborationPrivacyBudgetTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_collaboration_privacy_budget_templates_output.ListCollaborationPrivacyBudgetTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budget_templates

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_collaboration_privacy_budget_templates.async_list_collaboration_privacy_budget_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_collaboration_privacy_budget_templates_input.ListCollaborationPrivacyBudgetTemplatesInput = {
            "collaboration_identifier": collaboration_identifier
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

    async def iter_list_collaboration_privacy_budget_templates(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.collaboration_privacy_budget_template_summary.CollaborationPrivacyBudgetTemplateSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_privacy_budget_templates(
                collaboration_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("collaboration_privacy_budget_template_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_members(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_members_output.ListMembersOutput":
        """<p>Lists all members within a collaboration.</p>

        Args:
            collaboration_identifier: <p>The identifier of the collaboration in which the members are listed.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_members_input.ListMembersInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_members_output.ListMembersOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_members

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_members.async_list_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_members_input.ListMembersInput = {
            "collaboration_identifier": collaboration_identifier
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

    async def list_schemas(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        schema_type: Optional["capo_cleanrooms.types.schema_type.SchemaType"] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_schemas_output.ListSchemasOutput":
        """<p>Lists the schemas for relations within a collaboration.</p>

        Args:
            collaboration_identifier: <p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>
            schema_type: <p>If present, filter schemas by schema type.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_schemas_input.ListSchemasInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_schemas_output.ListSchemasOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_schemas

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_schemas.async_list_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_schemas_input.ListSchemasInput = {
            "collaboration_identifier": collaboration_identifier
        }
        if schema_type is not None:
            input_["schema_type"] = schema_type
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

    async def update_collaboration_change_request(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        change_request_identifier: "capo_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier",
        action: "capo_cleanrooms.types.change_request_action.ChangeRequestAction",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_collaboration_change_request_output.UpdateCollaborationChangeRequestOutput":
        """<p>Updates an existing collaboration change request. This operation allows approval actions for pending change requests in collaborations (APPROVE, DENY, CANCEL, COMMIT).</p> <p>For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.</p>

        Args:
            collaboration_identifier: <p>The unique identifier of the collaboration that contains the change request to be updated.</p>
            change_request_identifier: <p>The unique identifier of the specific change request to be updated within the collaboration.</p>
            action: <p>The action to perform on the change request. Valid values include APPROVE (approve the change), DENY (reject the change), CANCEL (cancel the request), and COMMIT (commit after the request is approved).</p> <p>For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_collaboration_change_request_input.UpdateCollaborationChangeRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_collaboration_change_request_output.UpdateCollaborationChangeRequestOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration_change_request

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_collaboration_change_request.async_update_collaboration_change_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_collaboration_change_request_input.UpdateCollaborationChangeRequestInput = {
            "collaboration_identifier": collaboration_identifier,
            "change_request_identifier": change_request_identifier,
            "action": action,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configured_audience_model_association(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_audience_model_arn: "capo_cleanrooms.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        configured_audience_model_association_name: "capo_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName",
        manage_resource_policies: bool,
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanrooms.types.create_configured_audience_model_association_output.CreateConfiguredAudienceModelAssociationOutput":
        """<p>Provides the details necessary to create a configured audience model association.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The configured audience model is associated to the collaboration that this membership belongs to. Accepts a membership ID.</p>
            configured_audience_model_arn: <p>A unique identifier for the configured audience model that you want to associate.</p>
            configured_audience_model_association_name: <p>The name of the configured audience model association.</p>
            manage_resource_policies: <p>When <code>TRUE</code>, indicates that the resource policy for the configured audience model resource being associated is configured for Clean Rooms to manage permissions related to the given collaboration. When <code>FALSE</code>, indicates that the configured audience model resource owner will manage permissions related to the given collaboration.</p> <p>Setting this to <code>TRUE</code> requires you to have permissions to create, update, and delete the resource policy for the <code>cleanrooms-ml</code> resource when you call the <a>DeleteConfiguredAudienceModelAssociation</a> resource. In addition, if you are the collaboration creator and specify <code>TRUE</code>, you must have the same permissions when you call the <a>DeleteMember</a> and <a>DeleteCollaboration</a> APIs.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            description: <p>A description of the configured audience model association.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_configured_audience_model_association_input.CreateConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_configured_audience_model_association_output.CreateConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_audience_model_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_audience_model_association.async_create_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_configured_audience_model_association_input.CreateConfiguredAudienceModelAssociationInput = {
            "membership_identifier": membership_identifier,
            "configured_audience_model_arn": configured_audience_model_arn,
            "configured_audience_model_association_name": configured_audience_model_association_name,
            "manage_resource_policies": manage_resource_policies,
        }
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configured_audience_model_association(
        self,
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_audience_model_association_output.GetConfiguredAudienceModelAssociationOutput":
        """<p>Returns information about a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to retrieve.</p>
            membership_identifier: <p>A unique identifier for the membership that contains the configured audience model association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_configured_audience_model_association_input.GetConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_configured_audience_model_association_output.GetConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_audience_model_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_audience_model_association.async_get_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_configured_audience_model_association_input.GetConfiguredAudienceModelAssociationInput = {
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configured_audience_model_association(
        self,
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        name: Optional[
            "capo_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName"
        ] = None,
    ) -> "capo_cleanrooms.types.update_configured_audience_model_association_output.UpdateConfiguredAudienceModelAssociationOutput":
        """<p>Provides the details necessary to update a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to update.</p>
            membership_identifier: <p>A unique identifier of the membership that contains the configured audience model association that you want to update.</p>
            description: <p>A new description for the configured audience model association.</p>
            name: <p>A new name for the configured audience model association.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_configured_audience_model_association_input.UpdateConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_configured_audience_model_association_output.UpdateConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_audience_model_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_audience_model_association.async_update_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_configured_audience_model_association_input.UpdateConfiguredAudienceModelAssociationInput = {
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configured_audience_model_association(
        self,
        configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_audience_model_association_output.DeleteConfiguredAudienceModelAssociationOutput":
        """<p>Provides the information necessary to delete a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier of the configured audience model association that you want to delete.</p>
            membership_identifier: <p>A unique identifier of the membership that contains the audience model association that you want to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_configured_audience_model_association_input.DeleteConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_configured_audience_model_association_output.DeleteConfiguredAudienceModelAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_audience_model_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_audience_model_association.async_delete_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_configured_audience_model_association_input.DeleteConfiguredAudienceModelAssociationInput = {
            "configured_audience_model_association_identifier": configured_audience_model_association_identifier,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configured_audience_model_associations(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_configured_audience_model_associations_output.ListConfiguredAudienceModelAssociationsOutput":
        """<p>Lists information about requested configured audience model associations.</p>

        Args:
            membership_identifier: <p>A unique identifier for a membership that contains the configured audience model associations that you want to retrieve.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_configured_audience_model_associations_input.ListConfiguredAudienceModelAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_configured_audience_model_associations_output.ListConfiguredAudienceModelAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_audience_model_associations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_audience_model_associations.async_list_configured_audience_model_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_configured_audience_model_associations_input.ListConfiguredAudienceModelAssociationsInput = {
            "membership_identifier": membership_identifier
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

    async def iter_list_configured_audience_model_associations(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.configured_audience_model_association_summary.ConfiguredAudienceModelAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_configured_audience_model_associations(
                membership_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("configured_audience_model_association_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_configured_table_association(
        self,
        name: "capo_cleanrooms.types.table_alias.TableAlias",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        role_arn: "capo_cleanrooms.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_association_output.CreateConfiguredTableAssociationOutput":
        """<p>Creates a configured table association. A configured table association links a configured table with a collaboration.</p>

        Args:
            name: <p>The name of the configured table association. This name is used to query the underlying configured table.</p>
            description: <p>A description for the configured table association.</p>
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The configured table is associated to the collaboration that this membership belongs to. Currently accepts a membership ID.</p>
            configured_table_identifier: <p>A unique identifier for the configured table to be associated to. Currently accepts a configured table ID.</p>
            role_arn: <p>The service will assume this role to access catalog metadata and query the table.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_configured_table_association_input.CreateConfiguredTableAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_configured_table_association_output.CreateConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association.async_create_configured_table_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_configured_table_association_input.CreateConfiguredTableAssociationInput = {
            "name": name,
            "membership_identifier": membership_identifier,
            "configured_table_identifier": configured_table_identifier,
            "role_arn": role_arn,
        }
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

    async def get_configured_table_association(
        self,
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_association_output.GetConfiguredTableAssociationOutput":
        """<p>Retrieves a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique ID for the configured table association to retrieve. Currently accepts the configured table ID.</p>
            membership_identifier: <p>A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_configured_table_association_input.GetConfiguredTableAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_configured_table_association_output.GetConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association.async_get_configured_table_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_configured_table_association_input.GetConfiguredTableAssociationInput = {
            "configured_table_association_identifier": configured_table_association_identifier,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configured_table_association(
        self,
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        role_arn: Optional["capo_cleanrooms.types.role_arn.RoleArn"] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_association_output.UpdateConfiguredTableAssociationOutput":
        """<p>Updates a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique identifier for the configured table association to update. Currently accepts the configured table association ID.</p>
            membership_identifier: <p>The unique ID for the membership that the configured table association belongs to.</p>
            description: <p>A new description for the configured table association.</p>
            role_arn: <p>The service will assume this role to access catalog metadata and query the table.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_configured_table_association_input.UpdateConfiguredTableAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_configured_table_association_output.UpdateConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association.async_update_configured_table_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_configured_table_association_input.UpdateConfiguredTableAssociationInput = {
            "configured_table_association_identifier": configured_table_association_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configured_table_association(
        self,
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_association_output.DeleteConfiguredTableAssociationOutput":
        """<p>Deletes a configured table association.</p>

        Args:
            configured_table_association_identifier: <p>The unique ID for the configured table association to be deleted. Currently accepts the configured table ID.</p>
            membership_identifier: <p>A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_configured_table_association_input.DeleteConfiguredTableAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_configured_table_association_output.DeleteConfiguredTableAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association.async_delete_configured_table_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_configured_table_association_input.DeleteConfiguredTableAssociationInput = {
            "configured_table_association_identifier": configured_table_association_identifier,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configured_table_associations(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_configured_table_associations_output.ListConfiguredTableAssociationsOutput":
        """<p>Lists configured table associations for a membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership to list configured table associations for. Currently accepts the membership ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_configured_table_associations_input.ListConfiguredTableAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_configured_table_associations_output.ListConfiguredTableAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_table_associations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_table_associations.async_list_configured_table_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_configured_table_associations_input.ListConfiguredTableAssociationsInput = {
            "membership_identifier": membership_identifier
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

    async def create_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_association_analysis_rule_output.CreateConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Creates a new analysis rule for an associated configured table.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The unique ID for the configured table association. Currently accepts the configured table association ID.</p>
            analysis_rule_type: <p> The type of analysis rule.</p>
            analysis_rule_policy: <p>The analysis rule policy that was created for the configured table association.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_configured_table_association_analysis_rule_input.CreateConfiguredTableAssociationAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_configured_table_association_analysis_rule_output.CreateConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_association_analysis_rule.async_create_configured_table_association_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_configured_table_association_analysis_rule_input.CreateConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
            "analysis_rule_type": analysis_rule_type,
            "analysis_rule_policy": analysis_rule_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_association_analysis_rule_output.DeleteConfiguredTableAssociationAnalysisRuleOutput":
        """<p>Deletes an analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p>The identiﬁer for the conﬁgured table association that's related to the analysis rule that you want to delete.</p>
            analysis_rule_type: <p>The type of the analysis rule that you want to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_configured_table_association_analysis_rule_input.DeleteConfiguredTableAssociationAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_configured_table_association_analysis_rule_output.DeleteConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_association_analysis_rule.async_delete_configured_table_association_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_configured_table_association_analysis_rule_input.DeleteConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_association_analysis_rule_output.GetConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Retrieves the analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The identiﬁer for the conﬁgured table association that's related to the analysis rule.</p>
            analysis_rule_type: <p> The type of analysis rule that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_configured_table_association_analysis_rule_input.GetConfiguredTableAssociationAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_configured_table_association_analysis_rule_output.GetConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_association_analysis_rule.async_get_configured_table_association_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_configured_table_association_analysis_rule_input.GetConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configured_table_association_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_association_analysis_rule_output.UpdateConfiguredTableAssociationAnalysisRuleOutput":
        """<p> Updates the analysis rule for a configured table association.</p>

        Args:
            membership_identifier: <p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>
            configured_table_association_identifier: <p> The identifier for the configured table association to update.</p>
            analysis_rule_type: <p> The analysis rule type that you want to update.</p>
            analysis_rule_policy: <p> The updated analysis rule policy for the conﬁgured table association.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_configured_table_association_analysis_rule_input.UpdateConfiguredTableAssociationAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_configured_table_association_analysis_rule_output.UpdateConfiguredTableAssociationAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_association_analysis_rule.async_update_configured_table_association_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_configured_table_association_analysis_rule_input.UpdateConfiguredTableAssociationAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "configured_table_association_identifier": configured_table_association_identifier,
            "analysis_rule_type": analysis_rule_type,
            "analysis_rule_policy": analysis_rule_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configured_table(
        self,
        name: "capo_cleanrooms.types.display_name.DisplayName",
        table_reference: "capo_cleanrooms.types.table_reference.TableReference",
        allowed_columns: "capo_cleanrooms.types.allowed_column_list.AllowedColumnList",
        analysis_method: "capo_cleanrooms.types.analysis_method.AnalysisMethod",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        selected_analysis_methods: Optional[
            "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_output.CreateConfiguredTableOutput":
        """<p>Creates a new configured table resource.</p>

        Args:
            name: <p>The name of the configured table.</p>
            description: <p>A description for the configured table.</p>
            table_reference: <p>A reference to the table being configured.</p>
            allowed_columns: <p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>
            analysis_method: <p>The analysis method allowed for the configured tables.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>
            selected_analysis_methods: <p> The analysis methods to enable for the configured table. When configured, you must specify at least two analysis methods.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_configured_table_input.CreateConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_configured_table_output.CreateConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table.async_create_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_configured_table_input.CreateConfiguredTableInput = {
            "name": name,
            "table_reference": table_reference,
            "allowed_columns": allowed_columns,
            "analysis_method": analysis_method,
        }
        if description is not None:
            input_["description"] = description
        if selected_analysis_methods is not None:
            input_["selected_analysis_methods"] = selected_analysis_methods
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configured_table(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_output.GetConfiguredTableOutput":
        """<p>Retrieves a configured table.</p>

        Args:
            configured_table_identifier: <p>The unique ID for the configured table to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_configured_table_input.GetConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_configured_table_output.GetConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table.async_get_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_configured_table_input.GetConfiguredTableInput = {
            "configured_table_identifier": configured_table_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configured_table(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        name: Optional["capo_cleanrooms.types.display_name.DisplayName"] = None,
        description: Optional[
            "capo_cleanrooms.types.table_description.TableDescription"
        ] = None,
        table_reference: Optional[
            "capo_cleanrooms.types.table_reference.TableReference"
        ] = None,
        allowed_columns: Optional[
            "capo_cleanrooms.types.allowed_column_list.AllowedColumnList"
        ] = None,
        analysis_method: Optional[
            "capo_cleanrooms.types.analysis_method.AnalysisMethod"
        ] = None,
        selected_analysis_methods: Optional[
            "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
        ] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_output.UpdateConfiguredTableOutput":
        """<p>Updates a configured table.</p>

        Args:
            configured_table_identifier: <p>The identifier for the configured table to update. Currently accepts the configured table ID.</p>
            name: <p>A new name for the configured table.</p>
            description: <p>A new description for the configured table.</p>
            allowed_columns: <p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>
            analysis_method: <p> The analysis method for the configured table.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>
            selected_analysis_methods: <p> The selected analysis methods for the table configuration update.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_configured_table_input.UpdateConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_configured_table_output.UpdateConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table.async_update_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_configured_table_input.UpdateConfiguredTableInput = {
            "configured_table_identifier": configured_table_identifier
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if table_reference is not None:
            input_["table_reference"] = table_reference
        if allowed_columns is not None:
            input_["allowed_columns"] = allowed_columns
        if analysis_method is not None:
            input_["analysis_method"] = analysis_method
        if selected_analysis_methods is not None:
            input_["selected_analysis_methods"] = selected_analysis_methods

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configured_table(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_output.DeleteConfiguredTableOutput":
        """<p>Deletes a configured table.</p>

        Args:
            configured_table_identifier: <p>The unique ID for the configured table to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_configured_table_input.DeleteConfiguredTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_configured_table_output.DeleteConfiguredTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table.async_delete_configured_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_configured_table_input.DeleteConfiguredTableInput = {
            "configured_table_identifier": configured_table_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configured_tables(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_cleanrooms.types.list_configured_tables_output.ListConfiguredTablesOutput"
    ):
        """<p>Lists configured tables.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_configured_tables_input.ListConfiguredTablesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_configured_tables_output.ListConfiguredTablesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_tables

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_tables.async_list_configured_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_configured_tables_input.ListConfiguredTablesInput = {}
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

    async def create_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_configured_table_analysis_rule_output.CreateConfiguredTableAnalysisRuleOutput":
        """<p>Creates a new analysis rule for a configured table. Currently, only one analysis rule can be created for a given configured table.</p>

        Args:
            configured_table_identifier: <p>The identifier for the configured table to create the analysis rule for. Currently accepts the configured table ID. </p>
            analysis_rule_type: <p>The type of analysis rule.</p>
            analysis_rule_policy: <p>The analysis rule policy that was created for the configured table.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_configured_table_analysis_rule_input.CreateConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_configured_table_analysis_rule_output.CreateConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_table_analysis_rule.async_create_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_configured_table_analysis_rule_input.CreateConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
            "analysis_rule_policy": analysis_rule_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_configured_table_analysis_rule_output.DeleteConfiguredTableAnalysisRuleOutput":
        """<p>Deletes a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule type to be deleted. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_configured_table_analysis_rule_input.DeleteConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_configured_table_analysis_rule_output.DeleteConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_table_analysis_rule.async_delete_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_configured_table_analysis_rule_input.DeleteConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_configured_table_analysis_rule_output.GetConfiguredTableAnalysisRuleOutput":
        """<p>Retrieves a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table to retrieve. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule to be retrieved. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_configured_table_analysis_rule_input.GetConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_configured_table_analysis_rule_output.GetConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_table_analysis_rule.async_get_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_configured_table_analysis_rule_input.GetConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configured_table_analysis_rule(
        self,
        configured_table_identifier: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_configured_table_analysis_rule_output.UpdateConfiguredTableAnalysisRuleOutput":
        """<p>Updates a configured table analysis rule.</p>

        Args:
            configured_table_identifier: <p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>
            analysis_rule_type: <p>The analysis rule type to be updated. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>
            analysis_rule_policy: <p>The new analysis rule policy for the configured table analysis rule.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_configured_table_analysis_rule_input.UpdateConfiguredTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_configured_table_analysis_rule_output.UpdateConfiguredTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_table_analysis_rule.async_update_configured_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_configured_table_analysis_rule_input.UpdateConfiguredTableAnalysisRuleInput = {
            "configured_table_identifier": configured_table_identifier,
            "analysis_rule_type": analysis_rule_type,
            "analysis_rule_policy": analysis_rule_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_id_mapping_table(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        name: "capo_cleanrooms.types.resource_alias.ResourceAlias",
        input_reference_config: "capo_cleanrooms.types.id_mapping_table_input_reference_config.IdMappingTableInputReferenceConfig",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
    ) -> "capo_cleanrooms.types.create_id_mapping_table_output.CreateIdMappingTableOutput":
        """<p>Creates an ID mapping table.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table.</p>
            name: <p>A name for the ID mapping table.</p>
            description: <p>A description of the ID mapping table.</p>
            input_reference_config: <p>The input reference configuration needed to create the ID mapping table.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key. This value is used to encrypt the mapping table data that is stored by Clean Rooms.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_id_mapping_table_input.CreateIdMappingTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_id_mapping_table_output.CreateIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_mapping_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_mapping_table.async_create_id_mapping_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_id_mapping_table_input.CreateIdMappingTableInput = {
            "membership_identifier": membership_identifier,
            "name": name,
            "input_reference_config": input_reference_config,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_id_mapping_table(
        self,
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_id_mapping_table_output.GetIdMappingTableOutput":
        """<p>Retrieves an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table identifier that you want to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_id_mapping_table_input.GetIdMappingTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_id_mapping_table_output.GetIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_mapping_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_mapping_table.async_get_id_mapping_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_id_mapping_table_input.GetIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_id_mapping_table(
        self,
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
    ) -> "capo_cleanrooms.types.update_id_mapping_table_output.UpdateIdMappingTableOutput":
        """<p>Provides the details that are necessary to update an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to update.</p>
            description: <p>A new description for the ID mapping table.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_id_mapping_table_input.UpdateIdMappingTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_id_mapping_table_output.UpdateIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_mapping_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_mapping_table.async_update_id_mapping_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_id_mapping_table_input.UpdateIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_id_mapping_table(
        self,
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_id_mapping_table_output.DeleteIdMappingTableOutput":
        """<p>Deletes an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to delete.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_id_mapping_table_input.DeleteIdMappingTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_id_mapping_table_output.DeleteIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_mapping_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_mapping_table.async_delete_id_mapping_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_id_mapping_table_input.DeleteIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_id_mapping_tables(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_cleanrooms.types.list_id_mapping_tables_output.ListIdMappingTablesOutput"
    ):
        """<p>Returns a list of ID mapping tables.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping tables that you want to view.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_id_mapping_tables_input.ListIdMappingTablesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_id_mapping_tables_output.ListIdMappingTablesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_mapping_tables

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_mapping_tables.async_list_id_mapping_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_id_mapping_tables_input.ListIdMappingTablesInput = {
            "membership_identifier": membership_identifier
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

    async def iter_list_id_mapping_tables(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.id_mapping_table_summary.IdMappingTableSummary]":
        _token = next_token
        while True:
            _response = await self.list_id_mapping_tables(
                membership_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("id_mapping_table_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def populate_id_mapping_table(
        self,
        id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        job_type: Optional["capo_cleanrooms.types.job_type.JobType"] = None,
    ) -> "capo_cleanrooms.types.populate_id_mapping_table_output.PopulateIdMappingTableOutput":
        """<p>Defines the information that's necessary to populate an ID mapping table.</p>

        Args:
            id_mapping_table_identifier: <p>The unique identifier of the ID mapping table that you want to populate.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID mapping table that you want to populate.</p>
            job_type: <p>The job type of the rule-based ID mapping job. Valid values include:</p> <p> <code>INCREMENTAL</code>: Processes only new or changed data since the last job run. This is the default job type if the ID mapping workflow was created in Entity Resolution with <code>incrementalRunConfig</code> specified.</p> <p> <code>BATCH</code>: Processes all data from the input source, regardless of previous job runs. This is the default job type if the ID mapping workflow was created in Entity Resolution but <code>incrementalRunConfig</code> wasn't specified.</p> <p> <code>DELETE_ONLY</code>: Processes only deletion requests from <code>BatchDeleteUniqueId</code>, which is set in Entity Resolution.</p> <p>For more information about <code>incrementalRunConfig</code> and <code>BatchDeleteUniqueId</code>, see the <a href="https://docs.aws.amazon.com/entityresolution/latest/apireference/Welcome.html">Entity Resolution API Reference</a>.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.populate_id_mapping_table_input.PopulateIdMappingTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.populate_id_mapping_table_output.PopulateIdMappingTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_id_mapping_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_id_mapping_table.async_populate_id_mapping_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.populate_id_mapping_table_input.PopulateIdMappingTableInput = {
            "id_mapping_table_identifier": id_mapping_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if job_type is not None:
            input_["job_type"] = job_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_id_namespace_association(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        input_reference_config: "capo_cleanrooms.types.id_namespace_association_input_reference_config.IdNamespaceAssociationInputReferenceConfig",
        name: "capo_cleanrooms.types.generic_resource_name.GenericResourceName",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        id_mapping_config: Optional[
            "capo_cleanrooms.types.id_mapping_config.IdMappingConfig"
        ] = None,
    ) -> "capo_cleanrooms.types.create_id_namespace_association_output.CreateIdNamespaceAssociationOutput":
        """<p>Creates an ID namespace association.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association.</p>
            input_reference_config: <p>The input reference configuration needed to create the ID namespace association.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            name: <p>The name for the ID namespace association.</p>
            description: <p>The description of the ID namespace association.</p>
            id_mapping_config: <p>The configuration settings for the ID mapping table.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_id_namespace_association_input.CreateIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_id_namespace_association_output.CreateIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_namespace_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_namespace_association.async_create_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_id_namespace_association_input.CreateIdNamespaceAssociationInput = {
            "membership_identifier": membership_identifier,
            "input_reference_config": input_reference_config,
            "name": name,
        }
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description
        if id_mapping_config is not None:
            input_["id_mapping_config"] = id_mapping_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_id_namespace_association(
        self,
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_id_namespace_association_output.GetIdNamespaceAssociationOutput":
        """<p>Retrieves an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_id_namespace_association_input.GetIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_id_namespace_association_output.GetIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_namespace_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_namespace_association.async_get_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_id_namespace_association_input.GetIdNamespaceAssociationInput = {
            "id_namespace_association_identifier": id_namespace_association_identifier,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_id_namespace_association(
        self,
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        name: Optional[
            "capo_cleanrooms.types.generic_resource_name.GenericResourceName"
        ] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        id_mapping_config: Optional[
            "capo_cleanrooms.types.id_mapping_config.IdMappingConfig"
        ] = None,
    ) -> "capo_cleanrooms.types.update_id_namespace_association_output.UpdateIdNamespaceAssociationOutput":
        """<p>Provides the details that are necessary to update an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to update.</p>
            name: <p>A new name for the ID namespace association.</p>
            description: <p>A new description for the ID namespace association.</p>
            id_mapping_config: <p>The configuration settings for the ID mapping table.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_id_namespace_association_input.UpdateIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_id_namespace_association_output.UpdateIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_namespace_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_namespace_association.async_update_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_id_namespace_association_input.UpdateIdNamespaceAssociationInput = {
            "id_namespace_association_identifier": id_namespace_association_identifier,
            "membership_identifier": membership_identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if id_mapping_config is not None:
            input_["id_mapping_config"] = id_mapping_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_id_namespace_association(
        self,
        id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_id_namespace_association_output.DeleteIdNamespaceAssociationOutput":
        """<p>Deletes an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to delete.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_id_namespace_association_input.DeleteIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_id_namespace_association_output.DeleteIdNamespaceAssociationOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_namespace_association

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_namespace_association.async_delete_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_id_namespace_association_input.DeleteIdNamespaceAssociationInput = {
            "id_namespace_association_identifier": id_namespace_association_identifier,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_id_namespace_associations(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_id_namespace_associations_output.ListIdNamespaceAssociationsOutput":
        """<p>Returns a list of ID namespace associations.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to view.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_id_namespace_associations_input.ListIdNamespaceAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_id_namespace_associations_output.ListIdNamespaceAssociationsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_namespace_associations

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_namespace_associations.async_list_id_namespace_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_id_namespace_associations_input.ListIdNamespaceAssociationsInput = {
            "membership_identifier": membership_identifier
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

    async def iter_list_id_namespace_associations(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.id_namespace_association_summary.IdNamespaceAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_id_namespace_associations(
                membership_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("id_namespace_association_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_intermediate_table(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        name: "capo_cleanrooms.types.display_name.DisplayName",
        population_analysis_configuration: "capo_cleanrooms.types.population_analysis_configuration.PopulationAnalysisConfiguration",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
        retention_in_days: Optional[int] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_intermediate_table_output.CreateIntermediateTableOutput":
        """<p>Creates an intermediate table in a membership. The intermediate table is owned by the member with the CAN_QUERY ability. To populate the table with results, use <code>PopulateIntermediateTable</code>.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership where the intermediate table is created.</p>
            name: <p>The display name for the intermediate table.</p>
            description: <p>A description of the intermediate table.</p>
            population_analysis_configuration: <p>The configuration that defines the analysis used to populate the intermediate table.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer-managed KMS key used to encrypt the intermediate table data.</p>
            retention_in_days: <p>The number of days to retain populated data versions.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_intermediate_table_input.CreateIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_intermediate_table_output.CreateIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table.async_create_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_intermediate_table_input.CreateIntermediateTableInput = {
            "membership_identifier": membership_identifier,
            "name": name,
            "population_analysis_configuration": population_analysis_configuration,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if retention_in_days is not None:
            input_["retention_in_days"] = retention_in_days
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_intermediate_table(
        self,
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> (
        "capo_cleanrooms.types.get_intermediate_table_output.GetIntermediateTableOutput"
    ):
        """<p>Retrieves an intermediate table. Returns the full details of the intermediate table, including schema, table dependencies, inherited constraints, child resources, and status. Only the intermediate table owner can call this operation.</p>

        Args:
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_intermediate_table_input.GetIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_intermediate_table_output.GetIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table.async_get_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_intermediate_table_input.GetIntermediateTableInput = {
            "intermediate_table_identifier": intermediate_table_identifier,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_intermediate_table(
        self,
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "capo_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"] = None,
        columns: Optional[
            "capo_cleanrooms.types.intermediate_table_column_list.IntermediateTableColumnList"
        ] = None,
    ) -> "capo_cleanrooms.types.update_intermediate_table_output.UpdateIntermediateTableOutput":
        """<p>Updates an intermediate table. You can update the description, KMS key ARN, and column types of existing columns. Only the intermediate table owner can call this operation.</p>

        Args:
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            description: <p>A new description for the intermediate table.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer-managed KMS key to use for encrypting future population data.</p>
            columns: <p>The list of columns with updated type definitions. Only the type of existing columns can be updated.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_intermediate_table_input.UpdateIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_intermediate_table_output.UpdateIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table.async_update_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_intermediate_table_input.UpdateIntermediateTableInput = {
            "intermediate_table_identifier": intermediate_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if columns is not None:
            input_["columns"] = columns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_intermediate_table(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_intermediate_table_output.DeleteIntermediateTableOutput":
        """<p>Deletes an intermediate table. The delete is idempotent. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to delete.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_intermediate_table_input.DeleteIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_intermediate_table_output.DeleteIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table.async_delete_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_intermediate_table_input.DeleteIntermediateTableInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_intermediate_tables(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_intermediate_tables_output.ListIntermediateTablesOutput":
        """<p>Lists intermediate tables owned by the caller in a membership. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership for which to list intermediate tables.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_intermediate_tables_input.ListIntermediateTablesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_intermediate_tables_output.ListIntermediateTablesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_tables

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_tables.async_list_intermediate_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_intermediate_tables_input.ListIntermediateTablesInput = {
            "membership_identifier": membership_identifier
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

    async def iter_list_intermediate_tables(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.intermediate_table_summary.IntermediateTableSummary]":
        _token = next_token
        while True:
            _response = await self.list_intermediate_tables(
                membership_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("intermediate_table_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.intermediate_table_analysis_rule_policy.IntermediateTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.create_intermediate_table_analysis_rule_output.CreateIntermediateTableAnalysisRuleOutput":
        """<p>Creates an analysis rule for an intermediate table. Only the CUSTOM analysis rule type is supported. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to create the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to create. Currently, only <code>CUSTOM</code> is supported.</p>
            analysis_rule_policy: <p>The analysis rule policy to apply to the intermediate table.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_intermediate_table_analysis_rule_input.CreateIntermediateTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_intermediate_table_analysis_rule_output.CreateIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_intermediate_table_analysis_rule.async_create_intermediate_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_intermediate_table_analysis_rule_input.CreateIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
            "analysis_rule_type": analysis_rule_type,
            "analysis_rule_policy": analysis_rule_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_intermediate_table_analysis_rule_output.DeleteIntermediateTableAnalysisRuleOutput":
        """<p>Deletes an analysis rule from an intermediate table. After the analysis rule is deleted, the intermediate table becomes unqueryable until a new analysis rule is attached. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table from which to delete the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to delete. Currently, only <code>CUSTOM</code> is supported.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_intermediate_table_analysis_rule_input.DeleteIntermediateTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_intermediate_table_analysis_rule_output.DeleteIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_intermediate_table_analysis_rule.async_delete_intermediate_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_intermediate_table_analysis_rule_input.DeleteIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_intermediate_table_analysis_rule_output.GetIntermediateTableAnalysisRuleOutput":
        """<p>Retrieves the analysis rule for an intermediate table.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to retrieve the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to retrieve. Currently, only <code>CUSTOM</code> is supported.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_intermediate_table_analysis_rule_input.GetIntermediateTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_intermediate_table_analysis_rule_output.GetIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_intermediate_table_analysis_rule.async_get_intermediate_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_intermediate_table_analysis_rule_input.GetIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
            "analysis_rule_type": analysis_rule_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_intermediate_table_versions(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_intermediate_table_versions_output.ListIntermediateTableVersionsOutput":
        """<p>Lists the version history of an intermediate table. Each call to <code>PopulateIntermediateTable</code> creates a new version. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to list versions.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_intermediate_table_versions_input.ListIntermediateTableVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_intermediate_table_versions_output.ListIntermediateTableVersionsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_table_versions

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_intermediate_table_versions.async_list_intermediate_table_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_intermediate_table_versions_input.ListIntermediateTableVersionsInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
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

    async def iter_list_intermediate_table_versions(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.intermediate_table_version_summary.IntermediateTableVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_intermediate_table_versions(
                membership_identifier,
                intermediate_table_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("intermediate_table_version_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def populate_intermediate_table(
        self,
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        parameters: Optional["capo_cleanrooms.types.parameter_map.ParameterMap"] = None,
        compute_configuration: Optional[
            "capo_cleanrooms.types.intermediate_table_compute_configuration.IntermediateTableComputeConfiguration"
        ] = None,
        analysis_payer_account_id: Optional[
            "capo_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "capo_cleanrooms.types.populate_intermediate_table_output.PopulateIntermediateTableOutput":
        """<p>Runs the stored query of an intermediate table and makes the results available for querying. Each call creates a new version. Use <code>GetProtectedQuery</code> with the returned analysis ID to track progress. Only the intermediate table owner can call this operation.</p>

        Args:
            intermediate_table_identifier: <p>The unique identifier of the intermediate table to populate.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            parameters: <p>The runtime parameter values that override the defaults in the stored query.</p>
            compute_configuration: <p>The compute configuration for the population query execution.</p>
            analysis_payer_account_id: <p>The account ID of the member that pays for the analysis compute costs.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.populate_intermediate_table_input.PopulateIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.populate_intermediate_table_output.PopulateIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.populate_intermediate_table.async_populate_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.populate_intermediate_table_input.PopulateIntermediateTableInput = {
            "intermediate_table_identifier": intermediate_table_identifier,
            "membership_identifier": membership_identifier,
        }
        if parameters is not None:
            input_["parameters"] = parameters
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if analysis_payer_account_id is not None:
            input_["analysis_payer_account_id"] = analysis_payer_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_intermediate_table_analysis_rule(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier",
        analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
        analysis_rule_policy: "capo_cleanrooms.types.intermediate_table_analysis_rule_policy.IntermediateTableAnalysisRulePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_intermediate_table_analysis_rule_output.UpdateIntermediateTableAnalysisRuleOutput":
        """<p>Updates the analysis rule policy for an intermediate table. Only the intermediate table owner can call this operation.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table.</p>
            intermediate_table_identifier: <p>The unique identifier of the intermediate table for which to update the analysis rule.</p>
            analysis_rule_type: <p>The type of analysis rule to update. Currently, only <code>CUSTOM</code> is supported.</p>
            analysis_rule_policy: <p>The updated analysis rule policy for the intermediate table.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_intermediate_table_analysis_rule_input.UpdateIntermediateTableAnalysisRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_intermediate_table_analysis_rule_output.UpdateIntermediateTableAnalysisRuleOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table_analysis_rule

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_intermediate_table_analysis_rule.async_update_intermediate_table_analysis_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_intermediate_table_analysis_rule_input.UpdateIntermediateTableAnalysisRuleInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_identifier": intermediate_table_identifier,
            "analysis_rule_type": analysis_rule_type,
            "analysis_rule_policy": analysis_rule_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_membership(
        self,
        collaboration_identifier: "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier",
        query_log_status: "capo_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        job_log_status: Optional[
            "capo_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
        default_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
        ] = None,
        default_job_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
        ] = None,
        payment_configuration: Optional[
            "capo_cleanrooms.types.membership_payment_configuration.MembershipPaymentConfiguration"
        ] = None,
        is_metrics_enabled: Optional[bool] = None,
    ) -> "capo_cleanrooms.types.create_membership_output.CreateMembershipOutput":
        """<p>Creates a membership for a specific collaboration identifier and joins the collaboration.</p>

        Args:
            collaboration_identifier: <p>The unique ID for the associated collaboration.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            default_result_configuration: <p>The default protected query result configuration as specified by the member who can receive results.</p>
            default_job_result_configuration: <p>The default job result configuration that determines how job results are protected and managed within this membership. This configuration applies to all jobs.</p>
            payment_configuration: <p>The payment responsibilities accepted by the collaboration member.</p> <p>Not required if the collaboration member has the member ability to run queries. </p> <p>Required if the collaboration member doesn't have the member ability to run queries but is configured as a payer by the collaboration creator. </p>
            is_metrics_enabled: <p>An indicator as to whether Amazon CloudWatch metrics have been enabled or disabled for the membership.</p> <p>Amazon CloudWatch metrics are only available when the collaboration has metrics enabled. This option can be set by collaboration members who have the ability to run queries (analysis runners) or by members who are configured as payers.</p> <p>When <code>true</code>, metrics about query execution are collected in Amazon CloudWatch. The default value is <code>false</code>.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_membership_input.CreateMembershipInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_membership_output.CreateMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_membership

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_membership.async_create_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_membership_input.CreateMembershipInput = {
            "collaboration_identifier": collaboration_identifier,
            "query_log_status": query_log_status,
        }
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if tags is not None:
            input_["tags"] = tags
        if default_result_configuration is not None:
            input_["default_result_configuration"] = default_result_configuration
        if default_job_result_configuration is not None:
            input_["default_job_result_configuration"] = (
                default_job_result_configuration
            )
        if payment_configuration is not None:
            input_["payment_configuration"] = payment_configuration
        if is_metrics_enabled is not None:
            input_["is_metrics_enabled"] = is_metrics_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_membership(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_membership_output.GetMembershipOutput":
        """<p>Retrieves a specified membership for an identifier.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_membership_input.GetMembershipInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_membership_output.GetMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_membership

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_membership.async_get_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_membership_input.GetMembershipInput = {
            "membership_identifier": membership_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_membership(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        query_log_status: Optional[
            "capo_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus"
        ] = None,
        job_log_status: Optional[
            "capo_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
        ] = None,
        default_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
        ] = None,
        default_job_result_configuration: Optional[
            "capo_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
        ] = None,
        membership_payment_configuration: Optional[
            "capo_cleanrooms.types.update_membership_payment_configuration.UpdateMembershipPaymentConfiguration"
        ] = None,
    ) -> "capo_cleanrooms.types.update_membership_output.UpdateMembershipOutput":
        """<p>Updates a membership.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership.</p>
            query_log_status: <p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            job_log_status: <p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>
            default_result_configuration: <p>The default protected query result configuration as specified by the member who can receive results.</p>
            default_job_result_configuration: <p> The default job result configuration.</p>
            membership_payment_configuration: <p>The payment configuration to update for the membership.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_membership_input.UpdateMembershipInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_membership_output.UpdateMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_membership

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_membership.async_update_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_membership_input.UpdateMembershipInput = {
            "membership_identifier": membership_identifier
        }
        if query_log_status is not None:
            input_["query_log_status"] = query_log_status
        if job_log_status is not None:
            input_["job_log_status"] = job_log_status
        if default_result_configuration is not None:
            input_["default_result_configuration"] = default_result_configuration
        if default_job_result_configuration is not None:
            input_["default_job_result_configuration"] = (
                default_job_result_configuration
            )
        if membership_payment_configuration is not None:
            input_["membership_payment_configuration"] = (
                membership_payment_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_membership(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_membership_output.DeleteMembershipOutput":
        """<p>Deletes a specified membership. All resources under a membership must be deleted.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_membership_input.DeleteMembershipInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_membership_output.DeleteMembershipOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_membership

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_membership.async_delete_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_membership_input.DeleteMembershipInput = {
            "membership_identifier": membership_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_memberships(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        status: Optional[
            "capo_cleanrooms.types.membership_status.MembershipStatus"
        ] = None,
    ) -> "capo_cleanrooms.types.list_memberships_output.ListMembershipsOutput":
        """<p>Lists all memberships resources within the caller's account.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            status: <p>A filter which will return only memberships in the specified status.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_memberships_input.ListMembershipsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_memberships_output.ListMembershipsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_memberships

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_memberships.async_list_memberships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_memberships_input.ListMembershipsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disallow_intermediate_table(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        intermediate_table_name: "capo_cleanrooms.types.display_name.DisplayName",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        include_descendants: Optional[bool] = None,
    ) -> "capo_cleanrooms.types.disallow_intermediate_table_output.DisallowIntermediateTableOutput":
        """<p>Marks an intermediate table as invalid when it references the caller's base table. The data provider (base table owner) calls this operation, not the intermediate table owner. By default, the operation also marks all descendant intermediate tables as invalid.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the intermediate table to disallow.</p>
            intermediate_table_name: <p>The name of the intermediate table to disallow.</p>
            include_descendants: <p>Specifies whether to cascade the disallow action to descendant intermediate tables. Default is <code>true</code>.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.disallow_intermediate_table_input.DisallowIntermediateTableInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.disallow_intermediate_table_output.DisallowIntermediateTableOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.disallow_intermediate_table

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.disallow_intermediate_table.async_disallow_intermediate_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.disallow_intermediate_table_input.DisallowIntermediateTableInput = {
            "membership_identifier": membership_identifier,
            "intermediate_table_name": intermediate_table_name,
        }
        if include_descendants is not None:
            input_["include_descendants"] = include_descendants

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_analysis_log_export(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_log_export_identifier: "capo_cleanrooms.types.analysis_log_export_identifier.AnalysisLogExportIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_analysis_log_export_output.GetAnalysisLogExportOutput":
        """<p>Returns information about an analysis log export, including its current status and, if the export failed, the reason for the failure.</p> <p>Poll this operation until the <code>status</code> is <code>SUCCESS</code> or <code>FAILED</code>. An export can't be canceled after it starts.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership that the analysis log export belongs to. Currently accepts the membership ID.</p>
            analysis_log_export_identifier: <p>The unique identifier of the analysis log export to retrieve.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_analysis_log_export_input.GetAnalysisLogExportInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_analysis_log_export_output.GetAnalysisLogExportOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_log_export

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_log_export.async_get_analysis_log_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_analysis_log_export_input.GetAnalysisLogExportInput = {
            "membership_identifier": membership_identifier,
            "analysis_log_export_identifier": analysis_log_export_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_protected_job(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_job_identifier: "capo_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_protected_job_output.GetProtectedJobOutput":
        """<p>Returns job processing metadata.</p>

        Args:
            membership_identifier: <p> The identifier for a membership in a protected job instance.</p>
            protected_job_identifier: <p> The identifier for the protected job instance.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_protected_job_input.GetProtectedJobInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_protected_job_output.GetProtectedJobOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_job

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_job.async_get_protected_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_protected_job_input.GetProtectedJobInput = {
            "membership_identifier": membership_identifier,
            "protected_job_identifier": protected_job_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_protected_query(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_query_identifier: "capo_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_protected_query_output.GetProtectedQueryOutput":
        """<p>Returns query processing metadata.</p>

        Args:
            membership_identifier: <p>The identifier for a membership in a protected query instance.</p>
            protected_query_identifier: <p>The identifier for a protected query instance.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_protected_query_input.GetProtectedQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_protected_query_output.GetProtectedQueryOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_query

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_protected_query.async_get_protected_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_protected_query_input.GetProtectedQueryInput = {
            "membership_identifier": membership_identifier,
            "protected_query_identifier": protected_query_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_analysis_log_exports(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        analysis_identifier: Optional["capo_cleanrooms.types.uuid.UUID"] = None,
        status: Optional[
            "capo_cleanrooms.types.analysis_log_export_status.AnalysisLogExportStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_analysis_log_exports_output.ListAnalysisLogExportsOutput":
        """<p>Lists analysis log exports, sorted by the most recent export. Results are paginated. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership to list analysis log exports for. Currently accepts the membership ID.</p>
            analysis_identifier: <p>A filter on the unique identifier of the protected query that the analysis logs were exported for.</p>
            status: <p>A filter on the status of the analysis log export.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a <code>nextToken</code> even if the <code>maxResults</code> value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_analysis_log_exports_input.ListAnalysisLogExportsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_analysis_log_exports_output.ListAnalysisLogExportsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_log_exports

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_log_exports.async_list_analysis_log_exports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_analysis_log_exports_input.ListAnalysisLogExportsInput = {
            "membership_identifier": membership_identifier
        }
        if analysis_identifier is not None:
            input_["analysis_identifier"] = analysis_identifier
        if status is not None:
            input_["status"] = status
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

    async def iter_list_analysis_log_exports(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        analysis_identifier: Optional["capo_cleanrooms.types.uuid.UUID"] = None,
        status: Optional[
            "capo_cleanrooms.types.analysis_log_export_status.AnalysisLogExportStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.analysis_log_export_summary.AnalysisLogExportSummary]":
        _token = next_token
        while True:
            _response = await self.list_analysis_log_exports(
                membership_identifier,
                config_overrides=config_overrides,
                analysis_identifier=analysis_identifier,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("analysis_log_exports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_privacy_budgets(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        access_budget_resource_arn: Optional[
            "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> "capo_cleanrooms.types.list_privacy_budgets_output.ListPrivacyBudgetsOutput":
        """<p>Returns detailed information about the privacy budgets in a specified membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget is retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_type: <p>The privacy budget type.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
            access_budget_resource_arn: <p>The Amazon Resource Name (ARN) of the access budget resource to filter privacy budgets by.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_privacy_budgets_input.ListPrivacyBudgetsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_privacy_budgets_output.ListPrivacyBudgetsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budgets

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budgets.async_list_privacy_budgets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_privacy_budgets_input.ListPrivacyBudgetsInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_type": privacy_budget_type,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if access_budget_resource_arn is not None:
            input_["access_budget_resource_arn"] = access_budget_resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_privacy_budgets(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
        access_budget_resource_arn: Optional[
            "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
        ] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.privacy_budget_summary.PrivacyBudgetSummary]":
        _token = next_token
        while True:
            _response = await self.list_privacy_budgets(
                membership_identifier,
                privacy_budget_type,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                access_budget_resource_arn=access_budget_resource_arn,
            )
            _page = _resolve_path(_response, ("privacy_budget_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_protected_jobs(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.protected_job_status.ProtectedJobStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_protected_jobs_output.ListProtectedJobsOutput":
        """<p>Lists protected jobs, sorted by most recent job.</p>

        Args:
            membership_identifier: <p>The identifier for the membership in the collaboration.</p>
            status: <p>A filter on the status of the protected job.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met. </p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_protected_jobs_input.ListProtectedJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_protected_jobs_output.ListProtectedJobsOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_jobs

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_jobs.async_list_protected_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_protected_jobs_input.ListProtectedJobsInput = {
            "membership_identifier": membership_identifier
        }
        if status is not None:
            input_["status"] = status
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

    async def iter_list_protected_jobs(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.protected_job_status.ProtectedJobStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[capo_cleanrooms.types.protected_job_summary.ProtectedJobSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_protected_jobs(
                membership_identifier,
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("protected_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_protected_queries(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.protected_query_status.ProtectedQueryStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_cleanrooms.types.list_protected_queries_output.ListProtectedQueriesOutput"
    ):
        """<p>Lists protected queries, sorted by the most recent query.</p>

        Args:
            membership_identifier: <p>The identifier for the membership in the collaboration.</p>
            status: <p>A filter on the status of the protected query.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met. </p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_protected_queries_input.ListProtectedQueriesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_protected_queries_output.ListProtectedQueriesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_queries

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_protected_queries.async_list_protected_queries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_protected_queries_input.ListProtectedQueriesInput = {
            "membership_identifier": membership_identifier
        }
        if status is not None:
            input_["status"] = status
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

    async def iter_list_protected_queries(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        status: Optional[
            "capo_cleanrooms.types.protected_query_status.ProtectedQueryStatus"
        ] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.protected_query_summary.ProtectedQuerySummary]":
        _token = next_token
        while True:
            _response = await self.list_protected_queries(
                membership_identifier,
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("protected_queries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def preview_privacy_impact(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        parameters: "capo_cleanrooms.types.preview_privacy_impact_parameters_input.PreviewPrivacyImpactParametersInput",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> (
        "capo_cleanrooms.types.preview_privacy_impact_output.PreviewPrivacyImpactOutput"
    ):
        """<p>An estimate of the number of aggregation functions that the member who can query can run given epsilon and noise parameters.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. Accepts a membership ID.</p>
            parameters: <p>Specifies the desired epsilon and noise parameters to preview.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.preview_privacy_impact_input.PreviewPrivacyImpactInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.preview_privacy_impact_output.PreviewPrivacyImpactOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.preview_privacy_impact

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.preview_privacy_impact.async_preview_privacy_impact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.preview_privacy_impact_input.PreviewPrivacyImpactInput = {
            "membership_identifier": membership_identifier,
            "parameters": parameters,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_analysis_log_export(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_id: "capo_cleanrooms.types.uuid.UUID",
        analysis_type: "capo_cleanrooms.types.log_export_analysis_type.LogExportAnalysisType",
        result_configuration: "capo_cleanrooms.types.analysis_log_export_result_configuration.AnalysisLogExportResultConfiguration",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.start_analysis_log_export_output.StartAnalysisLogExportOutput":
        """<p>Starts an export of the Apache Spark logs for a protected query to an Amazon S3 bucket that you own. Use the exported logs to diagnose a query that failed or that ran more slowly than you expected.</p> <p>Clean Rooms exports a redacted copy of the Spark logs instead of the raw logs. Analyze the exported logs with the tooling of your choice, such as Spark History Server. For details about what the exported logs contain, see <a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs-contents.html">https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs-contents.html</a>.</p> <p>The export runs asynchronously and returns with a <code>status</code> of <code>IN_PROGRESS</code>. Call <code>GetAnalysisLogExport</code> to poll for the final status.</p> <important> <p>To use this operation, you must have the <code>CAN_EXPORT_QUERY_ANALYSIS_LOG</code> ability for your membership. You must also be the query runner or the query payer. Having the ability alone is not sufficient.</p> <p>The query must have reached a terminal state, and it must have reached the execution stage. A query that failed validation or that was canceled before it started produces no Spark logs.</p> <p>Log export isn't supported for queries that use differential privacy, and isn't supported for PySpark jobs.</p> <p>The destination bucket must be in the same Amazon Web Services Region as the collaboration. Cross-Region export isn't supported.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs.html">https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs.html</a>.</p>

        Args:
            membership_identifier: <p>A unique identifier for the membership to export the analysis logs for. Currently accepts a membership ID.</p>
            analysis_id: <p>The unique identifier of the protected query that you want to export the analysis logs for.</p>
            analysis_type: <p>The type of analysis that the logs are exported for. Currently, only <code>PROTECTED_QUERY</code> is supported.</p>
            result_configuration: <p>The details needed to write the exported analysis logs.</p> <p>You don't need to create an IAM role for log export. Clean Rooms writes the exported logs using your own identity, so Clean Rooms writes the exported logs only where your existing permissions allow.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.start_analysis_log_export_input.StartAnalysisLogExportInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.start_analysis_log_export_output.StartAnalysisLogExportOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_analysis_log_export

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_analysis_log_export.async_start_analysis_log_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.start_analysis_log_export_input.StartAnalysisLogExportInput = {
            "membership_identifier": membership_identifier,
            "analysis_id": analysis_id,
            "analysis_type": analysis_type,
            "result_configuration": result_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_protected_job(
        self,
        type: "capo_cleanrooms.types.protected_job_type.ProtectedJobType",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        job_parameters: "capo_cleanrooms.types.protected_job_parameters.ProtectedJobParameters",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        result_configuration: Optional[
            "capo_cleanrooms.types.protected_job_result_configuration_input.ProtectedJobResultConfigurationInput"
        ] = None,
        compute_configuration: Optional[
            "capo_cleanrooms.types.protected_job_compute_configuration.ProtectedJobComputeConfiguration"
        ] = None,
        job_compute_payer_account_id: Optional[
            "capo_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "capo_cleanrooms.types.start_protected_job_output.StartProtectedJobOutput":
        """<p>Creates a protected job that is started by Clean Rooms.</p>

        Args:
            type: <p> The type of protected job to start.</p>
            membership_identifier: <p>A unique identifier for the membership to run this job against. Currently accepts a membership ID.</p>
            job_parameters: <p> The job parameters.</p>
            result_configuration: <p>The details needed to write the job results.</p>
            compute_configuration: <p>The compute configuration for the protected job.</p>
            job_compute_payer_account_id: <p>The account ID of the member that pays for the job compute costs.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.start_protected_job_input.StartProtectedJobInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.start_protected_job_output.StartProtectedJobOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_job

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_job.async_start_protected_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.start_protected_job_input.StartProtectedJobInput = {
            "type": type,
            "membership_identifier": membership_identifier,
            "job_parameters": job_parameters,
        }
        if result_configuration is not None:
            input_["result_configuration"] = result_configuration
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if job_compute_payer_account_id is not None:
            input_["job_compute_payer_account_id"] = job_compute_payer_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_protected_query(
        self,
        type: "capo_cleanrooms.types.protected_query_type.ProtectedQueryType",
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        sql_parameters: "capo_cleanrooms.types.protected_query_sql_parameters.ProtectedQuerySQLParameters",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        result_configuration: Optional[
            "capo_cleanrooms.types.protected_query_result_configuration.ProtectedQueryResultConfiguration"
        ] = None,
        compute_configuration: Optional[
            "capo_cleanrooms.types.compute_configuration.ComputeConfiguration"
        ] = None,
        query_compute_payer_account_id: Optional[
            "capo_cleanrooms.types.account_id.AccountId"
        ] = None,
    ) -> "capo_cleanrooms.types.start_protected_query_output.StartProtectedQueryOutput":
        """<p>Creates a protected query that is started by Clean Rooms.</p>

        Args:
            type: <p>The type of the protected query to be started.</p>
            membership_identifier: <p>A unique identifier for the membership to run this query against. Currently accepts a membership ID.</p>
            sql_parameters: <p>The protected SQL query parameters.</p>
            result_configuration: <p>The details needed to write the query results.</p>
            compute_configuration: <p> The compute configuration for the protected query.</p>
            query_compute_payer_account_id: <p>The account ID of the member that pays for the query compute costs.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.start_protected_query_input.StartProtectedQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.start_protected_query_output.StartProtectedQueryOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_query

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.start_protected_query.async_start_protected_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.start_protected_query_input.StartProtectedQueryInput = {
            "type": type,
            "membership_identifier": membership_identifier,
            "sql_parameters": sql_parameters,
        }
        if result_configuration is not None:
            input_["result_configuration"] = result_configuration
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if query_compute_payer_account_id is not None:
            input_["query_compute_payer_account_id"] = query_compute_payer_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_protected_job(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_job_identifier: "capo_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier",
        target_status: "capo_cleanrooms.types.target_protected_job_status.TargetProtectedJobStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.update_protected_job_output.UpdateProtectedJobOutput":
        """<p>Updates the processing of a currently running job.</p>

        Args:
            membership_identifier: <p>The identifier for a member of a protected job instance.</p>
            protected_job_identifier: <p> The identifier of the protected job to update.</p>
            target_status: <p>The target status of a protected job. Used to update the execution status of a currently running job.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_protected_job_input.UpdateProtectedJobInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_protected_job_output.UpdateProtectedJobOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_job

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_job.async_update_protected_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_protected_job_input.UpdateProtectedJobInput = {
            "membership_identifier": membership_identifier,
            "protected_job_identifier": protected_job_identifier,
            "target_status": target_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_protected_query(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        protected_query_identifier: "capo_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier",
        target_status: "capo_cleanrooms.types.target_protected_query_status.TargetProtectedQueryStatus",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> (
        "capo_cleanrooms.types.update_protected_query_output.UpdateProtectedQueryOutput"
    ):
        """<p>Updates the processing of a currently running query.</p>

        Args:
            membership_identifier: <p>The identifier for a member of a protected query instance.</p>
            protected_query_identifier: <p>The identifier for a protected query instance.</p>
            target_status: <p>The target status of a query. Used to update the execution status of a currently running query.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_protected_query_input.UpdateProtectedQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_protected_query_output.UpdateProtectedQueryOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_query

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_protected_query.async_update_protected_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_protected_query_input.UpdateProtectedQueryInput = {
            "membership_identifier": membership_identifier,
            "protected_query_identifier": protected_query_identifier,
            "target_status": target_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_privacy_budget_template(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        parameters: "capo_cleanrooms.types.privacy_budget_template_parameters_input.PrivacyBudgetTemplateParametersInput",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        auto_refresh: Optional[
            "capo_cleanrooms.types.privacy_budget_template_auto_refresh.PrivacyBudgetTemplateAutoRefresh"
        ] = None,
        tags: Optional["capo_cleanrooms.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanrooms.types.create_privacy_budget_template_output.CreatePrivacyBudgetTemplateOutput":
        """<p>Creates a privacy budget template for a specified collaboration. Each collaboration can have only one privacy budget template. If you need to change the privacy budget template, use the <a>UpdatePrivacyBudgetTemplate</a> operation.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is created in the collaboration that this membership belongs to. Accepts a membership ID.</p>
            auto_refresh: <p>How often the privacy budget refreshes.</p> <important> <p>If you plan to regularly bring new data into the collaboration, you can use <code>CALENDAR_MONTH</code> to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queries across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.</p> </important>
            privacy_budget_type: <p>Specifies the type of the privacy budget template.</p>
            parameters: <p>Specifies your parameters for the privacy budget template.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request denied because service quota has been exceeded.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.create_privacy_budget_template_input.CreatePrivacyBudgetTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.create_privacy_budget_template_output.CreatePrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_privacy_budget_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_privacy_budget_template.async_create_privacy_budget_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.create_privacy_budget_template_input.CreatePrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_type": privacy_budget_type,
            "parameters": parameters,
        }
        if auto_refresh is not None:
            input_["auto_refresh"] = auto_refresh
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_privacy_budget_template(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.get_privacy_budget_template_output.GetPrivacyBudgetTemplateOutput":
        """<p>Returns details for a specified privacy budget template.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_template_identifier: <p>A unique identifier for your privacy budget template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.get_privacy_budget_template_input.GetPrivacyBudgetTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.get_privacy_budget_template_output.GetPrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_privacy_budget_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_privacy_budget_template.async_get_privacy_budget_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.get_privacy_budget_template_input.GetPrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_privacy_budget_template(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        parameters: Optional[
            "capo_cleanrooms.types.privacy_budget_template_update_parameters.PrivacyBudgetTemplateUpdateParameters"
        ] = None,
    ) -> "capo_cleanrooms.types.update_privacy_budget_template_output.UpdatePrivacyBudgetTemplateOutput":
        """<p>Updates the privacy budget template for the specified collaboration.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is updated in the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_template_identifier: <p>A unique identifier for your privacy budget template that you want to update.</p>
            privacy_budget_type: <p>Specifies the type of the privacy budget template.</p>
            parameters: <p>Specifies the epsilon and noise parameters for the privacy budget template.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.update_privacy_budget_template_input.UpdatePrivacyBudgetTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.update_privacy_budget_template_output.UpdatePrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_privacy_budget_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_privacy_budget_template.async_update_privacy_budget_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.update_privacy_budget_template_input.UpdatePrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
            "privacy_budget_type": privacy_budget_type,
        }
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_privacy_budget_template(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "capo_cleanrooms.types.delete_privacy_budget_template_output.DeletePrivacyBudgetTemplateOutput":
        """<p>Deletes a privacy budget template for a specified collaboration.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is deleted from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            privacy_budget_template_identifier: <p>A unique identifier for your privacy budget template. </p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.delete_privacy_budget_template_input.DeletePrivacyBudgetTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.delete_privacy_budget_template_output.DeletePrivacyBudgetTemplateOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_privacy_budget_template

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_privacy_budget_template.async_delete_privacy_budget_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.delete_privacy_budget_template_input.DeletePrivacyBudgetTemplateInput = {
            "membership_identifier": membership_identifier,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_privacy_budget_templates(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanrooms.types.list_privacy_budget_templates_output.ListPrivacyBudgetTemplatesOutput":
        """<p>Returns detailed information about the privacy budget templates in a specified membership.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The privacy budget templates are retrieved from the collaboration that this membership belongs to. Accepts a membership ID.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>

        Raises:
            capo_cleanrooms.errors.access_denied_exception.AccessDeniedException: <p>Caller does not have sufficient access to perform this action.</p>
            capo_cleanrooms.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_cleanrooms.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanrooms.types.list_privacy_budget_templates_input.ListPrivacyBudgetTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_cleanrooms.types.list_privacy_budget_templates_output.ListPrivacyBudgetTemplatesOutput"
        ]:
            import capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budget_templates

            (
                output,
                http_response,
            ) = await capo_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_privacy_budget_templates.async_list_privacy_budget_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanrooms.types.list_privacy_budget_templates_input.ListPrivacyBudgetTemplatesInput = {
            "membership_identifier": membership_identifier
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

    async def iter_list_privacy_budget_templates(
        self,
        membership_identifier: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "capo_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanrooms.types.privacy_budget_template_summary.PrivacyBudgetTemplateSummary]":
        _token = next_token
        while True:
            _response = await self.list_privacy_budget_templates(
                membership_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("privacy_budget_template_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
