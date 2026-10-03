"""Generated from Smithy shape ``com.amazonaws.redshift#RedshiftServiceVersion20121201``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_redshift._auth._signers
import capo_redshift._auth._sigv4
from capo_redshift._auth._identity import Credentials
from capo_redshift._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_redshift._auth._zapros_handler import AuthMiddleware
from capo_redshift._pagination import resolve_path as _resolve_path
from capo_redshift._services._aws_config import aaws_config
from capo_redshift._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_redshift.types.accept_reserved_node_exchange_input_message
    import capo_redshift.types.accept_reserved_node_exchange_output_message
    import capo_redshift.types.account_attribute_list
    import capo_redshift.types.action_type
    import capo_redshift.types.application_type
    import capo_redshift.types.aqua_configuration_status
    import capo_redshift.types.associate_data_share_consumer_message
    import capo_redshift.types.association
    import capo_redshift.types.attribute_name_list
    import capo_redshift.types.authentication_profile_name_string
    import capo_redshift.types.authorize_cluster_security_group_ingress_message
    import capo_redshift.types.authorize_cluster_security_group_ingress_result
    import capo_redshift.types.authorize_data_share_message
    import capo_redshift.types.authorize_endpoint_access_message
    import capo_redshift.types.authorize_snapshot_access_message
    import capo_redshift.types.authorize_snapshot_access_result
    import capo_redshift.types.authorized_token_issuer_list
    import capo_redshift.types.batch_delete_cluster_snapshots_request
    import capo_redshift.types.batch_delete_cluster_snapshots_result
    import capo_redshift.types.batch_modify_cluster_snapshots_message
    import capo_redshift.types.batch_modify_cluster_snapshots_output_message
    import capo_redshift.types.boolean
    import capo_redshift.types.boolean_optional
    import capo_redshift.types.cancel_resize_message
    import capo_redshift.types.catalog_name_string
    import capo_redshift.types.cluster
    import capo_redshift.types.cluster_credentials
    import capo_redshift.types.cluster_db_revision
    import capo_redshift.types.cluster_db_revisions_message
    import capo_redshift.types.cluster_extended_credentials
    import capo_redshift.types.cluster_identifier_list
    import capo_redshift.types.cluster_parameter_group
    import capo_redshift.types.cluster_parameter_group_details
    import capo_redshift.types.cluster_parameter_group_name_message
    import capo_redshift.types.cluster_parameter_groups_message
    import capo_redshift.types.cluster_security_group
    import capo_redshift.types.cluster_security_group_message
    import capo_redshift.types.cluster_security_group_name_list
    import capo_redshift.types.cluster_subnet_group
    import capo_redshift.types.cluster_subnet_group_message
    import capo_redshift.types.cluster_version
    import capo_redshift.types.cluster_versions_message
    import capo_redshift.types.clusters_message
    import capo_redshift.types.consumer_identifier_list
    import capo_redshift.types.copy_cluster_snapshot_message
    import capo_redshift.types.copy_cluster_snapshot_result
    import capo_redshift.types.create_authentication_profile_message
    import capo_redshift.types.create_authentication_profile_result
    import capo_redshift.types.create_cluster_message
    import capo_redshift.types.create_cluster_parameter_group_message
    import capo_redshift.types.create_cluster_parameter_group_result
    import capo_redshift.types.create_cluster_result
    import capo_redshift.types.create_cluster_security_group_message
    import capo_redshift.types.create_cluster_security_group_result
    import capo_redshift.types.create_cluster_snapshot_message
    import capo_redshift.types.create_cluster_snapshot_result
    import capo_redshift.types.create_cluster_subnet_group_message
    import capo_redshift.types.create_cluster_subnet_group_result
    import capo_redshift.types.create_custom_domain_association_message
    import capo_redshift.types.create_custom_domain_association_result
    import capo_redshift.types.create_endpoint_access_message
    import capo_redshift.types.create_event_subscription_message
    import capo_redshift.types.create_event_subscription_result
    import capo_redshift.types.create_hsm_client_certificate_message
    import capo_redshift.types.create_hsm_client_certificate_result
    import capo_redshift.types.create_hsm_configuration_message
    import capo_redshift.types.create_hsm_configuration_result
    import capo_redshift.types.create_integration_message
    import capo_redshift.types.create_qev2_idc_application_message
    import capo_redshift.types.create_qev2_idc_application_result
    import capo_redshift.types.create_redshift_idc_application_message
    import capo_redshift.types.create_redshift_idc_application_result
    import capo_redshift.types.create_scheduled_action_message
    import capo_redshift.types.create_snapshot_copy_grant_message
    import capo_redshift.types.create_snapshot_copy_grant_result
    import capo_redshift.types.create_snapshot_schedule_message
    import capo_redshift.types.create_tags_message
    import capo_redshift.types.create_usage_limit_message
    import capo_redshift.types.custom_domain_associations_message
    import capo_redshift.types.custom_domain_certificate_arn_string
    import capo_redshift.types.custom_domain_name_string
    import capo_redshift.types.customer_storage_message
    import capo_redshift.types.data_share
    import capo_redshift.types.data_share_status_for_consumer
    import capo_redshift.types.data_share_status_for_producer
    import capo_redshift.types.db_group_list
    import capo_redshift.types.deauthorize_data_share_message
    import capo_redshift.types.delete_authentication_profile_message
    import capo_redshift.types.delete_authentication_profile_result
    import capo_redshift.types.delete_cluster_message
    import capo_redshift.types.delete_cluster_parameter_group_message
    import capo_redshift.types.delete_cluster_result
    import capo_redshift.types.delete_cluster_security_group_message
    import capo_redshift.types.delete_cluster_snapshot_message
    import capo_redshift.types.delete_cluster_snapshot_message_list
    import capo_redshift.types.delete_cluster_snapshot_result
    import capo_redshift.types.delete_cluster_subnet_group_message
    import capo_redshift.types.delete_custom_domain_association_message
    import capo_redshift.types.delete_endpoint_access_message
    import capo_redshift.types.delete_event_subscription_message
    import capo_redshift.types.delete_hsm_client_certificate_message
    import capo_redshift.types.delete_hsm_configuration_message
    import capo_redshift.types.delete_integration_message
    import capo_redshift.types.delete_qev2_idc_application_message
    import capo_redshift.types.delete_redshift_idc_application_message
    import capo_redshift.types.delete_resource_policy_message
    import capo_redshift.types.delete_scheduled_action_message
    import capo_redshift.types.delete_snapshot_copy_grant_message
    import capo_redshift.types.delete_snapshot_schedule_message
    import capo_redshift.types.delete_tags_message
    import capo_redshift.types.delete_usage_limit_message
    import capo_redshift.types.deregister_namespace_input_message
    import capo_redshift.types.deregister_namespace_output_message
    import capo_redshift.types.describe_account_attributes_message
    import capo_redshift.types.describe_authentication_profiles_message
    import capo_redshift.types.describe_authentication_profiles_result
    import capo_redshift.types.describe_cluster_db_revisions_message
    import capo_redshift.types.describe_cluster_parameter_groups_message
    import capo_redshift.types.describe_cluster_parameters_message
    import capo_redshift.types.describe_cluster_security_groups_message
    import capo_redshift.types.describe_cluster_snapshots_message
    import capo_redshift.types.describe_cluster_subnet_groups_message
    import capo_redshift.types.describe_cluster_tracks_message
    import capo_redshift.types.describe_cluster_versions_message
    import capo_redshift.types.describe_clusters_message
    import capo_redshift.types.describe_custom_domain_associations_message
    import capo_redshift.types.describe_data_shares_for_consumer_message
    import capo_redshift.types.describe_data_shares_for_consumer_result
    import capo_redshift.types.describe_data_shares_for_producer_message
    import capo_redshift.types.describe_data_shares_for_producer_result
    import capo_redshift.types.describe_data_shares_message
    import capo_redshift.types.describe_data_shares_result
    import capo_redshift.types.describe_default_cluster_parameters_message
    import capo_redshift.types.describe_default_cluster_parameters_result
    import capo_redshift.types.describe_endpoint_access_message
    import capo_redshift.types.describe_endpoint_authorization_message
    import capo_redshift.types.describe_event_categories_message
    import capo_redshift.types.describe_event_subscriptions_message
    import capo_redshift.types.describe_events_message
    import capo_redshift.types.describe_hsm_client_certificates_message
    import capo_redshift.types.describe_hsm_configurations_message
    import capo_redshift.types.describe_inbound_integrations_message
    import capo_redshift.types.describe_integrations_filter_list
    import capo_redshift.types.describe_integrations_message
    import capo_redshift.types.describe_logging_status_message
    import capo_redshift.types.describe_node_configuration_options_message
    import capo_redshift.types.describe_orderable_cluster_options_message
    import capo_redshift.types.describe_partners_input_message
    import capo_redshift.types.describe_partners_output_message
    import capo_redshift.types.describe_qev2_idc_applications_message
    import capo_redshift.types.describe_qev2_idc_applications_result
    import capo_redshift.types.describe_redshift_idc_applications_message
    import capo_redshift.types.describe_redshift_idc_applications_result
    import capo_redshift.types.describe_reserved_node_exchange_status_input_message
    import capo_redshift.types.describe_reserved_node_exchange_status_output_message
    import capo_redshift.types.describe_reserved_node_offerings_message
    import capo_redshift.types.describe_reserved_nodes_message
    import capo_redshift.types.describe_resize_message
    import capo_redshift.types.describe_scheduled_actions_message
    import capo_redshift.types.describe_snapshot_copy_grants_message
    import capo_redshift.types.describe_snapshot_schedules_message
    import capo_redshift.types.describe_snapshot_schedules_output_message
    import capo_redshift.types.describe_table_restore_status_message
    import capo_redshift.types.describe_tags_message
    import capo_redshift.types.describe_usage_limits_message
    import capo_redshift.types.disable_logging_message
    import capo_redshift.types.disable_snapshot_copy_message
    import capo_redshift.types.disable_snapshot_copy_result
    import capo_redshift.types.disassociate_data_share_consumer_message
    import capo_redshift.types.enable_logging_message
    import capo_redshift.types.enable_snapshot_copy_message
    import capo_redshift.types.enable_snapshot_copy_result
    import capo_redshift.types.encryption_context_map
    import capo_redshift.types.endpoint_access
    import capo_redshift.types.endpoint_access_list
    import capo_redshift.types.endpoint_authorization
    import capo_redshift.types.endpoint_authorization_list
    import capo_redshift.types.event
    import capo_redshift.types.event_categories_list
    import capo_redshift.types.event_categories_message
    import capo_redshift.types.event_subscription
    import capo_redshift.types.event_subscriptions_message
    import capo_redshift.types.events_message
    import capo_redshift.types.failover_primary_compute_input_message
    import capo_redshift.types.failover_primary_compute_result
    import capo_redshift.types.get_cluster_credentials_message
    import capo_redshift.types.get_cluster_credentials_with_iam_message
    import capo_redshift.types.get_identity_center_auth_token_request
    import capo_redshift.types.get_identity_center_auth_token_response
    import capo_redshift.types.get_reserved_node_exchange_configuration_options_input_message
    import capo_redshift.types.get_reserved_node_exchange_configuration_options_output_message
    import capo_redshift.types.get_reserved_node_exchange_offerings_input_message
    import capo_redshift.types.get_reserved_node_exchange_offerings_output_message
    import capo_redshift.types.get_resource_policy_message
    import capo_redshift.types.get_resource_policy_result
    import capo_redshift.types.hsm_client_certificate
    import capo_redshift.types.hsm_client_certificate_message
    import capo_redshift.types.hsm_configuration
    import capo_redshift.types.hsm_configuration_message
    import capo_redshift.types.iam_role_arn_list
    import capo_redshift.types.idc_display_name_string
    import capo_redshift.types.identity_namespace_string
    import capo_redshift.types.inbound_integration
    import capo_redshift.types.inbound_integration_arn
    import capo_redshift.types.inbound_integrations_message
    import capo_redshift.types.integer
    import capo_redshift.types.integer_optional
    import capo_redshift.types.integration
    import capo_redshift.types.integration_arn
    import capo_redshift.types.integration_description
    import capo_redshift.types.integration_name
    import capo_redshift.types.integrations_message
    import capo_redshift.types.lakehouse_configuration
    import capo_redshift.types.lakehouse_idc_registration
    import capo_redshift.types.lakehouse_registration
    import capo_redshift.types.list_recommendations_message
    import capo_redshift.types.list_recommendations_result
    import capo_redshift.types.log_destination_type
    import capo_redshift.types.log_type_list
    import capo_redshift.types.logging_status
    import capo_redshift.types.long
    import capo_redshift.types.long_optional
    import capo_redshift.types.maintenance_track
    import capo_redshift.types.modify_aqua_input_message
    import capo_redshift.types.modify_aqua_output_message
    import capo_redshift.types.modify_authentication_profile_message
    import capo_redshift.types.modify_authentication_profile_result
    import capo_redshift.types.modify_cluster_db_revision_message
    import capo_redshift.types.modify_cluster_db_revision_result
    import capo_redshift.types.modify_cluster_iam_roles_message
    import capo_redshift.types.modify_cluster_iam_roles_result
    import capo_redshift.types.modify_cluster_maintenance_message
    import capo_redshift.types.modify_cluster_maintenance_result
    import capo_redshift.types.modify_cluster_message
    import capo_redshift.types.modify_cluster_parameter_group_message
    import capo_redshift.types.modify_cluster_result
    import capo_redshift.types.modify_cluster_snapshot_message
    import capo_redshift.types.modify_cluster_snapshot_result
    import capo_redshift.types.modify_cluster_snapshot_schedule_message
    import capo_redshift.types.modify_cluster_subnet_group_message
    import capo_redshift.types.modify_cluster_subnet_group_result
    import capo_redshift.types.modify_custom_domain_association_message
    import capo_redshift.types.modify_custom_domain_association_result
    import capo_redshift.types.modify_endpoint_access_message
    import capo_redshift.types.modify_event_subscription_message
    import capo_redshift.types.modify_event_subscription_result
    import capo_redshift.types.modify_integration_message
    import capo_redshift.types.modify_lakehouse_configuration_message
    import capo_redshift.types.modify_qev2_idc_application_message
    import capo_redshift.types.modify_qev2_idc_application_result
    import capo_redshift.types.modify_redshift_idc_application_message
    import capo_redshift.types.modify_redshift_idc_application_result
    import capo_redshift.types.modify_scheduled_action_message
    import capo_redshift.types.modify_snapshot_copy_retention_period_message
    import capo_redshift.types.modify_snapshot_copy_retention_period_result
    import capo_redshift.types.modify_snapshot_schedule_message
    import capo_redshift.types.modify_usage_limit_message
    import capo_redshift.types.namespace_identifier_union
    import capo_redshift.types.node_configuration_option
    import capo_redshift.types.node_configuration_options_filter_list
    import capo_redshift.types.node_configuration_options_message
    import capo_redshift.types.orderable_cluster_option
    import capo_redshift.types.orderable_cluster_options_message
    import capo_redshift.types.parameter
    import capo_redshift.types.parameters_list
    import capo_redshift.types.partner_integration_account_id
    import capo_redshift.types.partner_integration_cluster_identifier
    import capo_redshift.types.partner_integration_database_name
    import capo_redshift.types.partner_integration_input_message
    import capo_redshift.types.partner_integration_output_message
    import capo_redshift.types.partner_integration_partner_name
    import capo_redshift.types.partner_integration_status
    import capo_redshift.types.partner_integration_status_message
    import capo_redshift.types.pause_cluster_message
    import capo_redshift.types.pause_cluster_result
    import capo_redshift.types.purchase_reserved_node_offering_message
    import capo_redshift.types.purchase_reserved_node_offering_result
    import capo_redshift.types.put_resource_policy_message
    import capo_redshift.types.put_resource_policy_result
    import capo_redshift.types.qev2_idc_application
    import capo_redshift.types.qev2_idc_application_name
    import capo_redshift.types.reboot_cluster_message
    import capo_redshift.types.reboot_cluster_result
    import capo_redshift.types.recommendation
    import capo_redshift.types.redshift_idc_application
    import capo_redshift.types.redshift_idc_application_name
    import capo_redshift.types.register_namespace_input_message
    import capo_redshift.types.register_namespace_output_message
    import capo_redshift.types.reject_data_share_message
    import capo_redshift.types.reserved_node
    import capo_redshift.types.reserved_node_configuration_option
    import capo_redshift.types.reserved_node_exchange_action_type
    import capo_redshift.types.reserved_node_exchange_status
    import capo_redshift.types.reserved_node_offering
    import capo_redshift.types.reserved_node_offerings_message
    import capo_redshift.types.reserved_nodes_message
    import capo_redshift.types.reset_cluster_parameter_group_message
    import capo_redshift.types.resize_cluster_message
    import capo_redshift.types.resize_cluster_result
    import capo_redshift.types.resize_progress_message
    import capo_redshift.types.restore_from_cluster_snapshot_message
    import capo_redshift.types.restore_from_cluster_snapshot_result
    import capo_redshift.types.restore_table_from_cluster_snapshot_message
    import capo_redshift.types.restore_table_from_cluster_snapshot_result
    import capo_redshift.types.resume_cluster_message
    import capo_redshift.types.resume_cluster_result
    import capo_redshift.types.revoke_cluster_security_group_ingress_message
    import capo_redshift.types.revoke_cluster_security_group_ingress_result
    import capo_redshift.types.revoke_endpoint_access_message
    import capo_redshift.types.revoke_snapshot_access_message
    import capo_redshift.types.revoke_snapshot_access_result
    import capo_redshift.types.rotate_encryption_key_message
    import capo_redshift.types.rotate_encryption_key_result
    import capo_redshift.types.s3_key_prefix_value
    import capo_redshift.types.schedule_definition_list
    import capo_redshift.types.scheduled_action
    import capo_redshift.types.scheduled_action_filter_list
    import capo_redshift.types.scheduled_action_type
    import capo_redshift.types.scheduled_action_type_values
    import capo_redshift.types.scheduled_actions_message
    import capo_redshift.types.sensitive_string
    import capo_redshift.types.service_integration_list
    import capo_redshift.types.snapshot
    import capo_redshift.types.snapshot_copy_grant
    import capo_redshift.types.snapshot_copy_grant_message
    import capo_redshift.types.snapshot_identifier_list
    import capo_redshift.types.snapshot_message
    import capo_redshift.types.snapshot_schedule
    import capo_redshift.types.snapshot_sorting_entity_list
    import capo_redshift.types.source_arn
    import capo_redshift.types.source_ids_list
    import capo_redshift.types.source_type
    import capo_redshift.types.string
    import capo_redshift.types.subnet_identifier_list
    import capo_redshift.types.t_stamp
    import capo_redshift.types.table_restore_status
    import capo_redshift.types.table_restore_status_message
    import capo_redshift.types.tag_key_list
    import capo_redshift.types.tag_list
    import capo_redshift.types.tag_value_list
    import capo_redshift.types.tagged_resource
    import capo_redshift.types.tagged_resource_list_message
    import capo_redshift.types.target_arn
    import capo_redshift.types.track_list_message
    import capo_redshift.types.update_partner_status_input_message
    import capo_redshift.types.usage_limit
    import capo_redshift.types.usage_limit_breach_action
    import capo_redshift.types.usage_limit_feature_type
    import capo_redshift.types.usage_limit_limit_type
    import capo_redshift.types.usage_limit_list
    import capo_redshift.types.usage_limit_period
    import capo_redshift.types.vpc_identifier_list
    import capo_redshift.types.vpc_security_group_id_list


class AsyncRedshiftClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncRedshiftClient:
    """A client for the ``Redshift`` service.

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
        self._config = AsyncRedshiftClientConfig(
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
        self, config_overrides: Optional[AsyncRedshiftClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRedshiftClientConfig = config_overrides or {}
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

    async def accept_reserved_node_exchange(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        reserved_node_id: Optional["capo_redshift.types.string.String"] = None,
        target_reserved_node_offering_id: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> "capo_redshift.types.accept_reserved_node_exchange_output_message.AcceptReservedNodeExchangeOutputMessage":
        """<p>Exchanges a DC1 Reserved Node for a DC2 Reserved Node with no changes to the configuration (term, payment type, or number of nodes) and no additional costs. </p>

        Args:
            reserved_node_id: <p>A string representing the node identifier of the DC1 Reserved Node to be exchanged.</p>
            target_reserved_node_offering_id: <p>The unique identifier of the DC2 Reserved Node offering to be used for the exchange. You can obtain the value for the parameter by calling <a>GetReservedNodeExchangeOfferings</a> </p>

        Raises:
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.invalid_reserved_node_state_fault.InvalidReservedNodeStateFault: <p>Indicates that the Reserved Node being exchanged is not in an active state.</p>
            capo_redshift.errors.reserved_node_already_exists_fault.ReservedNodeAlreadyExistsFault: <p>User already has a reservation with the given identifier.</p>
            capo_redshift.errors.reserved_node_already_migrated_fault.ReservedNodeAlreadyMigratedFault: <p>Indicates that the reserved node has already been exchanged.</p>
            capo_redshift.errors.reserved_node_not_found_fault.ReservedNodeNotFoundFault: <p>The specified reserved compute node not found.</p>
            capo_redshift.errors.reserved_node_offering_not_found_fault.ReservedNodeOfferingNotFoundFault: <p>Specified offering does not exist.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.accept_reserved_node_exchange_input_message.AcceptReservedNodeExchangeInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.accept_reserved_node_exchange_output_message.AcceptReservedNodeExchangeOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.accept_reserved_node_exchange

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.accept_reserved_node_exchange.async_accept_reserved_node_exchange(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.accept_reserved_node_exchange_input_message.AcceptReservedNodeExchangeInputMessage = {}
        if reserved_node_id is not None:
            input_["reserved_node_id"] = reserved_node_id
        if target_reserved_node_offering_id is not None:
            input_["target_reserved_node_offering_id"] = (
                target_reserved_node_offering_id
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_partner(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        account_id: Optional[
            "capo_redshift.types.partner_integration_account_id.PartnerIntegrationAccountId"
        ] = None,
        cluster_identifier: Optional[
            "capo_redshift.types.partner_integration_cluster_identifier.PartnerIntegrationClusterIdentifier"
        ] = None,
        database_name: Optional[
            "capo_redshift.types.partner_integration_database_name.PartnerIntegrationDatabaseName"
        ] = None,
        partner_name: Optional[
            "capo_redshift.types.partner_integration_partner_name.PartnerIntegrationPartnerName"
        ] = None,
    ) -> "capo_redshift.types.partner_integration_output_message.PartnerIntegrationOutputMessage":
        """<p>Adds a partner integration to a cluster. This operation authorizes a partner to push status updates for the specified database. To complete the integration, you also set up the integration on the partner website.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID that owns the cluster.</p>
            cluster_identifier: <p>The cluster identifier of the cluster that receives data from the partner.</p>
            database_name: <p>The name of the database that receives data from the partner.</p>
            partner_name: <p>The name of the partner that is authorized to send data.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.partner_not_found_fault.PartnerNotFoundFault: <p>The name of the partner was not found.</p>
            capo_redshift.errors.unauthorized_partner_integration_fault.UnauthorizedPartnerIntegrationFault: <p>The partner integration is not authorized.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.partner_integration_input_message.PartnerIntegrationInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.partner_integration_output_message.PartnerIntegrationOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.add_partner

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.add_partner.async_add_partner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.partner_integration_input_message.PartnerIntegrationInputMessage = {}
        if account_id is not None:
            input_["account_id"] = account_id
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if database_name is not None:
            input_["database_name"] = database_name
        if partner_name is not None:
            input_["partner_name"] = partner_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_data_share_consumer(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        data_share_arn: Optional["capo_redshift.types.string.String"] = None,
        associate_entire_account: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        consumer_arn: Optional["capo_redshift.types.string.String"] = None,
        consumer_region: Optional["capo_redshift.types.string.String"] = None,
        allow_writes: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_redshift.types.data_share.DataShare":
        """<p>From a datashare consumer account, associates a datashare with the account (AssociateEntireAccount) or the specified namespace (ConsumerArn). If you make this association, the consumer can consume the datashare.</p>

        Args:
            data_share_arn: <p>The Amazon Resource Name (ARN) of the datashare that the consumer is to use.</p>
            associate_entire_account: <p>A value that specifies whether the datashare is associated with the entire account.</p>
            consumer_arn: <p>The Amazon Resource Name (ARN) of the consumer namespace associated with the datashare.</p>
            consumer_region: <p>From a datashare consumer account, associates a datashare with all existing and future namespaces in the specified Amazon Web Services Region.</p>
            allow_writes: <p>If set to true, allows write operations for a datashare.</p>

        Raises:
            capo_redshift.errors.invalid_data_share_fault.InvalidDataShareFault: <p>There is an error with the datashare.</p>
            capo_redshift.errors.invalid_namespace_fault.InvalidNamespaceFault: <p>The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.associate_data_share_consumer_message.AssociateDataShareConsumerMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.data_share.DataShare"]:
            import capo_redshift._operations.redshift_service_version20121201.associate_data_share_consumer

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.associate_data_share_consumer.async_associate_data_share_consumer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.associate_data_share_consumer_message.AssociateDataShareConsumerMessage = {}
        if data_share_arn is not None:
            input_["data_share_arn"] = data_share_arn
        if associate_entire_account is not None:
            input_["associate_entire_account"] = associate_entire_account
        if consumer_arn is not None:
            input_["consumer_arn"] = consumer_arn
        if consumer_region is not None:
            input_["consumer_region"] = consumer_region
        if allow_writes is not None:
            input_["allow_writes"] = allow_writes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def authorize_cluster_security_group_ingress(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_security_group_name: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        cidrip: Optional["capo_redshift.types.string.String"] = None,
        ec2_security_group_name: Optional["capo_redshift.types.string.String"] = None,
        ec2_security_group_owner_id: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> "capo_redshift.types.authorize_cluster_security_group_ingress_result.AuthorizeClusterSecurityGroupIngressResult":
        """<p>Adds an inbound (ingress) rule to an Amazon Redshift security group. Depending on whether the application accessing your cluster is running on the Internet or an Amazon EC2 instance, you can authorize inbound access to either a Classless Interdomain Routing (CIDR)/Internet Protocol (IP) range or to an Amazon EC2 security group. You can add as many as 20 ingress rules to an Amazon Redshift security group.</p> <p>If you authorize access to an Amazon EC2 security group, specify <i>EC2SecurityGroupName</i> and <i>EC2SecurityGroupOwnerId</i>. The Amazon EC2 security group and Amazon Redshift cluster must be in the same Amazon Web Services Region. </p> <p>If you authorize access to a CIDR/IP address range, specify <i>CIDRIP</i>. For an overview of CIDR blocks, see the Wikipedia article on <a href="http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">Classless Inter-Domain Routing</a>. </p> <p>You must also associate the security group with a cluster so that clients running on these IP addresses or the EC2 instance are authorized to connect to the cluster. For information about managing security groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html">Working with Security Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            cluster_security_group_name: <p>The name of the security group to which the ingress rule is added.</p>
            cidrip: <p>The IP range to be added the Amazon Redshift security group.</p>
            ec2_security_group_name: <p>The EC2 security group to be added the Amazon Redshift security group.</p>
            ec2_security_group_owner_id: <p>The Amazon Web Services account number of the owner of the security group specified by the <i>EC2SecurityGroupName</i> parameter. The Amazon Web Services Access Key ID is not an acceptable value. </p> <p>Example: <code>111122223333</code> </p>

        Raises:
            capo_redshift.errors.authorization_already_exists_fault.AuthorizationAlreadyExistsFault: <p>The specified CIDR block or EC2 security group is already authorized for the specified cluster security group.</p>
            capo_redshift.errors.authorization_quota_exceeded_fault.AuthorizationQuotaExceededFault: <p>The authorization quota for the cluster security group has been reached.</p>
            capo_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault: <p>The cluster security group name does not refer to an existing cluster security group.</p>
            capo_redshift.errors.invalid_cluster_security_group_state_fault.InvalidClusterSecurityGroupStateFault: <p>The state of the cluster security group is not <code>available</code>. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.authorize_cluster_security_group_ingress_message.AuthorizeClusterSecurityGroupIngressMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.authorize_cluster_security_group_ingress_result.AuthorizeClusterSecurityGroupIngressResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.authorize_cluster_security_group_ingress

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.authorize_cluster_security_group_ingress.async_authorize_cluster_security_group_ingress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.authorize_cluster_security_group_ingress_message.AuthorizeClusterSecurityGroupIngressMessage = {}
        if cluster_security_group_name is not None:
            input_["cluster_security_group_name"] = cluster_security_group_name
        if cidrip is not None:
            input_["cidrip"] = cidrip
        if ec2_security_group_name is not None:
            input_["ec2_security_group_name"] = ec2_security_group_name
        if ec2_security_group_owner_id is not None:
            input_["ec2_security_group_owner_id"] = ec2_security_group_owner_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def authorize_data_share(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        data_share_arn: Optional["capo_redshift.types.string.String"] = None,
        consumer_identifier: Optional["capo_redshift.types.string.String"] = None,
        allow_writes: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_redshift.types.data_share.DataShare":
        """<p>From a data producer account, authorizes the sharing of a datashare with one or more consumer accounts or managing entities. To authorize a datashare for a data consumer, the producer account must have the correct access permissions.</p>

        Args:
            data_share_arn: <p>The Amazon Resource Name (ARN) of the datashare namespace that producers are to authorize sharing for.</p>
            consumer_identifier: <p>The identifier of the data consumer that is authorized to access the datashare. This identifier is an Amazon Web Services account ID or a keyword, such as ADX.</p>
            allow_writes: <p>If set to true, allows write operations for a datashare.</p>

        Raises:
            capo_redshift.errors.invalid_data_share_fault.InvalidDataShareFault: <p>There is an error with the datashare.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.authorize_data_share_message.AuthorizeDataShareMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.data_share.DataShare"]:
            import capo_redshift._operations.redshift_service_version20121201.authorize_data_share

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.authorize_data_share.async_authorize_data_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.authorize_data_share_message.AuthorizeDataShareMessage = {}
        if data_share_arn is not None:
            input_["data_share_arn"] = data_share_arn
        if consumer_identifier is not None:
            input_["consumer_identifier"] = consumer_identifier
        if allow_writes is not None:
            input_["allow_writes"] = allow_writes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def authorize_endpoint_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        account: Optional["capo_redshift.types.string.String"] = None,
        vpc_ids: Optional[
            "capo_redshift.types.vpc_identifier_list.VpcIdentifierList"
        ] = None,
    ) -> "capo_redshift.types.endpoint_authorization.EndpointAuthorization":
        """<p>Grants access to a cluster.</p>

        Args:
            cluster_identifier: <p>The cluster identifier of the cluster to grant access to.</p>
            account: <p>The Amazon Web Services account ID to grant access to.</p>
            vpc_ids: <p>The virtual private cloud (VPC) identifiers to grant access to.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.endpoint_authorization_already_exists_fault.EndpointAuthorizationAlreadyExistsFault: <p>The authorization already exists for this endpoint.</p>
            capo_redshift.errors.endpoint_authorizations_per_cluster_limit_exceeded_fault.EndpointAuthorizationsPerClusterLimitExceededFault: <p>The number of endpoint authorizations per cluster has exceeded its limit.</p>
            capo_redshift.errors.invalid_authorization_state_fault.InvalidAuthorizationStateFault: <p>The status of the authorization is not valid.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.authorize_endpoint_access_message.AuthorizeEndpointAccessMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.endpoint_authorization.EndpointAuthorization"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.authorize_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.authorize_endpoint_access.async_authorize_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.authorize_endpoint_access_message.AuthorizeEndpointAccessMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if account is not None:
            input_["account"] = account
        if vpc_ids is not None:
            input_["vpc_ids"] = vpc_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def authorize_snapshot_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_arn: Optional["capo_redshift.types.string.String"] = None,
        snapshot_cluster_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        account_with_restore_access: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> "capo_redshift.types.authorize_snapshot_access_result.AuthorizeSnapshotAccessResult":
        """<p>Authorizes the specified Amazon Web Services account to restore the specified snapshot.</p> <p> For more information about working with snapshots, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html">Amazon Redshift Snapshots</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            snapshot_identifier: <p>The identifier of the snapshot the account is authorized to restore.</p>
            snapshot_arn: <p>The Amazon Resource Name (ARN) of the snapshot to authorize access to.</p>
            snapshot_cluster_identifier: <p>The identifier of the cluster the snapshot was created from.</p> <ul> <li> <p> <i>If the snapshot to access doesn't exist and the associated IAM policy doesn't allow access to all (*) snapshots</i> - This parameter is required. Otherwise, permissions aren't available to check if the snapshot exists.</p> </li> <li> <p> <i>If the snapshot to access exists</i> - This parameter isn't required. Redshift can retrieve the cluster identifier and use it to validate snapshot authorization.</p> </li> </ul>
            account_with_restore_access: <p>The identifier of the Amazon Web Services account authorized to restore the specified snapshot.</p> <p>To share a snapshot with Amazon Web Services Support, specify amazon-redshift-support.</p>

        Raises:
            capo_redshift.errors.authorization_already_exists_fault.AuthorizationAlreadyExistsFault: <p>The specified CIDR block or EC2 security group is already authorized for the specified cluster security group.</p>
            capo_redshift.errors.authorization_quota_exceeded_fault.AuthorizationQuotaExceededFault: <p>The authorization quota for the cluster security group has been reached.</p>
            capo_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault: <p>The snapshot identifier does not refer to an existing cluster snapshot.</p>
            capo_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault: <p>The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.</p>
            capo_redshift.errors.invalid_cluster_snapshot_state_fault.InvalidClusterSnapshotStateFault: <p>The specified cluster snapshot is not in the <code>available</code> state, or other accounts are authorized to access the snapshot. </p>
            capo_redshift.errors.limit_exceeded_fault.LimitExceededFault: <p>The encryption key has exceeded its grant limit in Amazon Web Services KMS.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.authorize_snapshot_access_message.AuthorizeSnapshotAccessMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.authorize_snapshot_access_result.AuthorizeSnapshotAccessResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.authorize_snapshot_access

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.authorize_snapshot_access.async_authorize_snapshot_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.authorize_snapshot_access_message.AuthorizeSnapshotAccessMessage = {}
        if snapshot_identifier is not None:
            input_["snapshot_identifier"] = snapshot_identifier
        if snapshot_arn is not None:
            input_["snapshot_arn"] = snapshot_arn
        if snapshot_cluster_identifier is not None:
            input_["snapshot_cluster_identifier"] = snapshot_cluster_identifier
        if account_with_restore_access is not None:
            input_["account_with_restore_access"] = account_with_restore_access

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_cluster_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        identifiers: Optional[
            "capo_redshift.types.delete_cluster_snapshot_message_list.DeleteClusterSnapshotMessageList"
        ] = None,
    ) -> "capo_redshift.types.batch_delete_cluster_snapshots_result.BatchDeleteClusterSnapshotsResult":
        """<p>Deletes a set of cluster snapshots.</p>

        Args:
            identifiers: <p>A list of identifiers for the snapshots that you want to delete.</p>

        Raises:
            capo_redshift.errors.batch_delete_request_size_exceeded_fault.BatchDeleteRequestSizeExceededFault: <p>The maximum number for a batch delete of snapshots has been reached. The limit is 100. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.batch_delete_cluster_snapshots_request.BatchDeleteClusterSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.batch_delete_cluster_snapshots_result.BatchDeleteClusterSnapshotsResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.batch_delete_cluster_snapshots

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.batch_delete_cluster_snapshots.async_batch_delete_cluster_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.batch_delete_cluster_snapshots_request.BatchDeleteClusterSnapshotsRequest = {}
        if identifiers is not None:
            input_["identifiers"] = identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_modify_cluster_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        snapshot_identifier_list: Optional[
            "capo_redshift.types.snapshot_identifier_list.SnapshotIdentifierList"
        ] = None,
        manual_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        force: Optional["capo_redshift.types.boolean.Boolean"] = None,
    ) -> "capo_redshift.types.batch_modify_cluster_snapshots_output_message.BatchModifyClusterSnapshotsOutputMessage":
        """<p>Modifies the settings for a set of cluster snapshots.</p>

        Args:
            snapshot_identifier_list: <p>A list of snapshot identifiers you want to modify.</p>
            manual_snapshot_retention_period: <p>The number of days that a manual snapshot is retained. If you specify the value -1, the manual snapshot is retained indefinitely.</p> <p>The number must be either -1 or an integer between 1 and 3,653.</p> <p>If you decrease the manual snapshot retention period from its current value, existing manual snapshots that fall outside of the new retention period will return an error. If you want to suppress the errors and delete the snapshots, use the force option. </p>
            force: <p>A boolean value indicating whether to override an exception if the retention period has passed. </p>

        Raises:
            capo_redshift.errors.batch_modify_cluster_snapshots_limit_exceeded_fault.BatchModifyClusterSnapshotsLimitExceededFault: <p>The maximum number for snapshot identifiers has been reached. The limit is 100. </p>
            capo_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault: <p>The retention period specified is either in the past or is not a valid value.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.batch_modify_cluster_snapshots_message.BatchModifyClusterSnapshotsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.batch_modify_cluster_snapshots_output_message.BatchModifyClusterSnapshotsOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.batch_modify_cluster_snapshots

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.batch_modify_cluster_snapshots.async_batch_modify_cluster_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.batch_modify_cluster_snapshots_message.BatchModifyClusterSnapshotsMessage = {}
        if snapshot_identifier_list is not None:
            input_["snapshot_identifier_list"] = snapshot_identifier_list
        if manual_snapshot_retention_period is not None:
            input_["manual_snapshot_retention_period"] = (
                manual_snapshot_retention_period
            )
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_resize(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.resize_progress_message.ResizeProgressMessage":
        """<p>Cancels a resize operation for a cluster.</p>

        Args:
            cluster_identifier: <p>The unique identifier for the cluster that you want to cancel a resize operation for.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.resize_not_found_fault.ResizeNotFoundFault: <p>A resize operation for the specified cluster is not found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.cancel_resize_message.CancelResizeMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.resize_progress_message.ResizeProgressMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.cancel_resize

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.cancel_resize.async_cancel_resize(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.cancel_resize_message.CancelResizeMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def copy_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        source_snapshot_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        source_snapshot_cluster_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        target_snapshot_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        manual_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_redshift.types.copy_cluster_snapshot_result.CopyClusterSnapshotResult":
        """<p>Copies the specified automated cluster snapshot to a new manual cluster snapshot. The source must be an automated snapshot and it must be in the available state.</p> <p>When you delete a cluster, Amazon Redshift deletes any automated snapshots of the cluster. Also, when the retention period of the snapshot expires, Amazon Redshift automatically deletes it. If you want to keep an automated snapshot for a longer period, you can make a manual copy of the snapshot. Manual snapshots are retained until you delete them.</p> <p> For more information about working with snapshots, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html">Amazon Redshift Snapshots</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            source_snapshot_identifier: <p>The identifier for the source snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Must be the identifier for a valid automated snapshot whose state is <code>available</code>.</p> </li> </ul>
            source_snapshot_cluster_identifier: <p>The identifier of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.</p> <p>Constraints:</p> <ul> <li> <p>Must be the identifier for a valid cluster.</p> </li> </ul>
            target_snapshot_identifier: <p>The identifier given to the new manual snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Cannot be null, empty, or blank.</p> </li> <li> <p>Must contain from 1 to 255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique for the Amazon Web Services account that is making the request.</p> </li> </ul>
            manual_snapshot_retention_period: <p>The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. </p> <p>The value must be either -1 or an integer between 1 and 3,653.</p> <p>The default value is -1.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.cluster_snapshot_already_exists_fault.ClusterSnapshotAlreadyExistsFault: <p>The value specified as a snapshot identifier is already used by an existing snapshot.</p>
            capo_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault: <p>The snapshot identifier does not refer to an existing cluster snapshot.</p>
            capo_redshift.errors.cluster_snapshot_quota_exceeded_fault.ClusterSnapshotQuotaExceededFault: <p>The request would result in the user exceeding the allowed number of cluster snapshots.</p>
            capo_redshift.errors.invalid_cluster_snapshot_state_fault.InvalidClusterSnapshotStateFault: <p>The specified cluster snapshot is not in the <code>available</code> state, or other accounts are authorized to access the snapshot. </p>
            capo_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault: <p>The retention period specified is either in the past or is not a valid value.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.copy_cluster_snapshot_message.CopyClusterSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.copy_cluster_snapshot_result.CopyClusterSnapshotResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.copy_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.copy_cluster_snapshot.async_copy_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.copy_cluster_snapshot_message.CopyClusterSnapshotMessage = {}
        if source_snapshot_identifier is not None:
            input_["source_snapshot_identifier"] = source_snapshot_identifier
        if source_snapshot_cluster_identifier is not None:
            input_["source_snapshot_cluster_identifier"] = (
                source_snapshot_cluster_identifier
            )
        if target_snapshot_identifier is not None:
            input_["target_snapshot_identifier"] = target_snapshot_identifier
        if manual_snapshot_retention_period is not None:
            input_["manual_snapshot_retention_period"] = (
                manual_snapshot_retention_period
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_authentication_profile(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        authentication_profile_name: Optional[
            "capo_redshift.types.authentication_profile_name_string.AuthenticationProfileNameString"
        ] = None,
        authentication_profile_content: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> "capo_redshift.types.create_authentication_profile_result.CreateAuthenticationProfileResult":
        """<p>Creates an authentication profile with the specified parameters.</p>

        Args:
            authentication_profile_name: <p>The name of the authentication profile to be created.</p>
            authentication_profile_content: <p>The content of the authentication profile in JSON format. The maximum length of the JSON string is determined by a quota for your account.</p>

        Raises:
            capo_redshift.errors.authentication_profile_already_exists_fault.AuthenticationProfileAlreadyExistsFault: <p>The authentication profile already exists.</p>
            capo_redshift.errors.authentication_profile_quota_exceeded_fault.AuthenticationProfileQuotaExceededFault: <p>The size or number of authentication profiles has exceeded the quota. The maximum length of the JSON string and maximum number of authentication profiles is determined by a quota for your account.</p>
            capo_redshift.errors.invalid_authentication_profile_request_fault.InvalidAuthenticationProfileRequestFault: <p>The authentication profile request is not valid. The profile name can't be null or empty. The authentication profile API operation must be available in the Amazon Web Services Region.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_authentication_profile_message.CreateAuthenticationProfileMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_authentication_profile_result.CreateAuthenticationProfileResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_authentication_profile

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_authentication_profile.async_create_authentication_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_authentication_profile_message.CreateAuthenticationProfileMessage = {}
        if authentication_profile_name is not None:
            input_["authentication_profile_name"] = authentication_profile_name
        if authentication_profile_content is not None:
            input_["authentication_profile_content"] = authentication_profile_content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cluster(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        db_name: Optional["capo_redshift.types.string.String"] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        cluster_type: Optional["capo_redshift.types.string.String"] = None,
        node_type: Optional["capo_redshift.types.string.String"] = None,
        master_username: Optional["capo_redshift.types.string.String"] = None,
        master_user_password: Optional[
            "capo_redshift.types.sensitive_string.SensitiveString"
        ] = None,
        cluster_security_groups: Optional[
            "capo_redshift.types.cluster_security_group_name_list.ClusterSecurityGroupNameList"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_redshift.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        cluster_subnet_group_name: Optional["capo_redshift.types.string.String"] = None,
        availability_zone: Optional["capo_redshift.types.string.String"] = None,
        preferred_maintenance_window: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        cluster_parameter_group_name: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        automated_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        manual_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        port: Optional["capo_redshift.types.integer_optional.IntegerOptional"] = None,
        cluster_version: Optional["capo_redshift.types.string.String"] = None,
        allow_version_upgrade: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        number_of_nodes: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        publicly_accessible: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        encrypted: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        hsm_client_certificate_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        hsm_configuration_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        elastic_ip: Optional["capo_redshift.types.string.String"] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
        kms_key_id: Optional["capo_redshift.types.string.String"] = None,
        enhanced_vpc_routing: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        additional_info: Optional["capo_redshift.types.string.String"] = None,
        iam_roles: Optional[
            "capo_redshift.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        maintenance_track_name: Optional["capo_redshift.types.string.String"] = None,
        snapshot_schedule_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        availability_zone_relocation: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        aqua_configuration_status: Optional[
            "capo_redshift.types.aqua_configuration_status.AquaConfigurationStatus"
        ] = None,
        default_iam_role_arn: Optional["capo_redshift.types.string.String"] = None,
        load_sample_data: Optional["capo_redshift.types.string.String"] = None,
        manage_master_password: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        master_password_secret_kms_key_id: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        ip_address_type: Optional["capo_redshift.types.string.String"] = None,
        multi_az: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        redshift_idc_application_arn: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        catalog_name: Optional[
            "capo_redshift.types.catalog_name_string.CatalogNameString"
        ] = None,
        extra_compute_for_automatic_optimization: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_redshift.types.create_cluster_result.CreateClusterResult":
        r"""<p>Creates a new cluster with the specified parameters.</p> <p>To create a cluster in Virtual Private Cloud (VPC), you must provide a cluster subnet group name. The cluster subnet group identifies the subnets of your VPC that Amazon Redshift uses when creating the cluster. For more information about managing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html">Amazon Redshift Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a subnet group for a provisioned cluster is in an account with VPC BPA turned on, the following capabilities are blocked:</p> <ul> <li> <p>Creating a public cluster</p> </li> <li> <p>Restoring a public cluster</p> </li> <li> <p>Modifying a private cluster to be public</p> </li> <li> <p>Adding a subnet with VPC BPA turned on to the subnet group when there's at least one public cluster within the group</p> </li> </ul> <p>For more information about VPC BPA, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html">Block public access to VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            db_name: <p>The name of the first database to be created when the cluster is created.</p> <p>To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to <a href="https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html">Create a Database</a> in the Amazon Redshift Database Developer Guide. </p> <p>Default: <code>dev</code> </p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 64 alphanumeric characters.</p> </li> <li> <p>Must contain only lowercase letters.</p> </li> <li> <p>Cannot be a word that is reserved by the service. A list of reserved words can be found in <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html">Reserved Words</a> in the Amazon Redshift Database Developer Guide. </p> </li> </ul>
            cluster_identifier: <p>A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>Alphabetic characters must be lowercase.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique for all clusters within an Amazon Web Services account.</p> </li> </ul> <p>Example: <code>myexamplecluster</code> </p>
            cluster_type: <p>The type of the cluster. When cluster type is specified as</p> <ul> <li> <p> <code>single-node</code>, the <b>NumberOfNodes</b> parameter is not required.</p> </li> <li> <p> <code>multi-node</code>, the <b>NumberOfNodes</b> parameter is required.</p> </li> </ul> <p>Valid Values: <code>multi-node</code> | <code>single-node</code> </p> <p>Default: <code>multi-node</code> </p>
            node_type: <p>The node type to be provisioned for the cluster. For information about node types, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes"> Working with Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p> <p>Valid Values: <code>dc2.large</code> | <code>dc2.8xlarge</code> | <code>rg.large</code> | <code>rg.xlarge</code> | <code>rg.4xlarge</code> | <code>rg.12xlarge</code> | <code>ra3.large</code> | <code>ra3.xlplus</code> | <code>ra3.4xlarge</code> | <code>ra3.16xlarge</code> </p>
            master_username: <p>The user name associated with the admin user account for the cluster that is being created.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 - 128 alphanumeric characters or hyphens. The user name can't be <code>PUBLIC</code>.</p> </li> <li> <p>Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Must not contain a colon (:) or a slash (/).</p> </li> <li> <p>Cannot be a reserved word. A list of reserved words can be found in <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html">Reserved Words</a> in the Amazon Redshift Database Developer Guide. </p> </li> </ul>
            master_user_password: <p>The password associated with the admin user account for the cluster that is being created.</p> <p>You can't use <code>MasterUserPassword</code> if <code>ManageMasterPassword</code> is <code>true</code>.</p> <p>Constraints:</p> <ul> <li> <p>Must be between 8 and 64 characters in length.</p> </li> <li> <p>Must contain at least one uppercase letter.</p> </li> <li> <p>Must contain at least one lowercase letter.</p> </li> <li> <p>Must contain one number.</p> </li> <li> <p>Can be any printable ASCII character (ASCII code 33-126) except <code>'</code> (single quote), <code>"</code> (double quote), <code>\</code>, <code>/</code>, or <code>@</code>.</p> </li> </ul>
            cluster_security_groups: <p>A list of security groups to be associated with this cluster.</p> <p>Default: The default cluster security group for Amazon Redshift.</p>
            vpc_security_group_ids: <p>A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.</p> <p>Default: The default VPC security group is associated with the cluster.</p>
            cluster_subnet_group_name: <p>The name of a cluster subnet group to be associated with this cluster.</p> <p>If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).</p>
            availability_zone: <p>The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.</p> <p>Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint.</p> <p>Example: <code>us-east-2d</code> </p> <p>Constraint: The specified Availability Zone must be in the same region as the current endpoint.</p>
            preferred_maintenance_window: <p>The weekly time range (in UTC) during which automated cluster maintenance can occur.</p> <p> Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p> Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows">Maintenance Windows</a> in Amazon Redshift Cluster Management Guide.</p> <p>Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun</p> <p>Constraints: Minimum 30-minute window.</p>
            cluster_parameter_group_name: <p>The name of the parameter group to be associated with this cluster.</p> <p>Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Working with Amazon Redshift Parameter Groups</a> </p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            automated_snapshot_retention_period: <p>The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with <a>CreateClusterSnapshot</a>. </p> <p>You can't disable automated snapshots for RG or RA3 node types. Set the automated retention period from 1-35 days.</p> <p>Default: <code>1</code> </p> <p>Constraints: Must be a value from 0 to 35.</p>
            manual_snapshot_retention_period: <p>The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            port: <p>The port number on which the cluster accepts incoming connections.</p> <p>The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections.</p> <p>Default: <code>5439</code> </p> <p>Valid Values: </p> <ul> <li> <p>For clusters with RG or RA3 nodes - Select a port within the ranges <code>5431-5455</code> or <code>8191-8215</code>. (If you have an existing cluster with RG or RA3 nodes, it isn't required that you change the port to these ranges.)</p> </li> <li> <p>For clusters with dc2 nodes - Select a port within the range <code>1150-65535</code>.</p> </li> </ul>
            cluster_version: <p>The version of the Amazon Redshift engine software that you want to deploy on the cluster.</p> <p>The version selected runs on all the nodes in the cluster.</p> <p>Constraints: Only version 1.0 is currently available.</p> <p>Example: <code>1.0</code> </p>
            allow_version_upgrade: <p>If <code>true</code>, major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.</p> <p>When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster.</p> <p>Default: <code>true</code> </p>
            number_of_nodes: <p>The number of compute nodes in the cluster. This parameter is required when the <b>ClusterType</b> parameter is specified as <code>multi-node</code>. </p> <p>For information about determining how many nodes you need, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes"> Working with Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p> <p>If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster.</p> <p>Default: <code>1</code> </p> <p>Constraints: Value must be at least 1 and no more than 100.</p>
            publicly_accessible: <p>If <code>true</code>, the cluster can be accessed from a public network. </p> <p>Default: false</p>
            encrypted: <p>If <code>true</code>, the data in the cluster is encrypted at rest. If you set the value on this parameter to <code>false</code>, the request will fail.</p> <p>Default: true</p>
            hsm_client_certificate_identifier: <p>Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.</p>
            hsm_configuration_identifier: <p>Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.</p>
            elastic_ip: <p>The Elastic IP (EIP) address for the cluster.</p> <p>Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. Don't specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on. For more information about provisioning clusters in EC2-VPC, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms">Supported Platforms to Launch Your Cluster</a> in the Amazon Redshift Cluster Management Guide.</p>
            tags: <p>A list of tag instances.</p>
            kms_key_id: <p>The Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.</p>
            enhanced_vpc_routing: <p>An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html">Enhanced VPC Routing</a> in the Amazon Redshift Cluster Management Guide.</p> <p>If this option is <code>true</code>, enhanced VPC routing is enabled. </p> <p>Default: false</p>
            additional_info: <p>Reserved.</p>
            iam_roles: <p>A list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. </p> <p>The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Quotas and limits</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>
            maintenance_track_name: <p>An optional parameter for the name of the maintenance track for the cluster. If you don't provide a maintenance track name, the cluster is assigned to the <code>current</code> track.</p>
            snapshot_schedule_identifier: <p>A unique identifier for the snapshot schedule.</p>
            availability_zone_relocation: <p>The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.</p>
            aqua_configuration_status: <p>This parameter is retired. It does not set the AQUA configuration status. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was created. </p>
            load_sample_data: <p>A flag that specifies whether to load sample data once the cluster is created.</p>
            manage_master_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage this cluster's admin credentials. You can't use <code>MasterUserPassword</code> if <code>ManageMasterPassword</code> is true. If <code>ManageMasterPassword</code> is false or not set, Amazon Redshift uses <code>MasterUserPassword</code> for the admin user account's password. </p>
            master_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret. You can only use this parameter if <code>ManageMasterPassword</code> is true.</p>
            ip_address_type: <p>The IP address types that the cluster supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>
            multi_az: <p>If true, Amazon Redshift will deploy the cluster in two Availability Zones (AZ).</p>
            redshift_idc_application_arn: <p>The Amazon resource name (ARN) of the Amazon Redshift IAM Identity Center application.</p>
            catalog_name: <p>The name of the Glue data catalog that will be associated with the cluster enabled with Amazon Redshift federated permissions.</p> <p>Constraints:</p> <ul> <li> <p>Must contain at least one lowercase letter.</p> </li> <li> <p>Can only contain lowercase letters (a-z), numbers (0-9), underscores (_), and hyphens (-).</p> </li> </ul> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p> <p>Example: <code>my-catalog_01</code> </p>
            extra_compute_for_automatic_optimization: <p>If <code>true</code>, allocates additional compute resources for running automatic optimization operations.</p> <p>Default: false</p>

        Raises:
            capo_redshift.errors.cluster_already_exists_fault.ClusterAlreadyExistsFault: <p>The account already has a cluster with the given identifier.</p>
            capo_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault: <p>The parameter group name does not refer to an existing parameter group.</p>
            capo_redshift.errors.cluster_quota_exceeded_fault.ClusterQuotaExceededFault: <p>The request would exceed the allowed number of cluster instances for this account. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault: <p>The cluster security group name does not refer to an existing cluster security group.</p>
            capo_redshift.errors.cluster_subnet_group_not_found_fault.ClusterSubnetGroupNotFoundFault: <p>The cluster subnet group name does not refer to an existing cluster subnet group.</p>
            capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault: <p>A dependent service denied access for the integration.</p>
            capo_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault: <p>The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.hsm_client_certificate_not_found_fault.HsmClientCertificateNotFoundFault: <p>There is no Amazon Redshift HSM client certificate with the specified identifier.</p>
            capo_redshift.errors.hsm_configuration_not_found_fault.HsmConfigurationNotFoundFault: <p>There is no Amazon Redshift HSM configuration with the specified identifier.</p>
            capo_redshift.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault: <p>The number of nodes specified exceeds the allotted capacity of the cluster.</p>
            capo_redshift.errors.invalid_cluster_subnet_group_state_fault.InvalidClusterSubnetGroupStateFault: <p>The cluster subnet group cannot be deleted because it is in use.</p>
            capo_redshift.errors.invalid_cluster_track_fault.InvalidClusterTrackFault: <p>The provided cluster track name is not valid.</p>
            capo_redshift.errors.invalid_elastic_ip_fault.InvalidElasticIpFault: <p>The Elastic IP (EIP) is invalid or cannot be found.</p>
            capo_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault: <p>The retention period specified is either in the past or is not a valid value.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            capo_redshift.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is not valid, or not all of the subnets are in the same VPC.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The cluster subnet group does not cover all Availability Zones.</p>
            capo_redshift.errors.ipv6_cidr_block_not_found_fault.Ipv6CidrBlockNotFoundFault: <p>There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack mode, associate an IPv6 CIDR block with each subnet in your VPC.</p>
            capo_redshift.errors.limit_exceeded_fault.LimitExceededFault: <p>The encryption key has exceeded its grant limit in Amazon Web Services KMS.</p>
            capo_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault.NumberOfNodesPerClusterLimitExceededFault: <p>The operation would exceed the number of nodes allowed for a cluster.</p>
            capo_redshift.errors.number_of_nodes_quota_exceeded_fault.NumberOfNodesQuotaExceededFault: <p>The operation would exceed the number of nodes allotted to the account. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.redshift_idc_application_not_exists_fault.RedshiftIdcApplicationNotExistsFault: <p>The application you attempted to find doesn't exist.</p>
            capo_redshift.errors.snapshot_schedule_not_found_fault.SnapshotScheduleNotFoundFault: <p>We could not find the specified snapshot schedule. </p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_cluster_message.CreateClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_cluster_result.CreateClusterResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_cluster

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_cluster_message.CreateClusterMessage = {}
        if db_name is not None:
            input_["db_name"] = db_name
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if cluster_type is not None:
            input_["cluster_type"] = cluster_type
        if node_type is not None:
            input_["node_type"] = node_type
        if master_username is not None:
            input_["master_username"] = master_username
        if master_user_password is not None:
            input_["master_user_password"] = master_user_password
        if cluster_security_groups is not None:
            input_["cluster_security_groups"] = cluster_security_groups
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if cluster_subnet_group_name is not None:
            input_["cluster_subnet_group_name"] = cluster_subnet_group_name
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if cluster_parameter_group_name is not None:
            input_["cluster_parameter_group_name"] = cluster_parameter_group_name
        if automated_snapshot_retention_period is not None:
            input_["automated_snapshot_retention_period"] = (
                automated_snapshot_retention_period
            )
        if manual_snapshot_retention_period is not None:
            input_["manual_snapshot_retention_period"] = (
                manual_snapshot_retention_period
            )
        if port is not None:
            input_["port"] = port
        if cluster_version is not None:
            input_["cluster_version"] = cluster_version
        if allow_version_upgrade is not None:
            input_["allow_version_upgrade"] = allow_version_upgrade
        if number_of_nodes is not None:
            input_["number_of_nodes"] = number_of_nodes
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if encrypted is not None:
            input_["encrypted"] = encrypted
        if hsm_client_certificate_identifier is not None:
            input_["hsm_client_certificate_identifier"] = (
                hsm_client_certificate_identifier
            )
        if hsm_configuration_identifier is not None:
            input_["hsm_configuration_identifier"] = hsm_configuration_identifier
        if elastic_ip is not None:
            input_["elastic_ip"] = elastic_ip
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if enhanced_vpc_routing is not None:
            input_["enhanced_vpc_routing"] = enhanced_vpc_routing
        if additional_info is not None:
            input_["additional_info"] = additional_info
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if maintenance_track_name is not None:
            input_["maintenance_track_name"] = maintenance_track_name
        if snapshot_schedule_identifier is not None:
            input_["snapshot_schedule_identifier"] = snapshot_schedule_identifier
        if availability_zone_relocation is not None:
            input_["availability_zone_relocation"] = availability_zone_relocation
        if aqua_configuration_status is not None:
            input_["aqua_configuration_status"] = aqua_configuration_status
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if load_sample_data is not None:
            input_["load_sample_data"] = load_sample_data
        if manage_master_password is not None:
            input_["manage_master_password"] = manage_master_password
        if master_password_secret_kms_key_id is not None:
            input_["master_password_secret_kms_key_id"] = (
                master_password_secret_kms_key_id
            )
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if multi_az is not None:
            input_["multi_az"] = multi_az
        if redshift_idc_application_arn is not None:
            input_["redshift_idc_application_arn"] = redshift_idc_application_arn
        if catalog_name is not None:
            input_["catalog_name"] = catalog_name
        if extra_compute_for_automatic_optimization is not None:
            input_["extra_compute_for_automatic_optimization"] = (
                extra_compute_for_automatic_optimization
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        parameter_group_name: Optional["capo_redshift.types.string.String"] = None,
        parameter_group_family: Optional["capo_redshift.types.string.String"] = None,
        description: Optional["capo_redshift.types.string.String"] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
    ) -> "capo_redshift.types.create_cluster_parameter_group_result.CreateClusterParameterGroupResult":
        """<p>Creates an Amazon Redshift parameter group.</p> <p>Creating parameter groups is independent of creating clusters. You can associate a cluster with a parameter group when you create the cluster. You can also associate an existing cluster with a parameter group after the cluster is created by using <a>ModifyCluster</a>. </p> <p>Parameters in the parameter group define specific behavior that applies to the databases you create on the cluster. For more information about parameters and parameter groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Amazon Redshift Parameter Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            parameter_group_name: <p>The name of the cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters or hyphens</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique withing your Amazon Web Services account.</p> </li> </ul> <note> <p>This value is stored as a lower-case string.</p> </note>
            parameter_group_family: <p>The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.</p> <p>To get a list of valid parameter group family names, you can call <a>DescribeClusterParameterGroups</a>. By default, Amazon Redshift returns a list of all the parameter groups that are owned by your Amazon Web Services account, including the default parameter groups for each Amazon Redshift engine version. The parameter group family names associated with the default parameter groups provide you the valid values. For example, a valid family name is "redshift-1.0". </p>
            description: <p>A description of the parameter group.</p>
            tags: <p>A list of tag instances.</p>

        Raises:
            capo_redshift.errors.cluster_parameter_group_already_exists_fault.ClusterParameterGroupAlreadyExistsFault: <p>A cluster parameter group with the same name already exists.</p>
            capo_redshift.errors.cluster_parameter_group_quota_exceeded_fault.ClusterParameterGroupQuotaExceededFault: <p>The request would result in the user exceeding the allowed number of cluster parameter groups. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_cluster_parameter_group_message.CreateClusterParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_cluster_parameter_group_result.CreateClusterParameterGroupResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_cluster_parameter_group

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_cluster_parameter_group.async_create_cluster_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_cluster_parameter_group_message.CreateClusterParameterGroupMessage = {}
        if parameter_group_name is not None:
            input_["parameter_group_name"] = parameter_group_name
        if parameter_group_family is not None:
            input_["parameter_group_family"] = parameter_group_family
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

    async def create_cluster_security_group(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_security_group_name: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        description: Optional["capo_redshift.types.string.String"] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
    ) -> "capo_redshift.types.create_cluster_security_group_result.CreateClusterSecurityGroupResult":
        """<p>Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters.</p> <p> For information about managing security groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html">Amazon Redshift Cluster Security Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            cluster_security_group_name: <p>The name for the security group. Amazon Redshift stores the value as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain no more than 255 alphanumeric characters or hyphens.</p> </li> <li> <p>Must not be "Default".</p> </li> <li> <p>Must be unique for all security groups that are created by your Amazon Web Services account.</p> </li> </ul> <p>Example: <code>examplesecuritygroup</code> </p>
            description: <p>A description for the security group.</p>
            tags: <p>A list of tag instances.</p>

        Raises:
            capo_redshift.errors.cluster_security_group_already_exists_fault.ClusterSecurityGroupAlreadyExistsFault: <p>A cluster security group with the same name already exists.</p>
            capo_redshift.errors.cluster_security_group_quota_exceeded_fault.ClusterSecurityGroupQuotaExceededFault: <p>The request would result in the user exceeding the allowed number of cluster security groups. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_cluster_security_group_message.CreateClusterSecurityGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_cluster_security_group_result.CreateClusterSecurityGroupResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_cluster_security_group

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_cluster_security_group.async_create_cluster_security_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_cluster_security_group_message.CreateClusterSecurityGroupMessage = {}
        if cluster_security_group_name is not None:
            input_["cluster_security_group_name"] = cluster_security_group_name
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

    async def create_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        manual_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
    ) -> (
        "capo_redshift.types.create_cluster_snapshot_result.CreateClusterSnapshotResult"
    ):
        """<p>Creates a manual snapshot of the specified cluster. The cluster must be in the <code>available</code> state. </p> <p> For more information about working with snapshots, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html">Amazon Redshift Snapshots</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            snapshot_identifier: <p>A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the Amazon Web Services account.</p> <p>Constraints:</p> <ul> <li> <p>Cannot be null, empty, or blank</p> </li> <li> <p>Must contain from 1 to 255 alphanumeric characters or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-snapshot-id</code> </p>
            cluster_identifier: <p>The cluster identifier for which you want a snapshot.</p>
            manual_snapshot_retention_period: <p>The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. </p> <p>The value must be either -1 or an integer between 1 and 3,653.</p> <p>The default value is -1.</p>
            tags: <p>A list of tag instances.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.cluster_snapshot_already_exists_fault.ClusterSnapshotAlreadyExistsFault: <p>The value specified as a snapshot identifier is already used by an existing snapshot.</p>
            capo_redshift.errors.cluster_snapshot_quota_exceeded_fault.ClusterSnapshotQuotaExceededFault: <p>The request would result in the user exceeding the allowed number of cluster snapshots.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault: <p>The retention period specified is either in the past or is not a valid value.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_cluster_snapshot_message.CreateClusterSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_cluster_snapshot_result.CreateClusterSnapshotResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_cluster_snapshot.async_create_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_cluster_snapshot_message.CreateClusterSnapshotMessage = {}
        if snapshot_identifier is not None:
            input_["snapshot_identifier"] = snapshot_identifier
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if manual_snapshot_retention_period is not None:
            input_["manual_snapshot_retention_period"] = (
                manual_snapshot_retention_period
            )
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cluster_subnet_group(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_subnet_group_name: Optional["capo_redshift.types.string.String"] = None,
        description: Optional["capo_redshift.types.string.String"] = None,
        subnet_ids: Optional[
            "capo_redshift.types.subnet_identifier_list.SubnetIdentifierList"
        ] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
    ) -> "capo_redshift.types.create_cluster_subnet_group_result.CreateClusterSubnetGroupResult":
        """<p>Creates a new Amazon Redshift subnet group. You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud (Amazon VPC) when creating Amazon Redshift subnet group.</p> <p> For information about subnet groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html">Amazon Redshift Cluster Subnet Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            cluster_subnet_group_name: <p>The name for the subnet group. Amazon Redshift stores the value as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain no more than 255 alphanumeric characters or hyphens.</p> </li> <li> <p>Must not be "Default".</p> </li> <li> <p>Must be unique for all subnet groups that are created by your Amazon Web Services account.</p> </li> </ul> <p>Example: <code>examplesubnetgroup</code> </p>
            description: <p>A description for the subnet group.</p>
            subnet_ids: <p>An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.</p>
            tags: <p>A list of tag instances.</p>

        Raises:
            capo_redshift.errors.cluster_subnet_group_already_exists_fault.ClusterSubnetGroupAlreadyExistsFault: <p>A <i>ClusterSubnetGroupName</i> is already used by an existing cluster subnet group. </p>
            capo_redshift.errors.cluster_subnet_group_quota_exceeded_fault.ClusterSubnetGroupQuotaExceededFault: <p>The request would result in user exceeding the allowed number of cluster subnet groups. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.cluster_subnet_quota_exceeded_fault.ClusterSubnetQuotaExceededFault: <p>The request would result in user exceeding the allowed number of subnets in a cluster subnet groups. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault: <p>The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.</p>
            capo_redshift.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is not valid, or not all of the subnets are in the same VPC.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_cluster_subnet_group_message.CreateClusterSubnetGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_cluster_subnet_group_result.CreateClusterSubnetGroupResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_cluster_subnet_group

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_cluster_subnet_group.async_create_cluster_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_cluster_subnet_group_message.CreateClusterSubnetGroupMessage = {}
        if cluster_subnet_group_name is not None:
            input_["cluster_subnet_group_name"] = cluster_subnet_group_name
        if description is not None:
            input_["description"] = description
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_custom_domain_association(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        custom_domain_name: Optional[
            "capo_redshift.types.custom_domain_name_string.CustomDomainNameString"
        ] = None,
        custom_domain_certificate_arn: Optional[
            "capo_redshift.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
        ] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.create_custom_domain_association_result.CreateCustomDomainAssociationResult":
        """<p>Used to create a custom domain name for a cluster. Properties include the custom domain name, the cluster the custom domain is associated with, and the certificate Amazon Resource Name (ARN).</p>

        Args:
            custom_domain_name: <p>The custom domain name for a custom domain association.</p>
            custom_domain_certificate_arn: <p>The certificate Amazon Resource Name (ARN) for the custom domain name association.</p>
            cluster_identifier: <p>The cluster identifier that the custom domain is associated with.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.custom_cname_association_fault.CustomCnameAssociationFault: <p>An error occurred when an attempt was made to change the custom domain association.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_custom_domain_association_message.CreateCustomDomainAssociationMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_custom_domain_association_result.CreateCustomDomainAssociationResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_custom_domain_association

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_custom_domain_association.async_create_custom_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_custom_domain_association_message.CreateCustomDomainAssociationMessage = {}
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if custom_domain_certificate_arn is not None:
            input_["custom_domain_certificate_arn"] = custom_domain_certificate_arn
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_endpoint_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        resource_owner: Optional["capo_redshift.types.string.String"] = None,
        endpoint_name: Optional["capo_redshift.types.string.String"] = None,
        subnet_group_name: Optional["capo_redshift.types.string.String"] = None,
        vpc_security_group_ids: Optional[
            "capo_redshift.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
    ) -> "capo_redshift.types.endpoint_access.EndpointAccess":
        """<p>Creates a Redshift-managed VPC endpoint.</p>

        Args:
            cluster_identifier: <p>The cluster identifier of the cluster to access.</p>
            resource_owner: <p>The Amazon Web Services account ID of the owner of the cluster. This is only required if the cluster is in another Amazon Web Services account.</p>
            endpoint_name: <p>The Redshift-managed VPC endpoint name.</p> <p>An endpoint name must contain 1-30 characters. Valid characters are A-Z, a-z, 0-9, and hyphen(-). The first character must be a letter. The name can't contain two consecutive hyphens or end with a hyphen.</p>
            subnet_group_name: <p>The subnet group from which Amazon Redshift chooses the subnet to deploy the endpoint.</p>
            vpc_security_group_ids: <p>The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>

        Raises:
            capo_redshift.errors.access_to_cluster_denied_fault.AccessToClusterDeniedFault: <p>You are not authorized to access the cluster.</p>
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.cluster_subnet_group_not_found_fault.ClusterSubnetGroupNotFoundFault: <p>The cluster subnet group name does not refer to an existing cluster subnet group.</p>
            capo_redshift.errors.endpoint_already_exists_fault.EndpointAlreadyExistsFault: <p>The account already has a Redshift-managed VPC endpoint with the given identifier.</p>
            capo_redshift.errors.endpoints_per_authorization_limit_exceeded_fault.EndpointsPerAuthorizationLimitExceededFault: <p>The number of Redshift-managed VPC endpoints per authorization has exceeded its limit.</p>
            capo_redshift.errors.endpoints_per_cluster_limit_exceeded_fault.EndpointsPerClusterLimitExceededFault: <p>The number of Redshift-managed VPC endpoints per cluster has exceeded its limit.</p>
            capo_redshift.errors.invalid_cluster_security_group_state_fault.InvalidClusterSecurityGroupStateFault: <p>The state of the cluster security group is not <code>available</code>. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_endpoint_access_message.CreateEndpointAccessMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.endpoint_access.EndpointAccess"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_endpoint_access.async_create_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_endpoint_access_message.CreateEndpointAccessMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if endpoint_name is not None:
            input_["endpoint_name"] = endpoint_name
        if subnet_group_name is not None:
            input_["subnet_group_name"] = subnet_group_name
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_event_subscription(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        subscription_name: Optional["capo_redshift.types.string.String"] = None,
        sns_topic_arn: Optional["capo_redshift.types.string.String"] = None,
        source_type: Optional["capo_redshift.types.string.String"] = None,
        source_ids: Optional[
            "capo_redshift.types.source_ids_list.SourceIdsList"
        ] = None,
        event_categories: Optional[
            "capo_redshift.types.event_categories_list.EventCategoriesList"
        ] = None,
        severity: Optional["capo_redshift.types.string.String"] = None,
        enabled: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
    ) -> "capo_redshift.types.create_event_subscription_result.CreateEventSubscriptionResult":
        """<p>Creates an Amazon Redshift event notification subscription. This action requires an ARN (Amazon Resource Name) of an Amazon SNS topic created by either the Amazon Redshift console, the Amazon SNS console, or the Amazon SNS API. To obtain an ARN with Amazon SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.</p> <p>You can specify the source type, and lists of Amazon Redshift source IDs, event categories, and event severities. Notifications will be sent for all events you want that match those criteria. For example, you can specify source type = cluster, source ID = my-cluster-1 and mycluster2, event categories = Availability, Backup, and severity = ERROR. The subscription will only send notifications for those ERROR events in the Availability and Backup categories for the specified clusters.</p> <p>If you specify both the source type and source IDs, such as source type = cluster and source identifier = my-cluster-1, notifications will be sent for all the cluster events for my-cluster-1. If you specify a source type but do not specify a source identifier, you will receive notice of the events for the objects of that type in your Amazon Web Services account. If you do not specify either the SourceType nor the SourceIdentifier, you will be notified of events generated from all Amazon Redshift sources belonging to your Amazon Web Services account. You must specify a source type if you specify a source ID.</p>

        Args:
            subscription_name: <p>The name of the event subscription to be created.</p> <p>Constraints:</p> <ul> <li> <p>Cannot be null, empty, or blank.</p> </li> <li> <p>Must contain from 1 to 255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications. The ARN is created by Amazon SNS when you create a topic and subscribe to it.</p>
            source_type: <p>The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your Amazon Web Services account. You must specify a source type in order to specify source IDs.</p> <p>Valid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.</p>
            source_ids: <p>A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.</p> <p>Example: my-cluster-1, my-cluster-2</p> <p>Example: my-snapshot-20131010</p>
            event_categories: <p>Specifies the Amazon Redshift event categories to be published by the event notification subscription.</p> <p>Values: configuration, management, monitoring, security, pending</p>
            severity: <p>Specifies the Amazon Redshift event severity to be published by the event notification subscription.</p> <p>Values: ERROR, INFO</p>
            enabled: <p>A boolean value; set to <code>true</code> to activate the subscription, and set to <code>false</code> to create the subscription but not activate it. </p>
            tags: <p>A list of tag instances.</p>

        Raises:
            capo_redshift.errors.event_subscription_quota_exceeded_fault.EventSubscriptionQuotaExceededFault: <p>The request would exceed the allowed number of event subscriptions for this account. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.sns_invalid_topic_fault.SNSInvalidTopicFault: <p>Amazon SNS has responded that there is a problem with the specified Amazon SNS topic.</p>
            capo_redshift.errors.sns_no_authorization_fault.SNSNoAuthorizationFault: <p>You do not have permission to publish to the specified Amazon SNS topic.</p>
            capo_redshift.errors.sns_topic_arn_not_found_fault.SNSTopicArnNotFoundFault: <p>An Amazon SNS topic with the specified Amazon Resource Name (ARN) does not exist.</p>
            capo_redshift.errors.source_not_found_fault.SourceNotFoundFault: <p>The specified Amazon Redshift event source could not be found.</p>
            capo_redshift.errors.subscription_already_exist_fault.SubscriptionAlreadyExistFault: <p>There is already an existing event notification subscription with the specified name.</p>
            capo_redshift.errors.subscription_category_not_found_fault.SubscriptionCategoryNotFoundFault: <p>The value specified for the event category was not one of the allowed values, or it specified a category that does not apply to the specified source type. The allowed values are Configuration, Management, Monitoring, and Security.</p>
            capo_redshift.errors.subscription_event_id_not_found_fault.SubscriptionEventIdNotFoundFault: <p>An Amazon Redshift event with the specified event ID does not exist.</p>
            capo_redshift.errors.subscription_severity_not_found_fault.SubscriptionSeverityNotFoundFault: <p>The value specified for the event severity was not one of the allowed values, or it specified a severity that does not apply to the specified source type. The allowed values are ERROR and INFO.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_event_subscription_message.CreateEventSubscriptionMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_event_subscription_result.CreateEventSubscriptionResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_event_subscription

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_event_subscription.async_create_event_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_event_subscription_message.CreateEventSubscriptionMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if source_type is not None:
            input_["source_type"] = source_type
        if source_ids is not None:
            input_["source_ids"] = source_ids
        if event_categories is not None:
            input_["event_categories"] = event_categories
        if severity is not None:
            input_["severity"] = severity
        if enabled is not None:
            input_["enabled"] = enabled
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_hsm_client_certificate(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        hsm_client_certificate_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
    ) -> "capo_redshift.types.create_hsm_client_certificate_result.CreateHsmClientCertificateResult":
        """<p>Creates an HSM client certificate that an Amazon Redshift cluster will use to connect to the client's HSM in order to store and retrieve the keys used to encrypt the cluster databases.</p> <p>The command returns a public key, which you must store in the HSM. In addition to creating the HSM certificate, you must create an Amazon Redshift HSM configuration that provides a cluster the information needed to store and use encryption keys in the HSM. For more information, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM">Hardware Security Modules</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            hsm_client_certificate_identifier: <p>The identifier to be assigned to the new HSM client certificate that the cluster will use to connect to the HSM to use the database encryption keys.</p>
            tags: <p>A list of tag instances.</p>

        Raises:
            capo_redshift.errors.hsm_client_certificate_already_exists_fault.HsmClientCertificateAlreadyExistsFault: <p>There is already an existing Amazon Redshift HSM client certificate with the specified identifier.</p>
            capo_redshift.errors.hsm_client_certificate_quota_exceeded_fault.HsmClientCertificateQuotaExceededFault: <p>The quota for HSM client certificates has been reached. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_hsm_client_certificate_message.CreateHsmClientCertificateMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_hsm_client_certificate_result.CreateHsmClientCertificateResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_hsm_client_certificate

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_hsm_client_certificate.async_create_hsm_client_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_hsm_client_certificate_message.CreateHsmClientCertificateMessage = {}
        if hsm_client_certificate_identifier is not None:
            input_["hsm_client_certificate_identifier"] = (
                hsm_client_certificate_identifier
            )
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_hsm_configuration(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        hsm_configuration_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        description: Optional["capo_redshift.types.string.String"] = None,
        hsm_ip_address: Optional["capo_redshift.types.string.String"] = None,
        hsm_partition_name: Optional["capo_redshift.types.string.String"] = None,
        hsm_partition_password: Optional["capo_redshift.types.string.String"] = None,
        hsm_server_public_certificate: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
    ) -> "capo_redshift.types.create_hsm_configuration_result.CreateHsmConfigurationResult":
        """<p>Creates an HSM configuration that contains the information required by an Amazon Redshift cluster to store and use database encryption keys in a Hardware Security Module (HSM). After creating the HSM configuration, you can specify it as a parameter when creating a cluster. The cluster will then store its encryption keys in the HSM.</p> <p>In addition to creating an HSM configuration, you must also create an HSM client certificate. For more information, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-HSM.html">Hardware Security Modules</a> in the Amazon Redshift Cluster Management Guide.</p>

        Args:
            hsm_configuration_identifier: <p>The identifier to be assigned to the new Amazon Redshift HSM configuration.</p>
            description: <p>A text description of the HSM configuration to be created.</p>
            hsm_ip_address: <p>The IP address that the Amazon Redshift cluster must use to access the HSM.</p>
            hsm_partition_name: <p>The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.</p>
            hsm_partition_password: <p>The password required to access the HSM partition.</p>
            hsm_server_public_certificate: <p>The HSMs public certificate file. When using Cloud HSM, the file name is server.pem.</p>
            tags: <p>A list of tag instances.</p>

        Raises:
            capo_redshift.errors.hsm_configuration_already_exists_fault.HsmConfigurationAlreadyExistsFault: <p>There is already an existing Amazon Redshift HSM configuration with the specified identifier.</p>
            capo_redshift.errors.hsm_configuration_quota_exceeded_fault.HsmConfigurationQuotaExceededFault: <p>The quota for HSM configurations has been reached. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_hsm_configuration_message.CreateHsmConfigurationMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_hsm_configuration_result.CreateHsmConfigurationResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_hsm_configuration

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_hsm_configuration.async_create_hsm_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_hsm_configuration_message.CreateHsmConfigurationMessage = {}
        if hsm_configuration_identifier is not None:
            input_["hsm_configuration_identifier"] = hsm_configuration_identifier
        if description is not None:
            input_["description"] = description
        if hsm_ip_address is not None:
            input_["hsm_ip_address"] = hsm_ip_address
        if hsm_partition_name is not None:
            input_["hsm_partition_name"] = hsm_partition_name
        if hsm_partition_password is not None:
            input_["hsm_partition_password"] = hsm_partition_password
        if hsm_server_public_certificate is not None:
            input_["hsm_server_public_certificate"] = hsm_server_public_certificate
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_integration(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        source_arn: Optional["capo_redshift.types.source_arn.SourceArn"] = None,
        target_arn: Optional["capo_redshift.types.target_arn.TargetArn"] = None,
        integration_name: Optional[
            "capo_redshift.types.integration_name.IntegrationName"
        ] = None,
        kms_key_id: Optional["capo_redshift.types.string.String"] = None,
        tag_list: Optional["capo_redshift.types.tag_list.TagList"] = None,
        additional_encryption_context: Optional[
            "capo_redshift.types.encryption_context_map.EncryptionContextMap"
        ] = None,
        description: Optional[
            "capo_redshift.types.integration_description.IntegrationDescription"
        ] = None,
    ) -> "capo_redshift.types.integration.Integration":
        """<p>Creates a zero-ETL integration or S3 event integration with Amazon Redshift.</p>

        Args:
            source_arn: <p>The Amazon Resource Name (ARN) of the database to use as the source for replication.</p>
            target_arn: <p>The Amazon Resource Name (ARN) of the Amazon Redshift data warehouse to use as the target for replication.</p>
            integration_name: <p>The name of the integration.</p>
            kms_key_id: <p>An Key Management Service (KMS) key identifier for the key to use to encrypt the integration. If you don't specify an encryption key, the default Amazon Web Services owned key is used.</p>
            tag_list: <p>A list of tags.</p>
            additional_encryption_context: <p>An optional set of non-secret key–value pairs that contains additional contextual information about the data. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context">Encryption context</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p> <p>You can only include this parameter if you specify the <code>KMSKeyId</code> parameter.</p>
            description: <p>A description of the integration.</p>

        Raises:
            capo_redshift.errors.integration_already_exists_fault.IntegrationAlreadyExistsFault: <p>The integration you are trying to create already exists.</p>
            capo_redshift.errors.integration_conflict_operation_fault.IntegrationConflictOperationFault: <p>A conflicting conditional operation is currently in progress against this resource. This typically occurs when there are multiple requests being made to the same resource at the same time, and these requests conflict with each other.</p>
            capo_redshift.errors.integration_quota_exceeded_fault.IntegrationQuotaExceededFault: <p>You can't create any more zero-ETL or S3 event integrations because the quota has been reached.</p>
            capo_redshift.errors.integration_source_not_found_fault.IntegrationSourceNotFoundFault: <p>The specified integration source can't be found.</p>
            capo_redshift.errors.integration_target_not_found_fault.IntegrationTargetNotFoundFault: <p>The specified integration target can't be found.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_integration_message.CreateIntegrationMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.integration.Integration"]:
            import capo_redshift._operations.redshift_service_version20121201.create_integration

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_integration.async_create_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_integration_message.CreateIntegrationMessage = {}
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if target_arn is not None:
            input_["target_arn"] = target_arn
        if integration_name is not None:
            input_["integration_name"] = integration_name
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tag_list is not None:
            input_["tag_list"] = tag_list
        if additional_encryption_context is not None:
            input_["additional_encryption_context"] = additional_encryption_context
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_qev2_idc_application(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        idc_instance_arn: Optional["capo_redshift.types.string.String"] = None,
        qev2_idc_application_name: Optional[
            "capo_redshift.types.qev2_idc_application_name.Qev2IdcApplicationName"
        ] = None,
        idc_display_name: Optional[
            "capo_redshift.types.idc_display_name_string.IdcDisplayNameString"
        ] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
    ) -> "capo_redshift.types.create_qev2_idc_application_result.CreateQev2IdcApplicationResult":
        """<p>Creates an Amazon Redshift Query Editor (QEV2) IAM Identity Center application.</p>

        Args:
            idc_instance_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center instance used to create the Amazon Redshift Query Editor (QEV2) managed application.</p>
            qev2_idc_application_name: <p>The name of the Amazon Redshift Query Editor (QEV2) application in IAM Identity Center.</p>
            idc_display_name: <p>The display name for the Amazon Redshift Query Editor (QEV2) IAM Identity Center application. It appears in the console.</p>
            tags: <p>A list of tags to associate with the application. Tags are key-value pairs that you can use to organize and identify your resources.</p>

        Raises:
            capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault: <p>A dependent service denied access for the integration.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.qev2_idc_application_already_exists_fault.Qev2IdcApplicationAlreadyExistsFault: <p>The Amazon Redshift Query Editor (QEV2) IAM Identity Center application already exists. Use a different application name or describe existing applications to find the ARN.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_qev2_idc_application_message.CreateQev2IdcApplicationMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_qev2_idc_application_result.CreateQev2IdcApplicationResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_qev2_idc_application

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_qev2_idc_application.async_create_qev2_idc_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_qev2_idc_application_message.CreateQev2IdcApplicationMessage = {}
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if qev2_idc_application_name is not None:
            input_["qev2_idc_application_name"] = qev2_idc_application_name
        if idc_display_name is not None:
            input_["idc_display_name"] = idc_display_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_redshift_idc_application(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        idc_instance_arn: Optional["capo_redshift.types.string.String"] = None,
        redshift_idc_application_name: Optional[
            "capo_redshift.types.redshift_idc_application_name.RedshiftIdcApplicationName"
        ] = None,
        identity_namespace: Optional[
            "capo_redshift.types.identity_namespace_string.IdentityNamespaceString"
        ] = None,
        idc_display_name: Optional[
            "capo_redshift.types.idc_display_name_string.IdcDisplayNameString"
        ] = None,
        iam_role_arn: Optional["capo_redshift.types.string.String"] = None,
        authorized_token_issuer_list: Optional[
            "capo_redshift.types.authorized_token_issuer_list.AuthorizedTokenIssuerList"
        ] = None,
        service_integrations: Optional[
            "capo_redshift.types.service_integration_list.ServiceIntegrationList"
        ] = None,
        application_type: Optional[
            "capo_redshift.types.application_type.ApplicationType"
        ] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
        sso_tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
    ) -> "capo_redshift.types.create_redshift_idc_application_result.CreateRedshiftIdcApplicationResult":
        """<p>Creates an Amazon Redshift application for use with IAM Identity Center.</p>

        Args:
            idc_instance_arn: <p>The Amazon resource name (ARN) of the IAM Identity Center instance where Amazon Redshift creates a new managed application.</p>
            redshift_idc_application_name: <p>The name of the Redshift application in IAM Identity Center.</p>
            identity_namespace: <p>The namespace for the Amazon Redshift IAM Identity Center application instance. It determines which managed application verifies the connection token.</p>
            idc_display_name: <p>The display name for the Amazon Redshift IAM Identity Center application instance. It appears in the console.</p>
            iam_role_arn: <p>The IAM role ARN for the Amazon Redshift IAM Identity Center application instance. It has the required permissions to be assumed and invoke the IDC Identity Center API.</p>
            authorized_token_issuer_list: <p>The token issuer list for the Amazon Redshift IAM Identity Center application instance.</p>
            service_integrations: <p>A collection of service integrations for the Redshift IAM Identity Center application.</p>
            application_type: <p>The type of application being created. Valid values are <code>None</code> or <code>Lakehouse</code>. Use <code>Lakehouse</code> to enable Amazon Redshift federated permissions on cluster.</p>
            tags: <p>A list of tags.</p>
            sso_tag_keys: <p>A list of tags keys that Redshift Identity Center applications copy to IAM Identity Center. For each input key, the tag corresponding to the key-value pair is propagated.</p>

        Raises:
            capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault: <p>A dependent service denied access for the integration.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.redshift_idc_application_already_exists_fault.RedshiftIdcApplicationAlreadyExistsFault: <p>The application you attempted to add already exists.</p>
            capo_redshift.errors.redshift_idc_application_quota_exceeded_fault.RedshiftIdcApplicationQuotaExceededFault: <p>The maximum number of Redshift IAM Identity Center applications was exceeded.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_redshift_idc_application_message.CreateRedshiftIdcApplicationMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_redshift_idc_application_result.CreateRedshiftIdcApplicationResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_redshift_idc_application

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_redshift_idc_application.async_create_redshift_idc_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_redshift_idc_application_message.CreateRedshiftIdcApplicationMessage = {}
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if redshift_idc_application_name is not None:
            input_["redshift_idc_application_name"] = redshift_idc_application_name
        if identity_namespace is not None:
            input_["identity_namespace"] = identity_namespace
        if idc_display_name is not None:
            input_["idc_display_name"] = idc_display_name
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn
        if authorized_token_issuer_list is not None:
            input_["authorized_token_issuer_list"] = authorized_token_issuer_list
        if service_integrations is not None:
            input_["service_integrations"] = service_integrations
        if application_type is not None:
            input_["application_type"] = application_type
        if tags is not None:
            input_["tags"] = tags
        if sso_tag_keys is not None:
            input_["sso_tag_keys"] = sso_tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_scheduled_action(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        scheduled_action_name: Optional["capo_redshift.types.string.String"] = None,
        target_action: Optional[
            "capo_redshift.types.scheduled_action_type.ScheduledActionType"
        ] = None,
        schedule: Optional["capo_redshift.types.string.String"] = None,
        iam_role: Optional["capo_redshift.types.string.String"] = None,
        scheduled_action_description: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        start_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        enable: Optional["capo_redshift.types.boolean_optional.BooleanOptional"] = None,
    ) -> "capo_redshift.types.scheduled_action.ScheduledAction":
        """<p>Creates a scheduled action. A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the <code>ResizeCluster</code> API operation. </p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action. The name must be unique within an account. For more information about this parameter, see <a>ScheduledAction</a>. </p>
            target_action: <p>A JSON format string of the Amazon Redshift API operation with input parameters. For more information about this parameter, see <a>ScheduledAction</a>. </p>
            schedule: <p>The schedule in <code>at( )</code> or <code>cron( )</code> format. For more information about this parameter, see <a>ScheduledAction</a>.</p>
            iam_role: <p>The IAM role to assume to run the target action. For more information about this parameter, see <a>ScheduledAction</a>. </p>
            scheduled_action_description: <p>The description of the scheduled action. </p>
            start_time: <p>The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger. For more information about this parameter, see <a>ScheduledAction</a>.</p>
            end_time: <p>The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger. For more information about this parameter, see <a>ScheduledAction</a>. </p>
            enable: <p>If true, the schedule is enabled. If false, the scheduled action does not trigger. For more information about <code>state</code> of the scheduled action, see <a>ScheduledAction</a>. </p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_scheduled_action_fault.InvalidScheduledActionFault: <p>The scheduled action is not valid. </p>
            capo_redshift.errors.invalid_schedule_fault.InvalidScheduleFault: <p>The schedule you submitted isn't valid.</p>
            capo_redshift.errors.scheduled_action_already_exists_fault.ScheduledActionAlreadyExistsFault: <p>The scheduled action already exists. </p>
            capo_redshift.errors.scheduled_action_quota_exceeded_fault.ScheduledActionQuotaExceededFault: <p>The quota for scheduled actions exceeded. </p>
            capo_redshift.errors.scheduled_action_type_unsupported_fault.ScheduledActionTypeUnsupportedFault: <p>The action type specified for a scheduled action is not supported. </p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_scheduled_action_message.CreateScheduledActionMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.scheduled_action.ScheduledAction"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_scheduled_action

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_scheduled_action.async_create_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_scheduled_action_message.CreateScheduledActionMessage = {}
        if scheduled_action_name is not None:
            input_["scheduled_action_name"] = scheduled_action_name
        if target_action is not None:
            input_["target_action"] = target_action
        if schedule is not None:
            input_["schedule"] = schedule
        if iam_role is not None:
            input_["iam_role"] = iam_role
        if scheduled_action_description is not None:
            input_["scheduled_action_description"] = scheduled_action_description
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if enable is not None:
            input_["enable"] = enable

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_snapshot_copy_grant(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        snapshot_copy_grant_name: Optional["capo_redshift.types.string.String"] = None,
        kms_key_id: Optional["capo_redshift.types.string.String"] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
    ) -> "capo_redshift.types.create_snapshot_copy_grant_result.CreateSnapshotCopyGrantResult":
        """<p>Creates a snapshot copy grant that permits Amazon Redshift to use an encrypted symmetric key from Key Management Service (KMS) to encrypt copied snapshots in a destination region.</p> <p> For more information about managing snapshot copy grants, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html">Amazon Redshift Database Encryption</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>

        Args:
            snapshot_copy_grant_name: <p>The name of the snapshot copy grant. This name must be unique in the region for the Amazon Web Services account.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>Alphabetic characters must be lowercase.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique for all clusters within an Amazon Web Services account.</p> </li> </ul>
            kms_key_id: <p>The unique identifier of the encrypted symmetric key to which to grant Amazon Redshift permission. If no key is specified, the default key is used.</p>
            tags: <p>A list of tag instances.</p>

        Raises:
            capo_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault: <p>The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.limit_exceeded_fault.LimitExceededFault: <p>The encryption key has exceeded its grant limit in Amazon Web Services KMS.</p>
            capo_redshift.errors.snapshot_copy_grant_already_exists_fault.SnapshotCopyGrantAlreadyExistsFault: <p>The snapshot copy grant can't be created because a grant with the same name already exists.</p>
            capo_redshift.errors.snapshot_copy_grant_quota_exceeded_fault.SnapshotCopyGrantQuotaExceededFault: <p>The Amazon Web Services account has exceeded the maximum number of snapshot copy grants in this region.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_snapshot_copy_grant_message.CreateSnapshotCopyGrantMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.create_snapshot_copy_grant_result.CreateSnapshotCopyGrantResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_snapshot_copy_grant

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_snapshot_copy_grant.async_create_snapshot_copy_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_snapshot_copy_grant_message.CreateSnapshotCopyGrantMessage = {}
        if snapshot_copy_grant_name is not None:
            input_["snapshot_copy_grant_name"] = snapshot_copy_grant_name
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_snapshot_schedule(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        schedule_definitions: Optional[
            "capo_redshift.types.schedule_definition_list.ScheduleDefinitionList"
        ] = None,
        schedule_identifier: Optional["capo_redshift.types.string.String"] = None,
        schedule_description: Optional["capo_redshift.types.string.String"] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
        dry_run: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        next_invocations: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_redshift.types.snapshot_schedule.SnapshotSchedule":
        """<p>Create a snapshot schedule that can be associated to a cluster and which overrides the default system backup schedule. </p>

        Args:
            schedule_definitions: <p>The definition of the snapshot schedule. The definition is made up of schedule expressions, for example "cron(30 12 *)" or "rate(12 hours)". </p>
            schedule_identifier: <p>A unique identifier for a snapshot schedule. Only alphanumeric characters are allowed for the identifier.</p>
            schedule_description: <p>The description of the snapshot schedule.</p>
            tags: <p>An optional set of tags you can use to search for the schedule.</p>
            dry_run: <p></p>
            next_invocations: <p></p>

        Raises:
            capo_redshift.errors.invalid_schedule_fault.InvalidScheduleFault: <p>The schedule you submitted isn't valid.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.schedule_definition_type_unsupported_fault.ScheduleDefinitionTypeUnsupportedFault: <p>The definition you submitted is not supported.</p>
            capo_redshift.errors.snapshot_schedule_already_exists_fault.SnapshotScheduleAlreadyExistsFault: <p>The specified snapshot schedule already exists. </p>
            capo_redshift.errors.snapshot_schedule_quota_exceeded_fault.SnapshotScheduleQuotaExceededFault: <p>You have exceeded the quota of snapshot schedules. </p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_snapshot_schedule_message.CreateSnapshotScheduleMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.snapshot_schedule.SnapshotSchedule"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.create_snapshot_schedule

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_snapshot_schedule.async_create_snapshot_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_snapshot_schedule_message.CreateSnapshotScheduleMessage = {}
        if schedule_definitions is not None:
            input_["schedule_definitions"] = schedule_definitions
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if schedule_description is not None:
            input_["schedule_description"] = schedule_description
        if tags is not None:
            input_["tags"] = tags
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if next_invocations is not None:
            input_["next_invocations"] = next_invocations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_tags(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        resource_name: Optional["capo_redshift.types.string.String"] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
    ) -> None:
        """<p>Adds tags to a cluster.</p> <p>A resource can have up to 50 tags. If you try to create more than 50 tags for a resource, you will receive an error and the attempt will fail.</p> <p>If you specify a key that already exists for the resource, the value for that key will be updated with the new value.</p>

        Args:
            resource_name: <p>The Amazon Resource Name (ARN) to which you want to add the tag or tags. For example, <code>arn:aws:redshift:us-east-2:123456789:cluster:t1</code>. </p>
            tags: <p>One or more name/value pairs to add as tags to the specified resource. Each tag name is passed in with the parameter <code>Key</code> and the corresponding value is passed in with the parameter <code>Value</code>. The <code>Key</code> and <code>Value</code> parameters are separated by a comma (,). Separate multiple tags with a space. For example, <code>--tags "Key"="owner","Value"="admin" "Key"="environment","Value"="test" "Key"="version","Value"="1.0"</code>. </p>

        Raises:
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_tags_message.CreateTagsMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.create_tags

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_tags.async_create_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_tags_message.CreateTagsMessage = {}
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_usage_limit(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        feature_type: Optional[
            "capo_redshift.types.usage_limit_feature_type.UsageLimitFeatureType"
        ] = None,
        limit_type: Optional[
            "capo_redshift.types.usage_limit_limit_type.UsageLimitLimitType"
        ] = None,
        amount: Optional["capo_redshift.types.long.Long"] = None,
        period: Optional[
            "capo_redshift.types.usage_limit_period.UsageLimitPeriod"
        ] = None,
        breach_action: Optional[
            "capo_redshift.types.usage_limit_breach_action.UsageLimitBreachAction"
        ] = None,
        tags: Optional["capo_redshift.types.tag_list.TagList"] = None,
    ) -> "capo_redshift.types.usage_limit.UsageLimit":
        """<p>Creates a usage limit for a specified Amazon Redshift feature on a cluster. The usage limit is identified by the returned usage limit identifier.</p>

        Args:
            cluster_identifier: <p>The identifier of the cluster that you want to limit usage.</p>
            feature_type: <p>The Amazon Redshift feature that you want to limit.</p>
            limit_type: <p>The type of limit. Depending on the feature type, this can be based on a time duration or data size. If <code>FeatureType</code> is <code>spectrum</code>, then <code>LimitType</code> must be <code>data-scanned</code>. If <code>FeatureType</code> is <code>concurrency-scaling</code>, then <code>LimitType</code> must be <code>time</code>. If <code>FeatureType</code> is <code>cross-region-datasharing</code>, then <code>LimitType</code> must be <code>data-scanned</code>. If <code>FeatureType</code> is <code>extra-compute-for-automatic-optimization</code>, then <code>LimitType</code> must be <code>time</code>. </p>
            amount: <p>The limit amount. If time-based, this amount is in minutes. If data-based, this amount is in terabytes (TB). The value must be a positive number. </p>
            period: <p>The time period that the amount applies to. A <code>weekly</code> period begins on Sunday. The default is <code>monthly</code>. </p>
            breach_action: <p>The action that Amazon Redshift takes when the limit is reached. The default is log. For more information about this parameter, see <a>UsageLimit</a>.</p>
            tags: <p>A list of tag instances.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_usage_limit_fault.InvalidUsageLimitFault: <p>The usage limit is not valid.</p>
            capo_redshift.errors.limit_exceeded_fault.LimitExceededFault: <p>The encryption key has exceeded its grant limit in Amazon Web Services KMS.</p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.usage_limit_already_exists_fault.UsageLimitAlreadyExistsFault: <p>The usage limit already exists. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.create_usage_limit_message.CreateUsageLimitMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.usage_limit.UsageLimit"]:
            import capo_redshift._operations.redshift_service_version20121201.create_usage_limit

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.create_usage_limit.async_create_usage_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.create_usage_limit_message.CreateUsageLimitMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if feature_type is not None:
            input_["feature_type"] = feature_type
        if limit_type is not None:
            input_["limit_type"] = limit_type
        if amount is not None:
            input_["amount"] = amount
        if period is not None:
            input_["period"] = period
        if breach_action is not None:
            input_["breach_action"] = breach_action
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deauthorize_data_share(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        data_share_arn: Optional["capo_redshift.types.string.String"] = None,
        consumer_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.data_share.DataShare":
        """<p>From a datashare producer account, removes authorization from the specified datashare. </p>

        Args:
            data_share_arn: <p>The namespace Amazon Resource Name (ARN) of the datashare to remove authorization from.</p>
            consumer_identifier: <p>The identifier of the data consumer that is to have authorization removed from the datashare. This identifier is an Amazon Web Services account ID or a keyword, such as ADX.</p>

        Raises:
            capo_redshift.errors.invalid_data_share_fault.InvalidDataShareFault: <p>There is an error with the datashare.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.deauthorize_data_share_message.DeauthorizeDataShareMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.data_share.DataShare"]:
            import capo_redshift._operations.redshift_service_version20121201.deauthorize_data_share

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.deauthorize_data_share.async_deauthorize_data_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.deauthorize_data_share_message.DeauthorizeDataShareMessage = {}
        if data_share_arn is not None:
            input_["data_share_arn"] = data_share_arn
        if consumer_identifier is not None:
            input_["consumer_identifier"] = consumer_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_authentication_profile(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        authentication_profile_name: Optional[
            "capo_redshift.types.authentication_profile_name_string.AuthenticationProfileNameString"
        ] = None,
    ) -> "capo_redshift.types.delete_authentication_profile_result.DeleteAuthenticationProfileResult":
        """<p>Deletes an authentication profile.</p>

        Args:
            authentication_profile_name: <p>The name of the authentication profile to delete.</p>

        Raises:
            capo_redshift.errors.authentication_profile_not_found_fault.AuthenticationProfileNotFoundFault: <p>The authentication profile can't be found.</p>
            capo_redshift.errors.invalid_authentication_profile_request_fault.InvalidAuthenticationProfileRequestFault: <p>The authentication profile request is not valid. The profile name can't be null or empty. The authentication profile API operation must be available in the Amazon Web Services Region.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_authentication_profile_message.DeleteAuthenticationProfileMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.delete_authentication_profile_result.DeleteAuthenticationProfileResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.delete_authentication_profile

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_authentication_profile.async_delete_authentication_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_authentication_profile_message.DeleteAuthenticationProfileMessage = {}
        if authentication_profile_name is not None:
            input_["authentication_profile_name"] = authentication_profile_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        skip_final_cluster_snapshot: Optional[
            "capo_redshift.types.boolean.Boolean"
        ] = None,
        final_cluster_snapshot_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        final_cluster_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_redshift.types.delete_cluster_result.DeleteClusterResult":
        """<p>Deletes a previously provisioned cluster without its final snapshot being created. A successful response from the web service indicates that the request was received correctly. Use <a>DescribeClusters</a> to monitor the status of the deletion. The delete operation cannot be canceled or reverted once submitted. For more information about managing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html">Amazon Redshift Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>If you want to shut down the cluster and retain it for future use, set <i>SkipFinalClusterSnapshot</i> to <code>false</code> and specify a name for <i>FinalClusterSnapshotIdentifier</i>. You can later restore this snapshot to resume using the cluster. If a final cluster snapshot is requested, the status of the cluster will be "final-snapshot" while the snapshot is being taken, then it's "deleting" once Amazon Redshift begins deleting the cluster. </p> <p> For more information about managing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html">Amazon Redshift Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            cluster_identifier: <p>The identifier of the cluster to be deleted.</p> <p>Constraints:</p> <ul> <li> <p>Must contain lowercase characters.</p> </li> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            skip_final_cluster_snapshot: <p>Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If <code>true</code>, a final cluster snapshot is not created. If <code>false</code>, a final cluster snapshot is created before the cluster is deleted. </p> <note> <p>The <i>FinalClusterSnapshotIdentifier</i> parameter must be specified if <i>SkipFinalClusterSnapshot</i> is <code>false</code>.</p> </note> <p>Default: <code>false</code> </p>
            final_cluster_snapshot_identifier: <p>The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, <i>SkipFinalClusterSnapshot</i> must be <code>false</code>. </p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            final_cluster_snapshot_retention_period: <p>The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p> <p>The default value is -1.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.cluster_snapshot_already_exists_fault.ClusterSnapshotAlreadyExistsFault: <p>The value specified as a snapshot identifier is already used by an existing snapshot.</p>
            capo_redshift.errors.cluster_snapshot_quota_exceeded_fault.ClusterSnapshotQuotaExceededFault: <p>The request would result in the user exceeding the allowed number of cluster snapshots.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault: <p>The retention period specified is either in the past or is not a valid value.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_cluster_message.DeleteClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.delete_cluster_result.DeleteClusterResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.delete_cluster

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_cluster_message.DeleteClusterMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if skip_final_cluster_snapshot is not None:
            input_["skip_final_cluster_snapshot"] = skip_final_cluster_snapshot
        if final_cluster_snapshot_identifier is not None:
            input_["final_cluster_snapshot_identifier"] = (
                final_cluster_snapshot_identifier
            )
        if final_cluster_snapshot_retention_period is not None:
            input_["final_cluster_snapshot_retention_period"] = (
                final_cluster_snapshot_retention_period
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        parameter_group_name: Optional["capo_redshift.types.string.String"] = None,
    ) -> None:
        """<p>Deletes a specified Amazon Redshift parameter group.</p> <note> <p>You cannot delete a parameter group if it is associated with a cluster.</p> </note>

        Args:
            parameter_group_name: <p>The name of the parameter group to be deleted.</p> <p>Constraints:</p> <ul> <li> <p>Must be the name of an existing cluster parameter group.</p> </li> <li> <p>Cannot delete a default cluster parameter group.</p> </li> </ul>

        Raises:
            capo_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault: <p>The parameter group name does not refer to an existing parameter group.</p>
            capo_redshift.errors.invalid_cluster_parameter_group_state_fault.InvalidClusterParameterGroupStateFault: <p>The cluster parameter group action can not be completed because another task is in progress that involves the parameter group. Wait a few moments and try the operation again.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_cluster_parameter_group_message.DeleteClusterParameterGroupMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_cluster_parameter_group

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_cluster_parameter_group.async_delete_cluster_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_cluster_parameter_group_message.DeleteClusterParameterGroupMessage = {}
        if parameter_group_name is not None:
            input_["parameter_group_name"] = parameter_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster_security_group(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_security_group_name: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> None:
        """<p>Deletes an Amazon Redshift security group.</p> <note> <p>You cannot delete a security group that is associated with any clusters. You cannot delete the default security group.</p> </note> <p> For information about managing security groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html">Amazon Redshift Cluster Security Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            cluster_security_group_name: <p>The name of the cluster security group to be deleted.</p>

        Raises:
            capo_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault: <p>The cluster security group name does not refer to an existing cluster security group.</p>
            capo_redshift.errors.invalid_cluster_security_group_state_fault.InvalidClusterSecurityGroupStateFault: <p>The state of the cluster security group is not <code>available</code>. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_cluster_security_group_message.DeleteClusterSecurityGroupMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_cluster_security_group

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_cluster_security_group.async_delete_cluster_security_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_cluster_security_group_message.DeleteClusterSecurityGroupMessage = {}
        if cluster_security_group_name is not None:
            input_["cluster_security_group_name"] = cluster_security_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_cluster_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> (
        "capo_redshift.types.delete_cluster_snapshot_result.DeleteClusterSnapshotResult"
    ):
        """<p>Deletes the specified manual snapshot. The snapshot must be in the <code>available</code> state, with no other users authorized to access the snapshot. </p> <p>Unlike automated snapshots, manual snapshots are retained even after you delete your cluster. Amazon Redshift does not delete your manual snapshots. You must delete manual snapshot explicitly to avoid getting charged. If other accounts are authorized to access the snapshot, you must revoke all of the authorizations before you can delete the snapshot.</p>

        Args:
            snapshot_identifier: <p>The unique identifier of the manual snapshot to be deleted.</p> <p>Constraints: Must be the name of an existing snapshot that is in the <code>available</code>, <code>failed</code>, or <code>cancelled</code> state.</p>
            snapshot_cluster_identifier: <p>The unique identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.</p> <p>Constraints: Must be the name of valid cluster.</p>

        Raises:
            capo_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault: <p>The snapshot identifier does not refer to an existing cluster snapshot.</p>
            capo_redshift.errors.invalid_cluster_snapshot_state_fault.InvalidClusterSnapshotStateFault: <p>The specified cluster snapshot is not in the <code>available</code> state, or other accounts are authorized to access the snapshot. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_cluster_snapshot_message.DeleteClusterSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.delete_cluster_snapshot_result.DeleteClusterSnapshotResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.delete_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_cluster_snapshot.async_delete_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_cluster_snapshot_message.DeleteClusterSnapshotMessage = {}
        if snapshot_identifier is not None:
            input_["snapshot_identifier"] = snapshot_identifier
        if snapshot_cluster_identifier is not None:
            input_["snapshot_cluster_identifier"] = snapshot_cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster_subnet_group(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_subnet_group_name: Optional["capo_redshift.types.string.String"] = None,
    ) -> None:
        """<p>Deletes the specified cluster subnet group.</p>

        Args:
            cluster_subnet_group_name: <p>The name of the cluster subnet group name to be deleted.</p>

        Raises:
            capo_redshift.errors.cluster_subnet_group_not_found_fault.ClusterSubnetGroupNotFoundFault: <p>The cluster subnet group name does not refer to an existing cluster subnet group.</p>
            capo_redshift.errors.invalid_cluster_subnet_group_state_fault.InvalidClusterSubnetGroupStateFault: <p>The cluster subnet group cannot be deleted because it is in use.</p>
            capo_redshift.errors.invalid_cluster_subnet_state_fault.InvalidClusterSubnetStateFault: <p>The state of the subnet is invalid.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_cluster_subnet_group_message.DeleteClusterSubnetGroupMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_cluster_subnet_group

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_cluster_subnet_group.async_delete_cluster_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_cluster_subnet_group_message.DeleteClusterSubnetGroupMessage = {}
        if cluster_subnet_group_name is not None:
            input_["cluster_subnet_group_name"] = cluster_subnet_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_custom_domain_association(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        custom_domain_name: Optional[
            "capo_redshift.types.custom_domain_name_string.CustomDomainNameString"
        ] = None,
    ) -> None:
        """<p>Contains information about deleting a custom domain association for a cluster.</p>

        Args:
            cluster_identifier: <p>The identifier of the cluster to delete a custom domain association for.</p>
            custom_domain_name: <p>The custom domain name for the custom domain association.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.custom_cname_association_fault.CustomCnameAssociationFault: <p>An error occurred when an attempt was made to change the custom domain association.</p>
            capo_redshift.errors.custom_domain_association_not_found_fault.CustomDomainAssociationNotFoundFault: <p>An error occurred. The custom domain name couldn't be found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_custom_domain_association_message.DeleteCustomDomainAssociationMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_custom_domain_association

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_custom_domain_association.async_delete_custom_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_custom_domain_association_message.DeleteCustomDomainAssociationMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_endpoint_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        endpoint_name: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.endpoint_access.EndpointAccess":
        """<p>Deletes a Redshift-managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The Redshift-managed VPC endpoint to delete.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.endpoint_not_found_fault.EndpointNotFoundFault: <p>The endpoint name doesn't refer to an existing endpoint.</p>
            capo_redshift.errors.invalid_cluster_security_group_state_fault.InvalidClusterSecurityGroupStateFault: <p>The state of the cluster security group is not <code>available</code>. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_endpoint_state_fault.InvalidEndpointStateFault: <p>The status of the endpoint is not valid.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_endpoint_access_message.DeleteEndpointAccessMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.endpoint_access.EndpointAccess"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.delete_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_endpoint_access.async_delete_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_endpoint_access_message.DeleteEndpointAccessMessage = {}
        if endpoint_name is not None:
            input_["endpoint_name"] = endpoint_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_event_subscription(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        subscription_name: Optional["capo_redshift.types.string.String"] = None,
    ) -> None:
        """<p>Deletes an Amazon Redshift event notification subscription.</p>

        Args:
            subscription_name: <p>The name of the Amazon Redshift event notification subscription to be deleted.</p>

        Raises:
            capo_redshift.errors.invalid_subscription_state_fault.InvalidSubscriptionStateFault: <p>The subscription request is invalid because it is a duplicate request. This subscription request is already in progress.</p>
            capo_redshift.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>An Amazon Redshift event notification subscription with the specified name does not exist.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_event_subscription_message.DeleteEventSubscriptionMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_event_subscription

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_event_subscription.async_delete_event_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_event_subscription_message.DeleteEventSubscriptionMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_hsm_client_certificate(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        hsm_client_certificate_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> None:
        """<p>Deletes the specified HSM client certificate.</p>

        Args:
            hsm_client_certificate_identifier: <p>The identifier of the HSM client certificate to be deleted.</p>

        Raises:
            capo_redshift.errors.hsm_client_certificate_not_found_fault.HsmClientCertificateNotFoundFault: <p>There is no Amazon Redshift HSM client certificate with the specified identifier.</p>
            capo_redshift.errors.invalid_hsm_client_certificate_state_fault.InvalidHsmClientCertificateStateFault: <p>The specified HSM client certificate is not in the <code>available</code> state, or it is still in use by one or more Amazon Redshift clusters.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_hsm_client_certificate_message.DeleteHsmClientCertificateMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_hsm_client_certificate

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_hsm_client_certificate.async_delete_hsm_client_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_hsm_client_certificate_message.DeleteHsmClientCertificateMessage = {}
        if hsm_client_certificate_identifier is not None:
            input_["hsm_client_certificate_identifier"] = (
                hsm_client_certificate_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_hsm_configuration(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        hsm_configuration_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> None:
        """<p>Deletes the specified Amazon Redshift HSM configuration.</p>

        Args:
            hsm_configuration_identifier: <p>The identifier of the Amazon Redshift HSM configuration to be deleted.</p>

        Raises:
            capo_redshift.errors.hsm_configuration_not_found_fault.HsmConfigurationNotFoundFault: <p>There is no Amazon Redshift HSM configuration with the specified identifier.</p>
            capo_redshift.errors.invalid_hsm_configuration_state_fault.InvalidHsmConfigurationStateFault: <p>The specified HSM configuration is not in the <code>available</code> state, or it is still in use by one or more Amazon Redshift clusters.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_hsm_configuration_message.DeleteHsmConfigurationMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_hsm_configuration

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_hsm_configuration.async_delete_hsm_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_hsm_configuration_message.DeleteHsmConfigurationMessage = {}
        if hsm_configuration_identifier is not None:
            input_["hsm_configuration_identifier"] = hsm_configuration_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_integration(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        integration_arn: Optional[
            "capo_redshift.types.integration_arn.IntegrationArn"
        ] = None,
    ) -> "capo_redshift.types.integration.Integration":
        """<p>Deletes a zero-ETL integration or S3 event integration with Amazon Redshift.</p>

        Args:
            integration_arn: <p>The unique identifier of the integration to delete.</p>

        Raises:
            capo_redshift.errors.integration_conflict_operation_fault.IntegrationConflictOperationFault: <p>A conflicting conditional operation is currently in progress against this resource. This typically occurs when there are multiple requests being made to the same resource at the same time, and these requests conflict with each other.</p>
            capo_redshift.errors.integration_conflict_state_fault.IntegrationConflictStateFault: <p>The integration is in an invalid state and can't perform the requested operation.</p>
            capo_redshift.errors.integration_not_found_fault.IntegrationNotFoundFault: <p>The integration can't be found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_integration_message.DeleteIntegrationMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.integration.Integration"]:
            import capo_redshift._operations.redshift_service_version20121201.delete_integration

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_integration.async_delete_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_integration_message.DeleteIntegrationMessage = {}
        if integration_arn is not None:
            input_["integration_arn"] = integration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_partner(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        account_id: Optional[
            "capo_redshift.types.partner_integration_account_id.PartnerIntegrationAccountId"
        ] = None,
        cluster_identifier: Optional[
            "capo_redshift.types.partner_integration_cluster_identifier.PartnerIntegrationClusterIdentifier"
        ] = None,
        database_name: Optional[
            "capo_redshift.types.partner_integration_database_name.PartnerIntegrationDatabaseName"
        ] = None,
        partner_name: Optional[
            "capo_redshift.types.partner_integration_partner_name.PartnerIntegrationPartnerName"
        ] = None,
    ) -> "capo_redshift.types.partner_integration_output_message.PartnerIntegrationOutputMessage":
        """<p>Deletes a partner integration from a cluster. Data can still flow to the cluster until the integration is deleted at the partner's website.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID that owns the cluster.</p>
            cluster_identifier: <p>The cluster identifier of the cluster that receives data from the partner.</p>
            database_name: <p>The name of the database that receives data from the partner.</p>
            partner_name: <p>The name of the partner that is authorized to send data.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.partner_not_found_fault.PartnerNotFoundFault: <p>The name of the partner was not found.</p>
            capo_redshift.errors.unauthorized_partner_integration_fault.UnauthorizedPartnerIntegrationFault: <p>The partner integration is not authorized.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.partner_integration_input_message.PartnerIntegrationInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.partner_integration_output_message.PartnerIntegrationOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.delete_partner

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_partner.async_delete_partner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.partner_integration_input_message.PartnerIntegrationInputMessage = {}
        if account_id is not None:
            input_["account_id"] = account_id
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if database_name is not None:
            input_["database_name"] = database_name
        if partner_name is not None:
            input_["partner_name"] = partner_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_qev2_idc_application(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        qev2_idc_application_arn: Optional["capo_redshift.types.string.String"] = None,
    ) -> None:
        """<p>Deletes an Amazon Redshift Query Editor (QEV2) IAM Identity Center application.</p>

        Args:
            qev2_idc_application_arn: <p>The Amazon Resource Name (ARN) for the Amazon Redshift Query Editor (QEV2) IAM Identity Center application to delete.</p>

        Raises:
            capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault: <p>A dependent service denied access for the integration.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.qev2_idc_application_not_exists_fault.Qev2IdcApplicationNotExistsFault: <p>The specified Amazon Redshift Query Editor (QEV2) IAM Identity Center application doesn't exist. Verify that the application ARN is correct and that the application exists in this Region.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_qev2_idc_application_message.DeleteQev2IdcApplicationMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_qev2_idc_application

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_qev2_idc_application.async_delete_qev2_idc_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_qev2_idc_application_message.DeleteQev2IdcApplicationMessage = {}
        if qev2_idc_application_arn is not None:
            input_["qev2_idc_application_arn"] = qev2_idc_application_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_redshift_idc_application(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        redshift_idc_application_arn: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> None:
        """<p>Deletes an Amazon Redshift IAM Identity Center application.</p>

        Args:
            redshift_idc_application_arn: <p>The ARN for a deleted Amazon Redshift IAM Identity Center application.</p>

        Raises:
            capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault: <p>A dependent service denied access for the integration.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.redshift_idc_application_not_exists_fault.RedshiftIdcApplicationNotExistsFault: <p>The application you attempted to find doesn't exist.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_redshift_idc_application_message.DeleteRedshiftIdcApplicationMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_redshift_idc_application

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_redshift_idc_application.async_delete_redshift_idc_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_redshift_idc_application_message.DeleteRedshiftIdcApplicationMessage = {}
        if redshift_idc_application_arn is not None:
            input_["redshift_idc_application_arn"] = redshift_idc_application_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        resource_arn: Optional["capo_redshift.types.string.String"] = None,
    ) -> None:
        """<p>Deletes the resource policy for a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource of which its resource policy is deleted.</p>

        Raises:
            capo_redshift.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_resource_policy_message.DeleteResourcePolicyMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_resource_policy_message.DeleteResourcePolicyMessage = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_scheduled_action(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        scheduled_action_name: Optional["capo_redshift.types.string.String"] = None,
    ) -> None:
        """<p>Deletes a scheduled action. </p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action to delete. </p>

        Raises:
            capo_redshift.errors.scheduled_action_not_found_fault.ScheduledActionNotFoundFault: <p>The scheduled action cannot be found. </p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_scheduled_action_message.DeleteScheduledActionMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_scheduled_action

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_scheduled_action.async_delete_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_scheduled_action_message.DeleteScheduledActionMessage = {}
        if scheduled_action_name is not None:
            input_["scheduled_action_name"] = scheduled_action_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_snapshot_copy_grant(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        snapshot_copy_grant_name: Optional["capo_redshift.types.string.String"] = None,
    ) -> None:
        """<p>Deletes the specified snapshot copy grant.</p>

        Args:
            snapshot_copy_grant_name: <p>The name of the snapshot copy grant to delete.</p>

        Raises:
            capo_redshift.errors.invalid_snapshot_copy_grant_state_fault.InvalidSnapshotCopyGrantStateFault: <p>The snapshot copy grant can't be deleted because it is used by one or more clusters.</p>
            capo_redshift.errors.snapshot_copy_grant_not_found_fault.SnapshotCopyGrantNotFoundFault: <p>The specified snapshot copy grant can't be found. Make sure that the name is typed correctly and that the grant exists in the destination region.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_snapshot_copy_grant_message.DeleteSnapshotCopyGrantMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_snapshot_copy_grant

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_snapshot_copy_grant.async_delete_snapshot_copy_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_snapshot_copy_grant_message.DeleteSnapshotCopyGrantMessage = {}
        if snapshot_copy_grant_name is not None:
            input_["snapshot_copy_grant_name"] = snapshot_copy_grant_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_snapshot_schedule(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        schedule_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> None:
        """<p>Deletes a snapshot schedule.</p>

        Args:
            schedule_identifier: <p>A unique identifier of the snapshot schedule to delete.</p>

        Raises:
            capo_redshift.errors.invalid_cluster_snapshot_schedule_state_fault.InvalidClusterSnapshotScheduleStateFault: <p>The cluster snapshot schedule state is not valid.</p>
            capo_redshift.errors.snapshot_schedule_not_found_fault.SnapshotScheduleNotFoundFault: <p>We could not find the specified snapshot schedule. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_snapshot_schedule_message.DeleteSnapshotScheduleMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_snapshot_schedule

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_snapshot_schedule.async_delete_snapshot_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_snapshot_schedule_message.DeleteSnapshotScheduleMessage = {}
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_tags(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        resource_name: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
    ) -> None:
        """<p>Deletes tags from a resource. You must provide the ARN of the resource from which you want to delete the tag or tags.</p>

        Args:
            resource_name: <p>The Amazon Resource Name (ARN) from which you want to remove the tag or tags. For example, <code>arn:aws:redshift:us-east-2:123456789:cluster:t1</code>. </p>
            tag_keys: <p>The tag key that you want to delete.</p>

        Raises:
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_tags_message.DeleteTagsMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_tags

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_tags.async_delete_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_tags_message.DeleteTagsMessage = {}
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_usage_limit(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        usage_limit_id: Optional["capo_redshift.types.string.String"] = None,
    ) -> None:
        """<p>Deletes a usage limit from a cluster.</p>

        Args:
            usage_limit_id: <p>The identifier of the usage limit to delete.</p>

        Raises:
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.usage_limit_not_found_fault.UsageLimitNotFoundFault: <p>The usage limit identifier can't be found.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.delete_usage_limit_message.DeleteUsageLimitMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.delete_usage_limit

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.delete_usage_limit.async_delete_usage_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.delete_usage_limit_message.DeleteUsageLimitMessage = {}
        if usage_limit_id is not None:
            input_["usage_limit_id"] = usage_limit_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_namespace(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        namespace_identifier: Optional[
            "capo_redshift.types.namespace_identifier_union.NamespaceIdentifierUnion"
        ] = None,
        consumer_identifiers: Optional[
            "capo_redshift.types.consumer_identifier_list.ConsumerIdentifierList"
        ] = None,
    ) -> "capo_redshift.types.deregister_namespace_output_message.DeregisterNamespaceOutputMessage":
        """<p>Deregisters a cluster or serverless namespace from the Amazon Web Services Glue Data Catalog.</p>

        Args:
            namespace_identifier: <p>The unique identifier of the cluster or serverless namespace that you want to deregister.</p>
            consumer_identifiers: <p>An array containing the ID of the consumer account that you want to deregister the cluster or serverless namespace from.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_namespace_fault.InvalidNamespaceFault: <p>The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.deregister_namespace_input_message.DeregisterNamespaceInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.deregister_namespace_output_message.DeregisterNamespaceOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.deregister_namespace

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.deregister_namespace.async_deregister_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.deregister_namespace_input_message.DeregisterNamespaceInputMessage = {}
        if namespace_identifier is not None:
            input_["namespace_identifier"] = namespace_identifier
        if consumer_identifiers is not None:
            input_["consumer_identifiers"] = consumer_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_account_attributes(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        attribute_names: Optional[
            "capo_redshift.types.attribute_name_list.AttributeNameList"
        ] = None,
    ) -> "capo_redshift.types.account_attribute_list.AccountAttributeList":
        """<p>Returns a list of attributes attached to an account</p>

        Args:
            attribute_names: <p>A list of attribute names.</p>

        Raises:
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_account_attributes_message.DescribeAccountAttributesMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.account_attribute_list.AccountAttributeList"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_account_attributes

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_account_attributes.async_describe_account_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_account_attributes_message.DescribeAccountAttributesMessage = {}
        if attribute_names is not None:
            input_["attribute_names"] = attribute_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_authentication_profiles(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        authentication_profile_name: Optional[
            "capo_redshift.types.authentication_profile_name_string.AuthenticationProfileNameString"
        ] = None,
    ) -> "capo_redshift.types.describe_authentication_profiles_result.DescribeAuthenticationProfilesResult":
        """<p>Describes an authentication profile.</p>

        Args:
            authentication_profile_name: <p>The name of the authentication profile to describe. If not specified then all authentication profiles owned by the account are listed.</p>

        Raises:
            capo_redshift.errors.authentication_profile_not_found_fault.AuthenticationProfileNotFoundFault: <p>The authentication profile can't be found.</p>
            capo_redshift.errors.invalid_authentication_profile_request_fault.InvalidAuthenticationProfileRequestFault: <p>The authentication profile request is not valid. The profile name can't be null or empty. The authentication profile API operation must be available in the Amazon Web Services Region.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_authentication_profiles_message.DescribeAuthenticationProfilesMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.describe_authentication_profiles_result.DescribeAuthenticationProfilesResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_authentication_profiles

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_authentication_profiles.async_describe_authentication_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_authentication_profiles_message.DescribeAuthenticationProfilesMessage = {}
        if authentication_profile_name is not None:
            input_["authentication_profile_name"] = authentication_profile_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_cluster_db_revisions(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.cluster_db_revisions_message.ClusterDbRevisionsMessage":
        """<p>Returns an array of <code>ClusterDbRevision</code> objects.</p>

        Args:
            cluster_identifier: <p>A unique identifier for a cluster whose <code>ClusterDbRevisions</code> you are requesting. This parameter is case sensitive. All clusters defined for an account are returned by default.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in the <code>marker</code> field of the response. You can retrieve the next set of response records by providing the returned <code>marker</code> value in the <code>marker</code> parameter and retrying the request. </p> <p>Default: 100</p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point for returning a set of response records. When the results of a <code>DescribeClusterDbRevisions</code> request exceed the value specified in <code>MaxRecords</code>, Amazon Redshift returns a value in the <code>marker</code> field of the response. You can retrieve the next set of response records by providing the returned <code>marker</code> value in the <code>marker</code> parameter and retrying the request. </p> <p>Constraints: You can specify either the <code>ClusterIdentifier</code> parameter, or the <code>marker</code> parameter, but not both.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_cluster_db_revisions_message.DescribeClusterDbRevisionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.cluster_db_revisions_message.ClusterDbRevisionsMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_cluster_db_revisions

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_cluster_db_revisions.async_describe_cluster_db_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_cluster_db_revisions_message.DescribeClusterDbRevisionsMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_cluster_db_revisions(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.cluster_db_revision.ClusterDbRevision]":
        _token = marker
        while True:
            _response = await self.describe_cluster_db_revisions(
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("cluster_db_revisions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_cluster_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        parameter_group_name: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "capo_redshift.types.cluster_parameter_groups_message.ClusterParameterGroupsMessage":
        """<p>Returns a list of Amazon Redshift parameter groups, including parameter groups you created and the default parameter group. For each parameter group, the response includes the parameter group name, description, and parameter group family name. You can optionally specify a name to retrieve the description of a specific parameter group.</p> <p> For more information about parameters and parameter groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Amazon Redshift Parameter Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>If you specify both tag keys and tag values in the same request, Amazon Redshift returns all parameter groups that match any combination of the specified keys and values. For example, if you have <code>owner</code> and <code>environment</code> for tag keys, and <code>admin</code> and <code>test</code> for tag values, all parameter groups that have any combination of those values are returned.</p> <p>If both tag keys and values are omitted from the request, parameter groups are returned regardless of whether they have tag keys or values associated with them.</p>

        Args:
            parameter_group_name: <p>The name of a specific parameter group for which to return details. By default, details about all parameter groups and the default parameter group are returned.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeClusterParameterGroups</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>
            tag_keys: <p>A tag key or keys for which you want to return all matching cluster parameter groups that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag keys associated with them.</p>
            tag_values: <p>A tag value or values for which you want to return all matching cluster parameter groups that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag values associated with them.</p>

        Raises:
            capo_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault: <p>The parameter group name does not refer to an existing parameter group.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_cluster_parameter_groups_message.DescribeClusterParameterGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.cluster_parameter_groups_message.ClusterParameterGroupsMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_cluster_parameter_groups

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_cluster_parameter_groups.async_describe_cluster_parameter_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_cluster_parameter_groups_message.DescribeClusterParameterGroupsMessage = {}
        if parameter_group_name is not None:
            input_["parameter_group_name"] = parameter_group_name
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_cluster_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        parameter_group_name: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "AsyncIterator[capo_redshift.types.cluster_parameter_group.ClusterParameterGroup]":
        _token = marker
        while True:
            _response = await self.describe_cluster_parameter_groups(
                config_overrides=config_overrides,
                parameter_group_name=parameter_group_name,
                max_records=max_records,
                marker=_token,
                tag_keys=tag_keys,
                tag_values=tag_values,
            )
            _page = _resolve_path(_response, ("parameter_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_cluster_parameters(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        parameter_group_name: Optional["capo_redshift.types.string.String"] = None,
        source: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.cluster_parameter_group_details.ClusterParameterGroupDetails":
        """<p>Returns a detailed list of parameters contained within the specified Amazon Redshift parameter group. For each parameter the response includes information such as parameter name, description, data type, value, whether the parameter value is modifiable, and so on.</p> <p>You can specify <i>source</i> filter to retrieve parameters of only specific type. For example, to retrieve parameters that were modified by a user action such as from <a>ModifyClusterParameterGroup</a>, you can specify <i>source</i> equal to <i>user</i>.</p> <p> For more information about parameters and parameter groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Amazon Redshift Parameter Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            parameter_group_name: <p>The name of a cluster parameter group for which to return details.</p>
            source: <p>The parameter types to return. Specify <code>user</code> to show parameters that are different form the default. Similarly, specify <code>engine-default</code> to show parameters that are the same as the default parameter group. </p> <p>Default: All parameter types returned.</p> <p>Valid Values: <code>user</code> | <code>engine-default</code> </p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeClusterParameters</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault: <p>The parameter group name does not refer to an existing parameter group.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_cluster_parameters_message.DescribeClusterParametersMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.cluster_parameter_group_details.ClusterParameterGroupDetails"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_cluster_parameters

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_cluster_parameters.async_describe_cluster_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_cluster_parameters_message.DescribeClusterParametersMessage = {}
        if parameter_group_name is not None:
            input_["parameter_group_name"] = parameter_group_name
        if source is not None:
            input_["source"] = source
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_cluster_parameters(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        parameter_group_name: Optional["capo_redshift.types.string.String"] = None,
        source: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.parameter.Parameter]":
        _token = marker
        while True:
            _response = await self.describe_cluster_parameters(
                config_overrides=config_overrides,
                parameter_group_name=parameter_group_name,
                source=source,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("parameters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_clusters(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "capo_redshift.types.clusters_message.ClustersMessage":
        """<p>Returns properties of provisioned clusters including general cluster properties, cluster database properties, maintenance and backup properties, and security and access properties. This operation supports pagination. For more information about managing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html">Amazon Redshift Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>If you specify both tag keys and tag values in the same request, Amazon Redshift returns all clusters that match any combination of the specified keys and values. For example, if you have <code>owner</code> and <code>environment</code> for tag keys, and <code>admin</code> and <code>test</code> for tag values, all clusters that have any combination of those values are returned.</p> <p>If both tag keys and values are omitted from the request, clusters are returned regardless of whether they have tag keys or values associated with them.</p>

        Args:
            cluster_identifier: <p>The unique identifier of a cluster whose properties you are requesting. This parameter is case sensitive.</p> <p>The default is that all clusters defined for an account are returned.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeClusters</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p> <p>Constraints: You can specify either the <b>ClusterIdentifier</b> parameter or the <b>Marker</b> parameter, but not both. </p>
            tag_keys: <p>A tag key or keys for which you want to return all matching clusters that are associated with the specified key or keys. For example, suppose that you have clusters that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag keys associated with them.</p>
            tag_values: <p>A tag value or values for which you want to return all matching clusters that are associated with the specified tag value or values. For example, suppose that you have clusters that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag values associated with them.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_clusters_message.DescribeClustersMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.clusters_message.ClustersMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_clusters

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_clusters.async_describe_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_clusters_message.DescribeClustersMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_clusters(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "AsyncIterator[capo_redshift.types.cluster.Cluster]":
        _token = marker
        while True:
            _response = await self.describe_clusters(
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                max_records=max_records,
                marker=_token,
                tag_keys=tag_keys,
                tag_values=tag_values,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_cluster_security_groups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_security_group_name: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> (
        "capo_redshift.types.cluster_security_group_message.ClusterSecurityGroupMessage"
    ):
        """<p>Returns information about Amazon Redshift security groups. If the name of a security group is specified, the response will contain only information about only that security group.</p> <p> For information about managing security groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html">Amazon Redshift Cluster Security Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>If you specify both tag keys and tag values in the same request, Amazon Redshift returns all security groups that match any combination of the specified keys and values. For example, if you have <code>owner</code> and <code>environment</code> for tag keys, and <code>admin</code> and <code>test</code> for tag values, all security groups that have any combination of those values are returned.</p> <p>If both tag keys and values are omitted from the request, security groups are returned regardless of whether they have tag keys or values associated with them.</p>

        Args:
            cluster_security_group_name: <p>The name of a cluster security group for which you are requesting details. You must specify either the <b>Marker</b> parameter or a <b>ClusterSecurityGroupName</b> parameter, but not both. </p> <p> Example: <code>securitygroup1</code> </p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeClusterSecurityGroups</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p> <p>Constraints: You must specify either the <b>ClusterSecurityGroupName</b> parameter or the <b>Marker</b> parameter, but not both. </p>
            tag_keys: <p>A tag key or keys for which you want to return all matching cluster security groups that are associated with the specified key or keys. For example, suppose that you have security groups that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag keys associated with them.</p>
            tag_values: <p>A tag value or values for which you want to return all matching cluster security groups that are associated with the specified tag value or values. For example, suppose that you have security groups that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag values associated with them.</p>

        Raises:
            capo_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault: <p>The cluster security group name does not refer to an existing cluster security group.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_cluster_security_groups_message.DescribeClusterSecurityGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.cluster_security_group_message.ClusterSecurityGroupMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_cluster_security_groups

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_cluster_security_groups.async_describe_cluster_security_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_cluster_security_groups_message.DescribeClusterSecurityGroupsMessage = {}
        if cluster_security_group_name is not None:
            input_["cluster_security_group_name"] = cluster_security_group_name
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_cluster_security_groups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_security_group_name: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> (
        "AsyncIterator[capo_redshift.types.cluster_security_group.ClusterSecurityGroup]"
    ):
        _token = marker
        while True:
            _response = await self.describe_cluster_security_groups(
                config_overrides=config_overrides,
                cluster_security_group_name=cluster_security_group_name,
                max_records=max_records,
                marker=_token,
                tag_keys=tag_keys,
                tag_values=tag_values,
            )
            _page = _resolve_path(_response, ("cluster_security_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_cluster_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_arn: Optional["capo_redshift.types.string.String"] = None,
        snapshot_type: Optional["capo_redshift.types.string.String"] = None,
        start_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        owner_account: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
        cluster_exists: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        sorting_entities: Optional[
            "capo_redshift.types.snapshot_sorting_entity_list.SnapshotSortingEntityList"
        ] = None,
    ) -> "capo_redshift.types.snapshot_message.SnapshotMessage":
        """<p>Returns one or more snapshot objects, which contain metadata about your cluster snapshots. By default, this operation returns information about all snapshots of all clusters that are owned by your Amazon Web Services account. No information is returned for snapshots owned by inactive Amazon Web Services accounts.</p> <p>If you specify both tag keys and tag values in the same request, Amazon Redshift returns all snapshots that match any combination of the specified keys and values. For example, if you have <code>owner</code> and <code>environment</code> for tag keys, and <code>admin</code> and <code>test</code> for tag values, all snapshots that have any combination of those values are returned. Only snapshots that you own are returned in the response; shared snapshots are not returned with the tag key and tag value request parameters.</p> <p>If both tag keys and values are omitted from the request, snapshots are returned regardless of whether they have tag keys or values associated with them.</p>

        Args:
            cluster_identifier: <p>The identifier of the cluster which generated the requested snapshots.</p>
            snapshot_identifier: <p>The snapshot identifier of the snapshot about which to return information.</p>
            snapshot_arn: <p>The Amazon Resource Name (ARN) of the snapshot associated with the message to describe cluster snapshots.</p>
            snapshot_type: <p>The type of snapshots for which you are requesting information. By default, snapshots of all types are returned.</p> <p>Valid Values: <code>automated</code> | <code>manual</code> </p>
            start_time: <p>A value that requests only snapshots created at or after the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO8601 Wikipedia page.</a> </p> <p>Example: <code>2012-07-16T18:00:00Z</code> </p>
            end_time: <p>A time value that requests only snapshots created at or before the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO8601 Wikipedia page.</a> </p> <p>Example: <code>2012-07-16T18:00:00Z</code> </p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeClusterSnapshots</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>
            owner_account: <p>The Amazon Web Services account used to create or copy the snapshot. Use this field to filter the results to snapshots owned by a particular account. To describe snapshots you own, either specify your Amazon Web Services account, or do not specify the parameter.</p>
            tag_keys: <p>A tag key or keys for which you want to return all matching cluster snapshots that are associated with the specified key or keys. For example, suppose that you have snapshots that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag keys associated with them.</p>
            tag_values: <p>A tag value or values for which you want to return all matching cluster snapshots that are associated with the specified tag value or values. For example, suppose that you have snapshots that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag values associated with them.</p>
            cluster_exists: <p>A value that indicates whether to return snapshots only for an existing cluster. You can perform table-level restore only by using a snapshot of an existing cluster, that is, a cluster that has not been deleted. Values for this parameter work as follows: </p> <ul> <li> <p>If <code>ClusterExists</code> is set to <code>true</code>, <code>ClusterIdentifier</code> is required.</p> </li> <li> <p>If <code>ClusterExists</code> is set to <code>false</code> and <code>ClusterIdentifier</code> isn't specified, all snapshots associated with deleted clusters (orphaned snapshots) are returned. </p> </li> <li> <p>If <code>ClusterExists</code> is set to <code>false</code> and <code>ClusterIdentifier</code> is specified for a deleted cluster, snapshots associated with that cluster are returned.</p> </li> <li> <p>If <code>ClusterExists</code> is set to <code>false</code> and <code>ClusterIdentifier</code> is specified for an existing cluster, no snapshots are returned. </p> </li> </ul>
            sorting_entities: <p></p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault: <p>The snapshot identifier does not refer to an existing cluster snapshot.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_cluster_snapshots_message.DescribeClusterSnapshotsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.snapshot_message.SnapshotMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_cluster_snapshots

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_cluster_snapshots.async_describe_cluster_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_cluster_snapshots_message.DescribeClusterSnapshotsMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if snapshot_identifier is not None:
            input_["snapshot_identifier"] = snapshot_identifier
        if snapshot_arn is not None:
            input_["snapshot_arn"] = snapshot_arn
        if snapshot_type is not None:
            input_["snapshot_type"] = snapshot_type
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values
        if cluster_exists is not None:
            input_["cluster_exists"] = cluster_exists
        if sorting_entities is not None:
            input_["sorting_entities"] = sorting_entities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_cluster_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_arn: Optional["capo_redshift.types.string.String"] = None,
        snapshot_type: Optional["capo_redshift.types.string.String"] = None,
        start_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        owner_account: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
        cluster_exists: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        sorting_entities: Optional[
            "capo_redshift.types.snapshot_sorting_entity_list.SnapshotSortingEntityList"
        ] = None,
    ) -> "AsyncIterator[capo_redshift.types.snapshot.Snapshot]":
        _token = marker
        while True:
            _response = await self.describe_cluster_snapshots(
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                snapshot_identifier=snapshot_identifier,
                snapshot_arn=snapshot_arn,
                snapshot_type=snapshot_type,
                start_time=start_time,
                end_time=end_time,
                max_records=max_records,
                marker=_token,
                owner_account=owner_account,
                tag_keys=tag_keys,
                tag_values=tag_values,
                cluster_exists=cluster_exists,
                sorting_entities=sorting_entities,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_cluster_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_subnet_group_name: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "capo_redshift.types.cluster_subnet_group_message.ClusterSubnetGroupMessage":
        """<p>Returns one or more cluster subnet group objects, which contain metadata about your cluster subnet groups. By default, this operation returns information about all cluster subnet groups that are defined in your Amazon Web Services account.</p> <p>If you specify both tag keys and tag values in the same request, Amazon Redshift returns all subnet groups that match any combination of the specified keys and values. For example, if you have <code>owner</code> and <code>environment</code> for tag keys, and <code>admin</code> and <code>test</code> for tag values, all subnet groups that have any combination of those values are returned.</p> <p>If both tag keys and values are omitted from the request, subnet groups are returned regardless of whether they have tag keys or values associated with them.</p>

        Args:
            cluster_subnet_group_name: <p>The name of the cluster subnet group for which information is requested.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeClusterSubnetGroups</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>
            tag_keys: <p>A tag key or keys for which you want to return all matching cluster subnet groups that are associated with the specified key or keys. For example, suppose that you have subnet groups that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag keys associated with them.</p>
            tag_values: <p>A tag value or values for which you want to return all matching cluster subnet groups that are associated with the specified tag value or values. For example, suppose that you have subnet groups that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag values associated with them.</p>

        Raises:
            capo_redshift.errors.cluster_subnet_group_not_found_fault.ClusterSubnetGroupNotFoundFault: <p>The cluster subnet group name does not refer to an existing cluster subnet group.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_cluster_subnet_groups_message.DescribeClusterSubnetGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.cluster_subnet_group_message.ClusterSubnetGroupMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_cluster_subnet_groups

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_cluster_subnet_groups.async_describe_cluster_subnet_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_cluster_subnet_groups_message.DescribeClusterSubnetGroupsMessage = {}
        if cluster_subnet_group_name is not None:
            input_["cluster_subnet_group_name"] = cluster_subnet_group_name
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_cluster_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_subnet_group_name: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "AsyncIterator[capo_redshift.types.cluster_subnet_group.ClusterSubnetGroup]":
        _token = marker
        while True:
            _response = await self.describe_cluster_subnet_groups(
                config_overrides=config_overrides,
                cluster_subnet_group_name=cluster_subnet_group_name,
                max_records=max_records,
                marker=_token,
                tag_keys=tag_keys,
                tag_values=tag_values,
            )
            _page = _resolve_path(_response, ("cluster_subnet_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_cluster_tracks(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        maintenance_track_name: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.track_list_message.TrackListMessage":
        """<p>Returns a list of all the available maintenance tracks.</p>

        Args:
            maintenance_track_name: <p>The name of the maintenance track. </p>
            max_records: <p>An integer value for the maximum number of maintenance tracks to return.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <code>DescribeClusterTracks</code> request exceed the value specified in <code>MaxRecords</code>, Amazon Redshift returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.invalid_cluster_track_fault.InvalidClusterTrackFault: <p>The provided cluster track name is not valid.</p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_cluster_tracks_message.DescribeClusterTracksMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.track_list_message.TrackListMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_cluster_tracks

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_cluster_tracks.async_describe_cluster_tracks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_cluster_tracks_message.DescribeClusterTracksMessage = {}
        if maintenance_track_name is not None:
            input_["maintenance_track_name"] = maintenance_track_name
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_cluster_tracks(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        maintenance_track_name: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.maintenance_track.MaintenanceTrack]":
        _token = marker
        while True:
            _response = await self.describe_cluster_tracks(
                config_overrides=config_overrides,
                maintenance_track_name=maintenance_track_name,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("maintenance_tracks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_cluster_versions(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_version: Optional["capo_redshift.types.string.String"] = None,
        cluster_parameter_group_family: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.cluster_versions_message.ClusterVersionsMessage":
        """<p>Returns descriptions of the available Amazon Redshift cluster versions. You can call this operation even before creating any clusters to learn more about the Amazon Redshift versions. For more information about managing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html">Amazon Redshift Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            cluster_version: <p>The specific cluster version to return.</p> <p>Example: <code>1.0</code> </p>
            cluster_parameter_group_family: <p>The name of a specific cluster parameter group family to return details for.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeClusterVersions</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_cluster_versions_message.DescribeClusterVersionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.cluster_versions_message.ClusterVersionsMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_cluster_versions

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_cluster_versions.async_describe_cluster_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_cluster_versions_message.DescribeClusterVersionsMessage = {}
        if cluster_version is not None:
            input_["cluster_version"] = cluster_version
        if cluster_parameter_group_family is not None:
            input_["cluster_parameter_group_family"] = cluster_parameter_group_family
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_cluster_versions(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_version: Optional["capo_redshift.types.string.String"] = None,
        cluster_parameter_group_family: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.cluster_version.ClusterVersion]":
        _token = marker
        while True:
            _response = await self.describe_cluster_versions(
                config_overrides=config_overrides,
                cluster_version=cluster_version,
                cluster_parameter_group_family=cluster_parameter_group_family,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("cluster_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_custom_domain_associations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        custom_domain_name: Optional[
            "capo_redshift.types.custom_domain_name_string.CustomDomainNameString"
        ] = None,
        custom_domain_certificate_arn: Optional[
            "capo_redshift.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.custom_domain_associations_message.CustomDomainAssociationsMessage":
        """<p>Contains information about custom domain associations for a cluster.</p>

        Args:
            custom_domain_name: <p>The custom domain name for the custom domain association.</p>
            custom_domain_certificate_arn: <p>The certificate Amazon Resource Name (ARN) for the custom domain association.</p>
            max_records: <p>The maximum records setting for the associated custom domain.</p>
            marker: <p>The marker for the custom domain association.</p>

        Raises:
            capo_redshift.errors.custom_domain_association_not_found_fault.CustomDomainAssociationNotFoundFault: <p>An error occurred. The custom domain name couldn't be found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_custom_domain_associations_message.DescribeCustomDomainAssociationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.custom_domain_associations_message.CustomDomainAssociationsMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_custom_domain_associations

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_custom_domain_associations.async_describe_custom_domain_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_custom_domain_associations_message.DescribeCustomDomainAssociationsMessage = {}
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if custom_domain_certificate_arn is not None:
            input_["custom_domain_certificate_arn"] = custom_domain_certificate_arn
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_custom_domain_associations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        custom_domain_name: Optional[
            "capo_redshift.types.custom_domain_name_string.CustomDomainNameString"
        ] = None,
        custom_domain_certificate_arn: Optional[
            "capo_redshift.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.association.Association]":
        _token = marker
        while True:
            _response = await self.describe_custom_domain_associations(
                config_overrides=config_overrides,
                custom_domain_name=custom_domain_name,
                custom_domain_certificate_arn=custom_domain_certificate_arn,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_data_shares(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        data_share_arn: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.describe_data_shares_result.DescribeDataSharesResult":
        """<p>Shows the status of any inbound or outbound datashares available in the specified account.</p>

        Args:
            data_share_arn: <p>The Amazon resource name (ARN) of the datashare to describe details of.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeDataShares</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.invalid_data_share_fault.InvalidDataShareFault: <p>There is an error with the datashare.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_data_shares_message.DescribeDataSharesMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.describe_data_shares_result.DescribeDataSharesResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_data_shares

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_data_shares.async_describe_data_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_data_shares_message.DescribeDataSharesMessage = {}
        if data_share_arn is not None:
            input_["data_share_arn"] = data_share_arn
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_data_shares(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        data_share_arn: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.data_share.DataShare]":
        _token = marker
        while True:
            _response = await self.describe_data_shares(
                config_overrides=config_overrides,
                data_share_arn=data_share_arn,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("data_shares",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_data_shares_for_consumer(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        consumer_arn: Optional["capo_redshift.types.string.String"] = None,
        status: Optional[
            "capo_redshift.types.data_share_status_for_consumer.DataShareStatusForConsumer"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.describe_data_shares_for_consumer_result.DescribeDataSharesForConsumerResult":
        """<p>Returns a list of datashares where the account identifier being called is a consumer account identifier.</p>

        Args:
            consumer_arn: <p>The Amazon Resource Name (ARN) of the consumer namespace that returns in the list of datashares.</p>
            status: <p>An identifier giving the status of a datashare in the consumer cluster. If this field is specified, Amazon Redshift returns the list of datashares that have the specified status.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeDataSharesForConsumer</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.invalid_namespace_fault.InvalidNamespaceFault: <p>The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_data_shares_for_consumer_message.DescribeDataSharesForConsumerMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.describe_data_shares_for_consumer_result.DescribeDataSharesForConsumerResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_data_shares_for_consumer

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_data_shares_for_consumer.async_describe_data_shares_for_consumer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_data_shares_for_consumer_message.DescribeDataSharesForConsumerMessage = {}
        if consumer_arn is not None:
            input_["consumer_arn"] = consumer_arn
        if status is not None:
            input_["status"] = status
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_data_shares_for_consumer(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        consumer_arn: Optional["capo_redshift.types.string.String"] = None,
        status: Optional[
            "capo_redshift.types.data_share_status_for_consumer.DataShareStatusForConsumer"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.data_share.DataShare]":
        _token = marker
        while True:
            _response = await self.describe_data_shares_for_consumer(
                config_overrides=config_overrides,
                consumer_arn=consumer_arn,
                status=status,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("data_shares",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_data_shares_for_producer(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        producer_arn: Optional["capo_redshift.types.string.String"] = None,
        status: Optional[
            "capo_redshift.types.data_share_status_for_producer.DataShareStatusForProducer"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.describe_data_shares_for_producer_result.DescribeDataSharesForProducerResult":
        """<p>Returns a list of datashares when the account identifier being called is a producer account identifier.</p>

        Args:
            producer_arn: <p>The Amazon Resource Name (ARN) of the producer namespace that returns in the list of datashares.</p>
            status: <p>An identifier giving the status of a datashare in the producer. If this field is specified, Amazon Redshift returns the list of datashares that have the specified status.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeDataSharesForProducer</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.invalid_namespace_fault.InvalidNamespaceFault: <p>The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_data_shares_for_producer_message.DescribeDataSharesForProducerMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.describe_data_shares_for_producer_result.DescribeDataSharesForProducerResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_data_shares_for_producer

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_data_shares_for_producer.async_describe_data_shares_for_producer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_data_shares_for_producer_message.DescribeDataSharesForProducerMessage = {}
        if producer_arn is not None:
            input_["producer_arn"] = producer_arn
        if status is not None:
            input_["status"] = status
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_data_shares_for_producer(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        producer_arn: Optional["capo_redshift.types.string.String"] = None,
        status: Optional[
            "capo_redshift.types.data_share_status_for_producer.DataShareStatusForProducer"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.data_share.DataShare]":
        _token = marker
        while True:
            _response = await self.describe_data_shares_for_producer(
                config_overrides=config_overrides,
                producer_arn=producer_arn,
                status=status,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("data_shares",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_default_cluster_parameters(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        parameter_group_family: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.describe_default_cluster_parameters_result.DescribeDefaultClusterParametersResult":
        """<p>Returns a list of parameter settings for the specified parameter group family.</p> <p> For more information about parameters and parameter groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Amazon Redshift Parameter Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            parameter_group_family: <p>The name of the cluster parameter group family.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeDefaultClusterParameters</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_default_cluster_parameters_message.DescribeDefaultClusterParametersMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.describe_default_cluster_parameters_result.DescribeDefaultClusterParametersResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_default_cluster_parameters

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_default_cluster_parameters.async_describe_default_cluster_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_default_cluster_parameters_message.DescribeDefaultClusterParametersMessage = {}
        if parameter_group_family is not None:
            input_["parameter_group_family"] = parameter_group_family
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_default_cluster_parameters(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        parameter_group_family: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.parameter.Parameter]":
        _token = marker
        while True:
            _response = await self.describe_default_cluster_parameters(
                config_overrides=config_overrides,
                parameter_group_family=parameter_group_family,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(
                _response, ("default_cluster_parameters", "parameters")
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("default_cluster_parameters", "marker"))
            if not _token:
                break

    async def describe_endpoint_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        resource_owner: Optional["capo_redshift.types.string.String"] = None,
        endpoint_name: Optional["capo_redshift.types.string.String"] = None,
        vpc_id: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.endpoint_access_list.EndpointAccessList":
        """<p>Describes a Redshift-managed VPC endpoint.</p>

        Args:
            cluster_identifier: <p>The cluster identifier associated with the described endpoint.</p>
            resource_owner: <p>The Amazon Web Services account ID of the owner of the cluster.</p>
            endpoint_name: <p>The name of the endpoint to be described.</p>
            vpc_id: <p>The virtual private cloud (VPC) identifier with access to the cluster.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a <code>Marker</code> is included in the response so that the remaining results can be retrieved.</p>
            marker: <p>An optional pagination token provided by a previous <code>DescribeEndpointAccess</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.endpoint_not_found_fault.EndpointNotFoundFault: <p>The endpoint name doesn't refer to an existing endpoint.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_endpoint_access_message.DescribeEndpointAccessMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.endpoint_access_list.EndpointAccessList"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_endpoint_access.async_describe_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_endpoint_access_message.DescribeEndpointAccessMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if endpoint_name is not None:
            input_["endpoint_name"] = endpoint_name
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_endpoint_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        resource_owner: Optional["capo_redshift.types.string.String"] = None,
        endpoint_name: Optional["capo_redshift.types.string.String"] = None,
        vpc_id: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.endpoint_access.EndpointAccess]":
        _token = marker
        while True:
            _response = await self.describe_endpoint_access(
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                resource_owner=resource_owner,
                endpoint_name=endpoint_name,
                vpc_id=vpc_id,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("endpoint_access_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_endpoint_authorization(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        account: Optional["capo_redshift.types.string.String"] = None,
        grantee: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.endpoint_authorization_list.EndpointAuthorizationList":
        """<p>Describes an endpoint authorization.</p>

        Args:
            cluster_identifier: <p>The cluster identifier of the cluster to access.</p>
            account: <p>The Amazon Web Services account ID of either the cluster owner (grantor) or grantee. If <code>Grantee</code> parameter is true, then the <code>Account</code> value is of the grantor.</p>
            grantee: <p>Indicates whether to check authorization from a grantor or grantee point of view. If true, Amazon Redshift returns endpoint authorizations that you've been granted. If false (default), checks authorization from a grantor point of view.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a <code>Marker</code> is included in the response so that the remaining results can be retrieved.</p>
            marker: <p>An optional pagination token provided by a previous <code>DescribeEndpointAuthorization</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_endpoint_authorization_message.DescribeEndpointAuthorizationMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.endpoint_authorization_list.EndpointAuthorizationList"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_endpoint_authorization

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_endpoint_authorization.async_describe_endpoint_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_endpoint_authorization_message.DescribeEndpointAuthorizationMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if account is not None:
            input_["account"] = account
        if grantee is not None:
            input_["grantee"] = grantee
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_endpoint_authorization(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        account: Optional["capo_redshift.types.string.String"] = None,
        grantee: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.endpoint_authorization.EndpointAuthorization]":
        _token = marker
        while True:
            _response = await self.describe_endpoint_authorization(
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                account=account,
                grantee=grantee,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("endpoint_authorization_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_event_categories(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        source_type: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.event_categories_message.EventCategoriesMessage":
        """<p>Displays a list of event categories for all event source types, or for a specified source type. For a list of the event categories and source types, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html">Amazon Redshift Event Notifications</a>.</p>

        Args:
            source_type: <p>The source type, such as cluster or parameter group, to which the described event categories apply.</p> <p>Valid values: cluster, cluster-snapshot, cluster-parameter-group, cluster-security-group, and scheduled-action.</p>

        Raises:
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_event_categories_message.DescribeEventCategoriesMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.event_categories_message.EventCategoriesMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_event_categories

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_event_categories.async_describe_event_categories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_event_categories_message.DescribeEventCategoriesMessage = {}
        if source_type is not None:
            input_["source_type"] = source_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_events(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        source_identifier: Optional["capo_redshift.types.string.String"] = None,
        source_type: Optional["capo_redshift.types.source_type.SourceType"] = None,
        start_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        duration: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.events_message.EventsMessage":
        """<p>Returns events related to clusters, security groups, snapshots, and parameter groups for the past 14 days. Events specific to a particular cluster, security group, snapshot or parameter group can be obtained by providing the name as a parameter. By default, the past hour of events are returned.</p>

        Args:
            source_identifier: <p>The identifier of the event source for which events will be returned. If this parameter is not specified, then all sources are included in the response.</p> <p>Constraints:</p> <p>If <i>SourceIdentifier</i> is supplied, <i>SourceType</i> must also be provided.</p> <ul> <li> <p>Specify a cluster identifier when <i>SourceType</i> is <code>cluster</code>.</p> </li> <li> <p>Specify a cluster security group name when <i>SourceType</i> is <code>cluster-security-group</code>.</p> </li> <li> <p>Specify a cluster parameter group name when <i>SourceType</i> is <code>cluster-parameter-group</code>.</p> </li> <li> <p>Specify a cluster snapshot identifier when <i>SourceType</i> is <code>cluster-snapshot</code>.</p> </li> </ul>
            source_type: <p>The event source to retrieve events for. If no value is specified, all events are returned.</p> <p>Constraints:</p> <p>If <i>SourceType</i> is supplied, <i>SourceIdentifier</i> must also be provided.</p> <ul> <li> <p>Specify <code>cluster</code> when <i>SourceIdentifier</i> is a cluster identifier.</p> </li> <li> <p>Specify <code>cluster-security-group</code> when <i>SourceIdentifier</i> is a cluster security group name.</p> </li> <li> <p>Specify <code>cluster-parameter-group</code> when <i>SourceIdentifier</i> is a cluster parameter group name.</p> </li> <li> <p>Specify <code>cluster-snapshot</code> when <i>SourceIdentifier</i> is a cluster snapshot identifier.</p> </li> </ul>
            start_time: <p>The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO8601 Wikipedia page.</a> </p> <p>Example: <code>2009-07-08T18:00Z</code> </p>
            end_time: <p>The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO8601 Wikipedia page.</a> </p> <p>Example: <code>2009-07-08T18:00Z</code> </p>
            duration: <p>The number of minutes prior to the time of the request for which to retrieve events. For example, if the request is sent at 18:00 and you specify a duration of 60, then only events which have occurred after 17:00 will be returned.</p> <p>Default: <code>60</code> </p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeEvents</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_events_message.DescribeEventsMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.events_message.EventsMessage"]:
            import capo_redshift._operations.redshift_service_version20121201.describe_events

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_events.async_describe_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_events_message.DescribeEventsMessage = {}
        if source_identifier is not None:
            input_["source_identifier"] = source_identifier
        if source_type is not None:
            input_["source_type"] = source_type
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if duration is not None:
            input_["duration"] = duration
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_events(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        source_identifier: Optional["capo_redshift.types.string.String"] = None,
        source_type: Optional["capo_redshift.types.source_type.SourceType"] = None,
        start_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        duration: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.event.Event]":
        _token = marker
        while True:
            _response = await self.describe_events(
                config_overrides=config_overrides,
                source_identifier=source_identifier,
                source_type=source_type,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_event_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        subscription_name: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "capo_redshift.types.event_subscriptions_message.EventSubscriptionsMessage":
        """<p>Lists descriptions of all the Amazon Redshift event notification subscriptions for a customer account. If you specify a subscription name, lists the description for that subscription.</p> <p>If you specify both tag keys and tag values in the same request, Amazon Redshift returns all event notification subscriptions that match any combination of the specified keys and values. For example, if you have <code>owner</code> and <code>environment</code> for tag keys, and <code>admin</code> and <code>test</code> for tag values, all subscriptions that have any combination of those values are returned.</p> <p>If both tag keys and values are omitted from the request, subscriptions are returned regardless of whether they have tag keys or values associated with them.</p>

        Args:
            subscription_name: <p>The name of the Amazon Redshift event notification subscription to be described.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeEventSubscriptions request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>
            tag_keys: <p>A tag key or keys for which you want to return all matching event notification subscriptions that are associated with the specified key or keys. For example, suppose that you have subscriptions that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag keys associated with them.</p>
            tag_values: <p>A tag value or values for which you want to return all matching event notification subscriptions that are associated with the specified tag value or values. For example, suppose that you have subscriptions that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag values associated with them.</p>

        Raises:
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>An Amazon Redshift event notification subscription with the specified name does not exist.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_event_subscriptions_message.DescribeEventSubscriptionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.event_subscriptions_message.EventSubscriptionsMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_event_subscriptions

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_event_subscriptions.async_describe_event_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_event_subscriptions_message.DescribeEventSubscriptionsMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_event_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        subscription_name: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "AsyncIterator[capo_redshift.types.event_subscription.EventSubscription]":
        _token = marker
        while True:
            _response = await self.describe_event_subscriptions(
                config_overrides=config_overrides,
                subscription_name=subscription_name,
                max_records=max_records,
                marker=_token,
                tag_keys=tag_keys,
                tag_values=tag_values,
            )
            _page = _resolve_path(_response, ("event_subscriptions_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_hsm_client_certificates(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        hsm_client_certificate_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> (
        "capo_redshift.types.hsm_client_certificate_message.HsmClientCertificateMessage"
    ):
        """<p>Returns information about the specified HSM client certificate. If no certificate ID is specified, returns information about all the HSM certificates owned by your Amazon Web Services account.</p> <p>If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM client certificates that match any combination of the specified keys and values. For example, if you have <code>owner</code> and <code>environment</code> for tag keys, and <code>admin</code> and <code>test</code> for tag values, all HSM client certificates that have any combination of those values are returned.</p> <p>If both tag keys and values are omitted from the request, HSM client certificates are returned regardless of whether they have tag keys or values associated with them.</p>

        Args:
            hsm_client_certificate_identifier: <p>The identifier of a specific HSM client certificate for which you want information. If no identifier is specified, information is returned for all HSM client certificates owned by your Amazon Web Services account.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeHsmClientCertificates</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>
            tag_keys: <p>A tag key or keys for which you want to return all matching HSM client certificates that are associated with the specified key or keys. For example, suppose that you have HSM client certificates that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag keys associated with them.</p>
            tag_values: <p>A tag value or values for which you want to return all matching HSM client certificates that are associated with the specified tag value or values. For example, suppose that you have HSM client certificates that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag values associated with them.</p>

        Raises:
            capo_redshift.errors.hsm_client_certificate_not_found_fault.HsmClientCertificateNotFoundFault: <p>There is no Amazon Redshift HSM client certificate with the specified identifier.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_hsm_client_certificates_message.DescribeHsmClientCertificatesMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.hsm_client_certificate_message.HsmClientCertificateMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_hsm_client_certificates

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_hsm_client_certificates.async_describe_hsm_client_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_hsm_client_certificates_message.DescribeHsmClientCertificatesMessage = {}
        if hsm_client_certificate_identifier is not None:
            input_["hsm_client_certificate_identifier"] = (
                hsm_client_certificate_identifier
            )
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_hsm_client_certificates(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        hsm_client_certificate_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> (
        "AsyncIterator[capo_redshift.types.hsm_client_certificate.HsmClientCertificate]"
    ):
        _token = marker
        while True:
            _response = await self.describe_hsm_client_certificates(
                config_overrides=config_overrides,
                hsm_client_certificate_identifier=hsm_client_certificate_identifier,
                max_records=max_records,
                marker=_token,
                tag_keys=tag_keys,
                tag_values=tag_values,
            )
            _page = _resolve_path(_response, ("hsm_client_certificates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_hsm_configurations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        hsm_configuration_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "capo_redshift.types.hsm_configuration_message.HsmConfigurationMessage":
        """<p>Returns information about the specified Amazon Redshift HSM configuration. If no configuration ID is specified, returns information about all the HSM configurations owned by your Amazon Web Services account.</p> <p>If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM connections that match any combination of the specified keys and values. For example, if you have <code>owner</code> and <code>environment</code> for tag keys, and <code>admin</code> and <code>test</code> for tag values, all HSM connections that have any combination of those values are returned.</p> <p>If both tag keys and values are omitted from the request, HSM connections are returned regardless of whether they have tag keys or values associated with them.</p>

        Args:
            hsm_configuration_identifier: <p>The identifier of a specific Amazon Redshift HSM configuration to be described. If no identifier is specified, information is returned for all HSM configurations owned by your Amazon Web Services account.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeHsmConfigurations</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>
            tag_keys: <p>A tag key or keys for which you want to return all matching HSM configurations that are associated with the specified key or keys. For example, suppose that you have HSM configurations that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag keys associated with them.</p>
            tag_values: <p>A tag value or values for which you want to return all matching HSM configurations that are associated with the specified tag value or values. For example, suppose that you have HSM configurations that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag values associated with them.</p>

        Raises:
            capo_redshift.errors.hsm_configuration_not_found_fault.HsmConfigurationNotFoundFault: <p>There is no Amazon Redshift HSM configuration with the specified identifier.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_hsm_configurations_message.DescribeHsmConfigurationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.hsm_configuration_message.HsmConfigurationMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_hsm_configurations

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_hsm_configurations.async_describe_hsm_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_hsm_configurations_message.DescribeHsmConfigurationsMessage = {}
        if hsm_configuration_identifier is not None:
            input_["hsm_configuration_identifier"] = hsm_configuration_identifier
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_hsm_configurations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        hsm_configuration_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "AsyncIterator[capo_redshift.types.hsm_configuration.HsmConfiguration]":
        _token = marker
        while True:
            _response = await self.describe_hsm_configurations(
                config_overrides=config_overrides,
                hsm_configuration_identifier=hsm_configuration_identifier,
                max_records=max_records,
                marker=_token,
                tag_keys=tag_keys,
                tag_values=tag_values,
            )
            _page = _resolve_path(_response, ("hsm_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_inbound_integrations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        integration_arn: Optional[
            "capo_redshift.types.inbound_integration_arn.InboundIntegrationArn"
        ] = None,
        target_arn: Optional["capo_redshift.types.target_arn.TargetArn"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.inbound_integrations_message.InboundIntegrationsMessage":
        """<p>Returns a list of inbound integrations.</p>

        Args:
            integration_arn: <p>The Amazon Resource Name (ARN) of the inbound integration.</p>
            target_arn: <p>The Amazon Resource Name (ARN) of the target of an inbound integration.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeInboundIntegrations</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.integration_not_found_fault.IntegrationNotFoundFault: <p>The integration can't be found.</p>
            capo_redshift.errors.invalid_namespace_fault.InvalidNamespaceFault: <p>The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_inbound_integrations_message.DescribeInboundIntegrationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.inbound_integrations_message.InboundIntegrationsMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_inbound_integrations

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_inbound_integrations.async_describe_inbound_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_inbound_integrations_message.DescribeInboundIntegrationsMessage = {}
        if integration_arn is not None:
            input_["integration_arn"] = integration_arn
        if target_arn is not None:
            input_["target_arn"] = target_arn
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_inbound_integrations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        integration_arn: Optional[
            "capo_redshift.types.inbound_integration_arn.InboundIntegrationArn"
        ] = None,
        target_arn: Optional["capo_redshift.types.target_arn.TargetArn"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.inbound_integration.InboundIntegration]":
        _token = marker
        while True:
            _response = await self.describe_inbound_integrations(
                config_overrides=config_overrides,
                integration_arn=integration_arn,
                target_arn=target_arn,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("inbound_integrations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_integrations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        integration_arn: Optional[
            "capo_redshift.types.integration_arn.IntegrationArn"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        filters: Optional[
            "capo_redshift.types.describe_integrations_filter_list.DescribeIntegrationsFilterList"
        ] = None,
    ) -> "capo_redshift.types.integrations_message.IntegrationsMessage":
        """<p>Describes one or more zero-ETL or S3 event integrations with Amazon Redshift.</p>

        Args:
            integration_arn: <p>The unique identifier of the integration.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous <code>DescribeIntegrations</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>
            filters: <p>A filter that specifies one or more resources to return.</p>

        Raises:
            capo_redshift.errors.integration_not_found_fault.IntegrationNotFoundFault: <p>The integration can't be found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_integrations_message.DescribeIntegrationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.integrations_message.IntegrationsMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_integrations

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_integrations.async_describe_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_integrations_message.DescribeIntegrationsMessage = {}
        if integration_arn is not None:
            input_["integration_arn"] = integration_arn
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_integrations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        integration_arn: Optional[
            "capo_redshift.types.integration_arn.IntegrationArn"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        filters: Optional[
            "capo_redshift.types.describe_integrations_filter_list.DescribeIntegrationsFilterList"
        ] = None,
    ) -> "AsyncIterator[capo_redshift.types.integration.Integration]":
        _token = marker
        while True:
            _response = await self.describe_integrations(
                config_overrides=config_overrides,
                integration_arn=integration_arn,
                max_records=max_records,
                marker=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("integrations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_logging_status(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.logging_status.LoggingStatus":
        """<p>Describes whether information, such as queries and connection attempts, is being logged for the specified Amazon Redshift cluster.</p>

        Args:
            cluster_identifier: <p>The identifier of the cluster from which to get the logging status.</p> <p>Example: <code>examplecluster</code> </p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_logging_status_message.DescribeLoggingStatusMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.logging_status.LoggingStatus"]:
            import capo_redshift._operations.redshift_service_version20121201.describe_logging_status

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_logging_status.async_describe_logging_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_logging_status_message.DescribeLoggingStatusMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_node_configuration_options(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        action_type: Optional["capo_redshift.types.action_type.ActionType"] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_arn: Optional["capo_redshift.types.string.String"] = None,
        owner_account: Optional["capo_redshift.types.string.String"] = None,
        filters: Optional[
            "capo_redshift.types.node_configuration_options_filter_list.NodeConfigurationOptionsFilterList"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_redshift.types.node_configuration_options_message.NodeConfigurationOptionsMessage":
        """<p>Returns properties of possible node configurations such as node type, number of nodes, and disk usage for the specified action type.</p>

        Args:
            action_type: <p>The action type to evaluate for possible node configurations. Specify "restore-cluster" to get configuration combinations based on an existing snapshot. Specify "recommend-node-config" to get configuration recommendations based on an existing cluster or snapshot. Specify "resize-cluster" to get configuration combinations for elastic resize based on an existing cluster. </p>
            cluster_identifier: <p>The identifier of the cluster to evaluate for possible node configurations.</p>
            snapshot_identifier: <p>The identifier of the snapshot to evaluate for possible node configurations.</p>
            snapshot_arn: <p>The Amazon Resource Name (ARN) of the snapshot associated with the message to describe node configuration.</p>
            owner_account: <p>The Amazon Web Services account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.</p>
            filters: <p>A set of name, operator, and value items to filter the results.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeNodeConfigurationOptions</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>500</code> </p> <p>Constraints: minimum 100, maximum 500.</p>

        Raises:
            capo_redshift.errors.access_to_snapshot_denied_fault.AccessToSnapshotDeniedFault: <p>The owner of the specified snapshot has not authorized your account to access the snapshot.</p>
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault: <p>The snapshot identifier does not refer to an existing cluster snapshot.</p>
            capo_redshift.errors.invalid_cluster_snapshot_state_fault.InvalidClusterSnapshotStateFault: <p>The specified cluster snapshot is not in the <code>available</code> state, or other accounts are authorized to access the snapshot. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_node_configuration_options_message.DescribeNodeConfigurationOptionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.node_configuration_options_message.NodeConfigurationOptionsMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_node_configuration_options

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_node_configuration_options.async_describe_node_configuration_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_node_configuration_options_message.DescribeNodeConfigurationOptionsMessage = {}
        if action_type is not None:
            input_["action_type"] = action_type
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if snapshot_identifier is not None:
            input_["snapshot_identifier"] = snapshot_identifier
        if snapshot_arn is not None:
            input_["snapshot_arn"] = snapshot_arn
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if filters is not None:
            input_["filters"] = filters
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_node_configuration_options(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        action_type: Optional["capo_redshift.types.action_type.ActionType"] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_arn: Optional["capo_redshift.types.string.String"] = None,
        owner_account: Optional["capo_redshift.types.string.String"] = None,
        filters: Optional[
            "capo_redshift.types.node_configuration_options_filter_list.NodeConfigurationOptionsFilterList"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_redshift.types.node_configuration_option.NodeConfigurationOption]":
        _token = marker
        while True:
            _response = await self.describe_node_configuration_options(
                config_overrides=config_overrides,
                action_type=action_type,
                cluster_identifier=cluster_identifier,
                snapshot_identifier=snapshot_identifier,
                snapshot_arn=snapshot_arn,
                owner_account=owner_account,
                filters=filters,
                marker=_token,
                max_records=max_records,
            )
            _page = _resolve_path(_response, ("node_configuration_option_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_orderable_cluster_options(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_version: Optional["capo_redshift.types.string.String"] = None,
        node_type: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.orderable_cluster_options_message.OrderableClusterOptionsMessage":
        """<p>Returns a list of orderable cluster options. Before you create a new cluster you can use this operation to find what options are available, such as the EC2 Availability Zones (AZ) in the specific Amazon Web Services Region that you can specify, and the node types you can request. The node types differ by available storage, memory, CPU and price. With the cost involved you might want to obtain a list of cluster options in the specific region and specify values when creating a cluster. For more information about managing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html">Amazon Redshift Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            cluster_version: <p>The version filter value. Specify this parameter to show only the available offerings matching the specified version.</p> <p>Default: All versions.</p> <p>Constraints: Must be one of the version returned from <a>DescribeClusterVersions</a>.</p>
            node_type: <p>The node type filter value. Specify this parameter to show only the available offerings matching the specified node type.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeOrderableClusterOptions</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_orderable_cluster_options_message.DescribeOrderableClusterOptionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.orderable_cluster_options_message.OrderableClusterOptionsMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_orderable_cluster_options

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_orderable_cluster_options.async_describe_orderable_cluster_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_orderable_cluster_options_message.DescribeOrderableClusterOptionsMessage = {}
        if cluster_version is not None:
            input_["cluster_version"] = cluster_version
        if node_type is not None:
            input_["node_type"] = node_type
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_orderable_cluster_options(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_version: Optional["capo_redshift.types.string.String"] = None,
        node_type: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.orderable_cluster_option.OrderableClusterOption]":
        _token = marker
        while True:
            _response = await self.describe_orderable_cluster_options(
                config_overrides=config_overrides,
                cluster_version=cluster_version,
                node_type=node_type,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("orderable_cluster_options",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_partners(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        account_id: Optional[
            "capo_redshift.types.partner_integration_account_id.PartnerIntegrationAccountId"
        ] = None,
        cluster_identifier: Optional[
            "capo_redshift.types.partner_integration_cluster_identifier.PartnerIntegrationClusterIdentifier"
        ] = None,
        database_name: Optional[
            "capo_redshift.types.partner_integration_database_name.PartnerIntegrationDatabaseName"
        ] = None,
        partner_name: Optional[
            "capo_redshift.types.partner_integration_partner_name.PartnerIntegrationPartnerName"
        ] = None,
    ) -> "capo_redshift.types.describe_partners_output_message.DescribePartnersOutputMessage":
        """<p>Returns information about the partner integrations defined for a cluster.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID that owns the cluster.</p>
            cluster_identifier: <p>The cluster identifier of the cluster whose partner integration is being described.</p>
            database_name: <p>The name of the database whose partner integration is being described. If database name is not specified, then all databases in the cluster are described.</p>
            partner_name: <p>The name of the partner that is being described. If partner name is not specified, then all partner integrations are described.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.unauthorized_partner_integration_fault.UnauthorizedPartnerIntegrationFault: <p>The partner integration is not authorized.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_partners_input_message.DescribePartnersInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.describe_partners_output_message.DescribePartnersOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_partners

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_partners.async_describe_partners(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_partners_input_message.DescribePartnersInputMessage = {}
        if account_id is not None:
            input_["account_id"] = account_id
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if database_name is not None:
            input_["database_name"] = database_name
        if partner_name is not None:
            input_["partner_name"] = partner_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_qev2_idc_applications(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        qev2_idc_application_arn: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.describe_qev2_idc_applications_result.DescribeQev2IdcApplicationsResult":
        """<p>Lists the Amazon Redshift Query Editor (QEV2) IAM Identity Center applications. To retrieve additional results, use the MaxRecords and Marker parameters.</p>

        Args:
            qev2_idc_application_arn: <p>The Amazon Resource Name (ARN) for the Amazon Redshift Query Editor (QEV2) application that integrates with IAM Identity Center.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.</p>
            marker: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request. </p>

        Raises:
            capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault: <p>A dependent service denied access for the integration.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.qev2_idc_application_not_exists_fault.Qev2IdcApplicationNotExistsFault: <p>The specified Amazon Redshift Query Editor (QEV2) IAM Identity Center application doesn't exist. Verify that the application ARN is correct and that the application exists in this Region.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_qev2_idc_applications_message.DescribeQev2IdcApplicationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.describe_qev2_idc_applications_result.DescribeQev2IdcApplicationsResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_qev2_idc_applications

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_qev2_idc_applications.async_describe_qev2_idc_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_qev2_idc_applications_message.DescribeQev2IdcApplicationsMessage = {}
        if qev2_idc_application_arn is not None:
            input_["qev2_idc_application_arn"] = qev2_idc_application_arn
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_qev2_idc_applications(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        qev2_idc_application_arn: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.qev2_idc_application.Qev2IdcApplication]":
        _token = marker
        while True:
            _response = await self.describe_qev2_idc_applications(
                config_overrides=config_overrides,
                qev2_idc_application_arn=qev2_idc_application_arn,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("qev2_idc_applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_redshift_idc_applications(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        redshift_idc_application_arn: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.describe_redshift_idc_applications_result.DescribeRedshiftIdcApplicationsResult":
        """<p>Lists the Amazon Redshift IAM Identity Center applications.</p>

        Args:
            redshift_idc_application_arn: <p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.</p>
            marker: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request. </p>

        Raises:
            capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault: <p>A dependent service denied access for the integration.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.redshift_idc_application_not_exists_fault.RedshiftIdcApplicationNotExistsFault: <p>The application you attempted to find doesn't exist.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_redshift_idc_applications_message.DescribeRedshiftIdcApplicationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.describe_redshift_idc_applications_result.DescribeRedshiftIdcApplicationsResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_redshift_idc_applications

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_redshift_idc_applications.async_describe_redshift_idc_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_redshift_idc_applications_message.DescribeRedshiftIdcApplicationsMessage = {}
        if redshift_idc_application_arn is not None:
            input_["redshift_idc_application_arn"] = redshift_idc_application_arn
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_redshift_idc_applications(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        redshift_idc_application_arn: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.redshift_idc_application.RedshiftIdcApplication]":
        _token = marker
        while True:
            _response = await self.describe_redshift_idc_applications(
                config_overrides=config_overrides,
                redshift_idc_application_arn=redshift_idc_application_arn,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("redshift_idc_applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_reserved_node_exchange_status(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        reserved_node_id: Optional["capo_redshift.types.string.String"] = None,
        reserved_node_exchange_request_id: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.describe_reserved_node_exchange_status_output_message.DescribeReservedNodeExchangeStatusOutputMessage":
        """<p>Returns exchange status details and associated metadata for a reserved-node exchange. Statuses include such values as in progress and requested.</p>

        Args:
            reserved_node_id: <p>The identifier of the source reserved node in a reserved-node exchange request.</p>
            reserved_node_exchange_request_id: <p>The identifier of the reserved-node exchange request.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>Marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.</p>
            marker: <p>An optional pagination token provided by a previous <code>DescribeReservedNodeExchangeStatus</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request.</p>

        Raises:
            capo_redshift.errors.reserved_node_exchange_not_found_fault.ReservedNodeExchangeNotFoundFault: <p>The reserved-node exchange status wasn't found.</p>
            capo_redshift.errors.reserved_node_not_found_fault.ReservedNodeNotFoundFault: <p>The specified reserved compute node not found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_reserved_node_exchange_status_input_message.DescribeReservedNodeExchangeStatusInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.describe_reserved_node_exchange_status_output_message.DescribeReservedNodeExchangeStatusOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_reserved_node_exchange_status

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_reserved_node_exchange_status.async_describe_reserved_node_exchange_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_reserved_node_exchange_status_input_message.DescribeReservedNodeExchangeStatusInputMessage = {}
        if reserved_node_id is not None:
            input_["reserved_node_id"] = reserved_node_id
        if reserved_node_exchange_request_id is not None:
            input_["reserved_node_exchange_request_id"] = (
                reserved_node_exchange_request_id
            )
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_reserved_node_exchange_status(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        reserved_node_id: Optional["capo_redshift.types.string.String"] = None,
        reserved_node_exchange_request_id: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.reserved_node_exchange_status.ReservedNodeExchangeStatus]":
        _token = marker
        while True:
            _response = await self.describe_reserved_node_exchange_status(
                config_overrides=config_overrides,
                reserved_node_id=reserved_node_id,
                reserved_node_exchange_request_id=reserved_node_exchange_request_id,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("reserved_node_exchange_status_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_reserved_node_offerings(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        reserved_node_offering_id: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.reserved_node_offerings_message.ReservedNodeOfferingsMessage":
        """<p>Returns a list of the available reserved node offerings by Amazon Redshift with their descriptions including the node type, the fixed and recurring costs of reserving the node and duration the node will be reserved for you. These descriptions help you determine which reserve node offering you want to purchase. You then use the unique offering ID in you call to <a>PurchaseReservedNodeOffering</a> to reserve one or more nodes for your Amazon Redshift cluster. </p> <p> For more information about reserved node offerings, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html">Purchasing Reserved Nodes</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            reserved_node_offering_id: <p>The unique identifier for the offering.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeReservedNodeOfferings</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.reserved_node_offering_not_found_fault.ReservedNodeOfferingNotFoundFault: <p>Specified offering does not exist.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_reserved_node_offerings_message.DescribeReservedNodeOfferingsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.reserved_node_offerings_message.ReservedNodeOfferingsMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_reserved_node_offerings

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_reserved_node_offerings.async_describe_reserved_node_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_reserved_node_offerings_message.DescribeReservedNodeOfferingsMessage = {}
        if reserved_node_offering_id is not None:
            input_["reserved_node_offering_id"] = reserved_node_offering_id
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_reserved_node_offerings(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        reserved_node_offering_id: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> (
        "AsyncIterator[capo_redshift.types.reserved_node_offering.ReservedNodeOffering]"
    ):
        _token = marker
        while True:
            _response = await self.describe_reserved_node_offerings(
                config_overrides=config_overrides,
                reserved_node_offering_id=reserved_node_offering_id,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("reserved_node_offerings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_reserved_nodes(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        reserved_node_id: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.reserved_nodes_message.ReservedNodesMessage":
        """<p>Returns the descriptions of the reserved nodes.</p>

        Args:
            reserved_node_id: <p>Identifier for the node reservation.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeReservedNodes</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>

        Raises:
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.reserved_node_not_found_fault.ReservedNodeNotFoundFault: <p>The specified reserved compute node not found.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_reserved_nodes_message.DescribeReservedNodesMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.reserved_nodes_message.ReservedNodesMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_reserved_nodes

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_reserved_nodes.async_describe_reserved_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_reserved_nodes_message.DescribeReservedNodesMessage = {}
        if reserved_node_id is not None:
            input_["reserved_node_id"] = reserved_node_id
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_reserved_nodes(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        reserved_node_id: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.reserved_node.ReservedNode]":
        _token = marker
        while True:
            _response = await self.describe_reserved_nodes(
                config_overrides=config_overrides,
                reserved_node_id=reserved_node_id,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("reserved_nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_resize(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.resize_progress_message.ResizeProgressMessage":
        """<p>Returns information about the last resize operation for the specified cluster. If no resize operation has ever been initiated for the specified cluster, a <code>HTTP 404</code> error is returned. If a resize operation was initiated and completed, the status of the resize remains as <code>SUCCEEDED</code> until the next resize. </p> <p>A resize operation can be requested using <a>ModifyCluster</a> and specifying a different number or type of nodes for the cluster. </p>

        Args:
            cluster_identifier: <p>The unique identifier of a cluster whose resize progress you are requesting. This parameter is case-sensitive.</p> <p>By default, resize operations for all clusters defined for an Amazon Web Services account are returned.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.resize_not_found_fault.ResizeNotFoundFault: <p>A resize operation for the specified cluster is not found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_resize_message.DescribeResizeMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.resize_progress_message.ResizeProgressMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_resize

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_resize.async_describe_resize(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_resize_message.DescribeResizeMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_scheduled_actions(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        scheduled_action_name: Optional["capo_redshift.types.string.String"] = None,
        target_action_type: Optional[
            "capo_redshift.types.scheduled_action_type_values.ScheduledActionTypeValues"
        ] = None,
        start_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        active: Optional["capo_redshift.types.boolean_optional.BooleanOptional"] = None,
        filters: Optional[
            "capo_redshift.types.scheduled_action_filter_list.ScheduledActionFilterList"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_redshift.types.scheduled_actions_message.ScheduledActionsMessage":
        """<p>Describes properties of scheduled actions. </p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action to retrieve. </p>
            target_action_type: <p>The type of the scheduled actions to retrieve. </p>
            start_time: <p>The start time in UTC of the scheduled actions to retrieve. Only active scheduled actions that have invocations after this time are retrieved.</p>
            end_time: <p>The end time in UTC of the scheduled action to retrieve. Only active scheduled actions that have invocations before this time are retrieved.</p>
            active: <p>If true, retrieve only active scheduled actions. If false, retrieve only disabled scheduled actions. </p>
            filters: <p>List of scheduled action filters. </p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeScheduledActions</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>

        Raises:
            capo_redshift.errors.scheduled_action_not_found_fault.ScheduledActionNotFoundFault: <p>The scheduled action cannot be found. </p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_scheduled_actions_message.DescribeScheduledActionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.scheduled_actions_message.ScheduledActionsMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_scheduled_actions

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_scheduled_actions.async_describe_scheduled_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_scheduled_actions_message.DescribeScheduledActionsMessage = {}
        if scheduled_action_name is not None:
            input_["scheduled_action_name"] = scheduled_action_name
        if target_action_type is not None:
            input_["target_action_type"] = target_action_type
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if active is not None:
            input_["active"] = active
        if filters is not None:
            input_["filters"] = filters
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_scheduled_actions(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        scheduled_action_name: Optional["capo_redshift.types.string.String"] = None,
        target_action_type: Optional[
            "capo_redshift.types.scheduled_action_type_values.ScheduledActionTypeValues"
        ] = None,
        start_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        active: Optional["capo_redshift.types.boolean_optional.BooleanOptional"] = None,
        filters: Optional[
            "capo_redshift.types.scheduled_action_filter_list.ScheduledActionFilterList"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_redshift.types.scheduled_action.ScheduledAction]":
        _token = marker
        while True:
            _response = await self.describe_scheduled_actions(
                config_overrides=config_overrides,
                scheduled_action_name=scheduled_action_name,
                target_action_type=target_action_type,
                start_time=start_time,
                end_time=end_time,
                active=active,
                filters=filters,
                marker=_token,
                max_records=max_records,
            )
            _page = _resolve_path(_response, ("scheduled_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_snapshot_copy_grants(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        snapshot_copy_grant_name: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "capo_redshift.types.snapshot_copy_grant_message.SnapshotCopyGrantMessage":
        """<p>Returns a list of snapshot copy grants owned by the Amazon Web Services account in the destination region.</p> <p> For more information about managing snapshot copy grants, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html">Amazon Redshift Database Encryption</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>

        Args:
            snapshot_copy_grant_name: <p>The name of the snapshot copy grant.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <code>DescribeSnapshotCopyGrant</code> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p> <p>Constraints: You can specify either the <b>SnapshotCopyGrantName</b> parameter or the <b>Marker</b> parameter, but not both. </p>
            tag_keys: <p>A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.</p>
            tag_values: <p>A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.</p>

        Raises:
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.snapshot_copy_grant_not_found_fault.SnapshotCopyGrantNotFoundFault: <p>The specified snapshot copy grant can't be found. Make sure that the name is typed correctly and that the grant exists in the destination region.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_snapshot_copy_grants_message.DescribeSnapshotCopyGrantsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.snapshot_copy_grant_message.SnapshotCopyGrantMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_snapshot_copy_grants

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_snapshot_copy_grants.async_describe_snapshot_copy_grants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_snapshot_copy_grants_message.DescribeSnapshotCopyGrantsMessage = {}
        if snapshot_copy_grant_name is not None:
            input_["snapshot_copy_grant_name"] = snapshot_copy_grant_name
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_snapshot_copy_grants(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        snapshot_copy_grant_name: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "AsyncIterator[capo_redshift.types.snapshot_copy_grant.SnapshotCopyGrant]":
        _token = marker
        while True:
            _response = await self.describe_snapshot_copy_grants(
                config_overrides=config_overrides,
                snapshot_copy_grant_name=snapshot_copy_grant_name,
                max_records=max_records,
                marker=_token,
                tag_keys=tag_keys,
                tag_values=tag_values,
            )
            _page = _resolve_path(_response, ("snapshot_copy_grants",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_snapshot_schedules(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        schedule_identifier: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_redshift.types.describe_snapshot_schedules_output_message.DescribeSnapshotSchedulesOutputMessage":
        """<p>Returns a list of snapshot schedules. </p>

        Args:
            cluster_identifier: <p>The unique identifier for the cluster whose snapshot schedules you want to view.</p>
            schedule_identifier: <p>A unique identifier for a snapshot schedule.</p>
            tag_keys: <p>The key value for a snapshot schedule tag.</p>
            tag_values: <p>The value corresponding to the key of the snapshot schedule tag.</p>
            marker: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>marker</code> parameter and retrying the command. If the <code>marker</code> field is empty, all response records have been retrieved for the request.</p>
            max_records: <p>The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned <code>marker</code> value.</p>

        Raises:
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_snapshot_schedules_message.DescribeSnapshotSchedulesMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.describe_snapshot_schedules_output_message.DescribeSnapshotSchedulesOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_snapshot_schedules

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_snapshot_schedules.async_describe_snapshot_schedules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_snapshot_schedules_message.DescribeSnapshotSchedulesMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_snapshot_schedules(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        schedule_identifier: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_redshift.types.snapshot_schedule.SnapshotSchedule]":
        _token = marker
        while True:
            _response = await self.describe_snapshot_schedules(
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                schedule_identifier=schedule_identifier,
                tag_keys=tag_keys,
                tag_values=tag_values,
                marker=_token,
                max_records=max_records,
            )
            _page = _resolve_path(_response, ("snapshot_schedules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_storage(
        self, *, config_overrides: Optional[AsyncRedshiftClientConfig] = None
    ) -> "capo_redshift.types.customer_storage_message.CustomerStorageMessage":
        """<p>Returns account level backups storage size and provisional storage.</p>

        Raises:
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.customer_storage_message.CustomerStorageMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_storage

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_storage.async_describe_storage(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_table_restore_status(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        table_restore_request_id: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.table_restore_status_message.TableRestoreStatusMessage":
        """<p>Lists the status of one or more table restore requests made using the <a>RestoreTableFromClusterSnapshot</a> API action. If you don't specify a value for the <code>TableRestoreRequestId</code> parameter, then <code>DescribeTableRestoreStatus</code> returns the status of all table restore requests ordered by the date and time of the request in ascending order. Otherwise <code>DescribeTableRestoreStatus</code> returns the status of the table specified by <code>TableRestoreRequestId</code>.</p>

        Args:
            cluster_identifier: <p>The Amazon Redshift cluster that the table is being restored to.</p>
            table_restore_request_id: <p>The identifier of the table restore request to return status for. If you don't specify a <code>TableRestoreRequestId</code> value, then <code>DescribeTableRestoreStatus</code> returns the status of all in-progress table restore requests.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p>
            marker: <p>An optional pagination token provided by a previous <code>DescribeTableRestoreStatus</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.table_restore_not_found_fault.TableRestoreNotFoundFault: <p>The specified <code>TableRestoreRequestId</code> value was not found.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_table_restore_status_message.DescribeTableRestoreStatusMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.table_restore_status_message.TableRestoreStatusMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_table_restore_status

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_table_restore_status.async_describe_table_restore_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_table_restore_status_message.DescribeTableRestoreStatusMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if table_restore_request_id is not None:
            input_["table_restore_request_id"] = table_restore_request_id
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_table_restore_status(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        table_restore_request_id: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.table_restore_status.TableRestoreStatus]":
        _token = marker
        while True:
            _response = await self.describe_table_restore_status(
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                table_restore_request_id=table_restore_request_id,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("table_restore_status_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_tags(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        resource_name: Optional["capo_redshift.types.string.String"] = None,
        resource_type: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "capo_redshift.types.tagged_resource_list_message.TaggedResourceListMessage":
        """<p>Returns a list of tags. You can return tags from a specific resource by specifying an ARN, or you can return all tags for a given type of resource, such as clusters, snapshots, and so on.</p> <p>The following are limitations for <code>DescribeTags</code>: </p> <ul> <li> <p>You cannot specify an ARN and a resource-type value together in the same request.</p> </li> <li> <p>You cannot use the <code>MaxRecords</code> and <code>Marker</code> parameters together with the ARN parameter.</p> </li> <li> <p>The <code>MaxRecords</code> parameter can be a range from 10 to 50 results to return in a request.</p> </li> </ul> <p>If you specify both tag keys and tag values in the same request, Amazon Redshift returns all resources that match any combination of the specified keys and values. For example, if you have <code>owner</code> and <code>environment</code> for tag keys, and <code>admin</code> and <code>test</code> for tag values, all resources that have any combination of those values are returned.</p> <p>If both tag keys and values are omitted from the request, resources are returned regardless of whether they have tag keys or values associated with them.</p>

        Args:
            resource_name: <p>The Amazon Resource Name (ARN) for which you want to describe the tag or tags. For example, <code>arn:aws:redshift:us-east-2:123456789:cluster:t1</code>. </p>
            resource_type: <p>The type of resource with which you want to view tags. Valid resource types are: </p> <ul> <li> <p>Cluster</p> </li> <li> <p>CIDR/IP</p> </li> <li> <p>EC2 security group</p> </li> <li> <p>Snapshot</p> </li> <li> <p>Cluster security group</p> </li> <li> <p>Subnet group</p> </li> <li> <p>HSM connection</p> </li> <li> <p>HSM certificate</p> </li> <li> <p>Parameter group</p> </li> <li> <p>Snapshot copy grant</p> </li> <li> <p>Integration (zero-ETL integration or S3 event integration)</p> <note> <p>To describe the tags associated with an <code>integration</code>, don't specify <code>ResourceType</code>, instead specify the <code>ResourceName</code> of the integration.</p> </note> </li> </ul> <p>For more information about Amazon Redshift resource types and constructing ARNs, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-iam-access-control-specify-actions">Specifying Policy Elements: Actions, Effects, Resources, and Principals</a> in the Amazon Redshift Cluster Management Guide. </p>
            max_records: <p>The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned <code>marker</code> value. </p>
            marker: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>marker</code> parameter and retrying the command. If the <code>marker</code> field is empty, all response records have been retrieved for the request. </p>
            tag_keys: <p>A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.</p>
            tag_values: <p>A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.</p>

        Raises:
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_tags_message.DescribeTagsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.tagged_resource_list_message.TaggedResourceListMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_tags

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_tags.async_describe_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_tags_message.DescribeTagsMessage = {}
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_tags(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        resource_name: Optional["capo_redshift.types.string.String"] = None,
        resource_type: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "AsyncIterator[capo_redshift.types.tagged_resource.TaggedResource]":
        _token = marker
        while True:
            _response = await self.describe_tags(
                config_overrides=config_overrides,
                resource_name=resource_name,
                resource_type=resource_type,
                max_records=max_records,
                marker=_token,
                tag_keys=tag_keys,
                tag_values=tag_values,
            )
            _page = _resolve_path(_response, ("tagged_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_usage_limits(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        usage_limit_id: Optional["capo_redshift.types.string.String"] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        feature_type: Optional[
            "capo_redshift.types.usage_limit_feature_type.UsageLimitFeatureType"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "capo_redshift.types.usage_limit_list.UsageLimitList":
        """<p>Shows usage limits on a cluster. Results are filtered based on the combination of input usage limit identifier, cluster identifier, and feature type parameters:</p> <ul> <li> <p>If usage limit identifier, cluster identifier, and feature type are not provided, then all usage limit objects for the current account in the current region are returned.</p> </li> <li> <p>If usage limit identifier is provided, then the corresponding usage limit object is returned.</p> </li> <li> <p>If cluster identifier is provided, then all usage limit objects for the specified cluster are returned.</p> </li> <li> <p>If cluster identifier and feature type are provided, then all usage limit objects for the combination of cluster and feature are returned.</p> </li> </ul>

        Args:
            usage_limit_id: <p>The identifier of the usage limit to describe.</p>
            cluster_identifier: <p>The identifier of the cluster for which you want to describe usage limits.</p>
            feature_type: <p>The feature type for which you want to describe usage limits.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>
            marker: <p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeUsageLimits</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>
            tag_keys: <p>A tag key or keys for which you want to return all matching usage limit objects that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the usage limit objects have either or both of these tag keys associated with them.</p>
            tag_values: <p>A tag value or values for which you want to return all matching usage limit objects that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the usage limit objects that have either or both of these tag values associated with them.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.describe_usage_limits_message.DescribeUsageLimitsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.usage_limit_list.UsageLimitList"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.describe_usage_limits

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.describe_usage_limits.async_describe_usage_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.describe_usage_limits_message.DescribeUsageLimitsMessage = {}
        if usage_limit_id is not None:
            input_["usage_limit_id"] = usage_limit_id
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if feature_type is not None:
            input_["feature_type"] = feature_type
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if tag_values is not None:
            input_["tag_values"] = tag_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_usage_limits(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        usage_limit_id: Optional["capo_redshift.types.string.String"] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        feature_type: Optional[
            "capo_redshift.types.usage_limit_feature_type.UsageLimitFeatureType"
        ] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
        tag_keys: Optional["capo_redshift.types.tag_key_list.TagKeyList"] = None,
        tag_values: Optional["capo_redshift.types.tag_value_list.TagValueList"] = None,
    ) -> "AsyncIterator[capo_redshift.types.usage_limit.UsageLimit]":
        _token = marker
        while True:
            _response = await self.describe_usage_limits(
                config_overrides=config_overrides,
                usage_limit_id=usage_limit_id,
                cluster_identifier=cluster_identifier,
                feature_type=feature_type,
                max_records=max_records,
                marker=_token,
                tag_keys=tag_keys,
                tag_values=tag_values,
            )
            _page = _resolve_path(_response, ("usage_limits",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def disable_logging(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        log_destination_type: Optional[
            "capo_redshift.types.log_destination_type.LogDestinationType"
        ] = None,
        log_exports: Optional["capo_redshift.types.log_type_list.LogTypeList"] = None,
    ) -> "capo_redshift.types.logging_status.LoggingStatus":
        """<p>Stops logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.</p>

        Args:
            cluster_identifier: <p>The identifier of the cluster on which logging is to be stopped.</p> <p>Example: <code>examplecluster</code> </p>
            log_destination_type: <p>The log destination type. An enum with possible values of <code>s3</code>, <code>cloudwatch</code>, and <code>s3table</code>. When set to <code>s3table</code>, stops system table publishing. When omitted, the operation disables audit logging.</p>
            log_exports: <p>The collection of log types to stop exporting. When <code>LogDestinationType</code> is <code>s3table</code>, the values are the names of the system tables to stop publishing. Omitting this parameter or passing <code>all</code> stops publishing all system tables.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.disable_logging_message.DisableLoggingMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.logging_status.LoggingStatus"]:
            import capo_redshift._operations.redshift_service_version20121201.disable_logging

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.disable_logging.async_disable_logging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.disable_logging_message.DisableLoggingMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if log_destination_type is not None:
            input_["log_destination_type"] = log_destination_type
        if log_exports is not None:
            input_["log_exports"] = log_exports

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_snapshot_copy(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.disable_snapshot_copy_result.DisableSnapshotCopyResult":
        """<p>Disables the automatic copying of snapshots from one region to another region for a specified cluster.</p> <p>If your cluster and its snapshots are encrypted using an encrypted symmetric key from Key Management Service, use <a>DeleteSnapshotCopyGrant</a> to delete the grant that grants Amazon Redshift permission to the key in the destination region. </p>

        Args:
            cluster_identifier: <p>The unique identifier of the source cluster that you want to disable copying of snapshots to a destination region.</p> <p>Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.snapshot_copy_already_disabled_fault.SnapshotCopyAlreadyDisabledFault: <p>The cluster already has cross-region snapshot copy disabled.</p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.disable_snapshot_copy_message.DisableSnapshotCopyMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.disable_snapshot_copy_result.DisableSnapshotCopyResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.disable_snapshot_copy

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.disable_snapshot_copy.async_disable_snapshot_copy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.disable_snapshot_copy_message.DisableSnapshotCopyMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_data_share_consumer(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        data_share_arn: Optional["capo_redshift.types.string.String"] = None,
        disassociate_entire_account: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        consumer_arn: Optional["capo_redshift.types.string.String"] = None,
        consumer_region: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.data_share.DataShare":
        """<p>From a datashare consumer account, remove association for the specified datashare. </p>

        Args:
            data_share_arn: <p>The Amazon Resource Name (ARN) of the datashare to remove association for.</p>
            disassociate_entire_account: <p>A value that specifies whether association for the datashare is removed from the entire account.</p>
            consumer_arn: <p>The Amazon Resource Name (ARN) of the consumer namespace that association for the datashare is removed from.</p>
            consumer_region: <p>From a datashare consumer account, removes association of a datashare from all the existing and future namespaces in the specified Amazon Web Services Region.</p>

        Raises:
            capo_redshift.errors.invalid_data_share_fault.InvalidDataShareFault: <p>There is an error with the datashare.</p>
            capo_redshift.errors.invalid_namespace_fault.InvalidNamespaceFault: <p>The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.disassociate_data_share_consumer_message.DisassociateDataShareConsumerMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.data_share.DataShare"]:
            import capo_redshift._operations.redshift_service_version20121201.disassociate_data_share_consumer

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.disassociate_data_share_consumer.async_disassociate_data_share_consumer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.disassociate_data_share_consumer_message.DisassociateDataShareConsumerMessage = {}
        if data_share_arn is not None:
            input_["data_share_arn"] = data_share_arn
        if disassociate_entire_account is not None:
            input_["disassociate_entire_account"] = disassociate_entire_account
        if consumer_arn is not None:
            input_["consumer_arn"] = consumer_arn
        if consumer_region is not None:
            input_["consumer_region"] = consumer_region

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_logging(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        bucket_name: Optional["capo_redshift.types.string.String"] = None,
        s3_key_prefix: Optional[
            "capo_redshift.types.s3_key_prefix_value.S3KeyPrefixValue"
        ] = None,
        log_destination_type: Optional[
            "capo_redshift.types.log_destination_type.LogDestinationType"
        ] = None,
        log_exports: Optional["capo_redshift.types.log_type_list.LogTypeList"] = None,
        s3_table_kms_key_id: Optional["capo_redshift.types.string.String"] = None,
        s3_table_granularity: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.logging_status.LoggingStatus":
        r"""<p>Starts logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.</p>

        Args:
            cluster_identifier: <p>The identifier of the cluster on which logging is to be started.</p> <p>Example: <code>examplecluster</code> </p>
            bucket_name: <p>The name of an existing S3 bucket where the log files are to be stored.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the same region as the cluster</p> </li> <li> <p>The cluster must have read bucket and put object permissions</p> </li> </ul>
            s3_key_prefix: <p>The prefix applied to the log file names.</p> <p>Valid characters are any letter from any language, any whitespace character, any numeric character, and the following characters: underscore (<code>_</code>), period (<code>.</code>), colon (<code>:</code>), slash (<code>/</code>), equal (<code>=</code>), plus (<code>+</code>), backslash (<code>\</code>), hyphen (<code>-</code>), at symbol (<code>@</code>).</p>
            log_destination_type: <p>The log destination type. An enum with possible values of <code>s3</code>, <code>cloudwatch</code>, and <code>s3table</code>.</p>
            log_exports: <p>The collection of exported log types. When <code>LogDestinationType</code> is <code>s3</code> or <code>cloudwatch</code>, possible values are <code>connectionlog</code>, <code>useractivitylog</code>, and <code>userlog</code>. When <code>LogDestinationType</code> is <code>s3table</code>, the values are the names of the system tables to publish. Omitting this parameter, passing an empty list, or including the value <code>all</code> publishes all current and future system tables.</p>
            s3_table_kms_key_id: <p>The identifier of a customer managed KMS key used to encrypt the S3 tables. This parameter is valid only when <code>LogDestinationType</code> is <code>s3table</code>.</p>
            s3_table_granularity: <p>The scope of system table publishing. Valid values are <code>cluster</code> and <code>account</code>. A value of <code>cluster</code> scopes publishing to the individual cluster. A value of <code>account</code> scopes publishing to the Amazon Web Services account. This parameter is valid only when <code>LogDestinationType</code> is <code>s3table</code>.</p>

        Raises:
            capo_redshift.errors.bucket_not_found_fault.BucketNotFoundFault: <p>Could not find the specified S3 bucket.</p>
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.insufficient_s3_bucket_policy_fault.InsufficientS3BucketPolicyFault: <p>The cluster does not have read bucket or put object permissions on the S3 bucket specified when enabling logging.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_s3_bucket_name_fault.InvalidS3BucketNameFault: <p>The S3 bucket name is invalid. For more information about naming rules, go to <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html">Bucket Restrictions and Limitations</a> in the Amazon Simple Storage Service (S3) Developer Guide.</p>
            capo_redshift.errors.invalid_s3_key_prefix_fault.InvalidS3KeyPrefixFault: <p>The string specified for the logging S3 key prefix does not comply with the documented constraints.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.enable_logging_message.EnableLoggingMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.logging_status.LoggingStatus"]:
            import capo_redshift._operations.redshift_service_version20121201.enable_logging

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.enable_logging.async_enable_logging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.enable_logging_message.EnableLoggingMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if bucket_name is not None:
            input_["bucket_name"] = bucket_name
        if s3_key_prefix is not None:
            input_["s3_key_prefix"] = s3_key_prefix
        if log_destination_type is not None:
            input_["log_destination_type"] = log_destination_type
        if log_exports is not None:
            input_["log_exports"] = log_exports
        if s3_table_kms_key_id is not None:
            input_["s3_table_kms_key_id"] = s3_table_kms_key_id
        if s3_table_granularity is not None:
            input_["s3_table_granularity"] = s3_table_granularity

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_snapshot_copy(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        destination_region: Optional["capo_redshift.types.string.String"] = None,
        retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        snapshot_copy_grant_name: Optional["capo_redshift.types.string.String"] = None,
        manual_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_redshift.types.enable_snapshot_copy_result.EnableSnapshotCopyResult":
        """<p>Enables the automatic copy of snapshots from one region to another region for a specified cluster.</p>

        Args:
            cluster_identifier: <p>The unique identifier of the source cluster to copy snapshots from.</p> <p>Constraints: Must be the valid name of an existing cluster that does not already have cross-region snapshot copy enabled.</p>
            destination_region: <p>The destination Amazon Web Services Region that you want to copy snapshots to.</p> <p>Constraints: Must be the name of a valid Amazon Web Services Region. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html#redshift_region">Regions and Endpoints</a> in the Amazon Web Services General Reference. </p>
            retention_period: <p>The number of days to retain automated snapshots in the destination region after they are copied from the source region.</p> <p>Default: 7.</p> <p>Constraints: Must be at least 1 and no more than 35.</p>
            snapshot_copy_grant_name: <p>The name of the snapshot copy grant to use when snapshots of an Amazon Web Services KMS-encrypted cluster are copied to the destination region.</p>
            manual_snapshot_retention_period: <p>The number of days to retain newly copied snapshots in the destination Amazon Web Services Region after they are copied from the source Amazon Web Services Region. If the value is -1, the manual snapshot is retained indefinitely. </p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.copy_to_region_disabled_fault.CopyToRegionDisabledFault: <p>Cross-region snapshot copy was temporarily disabled. Try your request again.</p>
            capo_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault: <p>The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.</p>
            capo_redshift.errors.incompatible_orderable_options.IncompatibleOrderableOptions: <p>The specified options are incompatible.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault: <p>The retention period specified is either in the past or is not a valid value.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            capo_redshift.errors.limit_exceeded_fault.LimitExceededFault: <p>The encryption key has exceeded its grant limit in Amazon Web Services KMS.</p>
            capo_redshift.errors.snapshot_copy_already_enabled_fault.SnapshotCopyAlreadyEnabledFault: <p>The cluster already has cross-region snapshot copy enabled.</p>
            capo_redshift.errors.snapshot_copy_grant_not_found_fault.SnapshotCopyGrantNotFoundFault: <p>The specified snapshot copy grant can't be found. Make sure that the name is typed correctly and that the grant exists in the destination region.</p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.unknown_snapshot_copy_region_fault.UnknownSnapshotCopyRegionFault: <p>The specified region is incorrect or does not exist.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.enable_snapshot_copy_message.EnableSnapshotCopyMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.enable_snapshot_copy_result.EnableSnapshotCopyResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.enable_snapshot_copy

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.enable_snapshot_copy.async_enable_snapshot_copy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.enable_snapshot_copy_message.EnableSnapshotCopyMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if destination_region is not None:
            input_["destination_region"] = destination_region
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if snapshot_copy_grant_name is not None:
            input_["snapshot_copy_grant_name"] = snapshot_copy_grant_name
        if manual_snapshot_retention_period is not None:
            input_["manual_snapshot_retention_period"] = (
                manual_snapshot_retention_period
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def failover_primary_compute(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.failover_primary_compute_result.FailoverPrimaryComputeResult":
        """<p>Fails over the primary compute unit of the specified Multi-AZ cluster to another Availability Zone.</p>

        Args:
            cluster_identifier: <p>The unique identifier of the cluster for which the primary compute unit will be failed over to another Availability Zone.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.failover_primary_compute_input_message.FailoverPrimaryComputeInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.failover_primary_compute_result.FailoverPrimaryComputeResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.failover_primary_compute

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.failover_primary_compute.async_failover_primary_compute(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.failover_primary_compute_input_message.FailoverPrimaryComputeInputMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cluster_credentials(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        db_user: Optional["capo_redshift.types.string.String"] = None,
        db_name: Optional["capo_redshift.types.string.String"] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        duration_seconds: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        auto_create: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        db_groups: Optional["capo_redshift.types.db_group_list.DbGroupList"] = None,
        custom_domain_name: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.cluster_credentials.ClusterCredentials":
        """<p>Returns a database user name and temporary password with temporary authorization to log on to an Amazon Redshift database. The action returns the database user name prefixed with <code>IAM:</code> if <code>AutoCreate</code> is <code>False</code> or <code>IAMA:</code> if <code>AutoCreate</code> is <code>True</code>. You can optionally specify one or more database user groups that the user will join at log on. By default, the temporary credentials expire in 900 seconds. You can optionally specify a duration between 900 seconds (15 minutes) and 3600 seconds (60 minutes). For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/generating-user-credentials.html">Using IAM Authentication to Generate Database User Credentials</a> in the Amazon Redshift Cluster Management Guide.</p> <p>The Identity and Access Management (IAM) user or role that runs GetClusterCredentials must have an IAM policy attached that allows access to all necessary actions and resources. For more information about permissions, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html#redshift-policy-resources.getclustercredentials-resources">Resource Policies for GetClusterCredentials</a> in the Amazon Redshift Cluster Management Guide.</p> <p>If the <code>DbGroups</code> parameter is specified, the IAM policy must allow the <code>redshift:JoinGroup</code> action with access to the listed <code>dbgroups</code>. </p> <p>In addition, if the <code>AutoCreate</code> parameter is set to <code>True</code>, then the policy must include the <code>redshift:CreateClusterUser</code> permission.</p> <p>If the <code>DbName</code> parameter is specified, the IAM policy must allow access to the resource <code>dbname</code> for the specified database name. </p>

        Args:
            db_user: <p>The name of a database user. If a user name matching <code>DbUser</code> exists in the database, the temporary user credentials have the same permissions as the existing user. If <code>DbUser</code> doesn't exist in the database and <code>Autocreate</code> is <code>True</code>, a new user is created using the value for <code>DbUser</code> with PUBLIC permissions. If a database user matching the value for <code>DbUser</code> doesn't exist and <code>Autocreate</code> is <code>False</code>, then the command succeeds but the connection attempt will fail because the user doesn't exist in the database.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html">CREATE USER</a> in the Amazon Redshift Database Developer Guide. </p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 64 alphanumeric characters or hyphens. The user name can't be <code>PUBLIC</code>.</p> </li> <li> <p>Must contain uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Must not contain a colon ( : ) or slash ( / ). </p> </li> <li> <p>Cannot be a reserved word. A list of reserved words can be found in <a href="http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html">Reserved Words</a> in the Amazon Redshift Database Developer Guide.</p> </li> </ul>
            db_name: <p>The name of a database that <code>DbUser</code> is authorized to log on to. If <code>DbName</code> is not specified, <code>DbUser</code> can log on to any existing database.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 64 alphanumeric characters or hyphens</p> </li> <li> <p>Must contain uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Must not contain a colon ( : ) or slash ( / ). </p> </li> <li> <p>Cannot be a reserved word. A list of reserved words can be found in <a href="http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html">Reserved Words</a> in the Amazon Redshift Database Developer Guide.</p> </li> </ul>
            cluster_identifier: <p>The unique identifier of the cluster that contains the database for which you are requesting credentials. This parameter is case sensitive.</p>
            duration_seconds: <p>The number of seconds until the returned temporary password expires.</p> <p>Constraint: minimum 900, maximum 3600.</p> <p>Default: 900</p>
            auto_create: <p>Create a database user with the name specified for the user named in <code>DbUser</code> if one does not exist.</p>
            db_groups: <p>A list of the names of existing database groups that the user named in <code>DbUser</code> will join for the current session, in addition to any group memberships for an existing user. If not specified, a new user is added only to PUBLIC.</p> <p>Database group name constraints</p> <ul> <li> <p>Must be 1 to 64 alphanumeric characters or hyphens</p> </li> <li> <p>Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Must not contain a colon ( : ) or slash ( / ). </p> </li> <li> <p>Cannot be a reserved word. A list of reserved words can be found in <a href="http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html">Reserved Words</a> in the Amazon Redshift Database Developer Guide.</p> </li> </ul>
            custom_domain_name: <p>The custom domain name for the cluster credentials.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.get_cluster_credentials_message.GetClusterCredentialsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.cluster_credentials.ClusterCredentials"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.get_cluster_credentials

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.get_cluster_credentials.async_get_cluster_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.get_cluster_credentials_message.GetClusterCredentialsMessage = {}
        if db_user is not None:
            input_["db_user"] = db_user
        if db_name is not None:
            input_["db_name"] = db_name
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if auto_create is not None:
            input_["auto_create"] = auto_create
        if db_groups is not None:
            input_["db_groups"] = db_groups
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cluster_credentials_with_iam(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        db_name: Optional["capo_redshift.types.string.String"] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        duration_seconds: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        custom_domain_name: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.cluster_extended_credentials.ClusterExtendedCredentials":
        """<p>Returns a database user name and temporary password with temporary authorization to log in to an Amazon Redshift database. The database user is mapped 1:1 to the source Identity and Access Management (IAM) identity. For more information about IAM identities, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html">IAM Identities (users, user groups, and roles)</a> in the Amazon Web Services Identity and Access Management User Guide.</p> <p>The Identity and Access Management (IAM) identity that runs this operation must have an IAM policy attached that allows access to all necessary actions and resources. For more information about permissions, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html">Using identity-based policies (IAM policies)</a> in the Amazon Redshift Cluster Management Guide. </p>

        Args:
            db_name: <p>The name of the database for which you are requesting credentials. If the database name is specified, the IAM policy must allow access to the resource <code>dbname</code> for the specified database name. If the database name is not specified, access to all databases is allowed.</p>
            cluster_identifier: <p>The unique identifier of the cluster that contains the database for which you are requesting credentials. </p>
            duration_seconds: <p>The number of seconds until the returned temporary password expires.</p> <p>Range: 900-3600. Default: 900.</p>
            custom_domain_name: <p>The custom domain name for the IAM message cluster credentials.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.get_cluster_credentials_with_iam_message.GetClusterCredentialsWithIAMMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.cluster_extended_credentials.ClusterExtendedCredentials"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.get_cluster_credentials_with_iam

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.get_cluster_credentials_with_iam.async_get_cluster_credentials_with_iam(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.get_cluster_credentials_with_iam_message.GetClusterCredentialsWithIAMMessage = {}
        if db_name is not None:
            input_["db_name"] = db_name
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_identity_center_auth_token(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_ids: Optional[
            "capo_redshift.types.cluster_identifier_list.ClusterIdentifierList"
        ] = None,
    ) -> "capo_redshift.types.get_identity_center_auth_token_response.GetIdentityCenterAuthTokenResponse":
        """<p>Generates an encrypted authentication token that propagates the caller's Amazon Web Services IAM Identity Center identity to Amazon Redshift clusters. This API extracts the Amazon Web Services IAM Identity Center identity from enhanced credentials and creates a secure token that Amazon Redshift drivers can use for authentication.</p> <p>The token is encrypted using Key Management Service (KMS) and can only be decrypted by the specified Amazon Redshift clusters. The token contains the caller's Amazon Web Services IAM Identity Center identity information and is valid for a limited time period.</p> <p>This API is exclusively for use with Amazon Web Services IAM Identity Center enhanced credentials. If the caller is not using enhanced credentials with embedded Amazon Web Services IAM Identity Center identity, the API will return an error.</p>

        Args:
            cluster_ids: <p>A list of cluster identifiers that the generated token can be used with. The token will be scoped to only allow authentication to the specified clusters.</p> <p>Constraints:</p> <ul> <li> <p> <code>ClusterIds</code> must contain at least 1 cluster identifier.</p> </li> <li> <p> <code>ClusterIds</code> can hold a maximum of 20 cluster identifiers.</p> </li> <li> <p>Cluster identifiers must be 1 to 63 characters in length.</p> </li> <li> <p>The characters accepted for cluster identifiers are the following:</p> <ul> <li> <p>Alphanumeric characters</p> </li> <li> <p>Hyphens</p> </li> </ul> </li> <li> <p>Cluster identifiers must start with a letter.</p> </li> <li> <p>Cluster identifiers can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.redshift_invalid_parameter_fault.RedshiftInvalidParameterFault: <p>The request contains one or more invalid parameters. This error occurs when required parameters are missing, parameter values are outside acceptable ranges, or parameter formats are incorrect.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.get_identity_center_auth_token_request.GetIdentityCenterAuthTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.get_identity_center_auth_token_response.GetIdentityCenterAuthTokenResponse"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.get_identity_center_auth_token

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.get_identity_center_auth_token.async_get_identity_center_auth_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.get_identity_center_auth_token_request.GetIdentityCenterAuthTokenRequest = {}
        if cluster_ids is not None:
            input_["cluster_ids"] = cluster_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_reserved_node_exchange_configuration_options(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        action_type: Optional[
            "capo_redshift.types.reserved_node_exchange_action_type.ReservedNodeExchangeActionType"
        ] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.get_reserved_node_exchange_configuration_options_output_message.GetReservedNodeExchangeConfigurationOptionsOutputMessage":
        """<p>Gets the configuration options for the reserved-node exchange. These options include information about the source reserved node and target reserved node offering. Details include the node type, the price, the node count, and the offering type.</p>

        Args:
            action_type: <p>The action type of the reserved-node configuration. The action type can be an exchange initiated from either a snapshot or a resize.</p>
            cluster_identifier: <p>The identifier for the cluster that is the source for a reserved-node exchange.</p>
            snapshot_identifier: <p>The identifier for the snapshot that is the source for the reserved-node exchange.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>Marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.</p>
            marker: <p>An optional pagination token provided by a previous <code>GetReservedNodeExchangeConfigurationOptions</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault: <p>The snapshot identifier does not refer to an existing cluster snapshot.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.invalid_reserved_node_state_fault.InvalidReservedNodeStateFault: <p>Indicates that the Reserved Node being exchanged is not in an active state.</p>
            capo_redshift.errors.reserved_node_already_migrated_fault.ReservedNodeAlreadyMigratedFault: <p>Indicates that the reserved node has already been exchanged.</p>
            capo_redshift.errors.reserved_node_not_found_fault.ReservedNodeNotFoundFault: <p>The specified reserved compute node not found.</p>
            capo_redshift.errors.reserved_node_offering_not_found_fault.ReservedNodeOfferingNotFoundFault: <p>Specified offering does not exist.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.get_reserved_node_exchange_configuration_options_input_message.GetReservedNodeExchangeConfigurationOptionsInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.get_reserved_node_exchange_configuration_options_output_message.GetReservedNodeExchangeConfigurationOptionsOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.get_reserved_node_exchange_configuration_options

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.get_reserved_node_exchange_configuration_options.async_get_reserved_node_exchange_configuration_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.get_reserved_node_exchange_configuration_options_input_message.GetReservedNodeExchangeConfigurationOptionsInputMessage = {}
        if action_type is not None:
            input_["action_type"] = action_type
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if snapshot_identifier is not None:
            input_["snapshot_identifier"] = snapshot_identifier
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_reserved_node_exchange_configuration_options(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        action_type: Optional[
            "capo_redshift.types.reserved_node_exchange_action_type.ReservedNodeExchangeActionType"
        ] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.reserved_node_configuration_option.ReservedNodeConfigurationOption]":
        _token = marker
        while True:
            _response = await self.get_reserved_node_exchange_configuration_options(
                config_overrides=config_overrides,
                action_type=action_type,
                cluster_identifier=cluster_identifier,
                snapshot_identifier=snapshot_identifier,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(
                _response, ("reserved_node_configuration_option_list",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def get_reserved_node_exchange_offerings(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        reserved_node_id: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.get_reserved_node_exchange_offerings_output_message.GetReservedNodeExchangeOfferingsOutputMessage":
        """<p>Returns an array of DC2 ReservedNodeOfferings that matches the payment type, term, and usage price of the given DC1 reserved node.</p>

        Args:
            reserved_node_id: <p>A string representing the node identifier for the DC1 Reserved Node to be exchanged.</p>
            max_records: <p>An integer setting the maximum number of ReservedNodeOfferings to retrieve.</p>
            marker: <p>A value that indicates the starting point for the next set of ReservedNodeOfferings.</p>

        Raises:
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.invalid_reserved_node_state_fault.InvalidReservedNodeStateFault: <p>Indicates that the Reserved Node being exchanged is not in an active state.</p>
            capo_redshift.errors.reserved_node_already_migrated_fault.ReservedNodeAlreadyMigratedFault: <p>Indicates that the reserved node has already been exchanged.</p>
            capo_redshift.errors.reserved_node_not_found_fault.ReservedNodeNotFoundFault: <p>The specified reserved compute node not found.</p>
            capo_redshift.errors.reserved_node_offering_not_found_fault.ReservedNodeOfferingNotFoundFault: <p>Specified offering does not exist.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.get_reserved_node_exchange_offerings_input_message.GetReservedNodeExchangeOfferingsInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.get_reserved_node_exchange_offerings_output_message.GetReservedNodeExchangeOfferingsOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.get_reserved_node_exchange_offerings

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.get_reserved_node_exchange_offerings.async_get_reserved_node_exchange_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.get_reserved_node_exchange_offerings_input_message.GetReservedNodeExchangeOfferingsInputMessage = {}
        if reserved_node_id is not None:
            input_["reserved_node_id"] = reserved_node_id
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_reserved_node_exchange_offerings(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        reserved_node_id: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> (
        "AsyncIterator[capo_redshift.types.reserved_node_offering.ReservedNodeOffering]"
    ):
        _token = marker
        while True:
            _response = await self.get_reserved_node_exchange_offerings(
                config_overrides=config_overrides,
                reserved_node_id=reserved_node_id,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("reserved_node_offerings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def get_resource_policy(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        resource_arn: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.get_resource_policy_result.GetResourcePolicyResult":
        """<p>Get the resource policy for a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource of which its resource policy is fetched.</p>

        Raises:
            capo_redshift.errors.invalid_policy_fault.InvalidPolicyFault: <p>The resource policy isn't valid.</p>
            capo_redshift.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.get_resource_policy_message.GetResourcePolicyMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.get_resource_policy_result.GetResourcePolicyResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.get_resource_policy_message.GetResourcePolicyMessage = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        namespace_arn: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.list_recommendations_result.ListRecommendationsResult":
        """<p>List the Amazon Redshift Advisor recommendations for one or multiple Amazon Redshift clusters in an Amazon Web Services account.</p>

        Args:
            cluster_identifier: <p>The unique identifier of the Amazon Redshift cluster for which the list of Advisor recommendations is returned. If the neither the cluster identifier and the cluster namespace ARN parameters are specified, then recommendations for all clusters in the account are returned.</p>
            namespace_arn: <p>The Amazon Redshift cluster namespace Amazon Resource Name (ARN) for which the list of Advisor recommendations is returned. If the neither the cluster identifier and the cluster namespace ARN parameters are specified, then recommendations for all clusters in the account are returned.</p>
            max_records: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.</p>
            marker: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request. </p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.list_recommendations_message.ListRecommendationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.list_recommendations_result.ListRecommendationsResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.list_recommendations

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.list_recommendations.async_list_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.list_recommendations_message.ListRecommendationsMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if namespace_arn is not None:
            input_["namespace_arn"] = namespace_arn
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        namespace_arn: Optional["capo_redshift.types.string.String"] = None,
        max_records: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_redshift.types.string.String"] = None,
    ) -> "AsyncIterator[capo_redshift.types.recommendation.Recommendation]":
        _token = marker
        while True:
            _response = await self.list_recommendations(
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                namespace_arn=namespace_arn,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("recommendations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def modify_aqua_configuration(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        aqua_configuration_status: Optional[
            "capo_redshift.types.aqua_configuration_status.AquaConfigurationStatus"
        ] = None,
    ) -> "capo_redshift.types.modify_aqua_output_message.ModifyAquaOutputMessage":
        """<p>This operation is retired. Calling this operation does not change AQUA configuration. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator). </p>

        Args:
            cluster_identifier: <p>The identifier of the cluster to be modified.</p>
            aqua_configuration_status: <p>This parameter is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_aqua_input_message.ModifyAquaInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_aqua_output_message.ModifyAquaOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_aqua_configuration

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_aqua_configuration.async_modify_aqua_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_aqua_input_message.ModifyAquaInputMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if aqua_configuration_status is not None:
            input_["aqua_configuration_status"] = aqua_configuration_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_authentication_profile(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        authentication_profile_name: Optional[
            "capo_redshift.types.authentication_profile_name_string.AuthenticationProfileNameString"
        ] = None,
        authentication_profile_content: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> "capo_redshift.types.modify_authentication_profile_result.ModifyAuthenticationProfileResult":
        """<p>Modifies an authentication profile.</p>

        Args:
            authentication_profile_name: <p>The name of the authentication profile to replace.</p>
            authentication_profile_content: <p>The new content of the authentication profile in JSON format. The maximum length of the JSON string is determined by a quota for your account.</p>

        Raises:
            capo_redshift.errors.authentication_profile_not_found_fault.AuthenticationProfileNotFoundFault: <p>The authentication profile can't be found.</p>
            capo_redshift.errors.authentication_profile_quota_exceeded_fault.AuthenticationProfileQuotaExceededFault: <p>The size or number of authentication profiles has exceeded the quota. The maximum length of the JSON string and maximum number of authentication profiles is determined by a quota for your account.</p>
            capo_redshift.errors.invalid_authentication_profile_request_fault.InvalidAuthenticationProfileRequestFault: <p>The authentication profile request is not valid. The profile name can't be null or empty. The authentication profile API operation must be available in the Amazon Web Services Region.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_authentication_profile_message.ModifyAuthenticationProfileMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_authentication_profile_result.ModifyAuthenticationProfileResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_authentication_profile

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_authentication_profile.async_modify_authentication_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_authentication_profile_message.ModifyAuthenticationProfileMessage = {}
        if authentication_profile_name is not None:
            input_["authentication_profile_name"] = authentication_profile_name
        if authentication_profile_content is not None:
            input_["authentication_profile_content"] = authentication_profile_content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cluster(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        cluster_type: Optional["capo_redshift.types.string.String"] = None,
        node_type: Optional["capo_redshift.types.string.String"] = None,
        number_of_nodes: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        cluster_security_groups: Optional[
            "capo_redshift.types.cluster_security_group_name_list.ClusterSecurityGroupNameList"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_redshift.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        master_user_password: Optional[
            "capo_redshift.types.sensitive_string.SensitiveString"
        ] = None,
        cluster_parameter_group_name: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        automated_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        manual_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        preferred_maintenance_window: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        cluster_version: Optional["capo_redshift.types.string.String"] = None,
        allow_version_upgrade: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        hsm_client_certificate_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        hsm_configuration_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        new_cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        publicly_accessible: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        elastic_ip: Optional["capo_redshift.types.string.String"] = None,
        enhanced_vpc_routing: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        maintenance_track_name: Optional["capo_redshift.types.string.String"] = None,
        encrypted: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        kms_key_id: Optional["capo_redshift.types.string.String"] = None,
        availability_zone_relocation: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        availability_zone: Optional["capo_redshift.types.string.String"] = None,
        port: Optional["capo_redshift.types.integer_optional.IntegerOptional"] = None,
        manage_master_password: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        master_password_secret_kms_key_id: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        ip_address_type: Optional["capo_redshift.types.string.String"] = None,
        multi_az: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        extra_compute_for_automatic_optimization: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_redshift.types.modify_cluster_result.ModifyClusterResult":
        r"""<p>Modifies the settings for a cluster.</p> <p>You can also change node type and the number of nodes to scale up or down the cluster. When resizing a cluster, you must specify both the number of nodes and the node type even if one of the parameters does not change.</p> <p>You can add another security or parameter group, or change the admin user password. Resetting a cluster password or modifying the security groups associated with a cluster do not need a reboot. However, modifying a parameter group requires a reboot for parameters to take effect. For more information about managing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html">Amazon Redshift Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a subnet group for a provisioned cluster is in an account with VPC BPA turned on, the following capabilities are blocked:</p> <ul> <li> <p>Creating a public cluster</p> </li> <li> <p>Restoring a public cluster</p> </li> <li> <p>Modifying a private cluster to be public</p> </li> <li> <p>Adding a subnet with VPC BPA turned on to the subnet group when there's at least one public cluster within the group</p> </li> </ul> <p>For more information about VPC BPA, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html">Block public access to VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            cluster_identifier: <p>The unique identifier of the cluster to be modified.</p> <p>Example: <code>examplecluster</code> </p>
            cluster_type: <p>The new cluster type.</p> <p>When you submit your cluster resize request, your existing cluster goes into a read-only mode. After Amazon Redshift provisions a new cluster based on your resize requirements, there will be outage for a period while the old cluster is deleted and your connection is switched to the new cluster. You can use <a>DescribeResize</a> to track the progress of the resize request. </p> <p>Valid Values: <code> multi-node | single-node </code> </p>
            node_type: <p>The new node type of the cluster. If you specify a new node type, you must also specify the number of nodes parameter.</p> <p> For more information about resizing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/rs-resize-tutorial.html">Resizing Clusters in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>Valid Values: <code>dc2.large</code> | <code>dc2.8xlarge</code> | <code>rg.large</code> | <code>rg.xlarge</code> | <code>rg.4xlarge</code> | <code>rg.12xlarge</code> | <code>ra3.large</code> | <code>ra3.xlplus</code> | <code>ra3.4xlarge</code> | <code>ra3.16xlarge</code> </p>
            number_of_nodes: <p>The new number of nodes of the cluster. If you specify a new number of nodes, you must also specify the node type parameter.</p> <p> For more information about resizing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/rs-resize-tutorial.html">Resizing Clusters in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>Valid Values: Integer greater than <code>0</code>.</p>
            cluster_security_groups: <p>A list of cluster security groups to be authorized on this cluster. This change is asynchronously applied as soon as possible.</p> <p>Security groups currently associated with the cluster, and not in the list of groups to apply, will be revoked from the cluster.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul>
            vpc_security_group_ids: <p>A list of virtual private cloud (VPC) security groups to be associated with the cluster. This change is asynchronously applied as soon as possible.</p>
            master_user_password: <p>The new password for the cluster admin user. This change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the <code>MasterUserPassword</code> element exists in the <code>PendingModifiedValues</code> element of the operation response. </p> <p>You can't use <code>MasterUserPassword</code> if <code>ManageMasterPassword</code> is <code>true</code>.</p> <note> <p>Operations never return the password, so this operation provides a way to regain access to the admin user account for a cluster if the password is lost.</p> </note> <p>Default: Uses existing setting.</p> <p>Constraints:</p> <ul> <li> <p>Must be between 8 and 64 characters in length.</p> </li> <li> <p>Must contain at least one uppercase letter.</p> </li> <li> <p>Must contain at least one lowercase letter.</p> </li> <li> <p>Must contain one number.</p> </li> <li> <p>Can be any printable ASCII character (ASCII code 33-126) except <code>'</code> (single quote), <code>"</code> (double quote), <code>\</code>, <code>/</code>, or <code>@</code>.</p> </li> </ul>
            cluster_parameter_group_name: <p>The name of the cluster parameter group to apply to this cluster. This change is applied only after the cluster is rebooted. To reboot a cluster use <a>RebootCluster</a>. </p> <p>Default: Uses existing setting.</p> <p>Constraints: The cluster parameter group must be in the same parameter group family that matches the cluster version.</p>
            automated_snapshot_retention_period: <p>The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with <a>CreateClusterSnapshot</a>. </p> <p>If you decrease the automated snapshot retention period from its current value, existing automated snapshots that fall outside of the new retention period will be immediately deleted.</p> <p>You can't disable automated snapshots for RG or RA3 node types. Set the automated retention period from 1-35 days.</p> <p>Default: Uses existing setting.</p> <p>Constraints: Must be a value from 0 to 35.</p>
            manual_snapshot_retention_period: <p>The default for number of days that a newly created manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. This value doesn't retroactively change the retention periods of existing manual snapshots.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p> <p>The default value is -1.</p>
            preferred_maintenance_window: <p>The weekly time range (in UTC) during which system maintenance can occur, if necessary. If system maintenance is necessary during the window, it may result in an outage.</p> <p>This maintenance window change is made immediately. If the new maintenance window indicates the current time, there must be at least 120 minutes between the current time and end of the window in order to ensure that pending changes are applied.</p> <p>Default: Uses existing setting.</p> <p>Format: ddd:hh24:mi-ddd:hh24:mi, for example <code>wed:07:30-wed:08:00</code>.</p> <p>Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun</p> <p>Constraints: Must be at least 30 minutes.</p>
            cluster_version: <p>The new version number of the Amazon Redshift engine to upgrade to.</p> <p>For major version upgrades, if a non-default cluster parameter group is currently in use, a new cluster parameter group in the cluster parameter group family for the new version must be specified. The new cluster parameter group can be the default for that cluster parameter group family. For more information about parameters and parameter groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Amazon Redshift Parameter Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>Example: <code>1.0</code> </p>
            allow_version_upgrade: <p>If <code>true</code>, major version upgrades will be applied automatically to the cluster during the maintenance window. </p> <p>Default: <code>false</code> </p>
            hsm_client_certificate_identifier: <p>Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.</p>
            hsm_configuration_identifier: <p>Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.</p>
            new_cluster_identifier: <p>The new identifier for the cluster.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>Alphabetic characters must be lowercase.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique for all clusters within an Amazon Web Services account.</p> </li> </ul> <p>Example: <code>examplecluster</code> </p>
            publicly_accessible: <p>If <code>true</code>, the cluster can be accessed from a public network. Only clusters in VPCs can be set to be publicly available.</p> <p>Default: false</p>
            elastic_ip: <p>The Elastic IP (EIP) address for the cluster.</p> <p>Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms">Supported Platforms to Launch Your Cluster</a> in the Amazon Redshift Cluster Management Guide.</p>
            enhanced_vpc_routing: <p>An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html">Enhanced VPC Routing</a> in the Amazon Redshift Cluster Management Guide.</p> <p>If this option is <code>true</code>, enhanced VPC routing is enabled. </p> <p>Default: false</p>
            maintenance_track_name: <p>The name for the maintenance track that you want to assign for the cluster. This name change is asynchronous. The new track name stays in the <code>PendingModifiedValues</code> for the cluster until the next maintenance window. When the maintenance track changes, the cluster is switched to the latest cluster release available for the maintenance track. At this point, the maintenance track name is applied.</p>
            encrypted: <p>Indicates whether the cluster is encrypted. If the value is encrypted (true) and you provide a value for the <code>KmsKeyId</code> parameter, we encrypt the cluster with the provided <code>KmsKeyId</code>. If you don't provide a <code>KmsKeyId</code>, we encrypt with the default key. </p> <p>If the value is not encrypted (false), then the cluster is decrypted. </p>
            kms_key_id: <p>The Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.</p>
            availability_zone_relocation: <p>The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster modification is complete.</p>
            availability_zone: <p>The option to initiate relocation for an Amazon Redshift cluster to the target Availability Zone.</p>
            port: <p>The option to change the port of an Amazon Redshift cluster.</p> <p>Valid Values: </p> <ul> <li> <p>For clusters with RG or RA3 nodes - Select a port within the ranges <code>5431-5455</code> or <code>8191-8215</code>. (If you have an existing cluster with RG or RA3 nodes, it isn't required that you change the port to these ranges.)</p> </li> <li> <p>For clusters with dc2 nodes - Select a port within the range <code>1150-65535</code>.</p> </li> </ul>
            manage_master_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage this cluster's admin credentials. You can't use <code>MasterUserPassword</code> if <code>ManageMasterPassword</code> is true. If <code>ManageMasterPassword</code> is false or not set, Amazon Redshift uses <code>MasterUserPassword</code> for the admin user account's password. </p>
            master_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret. You can only use this parameter if <code>ManageMasterPassword</code> is true.</p>
            ip_address_type: <p>The IP address types that the cluster supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>
            multi_az: <p>If true and the cluster is currently only deployed in a single Availability Zone, the cluster will be modified to be deployed in two Availability Zones.</p>
            extra_compute_for_automatic_optimization: <p>If <code>true</code>, allocates additional compute resources for running automatic optimization operations.</p> <p>Default: false</p>

        Raises:
            capo_redshift.errors.cluster_already_exists_fault.ClusterAlreadyExistsFault: <p>The account already has a cluster with the given identifier.</p>
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault: <p>The parameter group name does not refer to an existing parameter group.</p>
            capo_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault: <p>The cluster security group name does not refer to an existing cluster security group.</p>
            capo_redshift.errors.custom_cname_association_fault.CustomCnameAssociationFault: <p>An error occurred when an attempt was made to change the custom domain association.</p>
            capo_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault: <p>The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.</p>
            capo_redshift.errors.hsm_client_certificate_not_found_fault.HsmClientCertificateNotFoundFault: <p>There is no Amazon Redshift HSM client certificate with the specified identifier.</p>
            capo_redshift.errors.hsm_configuration_not_found_fault.HsmConfigurationNotFoundFault: <p>There is no Amazon Redshift HSM configuration with the specified identifier.</p>
            capo_redshift.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault: <p>The number of nodes specified exceeds the allotted capacity of the cluster.</p>
            capo_redshift.errors.invalid_cluster_security_group_state_fault.InvalidClusterSecurityGroupStateFault: <p>The state of the cluster security group is not <code>available</code>. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_cluster_track_fault.InvalidClusterTrackFault: <p>The provided cluster track name is not valid.</p>
            capo_redshift.errors.invalid_elastic_ip_fault.InvalidElasticIpFault: <p>The Elastic IP (EIP) is invalid or cannot be found.</p>
            capo_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault: <p>The retention period specified is either in the past or is not a valid value.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            capo_redshift.errors.ipv6_cidr_block_not_found_fault.Ipv6CidrBlockNotFoundFault: <p>There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack mode, associate an IPv6 CIDR block with each subnet in your VPC.</p>
            capo_redshift.errors.limit_exceeded_fault.LimitExceededFault: <p>The encryption key has exceeded its grant limit in Amazon Web Services KMS.</p>
            capo_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault.NumberOfNodesPerClusterLimitExceededFault: <p>The operation would exceed the number of nodes allowed for a cluster.</p>
            capo_redshift.errors.number_of_nodes_quota_exceeded_fault.NumberOfNodesQuotaExceededFault: <p>The operation would exceed the number of nodes allotted to the account. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.table_limit_exceeded_fault.TableLimitExceededFault: <p>The number of tables in the cluster exceeds the limit for the requested new cluster node type. </p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.unsupported_option_fault.UnsupportedOptionFault: <p>A request option was specified that is not supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_cluster_message.ModifyClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_cluster_result.ModifyClusterResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_cluster

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_cluster.async_modify_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_cluster_message.ModifyClusterMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if cluster_type is not None:
            input_["cluster_type"] = cluster_type
        if node_type is not None:
            input_["node_type"] = node_type
        if number_of_nodes is not None:
            input_["number_of_nodes"] = number_of_nodes
        if cluster_security_groups is not None:
            input_["cluster_security_groups"] = cluster_security_groups
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if master_user_password is not None:
            input_["master_user_password"] = master_user_password
        if cluster_parameter_group_name is not None:
            input_["cluster_parameter_group_name"] = cluster_parameter_group_name
        if automated_snapshot_retention_period is not None:
            input_["automated_snapshot_retention_period"] = (
                automated_snapshot_retention_period
            )
        if manual_snapshot_retention_period is not None:
            input_["manual_snapshot_retention_period"] = (
                manual_snapshot_retention_period
            )
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if cluster_version is not None:
            input_["cluster_version"] = cluster_version
        if allow_version_upgrade is not None:
            input_["allow_version_upgrade"] = allow_version_upgrade
        if hsm_client_certificate_identifier is not None:
            input_["hsm_client_certificate_identifier"] = (
                hsm_client_certificate_identifier
            )
        if hsm_configuration_identifier is not None:
            input_["hsm_configuration_identifier"] = hsm_configuration_identifier
        if new_cluster_identifier is not None:
            input_["new_cluster_identifier"] = new_cluster_identifier
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if elastic_ip is not None:
            input_["elastic_ip"] = elastic_ip
        if enhanced_vpc_routing is not None:
            input_["enhanced_vpc_routing"] = enhanced_vpc_routing
        if maintenance_track_name is not None:
            input_["maintenance_track_name"] = maintenance_track_name
        if encrypted is not None:
            input_["encrypted"] = encrypted
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if availability_zone_relocation is not None:
            input_["availability_zone_relocation"] = availability_zone_relocation
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if port is not None:
            input_["port"] = port
        if manage_master_password is not None:
            input_["manage_master_password"] = manage_master_password
        if master_password_secret_kms_key_id is not None:
            input_["master_password_secret_kms_key_id"] = (
                master_password_secret_kms_key_id
            )
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if multi_az is not None:
            input_["multi_az"] = multi_az
        if extra_compute_for_automatic_optimization is not None:
            input_["extra_compute_for_automatic_optimization"] = (
                extra_compute_for_automatic_optimization
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cluster_db_revision(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        revision_target: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.modify_cluster_db_revision_result.ModifyClusterDbRevisionResult":
        """<p>Modifies the database revision of a cluster. The database revision is a unique revision of the database running in a cluster.</p>

        Args:
            cluster_identifier: <p>The unique identifier of a cluster whose database revision you want to modify. </p> <p>Example: <code>examplecluster</code> </p>
            revision_target: <p>The identifier of the database revision. You can retrieve this value from the response to the <a>DescribeClusterDbRevisions</a> request.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.cluster_on_latest_revision_fault.ClusterOnLatestRevisionFault: <p>Cluster is already on the latest database revision.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_cluster_db_revision_message.ModifyClusterDbRevisionMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_cluster_db_revision_result.ModifyClusterDbRevisionResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_cluster_db_revision

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_cluster_db_revision.async_modify_cluster_db_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_cluster_db_revision_message.ModifyClusterDbRevisionMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if revision_target is not None:
            input_["revision_target"] = revision_target

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cluster_iam_roles(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        add_iam_roles: Optional[
            "capo_redshift.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        remove_iam_roles: Optional[
            "capo_redshift.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        default_iam_role_arn: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.modify_cluster_iam_roles_result.ModifyClusterIamRolesResult":
        """<p>Modifies the list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services.</p> <p>The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Quotas and limits</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            cluster_identifier: <p>The unique identifier of the cluster for which you want to associate or disassociate IAM roles.</p>
            add_iam_roles: <p>Zero or more IAM roles to associate with the cluster. The roles must be in their Amazon Resource Name (ARN) format. </p>
            remove_iam_roles: <p>Zero or more IAM roles in ARN format to disassociate from the cluster. </p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was last modified.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_cluster_iam_roles_message.ModifyClusterIamRolesMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_cluster_iam_roles_result.ModifyClusterIamRolesResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_cluster_iam_roles

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_cluster_iam_roles.async_modify_cluster_iam_roles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_cluster_iam_roles_message.ModifyClusterIamRolesMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if add_iam_roles is not None:
            input_["add_iam_roles"] = add_iam_roles
        if remove_iam_roles is not None:
            input_["remove_iam_roles"] = remove_iam_roles
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cluster_maintenance(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        defer_maintenance: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        defer_maintenance_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        defer_maintenance_start_time: Optional[
            "capo_redshift.types.t_stamp.TStamp"
        ] = None,
        defer_maintenance_end_time: Optional[
            "capo_redshift.types.t_stamp.TStamp"
        ] = None,
        defer_maintenance_duration: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_redshift.types.modify_cluster_maintenance_result.ModifyClusterMaintenanceResult":
        """<p>Modifies the maintenance settings of a cluster.</p>

        Args:
            cluster_identifier: <p>A unique identifier for the cluster.</p>
            defer_maintenance: <p>A boolean indicating whether to enable the deferred maintenance window. </p>
            defer_maintenance_identifier: <p>A unique identifier for the deferred maintenance window.</p>
            defer_maintenance_start_time: <p>A timestamp indicating the start time for the deferred maintenance window.</p>
            defer_maintenance_end_time: <p>A timestamp indicating end time for the deferred maintenance window. If you specify an end time, you can't specify a duration.</p>
            defer_maintenance_duration: <p>An integer indicating the duration of the maintenance window in days. If you specify a duration, you can't specify an end time. The duration must be 60 days or less.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_cluster_maintenance_message.ModifyClusterMaintenanceMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_cluster_maintenance_result.ModifyClusterMaintenanceResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_cluster_maintenance

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_cluster_maintenance.async_modify_cluster_maintenance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_cluster_maintenance_message.ModifyClusterMaintenanceMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if defer_maintenance is not None:
            input_["defer_maintenance"] = defer_maintenance
        if defer_maintenance_identifier is not None:
            input_["defer_maintenance_identifier"] = defer_maintenance_identifier
        if defer_maintenance_start_time is not None:
            input_["defer_maintenance_start_time"] = defer_maintenance_start_time
        if defer_maintenance_end_time is not None:
            input_["defer_maintenance_end_time"] = defer_maintenance_end_time
        if defer_maintenance_duration is not None:
            input_["defer_maintenance_duration"] = defer_maintenance_duration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        parameter_group_name: Optional["capo_redshift.types.string.String"] = None,
        parameters: Optional[
            "capo_redshift.types.parameters_list.ParametersList"
        ] = None,
    ) -> "capo_redshift.types.cluster_parameter_group_name_message.ClusterParameterGroupNameMessage":
        """<p>Modifies the parameters of a parameter group. For the parameters parameter, it can't contain ASCII characters.</p> <p> For more information about parameters and parameter groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Amazon Redshift Parameter Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            parameter_group_name: <p>The name of the parameter group to be modified.</p>
            parameters: <p>An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.</p> <p>For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional.</p> <p>For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.</p>

        Raises:
            capo_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault: <p>The parameter group name does not refer to an existing parameter group.</p>
            capo_redshift.errors.invalid_cluster_parameter_group_state_fault.InvalidClusterParameterGroupStateFault: <p>The cluster parameter group action can not be completed because another task is in progress that involves the parameter group. Wait a few moments and try the operation again.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_cluster_parameter_group_message.ModifyClusterParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.cluster_parameter_group_name_message.ClusterParameterGroupNameMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_cluster_parameter_group

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_cluster_parameter_group.async_modify_cluster_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_cluster_parameter_group_message.ModifyClusterParameterGroupMessage = {}
        if parameter_group_name is not None:
            input_["parameter_group_name"] = parameter_group_name
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        manual_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        force: Optional["capo_redshift.types.boolean.Boolean"] = None,
    ) -> (
        "capo_redshift.types.modify_cluster_snapshot_result.ModifyClusterSnapshotResult"
    ):
        """<p>Modifies the settings for a snapshot.</p> <p>This exanmple modifies the manual retention period setting for a cluster snapshot.</p>

        Args:
            snapshot_identifier: <p>The identifier of the snapshot whose setting you want to modify.</p>
            manual_snapshot_retention_period: <p>The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.</p> <p>If the manual snapshot falls outside of the new retention period, you can specify the force option to immediately delete the snapshot.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            force: <p>A Boolean option to override an exception if the retention period has already passed.</p>

        Raises:
            capo_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault: <p>The snapshot identifier does not refer to an existing cluster snapshot.</p>
            capo_redshift.errors.invalid_cluster_snapshot_state_fault.InvalidClusterSnapshotStateFault: <p>The specified cluster snapshot is not in the <code>available</code> state, or other accounts are authorized to access the snapshot. </p>
            capo_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault: <p>The retention period specified is either in the past or is not a valid value.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_cluster_snapshot_message.ModifyClusterSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_cluster_snapshot_result.ModifyClusterSnapshotResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_cluster_snapshot.async_modify_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_cluster_snapshot_message.ModifyClusterSnapshotMessage = {}
        if snapshot_identifier is not None:
            input_["snapshot_identifier"] = snapshot_identifier
        if manual_snapshot_retention_period is not None:
            input_["manual_snapshot_retention_period"] = (
                manual_snapshot_retention_period
            )
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cluster_snapshot_schedule(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        schedule_identifier: Optional["capo_redshift.types.string.String"] = None,
        disassociate_schedule: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> None:
        """<p>Modifies a snapshot schedule for a cluster.</p>

        Args:
            cluster_identifier: <p>A unique identifier for the cluster whose snapshot schedule you want to modify. </p>
            schedule_identifier: <p>A unique alphanumeric identifier for the schedule that you want to associate with the cluster.</p>
            disassociate_schedule: <p>A boolean to indicate whether to remove the assoiciation between the cluster and the schedule.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_snapshot_schedule_state_fault.InvalidClusterSnapshotScheduleStateFault: <p>The cluster snapshot schedule state is not valid.</p>
            capo_redshift.errors.snapshot_schedule_not_found_fault.SnapshotScheduleNotFoundFault: <p>We could not find the specified snapshot schedule. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_cluster_snapshot_schedule_message.ModifyClusterSnapshotScheduleMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_redshift._operations.redshift_service_version20121201.modify_cluster_snapshot_schedule

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_cluster_snapshot_schedule.async_modify_cluster_snapshot_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_cluster_snapshot_schedule_message.ModifyClusterSnapshotScheduleMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if disassociate_schedule is not None:
            input_["disassociate_schedule"] = disassociate_schedule

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cluster_subnet_group(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_subnet_group_name: Optional["capo_redshift.types.string.String"] = None,
        description: Optional["capo_redshift.types.string.String"] = None,
        subnet_ids: Optional[
            "capo_redshift.types.subnet_identifier_list.SubnetIdentifierList"
        ] = None,
    ) -> "capo_redshift.types.modify_cluster_subnet_group_result.ModifyClusterSubnetGroupResult":
        """<p>Modifies a cluster subnet group to include the specified list of VPC subnets. The operation replaces the existing list of subnets with the new list of subnets.</p> <p>VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a subnet group for a provisioned cluster is in an account with VPC BPA turned on, the following capabilities are blocked:</p> <ul> <li> <p>Creating a public cluster</p> </li> <li> <p>Restoring a public cluster</p> </li> <li> <p>Modifying a private cluster to be public</p> </li> <li> <p>Adding a subnet with VPC BPA turned on to the subnet group when there's at least one public cluster within the group</p> </li> </ul> <p>For more information about VPC BPA, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html">Block public access to VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            cluster_subnet_group_name: <p>The name of the subnet group to be modified.</p>
            description: <p>A text description of the subnet group to be modified.</p>
            subnet_ids: <p>An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.</p>

        Raises:
            capo_redshift.errors.cluster_subnet_group_not_found_fault.ClusterSubnetGroupNotFoundFault: <p>The cluster subnet group name does not refer to an existing cluster subnet group.</p>
            capo_redshift.errors.cluster_subnet_quota_exceeded_fault.ClusterSubnetQuotaExceededFault: <p>The request would result in user exceeding the allowed number of subnets in a cluster subnet groups. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault: <p>The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.</p>
            capo_redshift.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is not valid, or not all of the subnets are in the same VPC.</p>
            capo_redshift.errors.subnet_already_in_use.SubnetAlreadyInUse: <p>A specified subnet is already in use by another cluster.</p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_cluster_subnet_group_message.ModifyClusterSubnetGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_cluster_subnet_group_result.ModifyClusterSubnetGroupResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_cluster_subnet_group

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_cluster_subnet_group.async_modify_cluster_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_cluster_subnet_group_message.ModifyClusterSubnetGroupMessage = {}
        if cluster_subnet_group_name is not None:
            input_["cluster_subnet_group_name"] = cluster_subnet_group_name
        if description is not None:
            input_["description"] = description
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_custom_domain_association(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        custom_domain_name: Optional[
            "capo_redshift.types.custom_domain_name_string.CustomDomainNameString"
        ] = None,
        custom_domain_certificate_arn: Optional[
            "capo_redshift.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
        ] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.modify_custom_domain_association_result.ModifyCustomDomainAssociationResult":
        """<p>Contains information for changing a custom domain association.</p>

        Args:
            custom_domain_name: <p>The custom domain name for a changed custom domain association.</p>
            custom_domain_certificate_arn: <p>The certificate Amazon Resource Name (ARN) for the changed custom domain association.</p>
            cluster_identifier: <p>The identifier of the cluster to change a custom domain association for.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.custom_cname_association_fault.CustomCnameAssociationFault: <p>An error occurred when an attempt was made to change the custom domain association.</p>
            capo_redshift.errors.custom_domain_association_not_found_fault.CustomDomainAssociationNotFoundFault: <p>An error occurred. The custom domain name couldn't be found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_custom_domain_association_message.ModifyCustomDomainAssociationMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_custom_domain_association_result.ModifyCustomDomainAssociationResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_custom_domain_association

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_custom_domain_association.async_modify_custom_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_custom_domain_association_message.ModifyCustomDomainAssociationMessage = {}
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if custom_domain_certificate_arn is not None:
            input_["custom_domain_certificate_arn"] = custom_domain_certificate_arn
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_endpoint_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        endpoint_name: Optional["capo_redshift.types.string.String"] = None,
        vpc_security_group_ids: Optional[
            "capo_redshift.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
    ) -> "capo_redshift.types.endpoint_access.EndpointAccess":
        """<p>Modifies a Redshift-managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The endpoint to be modified.</p>
            vpc_security_group_ids: <p>The complete list of VPC security groups associated with the endpoint after the endpoint is modified.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.endpoint_not_found_fault.EndpointNotFoundFault: <p>The endpoint name doesn't refer to an existing endpoint.</p>
            capo_redshift.errors.invalid_cluster_security_group_state_fault.InvalidClusterSecurityGroupStateFault: <p>The state of the cluster security group is not <code>available</code>. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_endpoint_state_fault.InvalidEndpointStateFault: <p>The status of the endpoint is not valid.</p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_endpoint_access_message.ModifyEndpointAccessMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.endpoint_access.EndpointAccess"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_endpoint_access.async_modify_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_endpoint_access_message.ModifyEndpointAccessMessage = {}
        if endpoint_name is not None:
            input_["endpoint_name"] = endpoint_name
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_event_subscription(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        subscription_name: Optional["capo_redshift.types.string.String"] = None,
        sns_topic_arn: Optional["capo_redshift.types.string.String"] = None,
        source_type: Optional["capo_redshift.types.string.String"] = None,
        source_ids: Optional[
            "capo_redshift.types.source_ids_list.SourceIdsList"
        ] = None,
        event_categories: Optional[
            "capo_redshift.types.event_categories_list.EventCategoriesList"
        ] = None,
        severity: Optional["capo_redshift.types.string.String"] = None,
        enabled: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_redshift.types.modify_event_subscription_result.ModifyEventSubscriptionResult":
        """<p>Modifies an existing Amazon Redshift event notification subscription.</p>

        Args:
            subscription_name: <p>The name of the modified Amazon Redshift event notification subscription.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) of the SNS topic to be used by the event notification subscription.</p>
            source_type: <p>The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your Amazon Web Services account. You must specify a source type in order to specify source IDs.</p> <p>Valid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.</p>
            source_ids: <p>A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.</p> <p>Example: my-cluster-1, my-cluster-2</p> <p>Example: my-snapshot-20131010</p>
            event_categories: <p>Specifies the Amazon Redshift event categories to be published by the event notification subscription.</p> <p>Values: configuration, management, monitoring, security, pending</p>
            severity: <p>Specifies the Amazon Redshift event severity to be published by the event notification subscription.</p> <p>Values: ERROR, INFO</p>
            enabled: <p>A Boolean value indicating if the subscription is enabled. <code>true</code> indicates the subscription is enabled </p>

        Raises:
            capo_redshift.errors.invalid_subscription_state_fault.InvalidSubscriptionStateFault: <p>The subscription request is invalid because it is a duplicate request. This subscription request is already in progress.</p>
            capo_redshift.errors.sns_invalid_topic_fault.SNSInvalidTopicFault: <p>Amazon SNS has responded that there is a problem with the specified Amazon SNS topic.</p>
            capo_redshift.errors.sns_no_authorization_fault.SNSNoAuthorizationFault: <p>You do not have permission to publish to the specified Amazon SNS topic.</p>
            capo_redshift.errors.sns_topic_arn_not_found_fault.SNSTopicArnNotFoundFault: <p>An Amazon SNS topic with the specified Amazon Resource Name (ARN) does not exist.</p>
            capo_redshift.errors.source_not_found_fault.SourceNotFoundFault: <p>The specified Amazon Redshift event source could not be found.</p>
            capo_redshift.errors.subscription_category_not_found_fault.SubscriptionCategoryNotFoundFault: <p>The value specified for the event category was not one of the allowed values, or it specified a category that does not apply to the specified source type. The allowed values are Configuration, Management, Monitoring, and Security.</p>
            capo_redshift.errors.subscription_event_id_not_found_fault.SubscriptionEventIdNotFoundFault: <p>An Amazon Redshift event with the specified event ID does not exist.</p>
            capo_redshift.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>An Amazon Redshift event notification subscription with the specified name does not exist.</p>
            capo_redshift.errors.subscription_severity_not_found_fault.SubscriptionSeverityNotFoundFault: <p>The value specified for the event severity was not one of the allowed values, or it specified a severity that does not apply to the specified source type. The allowed values are ERROR and INFO.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_event_subscription_message.ModifyEventSubscriptionMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_event_subscription_result.ModifyEventSubscriptionResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_event_subscription

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_event_subscription.async_modify_event_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_event_subscription_message.ModifyEventSubscriptionMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if source_type is not None:
            input_["source_type"] = source_type
        if source_ids is not None:
            input_["source_ids"] = source_ids
        if event_categories is not None:
            input_["event_categories"] = event_categories
        if severity is not None:
            input_["severity"] = severity
        if enabled is not None:
            input_["enabled"] = enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_integration(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        integration_arn: Optional[
            "capo_redshift.types.integration_arn.IntegrationArn"
        ] = None,
        description: Optional[
            "capo_redshift.types.integration_description.IntegrationDescription"
        ] = None,
        integration_name: Optional[
            "capo_redshift.types.integration_name.IntegrationName"
        ] = None,
    ) -> "capo_redshift.types.integration.Integration":
        """<p>Modifies a zero-ETL integration or S3 event integration with Amazon Redshift.</p>

        Args:
            integration_arn: <p>The unique identifier of the integration to modify.</p>
            description: <p>A new description for the integration.</p>
            integration_name: <p>A new name for the integration.</p>

        Raises:
            capo_redshift.errors.integration_already_exists_fault.IntegrationAlreadyExistsFault: <p>The integration you are trying to create already exists.</p>
            capo_redshift.errors.integration_conflict_operation_fault.IntegrationConflictOperationFault: <p>A conflicting conditional operation is currently in progress against this resource. This typically occurs when there are multiple requests being made to the same resource at the same time, and these requests conflict with each other.</p>
            capo_redshift.errors.integration_conflict_state_fault.IntegrationConflictStateFault: <p>The integration is in an invalid state and can't perform the requested operation.</p>
            capo_redshift.errors.integration_not_found_fault.IntegrationNotFoundFault: <p>The integration can't be found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_integration_message.ModifyIntegrationMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.integration.Integration"]:
            import capo_redshift._operations.redshift_service_version20121201.modify_integration

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_integration.async_modify_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_integration_message.ModifyIntegrationMessage = {}
        if integration_arn is not None:
            input_["integration_arn"] = integration_arn
        if description is not None:
            input_["description"] = description
        if integration_name is not None:
            input_["integration_name"] = integration_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_lakehouse_configuration(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        lakehouse_registration: Optional[
            "capo_redshift.types.lakehouse_registration.LakehouseRegistration"
        ] = None,
        catalog_name: Optional[
            "capo_redshift.types.catalog_name_string.CatalogNameString"
        ] = None,
        lakehouse_idc_registration: Optional[
            "capo_redshift.types.lakehouse_idc_registration.LakehouseIdcRegistration"
        ] = None,
        lakehouse_idc_application_arn: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        dry_run: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_redshift.types.lakehouse_configuration.LakehouseConfiguration":
        """<p>Modifies the lakehouse configuration for a cluster. This operation allows you to manage Amazon Redshift federated permissions and Amazon Web Services IAM Identity Center trusted identity propagation.</p>

        Args:
            cluster_identifier: <p>The unique identifier of the cluster whose lakehouse configuration you want to modify.</p>
            lakehouse_registration: <p>Specifies whether to register or deregister the cluster with Amazon Redshift federated permissions. Valid values are <code>Register</code> or <code>Deregister</code>.</p>
            catalog_name: <p>The name of the Glue data catalog that will be associated with the cluster enabled with Amazon Redshift federated permissions.</p> <p>Constraints:</p> <ul> <li> <p>Must contain at least one lowercase letter.</p> </li> <li> <p>Can only contain lowercase letters (a-z), numbers (0-9), underscores (_), and hyphens (-).</p> </li> </ul> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p> <p>Example: <code>my-catalog_01</code> </p>
            lakehouse_idc_registration: <p>Modifies the Amazon Web Services IAM Identity Center trusted identity propagation on a cluster enabled with Amazon Redshift federated permissions. Valid values are <code>Associate</code> or <code>Disassociate</code>.</p>
            lakehouse_idc_application_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation on a cluster enabled with Amazon Redshift federated permissions.</p>
            dry_run: <p>A boolean value that, if <code>true</code>, validates the request without actually modifying the lakehouse configuration. Use this to check for errors before making changes.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault: <p>A dependent service denied access for the integration.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.redshift_idc_application_not_exists_fault.RedshiftIdcApplicationNotExistsFault: <p>The application you attempted to find doesn't exist.</p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_lakehouse_configuration_message.ModifyLakehouseConfigurationMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.lakehouse_configuration.LakehouseConfiguration"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_lakehouse_configuration

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_lakehouse_configuration.async_modify_lakehouse_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_lakehouse_configuration_message.ModifyLakehouseConfigurationMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if lakehouse_registration is not None:
            input_["lakehouse_registration"] = lakehouse_registration
        if catalog_name is not None:
            input_["catalog_name"] = catalog_name
        if lakehouse_idc_registration is not None:
            input_["lakehouse_idc_registration"] = lakehouse_idc_registration
        if lakehouse_idc_application_arn is not None:
            input_["lakehouse_idc_application_arn"] = lakehouse_idc_application_arn
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_qev2_idc_application(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        qev2_idc_application_arn: Optional["capo_redshift.types.string.String"] = None,
        idc_display_name: Optional[
            "capo_redshift.types.idc_display_name_string.IdcDisplayNameString"
        ] = None,
    ) -> "capo_redshift.types.modify_qev2_idc_application_result.ModifyQev2IdcApplicationResult":
        """<p>Modifies an Amazon Redshift Query Editor (QEV2) IAM Identity Center application.</p>

        Args:
            qev2_idc_application_arn: <p>The Amazon Resource Name (ARN) for the Amazon Redshift Query Editor (QEV2) application that integrates with IAM Identity Center.</p>
            idc_display_name: <p>The display name for the Amazon Redshift Query Editor (QEV2) IAM Identity Center application. It appears in the console.</p>

        Raises:
            capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault: <p>A dependent service denied access for the integration.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.qev2_idc_application_not_exists_fault.Qev2IdcApplicationNotExistsFault: <p>The specified Amazon Redshift Query Editor (QEV2) IAM Identity Center application doesn't exist. Verify that the application ARN is correct and that the application exists in this Region.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_qev2_idc_application_message.ModifyQev2IdcApplicationMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_qev2_idc_application_result.ModifyQev2IdcApplicationResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_qev2_idc_application

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_qev2_idc_application.async_modify_qev2_idc_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_qev2_idc_application_message.ModifyQev2IdcApplicationMessage = {}
        if qev2_idc_application_arn is not None:
            input_["qev2_idc_application_arn"] = qev2_idc_application_arn
        if idc_display_name is not None:
            input_["idc_display_name"] = idc_display_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_redshift_idc_application(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        redshift_idc_application_arn: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        identity_namespace: Optional[
            "capo_redshift.types.identity_namespace_string.IdentityNamespaceString"
        ] = None,
        iam_role_arn: Optional["capo_redshift.types.string.String"] = None,
        idc_display_name: Optional[
            "capo_redshift.types.idc_display_name_string.IdcDisplayNameString"
        ] = None,
        authorized_token_issuer_list: Optional[
            "capo_redshift.types.authorized_token_issuer_list.AuthorizedTokenIssuerList"
        ] = None,
        service_integrations: Optional[
            "capo_redshift.types.service_integration_list.ServiceIntegrationList"
        ] = None,
    ) -> "capo_redshift.types.modify_redshift_idc_application_result.ModifyRedshiftIdcApplicationResult":
        """<p>Changes an existing Amazon Redshift IAM Identity Center application.</p>

        Args:
            redshift_idc_application_arn: <p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>
            identity_namespace: <p>The namespace for the Amazon Redshift IAM Identity Center application to change. It determines which managed application verifies the connection token.</p>
            iam_role_arn: <p>The IAM role ARN associated with the Amazon Redshift IAM Identity Center application to change. It has the required permissions to be assumed and invoke the IDC Identity Center API.</p>
            idc_display_name: <p>The display name for the Amazon Redshift IAM Identity Center application to change. It appears on the console.</p>
            authorized_token_issuer_list: <p>The authorized token issuer list for the Amazon Redshift IAM Identity Center application to change.</p>
            service_integrations: <p>A collection of service integrations associated with the application.</p>

        Raises:
            capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault: <p>A dependent service denied access for the integration.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.redshift_idc_application_not_exists_fault.RedshiftIdcApplicationNotExistsFault: <p>The application you attempted to find doesn't exist.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_redshift_idc_application_message.ModifyRedshiftIdcApplicationMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_redshift_idc_application_result.ModifyRedshiftIdcApplicationResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_redshift_idc_application

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_redshift_idc_application.async_modify_redshift_idc_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_redshift_idc_application_message.ModifyRedshiftIdcApplicationMessage = {}
        if redshift_idc_application_arn is not None:
            input_["redshift_idc_application_arn"] = redshift_idc_application_arn
        if identity_namespace is not None:
            input_["identity_namespace"] = identity_namespace
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn
        if idc_display_name is not None:
            input_["idc_display_name"] = idc_display_name
        if authorized_token_issuer_list is not None:
            input_["authorized_token_issuer_list"] = authorized_token_issuer_list
        if service_integrations is not None:
            input_["service_integrations"] = service_integrations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_scheduled_action(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        scheduled_action_name: Optional["capo_redshift.types.string.String"] = None,
        target_action: Optional[
            "capo_redshift.types.scheduled_action_type.ScheduledActionType"
        ] = None,
        schedule: Optional["capo_redshift.types.string.String"] = None,
        iam_role: Optional["capo_redshift.types.string.String"] = None,
        scheduled_action_description: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        start_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_redshift.types.t_stamp.TStamp"] = None,
        enable: Optional["capo_redshift.types.boolean_optional.BooleanOptional"] = None,
    ) -> "capo_redshift.types.scheduled_action.ScheduledAction":
        """<p>Modifies a scheduled action. </p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action to modify. </p>
            target_action: <p>A modified JSON format of the scheduled action. For more information about this parameter, see <a>ScheduledAction</a>. </p>
            schedule: <p>A modified schedule in either <code>at( )</code> or <code>cron( )</code> format. For more information about this parameter, see <a>ScheduledAction</a>.</p>
            iam_role: <p>A different IAM role to assume to run the target action. For more information about this parameter, see <a>ScheduledAction</a>.</p>
            scheduled_action_description: <p>A modified description of the scheduled action. </p>
            start_time: <p>A modified start time of the scheduled action. For more information about this parameter, see <a>ScheduledAction</a>. </p>
            end_time: <p>A modified end time of the scheduled action. For more information about this parameter, see <a>ScheduledAction</a>. </p>
            enable: <p>A modified enable flag of the scheduled action. If true, the scheduled action is active. If false, the scheduled action is disabled. </p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_scheduled_action_fault.InvalidScheduledActionFault: <p>The scheduled action is not valid. </p>
            capo_redshift.errors.invalid_schedule_fault.InvalidScheduleFault: <p>The schedule you submitted isn't valid.</p>
            capo_redshift.errors.scheduled_action_not_found_fault.ScheduledActionNotFoundFault: <p>The scheduled action cannot be found. </p>
            capo_redshift.errors.scheduled_action_type_unsupported_fault.ScheduledActionTypeUnsupportedFault: <p>The action type specified for a scheduled action is not supported. </p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_scheduled_action_message.ModifyScheduledActionMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.scheduled_action.ScheduledAction"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_scheduled_action

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_scheduled_action.async_modify_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_scheduled_action_message.ModifyScheduledActionMessage = {}
        if scheduled_action_name is not None:
            input_["scheduled_action_name"] = scheduled_action_name
        if target_action is not None:
            input_["target_action"] = target_action
        if schedule is not None:
            input_["schedule"] = schedule
        if iam_role is not None:
            input_["iam_role"] = iam_role
        if scheduled_action_description is not None:
            input_["scheduled_action_description"] = scheduled_action_description
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if enable is not None:
            input_["enable"] = enable

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_snapshot_copy_retention_period(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        retention_period: Optional["capo_redshift.types.integer.Integer"] = None,
        manual: Optional["capo_redshift.types.boolean.Boolean"] = None,
    ) -> "capo_redshift.types.modify_snapshot_copy_retention_period_result.ModifySnapshotCopyRetentionPeriodResult":
        """<p>Modifies the number of days to retain snapshots in the destination Amazon Web Services Region after they are copied from the source Amazon Web Services Region. By default, this operation only changes the retention period of copied automated snapshots. The retention periods for both new and existing copied automated snapshots are updated with the new retention period. You can set the manual option to change only the retention periods of copied manual snapshots. If you set this option, only newly copied manual snapshots have the new retention period. </p>

        Args:
            cluster_identifier: <p>The unique identifier of the cluster for which you want to change the retention period for either automated or manual snapshots that are copied to a destination Amazon Web Services Region.</p> <p>Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.</p>
            retention_period: <p>The number of days to retain automated snapshots in the destination Amazon Web Services Region after they are copied from the source Amazon Web Services Region.</p> <p>By default, this only changes the retention period of copied automated snapshots. </p> <p>If you decrease the retention period for automated snapshots that are copied to a destination Amazon Web Services Region, Amazon Redshift deletes any existing automated snapshots that were copied to the destination Amazon Web Services Region and that fall outside of the new retention period.</p> <p>Constraints: Must be at least 1 and no more than 35 for automated snapshots. </p> <p>If you specify the <code>manual</code> option, only newly copied manual snapshots will have the new retention period. </p> <p>If you specify the value of -1 newly copied manual snapshots are retained indefinitely.</p> <p>Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.</p>
            manual: <p>Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_retention_period_fault.InvalidRetentionPeriodFault: <p>The retention period specified is either in the past or is not a valid value.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            capo_redshift.errors.snapshot_copy_disabled_fault.SnapshotCopyDisabledFault: <p>Cross-region snapshot copy was temporarily disabled. Try your request again.</p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_snapshot_copy_retention_period_message.ModifySnapshotCopyRetentionPeriodMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.modify_snapshot_copy_retention_period_result.ModifySnapshotCopyRetentionPeriodResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_snapshot_copy_retention_period

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_snapshot_copy_retention_period.async_modify_snapshot_copy_retention_period(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_snapshot_copy_retention_period_message.ModifySnapshotCopyRetentionPeriodMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if manual is not None:
            input_["manual"] = manual

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_snapshot_schedule(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        schedule_identifier: Optional["capo_redshift.types.string.String"] = None,
        schedule_definitions: Optional[
            "capo_redshift.types.schedule_definition_list.ScheduleDefinitionList"
        ] = None,
    ) -> "capo_redshift.types.snapshot_schedule.SnapshotSchedule":
        """<p>Modifies a snapshot schedule. Any schedule associated with a cluster is modified asynchronously.</p>

        Args:
            schedule_identifier: <p>A unique alphanumeric identifier of the schedule to modify.</p>
            schedule_definitions: <p>An updated list of schedule definitions. A schedule definition is made up of schedule expressions, for example, "cron(30 12 *)" or "rate(12 hours)".</p>

        Raises:
            capo_redshift.errors.invalid_schedule_fault.InvalidScheduleFault: <p>The schedule you submitted isn't valid.</p>
            capo_redshift.errors.snapshot_schedule_not_found_fault.SnapshotScheduleNotFoundFault: <p>We could not find the specified snapshot schedule. </p>
            capo_redshift.errors.snapshot_schedule_update_in_progress_fault.SnapshotScheduleUpdateInProgressFault: <p>The specified snapshot schedule is already being updated.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_snapshot_schedule_message.ModifySnapshotScheduleMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.snapshot_schedule.SnapshotSchedule"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.modify_snapshot_schedule

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_snapshot_schedule.async_modify_snapshot_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_snapshot_schedule_message.ModifySnapshotScheduleMessage = {}
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if schedule_definitions is not None:
            input_["schedule_definitions"] = schedule_definitions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_usage_limit(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        usage_limit_id: Optional["capo_redshift.types.string.String"] = None,
        amount: Optional["capo_redshift.types.long_optional.LongOptional"] = None,
        breach_action: Optional[
            "capo_redshift.types.usage_limit_breach_action.UsageLimitBreachAction"
        ] = None,
    ) -> "capo_redshift.types.usage_limit.UsageLimit":
        """<p>Modifies a usage limit in a cluster. You can't modify the feature type or period of a usage limit.</p>

        Args:
            usage_limit_id: <p>The identifier of the usage limit to modify.</p>
            amount: <p>The new limit amount. For more information about this parameter, see <a>UsageLimit</a>. </p>
            breach_action: <p>The new action that Amazon Redshift takes when the limit is reached. For more information about this parameter, see <a>UsageLimit</a>. </p>

        Raises:
            capo_redshift.errors.invalid_usage_limit_fault.InvalidUsageLimitFault: <p>The usage limit is not valid.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.usage_limit_not_found_fault.UsageLimitNotFoundFault: <p>The usage limit identifier can't be found.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.modify_usage_limit_message.ModifyUsageLimitMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.usage_limit.UsageLimit"]:
            import capo_redshift._operations.redshift_service_version20121201.modify_usage_limit

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.modify_usage_limit.async_modify_usage_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.modify_usage_limit_message.ModifyUsageLimitMessage = {}
        if usage_limit_id is not None:
            input_["usage_limit_id"] = usage_limit_id
        if amount is not None:
            input_["amount"] = amount
        if breach_action is not None:
            input_["breach_action"] = breach_action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def pause_cluster(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.pause_cluster_result.PauseClusterResult":
        """<p>Pauses a cluster.</p>

        Args:
            cluster_identifier: <p>The identifier of the cluster to be paused.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.pause_cluster_message.PauseClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.pause_cluster_result.PauseClusterResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.pause_cluster

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.pause_cluster.async_pause_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.pause_cluster_message.PauseClusterMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def purchase_reserved_node_offering(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        reserved_node_offering_id: Optional["capo_redshift.types.string.String"] = None,
        node_count: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_redshift.types.purchase_reserved_node_offering_result.PurchaseReservedNodeOfferingResult":
        """<p>Allows you to purchase reserved nodes. Amazon Redshift offers a predefined set of reserved node offerings. You can purchase one or more of the offerings. You can call the <a>DescribeReservedNodeOfferings</a> API to obtain the available reserved node offerings. You can call this API by providing a specific reserved node offering and the number of nodes you want to reserve. </p> <p> For more information about reserved node offerings, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html">Purchasing Reserved Nodes</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            reserved_node_offering_id: <p>The unique identifier of the reserved node offering you want to purchase.</p>
            node_count: <p>The number of reserved nodes that you want to purchase.</p> <p>Default: <code>1</code> </p>

        Raises:
            capo_redshift.errors.reserved_node_already_exists_fault.ReservedNodeAlreadyExistsFault: <p>User already has a reservation with the given identifier.</p>
            capo_redshift.errors.reserved_node_offering_not_found_fault.ReservedNodeOfferingNotFoundFault: <p>Specified offering does not exist.</p>
            capo_redshift.errors.reserved_node_quota_exceeded_fault.ReservedNodeQuotaExceededFault: <p>Request would exceed the user's compute node quota. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.purchase_reserved_node_offering_message.PurchaseReservedNodeOfferingMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.purchase_reserved_node_offering_result.PurchaseReservedNodeOfferingResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.purchase_reserved_node_offering

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.purchase_reserved_node_offering.async_purchase_reserved_node_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.purchase_reserved_node_offering_message.PurchaseReservedNodeOfferingMessage = {}
        if reserved_node_offering_id is not None:
            input_["reserved_node_offering_id"] = reserved_node_offering_id
        if node_count is not None:
            input_["node_count"] = node_count

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        resource_arn: Optional["capo_redshift.types.string.String"] = None,
        policy: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.put_resource_policy_result.PutResourcePolicyResult":
        """<p>Updates the resource policy for a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource of which its resource policy is updated.</p>
            policy: <p>The content of the resource policy being updated.</p>

        Raises:
            capo_redshift.errors.conflict_policy_update_fault.ConflictPolicyUpdateFault: <p>There is a conflict while updating the resource policy.</p>
            capo_redshift.errors.invalid_policy_fault.InvalidPolicyFault: <p>The resource policy isn't valid.</p>
            capo_redshift.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.put_resource_policy_message.PutResourcePolicyMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.put_resource_policy_result.PutResourcePolicyResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.put_resource_policy_message.PutResourcePolicyMessage = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if policy is not None:
            input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reboot_cluster(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.reboot_cluster_result.RebootClusterResult":
        """<p>Reboots a cluster. This action is taken as soon as possible. It results in a momentary outage to the cluster, during which the cluster status is set to <code>rebooting</code>. A cluster event is created when the reboot is completed. Any pending cluster modifications (see <a>ModifyCluster</a>) are applied at this reboot. For more information about managing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html">Amazon Redshift Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>

        Args:
            cluster_identifier: <p>The cluster identifier.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.reboot_cluster_message.RebootClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.reboot_cluster_result.RebootClusterResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.reboot_cluster

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.reboot_cluster.async_reboot_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.reboot_cluster_message.RebootClusterMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_namespace(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        namespace_identifier: Optional[
            "capo_redshift.types.namespace_identifier_union.NamespaceIdentifierUnion"
        ] = None,
        consumer_identifiers: Optional[
            "capo_redshift.types.consumer_identifier_list.ConsumerIdentifierList"
        ] = None,
    ) -> "capo_redshift.types.register_namespace_output_message.RegisterNamespaceOutputMessage":
        """<p>Registers a cluster or serverless namespace to the Amazon Web Services Glue Data Catalog.</p>

        Args:
            namespace_identifier: <p>The unique identifier of the cluster or serverless namespace that you want to register. </p>
            consumer_identifiers: <p>An array containing the ID of the consumer account that you want to register the namespace to.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_namespace_fault.InvalidNamespaceFault: <p>The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.register_namespace_input_message.RegisterNamespaceInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.register_namespace_output_message.RegisterNamespaceOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.register_namespace

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.register_namespace.async_register_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.register_namespace_input_message.RegisterNamespaceInputMessage = {}
        if namespace_identifier is not None:
            input_["namespace_identifier"] = namespace_identifier
        if consumer_identifiers is not None:
            input_["consumer_identifiers"] = consumer_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_data_share(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        data_share_arn: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.data_share.DataShare":
        """<p>From a datashare consumer account, rejects the specified datashare.</p>

        Args:
            data_share_arn: <p>The Amazon Resource Name (ARN) of the datashare to reject.</p>

        Raises:
            capo_redshift.errors.invalid_data_share_fault.InvalidDataShareFault: <p>There is an error with the datashare.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.reject_data_share_message.RejectDataShareMessage]",
        ) -> AsyncOperationResponse["capo_redshift.types.data_share.DataShare"]:
            import capo_redshift._operations.redshift_service_version20121201.reject_data_share

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.reject_data_share.async_reject_data_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.reject_data_share_message.RejectDataShareMessage = {}
        if data_share_arn is not None:
            input_["data_share_arn"] = data_share_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        parameter_group_name: Optional["capo_redshift.types.string.String"] = None,
        reset_all_parameters: Optional["capo_redshift.types.boolean.Boolean"] = None,
        parameters: Optional[
            "capo_redshift.types.parameters_list.ParametersList"
        ] = None,
    ) -> "capo_redshift.types.cluster_parameter_group_name_message.ClusterParameterGroupNameMessage":
        """<p>Sets one or more parameters of the specified parameter group to their default values and sets the source values of the parameters to "engine-default". To reset the entire parameter group specify the <i>ResetAllParameters</i> parameter. For parameter changes to take effect you must reboot any associated clusters. </p>

        Args:
            parameter_group_name: <p>The name of the cluster parameter group to be reset.</p>
            reset_all_parameters: <p>If <code>true</code>, all parameters in the specified parameter group will be reset to their default values. </p> <p>Default: <code>true</code> </p>
            parameters: <p>An array of names of parameters to be reset. If <i>ResetAllParameters</i> option is not used, then at least one parameter name must be supplied. </p> <p>Constraints: A maximum of 20 parameters can be reset in a single request.</p>

        Raises:
            capo_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault: <p>The parameter group name does not refer to an existing parameter group.</p>
            capo_redshift.errors.invalid_cluster_parameter_group_state_fault.InvalidClusterParameterGroupStateFault: <p>The cluster parameter group action can not be completed because another task is in progress that involves the parameter group. Wait a few moments and try the operation again.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.reset_cluster_parameter_group_message.ResetClusterParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.cluster_parameter_group_name_message.ClusterParameterGroupNameMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.reset_cluster_parameter_group

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.reset_cluster_parameter_group.async_reset_cluster_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.reset_cluster_parameter_group_message.ResetClusterParameterGroupMessage = {}
        if parameter_group_name is not None:
            input_["parameter_group_name"] = parameter_group_name
        if reset_all_parameters is not None:
            input_["reset_all_parameters"] = reset_all_parameters
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resize_cluster(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        cluster_type: Optional["capo_redshift.types.string.String"] = None,
        node_type: Optional["capo_redshift.types.string.String"] = None,
        number_of_nodes: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        classic: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        reserved_node_id: Optional["capo_redshift.types.string.String"] = None,
        target_reserved_node_offering_id: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> "capo_redshift.types.resize_cluster_result.ResizeClusterResult":
        """<p>Changes the size of the cluster. You can change the cluster's type, or change the number or type of nodes. The default behavior is to use the elastic resize method. With an elastic resize, your cluster is available for read and write operations more quickly than with the classic resize method. </p> <p>Elastic resize operations have the following restrictions:</p> <ul> <li> <p>You can only resize clusters of the following types:</p> <ul> <li> <p>dc2.large</p> </li> <li> <p>dc2.8xlarge</p> </li> <li> <p>rg.large</p> </li> <li> <p>rg.xlarge</p> </li> <li> <p>rg.4xlarge</p> </li> <li> <p>rg.12xlarge</p> </li> <li> <p>ra3.large</p> </li> <li> <p>ra3.xlplus</p> </li> <li> <p>ra3.4xlarge</p> </li> <li> <p>ra3.16xlarge</p> </li> </ul> </li> <li> <p>The type of nodes that you add must match the node type for the cluster.</p> </li> </ul>

        Args:
            cluster_identifier: <p>The unique identifier for the cluster to resize.</p>
            cluster_type: <p>The new cluster type for the specified cluster.</p>
            node_type: <p>The new node type for the nodes you are adding. If not specified, the cluster's current node type is used.</p>
            number_of_nodes: <p>The new number of nodes for the cluster. If not specified, the cluster's current number of nodes is used.</p>
            classic: <p>A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to <code>false</code>, the resize type is elastic. </p>
            reserved_node_id: <p>The identifier of the reserved node.</p>
            target_reserved_node_offering_id: <p>The identifier of the target reserved node offering.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault: <p>The number of nodes specified exceeds the allotted capacity of the cluster.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_reserved_node_state_fault.InvalidReservedNodeStateFault: <p>Indicates that the Reserved Node being exchanged is not in an active state.</p>
            capo_redshift.errors.limit_exceeded_fault.LimitExceededFault: <p>The encryption key has exceeded its grant limit in Amazon Web Services KMS.</p>
            capo_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault.NumberOfNodesPerClusterLimitExceededFault: <p>The operation would exceed the number of nodes allowed for a cluster.</p>
            capo_redshift.errors.number_of_nodes_quota_exceeded_fault.NumberOfNodesQuotaExceededFault: <p>The operation would exceed the number of nodes allotted to the account. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.reserved_node_already_exists_fault.ReservedNodeAlreadyExistsFault: <p>User already has a reservation with the given identifier.</p>
            capo_redshift.errors.reserved_node_already_migrated_fault.ReservedNodeAlreadyMigratedFault: <p>Indicates that the reserved node has already been exchanged.</p>
            capo_redshift.errors.reserved_node_not_found_fault.ReservedNodeNotFoundFault: <p>The specified reserved compute node not found.</p>
            capo_redshift.errors.reserved_node_offering_not_found_fault.ReservedNodeOfferingNotFoundFault: <p>Specified offering does not exist.</p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.unsupported_option_fault.UnsupportedOptionFault: <p>A request option was specified that is not supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.resize_cluster_message.ResizeClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.resize_cluster_result.ResizeClusterResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.resize_cluster

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.resize_cluster.async_resize_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.resize_cluster_message.ResizeClusterMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if cluster_type is not None:
            input_["cluster_type"] = cluster_type
        if node_type is not None:
            input_["node_type"] = node_type
        if number_of_nodes is not None:
            input_["number_of_nodes"] = number_of_nodes
        if classic is not None:
            input_["classic"] = classic
        if reserved_node_id is not None:
            input_["reserved_node_id"] = reserved_node_id
        if target_reserved_node_offering_id is not None:
            input_["target_reserved_node_offering_id"] = (
                target_reserved_node_offering_id
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_from_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_arn: Optional["capo_redshift.types.string.String"] = None,
        snapshot_cluster_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        port: Optional["capo_redshift.types.integer_optional.IntegerOptional"] = None,
        availability_zone: Optional["capo_redshift.types.string.String"] = None,
        allow_version_upgrade: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        cluster_subnet_group_name: Optional["capo_redshift.types.string.String"] = None,
        publicly_accessible: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        owner_account: Optional["capo_redshift.types.string.String"] = None,
        hsm_client_certificate_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        hsm_configuration_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        elastic_ip: Optional["capo_redshift.types.string.String"] = None,
        cluster_parameter_group_name: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        cluster_security_groups: Optional[
            "capo_redshift.types.cluster_security_group_name_list.ClusterSecurityGroupNameList"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_redshift.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        preferred_maintenance_window: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        automated_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        manual_snapshot_retention_period: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        kms_key_id: Optional["capo_redshift.types.string.String"] = None,
        node_type: Optional["capo_redshift.types.string.String"] = None,
        enhanced_vpc_routing: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        additional_info: Optional["capo_redshift.types.string.String"] = None,
        iam_roles: Optional[
            "capo_redshift.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        maintenance_track_name: Optional["capo_redshift.types.string.String"] = None,
        snapshot_schedule_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        number_of_nodes: Optional[
            "capo_redshift.types.integer_optional.IntegerOptional"
        ] = None,
        availability_zone_relocation: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        aqua_configuration_status: Optional[
            "capo_redshift.types.aqua_configuration_status.AquaConfigurationStatus"
        ] = None,
        default_iam_role_arn: Optional["capo_redshift.types.string.String"] = None,
        reserved_node_id: Optional["capo_redshift.types.string.String"] = None,
        target_reserved_node_offering_id: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        encrypted: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        manage_master_password: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        master_password_secret_kms_key_id: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        ip_address_type: Optional["capo_redshift.types.string.String"] = None,
        multi_az: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
        catalog_name: Optional[
            "capo_redshift.types.catalog_name_string.CatalogNameString"
        ] = None,
        redshift_idc_application_arn: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> "capo_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult":
        """<p>Creates a new cluster from a snapshot. By default, Amazon Redshift creates the resulting cluster with the same configuration as the original cluster from which the snapshot was created, except that the new cluster is created with the default cluster security and parameter groups. After Amazon Redshift creates the cluster, you can use the <a>ModifyCluster</a> API to associate a different security group and different parameter group with the restored cluster. If you are using a DS node type, you can also choose to change to another DS node type of the same size during restore.</p> <p>If you restore a cluster into a VPC, you must provide a cluster subnet group where you want the cluster restored.</p> <p>VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a subnet group for a provisioned cluster is in an account with VPC BPA turned on, the following capabilities are blocked:</p> <ul> <li> <p>Creating a public cluster</p> </li> <li> <p>Restoring a public cluster</p> </li> <li> <p>Modifying a private cluster to be public</p> </li> <li> <p>Adding a subnet with VPC BPA turned on to the subnet group when there's at least one public cluster within the group</p> </li> </ul> <p>For more information about VPC BPA, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html">Block public access to VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p> <p> For more information about working with snapshots, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html">Amazon Redshift Snapshots</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            cluster_identifier: <p>The identifier of the cluster that will be created from restoring the snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>Alphabetic characters must be lowercase.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique for all clusters within an Amazon Web Services account.</p> </li> </ul>
            snapshot_identifier: <p>The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive. You must specify this parameter or <code>snapshotArn</code>, but not both.</p> <p>Example: <code>my-snapshot-id</code> </p>
            snapshot_arn: <p>The Amazon Resource Name (ARN) of the snapshot associated with the message to restore from a cluster. You must specify this parameter or <code>snapshotIdentifier</code>, but not both.</p>
            snapshot_cluster_identifier: <p>The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.</p>
            port: <p>The port number on which the cluster accepts connections.</p> <p>Default: The same port as the original cluster.</p> <p>Valid values: For clusters with DC2 nodes, must be within the range <code>1150</code>-<code>65535</code>. For clusters with RG or RA3 nodes, must be within the ranges <code>5431</code>-<code>5455</code> or <code>8191</code>-<code>8215</code>.</p>
            availability_zone: <p>The Amazon EC2 Availability Zone in which to restore the cluster.</p> <p>Default: A random, system-chosen Availability Zone.</p> <p>Example: <code>us-east-2a</code> </p>
            allow_version_upgrade: <p>If <code>true</code>, major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. </p> <p>Default: <code>true</code> </p>
            cluster_subnet_group_name: <p>The name of the subnet group where you want to cluster restored.</p> <p>A snapshot of cluster in VPC can be restored only in VPC. Therefore, you must provide subnet group name where you want the cluster restored.</p>
            publicly_accessible: <p>If <code>true</code>, the cluster can be accessed from a public network. </p> <p>Default: false</p>
            owner_account: <p>The Amazon Web Services account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.</p>
            hsm_client_certificate_identifier: <p>Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.</p>
            hsm_configuration_identifier: <p>Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.</p>
            elastic_ip: <p>The Elastic IP (EIP) address for the cluster. Don't specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on.</p>
            cluster_parameter_group_name: <p>The name of the parameter group to be associated with this cluster.</p> <p>Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Working with Amazon Redshift Parameter Groups</a>.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            cluster_security_groups: <p>A list of security groups to be associated with this cluster.</p> <p>Default: The default cluster security group for Amazon Redshift.</p> <p>Cluster security groups only apply to clusters outside of VPCs.</p>
            vpc_security_group_ids: <p>A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.</p> <p>Default: The default VPC security group is associated with the cluster.</p> <p>VPC security groups only apply to clusters in VPCs.</p>
            preferred_maintenance_window: <p>The weekly time range (in UTC) during which automated cluster maintenance can occur.</p> <p> Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p> Default: The value selected for the cluster from which the snapshot was taken. For more information about the time blocks for each region, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows">Maintenance Windows</a> in Amazon Redshift Cluster Management Guide. </p> <p>Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun</p> <p>Constraints: Minimum 30-minute window.</p>
            automated_snapshot_retention_period: <p>The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with <a>CreateClusterSnapshot</a>. </p> <p>You can't disable automated snapshots for RG or RA3 node types. Set the automated retention period from 1-35 days.</p> <p>Default: The value selected for the cluster from which the snapshot was taken.</p> <p>Constraints: Must be a value from 0 to 35.</p>
            manual_snapshot_retention_period: <p>The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>
            kms_key_id: <p>The Key Management Service (KMS) key ID of the encryption key that encrypts data in the cluster restored from a shared snapshot. You can also provide the key ID when you restore from an unencrypted snapshot to an encrypted cluster in the same account. Additionally, you can specify a new KMS key ID when you restore from an encrypted snapshot in the same account in order to change it. In that case, the restored cluster is encrypted with the new KMS key ID.</p>
            node_type: <p>The node type that the restored cluster will be provisioned with.</p> <p>If you have a DC instance type, you must restore into that same instance type and size. In other words, you can only restore a dc2.large node type into another dc2 type. For more information about node types, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-about-clusters-and-nodes"> About Clusters and Nodes</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            enhanced_vpc_routing: <p>An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html">Enhanced VPC Routing</a> in the Amazon Redshift Cluster Management Guide.</p> <p>If this option is <code>true</code>, enhanced VPC routing is enabled. </p> <p>Default: false</p>
            additional_info: <p>Reserved.</p>
            iam_roles: <p>A list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. </p> <p>The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Quotas and limits</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>
            maintenance_track_name: <p>The name of the maintenance track for the restored cluster. When you take a snapshot, the snapshot inherits the <code>MaintenanceTrack</code> value from the cluster. The snapshot might be on a different track than the cluster that was the source for the snapshot. For example, suppose that you take a snapshot of a cluster that is on the current track and then change the cluster to be on the trailing track. In this case, the snapshot and the source cluster are on different tracks.</p>
            snapshot_schedule_identifier: <p>A unique identifier for the snapshot schedule.</p>
            number_of_nodes: <p>The number of nodes specified when provisioning the restored cluster.</p>
            availability_zone_relocation: <p>The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is restored.</p>
            aqua_configuration_status: <p>This parameter is retired. It does not set the AQUA configuration status. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was last modified while it was restored from a snapshot.</p>
            reserved_node_id: <p>The identifier of the target reserved node offering.</p>
            target_reserved_node_offering_id: <p>The identifier of the target reserved node offering.</p>
            encrypted: <p>Enables support for restoring an unencrypted snapshot to a cluster encrypted with Key Management Service (KMS) and a customer managed key.</p>
            manage_master_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the restored cluster's admin credentials. If <code>ManageMasterPassword</code> is false or not set, Amazon Redshift uses the admin credentials the cluster had at the time the snapshot was taken.</p>
            master_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret. You can only use this parameter if <code>ManageMasterPassword</code> is true.</p>
            ip_address_type: <p>The IP address type for the cluster. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>
            multi_az: <p>If true, the snapshot will be restored to a cluster deployed in two Availability Zones.</p>
            catalog_name: <p>The name of the Glue Data Catalog that will be associated with the cluster enabled with Amazon Redshift federated permissions.</p> <p>Constraints:</p> <ul> <li> <p>Must contain at least one lowercase letter.</p> </li> <li> <p>Can only contain lowercase letters (a-z), numbers (0-9), underscores (_), and hyphens (-).</p> </li> </ul> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p> <p>Example: <code>my-catalog_01</code> </p>
            redshift_idc_application_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation on a cluster enabled with Amazon Redshift federated permissions.</p>

        Raises:
            capo_redshift.errors.access_to_snapshot_denied_fault.AccessToSnapshotDeniedFault: <p>The owner of the specified snapshot has not authorized your account to access the snapshot.</p>
            capo_redshift.errors.cluster_already_exists_fault.ClusterAlreadyExistsFault: <p>The account already has a cluster with the given identifier.</p>
            capo_redshift.errors.cluster_parameter_group_not_found_fault.ClusterParameterGroupNotFoundFault: <p>The parameter group name does not refer to an existing parameter group.</p>
            capo_redshift.errors.cluster_quota_exceeded_fault.ClusterQuotaExceededFault: <p>The request would exceed the allowed number of cluster instances for this account. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault: <p>The cluster security group name does not refer to an existing cluster security group.</p>
            capo_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault: <p>The snapshot identifier does not refer to an existing cluster snapshot.</p>
            capo_redshift.errors.cluster_subnet_group_not_found_fault.ClusterSubnetGroupNotFoundFault: <p>The cluster subnet group name does not refer to an existing cluster subnet group.</p>
            capo_redshift.errors.dependent_service_access_denied_fault.DependentServiceAccessDeniedFault: <p>A dependent service denied access for the integration.</p>
            capo_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault: <p>The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.</p>
            capo_redshift.errors.dependent_service_unavailable_fault.DependentServiceUnavailableFault: <p>Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.</p>
            capo_redshift.errors.hsm_client_certificate_not_found_fault.HsmClientCertificateNotFoundFault: <p>There is no Amazon Redshift HSM client certificate with the specified identifier.</p>
            capo_redshift.errors.hsm_configuration_not_found_fault.HsmConfigurationNotFoundFault: <p>There is no Amazon Redshift HSM configuration with the specified identifier.</p>
            capo_redshift.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault: <p>The number of nodes specified exceeds the allotted capacity of the cluster.</p>
            capo_redshift.errors.invalid_cluster_snapshot_state_fault.InvalidClusterSnapshotStateFault: <p>The specified cluster snapshot is not in the <code>available</code> state, or other accounts are authorized to access the snapshot. </p>
            capo_redshift.errors.invalid_cluster_subnet_group_state_fault.InvalidClusterSubnetGroupStateFault: <p>The cluster subnet group cannot be deleted because it is in use.</p>
            capo_redshift.errors.invalid_cluster_track_fault.InvalidClusterTrackFault: <p>The provided cluster track name is not valid.</p>
            capo_redshift.errors.invalid_elastic_ip_fault.InvalidElasticIpFault: <p>The Elastic IP (EIP) is invalid or cannot be found.</p>
            capo_redshift.errors.invalid_reserved_node_state_fault.InvalidReservedNodeStateFault: <p>Indicates that the Reserved Node being exchanged is not in an active state.</p>
            capo_redshift.errors.invalid_restore_fault.InvalidRestoreFault: <p>The restore is invalid.</p>
            capo_redshift.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is not valid, or not all of the subnets are in the same VPC.</p>
            capo_redshift.errors.invalid_tag_fault.InvalidTagFault: <p>The tag is invalid.</p>
            capo_redshift.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The cluster subnet group does not cover all Availability Zones.</p>
            capo_redshift.errors.ipv6_cidr_block_not_found_fault.Ipv6CidrBlockNotFoundFault: <p>There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack mode, associate an IPv6 CIDR block with each subnet in your VPC.</p>
            capo_redshift.errors.limit_exceeded_fault.LimitExceededFault: <p>The encryption key has exceeded its grant limit in Amazon Web Services KMS.</p>
            capo_redshift.errors.number_of_nodes_per_cluster_limit_exceeded_fault.NumberOfNodesPerClusterLimitExceededFault: <p>The operation would exceed the number of nodes allowed for a cluster.</p>
            capo_redshift.errors.number_of_nodes_quota_exceeded_fault.NumberOfNodesQuotaExceededFault: <p>The operation would exceed the number of nodes allotted to the account. For information about increasing your quota, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Limits in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>
            capo_redshift.errors.redshift_idc_application_not_exists_fault.RedshiftIdcApplicationNotExistsFault: <p>The application you attempted to find doesn't exist.</p>
            capo_redshift.errors.reserved_node_already_exists_fault.ReservedNodeAlreadyExistsFault: <p>User already has a reservation with the given identifier.</p>
            capo_redshift.errors.reserved_node_already_migrated_fault.ReservedNodeAlreadyMigratedFault: <p>Indicates that the reserved node has already been exchanged.</p>
            capo_redshift.errors.reserved_node_not_found_fault.ReservedNodeNotFoundFault: <p>The specified reserved compute node not found.</p>
            capo_redshift.errors.reserved_node_offering_not_found_fault.ReservedNodeOfferingNotFoundFault: <p>Specified offering does not exist.</p>
            capo_redshift.errors.snapshot_schedule_not_found_fault.SnapshotScheduleNotFoundFault: <p>We could not find the specified snapshot schedule. </p>
            capo_redshift.errors.tag_limit_exceeded_fault.TagLimitExceededFault: <p>You have exceeded the number of tags allowed.</p>
            capo_redshift.errors.unauthorized_operation.UnauthorizedOperation: <p>Your account is not authorized to perform the requested operation.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.restore_from_cluster_snapshot_message.RestoreFromClusterSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.restore_from_cluster_snapshot_result.RestoreFromClusterSnapshotResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.restore_from_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.restore_from_cluster_snapshot.async_restore_from_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.restore_from_cluster_snapshot_message.RestoreFromClusterSnapshotMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if snapshot_identifier is not None:
            input_["snapshot_identifier"] = snapshot_identifier
        if snapshot_arn is not None:
            input_["snapshot_arn"] = snapshot_arn
        if snapshot_cluster_identifier is not None:
            input_["snapshot_cluster_identifier"] = snapshot_cluster_identifier
        if port is not None:
            input_["port"] = port
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if allow_version_upgrade is not None:
            input_["allow_version_upgrade"] = allow_version_upgrade
        if cluster_subnet_group_name is not None:
            input_["cluster_subnet_group_name"] = cluster_subnet_group_name
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if hsm_client_certificate_identifier is not None:
            input_["hsm_client_certificate_identifier"] = (
                hsm_client_certificate_identifier
            )
        if hsm_configuration_identifier is not None:
            input_["hsm_configuration_identifier"] = hsm_configuration_identifier
        if elastic_ip is not None:
            input_["elastic_ip"] = elastic_ip
        if cluster_parameter_group_name is not None:
            input_["cluster_parameter_group_name"] = cluster_parameter_group_name
        if cluster_security_groups is not None:
            input_["cluster_security_groups"] = cluster_security_groups
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if automated_snapshot_retention_period is not None:
            input_["automated_snapshot_retention_period"] = (
                automated_snapshot_retention_period
            )
        if manual_snapshot_retention_period is not None:
            input_["manual_snapshot_retention_period"] = (
                manual_snapshot_retention_period
            )
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if node_type is not None:
            input_["node_type"] = node_type
        if enhanced_vpc_routing is not None:
            input_["enhanced_vpc_routing"] = enhanced_vpc_routing
        if additional_info is not None:
            input_["additional_info"] = additional_info
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if maintenance_track_name is not None:
            input_["maintenance_track_name"] = maintenance_track_name
        if snapshot_schedule_identifier is not None:
            input_["snapshot_schedule_identifier"] = snapshot_schedule_identifier
        if number_of_nodes is not None:
            input_["number_of_nodes"] = number_of_nodes
        if availability_zone_relocation is not None:
            input_["availability_zone_relocation"] = availability_zone_relocation
        if aqua_configuration_status is not None:
            input_["aqua_configuration_status"] = aqua_configuration_status
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if reserved_node_id is not None:
            input_["reserved_node_id"] = reserved_node_id
        if target_reserved_node_offering_id is not None:
            input_["target_reserved_node_offering_id"] = (
                target_reserved_node_offering_id
            )
        if encrypted is not None:
            input_["encrypted"] = encrypted
        if manage_master_password is not None:
            input_["manage_master_password"] = manage_master_password
        if master_password_secret_kms_key_id is not None:
            input_["master_password_secret_kms_key_id"] = (
                master_password_secret_kms_key_id
            )
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if multi_az is not None:
            input_["multi_az"] = multi_az
        if catalog_name is not None:
            input_["catalog_name"] = catalog_name
        if redshift_idc_application_arn is not None:
            input_["redshift_idc_application_arn"] = redshift_idc_application_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_table_from_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        source_database_name: Optional["capo_redshift.types.string.String"] = None,
        source_schema_name: Optional["capo_redshift.types.string.String"] = None,
        source_table_name: Optional["capo_redshift.types.string.String"] = None,
        target_database_name: Optional["capo_redshift.types.string.String"] = None,
        target_schema_name: Optional["capo_redshift.types.string.String"] = None,
        new_table_name: Optional["capo_redshift.types.string.String"] = None,
        enable_case_sensitive_identifier: Optional[
            "capo_redshift.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_redshift.types.restore_table_from_cluster_snapshot_result.RestoreTableFromClusterSnapshotResult":
        """<p>Creates a new table from a table in an Amazon Redshift cluster snapshot. You must create the new table within the Amazon Redshift cluster that the snapshot was taken from.</p> <p>You cannot use <code>RestoreTableFromClusterSnapshot</code> to restore a table with the same name as an existing table in an Amazon Redshift cluster. That is, you cannot overwrite an existing table in a cluster with a restored table. If you want to replace your original table with a new, restored table, then rename or drop your original table before you call <code>RestoreTableFromClusterSnapshot</code>. When you have renamed your original table, then you can pass the original name of the table as the <code>NewTableName</code> parameter value in the call to <code>RestoreTableFromClusterSnapshot</code>. This way, you can replace the original table with the table created from the snapshot.</p> <p>You can't use this operation to restore tables with <a href="https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html#t_Sorting_data-interleaved">interleaved sort keys</a>.</p>

        Args:
            cluster_identifier: <p>The identifier of the Amazon Redshift cluster to restore the table to.</p>
            snapshot_identifier: <p>The identifier of the snapshot to restore the table from. This snapshot must have been created from the Amazon Redshift cluster specified by the <code>ClusterIdentifier</code> parameter.</p>
            source_database_name: <p>The name of the source database that contains the table to restore from.</p>
            source_schema_name: <p>The name of the source schema that contains the table to restore from. If you do not specify a <code>SourceSchemaName</code> value, the default is <code>public</code>.</p>
            source_table_name: <p>The name of the source table to restore from.</p>
            target_database_name: <p>The name of the database to restore the table to.</p>
            target_schema_name: <p>The name of the schema to restore the table to.</p>
            new_table_name: <p>The name of the table to create as a result of the current request.</p>
            enable_case_sensitive_identifier: <p>Indicates whether name identifiers for database, schema, and table are case sensitive. If <code>true</code>, the names are case sensitive. If <code>false</code> (default), the names are not case sensitive.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault: <p>The snapshot identifier does not refer to an existing cluster snapshot.</p>
            capo_redshift.errors.in_progress_table_restore_quota_exceeded_fault.InProgressTableRestoreQuotaExceededFault: <p>You have exceeded the allowed number of table restore requests. Wait for your current table restore requests to complete before making a new request.</p>
            capo_redshift.errors.invalid_cluster_snapshot_state_fault.InvalidClusterSnapshotStateFault: <p>The specified cluster snapshot is not in the <code>available</code> state, or other accounts are authorized to access the snapshot. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_table_restore_argument_fault.InvalidTableRestoreArgumentFault: <p>The value specified for the <code>sourceDatabaseName</code>, <code>sourceSchemaName</code>, or <code>sourceTableName</code> parameter, or a combination of these, doesn't exist in the snapshot.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.restore_table_from_cluster_snapshot_message.RestoreTableFromClusterSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.restore_table_from_cluster_snapshot_result.RestoreTableFromClusterSnapshotResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.restore_table_from_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.restore_table_from_cluster_snapshot.async_restore_table_from_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.restore_table_from_cluster_snapshot_message.RestoreTableFromClusterSnapshotMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if snapshot_identifier is not None:
            input_["snapshot_identifier"] = snapshot_identifier
        if source_database_name is not None:
            input_["source_database_name"] = source_database_name
        if source_schema_name is not None:
            input_["source_schema_name"] = source_schema_name
        if source_table_name is not None:
            input_["source_table_name"] = source_table_name
        if target_database_name is not None:
            input_["target_database_name"] = target_database_name
        if target_schema_name is not None:
            input_["target_schema_name"] = target_schema_name
        if new_table_name is not None:
            input_["new_table_name"] = new_table_name
        if enable_case_sensitive_identifier is not None:
            input_["enable_case_sensitive_identifier"] = (
                enable_case_sensitive_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resume_cluster(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.resume_cluster_result.ResumeClusterResult":
        """<p>Resumes a paused cluster.</p>

        Args:
            cluster_identifier: <p>The identifier of the cluster to be resumed.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault: <p>The number of nodes specified exceeds the allotted capacity of the cluster.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.resume_cluster_message.ResumeClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.resume_cluster_result.ResumeClusterResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.resume_cluster

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.resume_cluster.async_resume_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.resume_cluster_message.ResumeClusterMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def revoke_cluster_security_group_ingress(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_security_group_name: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        cidrip: Optional["capo_redshift.types.string.String"] = None,
        ec2_security_group_name: Optional["capo_redshift.types.string.String"] = None,
        ec2_security_group_owner_id: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> "capo_redshift.types.revoke_cluster_security_group_ingress_result.RevokeClusterSecurityGroupIngressResult":
        """<p>Revokes an ingress rule in an Amazon Redshift security group for a previously authorized IP range or Amazon EC2 security group. To add an ingress rule, see <a>AuthorizeClusterSecurityGroupIngress</a>. For information about managing security groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html">Amazon Redshift Cluster Security Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>

        Args:
            cluster_security_group_name: <p>The name of the security Group from which to revoke the ingress rule.</p>
            cidrip: <p>The IP range for which to revoke access. This range must be a valid Classless Inter-Domain Routing (CIDR) block of IP addresses. If <code>CIDRIP</code> is specified, <code>EC2SecurityGroupName</code> and <code>EC2SecurityGroupOwnerId</code> cannot be provided. </p>
            ec2_security_group_name: <p>The name of the EC2 Security Group whose access is to be revoked. If <code>EC2SecurityGroupName</code> is specified, <code>EC2SecurityGroupOwnerId</code> must also be provided and <code>CIDRIP</code> cannot be provided. </p>
            ec2_security_group_owner_id: <p>The Amazon Web Services account number of the owner of the security group specified in the <code>EC2SecurityGroupName</code> parameter. The Amazon Web Services access key ID is not an acceptable value. If <code>EC2SecurityGroupOwnerId</code> is specified, <code>EC2SecurityGroupName</code> must also be provided. and <code>CIDRIP</code> cannot be provided. </p> <p>Example: <code>111122223333</code> </p>

        Raises:
            capo_redshift.errors.authorization_not_found_fault.AuthorizationNotFoundFault: <p>The specified CIDR IP range or EC2 security group is not authorized for the specified cluster security group.</p>
            capo_redshift.errors.cluster_security_group_not_found_fault.ClusterSecurityGroupNotFoundFault: <p>The cluster security group name does not refer to an existing cluster security group.</p>
            capo_redshift.errors.invalid_cluster_security_group_state_fault.InvalidClusterSecurityGroupStateFault: <p>The state of the cluster security group is not <code>available</code>. </p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.revoke_cluster_security_group_ingress_message.RevokeClusterSecurityGroupIngressMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.revoke_cluster_security_group_ingress_result.RevokeClusterSecurityGroupIngressResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.revoke_cluster_security_group_ingress

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.revoke_cluster_security_group_ingress.async_revoke_cluster_security_group_ingress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.revoke_cluster_security_group_ingress_message.RevokeClusterSecurityGroupIngressMessage = {}
        if cluster_security_group_name is not None:
            input_["cluster_security_group_name"] = cluster_security_group_name
        if cidrip is not None:
            input_["cidrip"] = cidrip
        if ec2_security_group_name is not None:
            input_["ec2_security_group_name"] = ec2_security_group_name
        if ec2_security_group_owner_id is not None:
            input_["ec2_security_group_owner_id"] = ec2_security_group_owner_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def revoke_endpoint_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
        account: Optional["capo_redshift.types.string.String"] = None,
        vpc_ids: Optional[
            "capo_redshift.types.vpc_identifier_list.VpcIdentifierList"
        ] = None,
        force: Optional["capo_redshift.types.boolean.Boolean"] = None,
    ) -> "capo_redshift.types.endpoint_authorization.EndpointAuthorization":
        """<p>Revokes access to a cluster.</p>

        Args:
            cluster_identifier: <p>The cluster to revoke access from.</p>
            account: <p>The Amazon Web Services account ID whose access is to be revoked.</p>
            vpc_ids: <p>The virtual private cloud (VPC) identifiers for which access is to be revoked.</p>
            force: <p>Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.endpoint_authorization_not_found_fault.EndpointAuthorizationNotFoundFault: <p>The authorization for this endpoint can't be found.</p>
            capo_redshift.errors.endpoint_not_found_fault.EndpointNotFoundFault: <p>The endpoint name doesn't refer to an existing endpoint.</p>
            capo_redshift.errors.invalid_authorization_state_fault.InvalidAuthorizationStateFault: <p>The status of the authorization is not valid.</p>
            capo_redshift.errors.invalid_cluster_security_group_state_fault.InvalidClusterSecurityGroupStateFault: <p>The state of the cluster security group is not <code>available</code>. </p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.invalid_endpoint_state_fault.InvalidEndpointStateFault: <p>The status of the endpoint is not valid.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.revoke_endpoint_access_message.RevokeEndpointAccessMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.endpoint_authorization.EndpointAuthorization"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.revoke_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.revoke_endpoint_access.async_revoke_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.revoke_endpoint_access_message.RevokeEndpointAccessMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if account is not None:
            input_["account"] = account
        if vpc_ids is not None:
            input_["vpc_ids"] = vpc_ids
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def revoke_snapshot_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        snapshot_identifier: Optional["capo_redshift.types.string.String"] = None,
        snapshot_arn: Optional["capo_redshift.types.string.String"] = None,
        snapshot_cluster_identifier: Optional[
            "capo_redshift.types.string.String"
        ] = None,
        account_with_restore_access: Optional[
            "capo_redshift.types.string.String"
        ] = None,
    ) -> "capo_redshift.types.revoke_snapshot_access_result.RevokeSnapshotAccessResult":
        """<p>Removes the ability of the specified Amazon Web Services account to restore the specified snapshot. If the account is currently restoring the snapshot, the restore will run to completion.</p> <p> For more information about working with snapshots, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html">Amazon Redshift Snapshots</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>

        Args:
            snapshot_identifier: <p>The identifier of the snapshot that the account can no longer access.</p>
            snapshot_arn: <p>The Amazon Resource Name (ARN) of the snapshot associated with the message to revoke access.</p>
            snapshot_cluster_identifier: <p>The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.</p>
            account_with_restore_access: <p>The identifier of the Amazon Web Services account that can no longer restore the specified snapshot.</p>

        Raises:
            capo_redshift.errors.access_to_snapshot_denied_fault.AccessToSnapshotDeniedFault: <p>The owner of the specified snapshot has not authorized your account to access the snapshot.</p>
            capo_redshift.errors.authorization_not_found_fault.AuthorizationNotFoundFault: <p>The specified CIDR IP range or EC2 security group is not authorized for the specified cluster security group.</p>
            capo_redshift.errors.cluster_snapshot_not_found_fault.ClusterSnapshotNotFoundFault: <p>The snapshot identifier does not refer to an existing cluster snapshot.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.revoke_snapshot_access_message.RevokeSnapshotAccessMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.revoke_snapshot_access_result.RevokeSnapshotAccessResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.revoke_snapshot_access

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.revoke_snapshot_access.async_revoke_snapshot_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.revoke_snapshot_access_message.RevokeSnapshotAccessMessage = {}
        if snapshot_identifier is not None:
            input_["snapshot_identifier"] = snapshot_identifier
        if snapshot_arn is not None:
            input_["snapshot_arn"] = snapshot_arn
        if snapshot_cluster_identifier is not None:
            input_["snapshot_cluster_identifier"] = snapshot_cluster_identifier
        if account_with_restore_access is not None:
            input_["account_with_restore_access"] = account_with_restore_access

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def rotate_encryption_key(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        cluster_identifier: Optional["capo_redshift.types.string.String"] = None,
    ) -> "capo_redshift.types.rotate_encryption_key_result.RotateEncryptionKeyResult":
        """<p>Rotates the encryption keys for a cluster.</p>

        Args:
            cluster_identifier: <p>The unique identifier of the cluster that you want to rotate the encryption keys for.</p> <p>Constraints: Must be the name of valid cluster that has encryption enabled.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.dependent_service_request_throttling_fault.DependentServiceRequestThrottlingFault: <p>The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.</p>
            capo_redshift.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The specified cluster is not in the <code>available</code> state. </p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.rotate_encryption_key_message.RotateEncryptionKeyMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.rotate_encryption_key_result.RotateEncryptionKeyResult"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.rotate_encryption_key

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.rotate_encryption_key.async_rotate_encryption_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.rotate_encryption_key_message.RotateEncryptionKeyMessage = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_partner_status(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftClientConfig] = None,
        account_id: Optional[
            "capo_redshift.types.partner_integration_account_id.PartnerIntegrationAccountId"
        ] = None,
        cluster_identifier: Optional[
            "capo_redshift.types.partner_integration_cluster_identifier.PartnerIntegrationClusterIdentifier"
        ] = None,
        database_name: Optional[
            "capo_redshift.types.partner_integration_database_name.PartnerIntegrationDatabaseName"
        ] = None,
        partner_name: Optional[
            "capo_redshift.types.partner_integration_partner_name.PartnerIntegrationPartnerName"
        ] = None,
        status: Optional[
            "capo_redshift.types.partner_integration_status.PartnerIntegrationStatus"
        ] = None,
        status_message: Optional[
            "capo_redshift.types.partner_integration_status_message.PartnerIntegrationStatusMessage"
        ] = None,
    ) -> "capo_redshift.types.partner_integration_output_message.PartnerIntegrationOutputMessage":
        """<p>Updates the status of a partner integration.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID that owns the cluster.</p>
            cluster_identifier: <p>The cluster identifier of the cluster whose partner integration status is being updated.</p>
            database_name: <p>The name of the database whose partner integration status is being updated.</p>
            partner_name: <p>The name of the partner whose integration status is being updated.</p>
            status: <p>The value of the updated status.</p>
            status_message: <p>The status message provided by the partner.</p>

        Raises:
            capo_redshift.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The <code>ClusterIdentifier</code> parameter does not refer to an existing cluster. </p>
            capo_redshift.errors.partner_not_found_fault.PartnerNotFoundFault: <p>The name of the partner was not found.</p>
            capo_redshift.errors.unauthorized_partner_integration_fault.UnauthorizedPartnerIntegrationFault: <p>The partner integration is not authorized.</p>
            capo_redshift.errors.unsupported_operation_fault.UnsupportedOperationFault: <p>The requested operation isn't supported.</p>
            capo_redshift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift.types.update_partner_status_input_message.UpdatePartnerStatusInputMessage]",
        ) -> AsyncOperationResponse[
            "capo_redshift.types.partner_integration_output_message.PartnerIntegrationOutputMessage"
        ]:
            import capo_redshift._operations.redshift_service_version20121201.update_partner_status

            (
                output,
                http_response,
            ) = await capo_redshift._operations.redshift_service_version20121201.update_partner_status.async_update_partner_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift.types.update_partner_status_input_message.UpdatePartnerStatusInputMessage = {}
        if account_id is not None:
            input_["account_id"] = account_id
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if database_name is not None:
            input_["database_name"] = database_name
        if partner_name is not None:
            input_["partner_name"] = partner_name
        if status is not None:
            input_["status"] = status
        if status_message is not None:
            input_["status_message"] = status_message

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
