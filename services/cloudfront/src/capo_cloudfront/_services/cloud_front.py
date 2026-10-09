"""Generated from Smithy shape ``com.amazonaws.cloudfront#Cloudfront2020_05_31``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_cloudfront._auth._signers
import capo_cloudfront._auth._sigv4
from capo_cloudfront._auth._identity import Credentials
from capo_cloudfront._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cloudfront._auth._zapros_handler import AuthMiddleware
from capo_cloudfront._pagination import resolve_path as _resolve_path
from capo_cloudfront._services._aws_config import aws_config
from capo_cloudfront._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_cloudfront.types.alias_string
    import capo_cloudfront.types.anycast_ip_list_name
    import capo_cloudfront.types.associate_alias_request
    import capo_cloudfront.types.associate_distribution_tenant_web_acl_request
    import capo_cloudfront.types.associate_distribution_tenant_web_acl_result
    import capo_cloudfront.types.associate_distribution_web_acl_request
    import capo_cloudfront.types.associate_distribution_web_acl_result
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.ca_certificates_bundle_source
    import capo_cloudfront.types.cache_policy_config
    import capo_cloudfront.types.cache_policy_type
    import capo_cloudfront.types.cloud_front_origin_access_identity_config
    import capo_cloudfront.types.cloud_front_origin_access_identity_summary
    import capo_cloudfront.types.connection_function_summary
    import capo_cloudfront.types.connection_group_association_filter
    import capo_cloudfront.types.connection_group_summary
    import capo_cloudfront.types.connection_mode
    import capo_cloudfront.types.continuous_deployment_policy_config
    import capo_cloudfront.types.copy_distribution_request
    import capo_cloudfront.types.copy_distribution_result
    import capo_cloudfront.types.create_anycast_ip_list_request
    import capo_cloudfront.types.create_anycast_ip_list_result
    import capo_cloudfront.types.create_cache_policy_request
    import capo_cloudfront.types.create_cache_policy_result
    import capo_cloudfront.types.create_cloud_front_origin_access_identity_request
    import capo_cloudfront.types.create_cloud_front_origin_access_identity_result
    import capo_cloudfront.types.create_connection_function_request
    import capo_cloudfront.types.create_connection_function_result
    import capo_cloudfront.types.create_connection_group_request
    import capo_cloudfront.types.create_connection_group_result
    import capo_cloudfront.types.create_continuous_deployment_policy_request
    import capo_cloudfront.types.create_continuous_deployment_policy_result
    import capo_cloudfront.types.create_distribution_request
    import capo_cloudfront.types.create_distribution_result
    import capo_cloudfront.types.create_distribution_tenant_request
    import capo_cloudfront.types.create_distribution_tenant_result
    import capo_cloudfront.types.create_distribution_with_tags_request
    import capo_cloudfront.types.create_distribution_with_tags_result
    import capo_cloudfront.types.create_field_level_encryption_config_request
    import capo_cloudfront.types.create_field_level_encryption_config_result
    import capo_cloudfront.types.create_field_level_encryption_profile_request
    import capo_cloudfront.types.create_field_level_encryption_profile_result
    import capo_cloudfront.types.create_function_request
    import capo_cloudfront.types.create_function_result
    import capo_cloudfront.types.create_invalidation_for_distribution_tenant_request
    import capo_cloudfront.types.create_invalidation_for_distribution_tenant_result
    import capo_cloudfront.types.create_invalidation_request
    import capo_cloudfront.types.create_invalidation_result
    import capo_cloudfront.types.create_key_group_request
    import capo_cloudfront.types.create_key_group_result
    import capo_cloudfront.types.create_key_value_store_request
    import capo_cloudfront.types.create_key_value_store_result
    import capo_cloudfront.types.create_monitoring_subscription_request
    import capo_cloudfront.types.create_monitoring_subscription_result
    import capo_cloudfront.types.create_origin_access_control_request
    import capo_cloudfront.types.create_origin_access_control_result
    import capo_cloudfront.types.create_origin_request_policy_request
    import capo_cloudfront.types.create_origin_request_policy_result
    import capo_cloudfront.types.create_public_key_request
    import capo_cloudfront.types.create_public_key_result
    import capo_cloudfront.types.create_realtime_log_config_request
    import capo_cloudfront.types.create_realtime_log_config_result
    import capo_cloudfront.types.create_response_headers_policy_request
    import capo_cloudfront.types.create_response_headers_policy_result
    import capo_cloudfront.types.create_streaming_distribution_request
    import capo_cloudfront.types.create_streaming_distribution_result
    import capo_cloudfront.types.create_streaming_distribution_with_tags_request
    import capo_cloudfront.types.create_streaming_distribution_with_tags_result
    import capo_cloudfront.types.create_trust_store_request
    import capo_cloudfront.types.create_trust_store_result
    import capo_cloudfront.types.create_vpc_origin_request
    import capo_cloudfront.types.create_vpc_origin_result
    import capo_cloudfront.types.customizations
    import capo_cloudfront.types.delete_anycast_ip_list_request
    import capo_cloudfront.types.delete_cache_policy_request
    import capo_cloudfront.types.delete_cloud_front_origin_access_identity_request
    import capo_cloudfront.types.delete_connection_function_request
    import capo_cloudfront.types.delete_connection_group_request
    import capo_cloudfront.types.delete_continuous_deployment_policy_request
    import capo_cloudfront.types.delete_distribution_request
    import capo_cloudfront.types.delete_distribution_tenant_request
    import capo_cloudfront.types.delete_field_level_encryption_config_request
    import capo_cloudfront.types.delete_field_level_encryption_profile_request
    import capo_cloudfront.types.delete_function_request
    import capo_cloudfront.types.delete_key_group_request
    import capo_cloudfront.types.delete_key_value_store_request
    import capo_cloudfront.types.delete_monitoring_subscription_request
    import capo_cloudfront.types.delete_monitoring_subscription_result
    import capo_cloudfront.types.delete_origin_access_control_request
    import capo_cloudfront.types.delete_origin_request_policy_request
    import capo_cloudfront.types.delete_public_key_request
    import capo_cloudfront.types.delete_realtime_log_config_request
    import capo_cloudfront.types.delete_resource_policy_request
    import capo_cloudfront.types.delete_response_headers_policy_request
    import capo_cloudfront.types.delete_streaming_distribution_request
    import capo_cloudfront.types.delete_trust_store_request
    import capo_cloudfront.types.delete_vpc_origin_request
    import capo_cloudfront.types.delete_vpc_origin_result
    import capo_cloudfront.types.describe_connection_function_request
    import capo_cloudfront.types.describe_connection_function_result
    import capo_cloudfront.types.describe_function_request
    import capo_cloudfront.types.describe_function_result
    import capo_cloudfront.types.describe_key_value_store_request
    import capo_cloudfront.types.describe_key_value_store_result
    import capo_cloudfront.types.disassociate_distribution_tenant_web_acl_request
    import capo_cloudfront.types.disassociate_distribution_tenant_web_acl_result
    import capo_cloudfront.types.disassociate_distribution_web_acl_request
    import capo_cloudfront.types.disassociate_distribution_web_acl_result
    import capo_cloudfront.types.distribution_config
    import capo_cloudfront.types.distribution_config_with_tags
    import capo_cloudfront.types.distribution_id_string
    import capo_cloudfront.types.distribution_resource_id
    import capo_cloudfront.types.distribution_summary
    import capo_cloudfront.types.distribution_tenant_association_filter
    import capo_cloudfront.types.distribution_tenant_summary
    import capo_cloudfront.types.domain_conflict
    import capo_cloudfront.types.domain_list
    import capo_cloudfront.types.end_point_list
    import capo_cloudfront.types.field_level_encryption_config
    import capo_cloudfront.types.field_level_encryption_profile_config
    import capo_cloudfront.types.field_list
    import capo_cloudfront.types.function_blob
    import capo_cloudfront.types.function_config
    import capo_cloudfront.types.function_event_object
    import capo_cloudfront.types.function_name
    import capo_cloudfront.types.function_stage
    import capo_cloudfront.types.get_anycast_ip_list_request
    import capo_cloudfront.types.get_anycast_ip_list_result
    import capo_cloudfront.types.get_cache_policy_config_request
    import capo_cloudfront.types.get_cache_policy_config_result
    import capo_cloudfront.types.get_cache_policy_request
    import capo_cloudfront.types.get_cache_policy_result
    import capo_cloudfront.types.get_cloud_front_origin_access_identity_config_request
    import capo_cloudfront.types.get_cloud_front_origin_access_identity_config_result
    import capo_cloudfront.types.get_cloud_front_origin_access_identity_request
    import capo_cloudfront.types.get_cloud_front_origin_access_identity_result
    import capo_cloudfront.types.get_connection_function_request
    import capo_cloudfront.types.get_connection_function_result
    import capo_cloudfront.types.get_connection_group_by_routing_endpoint_request
    import capo_cloudfront.types.get_connection_group_by_routing_endpoint_result
    import capo_cloudfront.types.get_connection_group_request
    import capo_cloudfront.types.get_connection_group_result
    import capo_cloudfront.types.get_continuous_deployment_policy_config_request
    import capo_cloudfront.types.get_continuous_deployment_policy_config_result
    import capo_cloudfront.types.get_continuous_deployment_policy_request
    import capo_cloudfront.types.get_continuous_deployment_policy_result
    import capo_cloudfront.types.get_distribution_config_request
    import capo_cloudfront.types.get_distribution_config_result
    import capo_cloudfront.types.get_distribution_request
    import capo_cloudfront.types.get_distribution_result
    import capo_cloudfront.types.get_distribution_tenant_by_domain_request
    import capo_cloudfront.types.get_distribution_tenant_by_domain_result
    import capo_cloudfront.types.get_distribution_tenant_request
    import capo_cloudfront.types.get_distribution_tenant_result
    import capo_cloudfront.types.get_field_level_encryption_config_request
    import capo_cloudfront.types.get_field_level_encryption_config_result
    import capo_cloudfront.types.get_field_level_encryption_profile_config_request
    import capo_cloudfront.types.get_field_level_encryption_profile_config_result
    import capo_cloudfront.types.get_field_level_encryption_profile_request
    import capo_cloudfront.types.get_field_level_encryption_profile_result
    import capo_cloudfront.types.get_field_level_encryption_request
    import capo_cloudfront.types.get_field_level_encryption_result
    import capo_cloudfront.types.get_function_request
    import capo_cloudfront.types.get_function_result
    import capo_cloudfront.types.get_invalidation_for_distribution_tenant_request
    import capo_cloudfront.types.get_invalidation_for_distribution_tenant_result
    import capo_cloudfront.types.get_invalidation_request
    import capo_cloudfront.types.get_invalidation_result
    import capo_cloudfront.types.get_key_group_config_request
    import capo_cloudfront.types.get_key_group_config_result
    import capo_cloudfront.types.get_key_group_request
    import capo_cloudfront.types.get_key_group_result
    import capo_cloudfront.types.get_managed_certificate_details_request
    import capo_cloudfront.types.get_managed_certificate_details_result
    import capo_cloudfront.types.get_monitoring_subscription_request
    import capo_cloudfront.types.get_monitoring_subscription_result
    import capo_cloudfront.types.get_origin_access_control_config_request
    import capo_cloudfront.types.get_origin_access_control_config_result
    import capo_cloudfront.types.get_origin_access_control_request
    import capo_cloudfront.types.get_origin_access_control_result
    import capo_cloudfront.types.get_origin_request_policy_config_request
    import capo_cloudfront.types.get_origin_request_policy_config_result
    import capo_cloudfront.types.get_origin_request_policy_request
    import capo_cloudfront.types.get_origin_request_policy_result
    import capo_cloudfront.types.get_public_key_config_request
    import capo_cloudfront.types.get_public_key_config_result
    import capo_cloudfront.types.get_public_key_request
    import capo_cloudfront.types.get_public_key_result
    import capo_cloudfront.types.get_realtime_log_config_request
    import capo_cloudfront.types.get_realtime_log_config_result
    import capo_cloudfront.types.get_resource_policy_request
    import capo_cloudfront.types.get_resource_policy_result
    import capo_cloudfront.types.get_response_headers_policy_config_request
    import capo_cloudfront.types.get_response_headers_policy_config_result
    import capo_cloudfront.types.get_response_headers_policy_request
    import capo_cloudfront.types.get_response_headers_policy_result
    import capo_cloudfront.types.get_streaming_distribution_config_request
    import capo_cloudfront.types.get_streaming_distribution_config_result
    import capo_cloudfront.types.get_streaming_distribution_request
    import capo_cloudfront.types.get_streaming_distribution_result
    import capo_cloudfront.types.get_trust_store_request
    import capo_cloudfront.types.get_trust_store_result
    import capo_cloudfront.types.get_vpc_origin_request
    import capo_cloudfront.types.get_vpc_origin_result
    import capo_cloudfront.types.import_source
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.invalidation_batch
    import capo_cloudfront.types.invalidation_summary
    import capo_cloudfront.types.ip_address_type
    import capo_cloudfront.types.ipam_cidr_config_list
    import capo_cloudfront.types.key_group_config
    import capo_cloudfront.types.key_value_store
    import capo_cloudfront.types.key_value_store_comment
    import capo_cloudfront.types.key_value_store_name
    import capo_cloudfront.types.list_anycast_ip_lists_request
    import capo_cloudfront.types.list_anycast_ip_lists_result
    import capo_cloudfront.types.list_cache_policies_request
    import capo_cloudfront.types.list_cache_policies_result
    import capo_cloudfront.types.list_cloud_front_origin_access_identities_request
    import capo_cloudfront.types.list_cloud_front_origin_access_identities_result
    import capo_cloudfront.types.list_conflicting_aliases_max_items_integer
    import capo_cloudfront.types.list_conflicting_aliases_request
    import capo_cloudfront.types.list_conflicting_aliases_result
    import capo_cloudfront.types.list_connection_functions_request
    import capo_cloudfront.types.list_connection_functions_result
    import capo_cloudfront.types.list_connection_groups_request
    import capo_cloudfront.types.list_connection_groups_result
    import capo_cloudfront.types.list_continuous_deployment_policies_request
    import capo_cloudfront.types.list_continuous_deployment_policies_result
    import capo_cloudfront.types.list_distribution_tenants_by_customization_request
    import capo_cloudfront.types.list_distribution_tenants_by_customization_result
    import capo_cloudfront.types.list_distribution_tenants_request
    import capo_cloudfront.types.list_distribution_tenants_result
    import capo_cloudfront.types.list_distributions_by_anycast_ip_list_id_request
    import capo_cloudfront.types.list_distributions_by_anycast_ip_list_id_result
    import capo_cloudfront.types.list_distributions_by_cache_policy_id_request
    import capo_cloudfront.types.list_distributions_by_cache_policy_id_result
    import capo_cloudfront.types.list_distributions_by_connection_function_request
    import capo_cloudfront.types.list_distributions_by_connection_function_result
    import capo_cloudfront.types.list_distributions_by_connection_mode_request
    import capo_cloudfront.types.list_distributions_by_connection_mode_result
    import capo_cloudfront.types.list_distributions_by_key_group_request
    import capo_cloudfront.types.list_distributions_by_key_group_result
    import capo_cloudfront.types.list_distributions_by_origin_request_policy_id_request
    import capo_cloudfront.types.list_distributions_by_origin_request_policy_id_result
    import capo_cloudfront.types.list_distributions_by_owned_resource_request
    import capo_cloudfront.types.list_distributions_by_owned_resource_result
    import capo_cloudfront.types.list_distributions_by_realtime_log_config_request
    import capo_cloudfront.types.list_distributions_by_realtime_log_config_result
    import capo_cloudfront.types.list_distributions_by_response_headers_policy_id_request
    import capo_cloudfront.types.list_distributions_by_response_headers_policy_id_result
    import capo_cloudfront.types.list_distributions_by_trust_store_request
    import capo_cloudfront.types.list_distributions_by_trust_store_result
    import capo_cloudfront.types.list_distributions_by_vpc_origin_id_request
    import capo_cloudfront.types.list_distributions_by_vpc_origin_id_result
    import capo_cloudfront.types.list_distributions_by_web_acl_id_request
    import capo_cloudfront.types.list_distributions_by_web_acl_id_result
    import capo_cloudfront.types.list_distributions_request
    import capo_cloudfront.types.list_distributions_result
    import capo_cloudfront.types.list_domain_conflicts_request
    import capo_cloudfront.types.list_domain_conflicts_result
    import capo_cloudfront.types.list_field_level_encryption_configs_request
    import capo_cloudfront.types.list_field_level_encryption_configs_result
    import capo_cloudfront.types.list_field_level_encryption_profiles_request
    import capo_cloudfront.types.list_field_level_encryption_profiles_result
    import capo_cloudfront.types.list_functions_request
    import capo_cloudfront.types.list_functions_result
    import capo_cloudfront.types.list_invalidations_for_distribution_tenant_request
    import capo_cloudfront.types.list_invalidations_for_distribution_tenant_result
    import capo_cloudfront.types.list_invalidations_request
    import capo_cloudfront.types.list_invalidations_result
    import capo_cloudfront.types.list_key_groups_request
    import capo_cloudfront.types.list_key_groups_result
    import capo_cloudfront.types.list_key_value_stores_request
    import capo_cloudfront.types.list_key_value_stores_result
    import capo_cloudfront.types.list_origin_access_controls_request
    import capo_cloudfront.types.list_origin_access_controls_result
    import capo_cloudfront.types.list_origin_request_policies_request
    import capo_cloudfront.types.list_origin_request_policies_result
    import capo_cloudfront.types.list_public_keys_request
    import capo_cloudfront.types.list_public_keys_result
    import capo_cloudfront.types.list_realtime_log_configs_request
    import capo_cloudfront.types.list_realtime_log_configs_result
    import capo_cloudfront.types.list_response_headers_policies_request
    import capo_cloudfront.types.list_response_headers_policies_result
    import capo_cloudfront.types.list_streaming_distributions_request
    import capo_cloudfront.types.list_streaming_distributions_result
    import capo_cloudfront.types.list_tags_for_resource_request
    import capo_cloudfront.types.list_tags_for_resource_result
    import capo_cloudfront.types.list_trust_stores_request
    import capo_cloudfront.types.list_trust_stores_result
    import capo_cloudfront.types.list_vpc_origins_request
    import capo_cloudfront.types.list_vpc_origins_result
    import capo_cloudfront.types.long
    import capo_cloudfront.types.managed_certificate_request
    import capo_cloudfront.types.monitoring_subscription
    import capo_cloudfront.types.origin_access_control_config
    import capo_cloudfront.types.origin_access_control_summary
    import capo_cloudfront.types.origin_request_policy_config
    import capo_cloudfront.types.origin_request_policy_type
    import capo_cloudfront.types.parameters
    import capo_cloudfront.types.public_key_config
    import capo_cloudfront.types.public_key_summary
    import capo_cloudfront.types.publish_connection_function_request
    import capo_cloudfront.types.publish_connection_function_result
    import capo_cloudfront.types.publish_function_request
    import capo_cloudfront.types.publish_function_result
    import capo_cloudfront.types.put_resource_policy_request
    import capo_cloudfront.types.put_resource_policy_result
    import capo_cloudfront.types.resource_arn
    import capo_cloudfront.types.resource_id
    import capo_cloudfront.types.response_headers_policy_config
    import capo_cloudfront.types.response_headers_policy_type
    import capo_cloudfront.types.streaming_distribution_config
    import capo_cloudfront.types.streaming_distribution_config_with_tags
    import capo_cloudfront.types.streaming_distribution_summary
    import capo_cloudfront.types.string
    import capo_cloudfront.types.tag_keys
    import capo_cloudfront.types.tag_resource_request
    import capo_cloudfront.types.tags
    import capo_cloudfront.types.test_connection_function_request
    import capo_cloudfront.types.test_connection_function_result
    import capo_cloudfront.types.test_function_request
    import capo_cloudfront.types.test_function_result
    import capo_cloudfront.types.trust_store_summary
    import capo_cloudfront.types.untag_resource_request
    import capo_cloudfront.types.update_anycast_ip_list_request
    import capo_cloudfront.types.update_anycast_ip_list_result
    import capo_cloudfront.types.update_cache_policy_request
    import capo_cloudfront.types.update_cache_policy_result
    import capo_cloudfront.types.update_cloud_front_origin_access_identity_request
    import capo_cloudfront.types.update_cloud_front_origin_access_identity_result
    import capo_cloudfront.types.update_connection_function_request
    import capo_cloudfront.types.update_connection_function_result
    import capo_cloudfront.types.update_connection_group_request
    import capo_cloudfront.types.update_connection_group_result
    import capo_cloudfront.types.update_continuous_deployment_policy_request
    import capo_cloudfront.types.update_continuous_deployment_policy_result
    import capo_cloudfront.types.update_distribution_request
    import capo_cloudfront.types.update_distribution_result
    import capo_cloudfront.types.update_distribution_tenant_request
    import capo_cloudfront.types.update_distribution_tenant_result
    import capo_cloudfront.types.update_distribution_with_staging_config_request
    import capo_cloudfront.types.update_distribution_with_staging_config_result
    import capo_cloudfront.types.update_domain_association_request
    import capo_cloudfront.types.update_domain_association_result
    import capo_cloudfront.types.update_field_level_encryption_config_request
    import capo_cloudfront.types.update_field_level_encryption_config_result
    import capo_cloudfront.types.update_field_level_encryption_profile_request
    import capo_cloudfront.types.update_field_level_encryption_profile_result
    import capo_cloudfront.types.update_function_request
    import capo_cloudfront.types.update_function_result
    import capo_cloudfront.types.update_key_group_request
    import capo_cloudfront.types.update_key_group_result
    import capo_cloudfront.types.update_key_value_store_request
    import capo_cloudfront.types.update_key_value_store_result
    import capo_cloudfront.types.update_origin_access_control_request
    import capo_cloudfront.types.update_origin_access_control_result
    import capo_cloudfront.types.update_origin_request_policy_request
    import capo_cloudfront.types.update_origin_request_policy_result
    import capo_cloudfront.types.update_public_key_request
    import capo_cloudfront.types.update_public_key_result
    import capo_cloudfront.types.update_realtime_log_config_request
    import capo_cloudfront.types.update_realtime_log_config_result
    import capo_cloudfront.types.update_response_headers_policy_request
    import capo_cloudfront.types.update_response_headers_policy_result
    import capo_cloudfront.types.update_streaming_distribution_request
    import capo_cloudfront.types.update_streaming_distribution_result
    import capo_cloudfront.types.update_trust_store_request
    import capo_cloudfront.types.update_trust_store_result
    import capo_cloudfront.types.update_vpc_origin_request
    import capo_cloudfront.types.update_vpc_origin_result
    import capo_cloudfront.types.verify_dns_configuration_request
    import capo_cloudfront.types.verify_dns_configuration_result
    import capo_cloudfront.types.vpc_origin_endpoint_config


class CloudFrontClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class CloudFrontClient:
    """A client for the ``CloudFront`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = CloudFrontClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[CloudFrontClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CloudFrontClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def associate_alias(
        self,
        target_distribution_id: "capo_cloudfront.types.string.string",
        alias: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<note> <p>The <code>AssociateAlias</code> API operation only supports standard distributions. To move domains between distribution tenants and/or standard distributions, we recommend that you use the <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDomainAssociation.html">UpdateDomainAssociation</a> API operation instead.</p> </note> <p>Associates an alias with a CloudFront standard distribution. An alias is commonly known as a custom domain or vanity domain. It can also be called a CNAME or alternate domain name.</p> <p>With this operation, you can move an alias that's already used for a standard distribution to a different standard distribution. This prevents the downtime that could occur if you first remove the alias from one standard distribution and then separately add the alias to another standard distribution.</p> <p>To use this operation, specify the alias and the ID of the target standard distribution.</p> <p>For more information, including how to set up the target standard distribution, prerequisites that you must complete, and other restrictions, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move">Moving an alternate domain name to a different standard distribution or distribution tenant</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            target_distribution_id: <p>The ID of the standard distribution that you're associating the alias with.</p>
            alias: <p>The alias (also known as a CNAME) to add to the target standard distribution.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.too_many_distribution_cnam_es.TooManyDistributionCNAMEs: <p>Your request contains more CNAMEs than are allowed per distribution.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.associate_alias_request.AssociateAliasRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.associate_alias

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.associate_alias.associate_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.associate_alias_request.AssociateAliasRequest = {
            "target_distribution_id": target_distribution_id,
            "alias": alias,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_distribution_tenant_web_acl(
        self,
        id: "capo_cloudfront.types.string.string",
        web_acl_arn: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.associate_distribution_tenant_web_acl_result.AssociateDistributionTenantWebACLResult":
        """<p>Associates the WAF web ACL with a distribution tenant.</p>

        Args:
            id: <p>The ID of the distribution tenant.</p>
            web_acl_arn: <p>The Amazon Resource Name (ARN) of the WAF web ACL to associate.</p>
            if_match: <p>The current <code>ETag</code> of the distribution tenant. This value is returned in the response of the <code>GetDistributionTenant</code> API operation.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.associate_distribution_tenant_web_acl_request.AssociateDistributionTenantWebACLRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.associate_distribution_tenant_web_acl_result.AssociateDistributionTenantWebACLResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.associate_distribution_tenant_web_acl

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.associate_distribution_tenant_web_acl.associate_distribution_tenant_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.associate_distribution_tenant_web_acl_request.AssociateDistributionTenantWebACLRequest = {
            "id": id,
            "web_acl_arn": web_acl_arn,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_distribution_web_acl(
        self,
        id: "capo_cloudfront.types.string.string",
        web_acl_arn: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.associate_distribution_web_acl_result.AssociateDistributionWebACLResult":
        """<p>Associates the WAF web ACL with a distribution.</p>

        Args:
            id: <p>The ID of the distribution.</p>
            web_acl_arn: <p>The Amazon Resource Name (ARN) of the WAF web ACL to associate.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the distribution that you're associating with the WAF web ACL.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.associate_distribution_web_acl_request.AssociateDistributionWebACLRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.associate_distribution_web_acl_result.AssociateDistributionWebACLResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.associate_distribution_web_acl

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.associate_distribution_web_acl.associate_distribution_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.associate_distribution_web_acl_request.AssociateDistributionWebACLRequest = {
            "id": id,
            "web_acl_arn": web_acl_arn,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def copy_distribution(
        self,
        primary_distribution_id: "capo_cloudfront.types.string.string",
        caller_reference: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        staging: Optional["capo_cloudfront.types.boolean.boolean"] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
        enabled: Optional["capo_cloudfront.types.boolean.boolean"] = None,
    ) -> "capo_cloudfront.types.copy_distribution_result.CopyDistributionResult":
        """<p>Creates a staging distribution using the configuration of the provided primary distribution. A staging distribution is a copy of an existing distribution (called the primary distribution) that you can use in a continuous deployment workflow.</p> <p>After you create a staging distribution, you can use <code>UpdateDistribution</code> to modify the staging distribution's configuration. Then you can use <code>CreateContinuousDeploymentPolicy</code> to incrementally move traffic to the staging distribution.</p> <p>This API operation requires the following IAM permissions:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html">GetDistribution</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html">CreateDistribution</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CopyDistribution.html">CopyDistribution</a> </p> </li> </ul>

        Args:
            primary_distribution_id: <p>The identifier of the primary distribution whose configuration you are copying. To get a distribution ID, use <code>ListDistributions</code>.</p>
            staging: <p>The type of distribution that your primary distribution will be copied to. The only valid value is <code>True</code>, indicating that you are copying to a staging distribution.</p>
            if_match: <p>The version identifier of the primary distribution whose configuration you are copying. This is the <code>ETag</code> value returned in the response to <code>GetDistribution</code> and <code>GetDistributionConfig</code>.</p>
            caller_reference: <p>A value that uniquely identifies a request to create a resource. This helps to prevent CloudFront from creating a duplicate resource if you accidentally resubmit an identical request.</p>
            enabled: <p>A Boolean flag to specify the state of the staging distribution when it's created. When you set this value to <code>True</code>, the staging distribution is enabled. When you set this value to <code>False</code>, the staging distribution is disabled.</p> <p>If you omit this field, the default value is <code>True</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists: <p>The CNAME specified is already defined for CloudFront.</p>
            capo_cloudfront.errors.distribution_already_exists.DistributionAlreadyExists: <p>The caller reference you attempted to create the distribution with is associated with another distribution.</p>
            capo_cloudfront.errors.illegal_field_level_encryption_config_association_with_cache_behavior.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior: <p>The specified configuration for field-level encryption can't be associated with the specified cache behavior.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_default_root_object.InvalidDefaultRootObject: <p>The default root object file name is too big or contains an invalid character.</p>
            capo_cloudfront.errors.invalid_error_code.InvalidErrorCode: <p>An invalid error code was specified.</p>
            capo_cloudfront.errors.invalid_forward_cookies.InvalidForwardCookies: <p>Your request contains forward cookies option which doesn't match with the expectation for the <code>whitelisted</code> list of cookie names. Either list of cookie names has been specified when not allowed or list of cookie names is missing when expected.</p>
            capo_cloudfront.errors.invalid_function_association.InvalidFunctionAssociation: <p>A CloudFront function association is invalid.</p>
            capo_cloudfront.errors.invalid_geo_restriction_parameter.InvalidGeoRestrictionParameter: <p>The specified geo restriction parameter is not valid.</p>
            capo_cloudfront.errors.invalid_headers_for_s3_origin.InvalidHeadersForS3Origin: <p>The headers specified are not valid for an Amazon S3 origin.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.invalid_lambda_function_association.InvalidLambdaFunctionAssociation: <p>The specified Lambda@Edge function association is invalid.</p>
            capo_cloudfront.errors.invalid_location_code.InvalidLocationCode: <p>The location code specified is not valid.</p>
            capo_cloudfront.errors.invalid_minimum_protocol_version.InvalidMinimumProtocolVersion: <p>The minimum protocol version specified is not valid.</p>
            capo_cloudfront.errors.invalid_origin.InvalidOrigin: <p>The Amazon S3 origin server specified does not refer to a valid Amazon S3 bucket.</p>
            capo_cloudfront.errors.invalid_origin_access_control.InvalidOriginAccessControl: <p>The origin access control is not valid.</p>
            capo_cloudfront.errors.invalid_origin_access_identity.InvalidOriginAccessIdentity: <p>The origin access identity is not valid or doesn't exist.</p>
            capo_cloudfront.errors.invalid_origin_keepalive_timeout.InvalidOriginKeepaliveTimeout: <p>The keep alive timeout specified for the origin is not valid.</p>
            capo_cloudfront.errors.invalid_origin_read_timeout.InvalidOriginReadTimeout: <p>The read timeout specified for the origin is not valid.</p>
            capo_cloudfront.errors.invalid_protocol_settings.InvalidProtocolSettings: <p>You cannot specify SSLv3 as the minimum protocol version if you only want to support only clients that support Server Name Indication (SNI).</p>
            capo_cloudfront.errors.invalid_query_string_parameters.InvalidQueryStringParameters: <p>The query string parameters specified are not valid.</p>
            capo_cloudfront.errors.invalid_relative_path.InvalidRelativePath: <p>The relative path is too big, is not URL-encoded, or does not begin with a slash (/).</p>
            capo_cloudfront.errors.invalid_required_protocol.InvalidRequiredProtocol: <p>This operation requires the HTTPS protocol. Ensure that you specify the HTTPS protocol in your request, or omit the <code>RequiredProtocols</code> element from your distribution configuration.</p>
            capo_cloudfront.errors.invalid_response_code.InvalidResponseCode: <p>A response code is not valid.</p>
            capo_cloudfront.errors.invalid_ttl_order.InvalidTTLOrder: <p>The TTL order specified is not valid.</p>
            capo_cloudfront.errors.invalid_viewer_certificate.InvalidViewerCertificate: <p>A viewer certificate specified is not valid.</p>
            capo_cloudfront.errors.invalid_web_acl_id.InvalidWebACLId: <p>A web ACL ID specified is not valid. To specify a web ACL created using the latest version of WAF, use the ACL ARN, for example <code>arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a</code>. To specify a web ACL created using WAF Classic, use the ACL ID, for example <code>473e64fd-f30b-4765-81a0-62ad96dd167a</code>.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy: <p>The cache policy does not exist.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig: <p>The specified configuration for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.no_such_origin.NoSuchOrigin: <p>No origin exists with the specified <code>Origin Id</code>.</p>
            capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy: <p>The origin request policy does not exist.</p>
            capo_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig: <p>The real-time log configuration does not exist.</p>
            capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy: <p>The response headers policy does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.realtime_log_config_owner_mismatch.RealtimeLogConfigOwnerMismatch: <p>The specified real-time log configuration belongs to a different Amazon Web Services account.</p>
            capo_cloudfront.errors.too_many_cache_behaviors.TooManyCacheBehaviors: <p>You cannot create more cache behaviors for the distribution.</p>
            capo_cloudfront.errors.too_many_certificates.TooManyCertificates: <p>You cannot create anymore custom SSL/TLS certificates.</p>
            capo_cloudfront.errors.too_many_cookie_names_in_white_list.TooManyCookieNamesInWhiteList: <p>Your request contains more cookie names in the whitelist than are allowed per cache behavior.</p>
            capo_cloudfront.errors.too_many_distribution_cnam_es.TooManyDistributionCNAMEs: <p>Your request contains more CNAMEs than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_distributions.TooManyDistributions: <p>Processing your request would cause you to exceed the maximum number of distributions allowed.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_cache_policy.TooManyDistributionsAssociatedToCachePolicy: <p>The maximum number of distributions have been associated with the specified cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_field_level_encryption_config.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig: <p>The maximum number of distributions have been associated with the specified configuration for field-level encryption.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_key_group.TooManyDistributionsAssociatedToKeyGroup: <p>The number of distributions that reference this key group is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_origin_access_control.TooManyDistributionsAssociatedToOriginAccessControl: <p>The maximum number of distributions have been associated with the specified origin access control.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_origin_request_policy.TooManyDistributionsAssociatedToOriginRequestPolicy: <p>The maximum number of distributions have been associated with the specified origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_response_headers_policy.TooManyDistributionsAssociatedToResponseHeadersPolicy: <p>The maximum number of distributions have been associated with the specified response headers policy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_with_function_associations.TooManyDistributionsWithFunctionAssociations: <p>You have reached the maximum number of distributions that are associated with a CloudFront function. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_with_lambda_associations.TooManyDistributionsWithLambdaAssociations: <p>Processing your request would cause the maximum number of distributions with Lambda@Edge function associations per owner to be exceeded.</p>
            capo_cloudfront.errors.too_many_distributions_with_single_function_arn.TooManyDistributionsWithSingleFunctionARN: <p>The maximum number of distributions have been associated with the specified Lambda@Edge function.</p>
            capo_cloudfront.errors.too_many_function_associations.TooManyFunctionAssociations: <p>You have reached the maximum number of CloudFront function associations for this distribution. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_headers_in_forwarded_values.TooManyHeadersInForwardedValues: <p>Your request contains too many headers in forwarded values.</p>
            capo_cloudfront.errors.too_many_key_groups_associated_to_distribution.TooManyKeyGroupsAssociatedToDistribution: <p>The number of key groups referenced by this distribution is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_lambda_function_associations.TooManyLambdaFunctionAssociations: <p>Your request contains more Lambda@Edge function associations than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_origin_custom_headers.TooManyOriginCustomHeaders: <p>Your request contains too many origin custom headers.</p>
            capo_cloudfront.errors.too_many_origin_groups_per_distribution.TooManyOriginGroupsPerDistribution: <p>Processing your request would cause you to exceed the maximum number of origin groups allowed.</p>
            capo_cloudfront.errors.too_many_origins.TooManyOrigins: <p>You cannot create more origins for the distribution.</p>
            capo_cloudfront.errors.too_many_query_string_parameters.TooManyQueryStringParameters: <p>Your request contains too many query string parameters.</p>
            capo_cloudfront.errors.too_many_trusted_signers.TooManyTrustedSigners: <p>Your request contains more trusted signers than are allowed per distribution.</p>
            capo_cloudfront.errors.trusted_key_group_does_not_exist.TrustedKeyGroupDoesNotExist: <p>The specified key group does not exist.</p>
            capo_cloudfront.errors.trusted_signer_does_not_exist.TrustedSignerDoesNotExist: <p>One or more of your trusted signers don't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.copy_distribution_request.CopyDistributionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.copy_distribution_result.CopyDistributionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.copy_distribution

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.copy_distribution.copy_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.copy_distribution_request.CopyDistributionRequest = {
            "primary_distribution_id": primary_distribution_id,
            "caller_reference": caller_reference,
        }
        if staging is not None:
            input_["staging"] = staging
        if if_match is not None:
            input_["if_match"] = if_match
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_anycast_ip_list(
        self,
        name: "capo_cloudfront.types.anycast_ip_list_name.AnycastIpListName",
        ip_count: "capo_cloudfront.types.integer.integer",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        tags: Optional["capo_cloudfront.types.tags.Tags"] = None,
        ip_address_type: Optional[
            "capo_cloudfront.types.ip_address_type.IpAddressType"
        ] = None,
        ipam_cidr_configs: Optional[
            "capo_cloudfront.types.ipam_cidr_config_list.IpamCidrConfigList"
        ] = None,
    ) -> (
        "capo_cloudfront.types.create_anycast_ip_list_result.CreateAnycastIpListResult"
    ):
        """<p>Creates an Anycast static IP list.</p>

        Args:
            name: <p>Name of the Anycast static IP list.</p>
            ip_count: <p>The number of static IP addresses that are allocated to the Anycast static IP list. Valid values: 21 or 3.</p>
            ip_address_type: <p>The IP address type for the Anycast static IP list. You can specify one of the following options:</p> <ul> <li> <p> <code>ipv4</code> only</p> </li> <li> <p> <code>ipv6</code> only </p> </li> <li> <p> <code>dualstack</code> - Allocate a list of both IPv4 and IPv6 addresses</p> </li> </ul>
            ipam_cidr_configs: <p> A list of IPAM CIDR configurations that specify the IP address ranges and IPAM pool settings for creating the Anycast static IP list. </p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_already_exists.EntityAlreadyExists: <p>The entity already exists. You must provide a unique entity.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_tagging.InvalidTagging: <p>The tagging specified is not valid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_anycast_ip_list_request.CreateAnycastIpListRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_anycast_ip_list_result.CreateAnycastIpListResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_anycast_ip_list

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_anycast_ip_list.create_anycast_ip_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_anycast_ip_list_request.CreateAnycastIpListRequest = {
            "name": name,
            "ip_count": ip_count,
        }
        if tags is not None:
            input_["tags"] = tags
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if ipam_cidr_configs is not None:
            input_["ipam_cidr_configs"] = ipam_cidr_configs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cache_policy(
        self,
        cache_policy_config: "capo_cloudfront.types.cache_policy_config.CachePolicyConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_cache_policy_result.CreateCachePolicyResult":
        """<p>Creates a cache policy.</p> <p>After you create a cache policy, you can attach it to one or more cache behaviors. When it's attached to a cache behavior, the cache policy determines the following:</p> <ul> <li> <p>The values that CloudFront includes in the <i>cache key</i>. These values can include HTTP headers, cookies, and URL query strings. CloudFront uses the cache key to find an object in its cache that it can return to the viewer.</p> </li> <li> <p>The default, minimum, and maximum time to live (TTL) values that you want objects to stay in the CloudFront cache.</p> <important> <p>If your minimum TTL is greater than 0, CloudFront will cache content for at least the duration specified in the cache policy's minimum TTL, even if the <code>Cache-Control: no-cache</code>, <code>no-store</code>, or <code>private</code> directives are present in the origin headers.</p> </important> </li> </ul> <p>The headers, cookies, and query strings that are included in the cache key are also included in requests that CloudFront sends to the origin. CloudFront sends a request when it can't find an object in its cache that matches the request's cache key. If you want to send values to the origin but <i>not</i> include them in the cache key, use <code>OriginRequestPolicy</code>.</p> <p>For more information about cache policies, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html">Controlling the cache key</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            cache_policy_config: <p>A cache policy configuration.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cache_policy_already_exists.CachePolicyAlreadyExists: <p>A cache policy with this name already exists. You must provide a unique name. To modify an existing cache policy, use <code>UpdateCachePolicy</code>.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.too_many_cache_policies.TooManyCachePolicies: <p>You have reached the maximum number of cache policies for this Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_cookies_in_cache_policy.TooManyCookiesInCachePolicy: <p>The number of cookies in the cache policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_headers_in_cache_policy.TooManyHeadersInCachePolicy: <p>The number of headers in the cache policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_query_strings_in_cache_policy.TooManyQueryStringsInCachePolicy: <p>The number of query strings in the cache policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_cache_policy_request.CreateCachePolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_cache_policy_result.CreateCachePolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_cache_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_cache_policy.create_cache_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_cache_policy_request.CreateCachePolicyRequest = {
            "cache_policy_config": cache_policy_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cloud_front_origin_access_identity(
        self,
        cloud_front_origin_access_identity_config: "capo_cloudfront.types.cloud_front_origin_access_identity_config.CloudFrontOriginAccessIdentityConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_cloud_front_origin_access_identity_result.CreateCloudFrontOriginAccessIdentityResult":
        """<p>Creates a new origin access identity. If you're using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            cloud_front_origin_access_identity_config: <p>The current configuration information for the identity.</p>

        Raises:
            capo_cloudfront.errors.cloud_front_origin_access_identity_already_exists.CloudFrontOriginAccessIdentityAlreadyExists: <p>If the <code>CallerReference</code> is a value you already sent in a previous request to create an identity but the content of the <code>CloudFrontOriginAccessIdentityConfig</code> is different from the original request, CloudFront returns a <code>CloudFrontOriginAccessIdentityAlreadyExists</code> error. </p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.too_many_cloud_front_origin_access_identities.TooManyCloudFrontOriginAccessIdentities: <p>Processing your request would cause you to exceed the maximum number of origin access identities allowed.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_cloud_front_origin_access_identity_request.CreateCloudFrontOriginAccessIdentityRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_cloud_front_origin_access_identity_result.CreateCloudFrontOriginAccessIdentityResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_cloud_front_origin_access_identity

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_cloud_front_origin_access_identity.create_cloud_front_origin_access_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_cloud_front_origin_access_identity_request.CreateCloudFrontOriginAccessIdentityRequest = {
            "cloud_front_origin_access_identity_config": cloud_front_origin_access_identity_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_connection_function(
        self,
        name: "capo_cloudfront.types.function_name.FunctionName",
        connection_function_config: "capo_cloudfront.types.function_config.FunctionConfig",
        connection_function_code: "capo_cloudfront.types.function_blob.FunctionBlob",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        tags: Optional["capo_cloudfront.types.tags.Tags"] = None,
    ) -> "capo_cloudfront.types.create_connection_function_result.CreateConnectionFunctionResult":
        """<p>Creates a connection function.</p>

        Args:
            name: <p>A name for the connection function.</p>
            connection_function_code: <p>The code for the connection function.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_already_exists.EntityAlreadyExists: <p>The entity already exists. You must provide a unique entity.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_size_limit_exceeded.EntitySizeLimitExceeded: <p>The entity size limit was exceeded.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_tagging.InvalidTagging: <p>The tagging specified is not valid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_connection_function_request.CreateConnectionFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_connection_function_result.CreateConnectionFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_connection_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_connection_function.create_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_connection_function_request.CreateConnectionFunctionRequest = {
            "name": name,
            "connection_function_config": connection_function_config,
            "connection_function_code": connection_function_code,
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

    def create_connection_group(
        self,
        name: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        ipv6_enabled: Optional["capo_cloudfront.types.boolean.boolean"] = None,
        tags: Optional["capo_cloudfront.types.tags.Tags"] = None,
        anycast_ip_list_id: Optional["capo_cloudfront.types.string.string"] = None,
        enabled: Optional["capo_cloudfront.types.boolean.boolean"] = None,
    ) -> "capo_cloudfront.types.create_connection_group_result.CreateConnectionGroupResult":
        """<p>Creates a connection group.</p>

        Args:
            name: <p>The name of the connection group. Enter a friendly identifier that is unique within your Amazon Web Services account. This name can't be updated after you create the connection group.</p>
            ipv6_enabled: <p>Enable IPv6 for the connection group. The default is <code>true</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesEnableIPv6">Enable IPv6</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
            anycast_ip_list_id: <p>The ID of the Anycast static IP list.</p>
            enabled: <p>Enable the connection group.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_already_exists.EntityAlreadyExists: <p>The entity already exists. You must provide a unique entity.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_tagging.InvalidTagging: <p>The tagging specified is not valid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_connection_group_request.CreateConnectionGroupRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_connection_group_result.CreateConnectionGroupResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_connection_group

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_connection_group.create_connection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_connection_group_request.CreateConnectionGroupRequest = {
            "name": name
        }
        if ipv6_enabled is not None:
            input_["ipv6_enabled"] = ipv6_enabled
        if tags is not None:
            input_["tags"] = tags
        if anycast_ip_list_id is not None:
            input_["anycast_ip_list_id"] = anycast_ip_list_id
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_continuous_deployment_policy(
        self,
        continuous_deployment_policy_config: "capo_cloudfront.types.continuous_deployment_policy_config.ContinuousDeploymentPolicyConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_continuous_deployment_policy_result.CreateContinuousDeploymentPolicyResult":
        """<p>Creates a continuous deployment policy that distributes traffic for a custom domain name to two different CloudFront distributions.</p> <p>To use a continuous deployment policy, first use <code>CopyDistribution</code> to create a staging distribution, then use <code>UpdateDistribution</code> to modify the staging distribution's configuration.</p> <p>After you create and update a staging distribution, you can use a continuous deployment policy to incrementally move traffic to the staging distribution. This workflow enables you to test changes to a distribution's configuration before moving all of your domain's production traffic to the new configuration.</p>

        Args:
            continuous_deployment_policy_config: <p>Contains the configuration for a continuous deployment policy.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.continuous_deployment_policy_already_exists.ContinuousDeploymentPolicyAlreadyExists: <p>A continuous deployment policy with this configuration already exists.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.staging_distribution_in_use.StagingDistributionInUse: <p>A continuous deployment policy for this staging distribution already exists.</p>
            capo_cloudfront.errors.too_many_continuous_deployment_policies.TooManyContinuousDeploymentPolicies: <p>You have reached the maximum number of continuous deployment policies for this Amazon Web Services account.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_continuous_deployment_policy_request.CreateContinuousDeploymentPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_continuous_deployment_policy_result.CreateContinuousDeploymentPolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_continuous_deployment_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_continuous_deployment_policy.create_continuous_deployment_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_continuous_deployment_policy_request.CreateContinuousDeploymentPolicyRequest = {
            "continuous_deployment_policy_config": continuous_deployment_policy_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_distribution(
        self,
        distribution_config: "capo_cloudfront.types.distribution_config.DistributionConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_distribution_result.CreateDistributionResult":
        """<p>Creates a CloudFront distribution.</p>

        Args:
            distribution_config: <p>The distribution's configuration information.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists: <p>The CNAME specified is already defined for CloudFront.</p>
            capo_cloudfront.errors.continuous_deployment_policy_in_use.ContinuousDeploymentPolicyInUse: <p>You cannot delete a continuous deployment policy that is associated with a primary distribution.</p>
            capo_cloudfront.errors.distribution_already_exists.DistributionAlreadyExists: <p>The caller reference you attempted to create the distribution with is associated with another distribution.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.illegal_field_level_encryption_config_association_with_cache_behavior.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior: <p>The specified configuration for field-level encryption can't be associated with the specified cache behavior.</p>
            capo_cloudfront.errors.illegal_origin_access_configuration.IllegalOriginAccessConfiguration: <p>An origin cannot contain both an origin access control (OAC) and an origin access identity (OAI).</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_default_root_object.InvalidDefaultRootObject: <p>The default root object file name is too big or contains an invalid character.</p>
            capo_cloudfront.errors.invalid_domain_name_for_origin_access_control.InvalidDomainNameForOriginAccessControl: <p>An origin access control is associated with an origin whose domain name is not supported.</p>
            capo_cloudfront.errors.invalid_error_code.InvalidErrorCode: <p>An invalid error code was specified.</p>
            capo_cloudfront.errors.invalid_forward_cookies.InvalidForwardCookies: <p>Your request contains forward cookies option which doesn't match with the expectation for the <code>whitelisted</code> list of cookie names. Either list of cookie names has been specified when not allowed or list of cookie names is missing when expected.</p>
            capo_cloudfront.errors.invalid_function_association.InvalidFunctionAssociation: <p>A CloudFront function association is invalid.</p>
            capo_cloudfront.errors.invalid_geo_restriction_parameter.InvalidGeoRestrictionParameter: <p>The specified geo restriction parameter is not valid.</p>
            capo_cloudfront.errors.invalid_headers_for_s3_origin.InvalidHeadersForS3Origin: <p>The headers specified are not valid for an Amazon S3 origin.</p>
            capo_cloudfront.errors.invalid_lambda_function_association.InvalidLambdaFunctionAssociation: <p>The specified Lambda@Edge function association is invalid.</p>
            capo_cloudfront.errors.invalid_location_code.InvalidLocationCode: <p>The location code specified is not valid.</p>
            capo_cloudfront.errors.invalid_minimum_protocol_version.InvalidMinimumProtocolVersion: <p>The minimum protocol version specified is not valid.</p>
            capo_cloudfront.errors.invalid_origin.InvalidOrigin: <p>The Amazon S3 origin server specified does not refer to a valid Amazon S3 bucket.</p>
            capo_cloudfront.errors.invalid_origin_access_control.InvalidOriginAccessControl: <p>The origin access control is not valid.</p>
            capo_cloudfront.errors.invalid_origin_access_identity.InvalidOriginAccessIdentity: <p>The origin access identity is not valid or doesn't exist.</p>
            capo_cloudfront.errors.invalid_origin_keepalive_timeout.InvalidOriginKeepaliveTimeout: <p>The keep alive timeout specified for the origin is not valid.</p>
            capo_cloudfront.errors.invalid_origin_read_timeout.InvalidOriginReadTimeout: <p>The read timeout specified for the origin is not valid.</p>
            capo_cloudfront.errors.invalid_protocol_settings.InvalidProtocolSettings: <p>You cannot specify SSLv3 as the minimum protocol version if you only want to support only clients that support Server Name Indication (SNI).</p>
            capo_cloudfront.errors.invalid_query_string_parameters.InvalidQueryStringParameters: <p>The query string parameters specified are not valid.</p>
            capo_cloudfront.errors.invalid_relative_path.InvalidRelativePath: <p>The relative path is too big, is not URL-encoded, or does not begin with a slash (/).</p>
            capo_cloudfront.errors.invalid_required_protocol.InvalidRequiredProtocol: <p>This operation requires the HTTPS protocol. Ensure that you specify the HTTPS protocol in your request, or omit the <code>RequiredProtocols</code> element from your distribution configuration.</p>
            capo_cloudfront.errors.invalid_response_code.InvalidResponseCode: <p>A response code is not valid.</p>
            capo_cloudfront.errors.invalid_ttl_order.InvalidTTLOrder: <p>The TTL order specified is not valid.</p>
            capo_cloudfront.errors.invalid_viewer_certificate.InvalidViewerCertificate: <p>A viewer certificate specified is not valid.</p>
            capo_cloudfront.errors.invalid_web_acl_id.InvalidWebACLId: <p>A web ACL ID specified is not valid. To specify a web ACL created using the latest version of WAF, use the ACL ARN, for example <code>arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a</code>. To specify a web ACL created using WAF Classic, use the ACL ID, for example <code>473e64fd-f30b-4765-81a0-62ad96dd167a</code>.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy: <p>The cache policy does not exist.</p>
            capo_cloudfront.errors.no_such_continuous_deployment_policy.NoSuchContinuousDeploymentPolicy: <p>The continuous deployment policy doesn't exist.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig: <p>The specified configuration for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.no_such_origin.NoSuchOrigin: <p>No origin exists with the specified <code>Origin Id</code>.</p>
            capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy: <p>The origin request policy does not exist.</p>
            capo_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig: <p>The real-time log configuration does not exist.</p>
            capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy: <p>The response headers policy does not exist.</p>
            capo_cloudfront.errors.realtime_log_config_owner_mismatch.RealtimeLogConfigOwnerMismatch: <p>The specified real-time log configuration belongs to a different Amazon Web Services account.</p>
            capo_cloudfront.errors.too_many_cache_behaviors.TooManyCacheBehaviors: <p>You cannot create more cache behaviors for the distribution.</p>
            capo_cloudfront.errors.too_many_certificates.TooManyCertificates: <p>You cannot create anymore custom SSL/TLS certificates.</p>
            capo_cloudfront.errors.too_many_cookie_names_in_white_list.TooManyCookieNamesInWhiteList: <p>Your request contains more cookie names in the whitelist than are allowed per cache behavior.</p>
            capo_cloudfront.errors.too_many_distribution_cnam_es.TooManyDistributionCNAMEs: <p>Your request contains more CNAMEs than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_distributions.TooManyDistributions: <p>Processing your request would cause you to exceed the maximum number of distributions allowed.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_cache_policy.TooManyDistributionsAssociatedToCachePolicy: <p>The maximum number of distributions have been associated with the specified cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_field_level_encryption_config.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig: <p>The maximum number of distributions have been associated with the specified configuration for field-level encryption.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_key_group.TooManyDistributionsAssociatedToKeyGroup: <p>The number of distributions that reference this key group is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_origin_access_control.TooManyDistributionsAssociatedToOriginAccessControl: <p>The maximum number of distributions have been associated with the specified origin access control.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_origin_request_policy.TooManyDistributionsAssociatedToOriginRequestPolicy: <p>The maximum number of distributions have been associated with the specified origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_response_headers_policy.TooManyDistributionsAssociatedToResponseHeadersPolicy: <p>The maximum number of distributions have been associated with the specified response headers policy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_with_function_associations.TooManyDistributionsWithFunctionAssociations: <p>You have reached the maximum number of distributions that are associated with a CloudFront function. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_with_lambda_associations.TooManyDistributionsWithLambdaAssociations: <p>Processing your request would cause the maximum number of distributions with Lambda@Edge function associations per owner to be exceeded.</p>
            capo_cloudfront.errors.too_many_distributions_with_single_function_arn.TooManyDistributionsWithSingleFunctionARN: <p>The maximum number of distributions have been associated with the specified Lambda@Edge function.</p>
            capo_cloudfront.errors.too_many_function_associations.TooManyFunctionAssociations: <p>You have reached the maximum number of CloudFront function associations for this distribution. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_headers_in_forwarded_values.TooManyHeadersInForwardedValues: <p>Your request contains too many headers in forwarded values.</p>
            capo_cloudfront.errors.too_many_key_groups_associated_to_distribution.TooManyKeyGroupsAssociatedToDistribution: <p>The number of key groups referenced by this distribution is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_lambda_function_associations.TooManyLambdaFunctionAssociations: <p>Your request contains more Lambda@Edge function associations than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_origin_custom_headers.TooManyOriginCustomHeaders: <p>Your request contains too many origin custom headers.</p>
            capo_cloudfront.errors.too_many_origin_groups_per_distribution.TooManyOriginGroupsPerDistribution: <p>Processing your request would cause you to exceed the maximum number of origin groups allowed.</p>
            capo_cloudfront.errors.too_many_origins.TooManyOrigins: <p>You cannot create more origins for the distribution.</p>
            capo_cloudfront.errors.too_many_query_string_parameters.TooManyQueryStringParameters: <p>Your request contains too many query string parameters.</p>
            capo_cloudfront.errors.too_many_trusted_signers.TooManyTrustedSigners: <p>Your request contains more trusted signers than are allowed per distribution.</p>
            capo_cloudfront.errors.trusted_key_group_does_not_exist.TrustedKeyGroupDoesNotExist: <p>The specified key group does not exist.</p>
            capo_cloudfront.errors.trusted_signer_does_not_exist.TrustedSignerDoesNotExist: <p>One or more of your trusted signers don't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_distribution_request.CreateDistributionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_distribution_result.CreateDistributionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_distribution

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_distribution.create_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_distribution_request.CreateDistributionRequest = {
            "distribution_config": distribution_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_distribution_tenant(
        self,
        distribution_id: "capo_cloudfront.types.string.string",
        name: "capo_cloudfront.types.string.string",
        domains: "capo_cloudfront.types.domain_list.DomainList",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        tags: Optional["capo_cloudfront.types.tags.Tags"] = None,
        customizations: Optional[
            "capo_cloudfront.types.customizations.Customizations"
        ] = None,
        parameters: Optional["capo_cloudfront.types.parameters.Parameters"] = None,
        connection_group_id: Optional["capo_cloudfront.types.string.string"] = None,
        managed_certificate_request: Optional[
            "capo_cloudfront.types.managed_certificate_request.ManagedCertificateRequest"
        ] = None,
        enabled: Optional["capo_cloudfront.types.boolean.boolean"] = None,
    ) -> "capo_cloudfront.types.create_distribution_tenant_result.CreateDistributionTenantResult":
        """<p>Creates a distribution tenant.</p>

        Args:
            distribution_id: <p>The ID of the multi-tenant distribution to use for creating the distribution tenant.</p>
            name: <p>The name of the distribution tenant. Enter a friendly identifier that is unique within your Amazon Web Services account. This name can't be updated after you create the distribution tenant.</p>
            domains: <p>The domains associated with the distribution tenant. You must specify at least one domain in the request.</p>
            customizations: <p>Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.</p>
            parameters: <p>A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.</p>
            connection_group_id: <p>The ID of the connection group to associate with the distribution tenant.</p>
            managed_certificate_request: <p>The configuration for the CloudFront managed ACM certificate request.</p>
            enabled: <p>Indicates whether the distribution tenant should be enabled when created. If the distribution tenant is disabled, the distribution tenant won't serve traffic.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists: <p>The CNAME specified is already defined for CloudFront.</p>
            capo_cloudfront.errors.entity_already_exists.EntityAlreadyExists: <p>The entity already exists. You must provide a unique entity.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_association.InvalidAssociation: <p>The specified CloudFront resource can't be associated.</p>
            capo_cloudfront.errors.invalid_tagging.InvalidTagging: <p>The tagging specified is not valid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_distribution_tenant_request.CreateDistributionTenantRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_distribution_tenant_result.CreateDistributionTenantResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_distribution_tenant

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_distribution_tenant.create_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_distribution_tenant_request.CreateDistributionTenantRequest = {
            "distribution_id": distribution_id,
            "name": name,
            "domains": domains,
        }
        if tags is not None:
            input_["tags"] = tags
        if customizations is not None:
            input_["customizations"] = customizations
        if parameters is not None:
            input_["parameters"] = parameters
        if connection_group_id is not None:
            input_["connection_group_id"] = connection_group_id
        if managed_certificate_request is not None:
            input_["managed_certificate_request"] = managed_certificate_request
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_distribution_with_tags(
        self,
        distribution_config_with_tags: "capo_cloudfront.types.distribution_config_with_tags.DistributionConfigWithTags",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_distribution_with_tags_result.CreateDistributionWithTagsResult":
        """<p>Create a new distribution with tags. This API operation requires the following IAM permissions:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html">CreateDistribution</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TagResource.html">TagResource</a> </p> </li> </ul>

        Args:
            distribution_config_with_tags: <p>The distribution's configuration information.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists: <p>The CNAME specified is already defined for CloudFront.</p>
            capo_cloudfront.errors.continuous_deployment_policy_in_use.ContinuousDeploymentPolicyInUse: <p>You cannot delete a continuous deployment policy that is associated with a primary distribution.</p>
            capo_cloudfront.errors.distribution_already_exists.DistributionAlreadyExists: <p>The caller reference you attempted to create the distribution with is associated with another distribution.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.illegal_field_level_encryption_config_association_with_cache_behavior.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior: <p>The specified configuration for field-level encryption can't be associated with the specified cache behavior.</p>
            capo_cloudfront.errors.illegal_origin_access_configuration.IllegalOriginAccessConfiguration: <p>An origin cannot contain both an origin access control (OAC) and an origin access identity (OAI).</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_default_root_object.InvalidDefaultRootObject: <p>The default root object file name is too big or contains an invalid character.</p>
            capo_cloudfront.errors.invalid_domain_name_for_origin_access_control.InvalidDomainNameForOriginAccessControl: <p>An origin access control is associated with an origin whose domain name is not supported.</p>
            capo_cloudfront.errors.invalid_error_code.InvalidErrorCode: <p>An invalid error code was specified.</p>
            capo_cloudfront.errors.invalid_forward_cookies.InvalidForwardCookies: <p>Your request contains forward cookies option which doesn't match with the expectation for the <code>whitelisted</code> list of cookie names. Either list of cookie names has been specified when not allowed or list of cookie names is missing when expected.</p>
            capo_cloudfront.errors.invalid_function_association.InvalidFunctionAssociation: <p>A CloudFront function association is invalid.</p>
            capo_cloudfront.errors.invalid_geo_restriction_parameter.InvalidGeoRestrictionParameter: <p>The specified geo restriction parameter is not valid.</p>
            capo_cloudfront.errors.invalid_headers_for_s3_origin.InvalidHeadersForS3Origin: <p>The headers specified are not valid for an Amazon S3 origin.</p>
            capo_cloudfront.errors.invalid_lambda_function_association.InvalidLambdaFunctionAssociation: <p>The specified Lambda@Edge function association is invalid.</p>
            capo_cloudfront.errors.invalid_location_code.InvalidLocationCode: <p>The location code specified is not valid.</p>
            capo_cloudfront.errors.invalid_minimum_protocol_version.InvalidMinimumProtocolVersion: <p>The minimum protocol version specified is not valid.</p>
            capo_cloudfront.errors.invalid_origin.InvalidOrigin: <p>The Amazon S3 origin server specified does not refer to a valid Amazon S3 bucket.</p>
            capo_cloudfront.errors.invalid_origin_access_control.InvalidOriginAccessControl: <p>The origin access control is not valid.</p>
            capo_cloudfront.errors.invalid_origin_access_identity.InvalidOriginAccessIdentity: <p>The origin access identity is not valid or doesn't exist.</p>
            capo_cloudfront.errors.invalid_origin_keepalive_timeout.InvalidOriginKeepaliveTimeout: <p>The keep alive timeout specified for the origin is not valid.</p>
            capo_cloudfront.errors.invalid_origin_read_timeout.InvalidOriginReadTimeout: <p>The read timeout specified for the origin is not valid.</p>
            capo_cloudfront.errors.invalid_protocol_settings.InvalidProtocolSettings: <p>You cannot specify SSLv3 as the minimum protocol version if you only want to support only clients that support Server Name Indication (SNI).</p>
            capo_cloudfront.errors.invalid_query_string_parameters.InvalidQueryStringParameters: <p>The query string parameters specified are not valid.</p>
            capo_cloudfront.errors.invalid_relative_path.InvalidRelativePath: <p>The relative path is too big, is not URL-encoded, or does not begin with a slash (/).</p>
            capo_cloudfront.errors.invalid_required_protocol.InvalidRequiredProtocol: <p>This operation requires the HTTPS protocol. Ensure that you specify the HTTPS protocol in your request, or omit the <code>RequiredProtocols</code> element from your distribution configuration.</p>
            capo_cloudfront.errors.invalid_response_code.InvalidResponseCode: <p>A response code is not valid.</p>
            capo_cloudfront.errors.invalid_tagging.InvalidTagging: <p>The tagging specified is not valid.</p>
            capo_cloudfront.errors.invalid_ttl_order.InvalidTTLOrder: <p>The TTL order specified is not valid.</p>
            capo_cloudfront.errors.invalid_viewer_certificate.InvalidViewerCertificate: <p>A viewer certificate specified is not valid.</p>
            capo_cloudfront.errors.invalid_web_acl_id.InvalidWebACLId: <p>A web ACL ID specified is not valid. To specify a web ACL created using the latest version of WAF, use the ACL ARN, for example <code>arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a</code>. To specify a web ACL created using WAF Classic, use the ACL ID, for example <code>473e64fd-f30b-4765-81a0-62ad96dd167a</code>.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy: <p>The cache policy does not exist.</p>
            capo_cloudfront.errors.no_such_continuous_deployment_policy.NoSuchContinuousDeploymentPolicy: <p>The continuous deployment policy doesn't exist.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig: <p>The specified configuration for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.no_such_origin.NoSuchOrigin: <p>No origin exists with the specified <code>Origin Id</code>.</p>
            capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy: <p>The origin request policy does not exist.</p>
            capo_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig: <p>The real-time log configuration does not exist.</p>
            capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy: <p>The response headers policy does not exist.</p>
            capo_cloudfront.errors.realtime_log_config_owner_mismatch.RealtimeLogConfigOwnerMismatch: <p>The specified real-time log configuration belongs to a different Amazon Web Services account.</p>
            capo_cloudfront.errors.too_many_cache_behaviors.TooManyCacheBehaviors: <p>You cannot create more cache behaviors for the distribution.</p>
            capo_cloudfront.errors.too_many_certificates.TooManyCertificates: <p>You cannot create anymore custom SSL/TLS certificates.</p>
            capo_cloudfront.errors.too_many_cookie_names_in_white_list.TooManyCookieNamesInWhiteList: <p>Your request contains more cookie names in the whitelist than are allowed per cache behavior.</p>
            capo_cloudfront.errors.too_many_distribution_cnam_es.TooManyDistributionCNAMEs: <p>Your request contains more CNAMEs than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_distributions.TooManyDistributions: <p>Processing your request would cause you to exceed the maximum number of distributions allowed.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_cache_policy.TooManyDistributionsAssociatedToCachePolicy: <p>The maximum number of distributions have been associated with the specified cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_field_level_encryption_config.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig: <p>The maximum number of distributions have been associated with the specified configuration for field-level encryption.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_key_group.TooManyDistributionsAssociatedToKeyGroup: <p>The number of distributions that reference this key group is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_origin_access_control.TooManyDistributionsAssociatedToOriginAccessControl: <p>The maximum number of distributions have been associated with the specified origin access control.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_origin_request_policy.TooManyDistributionsAssociatedToOriginRequestPolicy: <p>The maximum number of distributions have been associated with the specified origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_response_headers_policy.TooManyDistributionsAssociatedToResponseHeadersPolicy: <p>The maximum number of distributions have been associated with the specified response headers policy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_with_function_associations.TooManyDistributionsWithFunctionAssociations: <p>You have reached the maximum number of distributions that are associated with a CloudFront function. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_with_lambda_associations.TooManyDistributionsWithLambdaAssociations: <p>Processing your request would cause the maximum number of distributions with Lambda@Edge function associations per owner to be exceeded.</p>
            capo_cloudfront.errors.too_many_distributions_with_single_function_arn.TooManyDistributionsWithSingleFunctionARN: <p>The maximum number of distributions have been associated with the specified Lambda@Edge function.</p>
            capo_cloudfront.errors.too_many_function_associations.TooManyFunctionAssociations: <p>You have reached the maximum number of CloudFront function associations for this distribution. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_headers_in_forwarded_values.TooManyHeadersInForwardedValues: <p>Your request contains too many headers in forwarded values.</p>
            capo_cloudfront.errors.too_many_key_groups_associated_to_distribution.TooManyKeyGroupsAssociatedToDistribution: <p>The number of key groups referenced by this distribution is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_lambda_function_associations.TooManyLambdaFunctionAssociations: <p>Your request contains more Lambda@Edge function associations than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_origin_custom_headers.TooManyOriginCustomHeaders: <p>Your request contains too many origin custom headers.</p>
            capo_cloudfront.errors.too_many_origin_groups_per_distribution.TooManyOriginGroupsPerDistribution: <p>Processing your request would cause you to exceed the maximum number of origin groups allowed.</p>
            capo_cloudfront.errors.too_many_origins.TooManyOrigins: <p>You cannot create more origins for the distribution.</p>
            capo_cloudfront.errors.too_many_query_string_parameters.TooManyQueryStringParameters: <p>Your request contains too many query string parameters.</p>
            capo_cloudfront.errors.too_many_trusted_signers.TooManyTrustedSigners: <p>Your request contains more trusted signers than are allowed per distribution.</p>
            capo_cloudfront.errors.trusted_key_group_does_not_exist.TrustedKeyGroupDoesNotExist: <p>The specified key group does not exist.</p>
            capo_cloudfront.errors.trusted_signer_does_not_exist.TrustedSignerDoesNotExist: <p>One or more of your trusted signers don't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_distribution_with_tags_request.CreateDistributionWithTagsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_distribution_with_tags_result.CreateDistributionWithTagsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_distribution_with_tags

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_distribution_with_tags.create_distribution_with_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_distribution_with_tags_request.CreateDistributionWithTagsRequest = {
            "distribution_config_with_tags": distribution_config_with_tags
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_field_level_encryption_config(
        self,
        field_level_encryption_config: "capo_cloudfront.types.field_level_encryption_config.FieldLevelEncryptionConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_field_level_encryption_config_result.CreateFieldLevelEncryptionConfigResult":
        """<p>Create a new field-level encryption configuration.</p>

        Args:
            field_level_encryption_config: <p>The request to create a new field-level encryption configuration.</p>

        Raises:
            capo_cloudfront.errors.field_level_encryption_config_already_exists.FieldLevelEncryptionConfigAlreadyExists: <p>The specified configuration for field-level encryption already exists.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_profile.NoSuchFieldLevelEncryptionProfile: <p>The specified profile for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.query_arg_profile_empty.QueryArgProfileEmpty: <p>No profile specified for the field-level encryption query argument.</p>
            capo_cloudfront.errors.too_many_field_level_encryption_configs.TooManyFieldLevelEncryptionConfigs: <p>The maximum number of configurations for field-level encryption have been created.</p>
            capo_cloudfront.errors.too_many_field_level_encryption_content_type_profiles.TooManyFieldLevelEncryptionContentTypeProfiles: <p>The maximum number of content type profiles for field-level encryption have been created.</p>
            capo_cloudfront.errors.too_many_field_level_encryption_query_arg_profiles.TooManyFieldLevelEncryptionQueryArgProfiles: <p>The maximum number of query arg profiles for field-level encryption have been created.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_field_level_encryption_config_request.CreateFieldLevelEncryptionConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_field_level_encryption_config_result.CreateFieldLevelEncryptionConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_field_level_encryption_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_field_level_encryption_config.create_field_level_encryption_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_field_level_encryption_config_request.CreateFieldLevelEncryptionConfigRequest = {
            "field_level_encryption_config": field_level_encryption_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_field_level_encryption_profile(
        self,
        field_level_encryption_profile_config: "capo_cloudfront.types.field_level_encryption_profile_config.FieldLevelEncryptionProfileConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_field_level_encryption_profile_result.CreateFieldLevelEncryptionProfileResult":
        """<p>Create a field-level encryption profile.</p>

        Args:
            field_level_encryption_profile_config: <p>The request to create a field-level encryption profile.</p>

        Raises:
            capo_cloudfront.errors.field_level_encryption_profile_already_exists.FieldLevelEncryptionProfileAlreadyExists: <p>The specified profile for field-level encryption already exists.</p>
            capo_cloudfront.errors.field_level_encryption_profile_size_exceeded.FieldLevelEncryptionProfileSizeExceeded: <p>The maximum size of a profile for field-level encryption was exceeded.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_public_key.NoSuchPublicKey: <p>The specified public key doesn't exist.</p>
            capo_cloudfront.errors.too_many_field_level_encryption_encryption_entities.TooManyFieldLevelEncryptionEncryptionEntities: <p>The maximum number of encryption entities for field-level encryption have been created.</p>
            capo_cloudfront.errors.too_many_field_level_encryption_field_patterns.TooManyFieldLevelEncryptionFieldPatterns: <p>The maximum number of field patterns for field-level encryption have been created.</p>
            capo_cloudfront.errors.too_many_field_level_encryption_profiles.TooManyFieldLevelEncryptionProfiles: <p>The maximum number of profiles for field-level encryption have been created.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_field_level_encryption_profile_request.CreateFieldLevelEncryptionProfileRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_field_level_encryption_profile_result.CreateFieldLevelEncryptionProfileResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_field_level_encryption_profile

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_field_level_encryption_profile.create_field_level_encryption_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_field_level_encryption_profile_request.CreateFieldLevelEncryptionProfileRequest = {
            "field_level_encryption_profile_config": field_level_encryption_profile_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_function(
        self,
        name: "capo_cloudfront.types.function_name.FunctionName",
        function_config: "capo_cloudfront.types.function_config.FunctionConfig",
        function_code: "capo_cloudfront.types.function_blob.FunctionBlob",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        tags: Optional["capo_cloudfront.types.tags.Tags"] = None,
    ) -> "capo_cloudfront.types.create_function_result.CreateFunctionResult":
        """<p>Creates a CloudFront function.</p> <p>To create a function, you provide the function code and some configuration information about the function. The response contains an Amazon Resource Name (ARN) that uniquely identifies the function.</p> <p>When you create a function, it's in the <code>DEVELOPMENT</code> stage. In this stage, you can test the function with <code>TestFunction</code>, and update it with <code>UpdateFunction</code>.</p> <p>When you're ready to use your function with a CloudFront distribution, use <code>PublishFunction</code> to copy the function from the <code>DEVELOPMENT</code> stage to <code>LIVE</code>. When it's live, you can attach the function to a distribution's cache behavior, using the function's ARN.</p>

        Args:
            name: <p>A name to identify the function.</p>
            function_config: <p>Configuration information about the function, including an optional comment and the function's runtime.</p>
            function_code: <p>The function code. For more information about writing a CloudFront function, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/writing-function-code.html">Writing function code for CloudFront Functions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Raises:
            capo_cloudfront.errors.function_already_exists.FunctionAlreadyExists: <p>A function with the same name already exists in this Amazon Web Services account. To create a function, you must provide a unique name. To update an existing function, use <code>UpdateFunction</code>.</p>
            capo_cloudfront.errors.function_size_limit_exceeded.FunctionSizeLimitExceeded: <p>The function is too large. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.too_many_functions.TooManyFunctions: <p>You have reached the maximum number of CloudFront functions for this Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a function
            Use the following command to create a function.

            >>> client.create_function(name='my-function-name', function_config={'Comment': 'my-function-comment', 'Runtime': 'cloudfront-js-2.0', 'KeyValueStoreAssociations': {'Quantity': 1, 'Items': [{'KeyValueStoreARN': 'arn:aws:cloudfront::123456789012:key-value-store/54947df8-0e9e-4471-a2f9-9af509fb5889'}]}}, function_code='function-code.js')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_function_request.CreateFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_function_result.CreateFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_function.create_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_function_request.CreateFunctionRequest = {
            "name": name,
            "function_config": function_config,
            "function_code": function_code,
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

    def create_invalidation(
        self,
        distribution_id: "capo_cloudfront.types.string.string",
        invalidation_batch: "capo_cloudfront.types.invalidation_batch.InvalidationBatch",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_invalidation_result.CreateInvalidationResult":
        """<p>Create a new invalidation. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html">Invalidating files</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            distribution_id: <p>The distribution's id.</p>
            invalidation_batch: <p>The batch information for the invalidation.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.batch_too_large.BatchTooLarge: <p>Invalidation batch specified is too large.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.too_many_invalidations_in_progress.TooManyInvalidationsInProgress: <p>You have exceeded the maximum number of allowable InProgress invalidation batch requests, or invalidation objects.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_invalidation_request.CreateInvalidationRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_invalidation_result.CreateInvalidationResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_invalidation

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_invalidation.create_invalidation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_invalidation_request.CreateInvalidationRequest = {
            "distribution_id": distribution_id,
            "invalidation_batch": invalidation_batch,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_invalidation_for_distribution_tenant(
        self,
        id: "capo_cloudfront.types.string.string",
        invalidation_batch: "capo_cloudfront.types.invalidation_batch.InvalidationBatch",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_invalidation_for_distribution_tenant_result.CreateInvalidationForDistributionTenantResult":
        """<p>Creates an invalidation for a distribution tenant. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html">Invalidating files</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            id: <p>The ID of the distribution tenant.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.batch_too_large.BatchTooLarge: <p>Invalidation batch specified is too large.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.too_many_invalidations_in_progress.TooManyInvalidationsInProgress: <p>You have exceeded the maximum number of allowable InProgress invalidation batch requests, or invalidation objects.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_invalidation_for_distribution_tenant_request.CreateInvalidationForDistributionTenantRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_invalidation_for_distribution_tenant_result.CreateInvalidationForDistributionTenantResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_invalidation_for_distribution_tenant

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_invalidation_for_distribution_tenant.create_invalidation_for_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_invalidation_for_distribution_tenant_request.CreateInvalidationForDistributionTenantRequest = {
            "id": id,
            "invalidation_batch": invalidation_batch,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_key_group(
        self,
        key_group_config: "capo_cloudfront.types.key_group_config.KeyGroupConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_key_group_result.CreateKeyGroupResult":
        """<p>Creates a key group that you can use with <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">CloudFront signed URLs and signed cookies</a>.</p> <p>To create a key group, you must specify at least one public key for the key group. After you create a key group, you can reference it from one or more cache behaviors. When you reference a key group in a cache behavior, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with a private key whose corresponding public key is in the key group. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving private content</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            key_group_config: <p>A key group configuration.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.key_group_already_exists.KeyGroupAlreadyExists: <p>A key group with this name already exists. You must provide a unique name. To modify an existing key group, use <code>UpdateKeyGroup</code>.</p>
            capo_cloudfront.errors.too_many_key_groups.TooManyKeyGroups: <p>You have reached the maximum number of key groups for this Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_public_keys_in_key_group.TooManyPublicKeysInKeyGroup: <p>The number of public keys in this key group is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_key_group_request.CreateKeyGroupRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_key_group_result.CreateKeyGroupResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_key_group

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_key_group.create_key_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_key_group_request.CreateKeyGroupRequest = {
            "key_group_config": key_group_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_key_value_store(
        self,
        name: "capo_cloudfront.types.key_value_store_name.KeyValueStoreName",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        comment: Optional[
            "capo_cloudfront.types.key_value_store_comment.KeyValueStoreComment"
        ] = None,
        import_source: Optional[
            "capo_cloudfront.types.import_source.ImportSource"
        ] = None,
        tags: Optional["capo_cloudfront.types.tags.Tags"] = None,
    ) -> (
        "capo_cloudfront.types.create_key_value_store_result.CreateKeyValueStoreResult"
    ):
        """<p>Specifies the key value store resource to add to your account. In your account, the key value store names must be unique. You can also import key value store data in JSON format from an S3 bucket by providing a valid <code>ImportSource</code> that you own.</p>

        Args:
            name: <p>The name of the key value store. The minimum length is 1 character and the maximum length is 64 characters.</p>
            comment: <p>The comment of the key value store.</p>
            import_source: <p>The S3 bucket that provides the source for the import. The source must be in a valid JSON format.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_already_exists.EntityAlreadyExists: <p>The entity already exists. You must provide a unique entity.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_size_limit_exceeded.EntitySizeLimitExceeded: <p>The entity size limit was exceeded.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a KeyValueStore
            Use the following command to create a KeyValueStore.

            >>> client.create_key_value_store(name='my-keyvaluestore-name', comment='my-key-valuestore-comment', import_source={'SourceType': 'S3', 'SourceARN': 'arn:aws:s3:::amzn-s3-demo-bucket/validJSON.json'})
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_key_value_store_request.CreateKeyValueStoreRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_key_value_store_result.CreateKeyValueStoreResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_key_value_store

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_key_value_store.create_key_value_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_key_value_store_request.CreateKeyValueStoreRequest = {
            "name": name
        }
        if comment is not None:
            input_["comment"] = comment
        if import_source is not None:
            input_["import_source"] = import_source
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_monitoring_subscription(
        self,
        distribution_id: "capo_cloudfront.types.string.string",
        monitoring_subscription: "capo_cloudfront.types.monitoring_subscription.MonitoringSubscription",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_monitoring_subscription_result.CreateMonitoringSubscriptionResult":
        """<p>Enables or disables additional Amazon CloudWatch metrics for the specified CloudFront distribution. The additional metrics incur an additional cost.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.html#monitoring-console.distributions-additional">Viewing additional CloudFront distribution metrics</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            distribution_id: <p>The ID of the distribution that you are enabling metrics for.</p>
            monitoring_subscription: <p>A monitoring subscription. This structure contains information about whether additional CloudWatch metrics are enabled for a given CloudFront distribution.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.monitoring_subscription_already_exists.MonitoringSubscriptionAlreadyExists: <p>A monitoring subscription already exists for the specified distribution.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_monitoring_subscription_request.CreateMonitoringSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_monitoring_subscription_result.CreateMonitoringSubscriptionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_monitoring_subscription

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_monitoring_subscription.create_monitoring_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_monitoring_subscription_request.CreateMonitoringSubscriptionRequest = {
            "distribution_id": distribution_id,
            "monitoring_subscription": monitoring_subscription,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_origin_access_control(
        self,
        origin_access_control_config: "capo_cloudfront.types.origin_access_control_config.OriginAccessControlConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_origin_access_control_result.CreateOriginAccessControlResult":
        """<p>Creates a new origin access control in CloudFront. After you create an origin access control, you can add it to an origin in a CloudFront distribution so that CloudFront sends authenticated (signed) requests to the origin.</p> <p>This makes it possible to block public access to the origin, allowing viewers (users) to access the origin's content only through CloudFront.</p> <p>For more information about using a CloudFront origin access control, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html">Restricting access to an Amazon Web Services origin</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            origin_access_control_config: <p>Contains the origin access control.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.origin_access_control_already_exists.OriginAccessControlAlreadyExists: <p>An origin access control with the specified parameters already exists.</p>
            capo_cloudfront.errors.too_many_origin_access_controls.TooManyOriginAccessControls: <p>The number of origin access controls in your Amazon Web Services account exceeds the maximum allowed.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_origin_access_control_request.CreateOriginAccessControlRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_origin_access_control_result.CreateOriginAccessControlResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_origin_access_control

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_origin_access_control.create_origin_access_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_origin_access_control_request.CreateOriginAccessControlRequest = {
            "origin_access_control_config": origin_access_control_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_origin_request_policy(
        self,
        origin_request_policy_config: "capo_cloudfront.types.origin_request_policy_config.OriginRequestPolicyConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult":
        """<p>Creates an origin request policy.</p> <p>After you create an origin request policy, you can attach it to one or more cache behaviors. When it's attached to a cache behavior, the origin request policy determines the values that CloudFront includes in requests that it sends to the origin. Each request that CloudFront sends to the origin includes the following:</p> <ul> <li> <p>The request body and the URL path (without the domain name) from the viewer request.</p> </li> <li> <p>The headers that CloudFront automatically includes in every origin request, including <code>Host</code>, <code>User-Agent</code>, and <code>X-Amz-Cf-Id</code>.</p> </li> <li> <p>All HTTP headers, cookies, and URL query strings that are specified in the cache policy or the origin request policy. These can include items from the viewer request and, in the case of headers, additional ones that are added by CloudFront.</p> </li> </ul> <p>CloudFront sends a request when it can't find a valid object in its cache that matches the request. If you want to send values to the origin and also include them in the cache key, use <code>CachePolicy</code>.</p> <p>For more information about origin request policies, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html">Controlling origin requests</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            origin_request_policy_config: <p>An origin request policy configuration.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.origin_request_policy_already_exists.OriginRequestPolicyAlreadyExists: <p>An origin request policy with this name already exists. You must provide a unique name. To modify an existing origin request policy, use <code>UpdateOriginRequestPolicy</code>.</p>
            capo_cloudfront.errors.too_many_cookies_in_origin_request_policy.TooManyCookiesInOriginRequestPolicy: <p>The number of cookies in the origin request policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_headers_in_origin_request_policy.TooManyHeadersInOriginRequestPolicy: <p>The number of headers in the origin request policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_origin_request_policies.TooManyOriginRequestPolicies: <p>You have reached the maximum number of origin request policies for this Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_query_strings_in_origin_request_policy.TooManyQueryStringsInOriginRequestPolicy: <p>The number of query strings in the origin request policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_origin_request_policy_request.CreateOriginRequestPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_origin_request_policy_result.CreateOriginRequestPolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_origin_request_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_origin_request_policy.create_origin_request_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_origin_request_policy_request.CreateOriginRequestPolicyRequest = {
            "origin_request_policy_config": origin_request_policy_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_public_key(
        self,
        public_key_config: "capo_cloudfront.types.public_key_config.PublicKeyConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_public_key_result.CreatePublicKeyResult":
        """<p>Uploads a public key to CloudFront that you can use with <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">signed URLs and signed cookies</a>, or with <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html">field-level encryption</a>.</p>

        Args:
            public_key_config: <p>A CloudFront public key configuration.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.public_key_already_exists.PublicKeyAlreadyExists: <p>The specified public key already exists.</p>
            capo_cloudfront.errors.too_many_public_keys.TooManyPublicKeys: <p>The maximum number of public keys for field-level encryption have been created. To create a new public key, delete one of the existing keys.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_public_key_request.CreatePublicKeyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_public_key_result.CreatePublicKeyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_public_key

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_public_key.create_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_public_key_request.CreatePublicKeyRequest = {
            "public_key_config": public_key_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_realtime_log_config(
        self,
        end_points: "capo_cloudfront.types.end_point_list.EndPointList",
        fields: "capo_cloudfront.types.field_list.FieldList",
        name: "capo_cloudfront.types.string.string",
        sampling_rate: "capo_cloudfront.types.long.long",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_realtime_log_config_result.CreateRealtimeLogConfigResult":
        """<p>Creates a real-time log configuration.</p> <p>After you create a real-time log configuration, you can attach it to one or more cache behaviors to send real-time log data to the specified Amazon Kinesis data stream.</p> <p>For more information about real-time log configurations, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html">Real-time logs</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            end_points: <p>Contains information about the Amazon Kinesis data stream where you are sending real-time log data.</p>
            fields: <p>A list of fields to include in each real-time log record.</p> <p>For more information about fields, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields">Real-time log configuration fields</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
            name: <p>A unique name to identify this real-time log configuration.</p>
            sampling_rate: <p>The sampling rate for this real-time log configuration. You can specify a whole number between 1 and 100 (inclusive) to determine the percentage of viewer requests that are represented in the real-time log data.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.realtime_log_config_already_exists.RealtimeLogConfigAlreadyExists: <p>A real-time log configuration with this name already exists. You must provide a unique name. To modify an existing real-time log configuration, use <code>UpdateRealtimeLogConfig</code>.</p>
            capo_cloudfront.errors.too_many_realtime_log_configs.TooManyRealtimeLogConfigs: <p>You have reached the maximum number of real-time log configurations for this Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_realtime_log_config_request.CreateRealtimeLogConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_realtime_log_config_result.CreateRealtimeLogConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_realtime_log_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_realtime_log_config.create_realtime_log_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_realtime_log_config_request.CreateRealtimeLogConfigRequest = {
            "end_points": end_points,
            "fields": fields,
            "name": name,
            "sampling_rate": sampling_rate,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_response_headers_policy(
        self,
        response_headers_policy_config: "capo_cloudfront.types.response_headers_policy_config.ResponseHeadersPolicyConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_response_headers_policy_result.CreateResponseHeadersPolicyResult":
        """<p>Creates a response headers policy.</p> <p>A response headers policy contains information about a set of HTTP headers. To create a response headers policy, you provide some metadata about the policy and a set of configurations that specify the headers.</p> <p>After you create a response headers policy, you can use its ID to attach it to one or more cache behaviors in a CloudFront distribution. When it's attached to a cache behavior, the response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to requests that match the cache behavior. CloudFront adds or removes response headers according to the configuration of the response headers policy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html">Adding or removing HTTP headers in CloudFront responses</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            response_headers_policy_config: <p>Contains metadata about the response headers policy, and a set of configurations that specify the HTTP headers.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.response_headers_policy_already_exists.ResponseHeadersPolicyAlreadyExists: <p>A response headers policy with this name already exists. You must provide a unique name. To modify an existing response headers policy, use <code>UpdateResponseHeadersPolicy</code>.</p>
            capo_cloudfront.errors.too_long_csp_in_response_headers_policy.TooLongCSPInResponseHeadersPolicy: <p>The length of the <code>Content-Security-Policy</code> header value in the response headers policy exceeds the maximum.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_custom_headers_in_response_headers_policy.TooManyCustomHeadersInResponseHeadersPolicy: <p>The number of custom headers in the response headers policy exceeds the maximum.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_remove_headers_in_response_headers_policy.TooManyRemoveHeadersInResponseHeadersPolicy: <p>The number of headers in <code>RemoveHeadersConfig</code> in the response headers policy exceeds the maximum.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_response_headers_policies.TooManyResponseHeadersPolicies: <p>You have reached the maximum number of response headers policies for this Amazon Web Services account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_response_headers_policy_request.CreateResponseHeadersPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_response_headers_policy_result.CreateResponseHeadersPolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_response_headers_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_response_headers_policy.create_response_headers_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_response_headers_policy_request.CreateResponseHeadersPolicyRequest = {
            "response_headers_policy_config": response_headers_policy_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_streaming_distribution(
        self,
        streaming_distribution_config: "capo_cloudfront.types.streaming_distribution_config.StreamingDistributionConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_streaming_distribution_result.CreateStreamingDistributionResult":
        """<p>This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP) distributions on December 31, 2020. For more information, <a href="http://forums.aws.amazon.com/ann.jspa?annID=7356">read the announcement</a> on the Amazon CloudFront discussion forum.</p>

        Args:
            streaming_distribution_config: <p>The streaming distribution's configuration information.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists: <p>The CNAME specified is already defined for CloudFront.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_origin.InvalidOrigin: <p>The Amazon S3 origin server specified does not refer to a valid Amazon S3 bucket.</p>
            capo_cloudfront.errors.invalid_origin_access_control.InvalidOriginAccessControl: <p>The origin access control is not valid.</p>
            capo_cloudfront.errors.invalid_origin_access_identity.InvalidOriginAccessIdentity: <p>The origin access identity is not valid or doesn't exist.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.streaming_distribution_already_exists.StreamingDistributionAlreadyExists: <p>The caller reference you attempted to create the streaming distribution with is associated with another distribution</p>
            capo_cloudfront.errors.too_many_streaming_distribution_cnam_es.TooManyStreamingDistributionCNAMEs: <p>Your request contains more CNAMEs than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_streaming_distributions.TooManyStreamingDistributions: <p>Processing your request would cause you to exceed the maximum number of streaming distributions allowed.</p>
            capo_cloudfront.errors.too_many_trusted_signers.TooManyTrustedSigners: <p>Your request contains more trusted signers than are allowed per distribution.</p>
            capo_cloudfront.errors.trusted_signer_does_not_exist.TrustedSignerDoesNotExist: <p>One or more of your trusted signers don't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_streaming_distribution_request.CreateStreamingDistributionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_streaming_distribution_result.CreateStreamingDistributionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_streaming_distribution

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_streaming_distribution.create_streaming_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_streaming_distribution_request.CreateStreamingDistributionRequest = {
            "streaming_distribution_config": streaming_distribution_config
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_streaming_distribution_with_tags(
        self,
        streaming_distribution_config_with_tags: "capo_cloudfront.types.streaming_distribution_config_with_tags.StreamingDistributionConfigWithTags",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.create_streaming_distribution_with_tags_result.CreateStreamingDistributionWithTagsResult":
        """<p>This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP) distributions on December 31, 2020. For more information, <a href="http://forums.aws.amazon.com/ann.jspa?annID=7356">read the announcement</a> on the Amazon CloudFront discussion forum.</p>

        Args:
            streaming_distribution_config_with_tags: <p>The streaming distribution's configuration information.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists: <p>The CNAME specified is already defined for CloudFront.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_origin.InvalidOrigin: <p>The Amazon S3 origin server specified does not refer to a valid Amazon S3 bucket.</p>
            capo_cloudfront.errors.invalid_origin_access_control.InvalidOriginAccessControl: <p>The origin access control is not valid.</p>
            capo_cloudfront.errors.invalid_origin_access_identity.InvalidOriginAccessIdentity: <p>The origin access identity is not valid or doesn't exist.</p>
            capo_cloudfront.errors.invalid_tagging.InvalidTagging: <p>The tagging specified is not valid.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.streaming_distribution_already_exists.StreamingDistributionAlreadyExists: <p>The caller reference you attempted to create the streaming distribution with is associated with another distribution</p>
            capo_cloudfront.errors.too_many_streaming_distribution_cnam_es.TooManyStreamingDistributionCNAMEs: <p>Your request contains more CNAMEs than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_streaming_distributions.TooManyStreamingDistributions: <p>Processing your request would cause you to exceed the maximum number of streaming distributions allowed.</p>
            capo_cloudfront.errors.too_many_trusted_signers.TooManyTrustedSigners: <p>Your request contains more trusted signers than are allowed per distribution.</p>
            capo_cloudfront.errors.trusted_signer_does_not_exist.TrustedSignerDoesNotExist: <p>One or more of your trusted signers don't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_streaming_distribution_with_tags_request.CreateStreamingDistributionWithTagsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_streaming_distribution_with_tags_result.CreateStreamingDistributionWithTagsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_streaming_distribution_with_tags

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_streaming_distribution_with_tags.create_streaming_distribution_with_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_streaming_distribution_with_tags_request.CreateStreamingDistributionWithTagsRequest = {
            "streaming_distribution_config_with_tags": streaming_distribution_config_with_tags
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_trust_store(
        self,
        name: "capo_cloudfront.types.string.string",
        ca_certificates_bundle_source: "capo_cloudfront.types.ca_certificates_bundle_source.CaCertificatesBundleSource",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        use_client_certificate_ocsp_endpoint: Optional[
            "capo_cloudfront.types.boolean.boolean"
        ] = None,
        tags: Optional["capo_cloudfront.types.tags.Tags"] = None,
    ) -> "capo_cloudfront.types.create_trust_store_result.CreateTrustStoreResult":
        """<p>Creates a trust store.</p>

        Args:
            name: <p>A name for the trust store.</p>
            ca_certificates_bundle_source: <p>The CA certificates bundle source for the trust store.</p>
            use_client_certificate_ocsp_endpoint: <p>A Boolean that determines whether to use the CA certificate's OCSP endpoint to check certificate revocation status.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_already_exists.EntityAlreadyExists: <p>The entity already exists. You must provide a unique entity.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_tagging.InvalidTagging: <p>The tagging specified is not valid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_trust_store_request.CreateTrustStoreRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_trust_store_result.CreateTrustStoreResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_trust_store

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_trust_store.create_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_trust_store_request.CreateTrustStoreRequest = {
            "name": name,
            "ca_certificates_bundle_source": ca_certificates_bundle_source,
        }
        if use_client_certificate_ocsp_endpoint is not None:
            input_["use_client_certificate_ocsp_endpoint"] = (
                use_client_certificate_ocsp_endpoint
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

    def create_vpc_origin(
        self,
        vpc_origin_endpoint_config: "capo_cloudfront.types.vpc_origin_endpoint_config.VpcOriginEndpointConfig",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        tags: Optional["capo_cloudfront.types.tags.Tags"] = None,
    ) -> "capo_cloudfront.types.create_vpc_origin_result.CreateVpcOriginResult":
        """<p>Create an Amazon CloudFront VPC origin.</p>

        Args:
            vpc_origin_endpoint_config: <p>The VPC origin endpoint configuration.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_already_exists.EntityAlreadyExists: <p>The entity already exists. You must provide a unique entity.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_tagging.InvalidTagging: <p>The tagging specified is not valid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a VPC origin
            The following command creates a VPC origin:

            >>> client.create_vpc_origin(vpc_origin_endpoint_config={'Name': 'my-vpcorigin-name', 'Arn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-alb-us-west-2/e6aa5c7d26415c6d', 'HTTPPort': 80, 'HTTPSPort': 443, 'OriginProtocolPolicy': 'match-viewer', 'OriginSslProtocols': {'Quantity': 2, 'Items': ['TLSv1.1', 'TLSv1.2']}})
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.create_vpc_origin_request.CreateVpcOriginRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.create_vpc_origin_result.CreateVpcOriginResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.create_vpc_origin

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.create_vpc_origin.create_vpc_origin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.create_vpc_origin_request.CreateVpcOriginRequest = {
            "vpc_origin_endpoint_config": vpc_origin_endpoint_config
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

    def delete_anycast_ip_list(
        self,
        id: "capo_cloudfront.types.string.string",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes an Anycast static IP list.</p>

        Args:
            id: <p>The ID of the Anycast static IP list.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the Anycast static IP list that you are deleting.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cannot_delete_entity_while_in_use.CannotDeleteEntityWhileInUse: <p>The entity cannot be deleted while it is in use.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.illegal_delete.IllegalDelete: <p>Deletion is not allowed for this entity.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_anycast_ip_list_request.DeleteAnycastIpListRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_anycast_ip_list

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_anycast_ip_list.delete_anycast_ip_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_anycast_ip_list_request.DeleteAnycastIpListRequest = {
            "id": id,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cache_policy(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a cache policy.</p> <p>You cannot delete a cache policy if it's attached to a cache behavior. First update your distributions to remove the cache policy from all cache behaviors, then delete the cache policy.</p> <p>To delete a cache policy, you must provide the policy's identifier and version. To get these values, you can use <code>ListCachePolicies</code> or <code>GetCachePolicy</code>.</p>

        Args:
            id: <p>The unique identifier for the cache policy that you are deleting. To get the identifier, you can use <code>ListCachePolicies</code>.</p>
            if_match: <p>The version of the cache policy that you are deleting. The version is the cache policy's <code>ETag</code> value, which you can get using <code>ListCachePolicies</code>, <code>GetCachePolicy</code>, or <code>GetCachePolicyConfig</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cache_policy_in_use.CachePolicyInUse: <p>Cannot delete the cache policy because it is attached to one or more cache behaviors.</p>
            capo_cloudfront.errors.illegal_delete.IllegalDelete: <p>Deletion is not allowed for this entity.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy: <p>The cache policy does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_cache_policy_request.DeleteCachePolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_cache_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_cache_policy.delete_cache_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_cache_policy_request.DeleteCachePolicyRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cloud_front_origin_access_identity(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Delete an origin access identity.</p>

        Args:
            id: <p>The origin access identity's ID.</p>
            if_match: <p>The value of the <code>ETag</code> header you received from a previous <code>GET</code> or <code>PUT</code> request. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cloud_front_origin_access_identity_in_use.CloudFrontOriginAccessIdentityInUse: <p>The Origin Access Identity specified is already in use.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_cloud_front_origin_access_identity.NoSuchCloudFrontOriginAccessIdentity: <p>The specified origin access identity does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_cloud_front_origin_access_identity_request.DeleteCloudFrontOriginAccessIdentityRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_cloud_front_origin_access_identity

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_cloud_front_origin_access_identity.delete_cloud_front_origin_access_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_cloud_front_origin_access_identity_request.DeleteCloudFrontOriginAccessIdentityRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_connection_function(
        self,
        id: "capo_cloudfront.types.resource_id.ResourceId",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes a connection function.</p>

        Args:
            id: <p>The connection function's ID.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the connection function you are deleting.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cannot_delete_entity_while_in_use.CannotDeleteEntityWhileInUse: <p>The entity cannot be deleted while it is in use.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_connection_function_request.DeleteConnectionFunctionRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_connection_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_connection_function.delete_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_connection_function_request.DeleteConnectionFunctionRequest = {
            "id": id,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_connection_group(
        self,
        id: "capo_cloudfront.types.string.string",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes a connection group.</p>

        Args:
            id: <p>The ID of the connection group to delete.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the connection group to delete.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cannot_delete_entity_while_in_use.CannotDeleteEntityWhileInUse: <p>The entity cannot be deleted while it is in use.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.resource_not_disabled.ResourceNotDisabled: <p>The specified CloudFront resource hasn't been disabled yet.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_connection_group_request.DeleteConnectionGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_connection_group

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_connection_group.delete_connection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_connection_group_request.DeleteConnectionGroupRequest = {
            "id": id,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_continuous_deployment_policy(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a continuous deployment policy.</p> <p>You cannot delete a continuous deployment policy that's attached to a primary distribution. First update your distribution to remove the continuous deployment policy, then you can delete the policy.</p>

        Args:
            id: <p>The identifier of the continuous deployment policy that you are deleting.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the continuous deployment policy that you are deleting.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.continuous_deployment_policy_in_use.ContinuousDeploymentPolicyInUse: <p>You cannot delete a continuous deployment policy that is associated with a primary distribution.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_continuous_deployment_policy.NoSuchContinuousDeploymentPolicy: <p>The continuous deployment policy doesn't exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_continuous_deployment_policy_request.DeleteContinuousDeploymentPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_continuous_deployment_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_continuous_deployment_policy.delete_continuous_deployment_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_continuous_deployment_policy_request.DeleteContinuousDeploymentPolicyRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_distribution(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Delete a distribution.</p> <important> <p>Before you can delete a distribution, you must disable it, which requires permission to update the distribution. Once deleted, a distribution cannot be recovered.</p> </important>

        Args:
            id: <p>The distribution ID.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when you disabled the distribution. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.distribution_not_disabled.DistributionNotDisabled: <p>The specified CloudFront distribution is not disabled. You must disable the distribution before you can delete it.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.resource_in_use.ResourceInUse: <p>Cannot delete this resource because it is in use.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_distribution_request.DeleteDistributionRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_distribution

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_distribution.delete_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_distribution_request.DeleteDistributionRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_distribution_tenant(
        self,
        id: "capo_cloudfront.types.string.string",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes a distribution tenant. If you use this API operation to delete a distribution tenant that is currently enabled, the request will fail.</p> <p>To delete a distribution tenant, you must first disable the distribution tenant by using the <code>UpdateDistributionTenant</code> API operation.</p>

        Args:
            id: <p>The ID of the distribution tenant to delete.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the distribution tenant. This value is returned in the response of the <code>GetDistributionTenant</code> API operation.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.resource_not_disabled.ResourceNotDisabled: <p>The specified CloudFront resource hasn't been disabled yet.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_distribution_tenant_request.DeleteDistributionTenantRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_distribution_tenant

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_distribution_tenant.delete_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_distribution_tenant_request.DeleteDistributionTenantRequest = {
            "id": id,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_field_level_encryption_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Remove a field-level encryption configuration.</p>

        Args:
            id: <p>The ID of the configuration you want to delete from CloudFront.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the configuration identity to delete. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.field_level_encryption_config_in_use.FieldLevelEncryptionConfigInUse: <p>The specified configuration for field-level encryption is in use.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig: <p>The specified configuration for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_field_level_encryption_config_request.DeleteFieldLevelEncryptionConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_field_level_encryption_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_field_level_encryption_config.delete_field_level_encryption_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_field_level_encryption_config_request.DeleteFieldLevelEncryptionConfigRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_field_level_encryption_profile(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Remove a field-level encryption profile.</p>

        Args:
            id: <p>Request the ID of the profile you want to delete from CloudFront.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the profile to delete. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.field_level_encryption_profile_in_use.FieldLevelEncryptionProfileInUse: <p>The specified profile for field-level encryption is in use.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_profile.NoSuchFieldLevelEncryptionProfile: <p>The specified profile for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_field_level_encryption_profile_request.DeleteFieldLevelEncryptionProfileRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_field_level_encryption_profile

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_field_level_encryption_profile.delete_field_level_encryption_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_field_level_encryption_profile_request.DeleteFieldLevelEncryptionProfileRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function(
        self,
        name: "capo_cloudfront.types.function_name.FunctionName",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes a CloudFront function.</p> <p>You cannot delete a function if it's associated with a cache behavior. First, update your distributions to remove the function association from all cache behaviors, then delete the function.</p> <p>To delete a function, you must provide the function's name and version (<code>ETag</code> value). To get these values, you can use <code>ListFunctions</code> and <code>DescribeFunction</code>.</p>

        Args:
            name: <p>The name of the function that you are deleting.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the function that you are deleting, which you can get using <code>DescribeFunction</code>.</p>

        Raises:
            capo_cloudfront.errors.function_in_use.FunctionInUse: <p>Cannot delete the function because it's attached to one or more cache behaviors.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_function_exists.NoSuchFunctionExists: <p>The function does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_function_request.DeleteFunctionRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_function.delete_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_function_request.DeleteFunctionRequest = {
            "name": name,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_key_group(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a key group.</p> <p>You cannot delete a key group that is referenced in a cache behavior. First update your distributions to remove the key group from all cache behaviors, then delete the key group.</p> <p>To delete a key group, you must provide the key group's identifier and version. To get these values, use <code>ListKeyGroups</code> followed by <code>GetKeyGroup</code> or <code>GetKeyGroupConfig</code>.</p>

        Args:
            id: <p>The identifier of the key group that you are deleting. To get the identifier, use <code>ListKeyGroups</code>.</p>
            if_match: <p>The version of the key group that you are deleting. The version is the key group's <code>ETag</code> value. To get the <code>ETag</code>, use <code>GetKeyGroup</code> or <code>GetKeyGroupConfig</code>.</p>

        Raises:
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_resource.NoSuchResource: <p>A resource that was specified is not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.resource_in_use.ResourceInUse: <p>Cannot delete this resource because it is in use.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_key_group_request.DeleteKeyGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_key_group

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_key_group.delete_key_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_key_group_request.DeleteKeyGroupRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_key_value_store(
        self,
        name: "capo_cloudfront.types.key_value_store_name.KeyValueStoreName",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Specifies the key value store to delete.</p>

        Args:
            name: <p>The name of the key value store.</p>
            if_match: <p>The key value store to delete, if a match occurs.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cannot_delete_entity_while_in_use.CannotDeleteEntityWhileInUse: <p>The entity cannot be deleted while it is in use.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a KeyValueStore
            Use the following command to delete a KeyValueStore.

            >>> client.delete_key_value_store(name='my-keyvaluestore-name', if_match='ETVPDKIKX0DER')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_key_value_store_request.DeleteKeyValueStoreRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_key_value_store

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_key_value_store.delete_key_value_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_key_value_store_request.DeleteKeyValueStoreRequest = {
            "name": name,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_monitoring_subscription(
        self,
        distribution_id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.delete_monitoring_subscription_result.DeleteMonitoringSubscriptionResult":
        """<p>Disables additional CloudWatch metrics for the specified CloudFront distribution.</p>

        Args:
            distribution_id: <p>The ID of the distribution that you are disabling metrics for.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.no_such_monitoring_subscription.NoSuchMonitoringSubscription: <p>A monitoring subscription does not exist for the specified distribution.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_monitoring_subscription_request.DeleteMonitoringSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.delete_monitoring_subscription_result.DeleteMonitoringSubscriptionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_monitoring_subscription

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_monitoring_subscription.delete_monitoring_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_monitoring_subscription_request.DeleteMonitoringSubscriptionRequest = {
            "distribution_id": distribution_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_origin_access_control(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a CloudFront origin access control.</p> <p>You cannot delete an origin access control if it's in use. First, update all distributions to remove the origin access control from all origins, then delete the origin access control.</p>

        Args:
            id: <p>The unique identifier of the origin access control that you are deleting.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the origin access control that you are deleting.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_origin_access_control.NoSuchOriginAccessControl: <p>The origin access control does not exist.</p>
            capo_cloudfront.errors.origin_access_control_in_use.OriginAccessControlInUse: <p>Cannot delete the origin access control because it's in use by one or more distributions.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_origin_access_control_request.DeleteOriginAccessControlRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_origin_access_control

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_origin_access_control.delete_origin_access_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_origin_access_control_request.DeleteOriginAccessControlRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_origin_request_policy(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes an origin request policy.</p> <p>You cannot delete an origin request policy if it's attached to any cache behaviors. First update your distributions to remove the origin request policy from all cache behaviors, then delete the origin request policy.</p> <p>To delete an origin request policy, you must provide the policy's identifier and version. To get the identifier, you can use <code>ListOriginRequestPolicies</code> or <code>GetOriginRequestPolicy</code>.</p>

        Args:
            id: <p>The unique identifier for the origin request policy that you are deleting. To get the identifier, you can use <code>ListOriginRequestPolicies</code>.</p>
            if_match: <p>The version of the origin request policy that you are deleting. The version is the origin request policy's <code>ETag</code> value, which you can get using <code>ListOriginRequestPolicies</code>, <code>GetOriginRequestPolicy</code>, or <code>GetOriginRequestPolicyConfig</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.illegal_delete.IllegalDelete: <p>Deletion is not allowed for this entity.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy: <p>The origin request policy does not exist.</p>
            capo_cloudfront.errors.origin_request_policy_in_use.OriginRequestPolicyInUse: <p>Cannot delete the origin request policy because it is attached to one or more cache behaviors.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_origin_request_policy_request.DeleteOriginRequestPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_origin_request_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_origin_request_policy.delete_origin_request_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_origin_request_policy_request.DeleteOriginRequestPolicyRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_public_key(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Remove a public key you previously added to CloudFront.</p>

        Args:
            id: <p>The ID of the public key you want to remove from CloudFront.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the public key identity to delete. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_public_key.NoSuchPublicKey: <p>The specified public key doesn't exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.public_key_in_use.PublicKeyInUse: <p>The specified public key is in use.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_public_key_request.DeletePublicKeyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_public_key

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_public_key.delete_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_public_key_request.DeletePublicKeyRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_realtime_log_config(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        name: Optional["capo_cloudfront.types.string.string"] = None,
        arn: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a real-time log configuration.</p> <p>You cannot delete a real-time log configuration if it's attached to a cache behavior. First update your distributions to remove the real-time log configuration from all cache behaviors, then delete the real-time log configuration.</p> <p>To delete a real-time log configuration, you can provide the configuration's name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to delete.</p>

        Args:
            name: <p>The name of the real-time log configuration to delete.</p>
            arn: <p>The Amazon Resource Name (ARN) of the real-time log configuration to delete.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig: <p>The real-time log configuration does not exist.</p>
            capo_cloudfront.errors.realtime_log_config_in_use.RealtimeLogConfigInUse: <p>Cannot delete the real-time log configuration because it is attached to one or more cache behaviors.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_realtime_log_config_request.DeleteRealtimeLogConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_realtime_log_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_realtime_log_config.delete_realtime_log_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_realtime_log_config_request.DeleteRealtimeLogConfigRequest = {}
        if name is not None:
            input_["name"] = name
        if arn is not None:
            input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        resource_arn: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes the resource policy attached to the CloudFront resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudFront resource for which the resource policy should be deleted.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.illegal_delete.IllegalDelete: <p>Deletion is not allowed for this entity.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_resource_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_response_headers_policy(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Deletes a response headers policy.</p> <p>You cannot delete a response headers policy if it's attached to a cache behavior. First update your distributions to remove the response headers policy from all cache behaviors, then delete the response headers policy.</p> <p>To delete a response headers policy, you must provide the policy's identifier and version. To get these values, you can use <code>ListResponseHeadersPolicies</code> or <code>GetResponseHeadersPolicy</code>.</p>

        Args:
            id: <p>The identifier for the response headers policy that you are deleting.</p> <p>To get the identifier, you can use <code>ListResponseHeadersPolicies</code>.</p>
            if_match: <p>The version of the response headers policy that you are deleting.</p> <p>The version is the response headers policy's <code>ETag</code> value, which you can get using <code>ListResponseHeadersPolicies</code>, <code>GetResponseHeadersPolicy</code>, or <code>GetResponseHeadersPolicyConfig</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.illegal_delete.IllegalDelete: <p>Deletion is not allowed for this entity.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy: <p>The response headers policy does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.response_headers_policy_in_use.ResponseHeadersPolicyInUse: <p>Cannot delete the response headers policy because it is attached to one or more cache behaviors in a CloudFront distribution.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_response_headers_policy_request.DeleteResponseHeadersPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_response_headers_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_response_headers_policy.delete_response_headers_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_response_headers_policy_request.DeleteResponseHeadersPolicyRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_streaming_distribution(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> None:
        """<p>Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.</p> <p> <b>To delete an RTMP distribution using the CloudFront API</b>:</p> <ol> <li> <p>Disable the RTMP distribution.</p> </li> <li> <p>Submit a <code>GET Streaming Distribution Config</code> request to get the current configuration and the <code>Etag</code> header for the distribution. </p> </li> <li> <p>Update the XML document that was returned in the response to your <code>GET Streaming Distribution Config</code> request to change the value of <code>Enabled</code> to <code>false</code>.</p> </li> <li> <p>Submit a <code>PUT Streaming Distribution Config</code> request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP <code>If-Match</code> header to the value of the <code>ETag</code> header that CloudFront returned when you submitted the <code>GET Streaming Distribution Config</code> request in Step 2.</p> </li> <li> <p>Review the response to the <code>PUT Streaming Distribution Config</code> request to confirm that the distribution was successfully disabled.</p> </li> <li> <p>Submit a <code>GET Streaming Distribution Config</code> request to confirm that your changes have propagated. When propagation is complete, the value of <code>Status</code> is <code>Deployed</code>.</p> </li> <li> <p>Submit a <code>DELETE Streaming Distribution</code> request. Set the value of the HTTP <code>If-Match</code> header to the value of the <code>ETag</code> header that CloudFront returned when you submitted the <code>GET Streaming Distribution Config</code> request in Step 2.</p> </li> <li> <p>Review the response to your <code>DELETE Streaming Distribution</code> request to confirm that the distribution was successfully deleted.</p> </li> </ol> <p>For information about deleting a distribution using the CloudFront console, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html">Deleting a Distribution</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            id: <p>The distribution ID.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when you disabled the streaming distribution. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_streaming_distribution.NoSuchStreamingDistribution: <p>The specified streaming distribution does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.streaming_distribution_not_disabled.StreamingDistributionNotDisabled: <p>The specified CloudFront distribution is not disabled. You must disable the distribution before you can delete it.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_streaming_distribution_request.DeleteStreamingDistributionRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_streaming_distribution

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_streaming_distribution.delete_streaming_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_streaming_distribution_request.DeleteStreamingDistributionRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_trust_store(
        self,
        id: "capo_cloudfront.types.resource_id.ResourceId",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Deletes a trust store.</p>

        Args:
            id: <p>The trust store's ID.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the trust store you are deleting.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cannot_delete_entity_while_in_use.CannotDeleteEntityWhileInUse: <p>The entity cannot be deleted while it is in use.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_trust_store_request.DeleteTrustStoreRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_trust_store

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_trust_store.delete_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_trust_store_request.DeleteTrustStoreRequest = {
            "id": id,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vpc_origin(
        self,
        id: "capo_cloudfront.types.string.string",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.delete_vpc_origin_result.DeleteVpcOriginResult":
        """<p>Delete an Amazon CloudFront VPC origin.</p>

        Args:
            id: <p>The VPC origin ID.</p>
            if_match: <p>The version identifier of the VPC origin to delete. This is the <code>ETag</code> value returned in the response to <a>GetVpcOrigin</a>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cannot_delete_entity_while_in_use.CannotDeleteEntityWhileInUse: <p>The entity cannot be deleted while it is in use.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.illegal_delete.IllegalDelete: <p>Deletion is not allowed for this entity.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a VPC origin
            The following command deletes a VPC origin:

            >>> client.delete_vpc_origin(id='vo_BQwjxxQxjCaBcQLzJUFkDM', if_match='E1F83G8C2ARO7P')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.delete_vpc_origin_request.DeleteVpcOriginRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.delete_vpc_origin_result.DeleteVpcOriginResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.delete_vpc_origin

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.delete_vpc_origin.delete_vpc_origin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.delete_vpc_origin_request.DeleteVpcOriginRequest = {
            "id": id,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_connection_function(
        self,
        identifier: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["capo_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "capo_cloudfront.types.describe_connection_function_result.DescribeConnectionFunctionResult":
        """<p>Describes a connection function.</p>

        Args:
            identifier: <p>The connection function's identifier.</p>
            stage: <p>The connection function's stage.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.describe_connection_function_request.DescribeConnectionFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.describe_connection_function_result.DescribeConnectionFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.describe_connection_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.describe_connection_function.describe_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.describe_connection_function_request.DescribeConnectionFunctionRequest = {
            "identifier": identifier
        }
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_function(
        self,
        name: "capo_cloudfront.types.function_name.FunctionName",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["capo_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "capo_cloudfront.types.describe_function_result.DescribeFunctionResult":
        """<p>Gets configuration information and metadata about a CloudFront function, but not the function's code. To get a function's code, use <code>GetFunction</code>.</p> <p>To get configuration information and metadata about a function, you must provide the function's name and stage. To get these values, you can use <code>ListFunctions</code>.</p>

        Args:
            name: <p>The name of the function that you are getting information about.</p>
            stage: <p>The function's stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>

        Raises:
            capo_cloudfront.errors.no_such_function_exists.NoSuchFunctionExists: <p>The function does not exist.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.describe_function_request.DescribeFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.describe_function_result.DescribeFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.describe_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.describe_function.describe_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.describe_function_request.DescribeFunctionRequest = {
            "name": name
        }
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_key_value_store(
        self,
        name: "capo_cloudfront.types.key_value_store_name.KeyValueStoreName",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.describe_key_value_store_result.DescribeKeyValueStoreResult":
        """<p>Specifies the key value store and its configuration.</p>

        Args:
            name: <p>The name of the key value store.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a KeyValueStore
            Use the following command to describe a KeyValueStore.

            >>> client.describe_key_value_store(name='my-keyvaluestore-name')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.describe_key_value_store_request.DescribeKeyValueStoreRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.describe_key_value_store_result.DescribeKeyValueStoreResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.describe_key_value_store

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.describe_key_value_store.describe_key_value_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.describe_key_value_store_request.DescribeKeyValueStoreRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_distribution_tenant_web_acl(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.disassociate_distribution_tenant_web_acl_result.DisassociateDistributionTenantWebACLResult":
        """<p>Disassociates a distribution tenant from the WAF web ACL.</p>

        Args:
            id: <p>The ID of the distribution tenant.</p>
            if_match: <p>The current version of the distribution tenant that you're disassociating from the WAF web ACL. This is the <code>ETag</code> value returned in the response to the <code>GetDistributionTenant</code> API operation.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.disassociate_distribution_tenant_web_acl_request.DisassociateDistributionTenantWebACLRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.disassociate_distribution_tenant_web_acl_result.DisassociateDistributionTenantWebACLResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.disassociate_distribution_tenant_web_acl

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.disassociate_distribution_tenant_web_acl.disassociate_distribution_tenant_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.disassociate_distribution_tenant_web_acl_request.DisassociateDistributionTenantWebACLRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_distribution_web_acl(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.disassociate_distribution_web_acl_result.DisassociateDistributionWebACLResult":
        """<p>Disassociates a distribution from the WAF web ACL.</p>

        Args:
            id: <p>The ID of the distribution.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the distribution that you're disassociating from the WAF web ACL.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.disassociate_distribution_web_acl_request.DisassociateDistributionWebACLRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.disassociate_distribution_web_acl_result.DisassociateDistributionWebACLResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.disassociate_distribution_web_acl

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.disassociate_distribution_web_acl.disassociate_distribution_web_acl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.disassociate_distribution_web_acl_request.DisassociateDistributionWebACLRequest = {
            "id": id
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_anycast_ip_list(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_anycast_ip_list_result.GetAnycastIpListResult":
        """<p>Gets an Anycast static IP list.</p>

        Args:
            id: <p>The ID of the Anycast static IP list.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_anycast_ip_list_request.GetAnycastIpListRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_anycast_ip_list_result.GetAnycastIpListResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_anycast_ip_list

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_anycast_ip_list.get_anycast_ip_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_anycast_ip_list_request.GetAnycastIpListRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cache_policy(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_cache_policy_result.GetCachePolicyResult":
        """<p>Gets a cache policy, including the following metadata:</p> <ul> <li> <p>The policy's identifier.</p> </li> <li> <p>The date and time when the policy was last modified.</p> </li> </ul> <p>To get a cache policy, you must provide the policy's identifier. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.</p>

        Args:
            id: <p>The unique identifier for the cache policy. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy: <p>The cache policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_cache_policy_request.GetCachePolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_cache_policy_result.GetCachePolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_cache_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_cache_policy.get_cache_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_cache_policy_request.GetCachePolicyRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cache_policy_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_cache_policy_config_result.GetCachePolicyConfigResult":
        """<p>Gets a cache policy configuration.</p> <p>To get a cache policy configuration, you must provide the policy's identifier. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.</p>

        Args:
            id: <p>The unique identifier for the cache policy. If the cache policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the cache policy is not attached to a cache behavior, you can get the identifier using <code>ListCachePolicies</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy: <p>The cache policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_cache_policy_config_request.GetCachePolicyConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_cache_policy_config_result.GetCachePolicyConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_cache_policy_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_cache_policy_config.get_cache_policy_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_cache_policy_config_request.GetCachePolicyConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cloud_front_origin_access_identity(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_cloud_front_origin_access_identity_result.GetCloudFrontOriginAccessIdentityResult":
        """<p>Get the information about an origin access identity.</p>

        Args:
            id: <p>The identity's ID.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_cloud_front_origin_access_identity.NoSuchCloudFrontOriginAccessIdentity: <p>The specified origin access identity does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_cloud_front_origin_access_identity_request.GetCloudFrontOriginAccessIdentityRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_cloud_front_origin_access_identity_result.GetCloudFrontOriginAccessIdentityResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_cloud_front_origin_access_identity

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_cloud_front_origin_access_identity.get_cloud_front_origin_access_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_cloud_front_origin_access_identity_request.GetCloudFrontOriginAccessIdentityRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cloud_front_origin_access_identity_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_cloud_front_origin_access_identity_config_result.GetCloudFrontOriginAccessIdentityConfigResult":
        """<p>Get the configuration information about an origin access identity.</p>

        Args:
            id: <p>The identity's ID.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_cloud_front_origin_access_identity.NoSuchCloudFrontOriginAccessIdentity: <p>The specified origin access identity does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_cloud_front_origin_access_identity_config_request.GetCloudFrontOriginAccessIdentityConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_cloud_front_origin_access_identity_config_result.GetCloudFrontOriginAccessIdentityConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_cloud_front_origin_access_identity_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_cloud_front_origin_access_identity_config.get_cloud_front_origin_access_identity_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_cloud_front_origin_access_identity_config_request.GetCloudFrontOriginAccessIdentityConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_connection_function(
        self,
        identifier: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["capo_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "capo_cloudfront.types.get_connection_function_result.GetConnectionFunctionResult":
        """<p>Gets a connection function.</p>

        Args:
            identifier: <p>The connection function's identifier.</p>
            stage: <p>The connection function's stage.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_connection_function_request.GetConnectionFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_connection_function_result.GetConnectionFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_connection_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_connection_function.get_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_connection_function_request.GetConnectionFunctionRequest = {
            "identifier": identifier
        }
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_connection_group(
        self,
        identifier: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_connection_group_result.GetConnectionGroupResult":
        """<p>Gets information about a connection group.</p>

        Args:
            identifier: <p>The ID, name, or Amazon Resource Name (ARN) of the connection group.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_connection_group_request.GetConnectionGroupRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_connection_group_result.GetConnectionGroupResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_connection_group

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_connection_group.get_connection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_connection_group_request.GetConnectionGroupRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_connection_group_by_routing_endpoint(
        self,
        routing_endpoint: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_connection_group_by_routing_endpoint_result.GetConnectionGroupByRoutingEndpointResult":
        """<p>Gets information about a connection group by using the endpoint that you specify.</p>

        Args:
            routing_endpoint: <p>The routing endpoint for the target connection group, such as d111111abcdef8.cloudfront.net.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_connection_group_by_routing_endpoint_request.GetConnectionGroupByRoutingEndpointRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_connection_group_by_routing_endpoint_result.GetConnectionGroupByRoutingEndpointResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_connection_group_by_routing_endpoint

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_connection_group_by_routing_endpoint.get_connection_group_by_routing_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_connection_group_by_routing_endpoint_request.GetConnectionGroupByRoutingEndpointRequest = {
            "routing_endpoint": routing_endpoint
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_continuous_deployment_policy(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_continuous_deployment_policy_result.GetContinuousDeploymentPolicyResult":
        """<p>Gets a continuous deployment policy, including metadata (the policy's identifier and the date and time when the policy was last modified).</p>

        Args:
            id: <p>The identifier of the continuous deployment policy that you are getting.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_continuous_deployment_policy.NoSuchContinuousDeploymentPolicy: <p>The continuous deployment policy doesn't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_continuous_deployment_policy_request.GetContinuousDeploymentPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_continuous_deployment_policy_result.GetContinuousDeploymentPolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_continuous_deployment_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_continuous_deployment_policy.get_continuous_deployment_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_continuous_deployment_policy_request.GetContinuousDeploymentPolicyRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_continuous_deployment_policy_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_continuous_deployment_policy_config_result.GetContinuousDeploymentPolicyConfigResult":
        """<p>Gets configuration information about a continuous deployment policy.</p>

        Args:
            id: <p>The identifier of the continuous deployment policy whose configuration you are getting.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_continuous_deployment_policy.NoSuchContinuousDeploymentPolicy: <p>The continuous deployment policy doesn't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_continuous_deployment_policy_config_request.GetContinuousDeploymentPolicyConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_continuous_deployment_policy_config_result.GetContinuousDeploymentPolicyConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_continuous_deployment_policy_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_continuous_deployment_policy_config.get_continuous_deployment_policy_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_continuous_deployment_policy_config_request.GetContinuousDeploymentPolicyConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_distribution(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_distribution_result.GetDistributionResult":
        """<p>Get the information about a distribution.</p>

        Args:
            id: <p>The distribution's ID. If the ID is empty, an empty distribution configuration is returned.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_distribution_request.GetDistributionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_distribution_result.GetDistributionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_distribution

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_distribution.get_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_distribution_request.GetDistributionRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_distribution_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_distribution_config_result.GetDistributionConfigResult":
        """<p>Get the configuration information about a distribution.</p>

        Args:
            id: <p>The distribution's ID. If the ID is empty, an empty distribution configuration is returned.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_distribution_config_request.GetDistributionConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_distribution_config_result.GetDistributionConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_distribution_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_distribution_config.get_distribution_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_distribution_config_request.GetDistributionConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_distribution_tenant(
        self,
        identifier: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_distribution_tenant_result.GetDistributionTenantResult":
        """<p>Gets information about a distribution tenant.</p>

        Args:
            identifier: <p>The identifier of the distribution tenant. You can specify the ARN, ID, or name of the distribution tenant.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_distribution_tenant_request.GetDistributionTenantRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_distribution_tenant_result.GetDistributionTenantResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_distribution_tenant

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_distribution_tenant.get_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_distribution_tenant_request.GetDistributionTenantRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_distribution_tenant_by_domain(
        self,
        domain: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_distribution_tenant_by_domain_result.GetDistributionTenantByDomainResult":
        """<p>Gets information about a distribution tenant by the associated domain.</p>

        Args:
            domain: <p>A domain name associated with the target distribution tenant.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_distribution_tenant_by_domain_request.GetDistributionTenantByDomainRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_distribution_tenant_by_domain_result.GetDistributionTenantByDomainResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_distribution_tenant_by_domain

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_distribution_tenant_by_domain.get_distribution_tenant_by_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_distribution_tenant_by_domain_request.GetDistributionTenantByDomainRequest = {
            "domain": domain
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_field_level_encryption(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_field_level_encryption_result.GetFieldLevelEncryptionResult":
        """<p>Get the field-level encryption configuration information.</p>

        Args:
            id: <p>Request the ID for the field-level encryption configuration information.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig: <p>The specified configuration for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_field_level_encryption_request.GetFieldLevelEncryptionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_field_level_encryption_result.GetFieldLevelEncryptionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption.get_field_level_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_field_level_encryption_request.GetFieldLevelEncryptionRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_field_level_encryption_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_field_level_encryption_config_result.GetFieldLevelEncryptionConfigResult":
        """<p>Get the field-level encryption configuration information.</p>

        Args:
            id: <p>Request the ID for the field-level encryption configuration information.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig: <p>The specified configuration for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_field_level_encryption_config_request.GetFieldLevelEncryptionConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_field_level_encryption_config_result.GetFieldLevelEncryptionConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_config.get_field_level_encryption_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_field_level_encryption_config_request.GetFieldLevelEncryptionConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_field_level_encryption_profile(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_field_level_encryption_profile_result.GetFieldLevelEncryptionProfileResult":
        """<p>Get the field-level encryption profile information.</p>

        Args:
            id: <p>Get the ID for the field-level encryption profile information.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_profile.NoSuchFieldLevelEncryptionProfile: <p>The specified profile for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_field_level_encryption_profile_request.GetFieldLevelEncryptionProfileRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_field_level_encryption_profile_result.GetFieldLevelEncryptionProfileResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_profile

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_profile.get_field_level_encryption_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_field_level_encryption_profile_request.GetFieldLevelEncryptionProfileRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_field_level_encryption_profile_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_field_level_encryption_profile_config_result.GetFieldLevelEncryptionProfileConfigResult":
        """<p>Get the field-level encryption profile configuration information.</p>

        Args:
            id: <p>Get the ID for the field-level encryption profile configuration information.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_profile.NoSuchFieldLevelEncryptionProfile: <p>The specified profile for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_field_level_encryption_profile_config_request.GetFieldLevelEncryptionProfileConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_field_level_encryption_profile_config_result.GetFieldLevelEncryptionProfileConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_profile_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_field_level_encryption_profile_config.get_field_level_encryption_profile_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_field_level_encryption_profile_config_request.GetFieldLevelEncryptionProfileConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function(
        self,
        name: "capo_cloudfront.types.function_name.FunctionName",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["capo_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "capo_cloudfront.types.get_function_result.GetFunctionResult":
        """<p>Gets the code of a CloudFront function. To get configuration information and metadata about a function, use <code>DescribeFunction</code>.</p> <p>To get a function's code, you must provide the function's name and stage. To get these values, you can use <code>ListFunctions</code>.</p>

        Args:
            name: <p>The name of the function whose code you are getting.</p>
            stage: <p>The function's stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>

        Raises:
            capo_cloudfront.errors.no_such_function_exists.NoSuchFunctionExists: <p>The function does not exist.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_function_request.GetFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_function_result.GetFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_function.get_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_function_request.GetFunctionRequest = {
            "name": name
        }
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_invalidation(
        self,
        distribution_id: "capo_cloudfront.types.string.string",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_invalidation_result.GetInvalidationResult":
        """<p>Get the information about an invalidation.</p>

        Args:
            distribution_id: <p>The distribution's ID.</p>
            id: <p>The identifier for the invalidation request, for example, <code>IDFDVBD632BHDS5</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.no_such_invalidation.NoSuchInvalidation: <p>The specified invalidation does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_invalidation_request.GetInvalidationRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_invalidation_result.GetInvalidationResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_invalidation

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_invalidation.get_invalidation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_invalidation_request.GetInvalidationRequest = {
            "distribution_id": distribution_id,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_invalidation_for_distribution_tenant(
        self,
        distribution_tenant_id: "capo_cloudfront.types.string.string",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_invalidation_for_distribution_tenant_result.GetInvalidationForDistributionTenantResult":
        """<p>Gets information about a specific invalidation for a distribution tenant.</p>

        Args:
            distribution_tenant_id: <p>The ID of the distribution tenant.</p>
            id: <p>The ID of the invalidation to retrieve.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.no_such_invalidation.NoSuchInvalidation: <p>The specified invalidation does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_invalidation_for_distribution_tenant_request.GetInvalidationForDistributionTenantRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_invalidation_for_distribution_tenant_result.GetInvalidationForDistributionTenantResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_invalidation_for_distribution_tenant

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_invalidation_for_distribution_tenant.get_invalidation_for_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_invalidation_for_distribution_tenant_request.GetInvalidationForDistributionTenantRequest = {
            "distribution_tenant_id": distribution_tenant_id,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_key_group(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_key_group_result.GetKeyGroupResult":
        """<p>Gets a key group, including the date and time when the key group was last modified.</p> <p>To get a key group, you must provide the key group's identifier. If the key group is referenced in a distribution's cache behavior, you can get the key group's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the key group is not referenced in a cache behavior, you can get the identifier using <code>ListKeyGroups</code>.</p>

        Args:
            id: <p>The identifier of the key group that you are getting. To get the identifier, use <code>ListKeyGroups</code>.</p>

        Raises:
            capo_cloudfront.errors.no_such_resource.NoSuchResource: <p>A resource that was specified is not valid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_key_group_request.GetKeyGroupRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_key_group_result.GetKeyGroupResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_key_group

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_key_group.get_key_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_key_group_request.GetKeyGroupRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_key_group_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_key_group_config_result.GetKeyGroupConfigResult":
        """<p>Gets a key group configuration.</p> <p>To get a key group configuration, you must provide the key group's identifier. If the key group is referenced in a distribution's cache behavior, you can get the key group's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the key group is not referenced in a cache behavior, you can get the identifier using <code>ListKeyGroups</code>.</p>

        Args:
            id: <p>The identifier of the key group whose configuration you are getting. To get the identifier, use <code>ListKeyGroups</code>.</p>

        Raises:
            capo_cloudfront.errors.no_such_resource.NoSuchResource: <p>A resource that was specified is not valid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_key_group_config_request.GetKeyGroupConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_key_group_config_result.GetKeyGroupConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_key_group_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_key_group_config.get_key_group_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_key_group_config_request.GetKeyGroupConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_managed_certificate_details(
        self,
        identifier: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_managed_certificate_details_result.GetManagedCertificateDetailsResult":
        """<p>Gets details about the CloudFront managed ACM certificate.</p>

        Args:
            identifier: <p>The identifier of the distribution tenant. You can specify the ARN, ID, or name of the distribution tenant.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_managed_certificate_details_request.GetManagedCertificateDetailsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_managed_certificate_details_result.GetManagedCertificateDetailsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_managed_certificate_details

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_managed_certificate_details.get_managed_certificate_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_managed_certificate_details_request.GetManagedCertificateDetailsRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_monitoring_subscription(
        self,
        distribution_id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_monitoring_subscription_result.GetMonitoringSubscriptionResult":
        """<p>Gets information about whether additional CloudWatch metrics are enabled for the specified CloudFront distribution.</p>

        Args:
            distribution_id: <p>The ID of the distribution that you are getting metrics information for.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.no_such_monitoring_subscription.NoSuchMonitoringSubscription: <p>A monitoring subscription does not exist for the specified distribution.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_monitoring_subscription_request.GetMonitoringSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_monitoring_subscription_result.GetMonitoringSubscriptionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_monitoring_subscription

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_monitoring_subscription.get_monitoring_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_monitoring_subscription_request.GetMonitoringSubscriptionRequest = {
            "distribution_id": distribution_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_origin_access_control(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_origin_access_control_result.GetOriginAccessControlResult":
        """<p>Gets a CloudFront origin access control, including its unique identifier.</p>

        Args:
            id: <p>The unique identifier of the origin access control.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_origin_access_control.NoSuchOriginAccessControl: <p>The origin access control does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_origin_access_control_request.GetOriginAccessControlRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_origin_access_control_result.GetOriginAccessControlResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_origin_access_control

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_origin_access_control.get_origin_access_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_origin_access_control_request.GetOriginAccessControlRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_origin_access_control_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_origin_access_control_config_result.GetOriginAccessControlConfigResult":
        """<p>Gets a CloudFront origin access control configuration.</p>

        Args:
            id: <p>The unique identifier of the origin access control.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_origin_access_control.NoSuchOriginAccessControl: <p>The origin access control does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_origin_access_control_config_request.GetOriginAccessControlConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_origin_access_control_config_result.GetOriginAccessControlConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_origin_access_control_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_origin_access_control_config.get_origin_access_control_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_origin_access_control_config_request.GetOriginAccessControlConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_origin_request_policy(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_origin_request_policy_result.GetOriginRequestPolicyResult":
        """<p>Gets an origin request policy, including the following metadata:</p> <ul> <li> <p>The policy's identifier.</p> </li> <li> <p>The date and time when the policy was last modified.</p> </li> </ul> <p>To get an origin request policy, you must provide the policy's identifier. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.</p>

        Args:
            id: <p>The unique identifier for the origin request policy. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy: <p>The origin request policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_origin_request_policy_request.GetOriginRequestPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_origin_request_policy_result.GetOriginRequestPolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_origin_request_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_origin_request_policy.get_origin_request_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_origin_request_policy_request.GetOriginRequestPolicyRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_origin_request_policy_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_origin_request_policy_config_result.GetOriginRequestPolicyConfigResult":
        """<p>Gets an origin request policy configuration.</p> <p>To get an origin request policy configuration, you must provide the policy's identifier. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.</p>

        Args:
            id: <p>The unique identifier for the origin request policy. If the origin request policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the origin request policy is not attached to a cache behavior, you can get the identifier using <code>ListOriginRequestPolicies</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy: <p>The origin request policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_origin_request_policy_config_request.GetOriginRequestPolicyConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_origin_request_policy_config_result.GetOriginRequestPolicyConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_origin_request_policy_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_origin_request_policy_config.get_origin_request_policy_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_origin_request_policy_config_request.GetOriginRequestPolicyConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_public_key(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_public_key_result.GetPublicKeyResult":
        """<p>Gets a public key.</p>

        Args:
            id: <p>The identifier of the public key you are getting.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_public_key.NoSuchPublicKey: <p>The specified public key doesn't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_public_key_request.GetPublicKeyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_public_key_result.GetPublicKeyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_public_key

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_public_key.get_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_public_key_request.GetPublicKeyRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_public_key_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_public_key_config_result.GetPublicKeyConfigResult":
        """<p>Gets a public key configuration.</p>

        Args:
            id: <p>The identifier of the public key whose configuration you are getting.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_public_key.NoSuchPublicKey: <p>The specified public key doesn't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_public_key_config_request.GetPublicKeyConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_public_key_config_result.GetPublicKeyConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_public_key_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_public_key_config.get_public_key_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_public_key_config_request.GetPublicKeyConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_realtime_log_config(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        name: Optional["capo_cloudfront.types.string.string"] = None,
        arn: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.get_realtime_log_config_result.GetRealtimeLogConfigResult":
        """<p>Gets a real-time log configuration.</p> <p>To get a real-time log configuration, you can provide the configuration's name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to get.</p>

        Args:
            name: <p>The name of the real-time log configuration to get.</p>
            arn: <p>The Amazon Resource Name (ARN) of the real-time log configuration to get.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig: <p>The real-time log configuration does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_realtime_log_config_request.GetRealtimeLogConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_realtime_log_config_result.GetRealtimeLogConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_realtime_log_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_realtime_log_config.get_realtime_log_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_realtime_log_config_request.GetRealtimeLogConfigRequest = {}
        if name is not None:
            input_["name"] = name
        if arn is not None:
            input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_resource_policy_result.GetResourcePolicyResult":
        """<p>Retrieves the resource policy for the specified CloudFront resource that you own and have shared.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudFront resource that is associated with the resource policy.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_resource_policy_result.GetResourcePolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_resource_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_response_headers_policy(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_response_headers_policy_result.GetResponseHeadersPolicyResult":
        """<p>Gets a response headers policy, including metadata (the policy's identifier and the date and time when the policy was last modified).</p> <p>To get a response headers policy, you must provide the policy's identifier. If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>

        Args:
            id: <p>The identifier for the response headers policy.</p> <p>If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy: <p>The response headers policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_response_headers_policy_request.GetResponseHeadersPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_response_headers_policy_result.GetResponseHeadersPolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_response_headers_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_response_headers_policy.get_response_headers_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_response_headers_policy_request.GetResponseHeadersPolicyRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_response_headers_policy_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_response_headers_policy_config_result.GetResponseHeadersPolicyConfigResult":
        """<p>Gets a response headers policy configuration.</p> <p>To get a response headers policy configuration, you must provide the policy's identifier. If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>

        Args:
            id: <p>The identifier for the response headers policy.</p> <p>If the response headers policy is attached to a distribution's cache behavior, you can get the policy's identifier using <code>ListDistributions</code> or <code>GetDistribution</code>. If the response headers policy is not attached to a cache behavior, you can get the identifier using <code>ListResponseHeadersPolicies</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy: <p>The response headers policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_response_headers_policy_config_request.GetResponseHeadersPolicyConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_response_headers_policy_config_result.GetResponseHeadersPolicyConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_response_headers_policy_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_response_headers_policy_config.get_response_headers_policy_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_response_headers_policy_config_request.GetResponseHeadersPolicyConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_streaming_distribution(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_streaming_distribution_result.GetStreamingDistributionResult":
        """<p>Gets information about a specified RTMP distribution, including the distribution configuration.</p>

        Args:
            id: <p>The streaming distribution's ID.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_streaming_distribution.NoSuchStreamingDistribution: <p>The specified streaming distribution does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_streaming_distribution_request.GetStreamingDistributionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_streaming_distribution_result.GetStreamingDistributionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_streaming_distribution

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_streaming_distribution.get_streaming_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_streaming_distribution_request.GetStreamingDistributionRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_streaming_distribution_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_streaming_distribution_config_result.GetStreamingDistributionConfigResult":
        """<p>Get the configuration information about a streaming distribution.</p>

        Args:
            id: <p>The streaming distribution's ID.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.no_such_streaming_distribution.NoSuchStreamingDistribution: <p>The specified streaming distribution does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_streaming_distribution_config_request.GetStreamingDistributionConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_streaming_distribution_config_result.GetStreamingDistributionConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_streaming_distribution_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_streaming_distribution_config.get_streaming_distribution_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_streaming_distribution_config_request.GetStreamingDistributionConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_trust_store(
        self,
        identifier: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_trust_store_result.GetTrustStoreResult":
        """<p>Gets a trust store.</p>

        Args:
            identifier: <p>The trust store's identifier.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_trust_store_request.GetTrustStoreRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_trust_store_result.GetTrustStoreResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_trust_store

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_trust_store.get_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_trust_store_request.GetTrustStoreRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_vpc_origin(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.get_vpc_origin_result.GetVpcOriginResult":
        """<p>Get the details of an Amazon CloudFront VPC origin.</p>

        Args:
            id: <p>The VPC origin ID.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a VPC origin
            The following command gets a VPC origin:

            >>> client.get_vpc_origin(id='vo_BQwjxxQxjCaBcQLzJUFkDM')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.get_vpc_origin_request.GetVpcOriginRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.get_vpc_origin_result.GetVpcOriginResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.get_vpc_origin

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.get_vpc_origin.get_vpc_origin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.get_vpc_origin_request.GetVpcOriginRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_anycast_ip_lists(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_anycast_ip_lists_result.ListAnycastIpListsResult":
        """<p>Lists your Anycast static IP lists.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of Anycast static IP lists that you want returned in the response.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_anycast_ip_lists_request.ListAnycastIpListsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_anycast_ip_lists_result.ListAnycastIpListsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_anycast_ip_lists

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_anycast_ip_lists.list_anycast_ip_lists(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_anycast_ip_lists_request.ListAnycastIpListsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_cache_policies(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        type: Optional[
            "capo_cloudfront.types.cache_policy_type.CachePolicyType"
        ] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_cache_policies_result.ListCachePoliciesResult":
        """<p>Gets a list of cache policies.</p> <p>You can optionally apply a filter to return only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            type: <p>A filter to return only the specified kinds of cache policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Returns only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Returns only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
            marker: <p>Use this field when paginating results to indicate where to begin in your list of cache policies. The response includes cache policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of cache policies that you want in the response.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy: <p>The cache policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_cache_policies_request.ListCachePoliciesRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_cache_policies_result.ListCachePoliciesResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_cache_policies

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_cache_policies.list_cache_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_cache_policies_request.ListCachePoliciesRequest = {}
        if type is not None:
            input_["type"] = type
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_cloud_front_origin_access_identities(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_cloud_front_origin_access_identities_result.ListCloudFrontOriginAccessIdentitiesResult":
        """<p>Lists origin access identities.</p>

        Args:
            marker: <p>Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last identity on that page).</p>
            max_items: <p>The maximum number of origin access identities you want in the response body.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_cloud_front_origin_access_identities_request.ListCloudFrontOriginAccessIdentitiesRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_cloud_front_origin_access_identities_result.ListCloudFrontOriginAccessIdentitiesResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_cloud_front_origin_access_identities

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_cloud_front_origin_access_identities.list_cloud_front_origin_access_identities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_cloud_front_origin_access_identities_request.ListCloudFrontOriginAccessIdentitiesRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_cloud_front_origin_access_identities(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.cloud_front_origin_access_identity_summary.CloudFrontOriginAccessIdentitySummary]":
        _token = marker
        while True:
            _response = self.list_cloud_front_origin_access_identities(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(
                _response, ("cloud_front_origin_access_identity_list", "items")
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(
                _response, ("cloud_front_origin_access_identity_list", "next_marker")
            )
            if not _token:
                break

    def list_conflicting_aliases(
        self,
        distribution_id: "capo_cloudfront.types.distribution_id_string.distributionIdString",
        alias: "capo_cloudfront.types.alias_string.aliasString",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional[
            "capo_cloudfront.types.list_conflicting_aliases_max_items_integer.listConflictingAliasesMaxItemsInteger"
        ] = None,
    ) -> "capo_cloudfront.types.list_conflicting_aliases_result.ListConflictingAliasesResult":
        """<note> <p>The <code>ListConflictingAliases</code> API operation only supports standard distributions. To list domain conflicts for both standard distributions and distribution tenants, we recommend that you use the <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDomainConflicts.html">ListDomainConflicts</a> API operation instead.</p> </note> <p>Gets a list of aliases that conflict or overlap with the provided alias, and the associated CloudFront standard distribution and Amazon Web Services accounts for each conflicting alias. An alias is commonly known as a custom domain or vanity domain. It can also be called a CNAME or alternate domain name.</p> <p>In the returned list, the standard distribution and account IDs are partially hidden, which allows you to identify the standard distribution and accounts that you own, and helps to protect the information of ones that you don't own.</p> <p>Use this operation to find aliases that are in use in CloudFront that conflict or overlap with the provided alias. For example, if you provide <code>www.example.com</code> as input, the returned list can include <code>www.example.com</code> and the overlapping wildcard alternate domain name (<code>*.example.com</code>), if they exist. If you provide <code>*.example.com</code> as input, the returned list can include <code>*.example.com</code> and any alternate domain names covered by that wildcard (for example, <code>www.example.com</code>, <code>test.example.com</code>, <code>dev.example.com</code>, and so on), if they exist.</p> <p>To list conflicting aliases, specify the alias to search and the ID of a standard distribution in your account that has an attached TLS certificate that includes the provided alias. For more information, including how to set up the standard distribution and certificate, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move">Moving an alternate domain name to a different standard distribution or distribution tenant</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            distribution_id: <p>The ID of a standard distribution in your account that has an attached TLS certificate that includes the provided alias.</p>
            alias: <p>The alias (also called a CNAME) to search for conflicting aliases.</p>
            marker: <p>Use this field when paginating results to indicate where to begin in the list of conflicting aliases. The response includes conflicting aliases in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of conflicting aliases that you want in the response.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_conflicting_aliases_request.ListConflictingAliasesRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_conflicting_aliases_result.ListConflictingAliasesResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_conflicting_aliases

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_conflicting_aliases.list_conflicting_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_conflicting_aliases_request.ListConflictingAliasesRequest = {
            "distribution_id": distribution_id,
            "alias": alias,
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_connection_functions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
        stage: Optional["capo_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "capo_cloudfront.types.list_connection_functions_result.ListConnectionFunctionsResult":
        """<p>Lists connection functions.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of connection functions that you want returned in the response.</p>
            stage: <p>The connection function's stage.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_connection_functions_request.ListConnectionFunctionsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_connection_functions_result.ListConnectionFunctionsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_connection_functions

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_connection_functions.list_connection_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_connection_functions_request.ListConnectionFunctionsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_connection_functions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
        stage: Optional["capo_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "Iterator[capo_cloudfront.types.connection_function_summary.ConnectionFunctionSummary]":
        _token = marker
        while True:
            _response = self.list_connection_functions(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
                stage=stage,
            )
            _page = _resolve_path(_response, ("connection_functions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_connection_groups(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        association_filter: Optional[
            "capo_cloudfront.types.connection_group_association_filter.ConnectionGroupAssociationFilter"
        ] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> (
        "capo_cloudfront.types.list_connection_groups_result.ListConnectionGroupsResult"
    ):
        """<p>Lists the connection groups in your Amazon Web Services account.</p>

        Args:
            association_filter: <p>Filter by associated Anycast IP list ID.</p>
            marker: <p>The marker for the next set of connection groups to retrieve.</p>
            max_items: <p>The maximum number of connection groups to return.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_connection_groups_request.ListConnectionGroupsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_connection_groups_result.ListConnectionGroupsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_connection_groups

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_connection_groups.list_connection_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_connection_groups_request.ListConnectionGroupsRequest = {}
        if association_filter is not None:
            input_["association_filter"] = association_filter
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_connection_groups(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        association_filter: Optional[
            "capo_cloudfront.types.connection_group_association_filter.ConnectionGroupAssociationFilter"
        ] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.connection_group_summary.ConnectionGroupSummary]":
        _token = marker
        while True:
            _response = self.list_connection_groups(
                config_overrides=config_overrides,
                association_filter=association_filter,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("connection_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_continuous_deployment_policies(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_continuous_deployment_policies_result.ListContinuousDeploymentPoliciesResult":
        """<p>Gets a list of the continuous deployment policies in your Amazon Web Services account.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of continuous deployment policies. The response includes policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of continuous deployment policies that you want returned in the response.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_continuous_deployment_policy.NoSuchContinuousDeploymentPolicy: <p>The continuous deployment policy doesn't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_continuous_deployment_policies_request.ListContinuousDeploymentPoliciesRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_continuous_deployment_policies_result.ListContinuousDeploymentPoliciesResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_continuous_deployment_policies

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_continuous_deployment_policies.list_continuous_deployment_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_continuous_deployment_policies_request.ListContinuousDeploymentPoliciesRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_distributions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_result.ListDistributionsResult":
        """<p>List CloudFront distributions.</p>

        Args:
            marker: <p>Use this when paginating results to indicate where to begin in your list of distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last distribution on that page).</p>
            max_items: <p>The maximum number of distributions you want in the response body.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_request.ListDistributionsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_result.ListDistributionsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions.list_distributions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_request.ListDistributionsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_distributions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.distribution_summary.DistributionSummary]":
        _token = marker
        while True:
            _response = self.list_distributions(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("distribution_list", "next_marker"))
            if not _token:
                break

    def list_distributions_by_anycast_ip_list_id(
        self,
        anycast_ip_list_id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_anycast_ip_list_id_result.ListDistributionsByAnycastIpListIdResult":
        """<p>Lists the distributions in your account that are associated with the specified <code>AnycastIpListId</code>.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distributions that you want returned in the response.</p>
            anycast_ip_list_id: <p>The ID of the Anycast static IP list.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_anycast_ip_list_id_request.ListDistributionsByAnycastIpListIdRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_anycast_ip_list_id_result.ListDistributionsByAnycastIpListIdResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_anycast_ip_list_id

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_anycast_ip_list_id.list_distributions_by_anycast_ip_list_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_anycast_ip_list_id_request.ListDistributionsByAnycastIpListIdRequest = {
            "anycast_ip_list_id": anycast_ip_list_id
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_distributions_by_cache_policy_id(
        self,
        cache_policy_id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_cache_policy_id_result.ListDistributionsByCachePolicyIdResult":
        """<p>Gets a list of distribution IDs for distributions that have a cache behavior that's associated with the specified cache policy.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distribution IDs that you want in the response.</p>
            cache_policy_id: <p>The ID of the cache policy whose associated distribution IDs you want to list.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy: <p>The cache policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_cache_policy_id_request.ListDistributionsByCachePolicyIdRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_cache_policy_id_result.ListDistributionsByCachePolicyIdResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_cache_policy_id

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_cache_policy_id.list_distributions_by_cache_policy_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_cache_policy_id_request.ListDistributionsByCachePolicyIdRequest = {
            "cache_policy_id": cache_policy_id
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_distributions_by_connection_function(
        self,
        connection_function_identifier: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_connection_function_result.ListDistributionsByConnectionFunctionResult":
        """<p>Lists distributions by connection function.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distributions that you want returned in the response.</p>
            connection_function_identifier: <p>The distributions by connection function identifier.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_connection_function_request.ListDistributionsByConnectionFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_connection_function_result.ListDistributionsByConnectionFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_connection_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_connection_function.list_distributions_by_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_connection_function_request.ListDistributionsByConnectionFunctionRequest = {
            "connection_function_identifier": connection_function_identifier
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_distributions_by_connection_function(
        self,
        connection_function_identifier: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.distribution_summary.DistributionSummary]":
        _token = marker
        while True:
            _response = self.list_distributions_by_connection_function(
                connection_function_identifier,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("distribution_list", "next_marker"))
            if not _token:
                break

    def list_distributions_by_connection_mode(
        self,
        connection_mode: "capo_cloudfront.types.connection_mode.ConnectionMode",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_connection_mode_result.ListDistributionsByConnectionModeResult":
        """<p>Lists the distributions by the connection mode that you specify.</p>

        Args:
            marker: <p> The marker for the next set of distributions to retrieve.</p>
            max_items: <p>The maximum number of distributions to return.</p>
            connection_mode: <p>This field specifies whether the connection mode is through a standard distribution (direct) or a multi-tenant distribution with distribution tenants (tenant-only).</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_connection_mode_request.ListDistributionsByConnectionModeRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_connection_mode_result.ListDistributionsByConnectionModeResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_connection_mode

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_connection_mode.list_distributions_by_connection_mode(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_connection_mode_request.ListDistributionsByConnectionModeRequest = {
            "connection_mode": connection_mode
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_distributions_by_connection_mode(
        self,
        connection_mode: "capo_cloudfront.types.connection_mode.ConnectionMode",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.distribution_summary.DistributionSummary]":
        _token = marker
        while True:
            _response = self.list_distributions_by_connection_mode(
                connection_mode,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("distribution_list", "next_marker"))
            if not _token:
                break

    def list_distributions_by_key_group(
        self,
        key_group_id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_key_group_result.ListDistributionsByKeyGroupResult":
        """<p>Gets a list of distribution IDs for distributions that have a cache behavior that references the specified key group.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distribution IDs that you want in the response.</p>
            key_group_id: <p>The ID of the key group whose associated distribution IDs you are listing.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_resource.NoSuchResource: <p>A resource that was specified is not valid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_key_group_request.ListDistributionsByKeyGroupRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_key_group_result.ListDistributionsByKeyGroupResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_key_group

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_key_group.list_distributions_by_key_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_key_group_request.ListDistributionsByKeyGroupRequest = {
            "key_group_id": key_group_id
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_distributions_by_origin_request_policy_id(
        self,
        origin_request_policy_id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_origin_request_policy_id_result.ListDistributionsByOriginRequestPolicyIdResult":
        """<p>Gets a list of distribution IDs for distributions that have a cache behavior that's associated with the specified origin request policy.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distribution IDs that you want in the response.</p>
            origin_request_policy_id: <p>The ID of the origin request policy whose associated distribution IDs you want to list.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy: <p>The origin request policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_origin_request_policy_id_request.ListDistributionsByOriginRequestPolicyIdRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_origin_request_policy_id_result.ListDistributionsByOriginRequestPolicyIdResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_origin_request_policy_id

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_origin_request_policy_id.list_distributions_by_origin_request_policy_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_origin_request_policy_id_request.ListDistributionsByOriginRequestPolicyIdRequest = {
            "origin_request_policy_id": origin_request_policy_id
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_distributions_by_owned_resource(
        self,
        resource_arn: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_owned_resource_result.ListDistributionsByOwnedResourceResult":
        """<p>Lists the CloudFront distributions that are associated with the specified resource that you own.</p>

        Args:
            resource_arn: <p>The ARN of the CloudFront resource that you've shared with other Amazon Web Services accounts.</p>
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distributions. The response includes distributions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distributions to return.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_owned_resource_request.ListDistributionsByOwnedResourceRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_owned_resource_result.ListDistributionsByOwnedResourceResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_owned_resource

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_owned_resource.list_distributions_by_owned_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_owned_resource_request.ListDistributionsByOwnedResourceRequest = {
            "resource_arn": resource_arn
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_distributions_by_realtime_log_config(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
        realtime_log_config_name: Optional[
            "capo_cloudfront.types.string.string"
        ] = None,
        realtime_log_config_arn: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_realtime_log_config_result.ListDistributionsByRealtimeLogConfigResult":
        """<p>Gets a list of distributions that have a cache behavior that's associated with the specified real-time log configuration.</p> <p>You can specify the real-time log configuration by its name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to list distributions for.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distributions. The response includes distributions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distributions that you want in the response.</p>
            realtime_log_config_name: <p>The name of the real-time log configuration whose associated distributions you want to list.</p>
            realtime_log_config_arn: <p>The Amazon Resource Name (ARN) of the real-time log configuration whose associated distributions you want to list.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_realtime_log_config_request.ListDistributionsByRealtimeLogConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_realtime_log_config_result.ListDistributionsByRealtimeLogConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_realtime_log_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_realtime_log_config.list_distributions_by_realtime_log_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_realtime_log_config_request.ListDistributionsByRealtimeLogConfigRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        if realtime_log_config_name is not None:
            input_["realtime_log_config_name"] = realtime_log_config_name
        if realtime_log_config_arn is not None:
            input_["realtime_log_config_arn"] = realtime_log_config_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_distributions_by_response_headers_policy_id(
        self,
        response_headers_policy_id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_response_headers_policy_id_result.ListDistributionsByResponseHeadersPolicyIdResult":
        """<p>Gets a list of distribution IDs for distributions that have a cache behavior that's associated with the specified response headers policy.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distribution IDs that you want to get in the response.</p>
            response_headers_policy_id: <p>The ID of the response headers policy whose associated distribution IDs you want to list.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy: <p>The response headers policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_response_headers_policy_id_request.ListDistributionsByResponseHeadersPolicyIdRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_response_headers_policy_id_result.ListDistributionsByResponseHeadersPolicyIdResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_response_headers_policy_id

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_response_headers_policy_id.list_distributions_by_response_headers_policy_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_response_headers_policy_id_request.ListDistributionsByResponseHeadersPolicyIdRequest = {
            "response_headers_policy_id": response_headers_policy_id
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_distributions_by_trust_store(
        self,
        trust_store_identifier: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_trust_store_result.ListDistributionsByTrustStoreResult":
        """<p>Lists distributions by trust store.</p>

        Args:
            trust_store_identifier: <p>The distributions by trust store identifier.</p>
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of distributions that you want returned in the response.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_trust_store_request.ListDistributionsByTrustStoreRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_trust_store_result.ListDistributionsByTrustStoreResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_trust_store

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_trust_store.list_distributions_by_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_trust_store_request.ListDistributionsByTrustStoreRequest = {
            "trust_store_identifier": trust_store_identifier
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_distributions_by_trust_store(
        self,
        trust_store_identifier: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.distribution_summary.DistributionSummary]":
        _token = marker
        while True:
            _response = self.list_distributions_by_trust_store(
                trust_store_identifier,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("distribution_list", "next_marker"))
            if not _token:
                break

    def list_distributions_by_vpc_origin_id(
        self,
        vpc_origin_id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_vpc_origin_id_result.ListDistributionsByVpcOriginIdResult":
        """<p>List CloudFront distributions by their VPC origin ID.</p>

        Args:
            marker: <p>The marker associated with the VPC origin distributions list.</p>
            max_items: <p>The maximum number of items included in the list.</p>
            vpc_origin_id: <p>The VPC origin ID.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list distributions by VPC origin ID
            The following command lists distributions by VPC origin ID:

            >>> client.list_distributions_by_vpc_origin_id(vpc_origin_id='vo_BQwjxxQxjCaBcQLzJUFkDM')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_vpc_origin_id_request.ListDistributionsByVpcOriginIdRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_vpc_origin_id_result.ListDistributionsByVpcOriginIdResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_vpc_origin_id

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_vpc_origin_id.list_distributions_by_vpc_origin_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_vpc_origin_id_request.ListDistributionsByVpcOriginIdRequest = {
            "vpc_origin_id": vpc_origin_id
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_distributions_by_web_acl_id(
        self,
        web_acl_id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distributions_by_web_acl_id_result.ListDistributionsByWebACLIdResult":
        """<p>List the distributions that are associated with a specified WAF web ACL.</p>

        Args:
            marker: <p>Use <code>Marker</code> and <code>MaxItems</code> to control pagination of results. If you have more than <code>MaxItems</code> distributions that satisfy the request, the response includes a <code>NextMarker</code> element. To get the next page of results, submit another request. For the value of <code>Marker</code>, specify the value of <code>NextMarker</code> from the last response. (For the first request, omit <code>Marker</code>.)</p>
            max_items: <p>The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100.</p>
            web_acl_id: <p>The ID of the WAF web ACL that you want to list the associated distributions. If you specify "null" for the ID, the request returns a list of the distributions that aren't associated with a web ACL. </p> <p>For WAFV2, this is the ARN of the web ACL, such as <code>arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>.</p> <p>For WAF Classic, this is the ID of the web ACL, such as <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_web_acl_id.InvalidWebACLId: <p>A web ACL ID specified is not valid. To specify a web ACL created using the latest version of WAF, use the ACL ARN, for example <code>arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a</code>. To specify a web ACL created using WAF Classic, use the ACL ID, for example <code>473e64fd-f30b-4765-81a0-62ad96dd167a</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distributions_by_web_acl_id_request.ListDistributionsByWebACLIdRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distributions_by_web_acl_id_result.ListDistributionsByWebACLIdResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_web_acl_id

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distributions_by_web_acl_id.list_distributions_by_web_acl_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distributions_by_web_acl_id_request.ListDistributionsByWebACLIdRequest = {
            "web_acl_id": web_acl_id
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_distribution_tenants(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        association_filter: Optional[
            "capo_cloudfront.types.distribution_tenant_association_filter.DistributionTenantAssociationFilter"
        ] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distribution_tenants_result.ListDistributionTenantsResult":
        """<p>Lists the distribution tenants in your Amazon Web Services account.</p>

        Args:
            marker: <p>The marker for the next set of results.</p>
            max_items: <p>The maximum number of distribution tenants to return.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distribution_tenants_request.ListDistributionTenantsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distribution_tenants_result.ListDistributionTenantsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distribution_tenants

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distribution_tenants.list_distribution_tenants(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distribution_tenants_request.ListDistributionTenantsRequest = {}
        if association_filter is not None:
            input_["association_filter"] = association_filter
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_distribution_tenants(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        association_filter: Optional[
            "capo_cloudfront.types.distribution_tenant_association_filter.DistributionTenantAssociationFilter"
        ] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.distribution_tenant_summary.DistributionTenantSummary]":
        _token = marker
        while True:
            _response = self.list_distribution_tenants(
                config_overrides=config_overrides,
                association_filter=association_filter,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_tenant_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_distribution_tenants_by_customization(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        web_acl_arn: Optional["capo_cloudfront.types.string.string"] = None,
        certificate_arn: Optional["capo_cloudfront.types.string.string"] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_distribution_tenants_by_customization_result.ListDistributionTenantsByCustomizationResult":
        """<p>Lists distribution tenants by the customization that you specify.</p> <p>You must specify either the <code>CertificateArn</code> parameter or <code>WebACLArn</code> parameter, but not both in the same request.</p>

        Args:
            web_acl_arn: <p>Filter by the ARN of the associated WAF web ACL.</p>
            certificate_arn: <p>Filter by the ARN of the associated ACM certificate.</p>
            marker: <p>The marker for the next set of results.</p>
            max_items: <p>The maximum number of distribution tenants to return by the specified customization.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_distribution_tenants_by_customization_request.ListDistributionTenantsByCustomizationRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_distribution_tenants_by_customization_result.ListDistributionTenantsByCustomizationResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_distribution_tenants_by_customization

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_distribution_tenants_by_customization.list_distribution_tenants_by_customization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_distribution_tenants_by_customization_request.ListDistributionTenantsByCustomizationRequest = {}
        if web_acl_arn is not None:
            input_["web_acl_arn"] = web_acl_arn
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_distribution_tenants_by_customization(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        web_acl_arn: Optional["capo_cloudfront.types.string.string"] = None,
        certificate_arn: Optional["capo_cloudfront.types.string.string"] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.distribution_tenant_summary.DistributionTenantSummary]":
        _token = marker
        while True:
            _response = self.list_distribution_tenants_by_customization(
                config_overrides=config_overrides,
                web_acl_arn=web_acl_arn,
                certificate_arn=certificate_arn,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("distribution_tenant_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_domain_conflicts(
        self,
        domain: "capo_cloudfront.types.string.string",
        domain_control_validation_resource: "capo_cloudfront.types.distribution_resource_id.DistributionResourceId",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.list_domain_conflicts_result.ListDomainConflictsResult":
        """<note> <p>We recommend that you use the <code>ListDomainConflicts</code> API operation to check for domain conflicts, as it supports both standard distributions and distribution tenants. <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListConflictingAliases.html">ListConflictingAliases</a> performs similar checks but only supports standard distributions.</p> </note> <p>Lists existing domain associations that conflict with the domain that you specify.</p> <p>You can use this API operation to identify potential domain conflicts when moving domains between standard distributions and/or distribution tenants. Domain conflicts must be resolved first before they can be moved. </p> <p>For example, if you provide <code>www.example.com</code> as input, the returned list can include <code>www.example.com</code> and the overlapping wildcard alternate domain name (<code>*.example.com</code>), if they exist. If you provide <code>*.example.com</code> as input, the returned list can include <code>*.example.com</code> and any alternate domain names covered by that wildcard (for example, <code>www.example.com</code>, <code>test.example.com</code>, <code>dev.example.com</code>, and so on), if they exist.</p> <p>To list conflicting domains, specify the following:</p> <ul> <li> <p>The domain to search for</p> </li> <li> <p>The ID of a standard distribution or distribution tenant in your account that has an attached TLS certificate, which covers the specified domain</p> </li> </ul> <p>For more information, including how to set up the standard distribution or distribution tenant, and the certificate, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move">Moving an alternate domain name to a different standard distribution or distribution tenant</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            domain: <p>The domain to check for conflicts.</p>
            domain_control_validation_resource: <p>The distribution resource identifier. This can be the standard distribution or distribution tenant that has a valid certificate, which covers the domain that you specify.</p>
            max_items: <p>The maximum number of domain conflicts to return.</p>
            marker: <p>The marker for the next set of domain conflicts.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_domain_conflicts_request.ListDomainConflictsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_domain_conflicts_result.ListDomainConflictsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_domain_conflicts

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_domain_conflicts.list_domain_conflicts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_domain_conflicts_request.ListDomainConflictsRequest = {
            "domain": domain,
            "domain_control_validation_resource": domain_control_validation_resource,
        }
        if max_items is not None:
            input_["max_items"] = max_items
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_domain_conflicts(
        self,
        domain: "capo_cloudfront.types.string.string",
        domain_control_validation_resource: "capo_cloudfront.types.distribution_resource_id.DistributionResourceId",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "Iterator[capo_cloudfront.types.domain_conflict.DomainConflict]":
        _token = marker
        while True:
            _response = self.list_domain_conflicts(
                domain,
                domain_control_validation_resource,
                config_overrides=config_overrides,
                max_items=max_items,
                marker=_token,
            )
            _page = _resolve_path(_response, ("domain_conflicts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_field_level_encryption_configs(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_field_level_encryption_configs_result.ListFieldLevelEncryptionConfigsResult":
        """<p>List all field-level encryption configurations that have been created in CloudFront for this account.</p>

        Args:
            marker: <p>Use this when paginating results to indicate where to begin in your list of configurations. The results include configurations in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last configuration on that page).</p>
            max_items: <p>The maximum number of field-level encryption configurations you want in the response body.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_field_level_encryption_configs_request.ListFieldLevelEncryptionConfigsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_field_level_encryption_configs_result.ListFieldLevelEncryptionConfigsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_field_level_encryption_configs

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_field_level_encryption_configs.list_field_level_encryption_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_field_level_encryption_configs_request.ListFieldLevelEncryptionConfigsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_field_level_encryption_profiles(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_field_level_encryption_profiles_result.ListFieldLevelEncryptionProfilesResult":
        """<p>Request a list of field-level encryption profiles that have been created in CloudFront for this account.</p>

        Args:
            marker: <p>Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last profile on that page).</p>
            max_items: <p>The maximum number of field-level encryption profiles you want in the response body. </p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_field_level_encryption_profiles_request.ListFieldLevelEncryptionProfilesRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_field_level_encryption_profiles_result.ListFieldLevelEncryptionProfilesResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_field_level_encryption_profiles

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_field_level_encryption_profiles.list_field_level_encryption_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_field_level_encryption_profiles_request.ListFieldLevelEncryptionProfilesRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_functions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
        stage: Optional["capo_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "capo_cloudfront.types.list_functions_result.ListFunctionsResult":
        """<p>Gets a list of all CloudFront functions in your Amazon Web Services account.</p> <p>You can optionally apply a filter to return only the functions that are in the specified stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of functions. The response includes functions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of functions that you want in the response.</p>
            stage: <p>An optional filter to return only the functions that are in the specified stage, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_functions_request.ListFunctionsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_functions_result.ListFunctionsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_functions

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_functions.list_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_functions_request.ListFunctionsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_invalidations(
        self,
        distribution_id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_invalidations_result.ListInvalidationsResult":
        """<p>Lists invalidation batches.</p>

        Args:
            distribution_id: <p>The distribution's ID.</p>
            marker: <p>Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response. This value is the same as the ID of the last invalidation batch on that page.</p>
            max_items: <p>The maximum number of invalidation batches that you want in the response body.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_invalidations_request.ListInvalidationsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_invalidations_result.ListInvalidationsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_invalidations

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_invalidations.list_invalidations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_invalidations_request.ListInvalidationsRequest = {
            "distribution_id": distribution_id
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_invalidations(
        self,
        distribution_id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.invalidation_summary.InvalidationSummary]":
        _token = marker
        while True:
            _response = self.list_invalidations(
                distribution_id,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("invalidation_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("invalidation_list", "next_marker"))
            if not _token:
                break

    def list_invalidations_for_distribution_tenant(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_invalidations_for_distribution_tenant_result.ListInvalidationsForDistributionTenantResult":
        """<p>Lists the invalidations for a distribution tenant.</p>

        Args:
            id: <p>The ID of the distribution tenant.</p>
            marker: <p>Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response. This value is the same as the ID of the last invalidation batch on that page.</p>
            max_items: <p>The maximum number of invalidations to return for the distribution tenant.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_invalidations_for_distribution_tenant_request.ListInvalidationsForDistributionTenantRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_invalidations_for_distribution_tenant_result.ListInvalidationsForDistributionTenantResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_invalidations_for_distribution_tenant

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_invalidations_for_distribution_tenant.list_invalidations_for_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_invalidations_for_distribution_tenant_request.ListInvalidationsForDistributionTenantRequest = {
            "id": id
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_invalidations_for_distribution_tenant(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.invalidation_summary.InvalidationSummary]":
        _token = marker
        while True:
            _response = self.list_invalidations_for_distribution_tenant(
                id,
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("invalidation_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("invalidation_list", "next_marker"))
            if not _token:
                break

    def list_key_groups(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_key_groups_result.ListKeyGroupsResult":
        """<p>Gets a list of key groups.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of key groups. The response includes key groups in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of key groups that you want in the response.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_key_groups_request.ListKeyGroupsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_key_groups_result.ListKeyGroupsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_key_groups

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_key_groups.list_key_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_key_groups_request.ListKeyGroupsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_key_value_stores(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
        status: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.list_key_value_stores_result.ListKeyValueStoresResult":
        """<p>Specifies the key value stores to list.</p>

        Args:
            marker: <p>The marker associated with the key value stores list.</p>
            max_items: <p>The maximum number of items in the key value stores list.</p>
            status: <p>The status of the request for the key value stores list.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of KeyValueStores
            The following command retrieves a list of KeyValueStores with READY status.

            >>> client.list_key_value_stores(status='READY')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_key_value_stores_request.ListKeyValueStoresRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_key_value_stores_result.ListKeyValueStoresResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_key_value_stores

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_key_value_stores.list_key_value_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_key_value_stores_request.ListKeyValueStoresRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_key_value_stores(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
        status: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "Iterator[capo_cloudfront.types.key_value_store.KeyValueStore]":
        _token = marker
        while True:
            _response = self.list_key_value_stores(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
                status=status,
            )
            _page = _resolve_path(_response, ("key_value_store_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("key_value_store_list", "next_marker"))
            if not _token:
                break

    def list_origin_access_controls(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_origin_access_controls_result.ListOriginAccessControlsResult":
        """<p>Gets the list of CloudFront origin access controls (OACs) in this Amazon Web Services account.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send another request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the next request.</p> <note> <p>If you're not using origin access controls for your Amazon Web Services account, the <code>ListOriginAccessControls</code> operation doesn't return the <code>Items</code> element in the response.</p> </note>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list of origin access controls. The response includes the items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of origin access controls that you want in the response.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_origin_access_controls_request.ListOriginAccessControlsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_origin_access_controls_result.ListOriginAccessControlsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_origin_access_controls

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_origin_access_controls.list_origin_access_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_origin_access_controls_request.ListOriginAccessControlsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_origin_access_controls(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.origin_access_control_summary.OriginAccessControlSummary]":
        _token = marker
        while True:
            _response = self.list_origin_access_controls(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("origin_access_control_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(
                _response, ("origin_access_control_list", "next_marker")
            )
            if not _token:
                break

    def list_origin_request_policies(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        type: Optional[
            "capo_cloudfront.types.origin_request_policy_type.OriginRequestPolicyType"
        ] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_origin_request_policies_result.ListOriginRequestPoliciesResult":
        """<p>Gets a list of origin request policies.</p> <p>You can optionally apply a filter to return only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            type: <p>A filter to return only the specified kinds of origin request policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Returns only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Returns only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
            marker: <p>Use this field when paginating results to indicate where to begin in your list of origin request policies. The response includes origin request policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of origin request policies that you want in the response.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy: <p>The origin request policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_origin_request_policies_request.ListOriginRequestPoliciesRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_origin_request_policies_result.ListOriginRequestPoliciesResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_origin_request_policies

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_origin_request_policies.list_origin_request_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_origin_request_policies_request.ListOriginRequestPoliciesRequest = {}
        if type is not None:
            input_["type"] = type
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_public_keys(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_public_keys_result.ListPublicKeysResult":
        """<p>List all public keys that have been added to CloudFront for this account.</p>

        Args:
            marker: <p>Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last public key on that page).</p>
            max_items: <p>The maximum number of public keys you want in the response body.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_public_keys_request.ListPublicKeysRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_public_keys_result.ListPublicKeysResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_public_keys

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_public_keys.list_public_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_public_keys_request.ListPublicKeysRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_public_keys(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.public_key_summary.PublicKeySummary]":
        _token = marker
        while True:
            _response = self.list_public_keys(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("public_key_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("public_key_list", "next_marker"))
            if not _token:
                break

    def list_realtime_log_configs(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.list_realtime_log_configs_result.ListRealtimeLogConfigsResult":
        """<p>Gets a list of real-time log configurations.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            max_items: <p>The maximum number of real-time log configurations that you want in the response.</p>
            marker: <p>Use this field when paginating results to indicate where to begin in your list of real-time log configurations. The response includes real-time log configurations in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig: <p>The real-time log configuration does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_realtime_log_configs_request.ListRealtimeLogConfigsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_realtime_log_configs_result.ListRealtimeLogConfigsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_realtime_log_configs

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_realtime_log_configs.list_realtime_log_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_realtime_log_configs_request.ListRealtimeLogConfigsRequest = {}
        if max_items is not None:
            input_["max_items"] = max_items
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_response_headers_policies(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        type: Optional[
            "capo_cloudfront.types.response_headers_policy_type.ResponseHeadersPolicyType"
        ] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_response_headers_policies_result.ListResponseHeadersPoliciesResult":
        """<p>Gets a list of response headers policies.</p> <p>You can optionally apply a filter to get only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.</p> <p>You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the <code>NextMarker</code> value from the current response as the <code>Marker</code> value in the subsequent request.</p>

        Args:
            type: <p>A filter to get only the specified kind of response headers policies. Valid values are:</p> <ul> <li> <p> <code>managed</code> – Gets only the managed policies created by Amazon Web Services.</p> </li> <li> <p> <code>custom</code> – Gets only the custom policies created in your Amazon Web Services account.</p> </li> </ul>
            marker: <p>Use this field when paginating results to indicate where to begin in your list of response headers policies. The response includes response headers policies in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of response headers policies that you want to get in the response.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy: <p>The response headers policy does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_response_headers_policies_request.ListResponseHeadersPoliciesRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_response_headers_policies_result.ListResponseHeadersPoliciesResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_response_headers_policies

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_response_headers_policies.list_response_headers_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_response_headers_policies_request.ListResponseHeadersPoliciesRequest = {}
        if type is not None:
            input_["type"] = type
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_streaming_distributions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_streaming_distributions_result.ListStreamingDistributionsResult":
        """<p>List streaming distributions.</p>

        Args:
            marker: <p>The value that you provided for the <code>Marker</code> request parameter.</p>
            max_items: <p>The value that you provided for the <code>MaxItems</code> request parameter.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_streaming_distributions_request.ListStreamingDistributionsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_streaming_distributions_result.ListStreamingDistributionsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_streaming_distributions

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_streaming_distributions.list_streaming_distributions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_streaming_distributions_request.ListStreamingDistributionsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_streaming_distributions(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.streaming_distribution_summary.StreamingDistributionSummary]":
        _token = marker
        while True:
            _response = self.list_streaming_distributions(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("streaming_distribution_list", "items"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(
                _response, ("streaming_distribution_list", "next_marker")
            )
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource: "capo_cloudfront.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> (
        "capo_cloudfront.types.list_tags_for_resource_result.ListTagsForResourceResult"
    ):
        """<p>List tags for a CloudFront resource. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tagging.html">Tagging a distribution</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            resource: <p>An ARN of a CloudFront resource.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_tagging.InvalidTagging: <p>The tagging specified is not valid.</p>
            capo_cloudfront.errors.no_such_resource.NoSuchResource: <p>A resource that was specified is not valid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_tags_for_resource_result.ListTagsForResourceResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_tags_for_resource

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource": resource
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_trust_stores(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_trust_stores_result.ListTrustStoresResult":
        """<p>Lists trust stores.</p>

        Args:
            marker: <p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>
            max_items: <p>The maximum number of trust stores that you want returned in the response.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_trust_stores_request.ListTrustStoresRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_trust_stores_result.ListTrustStoresResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_trust_stores

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_trust_stores.list_trust_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_trust_stores_request.ListTrustStoresRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_trust_stores(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "Iterator[capo_cloudfront.types.trust_store_summary.TrustStoreSummary]":
        _token = marker
        while True:
            _response = self.list_trust_stores(
                config_overrides=config_overrides,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("trust_store_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    def list_vpc_origins(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        marker: Optional["capo_cloudfront.types.string.string"] = None,
        max_items: Optional["capo_cloudfront.types.integer.integer"] = None,
    ) -> "capo_cloudfront.types.list_vpc_origins_result.ListVpcOriginsResult":
        """<p>List the CloudFront VPC origins in your account.</p>

        Args:
            marker: <p>The marker associated with the VPC origins list.</p>
            max_items: <p>The maximum number of items included in the list.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list VPC origins
            The following command lists VPC origins:

            >>> client.list_vpc_origins()
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.list_vpc_origins_request.ListVpcOriginsRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.list_vpc_origins_result.ListVpcOriginsResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.list_vpc_origins

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.list_vpc_origins.list_vpc_origins(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.list_vpc_origins_request.ListVpcOriginsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def publish_connection_function(
        self,
        id: "capo_cloudfront.types.resource_id.ResourceId",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.publish_connection_function_result.PublishConnectionFunctionResult":
        """<p>Publishes a connection function.</p>

        Args:
            id: <p>The connection function ID.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the connection function.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.publish_connection_function_request.PublishConnectionFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.publish_connection_function_result.PublishConnectionFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.publish_connection_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.publish_connection_function.publish_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.publish_connection_function_request.PublishConnectionFunctionRequest = {
            "id": id,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def publish_function(
        self,
        name: "capo_cloudfront.types.function_name.FunctionName",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.publish_function_result.PublishFunctionResult":
        """<p>Publishes a CloudFront function by copying the function code from the <code>DEVELOPMENT</code> stage to <code>LIVE</code>. This automatically updates all cache behaviors that are using this function to use the newly published copy in the <code>LIVE</code> stage.</p> <p>When a function is published to the <code>LIVE</code> stage, you can attach the function to a distribution's cache behavior, using the function's Amazon Resource Name (ARN).</p> <p>To publish a function, you must provide the function's name and version (<code>ETag</code> value). To get these values, you can use <code>ListFunctions</code> and <code>DescribeFunction</code>.</p>

        Args:
            name: <p>The name of the function that you are publishing.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the function that you are publishing, which you can get using <code>DescribeFunction</code>.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_function_exists.NoSuchFunctionExists: <p>The function does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.publish_function_request.PublishFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.publish_function_result.PublishFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.publish_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.publish_function.publish_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.publish_function_request.PublishFunctionRequest = {
            "name": name,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "capo_cloudfront.types.string.string",
        policy_document: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.put_resource_policy_result.PutResourcePolicyResult":
        """<p>Creates a resource control policy for a given CloudFront resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudFront resource for which the policy is being created.</p>
            policy_document: <p>The JSON-formatted resource policy to create.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.put_resource_policy_result.PutResourcePolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.put_resource_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy_document": policy_document,
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
        resource: "capo_cloudfront.types.resource_arn.ResourceARN",
        tags: "capo_cloudfront.types.tags.Tags",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Add tags to a CloudFront resource. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tagging.html">Tagging a distribution</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            resource: <p>An ARN of a CloudFront resource.</p>
            tags: <p>A complex type that contains zero or more <code>Tag</code> elements.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_tagging.InvalidTagging: <p>The tagging specified is not valid.</p>
            capo_cloudfront.errors.no_such_resource.NoSuchResource: <p>A resource that was specified is not valid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.tag_resource

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.tag_resource_request.TagResourceRequest = {
            "resource": resource,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def test_connection_function(
        self,
        id: "capo_cloudfront.types.resource_id.ResourceId",
        if_match: "capo_cloudfront.types.string.string",
        connection_object: "capo_cloudfront.types.function_event_object.FunctionEventObject",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["capo_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "capo_cloudfront.types.test_connection_function_result.TestConnectionFunctionResult":
        """<p>Tests a connection function.</p>

        Args:
            id: <p>The connection function ID.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the connection function.</p>
            stage: <p>The connection function stage.</p>
            connection_object: <p>The connection object.</p>

        Raises:
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.test_function_failed.TestFunctionFailed: <p>The CloudFront function failed.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.test_connection_function_request.TestConnectionFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.test_connection_function_result.TestConnectionFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.test_connection_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.test_connection_function.test_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.test_connection_function_request.TestConnectionFunctionRequest = {
            "id": id,
            "if_match": if_match,
            "connection_object": connection_object,
        }
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def test_function(
        self,
        name: "capo_cloudfront.types.function_name.FunctionName",
        if_match: "capo_cloudfront.types.string.string",
        event_object: "capo_cloudfront.types.function_event_object.FunctionEventObject",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        stage: Optional["capo_cloudfront.types.function_stage.FunctionStage"] = None,
    ) -> "capo_cloudfront.types.test_function_result.TestFunctionResult":
        """<p>Tests a CloudFront function.</p> <p>To test a function, you provide an <i>event object</i> that represents an HTTP request or response that your CloudFront distribution could receive in production. CloudFront runs the function, passing it the event object that you provided, and returns the function's result (the modified event object) in the response. The response also contains function logs and error messages, if any exist. For more information about testing functions, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managing-functions.html#test-function">Testing functions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>To test a function, you provide the function's name and version (<code>ETag</code> value) along with the event object. To get the function's name and version, you can use <code>ListFunctions</code> and <code>DescribeFunction</code>.</p>

        Args:
            name: <p>The name of the function that you are testing.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the function that you are testing, which you can get using <code>DescribeFunction</code>.</p>
            stage: <p>The stage of the function that you are testing, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>
            event_object: <p>The event object to test the function with. For more information about the structure of the event object, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managing-functions.html#test-function">Testing functions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_function_exists.NoSuchFunctionExists: <p>The function does not exist.</p>
            capo_cloudfront.errors.test_function_failed.TestFunctionFailed: <p>The CloudFront function failed.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.test_function_request.TestFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.test_function_result.TestFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.test_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.test_function.test_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.test_function_request.TestFunctionRequest = {
            "name": name,
            "if_match": if_match,
            "event_object": event_object,
        }
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource: "capo_cloudfront.types.resource_arn.ResourceARN",
        tag_keys: "capo_cloudfront.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> None:
        """<p>Remove tags from a CloudFront resource. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tagging.html">Tagging a distribution</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            resource: <p>An ARN of a CloudFront resource.</p>
            tag_keys: <p>A complex type that contains zero or more <code>Tag</code> key elements.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_tagging.InvalidTagging: <p>The tagging specified is not valid.</p>
            capo_cloudfront.errors.no_such_resource.NoSuchResource: <p>A resource that was specified is not valid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudfront._operations.cloudfront2020_05_31.untag_resource

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.untag_resource_request.UntagResourceRequest = {
            "resource": resource,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_anycast_ip_list(
        self,
        id: "capo_cloudfront.types.string.string",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        ip_address_type: Optional[
            "capo_cloudfront.types.ip_address_type.IpAddressType"
        ] = None,
        ipam_cidr_configs: Optional[
            "capo_cloudfront.types.ipam_cidr_config_list.IpamCidrConfigList"
        ] = None,
    ) -> (
        "capo_cloudfront.types.update_anycast_ip_list_result.UpdateAnycastIpListResult"
    ):
        """<p>Updates an Anycast static IP list.</p>

        Args:
            id: <p>The ID of the Anycast static IP list.</p>
            ip_address_type: <p>The IP address type for the Anycast static IP list. You can specify one of the following options:</p> <ul> <li> <p> <code>ipv4</code> only</p> </li> <li> <p> <code>ipv6</code> only</p> </li> <li> <p> <code>dualstack</code> - Allocate a list of both IPv4 and IPv6 addresses</p> </li> </ul>
            ipam_cidr_configs: <p>A list of IPAM CIDR configurations that specify the IP address ranges and IPAM pool settings for updating the Anycast static IP list.</p>
            if_match: <p>The current version (ETag value) of the Anycast static IP list that you are updating.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_anycast_ip_list_request.UpdateAnycastIpListRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_anycast_ip_list_result.UpdateAnycastIpListResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_anycast_ip_list

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_anycast_ip_list.update_anycast_ip_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_anycast_ip_list_request.UpdateAnycastIpListRequest = {
            "id": id,
            "if_match": if_match,
        }
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if ipam_cidr_configs is not None:
            input_["ipam_cidr_configs"] = ipam_cidr_configs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cache_policy(
        self,
        cache_policy_config: "capo_cloudfront.types.cache_policy_config.CachePolicyConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_cache_policy_result.UpdateCachePolicyResult":
        """<p>Updates a cache policy configuration.</p> <p>When you update a cache policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a cache policy configuration:</p> <ol> <li> <p>Use <code>GetCachePolicyConfig</code> to get the current configuration.</p> </li> <li> <p>Locally modify the fields in the cache policy configuration that you want to update.</p> </li> <li> <p>Call <code>UpdateCachePolicy</code> by providing the entire cache policy configuration, including the fields that you modified and those that you didn't.</p> </li> </ol> <important> <p>If your minimum TTL is greater than 0, CloudFront will cache content for at least the duration specified in the cache policy's minimum TTL, even if the <code>Cache-Control: no-cache</code>, <code>no-store</code>, or <code>private</code> directives are present in the origin headers.</p> </important>

        Args:
            cache_policy_config: <p>A cache policy configuration.</p>
            id: <p>The unique identifier for the cache policy that you are updating. The identifier is returned in a cache behavior's <code>CachePolicyId</code> field in the response to <code>GetDistributionConfig</code>.</p>
            if_match: <p>The version of the cache policy that you are updating. The version is returned in the cache policy's <code>ETag</code> field in the response to <code>GetCachePolicyConfig</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cache_policy_already_exists.CachePolicyAlreadyExists: <p>A cache policy with this name already exists. You must provide a unique name. To modify an existing cache policy, use <code>UpdateCachePolicy</code>.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy: <p>The cache policy does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.too_many_cookies_in_cache_policy.TooManyCookiesInCachePolicy: <p>The number of cookies in the cache policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_headers_in_cache_policy.TooManyHeadersInCachePolicy: <p>The number of headers in the cache policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_query_strings_in_cache_policy.TooManyQueryStringsInCachePolicy: <p>The number of query strings in the cache policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_cache_policy_request.UpdateCachePolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_cache_policy_result.UpdateCachePolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_cache_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_cache_policy.update_cache_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_cache_policy_request.UpdateCachePolicyRequest = {
            "cache_policy_config": cache_policy_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cloud_front_origin_access_identity(
        self,
        cloud_front_origin_access_identity_config: "capo_cloudfront.types.cloud_front_origin_access_identity_config.CloudFrontOriginAccessIdentityConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_cloud_front_origin_access_identity_result.UpdateCloudFrontOriginAccessIdentityResult":
        """<p>Update an origin access identity.</p>

        Args:
            cloud_front_origin_access_identity_config: <p>The identity's configuration information.</p>
            id: <p>The identity's id.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the identity's configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.no_such_cloud_front_origin_access_identity.NoSuchCloudFrontOriginAccessIdentity: <p>The specified origin access identity does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_cloud_front_origin_access_identity_request.UpdateCloudFrontOriginAccessIdentityRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_cloud_front_origin_access_identity_result.UpdateCloudFrontOriginAccessIdentityResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_cloud_front_origin_access_identity

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_cloud_front_origin_access_identity.update_cloud_front_origin_access_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_cloud_front_origin_access_identity_request.UpdateCloudFrontOriginAccessIdentityRequest = {
            "cloud_front_origin_access_identity_config": cloud_front_origin_access_identity_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_connection_function(
        self,
        id: "capo_cloudfront.types.resource_id.ResourceId",
        if_match: "capo_cloudfront.types.string.string",
        connection_function_config: "capo_cloudfront.types.function_config.FunctionConfig",
        connection_function_code: "capo_cloudfront.types.function_blob.FunctionBlob",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.update_connection_function_result.UpdateConnectionFunctionResult":
        """<p>Updates a connection function.</p>

        Args:
            id: <p>The connection function ID.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the connection function you are updating.</p>
            connection_function_code: <p>The connection function code.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.entity_size_limit_exceeded.EntitySizeLimitExceeded: <p>The entity size limit was exceeded.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_connection_function_request.UpdateConnectionFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_connection_function_result.UpdateConnectionFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_connection_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_connection_function.update_connection_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_connection_function_request.UpdateConnectionFunctionRequest = {
            "id": id,
            "if_match": if_match,
            "connection_function_config": connection_function_config,
            "connection_function_code": connection_function_code,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_connection_group(
        self,
        id: "capo_cloudfront.types.string.string",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        ipv6_enabled: Optional["capo_cloudfront.types.boolean.boolean"] = None,
        anycast_ip_list_id: Optional["capo_cloudfront.types.string.string"] = None,
        enabled: Optional["capo_cloudfront.types.boolean.boolean"] = None,
    ) -> "capo_cloudfront.types.update_connection_group_result.UpdateConnectionGroupResult":
        """<p>Updates a connection group.</p>

        Args:
            id: <p>The ID of the connection group.</p>
            ipv6_enabled: <p>Enable IPv6 for the connection group. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesEnableIPv6">Enable IPv6</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the connection group that you're updating.</p>
            anycast_ip_list_id: <p>The ID of the Anycast static IP list.</p>
            enabled: <p>Whether the connection group is enabled.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_already_exists.EntityAlreadyExists: <p>The entity already exists. You must provide a unique entity.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.resource_in_use.ResourceInUse: <p>Cannot delete this resource because it is in use.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_connection_group_request.UpdateConnectionGroupRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_connection_group_result.UpdateConnectionGroupResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_connection_group

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_connection_group.update_connection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_connection_group_request.UpdateConnectionGroupRequest = {
            "id": id,
            "if_match": if_match,
        }
        if ipv6_enabled is not None:
            input_["ipv6_enabled"] = ipv6_enabled
        if anycast_ip_list_id is not None:
            input_["anycast_ip_list_id"] = anycast_ip_list_id
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_continuous_deployment_policy(
        self,
        continuous_deployment_policy_config: "capo_cloudfront.types.continuous_deployment_policy_config.ContinuousDeploymentPolicyConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_continuous_deployment_policy_result.UpdateContinuousDeploymentPolicyResult":
        """<p>Updates a continuous deployment policy. You can update a continuous deployment policy to enable or disable it, to change the percentage of traffic that it sends to the staging distribution, or to change the staging distribution that it sends traffic to.</p> <p>When you update a continuous deployment policy configuration, all the fields are updated with the values that are provided in the request. You cannot update some fields independent of others. To update a continuous deployment policy configuration:</p> <ol> <li> <p>Use <code>GetContinuousDeploymentPolicyConfig</code> to get the current configuration.</p> </li> <li> <p>Locally modify the fields in the continuous deployment policy configuration that you want to update.</p> </li> <li> <p>Use <code>UpdateContinuousDeploymentPolicy</code>, providing the entire continuous deployment policy configuration, including the fields that you modified and those that you didn't.</p> </li> </ol>

        Args:
            continuous_deployment_policy_config: <p>The continuous deployment policy configuration.</p>
            id: <p>The identifier of the continuous deployment policy that you are updating.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the continuous deployment policy that you are updating.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_continuous_deployment_policy.NoSuchContinuousDeploymentPolicy: <p>The continuous deployment policy doesn't exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.staging_distribution_in_use.StagingDistributionInUse: <p>A continuous deployment policy for this staging distribution already exists.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_continuous_deployment_policy_request.UpdateContinuousDeploymentPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_continuous_deployment_policy_result.UpdateContinuousDeploymentPolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_continuous_deployment_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_continuous_deployment_policy.update_continuous_deployment_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_continuous_deployment_policy_request.UpdateContinuousDeploymentPolicyRequest = {
            "continuous_deployment_policy_config": continuous_deployment_policy_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_distribution(
        self,
        distribution_config: "capo_cloudfront.types.distribution_config.DistributionConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_distribution_result.UpdateDistributionResult":
        """<p>Updates the configuration for a CloudFront distribution.</p> <p>The update process includes getting the current distribution configuration, updating it to make your changes, and then submitting an <code>UpdateDistribution</code> request to make the updates.</p> <p> <b>To update a web distribution using the CloudFront API</b> </p> <ol> <li> <p>Use <code>GetDistributionConfig</code> to get the current configuration, including the version identifier (<code>ETag</code>).</p> </li> <li> <p>Update the distribution configuration that was returned in the response. Note the following important requirements and restrictions:</p> <ul> <li> <p>You must copy the <code>ETag</code> field value from the response. (You'll use it for the <code>IfMatch</code> parameter in your request.) Then, remove the <code>ETag</code> field from the distribution configuration.</p> </li> <li> <p>You can't change the value of <code>CallerReference</code>.</p> </li> </ul> </li> <li> <p>Submit an <code>UpdateDistribution</code> request, providing the updated distribution configuration. The new configuration replaces the existing configuration. The values that you specify in an <code>UpdateDistribution</code> request are not merged into your existing configuration. Make sure to include all fields: the ones that you modified and also the ones that you didn't.</p> </li> </ol>

        Args:
            distribution_config: <p>The distribution's configuration information.</p>
            id: <p>The distribution's id.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists: <p>The CNAME specified is already defined for CloudFront.</p>
            capo_cloudfront.errors.continuous_deployment_policy_in_use.ContinuousDeploymentPolicyInUse: <p>You cannot delete a continuous deployment policy that is associated with a primary distribution.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.illegal_field_level_encryption_config_association_with_cache_behavior.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior: <p>The specified configuration for field-level encryption can't be associated with the specified cache behavior.</p>
            capo_cloudfront.errors.illegal_origin_access_configuration.IllegalOriginAccessConfiguration: <p>An origin cannot contain both an origin access control (OAC) and an origin access identity (OAI).</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_default_root_object.InvalidDefaultRootObject: <p>The default root object file name is too big or contains an invalid character.</p>
            capo_cloudfront.errors.invalid_domain_name_for_origin_access_control.InvalidDomainNameForOriginAccessControl: <p>An origin access control is associated with an origin whose domain name is not supported.</p>
            capo_cloudfront.errors.invalid_error_code.InvalidErrorCode: <p>An invalid error code was specified.</p>
            capo_cloudfront.errors.invalid_forward_cookies.InvalidForwardCookies: <p>Your request contains forward cookies option which doesn't match with the expectation for the <code>whitelisted</code> list of cookie names. Either list of cookie names has been specified when not allowed or list of cookie names is missing when expected.</p>
            capo_cloudfront.errors.invalid_function_association.InvalidFunctionAssociation: <p>A CloudFront function association is invalid.</p>
            capo_cloudfront.errors.invalid_geo_restriction_parameter.InvalidGeoRestrictionParameter: <p>The specified geo restriction parameter is not valid.</p>
            capo_cloudfront.errors.invalid_headers_for_s3_origin.InvalidHeadersForS3Origin: <p>The headers specified are not valid for an Amazon S3 origin.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.invalid_lambda_function_association.InvalidLambdaFunctionAssociation: <p>The specified Lambda@Edge function association is invalid.</p>
            capo_cloudfront.errors.invalid_location_code.InvalidLocationCode: <p>The location code specified is not valid.</p>
            capo_cloudfront.errors.invalid_minimum_protocol_version.InvalidMinimumProtocolVersion: <p>The minimum protocol version specified is not valid.</p>
            capo_cloudfront.errors.invalid_origin_access_control.InvalidOriginAccessControl: <p>The origin access control is not valid.</p>
            capo_cloudfront.errors.invalid_origin_access_identity.InvalidOriginAccessIdentity: <p>The origin access identity is not valid or doesn't exist.</p>
            capo_cloudfront.errors.invalid_origin_keepalive_timeout.InvalidOriginKeepaliveTimeout: <p>The keep alive timeout specified for the origin is not valid.</p>
            capo_cloudfront.errors.invalid_origin_read_timeout.InvalidOriginReadTimeout: <p>The read timeout specified for the origin is not valid.</p>
            capo_cloudfront.errors.invalid_query_string_parameters.InvalidQueryStringParameters: <p>The query string parameters specified are not valid.</p>
            capo_cloudfront.errors.invalid_relative_path.InvalidRelativePath: <p>The relative path is too big, is not URL-encoded, or does not begin with a slash (/).</p>
            capo_cloudfront.errors.invalid_required_protocol.InvalidRequiredProtocol: <p>This operation requires the HTTPS protocol. Ensure that you specify the HTTPS protocol in your request, or omit the <code>RequiredProtocols</code> element from your distribution configuration.</p>
            capo_cloudfront.errors.invalid_response_code.InvalidResponseCode: <p>A response code is not valid.</p>
            capo_cloudfront.errors.invalid_ttl_order.InvalidTTLOrder: <p>The TTL order specified is not valid.</p>
            capo_cloudfront.errors.invalid_viewer_certificate.InvalidViewerCertificate: <p>A viewer certificate specified is not valid.</p>
            capo_cloudfront.errors.invalid_web_acl_id.InvalidWebACLId: <p>A web ACL ID specified is not valid. To specify a web ACL created using the latest version of WAF, use the ACL ARN, for example <code>arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a</code>. To specify a web ACL created using WAF Classic, use the ACL ID, for example <code>473e64fd-f30b-4765-81a0-62ad96dd167a</code>.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy: <p>The cache policy does not exist.</p>
            capo_cloudfront.errors.no_such_continuous_deployment_policy.NoSuchContinuousDeploymentPolicy: <p>The continuous deployment policy doesn't exist.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig: <p>The specified configuration for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.no_such_origin.NoSuchOrigin: <p>No origin exists with the specified <code>Origin Id</code>.</p>
            capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy: <p>The origin request policy does not exist.</p>
            capo_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig: <p>The real-time log configuration does not exist.</p>
            capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy: <p>The response headers policy does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.realtime_log_config_owner_mismatch.RealtimeLogConfigOwnerMismatch: <p>The specified real-time log configuration belongs to a different Amazon Web Services account.</p>
            capo_cloudfront.errors.staging_distribution_in_use.StagingDistributionInUse: <p>A continuous deployment policy for this staging distribution already exists.</p>
            capo_cloudfront.errors.too_many_cache_behaviors.TooManyCacheBehaviors: <p>You cannot create more cache behaviors for the distribution.</p>
            capo_cloudfront.errors.too_many_certificates.TooManyCertificates: <p>You cannot create anymore custom SSL/TLS certificates.</p>
            capo_cloudfront.errors.too_many_cookie_names_in_white_list.TooManyCookieNamesInWhiteList: <p>Your request contains more cookie names in the whitelist than are allowed per cache behavior.</p>
            capo_cloudfront.errors.too_many_distribution_cnam_es.TooManyDistributionCNAMEs: <p>Your request contains more CNAMEs than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_cache_policy.TooManyDistributionsAssociatedToCachePolicy: <p>The maximum number of distributions have been associated with the specified cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_field_level_encryption_config.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig: <p>The maximum number of distributions have been associated with the specified configuration for field-level encryption.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_key_group.TooManyDistributionsAssociatedToKeyGroup: <p>The number of distributions that reference this key group is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_origin_access_control.TooManyDistributionsAssociatedToOriginAccessControl: <p>The maximum number of distributions have been associated with the specified origin access control.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_origin_request_policy.TooManyDistributionsAssociatedToOriginRequestPolicy: <p>The maximum number of distributions have been associated with the specified origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_response_headers_policy.TooManyDistributionsAssociatedToResponseHeadersPolicy: <p>The maximum number of distributions have been associated with the specified response headers policy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_with_function_associations.TooManyDistributionsWithFunctionAssociations: <p>You have reached the maximum number of distributions that are associated with a CloudFront function. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_with_lambda_associations.TooManyDistributionsWithLambdaAssociations: <p>Processing your request would cause the maximum number of distributions with Lambda@Edge function associations per owner to be exceeded.</p>
            capo_cloudfront.errors.too_many_distributions_with_single_function_arn.TooManyDistributionsWithSingleFunctionARN: <p>The maximum number of distributions have been associated with the specified Lambda@Edge function.</p>
            capo_cloudfront.errors.too_many_function_associations.TooManyFunctionAssociations: <p>You have reached the maximum number of CloudFront function associations for this distribution. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_headers_in_forwarded_values.TooManyHeadersInForwardedValues: <p>Your request contains too many headers in forwarded values.</p>
            capo_cloudfront.errors.too_many_key_groups_associated_to_distribution.TooManyKeyGroupsAssociatedToDistribution: <p>The number of key groups referenced by this distribution is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_lambda_function_associations.TooManyLambdaFunctionAssociations: <p>Your request contains more Lambda@Edge function associations than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_origin_custom_headers.TooManyOriginCustomHeaders: <p>Your request contains too many origin custom headers.</p>
            capo_cloudfront.errors.too_many_origin_groups_per_distribution.TooManyOriginGroupsPerDistribution: <p>Processing your request would cause you to exceed the maximum number of origin groups allowed.</p>
            capo_cloudfront.errors.too_many_origins.TooManyOrigins: <p>You cannot create more origins for the distribution.</p>
            capo_cloudfront.errors.too_many_query_string_parameters.TooManyQueryStringParameters: <p>Your request contains too many query string parameters.</p>
            capo_cloudfront.errors.too_many_trusted_signers.TooManyTrustedSigners: <p>Your request contains more trusted signers than are allowed per distribution.</p>
            capo_cloudfront.errors.trusted_key_group_does_not_exist.TrustedKeyGroupDoesNotExist: <p>The specified key group does not exist.</p>
            capo_cloudfront.errors.trusted_signer_does_not_exist.TrustedSignerDoesNotExist: <p>One or more of your trusted signers don't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_distribution_request.UpdateDistributionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_distribution_result.UpdateDistributionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_distribution

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_distribution.update_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_distribution_request.UpdateDistributionRequest = {
            "distribution_config": distribution_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_distribution_tenant(
        self,
        id: "capo_cloudfront.types.string.string",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        distribution_id: Optional["capo_cloudfront.types.string.string"] = None,
        domains: Optional["capo_cloudfront.types.domain_list.DomainList"] = None,
        customizations: Optional[
            "capo_cloudfront.types.customizations.Customizations"
        ] = None,
        parameters: Optional["capo_cloudfront.types.parameters.Parameters"] = None,
        connection_group_id: Optional["capo_cloudfront.types.string.string"] = None,
        managed_certificate_request: Optional[
            "capo_cloudfront.types.managed_certificate_request.ManagedCertificateRequest"
        ] = None,
        enabled: Optional["capo_cloudfront.types.boolean.boolean"] = None,
    ) -> "capo_cloudfront.types.update_distribution_tenant_result.UpdateDistributionTenantResult":
        """<p>Updates a distribution tenant.</p>

        Args:
            id: <p>The ID of the distribution tenant.</p>
            distribution_id: <p>The ID for the multi-tenant distribution.</p>
            domains: <p>The domains to update for the distribution tenant. A domain object can contain only a domain property. You must specify at least one domain. Each distribution tenant can have up to 5 domains.</p>
            customizations: <p>Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.</p>
            parameters: <p>A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.</p>
            connection_group_id: <p>The ID of the target connection group.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the distribution tenant to update. This value is returned in the response of the <code>GetDistributionTenant</code> API operation.</p>
            managed_certificate_request: <p>An object that contains the CloudFront managed ACM certificate request.</p>
            enabled: <p>Indicates whether the distribution tenant should be updated to an enabled state. If you update the distribution tenant and it's not enabled, the distribution tenant won't serve traffic.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists: <p>The CNAME specified is already defined for CloudFront.</p>
            capo_cloudfront.errors.entity_already_exists.EntityAlreadyExists: <p>The entity already exists. You must provide a unique entity.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_association.InvalidAssociation: <p>The specified CloudFront resource can't be associated.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_distribution_tenant_request.UpdateDistributionTenantRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_distribution_tenant_result.UpdateDistributionTenantResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_distribution_tenant

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_distribution_tenant.update_distribution_tenant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_distribution_tenant_request.UpdateDistributionTenantRequest = {
            "id": id,
            "if_match": if_match,
        }
        if distribution_id is not None:
            input_["distribution_id"] = distribution_id
        if domains is not None:
            input_["domains"] = domains
        if customizations is not None:
            input_["customizations"] = customizations
        if parameters is not None:
            input_["parameters"] = parameters
        if connection_group_id is not None:
            input_["connection_group_id"] = connection_group_id
        if managed_certificate_request is not None:
            input_["managed_certificate_request"] = managed_certificate_request
        if enabled is not None:
            input_["enabled"] = enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_distribution_with_staging_config(
        self,
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        staging_distribution_id: Optional["capo_cloudfront.types.string.string"] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_distribution_with_staging_config_result.UpdateDistributionWithStagingConfigResult":
        """<p>Copies the staging distribution's configuration to its corresponding primary distribution. The primary distribution retains its <code>Aliases</code> (also known as alternate domain names or CNAMEs) and <code>ContinuousDeploymentPolicyId</code> value, but otherwise its configuration is overwritten to match the staging distribution.</p> <p>You can use this operation in a continuous deployment workflow after you have tested configuration changes on the staging distribution. After using a continuous deployment policy to move a portion of your domain name's traffic to the staging distribution and verifying that it works as intended, you can use this operation to copy the staging distribution's configuration to the primary distribution. This action will disable the continuous deployment policy and move your domain's traffic back to the primary distribution.</p> <p>This API operation requires the following IAM permissions:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html">GetDistribution</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html">UpdateDistribution</a> </p> </li> </ul>

        Args:
            id: <p>The identifier of the primary distribution to which you are copying a staging distribution's configuration.</p>
            staging_distribution_id: <p>The identifier of the staging distribution whose configuration you are copying to the primary distribution.</p>
            if_match: <p>The current versions (<code>ETag</code> values) of both primary and staging distributions. Provide these in the following format:</p> <p> <code>&lt;primary ETag&gt;, &lt;staging ETag&gt;</code> </p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists: <p>The CNAME specified is already defined for CloudFront.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.illegal_field_level_encryption_config_association_with_cache_behavior.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior: <p>The specified configuration for field-level encryption can't be associated with the specified cache behavior.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_default_root_object.InvalidDefaultRootObject: <p>The default root object file name is too big or contains an invalid character.</p>
            capo_cloudfront.errors.invalid_error_code.InvalidErrorCode: <p>An invalid error code was specified.</p>
            capo_cloudfront.errors.invalid_forward_cookies.InvalidForwardCookies: <p>Your request contains forward cookies option which doesn't match with the expectation for the <code>whitelisted</code> list of cookie names. Either list of cookie names has been specified when not allowed or list of cookie names is missing when expected.</p>
            capo_cloudfront.errors.invalid_function_association.InvalidFunctionAssociation: <p>A CloudFront function association is invalid.</p>
            capo_cloudfront.errors.invalid_geo_restriction_parameter.InvalidGeoRestrictionParameter: <p>The specified geo restriction parameter is not valid.</p>
            capo_cloudfront.errors.invalid_headers_for_s3_origin.InvalidHeadersForS3Origin: <p>The headers specified are not valid for an Amazon S3 origin.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.invalid_lambda_function_association.InvalidLambdaFunctionAssociation: <p>The specified Lambda@Edge function association is invalid.</p>
            capo_cloudfront.errors.invalid_location_code.InvalidLocationCode: <p>The location code specified is not valid.</p>
            capo_cloudfront.errors.invalid_minimum_protocol_version.InvalidMinimumProtocolVersion: <p>The minimum protocol version specified is not valid.</p>
            capo_cloudfront.errors.invalid_origin_access_control.InvalidOriginAccessControl: <p>The origin access control is not valid.</p>
            capo_cloudfront.errors.invalid_origin_access_identity.InvalidOriginAccessIdentity: <p>The origin access identity is not valid or doesn't exist.</p>
            capo_cloudfront.errors.invalid_origin_keepalive_timeout.InvalidOriginKeepaliveTimeout: <p>The keep alive timeout specified for the origin is not valid.</p>
            capo_cloudfront.errors.invalid_origin_read_timeout.InvalidOriginReadTimeout: <p>The read timeout specified for the origin is not valid.</p>
            capo_cloudfront.errors.invalid_query_string_parameters.InvalidQueryStringParameters: <p>The query string parameters specified are not valid.</p>
            capo_cloudfront.errors.invalid_relative_path.InvalidRelativePath: <p>The relative path is too big, is not URL-encoded, or does not begin with a slash (/).</p>
            capo_cloudfront.errors.invalid_required_protocol.InvalidRequiredProtocol: <p>This operation requires the HTTPS protocol. Ensure that you specify the HTTPS protocol in your request, or omit the <code>RequiredProtocols</code> element from your distribution configuration.</p>
            capo_cloudfront.errors.invalid_response_code.InvalidResponseCode: <p>A response code is not valid.</p>
            capo_cloudfront.errors.invalid_ttl_order.InvalidTTLOrder: <p>The TTL order specified is not valid.</p>
            capo_cloudfront.errors.invalid_viewer_certificate.InvalidViewerCertificate: <p>A viewer certificate specified is not valid.</p>
            capo_cloudfront.errors.invalid_web_acl_id.InvalidWebACLId: <p>A web ACL ID specified is not valid. To specify a web ACL created using the latest version of WAF, use the ACL ARN, for example <code>arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a</code>. To specify a web ACL created using WAF Classic, use the ACL ID, for example <code>473e64fd-f30b-4765-81a0-62ad96dd167a</code>.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.no_such_cache_policy.NoSuchCachePolicy: <p>The cache policy does not exist.</p>
            capo_cloudfront.errors.no_such_distribution.NoSuchDistribution: <p>The specified distribution does not exist.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig: <p>The specified configuration for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.no_such_origin.NoSuchOrigin: <p>No origin exists with the specified <code>Origin Id</code>.</p>
            capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy: <p>The origin request policy does not exist.</p>
            capo_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig: <p>The real-time log configuration does not exist.</p>
            capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy: <p>The response headers policy does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.realtime_log_config_owner_mismatch.RealtimeLogConfigOwnerMismatch: <p>The specified real-time log configuration belongs to a different Amazon Web Services account.</p>
            capo_cloudfront.errors.too_many_cache_behaviors.TooManyCacheBehaviors: <p>You cannot create more cache behaviors for the distribution.</p>
            capo_cloudfront.errors.too_many_certificates.TooManyCertificates: <p>You cannot create anymore custom SSL/TLS certificates.</p>
            capo_cloudfront.errors.too_many_cookie_names_in_white_list.TooManyCookieNamesInWhiteList: <p>Your request contains more cookie names in the whitelist than are allowed per cache behavior.</p>
            capo_cloudfront.errors.too_many_distribution_cnam_es.TooManyDistributionCNAMEs: <p>Your request contains more CNAMEs than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_cache_policy.TooManyDistributionsAssociatedToCachePolicy: <p>The maximum number of distributions have been associated with the specified cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_field_level_encryption_config.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig: <p>The maximum number of distributions have been associated with the specified configuration for field-level encryption.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_key_group.TooManyDistributionsAssociatedToKeyGroup: <p>The number of distributions that reference this key group is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_origin_access_control.TooManyDistributionsAssociatedToOriginAccessControl: <p>The maximum number of distributions have been associated with the specified origin access control.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_origin_request_policy.TooManyDistributionsAssociatedToOriginRequestPolicy: <p>The maximum number of distributions have been associated with the specified origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_associated_to_response_headers_policy.TooManyDistributionsAssociatedToResponseHeadersPolicy: <p>The maximum number of distributions have been associated with the specified response headers policy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_with_function_associations.TooManyDistributionsWithFunctionAssociations: <p>You have reached the maximum number of distributions that are associated with a CloudFront function. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_distributions_with_lambda_associations.TooManyDistributionsWithLambdaAssociations: <p>Processing your request would cause the maximum number of distributions with Lambda@Edge function associations per owner to be exceeded.</p>
            capo_cloudfront.errors.too_many_distributions_with_single_function_arn.TooManyDistributionsWithSingleFunctionARN: <p>The maximum number of distributions have been associated with the specified Lambda@Edge function.</p>
            capo_cloudfront.errors.too_many_function_associations.TooManyFunctionAssociations: <p>You have reached the maximum number of CloudFront function associations for this distribution. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_headers_in_forwarded_values.TooManyHeadersInForwardedValues: <p>Your request contains too many headers in forwarded values.</p>
            capo_cloudfront.errors.too_many_key_groups_associated_to_distribution.TooManyKeyGroupsAssociatedToDistribution: <p>The number of key groups referenced by this distribution is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_lambda_function_associations.TooManyLambdaFunctionAssociations: <p>Your request contains more Lambda@Edge function associations than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_origin_custom_headers.TooManyOriginCustomHeaders: <p>Your request contains too many origin custom headers.</p>
            capo_cloudfront.errors.too_many_origin_groups_per_distribution.TooManyOriginGroupsPerDistribution: <p>Processing your request would cause you to exceed the maximum number of origin groups allowed.</p>
            capo_cloudfront.errors.too_many_origins.TooManyOrigins: <p>You cannot create more origins for the distribution.</p>
            capo_cloudfront.errors.too_many_query_string_parameters.TooManyQueryStringParameters: <p>Your request contains too many query string parameters.</p>
            capo_cloudfront.errors.too_many_trusted_signers.TooManyTrustedSigners: <p>Your request contains more trusted signers than are allowed per distribution.</p>
            capo_cloudfront.errors.trusted_key_group_does_not_exist.TrustedKeyGroupDoesNotExist: <p>The specified key group does not exist.</p>
            capo_cloudfront.errors.trusted_signer_does_not_exist.TrustedSignerDoesNotExist: <p>One or more of your trusted signers don't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_distribution_with_staging_config_request.UpdateDistributionWithStagingConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_distribution_with_staging_config_result.UpdateDistributionWithStagingConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_distribution_with_staging_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_distribution_with_staging_config.update_distribution_with_staging_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_distribution_with_staging_config_request.UpdateDistributionWithStagingConfigRequest = {
            "id": id
        }
        if staging_distribution_id is not None:
            input_["staging_distribution_id"] = staging_distribution_id
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_domain_association(
        self,
        domain: "capo_cloudfront.types.string.string",
        target_resource: "capo_cloudfront.types.distribution_resource_id.DistributionResourceId",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_domain_association_result.UpdateDomainAssociationResult":
        """<note> <p>We recommend that you use the <code>UpdateDomainAssociation</code> API operation to move a domain association, as it supports both standard distributions and distribution tenants. <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_AssociateAlias.html">AssociateAlias</a> performs similar checks but only supports standard distributions.</p> </note> <p>Moves a domain from its current standard distribution or distribution tenant to another one.</p> <p>You must first disable the source distribution (standard distribution or distribution tenant) and then separately call this operation to move the domain to another target distribution (standard distribution or distribution tenant).</p> <p>To use this operation, specify the domain and the ID of the target resource (standard distribution or distribution tenant). For more information, including how to set up the target resource, prerequisites that you must complete, and other restrictions, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move">Moving an alternate domain name to a different standard distribution or distribution tenant</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Args:
            domain: <p>The domain to update.</p>
            target_resource: <p>The target standard distribution or distribution tenant resource for the domain. You can specify either <code>DistributionId</code> or <code>DistributionTenantId</code>, but not both.</p>
            if_match: <p>The value of the <code>ETag</code> identifier for the standard distribution or distribution tenant that will be associated with the domain.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_domain_association_request.UpdateDomainAssociationRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_domain_association_result.UpdateDomainAssociationResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_domain_association

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_domain_association.update_domain_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_domain_association_request.UpdateDomainAssociationRequest = {
            "domain": domain,
            "target_resource": target_resource,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_field_level_encryption_config(
        self,
        field_level_encryption_config: "capo_cloudfront.types.field_level_encryption_config.FieldLevelEncryptionConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_field_level_encryption_config_result.UpdateFieldLevelEncryptionConfigResult":
        """<p>Update a field-level encryption configuration.</p>

        Args:
            field_level_encryption_config: <p>Request to update a field-level encryption configuration.</p>
            id: <p>The ID of the configuration you want to update.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the configuration identity to update. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig: <p>The specified configuration for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_profile.NoSuchFieldLevelEncryptionProfile: <p>The specified profile for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.query_arg_profile_empty.QueryArgProfileEmpty: <p>No profile specified for the field-level encryption query argument.</p>
            capo_cloudfront.errors.too_many_field_level_encryption_content_type_profiles.TooManyFieldLevelEncryptionContentTypeProfiles: <p>The maximum number of content type profiles for field-level encryption have been created.</p>
            capo_cloudfront.errors.too_many_field_level_encryption_query_arg_profiles.TooManyFieldLevelEncryptionQueryArgProfiles: <p>The maximum number of query arg profiles for field-level encryption have been created.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_field_level_encryption_config_request.UpdateFieldLevelEncryptionConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_field_level_encryption_config_result.UpdateFieldLevelEncryptionConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_field_level_encryption_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_field_level_encryption_config.update_field_level_encryption_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_field_level_encryption_config_request.UpdateFieldLevelEncryptionConfigRequest = {
            "field_level_encryption_config": field_level_encryption_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_field_level_encryption_profile(
        self,
        field_level_encryption_profile_config: "capo_cloudfront.types.field_level_encryption_profile_config.FieldLevelEncryptionProfileConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_field_level_encryption_profile_result.UpdateFieldLevelEncryptionProfileResult":
        """<p>Update a field-level encryption profile.</p>

        Args:
            field_level_encryption_profile_config: <p>Request to update a field-level encryption profile.</p>
            id: <p>The ID of the field-level encryption profile request.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the profile identity to update. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.field_level_encryption_profile_already_exists.FieldLevelEncryptionProfileAlreadyExists: <p>The specified profile for field-level encryption already exists.</p>
            capo_cloudfront.errors.field_level_encryption_profile_size_exceeded.FieldLevelEncryptionProfileSizeExceeded: <p>The maximum size of a profile for field-level encryption was exceeded.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_field_level_encryption_profile.NoSuchFieldLevelEncryptionProfile: <p>The specified profile for field-level encryption doesn't exist.</p>
            capo_cloudfront.errors.no_such_public_key.NoSuchPublicKey: <p>The specified public key doesn't exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.too_many_field_level_encryption_encryption_entities.TooManyFieldLevelEncryptionEncryptionEntities: <p>The maximum number of encryption entities for field-level encryption have been created.</p>
            capo_cloudfront.errors.too_many_field_level_encryption_field_patterns.TooManyFieldLevelEncryptionFieldPatterns: <p>The maximum number of field patterns for field-level encryption have been created.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_field_level_encryption_profile_request.UpdateFieldLevelEncryptionProfileRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_field_level_encryption_profile_result.UpdateFieldLevelEncryptionProfileResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_field_level_encryption_profile

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_field_level_encryption_profile.update_field_level_encryption_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_field_level_encryption_profile_request.UpdateFieldLevelEncryptionProfileRequest = {
            "field_level_encryption_profile_config": field_level_encryption_profile_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_function(
        self,
        name: "capo_cloudfront.types.function_name.FunctionName",
        if_match: "capo_cloudfront.types.string.string",
        function_config: "capo_cloudfront.types.function_config.FunctionConfig",
        function_code: "capo_cloudfront.types.function_blob.FunctionBlob",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.update_function_result.UpdateFunctionResult":
        """<p>Updates a CloudFront function.</p> <p>You can update a function's code or the comment that describes the function. You cannot update a function's name.</p> <p>To update a function, you provide the function's name and version (<code>ETag</code> value) along with the updated function code. To get the name and version, you can use <code>ListFunctions</code> and <code>DescribeFunction</code>.</p>

        Args:
            name: <p>The name of the function that you are updating.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the function that you are updating, which you can get using <code>DescribeFunction</code>.</p>
            function_config: <p>Configuration information about the function.</p>
            function_code: <p>The function code. For more information about writing a CloudFront function, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/writing-function-code.html">Writing function code for CloudFront Functions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

        Raises:
            capo_cloudfront.errors.function_size_limit_exceeded.FunctionSizeLimitExceeded: <p>The function is too large. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_function_exists.NoSuchFunctionExists: <p>The function does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a function
            Use the following command to update a function.

            >>> client.update_function(name='my-function-name', function_config={'Comment': 'my-changed-comment', 'Runtime': 'cloudfront-js-2.0', 'KeyValueStoreAssociations': {'Quantity': 1, 'Items': [{'KeyValueStoreARN': 'arn:aws:cloudfront::123456789012:key-value-store/54947df8-0e9e-4471-a2f9-9af509fb5889'}]}}, function_code='function-code-changed.js', if_match='ETVPDKIKX0DER')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_function_request.UpdateFunctionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_function_result.UpdateFunctionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_function

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_function.update_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_function_request.UpdateFunctionRequest = {
            "name": name,
            "if_match": if_match,
            "function_config": function_config,
            "function_code": function_code,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_key_group(
        self,
        key_group_config: "capo_cloudfront.types.key_group_config.KeyGroupConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_key_group_result.UpdateKeyGroupResult":
        """<p>Updates a key group.</p> <p>When you update a key group, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a key group:</p> <ol> <li> <p>Get the current key group with <code>GetKeyGroup</code> or <code>GetKeyGroupConfig</code>.</p> </li> <li> <p>Locally modify the fields in the key group that you want to update. For example, add or remove public key IDs.</p> </li> <li> <p>Call <code>UpdateKeyGroup</code> with the entire key group object, including the fields that you modified and those that you didn't.</p> </li> </ol>

        Args:
            key_group_config: <p>The key group configuration.</p>
            id: <p>The identifier of the key group that you are updating.</p>
            if_match: <p>The version of the key group that you are updating. The version is the key group's <code>ETag</code> value.</p>

        Raises:
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.key_group_already_exists.KeyGroupAlreadyExists: <p>A key group with this name already exists. You must provide a unique name. To modify an existing key group, use <code>UpdateKeyGroup</code>.</p>
            capo_cloudfront.errors.no_such_resource.NoSuchResource: <p>A resource that was specified is not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.too_many_public_keys_in_key_group.TooManyPublicKeysInKeyGroup: <p>The number of public keys in this key group is more than the maximum allowed. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_key_group_request.UpdateKeyGroupRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_key_group_result.UpdateKeyGroupResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_key_group

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_key_group.update_key_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_key_group_request.UpdateKeyGroupRequest = {
            "key_group_config": key_group_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_key_value_store(
        self,
        name: "capo_cloudfront.types.key_value_store_name.KeyValueStoreName",
        comment: "capo_cloudfront.types.key_value_store_comment.KeyValueStoreComment",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> (
        "capo_cloudfront.types.update_key_value_store_result.UpdateKeyValueStoreResult"
    ):
        """<p>Specifies the key value store to update.</p>

        Args:
            name: <p>The name of the key value store to update.</p>
            comment: <p>The comment of the key value store to update.</p>
            if_match: <p>The key value store to update, if a match occurs.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a KeyValueStore
            Use the following command to update a KeyValueStore.

            >>> client.update_key_value_store(name='my-keyvaluestore-name', comment='my-changed-comment', if_match='ETVPDKIKX0DER')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_key_value_store_request.UpdateKeyValueStoreRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_key_value_store_result.UpdateKeyValueStoreResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_key_value_store

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_key_value_store.update_key_value_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_key_value_store_request.UpdateKeyValueStoreRequest = {
            "name": name,
            "comment": comment,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_origin_access_control(
        self,
        origin_access_control_config: "capo_cloudfront.types.origin_access_control_config.OriginAccessControlConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_origin_access_control_result.UpdateOriginAccessControlResult":
        """<p>Updates a CloudFront origin access control.</p>

        Args:
            origin_access_control_config: <p>An origin access control.</p>
            id: <p>The unique identifier of the origin access control that you are updating.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the origin access control that you are updating.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_origin_access_control.NoSuchOriginAccessControl: <p>The origin access control does not exist.</p>
            capo_cloudfront.errors.origin_access_control_already_exists.OriginAccessControlAlreadyExists: <p>An origin access control with the specified parameters already exists.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_origin_access_control_request.UpdateOriginAccessControlRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_origin_access_control_result.UpdateOriginAccessControlResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_origin_access_control

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_origin_access_control.update_origin_access_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_origin_access_control_request.UpdateOriginAccessControlRequest = {
            "origin_access_control_config": origin_access_control_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_origin_request_policy(
        self,
        origin_request_policy_config: "capo_cloudfront.types.origin_request_policy_config.OriginRequestPolicyConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_origin_request_policy_result.UpdateOriginRequestPolicyResult":
        """<p>Updates an origin request policy configuration.</p> <p>When you update an origin request policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update an origin request policy configuration:</p> <ol> <li> <p>Use <code>GetOriginRequestPolicyConfig</code> to get the current configuration.</p> </li> <li> <p>Locally modify the fields in the origin request policy configuration that you want to update.</p> </li> <li> <p>Call <code>UpdateOriginRequestPolicy</code> by providing the entire origin request policy configuration, including the fields that you modified and those that you didn't.</p> </li> </ol>

        Args:
            origin_request_policy_config: <p>An origin request policy configuration.</p>
            id: <p>The unique identifier for the origin request policy that you are updating. The identifier is returned in a cache behavior's <code>OriginRequestPolicyId</code> field in the response to <code>GetDistributionConfig</code>.</p>
            if_match: <p>The version of the origin request policy that you are updating. The version is returned in the origin request policy's <code>ETag</code> field in the response to <code>GetOriginRequestPolicyConfig</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_origin_request_policy.NoSuchOriginRequestPolicy: <p>The origin request policy does not exist.</p>
            capo_cloudfront.errors.origin_request_policy_already_exists.OriginRequestPolicyAlreadyExists: <p>An origin request policy with this name already exists. You must provide a unique name. To modify an existing origin request policy, use <code>UpdateOriginRequestPolicy</code>.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.too_many_cookies_in_origin_request_policy.TooManyCookiesInOriginRequestPolicy: <p>The number of cookies in the origin request policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_headers_in_origin_request_policy.TooManyHeadersInOriginRequestPolicy: <p>The number of headers in the origin request policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_query_strings_in_origin_request_policy.TooManyQueryStringsInOriginRequestPolicy: <p>The number of query strings in the origin request policy exceeds the maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_origin_request_policy_request.UpdateOriginRequestPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_origin_request_policy_result.UpdateOriginRequestPolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_origin_request_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_origin_request_policy.update_origin_request_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_origin_request_policy_request.UpdateOriginRequestPolicyRequest = {
            "origin_request_policy_config": origin_request_policy_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_public_key(
        self,
        public_key_config: "capo_cloudfront.types.public_key_config.PublicKeyConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_public_key_result.UpdatePublicKeyResult":
        """<p>Update public key information. Note that the only value you can change is the comment.</p>

        Args:
            public_key_config: <p>A public key configuration.</p>
            id: <p>The identifier of the public key that you are updating.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the public key to update. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cannot_change_immutable_public_key_fields.CannotChangeImmutablePublicKeyFields: <p>You can't change the value of a public key.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_public_key.NoSuchPublicKey: <p>The specified public key doesn't exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_public_key_request.UpdatePublicKeyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_public_key_result.UpdatePublicKeyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_public_key

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_public_key.update_public_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_public_key_request.UpdatePublicKeyRequest = {
            "public_key_config": public_key_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_realtime_log_config(
        self,
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        end_points: Optional[
            "capo_cloudfront.types.end_point_list.EndPointList"
        ] = None,
        fields: Optional["capo_cloudfront.types.field_list.FieldList"] = None,
        name: Optional["capo_cloudfront.types.string.string"] = None,
        arn: Optional["capo_cloudfront.types.string.string"] = None,
        sampling_rate: Optional["capo_cloudfront.types.long.long"] = None,
    ) -> "capo_cloudfront.types.update_realtime_log_config_result.UpdateRealtimeLogConfigResult":
        """<p>Updates a real-time log configuration.</p> <p>When you update a real-time log configuration, all the parameters are updated with the values provided in the request. You cannot update some parameters independent of others. To update a real-time log configuration:</p> <ol> <li> <p>Call <code>GetRealtimeLogConfig</code> to get the current real-time log configuration.</p> </li> <li> <p>Locally modify the parameters in the real-time log configuration that you want to update.</p> </li> <li> <p>Call this API (<code>UpdateRealtimeLogConfig</code>) by providing the entire real-time log configuration, including the parameters that you modified and those that you didn't.</p> </li> </ol> <p>You cannot update a real-time log configuration's <code>Name</code> or <code>ARN</code>.</p>

        Args:
            end_points: <p>Contains information about the Amazon Kinesis data stream where you are sending real-time log data.</p>
            fields: <p>A list of fields to include in each real-time log record.</p> <p>For more information about fields, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields">Real-time log configuration fields</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
            name: <p>The name for this real-time log configuration.</p>
            arn: <p>The Amazon Resource Name (ARN) for this real-time log configuration.</p>
            sampling_rate: <p>The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. You must provide an integer between 1 and 100, inclusive.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.no_such_realtime_log_config.NoSuchRealtimeLogConfig: <p>The real-time log configuration does not exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_realtime_log_config_request.UpdateRealtimeLogConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_realtime_log_config_result.UpdateRealtimeLogConfigResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_realtime_log_config

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_realtime_log_config.update_realtime_log_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_realtime_log_config_request.UpdateRealtimeLogConfigRequest = {}
        if end_points is not None:
            input_["end_points"] = end_points
        if fields is not None:
            input_["fields"] = fields
        if name is not None:
            input_["name"] = name
        if arn is not None:
            input_["arn"] = arn
        if sampling_rate is not None:
            input_["sampling_rate"] = sampling_rate

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_response_headers_policy(
        self,
        response_headers_policy_config: "capo_cloudfront.types.response_headers_policy_config.ResponseHeadersPolicyConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_response_headers_policy_result.UpdateResponseHeadersPolicyResult":
        """<p>Updates a response headers policy.</p> <p>When you update a response headers policy, the entire policy is replaced. You cannot update some policy fields independent of others. To update a response headers policy configuration:</p> <ol> <li> <p>Use <code>GetResponseHeadersPolicyConfig</code> to get the current policy's configuration.</p> </li> <li> <p>Modify the fields in the response headers policy configuration that you want to update.</p> </li> <li> <p>Call <code>UpdateResponseHeadersPolicy</code>, providing the entire response headers policy configuration, including the fields that you modified and those that you didn't.</p> </li> </ol>

        Args:
            response_headers_policy_config: <p>A response headers policy configuration.</p>
            id: <p>The identifier for the response headers policy that you are updating.</p>
            if_match: <p>The version of the response headers policy that you are updating.</p> <p>The version is returned in the cache policy's <code>ETag</code> field in the response to <code>GetResponseHeadersPolicyConfig</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.no_such_response_headers_policy.NoSuchResponseHeadersPolicy: <p>The response headers policy does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.response_headers_policy_already_exists.ResponseHeadersPolicyAlreadyExists: <p>A response headers policy with this name already exists. You must provide a unique name. To modify an existing response headers policy, use <code>UpdateResponseHeadersPolicy</code>.</p>
            capo_cloudfront.errors.too_long_csp_in_response_headers_policy.TooLongCSPInResponseHeadersPolicy: <p>The length of the <code>Content-Security-Policy</code> header value in the response headers policy exceeds the maximum.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_custom_headers_in_response_headers_policy.TooManyCustomHeadersInResponseHeadersPolicy: <p>The number of custom headers in the response headers policy exceeds the maximum.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.too_many_remove_headers_in_response_headers_policy.TooManyRemoveHeadersInResponseHeadersPolicy: <p>The number of headers in <code>RemoveHeadersConfig</code> in the response headers policy exceeds the maximum.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html">Quotas</a> (formerly known as limits) in the <i>Amazon CloudFront Developer Guide</i>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_response_headers_policy_request.UpdateResponseHeadersPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_response_headers_policy_result.UpdateResponseHeadersPolicyResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_response_headers_policy

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_response_headers_policy.update_response_headers_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_response_headers_policy_request.UpdateResponseHeadersPolicyRequest = {
            "response_headers_policy_config": response_headers_policy_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_streaming_distribution(
        self,
        streaming_distribution_config: "capo_cloudfront.types.streaming_distribution_config.StreamingDistributionConfig",
        id: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        if_match: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.update_streaming_distribution_result.UpdateStreamingDistributionResult":
        """<p>Update a streaming distribution.</p>

        Args:
            streaming_distribution_config: <p>The streaming distribution's configuration information.</p>
            id: <p>The streaming distribution's id.</p>
            if_match: <p>The value of the <code>ETag</code> header that you received when retrieving the streaming distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cname_already_exists.CNAMEAlreadyExists: <p>The CNAME specified is already defined for CloudFront.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.invalid_origin_access_control.InvalidOriginAccessControl: <p>The origin access control is not valid.</p>
            capo_cloudfront.errors.invalid_origin_access_identity.InvalidOriginAccessIdentity: <p>The origin access identity is not valid or doesn't exist.</p>
            capo_cloudfront.errors.missing_body.MissingBody: <p>This operation requires a body. Ensure that the body is present and the <code>Content-Type</code> header is set.</p>
            capo_cloudfront.errors.no_such_streaming_distribution.NoSuchStreamingDistribution: <p>The specified streaming distribution does not exist.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.too_many_streaming_distribution_cnam_es.TooManyStreamingDistributionCNAMEs: <p>Your request contains more CNAMEs than are allowed per distribution.</p>
            capo_cloudfront.errors.too_many_trusted_signers.TooManyTrustedSigners: <p>Your request contains more trusted signers than are allowed per distribution.</p>
            capo_cloudfront.errors.trusted_signer_does_not_exist.TrustedSignerDoesNotExist: <p>One or more of your trusted signers don't exist.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_streaming_distribution_request.UpdateStreamingDistributionRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_streaming_distribution_result.UpdateStreamingDistributionResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_streaming_distribution

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_streaming_distribution.update_streaming_distribution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_streaming_distribution_request.UpdateStreamingDistributionRequest = {
            "streaming_distribution_config": streaming_distribution_config,
            "id": id,
        }
        if if_match is not None:
            input_["if_match"] = if_match

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_trust_store(
        self,
        id: "capo_cloudfront.types.resource_id.ResourceId",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        ca_certificates_bundle_source: Optional[
            "capo_cloudfront.types.ca_certificates_bundle_source.CaCertificatesBundleSource"
        ] = None,
        use_client_certificate_ocsp_endpoint: Optional[
            "capo_cloudfront.types.boolean.boolean"
        ] = None,
    ) -> "capo_cloudfront.types.update_trust_store_result.UpdateTrustStoreResult":
        """<p>Updates a trust store.</p>

        Args:
            id: <p>The trust store ID.</p>
            ca_certificates_bundle_source: <p>The CA certificates bundle source.</p>
            use_client_certificate_ocsp_endpoint: <p>A Boolean that determines whether to use the CA certificate's OCSP endpoint to check certificate revocation status.</p>
            if_match: <p>The current version (<code>ETag</code> value) of the trust store you are updating.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_trust_store_request.UpdateTrustStoreRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_trust_store_result.UpdateTrustStoreResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_trust_store

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_trust_store.update_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_trust_store_request.UpdateTrustStoreRequest = {
            "id": id,
            "if_match": if_match,
        }
        if ca_certificates_bundle_source is not None:
            input_["ca_certificates_bundle_source"] = ca_certificates_bundle_source
        if use_client_certificate_ocsp_endpoint is not None:
            input_["use_client_certificate_ocsp_endpoint"] = (
                use_client_certificate_ocsp_endpoint
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_vpc_origin(
        self,
        vpc_origin_endpoint_config: "capo_cloudfront.types.vpc_origin_endpoint_config.VpcOriginEndpointConfig",
        id: "capo_cloudfront.types.string.string",
        if_match: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
    ) -> "capo_cloudfront.types.update_vpc_origin_result.UpdateVpcOriginResult":
        """<p>Update an Amazon CloudFront VPC origin in your account.</p>

        Args:
            vpc_origin_endpoint_config: <p>The VPC origin endpoint configuration.</p>
            id: <p>The VPC origin ID.</p>
            if_match: <p>The VPC origin to update, if a match occurs.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.cannot_update_entity_while_in_use.CannotUpdateEntityWhileInUse: <p>The entity cannot be updated while it is in use.</p>
            capo_cloudfront.errors.entity_already_exists.EntityAlreadyExists: <p>The entity already exists. You must provide a unique entity.</p>
            capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded: <p>The entity limit has been exceeded.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.illegal_update.IllegalUpdate: <p>The update contains modifications that are not allowed.</p>
            capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities: <p>The value of <code>Quantity</code> and the size of <code>Items</code> don't match.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion: <p>The <code>If-Match</code> version is missing or not valid.</p>
            capo_cloudfront.errors.precondition_failed.PreconditionFailed: <p>The precondition in one or more of the request fields evaluated to <code>false</code>.</p>
            capo_cloudfront.errors.unsupported_operation.UnsupportedOperation: <p>This operation is not supported in this Amazon Web Services Region.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a VPC origin
            The following command updates a VPC origin:

            >>> client.update_vpc_origin(vpc_origin_endpoint_config={'Name': 'my-vpcorigin-name', 'Arn': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-alb-us-west-2/e6aa5c7d26415c6d', 'HTTPPort': 80, 'HTTPSPort': 443, 'OriginProtocolPolicy': 'match-viewer', 'OriginSslProtocols': {'Quantity': 2, 'Items': ['TLSv1.1', 'TLSv1.2']}}, id='vo_BQwjxxQxjCaBcQLzJUFkDM', if_match='ETVPDKIKX0DER')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.update_vpc_origin_request.UpdateVpcOriginRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.update_vpc_origin_result.UpdateVpcOriginResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.update_vpc_origin

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.update_vpc_origin.update_vpc_origin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.update_vpc_origin_request.UpdateVpcOriginRequest = {
            "vpc_origin_endpoint_config": vpc_origin_endpoint_config,
            "id": id,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def verify_dns_configuration(
        self,
        identifier: "capo_cloudfront.types.string.string",
        *,
        config_overrides: Optional[CloudFrontClientConfig] = None,
        domain: Optional["capo_cloudfront.types.string.string"] = None,
    ) -> "capo_cloudfront.types.verify_dns_configuration_result.VerifyDnsConfigurationResult":
        """<p>Verify the DNS configuration for your domain names. This API operation checks whether your domain name points to the correct routing endpoint of the connection group, such as d111111abcdef8.cloudfront.net. You can use this API operation to troubleshoot and resolve DNS configuration issues.</p>

        Args:
            domain: <p>The domain name that you're verifying.</p>
            identifier: <p>The identifier of the distribution tenant. You can specify the ARN, ID, or name of the distribution tenant.</p>

        Raises:
            capo_cloudfront.errors.access_denied.AccessDenied: <p>Access denied.</p>
            capo_cloudfront.errors.entity_not_found.EntityNotFound: <p>The entity was not found.</p>
            capo_cloudfront.errors.invalid_argument.InvalidArgument: <p>An argument is invalid.</p>
            capo_cloudfront.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront.types.verify_dns_configuration_request.VerifyDnsConfigurationRequest]",
        ) -> OperationResponse[
            "capo_cloudfront.types.verify_dns_configuration_result.VerifyDnsConfigurationResult"
        ]:
            import capo_cloudfront._operations.cloudfront2020_05_31.verify_dns_configuration

            output, http_response = (
                capo_cloudfront._operations.cloudfront2020_05_31.verify_dns_configuration.verify_dns_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront.types.verify_dns_configuration_request.VerifyDnsConfigurationRequest = {
            "identifier": identifier
        }
        if domain is not None:
            input_["domain"] = domain

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
