"""Generated from Smithy shape ``com.amazonaws.elasticache#AmazonElastiCacheV9``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_elasticache._auth._signers
import capo_elasticache._auth._sigv4
from capo_elasticache._auth._identity import Credentials
from capo_elasticache._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_elasticache._auth._zapros_handler import AuthMiddleware
from capo_elasticache._pagination import resolve_path as _resolve_path
from capo_elasticache._services._aws_config import aaws_config
from capo_elasticache._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_elasticache.types.access_string
    import capo_elasticache.types.add_tags_to_resource_message
    import capo_elasticache.types.allowed_node_group_id
    import capo_elasticache.types.allowed_node_type_modifications_message
    import capo_elasticache.types.auth_token_update_strategy_type
    import capo_elasticache.types.authentication_mode
    import capo_elasticache.types.authorize_cache_security_group_ingress_message
    import capo_elasticache.types.authorize_cache_security_group_ingress_result
    import capo_elasticache.types.availability_zones_list
    import capo_elasticache.types.az_mode
    import capo_elasticache.types.batch_apply_update_action_message
    import capo_elasticache.types.batch_stop_update_action_message
    import capo_elasticache.types.boolean
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.cache_cluster
    import capo_elasticache.types.cache_cluster_id_list
    import capo_elasticache.types.cache_cluster_message
    import capo_elasticache.types.cache_engine_version
    import capo_elasticache.types.cache_engine_version_message
    import capo_elasticache.types.cache_node_ids_list
    import capo_elasticache.types.cache_parameter_group
    import capo_elasticache.types.cache_parameter_group_details
    import capo_elasticache.types.cache_parameter_group_name_message
    import capo_elasticache.types.cache_parameter_groups_message
    import capo_elasticache.types.cache_security_group
    import capo_elasticache.types.cache_security_group_message
    import capo_elasticache.types.cache_security_group_name_list
    import capo_elasticache.types.cache_subnet_group
    import capo_elasticache.types.cache_subnet_group_message
    import capo_elasticache.types.cache_usage_limits
    import capo_elasticache.types.cluster_mode
    import capo_elasticache.types.complete_migration_message
    import capo_elasticache.types.complete_migration_response
    import capo_elasticache.types.connection_type
    import capo_elasticache.types.copy_serverless_cache_snapshot_request
    import capo_elasticache.types.copy_serverless_cache_snapshot_response
    import capo_elasticache.types.copy_snapshot_message
    import capo_elasticache.types.copy_snapshot_result
    import capo_elasticache.types.create_cache_cluster_message
    import capo_elasticache.types.create_cache_cluster_result
    import capo_elasticache.types.create_cache_parameter_group_message
    import capo_elasticache.types.create_cache_parameter_group_result
    import capo_elasticache.types.create_cache_security_group_message
    import capo_elasticache.types.create_cache_security_group_result
    import capo_elasticache.types.create_cache_subnet_group_message
    import capo_elasticache.types.create_cache_subnet_group_result
    import capo_elasticache.types.create_global_replication_group_message
    import capo_elasticache.types.create_global_replication_group_result
    import capo_elasticache.types.create_replication_group_message
    import capo_elasticache.types.create_replication_group_result
    import capo_elasticache.types.create_serverless_cache_request
    import capo_elasticache.types.create_serverless_cache_response
    import capo_elasticache.types.create_serverless_cache_snapshot_request
    import capo_elasticache.types.create_serverless_cache_snapshot_response
    import capo_elasticache.types.create_snapshot_message
    import capo_elasticache.types.create_snapshot_result
    import capo_elasticache.types.create_user_group_message
    import capo_elasticache.types.create_user_message
    import capo_elasticache.types.customer_node_endpoint_list
    import capo_elasticache.types.decrease_node_groups_in_global_replication_group_message
    import capo_elasticache.types.decrease_node_groups_in_global_replication_group_result
    import capo_elasticache.types.decrease_replica_count_message
    import capo_elasticache.types.decrease_replica_count_result
    import capo_elasticache.types.delete_cache_cluster_message
    import capo_elasticache.types.delete_cache_cluster_result
    import capo_elasticache.types.delete_cache_parameter_group_message
    import capo_elasticache.types.delete_cache_security_group_message
    import capo_elasticache.types.delete_cache_subnet_group_message
    import capo_elasticache.types.delete_global_replication_group_message
    import capo_elasticache.types.delete_global_replication_group_result
    import capo_elasticache.types.delete_replication_group_message
    import capo_elasticache.types.delete_replication_group_result
    import capo_elasticache.types.delete_serverless_cache_request
    import capo_elasticache.types.delete_serverless_cache_response
    import capo_elasticache.types.delete_serverless_cache_snapshot_request
    import capo_elasticache.types.delete_serverless_cache_snapshot_response
    import capo_elasticache.types.delete_snapshot_message
    import capo_elasticache.types.delete_snapshot_result
    import capo_elasticache.types.delete_user_group_message
    import capo_elasticache.types.delete_user_message
    import capo_elasticache.types.describe_cache_clusters_message
    import capo_elasticache.types.describe_cache_engine_versions_message
    import capo_elasticache.types.describe_cache_parameter_groups_message
    import capo_elasticache.types.describe_cache_parameters_message
    import capo_elasticache.types.describe_cache_security_groups_message
    import capo_elasticache.types.describe_cache_subnet_groups_message
    import capo_elasticache.types.describe_engine_default_parameters_message
    import capo_elasticache.types.describe_engine_default_parameters_result
    import capo_elasticache.types.describe_events_message
    import capo_elasticache.types.describe_global_replication_groups_message
    import capo_elasticache.types.describe_global_replication_groups_result
    import capo_elasticache.types.describe_replication_groups_message
    import capo_elasticache.types.describe_reserved_cache_nodes_message
    import capo_elasticache.types.describe_reserved_cache_nodes_offerings_message
    import capo_elasticache.types.describe_serverless_cache_snapshots_request
    import capo_elasticache.types.describe_serverless_cache_snapshots_response
    import capo_elasticache.types.describe_serverless_caches_request
    import capo_elasticache.types.describe_serverless_caches_response
    import capo_elasticache.types.describe_service_updates_message
    import capo_elasticache.types.describe_snapshots_list_message
    import capo_elasticache.types.describe_snapshots_message
    import capo_elasticache.types.describe_update_actions_message
    import capo_elasticache.types.describe_user_groups_message
    import capo_elasticache.types.describe_user_groups_result
    import capo_elasticache.types.describe_users_message
    import capo_elasticache.types.describe_users_result
    import capo_elasticache.types.disassociate_global_replication_group_message
    import capo_elasticache.types.disassociate_global_replication_group_result
    import capo_elasticache.types.durability
    import capo_elasticache.types.engine_type
    import capo_elasticache.types.event
    import capo_elasticache.types.events_message
    import capo_elasticache.types.export_serverless_cache_snapshot_request
    import capo_elasticache.types.export_serverless_cache_snapshot_response
    import capo_elasticache.types.failover_global_replication_group_message
    import capo_elasticache.types.failover_global_replication_group_result
    import capo_elasticache.types.filter_list
    import capo_elasticache.types.global_node_group_id_list
    import capo_elasticache.types.global_replication_group
    import capo_elasticache.types.increase_node_groups_in_global_replication_group_message
    import capo_elasticache.types.increase_node_groups_in_global_replication_group_result
    import capo_elasticache.types.increase_replica_count_message
    import capo_elasticache.types.increase_replica_count_result
    import capo_elasticache.types.integer
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.ip_discovery
    import capo_elasticache.types.key_list
    import capo_elasticache.types.list_allowed_node_type_modifications_message
    import capo_elasticache.types.list_tags_for_resource_message
    import capo_elasticache.types.log_delivery_configuration_request_list
    import capo_elasticache.types.modify_cache_cluster_message
    import capo_elasticache.types.modify_cache_cluster_result
    import capo_elasticache.types.modify_cache_parameter_group_message
    import capo_elasticache.types.modify_cache_subnet_group_message
    import capo_elasticache.types.modify_cache_subnet_group_result
    import capo_elasticache.types.modify_global_replication_group_message
    import capo_elasticache.types.modify_global_replication_group_result
    import capo_elasticache.types.modify_replication_group_message
    import capo_elasticache.types.modify_replication_group_result
    import capo_elasticache.types.modify_replication_group_shard_configuration_message
    import capo_elasticache.types.modify_replication_group_shard_configuration_result
    import capo_elasticache.types.modify_serverless_cache_request
    import capo_elasticache.types.modify_serverless_cache_response
    import capo_elasticache.types.modify_user_group_message
    import capo_elasticache.types.modify_user_message
    import capo_elasticache.types.network_type
    import capo_elasticache.types.node_group_configuration_list
    import capo_elasticache.types.node_groups_to_remove_list
    import capo_elasticache.types.node_groups_to_retain_list
    import capo_elasticache.types.outpost_mode
    import capo_elasticache.types.parameter
    import capo_elasticache.types.parameter_name_value_list
    import capo_elasticache.types.password_list_input
    import capo_elasticache.types.preferred_availability_zone_list
    import capo_elasticache.types.preferred_outpost_arn_list
    import capo_elasticache.types.purchase_reserved_cache_nodes_offering_message
    import capo_elasticache.types.purchase_reserved_cache_nodes_offering_result
    import capo_elasticache.types.rebalance_slots_in_global_replication_group_message
    import capo_elasticache.types.rebalance_slots_in_global_replication_group_result
    import capo_elasticache.types.reboot_cache_cluster_message
    import capo_elasticache.types.reboot_cache_cluster_result
    import capo_elasticache.types.regional_configuration_list
    import capo_elasticache.types.remove_replicas_list
    import capo_elasticache.types.remove_tags_from_resource_message
    import capo_elasticache.types.replica_configuration_list
    import capo_elasticache.types.replication_group
    import capo_elasticache.types.replication_group_id_list
    import capo_elasticache.types.replication_group_message
    import capo_elasticache.types.reserved_cache_node
    import capo_elasticache.types.reserved_cache_node_message
    import capo_elasticache.types.reserved_cache_nodes_offering
    import capo_elasticache.types.reserved_cache_nodes_offering_message
    import capo_elasticache.types.reset_cache_parameter_group_message
    import capo_elasticache.types.resharding_configuration_list
    import capo_elasticache.types.revoke_cache_security_group_ingress_message
    import capo_elasticache.types.revoke_cache_security_group_ingress_result
    import capo_elasticache.types.scale_config
    import capo_elasticache.types.security_group_ids_list
    import capo_elasticache.types.serverless_cache
    import capo_elasticache.types.serverless_cache_snapshot
    import capo_elasticache.types.service_update
    import capo_elasticache.types.service_update_status_list
    import capo_elasticache.types.service_updates_message
    import capo_elasticache.types.snapshot
    import capo_elasticache.types.snapshot_arns_list
    import capo_elasticache.types.source_type
    import capo_elasticache.types.start_migration_message
    import capo_elasticache.types.start_migration_response
    import capo_elasticache.types.string
    import capo_elasticache.types.subnet_identifier_list
    import capo_elasticache.types.subnet_ids_list
    import capo_elasticache.types.t_stamp
    import capo_elasticache.types.tag_list
    import capo_elasticache.types.tag_list_message
    import capo_elasticache.types.test_failover_message
    import capo_elasticache.types.test_failover_result
    import capo_elasticache.types.test_migration_message
    import capo_elasticache.types.test_migration_response
    import capo_elasticache.types.time_range_filter
    import capo_elasticache.types.transit_encryption_mode
    import capo_elasticache.types.update_action
    import capo_elasticache.types.update_action_results_message
    import capo_elasticache.types.update_action_status_list
    import capo_elasticache.types.update_actions_message
    import capo_elasticache.types.user
    import capo_elasticache.types.user_group
    import capo_elasticache.types.user_group_id_list
    import capo_elasticache.types.user_group_id_list_input
    import capo_elasticache.types.user_id
    import capo_elasticache.types.user_id_list_input
    import capo_elasticache.types.user_name


class AsyncElastiCacheClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncElastiCacheClient:
    """A client for the ``ElastiCache`` service.

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
        self._config = AsyncElastiCacheClientConfig(
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
        self, config_overrides: Optional[AsyncElastiCacheClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncElastiCacheClientConfig = config_overrides or {}
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

    async def add_tags_to_resource(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        resource_name: Optional["capo_elasticache.types.string.String"] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
    ) -> "capo_elasticache.types.tag_list_message.TagListMessage":
        """<p>A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your ElastiCache resources. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.ResourceLevelPermissions.html">Resource-level permissions</a>.</p> <p> For example, you can use cost-allocation tags to your ElastiCache resources, Amazon generates a cost allocation report as a comma-separated value (CSV) file with your usage and costs aggregated by your tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Tagging.html">Using Cost Allocation Tags in Amazon ElastiCache</a> in the <i>ElastiCache User Guide</i>.</p>

        Args:
            resource_name: <p>The Amazon Resource Name (ARN) of the resource to which the tags are to be added, for example <code>arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster</code> or <code>arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot</code>. ElastiCache resources are <i>cluster</i> and <i>snapshot</i>.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Service Namespaces</a>.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault: <p>The requested cache security group name does not refer to an existing cache security group.</p>
            capo_elasticache.errors.cache_subnet_group_not_found_fault.CacheSubnetGroupNotFoundFault: <p>The requested cache subnet group name does not refer to an existing cache subnet group.</p>
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.invalid_arn_fault.InvalidARNFault: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_serverless_cache_snapshot_state_fault.InvalidServerlessCacheSnapshotStateFault: <p>The state of the serverless cache snapshot was not received. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.invalid_serverless_cache_state_fault.InvalidServerlessCacheStateFault: <p>The account for these credentials is not currently active.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.reserved_cache_node_not_found_fault.ReservedCacheNodeNotFoundFault: <p>The requested reserved cache node was not found.</p>
            capo_elasticache.errors.serverless_cache_not_found_fault.ServerlessCacheNotFoundFault: <p>The serverless cache was not found or does not exist.</p>
            capo_elasticache.errors.serverless_cache_snapshot_not_found_fault.ServerlessCacheSnapshotNotFoundFault: <p>This serverless cache snapshot could not be found or does not exist. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The requested snapshot name does not refer to an existing snapshot.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.user_group_not_found_fault.UserGroupNotFoundFault: <p>The user group was not found or does not exist</p>
            capo_elasticache.errors.user_not_found_fault.UserNotFoundFault: <p>The user does not exist or could not be found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            AddTagsToResource
            Adds up to 10 tags, key/value pairs, to a cluster or snapshot resource.

            >>> await client.add_tags_to_resource(resource_name='arn:aws:elasticache:us-east-1:1234567890:cluster:my-mem-cluster', tags=[{'Value': '20150202', 'Key': 'APIVersion'}, {'Value': 'ElastiCache', 'Key': 'Service'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.add_tags_to_resource_message.AddTagsToResourceMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.tag_list_message.TagListMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.add_tags_to_resource

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.add_tags_to_resource.async_add_tags_to_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.add_tags_to_resource_message.AddTagsToResourceMessage = {}
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

    async def authorize_cache_security_group_ingress(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_security_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        ec2_security_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        ec2_security_group_owner_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
    ) -> "capo_elasticache.types.authorize_cache_security_group_ingress_result.AuthorizeCacheSecurityGroupIngressResult":
        """<p>Allows network ingress to a cache security group. Applications using ElastiCache must be running on Amazon EC2, and Amazon EC2 security groups are used as the authorization mechanism.</p> <note> <p>You cannot authorize ingress from an Amazon EC2 security group in one region to an ElastiCache cluster in another region.</p> </note>

        Args:
            cache_security_group_name: <p>The cache security group that allows network ingress.</p>
            ec2_security_group_name: <p>The Amazon EC2 security group to be authorized for ingress to the cache security group.</p>
            ec2_security_group_owner_id: <p>The Amazon account number of the Amazon EC2 security group owner. Note that this is not the same thing as an Amazon access key ID - you must provide a valid Amazon account number for this parameter.</p>

        Raises:
            capo_elasticache.errors.authorization_already_exists_fault.AuthorizationAlreadyExistsFault: <p>The specified Amazon EC2 security group is already authorized for the specified cache security group.</p>
            capo_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault: <p>The requested cache security group name does not refer to an existing cache security group.</p>
            capo_elasticache.errors.invalid_cache_security_group_state_fault.InvalidCacheSecurityGroupStateFault: <p>The current state of the cache security group does not allow deletion.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            AuthorizeCacheCacheSecurityGroupIngress
            Allows network ingress to a cache security group. Applications using ElastiCache must be running on Amazon EC2. Amazon EC2 security groups are used as the authorization mechanism.

            >>> await client.authorize_cache_security_group_ingress(cache_security_group_name='my-sec-grp', ec2_security_group_name='my-ec2-sec-grp', ec2_security_group_owner_id='1234567890')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.authorize_cache_security_group_ingress_message.AuthorizeCacheSecurityGroupIngressMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.authorize_cache_security_group_ingress_result.AuthorizeCacheSecurityGroupIngressResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.authorize_cache_security_group_ingress

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.authorize_cache_security_group_ingress.async_authorize_cache_security_group_ingress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.authorize_cache_security_group_ingress_message.AuthorizeCacheSecurityGroupIngressMessage = {}
        if cache_security_group_name is not None:
            input_["cache_security_group_name"] = cache_security_group_name
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

    async def batch_apply_update_action(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_ids: Optional[
            "capo_elasticache.types.replication_group_id_list.ReplicationGroupIdList"
        ] = None,
        cache_cluster_ids: Optional[
            "capo_elasticache.types.cache_cluster_id_list.CacheClusterIdList"
        ] = None,
        service_update_name: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.update_action_results_message.UpdateActionResultsMessage":
        """<p>Apply the service update. For more information on service updates and applying them, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/applying-updates.html">Applying Service Updates</a>.</p>

        Args:
            replication_group_ids: <p>The replication group IDs</p>
            cache_cluster_ids: <p>The cache cluster IDs</p>
            service_update_name: <p>The unique ID of the service update</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.service_update_not_found_fault.ServiceUpdateNotFoundFault: <p>The service update doesn't exist</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.batch_apply_update_action_message.BatchApplyUpdateActionMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.update_action_results_message.UpdateActionResultsMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.batch_apply_update_action

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.batch_apply_update_action.async_batch_apply_update_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.batch_apply_update_action_message.BatchApplyUpdateActionMessage = {}
        if replication_group_ids is not None:
            input_["replication_group_ids"] = replication_group_ids
        if cache_cluster_ids is not None:
            input_["cache_cluster_ids"] = cache_cluster_ids
        if service_update_name is not None:
            input_["service_update_name"] = service_update_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_stop_update_action(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_ids: Optional[
            "capo_elasticache.types.replication_group_id_list.ReplicationGroupIdList"
        ] = None,
        cache_cluster_ids: Optional[
            "capo_elasticache.types.cache_cluster_id_list.CacheClusterIdList"
        ] = None,
        service_update_name: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.update_action_results_message.UpdateActionResultsMessage":
        """<p>Stop the service update. For more information on service updates and stopping them, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/stopping-self-service-updates.html">Stopping Service Updates</a>.</p>

        Args:
            replication_group_ids: <p>The replication group IDs</p>
            cache_cluster_ids: <p>The cache cluster IDs</p>
            service_update_name: <p>The unique ID of the service update</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.service_update_not_found_fault.ServiceUpdateNotFoundFault: <p>The service update doesn't exist</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.batch_stop_update_action_message.BatchStopUpdateActionMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.update_action_results_message.UpdateActionResultsMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.batch_stop_update_action

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.batch_stop_update_action.async_batch_stop_update_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.batch_stop_update_action_message.BatchStopUpdateActionMessage = {}
        if replication_group_ids is not None:
            input_["replication_group_ids"] = replication_group_ids
        if cache_cluster_ids is not None:
            input_["cache_cluster_ids"] = cache_cluster_ids
        if service_update_name is not None:
            input_["service_update_name"] = service_update_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def complete_migration(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        force: Optional["capo_elasticache.types.boolean.Boolean"] = None,
    ) -> "capo_elasticache.types.complete_migration_response.CompleteMigrationResponse":
        """<p>Complete the migration of data.</p>

        Args:
            replication_group_id: <p>The ID of the replication group to which data is being migrated.</p>
            force: <p>Forces the migration to stop without ensuring that data is in sync. It is recommended to use this option only to abort the migration and not recommended when application wants to continue migration to ElastiCache.</p>

        Raises:
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.replication_group_not_under_migration_fault.ReplicationGroupNotUnderMigrationFault: <p>The designated replication group is not available for data migration.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.complete_migration_message.CompleteMigrationMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.complete_migration_response.CompleteMigrationResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.complete_migration

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.complete_migration.async_complete_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.complete_migration_message.CompleteMigrationMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def copy_serverless_cache_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        source_serverless_cache_snapshot_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        target_serverless_cache_snapshot_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        kms_key_id: Optional["capo_elasticache.types.string.String"] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
    ) -> "capo_elasticache.types.copy_serverless_cache_snapshot_response.CopyServerlessCacheSnapshotResponse":
        """<p>Creates a copy of an existing serverless cache’s snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.</p>

        Args:
            source_serverless_cache_snapshot_name: <p>The identifier of the existing serverless cache’s snapshot to be copied. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            target_serverless_cache_snapshot_name: <p>The identifier for the snapshot to be created. Available for Valkey, Redis OSS and Serverless Memcached only. This value is stored as a lowercase string.</p>
            kms_key_id: <p>The identifier of the KMS key used to encrypt the target snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            tags: <p>A list of tags to be added to the target snapshot resource. A tag is a key-value pair. Available for Valkey, Redis OSS and Serverless Memcached only. Default: NULL</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_serverless_cache_snapshot_state_fault.InvalidServerlessCacheSnapshotStateFault: <p>The state of the serverless cache snapshot was not received. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.serverless_cache_snapshot_already_exists_fault.ServerlessCacheSnapshotAlreadyExistsFault: <p>A serverless cache snapshot with this name already exists. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.serverless_cache_snapshot_not_found_fault.ServerlessCacheSnapshotNotFoundFault: <p>This serverless cache snapshot could not be found or does not exist. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.serverless_cache_snapshot_quota_exceeded_fault.ServerlessCacheSnapshotQuotaExceededFault: <p>The number of serverless cache snapshots exceeds the customer snapshot quota. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.copy_serverless_cache_snapshot_request.CopyServerlessCacheSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.copy_serverless_cache_snapshot_response.CopyServerlessCacheSnapshotResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.copy_serverless_cache_snapshot

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.copy_serverless_cache_snapshot.async_copy_serverless_cache_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.copy_serverless_cache_snapshot_request.CopyServerlessCacheSnapshotRequest = {}
        if source_serverless_cache_snapshot_name is not None:
            input_["source_serverless_cache_snapshot_name"] = (
                source_serverless_cache_snapshot_name
            )
        if target_serverless_cache_snapshot_name is not None:
            input_["target_serverless_cache_snapshot_name"] = (
                target_serverless_cache_snapshot_name
            )
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

    async def copy_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        source_snapshot_name: Optional["capo_elasticache.types.string.String"] = None,
        target_snapshot_name: Optional["capo_elasticache.types.string.String"] = None,
        target_bucket: Optional["capo_elasticache.types.string.String"] = None,
        kms_key_id: Optional["capo_elasticache.types.string.String"] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
    ) -> "capo_elasticache.types.copy_snapshot_result.CopySnapshotResult":
        """<p>Makes a copy of an existing snapshot.</p> <note> <p>This operation is valid for Valkey or Redis OSS only.</p> </note> <important> <p>Users or groups that have permissions to use the <code>CopySnapshot</code> operation can create their own Amazon S3 buckets and copy snapshots to it. To control access to your snapshots, use an IAM policy to control who has the ability to use the <code>CopySnapshot</code> operation. For more information about using IAM to control the use of ElastiCache operations, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html">Exporting Snapshots</a> and <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.html">Authentication & Access Control</a>.</p> </important> <p>You could receive the following error messages.</p> <p class="title"> <b>Error Messages</b> </p> <ul> <li> <p> <b>Error Message:</b> The S3 bucket %s is outside of the region.</p> <p> <b>Solution:</b> Create an Amazon S3 bucket in the same region as your snapshot. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-create-s3-bucket">Step 1: Create an Amazon S3 Bucket</a> in the ElastiCache User Guide.</p> </li> <li> <p> <b>Error Message:</b> The S3 bucket %s does not exist.</p> <p> <b>Solution:</b> Create an Amazon S3 bucket in the same region as your snapshot. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-create-s3-bucket">Step 1: Create an Amazon S3 Bucket</a> in the ElastiCache User Guide.</p> </li> <li> <p> <b>Error Message:</b> The S3 bucket %s is not owned by the authenticated user.</p> <p> <b>Solution:</b> Create an Amazon S3 bucket in the same region as your snapshot. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-create-s3-bucket">Step 1: Create an Amazon S3 Bucket</a> in the ElastiCache User Guide.</p> </li> <li> <p> <b>Error Message:</b> The authenticated user does not have sufficient permissions to perform the desired activity.</p> <p> <b>Solution:</b> Contact your system administrator to get the needed permissions.</p> </li> <li> <p> <b>Error Message:</b> The S3 bucket %s already contains an object with key %s.</p> <p> <b>Solution:</b> Give the <code>TargetSnapshotName</code> a new and unique value. If exporting a snapshot, you could alternatively create a new Amazon S3 bucket and use this same value for <code>TargetSnapshotName</code>.</p> </li> <li> <p> <b>Error Message: </b> ElastiCache has not been granted READ permissions %s on the S3 Bucket.</p> <p> <b>Solution:</b> Add List and Read permissions on the bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access">Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket</a> in the ElastiCache User Guide.</p> </li> <li> <p> <b>Error Message: </b> ElastiCache has not been granted WRITE permissions %s on the S3 Bucket.</p> <p> <b>Solution:</b> Add Upload/Delete permissions on the bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access">Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket</a> in the ElastiCache User Guide.</p> </li> <li> <p> <b>Error Message: </b> ElastiCache has not been granted READ_ACP permissions %s on the S3 Bucket.</p> <p> <b>Solution:</b> Add View Permissions on the bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access">Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket</a> in the ElastiCache User Guide.</p> </li> </ul>

        Args:
            source_snapshot_name: <p>The name of an existing snapshot from which to make a copy.</p>
            target_snapshot_name: <p>A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting. This value is stored as a lowercase string.</p>
            target_bucket: <p>The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access.</p> <p>When using this parameter to export a snapshot, be sure Amazon ElastiCache has the needed permissions to this S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access">Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket</a> in the <i>Amazon ElastiCache User Guide</i>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html">Exporting a Snapshot</a> in the <i>Amazon ElastiCache User Guide</i>.</p>
            kms_key_id: <p>The ID of the KMS key used to encrypt the target snapshot.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_snapshot_state_fault.InvalidSnapshotStateFault: <p>The current state of the snapshot does not allow the requested operation to occur.</p>
            capo_elasticache.errors.snapshot_already_exists_fault.SnapshotAlreadyExistsFault: <p>You already have a snapshot with the given name.</p>
            capo_elasticache.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The requested snapshot name does not refer to an existing snapshot.</p>
            capo_elasticache.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of snapshots.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CopySnapshot
            Copies a snapshot to a specified name.

            >>> await client.copy_snapshot(source_snapshot_name='my-snapshot', target_snapshot_name='my-snapshot-copy', target_bucket='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.copy_snapshot_message.CopySnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.copy_snapshot_result.CopySnapshotResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.copy_snapshot

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.copy_snapshot.async_copy_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.copy_snapshot_message.CopySnapshotMessage = {}
        if source_snapshot_name is not None:
            input_["source_snapshot_name"] = source_snapshot_name
        if target_snapshot_name is not None:
            input_["target_snapshot_name"] = target_snapshot_name
        if target_bucket is not None:
            input_["target_bucket"] = target_bucket
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

    async def create_cache_cluster(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        az_mode: Optional["capo_elasticache.types.az_mode.AZMode"] = None,
        preferred_availability_zone: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        preferred_availability_zones: Optional[
            "capo_elasticache.types.preferred_availability_zone_list.PreferredAvailabilityZoneList"
        ] = None,
        num_cache_nodes: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        cache_node_type: Optional["capo_elasticache.types.string.String"] = None,
        engine: Optional["capo_elasticache.types.string.String"] = None,
        engine_version: Optional["capo_elasticache.types.string.String"] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        cache_subnet_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        cache_security_group_names: Optional[
            "capo_elasticache.types.cache_security_group_name_list.CacheSecurityGroupNameList"
        ] = None,
        security_group_ids: Optional[
            "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
        ] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
        snapshot_arns: Optional[
            "capo_elasticache.types.snapshot_arns_list.SnapshotArnsList"
        ] = None,
        snapshot_name: Optional["capo_elasticache.types.string.String"] = None,
        preferred_maintenance_window: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        port: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        notification_topic_arn: Optional["capo_elasticache.types.string.String"] = None,
        auto_minor_version_upgrade: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        snapshot_retention_limit: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        snapshot_window: Optional["capo_elasticache.types.string.String"] = None,
        auth_token: Optional["capo_elasticache.types.string.String"] = None,
        outpost_mode: Optional[
            "capo_elasticache.types.outpost_mode.OutpostMode"
        ] = None,
        preferred_outpost_arn: Optional["capo_elasticache.types.string.String"] = None,
        preferred_outpost_arns: Optional[
            "capo_elasticache.types.preferred_outpost_arn_list.PreferredOutpostArnList"
        ] = None,
        log_delivery_configurations: Optional[
            "capo_elasticache.types.log_delivery_configuration_request_list.LogDeliveryConfigurationRequestList"
        ] = None,
        transit_encryption_enabled: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        network_type: Optional[
            "capo_elasticache.types.network_type.NetworkType"
        ] = None,
        ip_discovery: Optional[
            "capo_elasticache.types.ip_discovery.IpDiscovery"
        ] = None,
    ) -> "capo_elasticache.types.create_cache_cluster_result.CreateCacheClusterResult":
        """<p>Creates a cluster. All nodes in the cluster run the same protocol-compliant cache engine software, either Memcached, Valkey or Redis OSS.</p> <p>This operation is not supported for Valkey or Redis OSS (cluster mode enabled) clusters.</p>

        Args:
            cache_cluster_id: <p>The node group (shard) identifier. This parameter is stored as a lowercase string.</p> <p> <b>Constraints:</b> </p> <ul> <li> <p>A name must contain from 1 to 50 alphanumeric characters or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>A name cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            replication_group_id: <p>The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.</p> <p>If the specified replication group is Multi-AZ enabled and the Availability Zone is not specified, the cluster is created in Availability Zones that provide the best spread of read replicas across Availability Zones.</p> <note> <p>This parameter is only valid if the <code>Engine</code> parameter is <code>redis</code>.</p> </note>
            az_mode: <p>Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region.</p> <p>This parameter is only supported for Memcached clusters.</p> <p>If the <code>AZMode</code> and <code>PreferredAvailabilityZones</code> are not specified, ElastiCache assumes <code>single-az</code> mode.</p>
            preferred_availability_zone: <p>The EC2 Availability Zone in which the cluster is created.</p> <p>All nodes belonging to this cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use <code>PreferredAvailabilityZones</code>.</p> <p>Default: System chosen Availability Zone.</p>
            preferred_availability_zones: <p>A list of the Availability Zones in which cache nodes are created. The order of the zones in the list is not important.</p> <p>This option is only supported on Memcached.</p> <note> <p>If you are creating your cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group.</p> <p>The number of Availability Zones listed must equal the value of <code>NumCacheNodes</code>.</p> </note> <p>If you want all the nodes in the same Availability Zone, use <code>PreferredAvailabilityZone</code> instead, or repeat the Availability Zone multiple times in the list.</p> <p>Default: System chosen Availability Zones.</p>
            num_cache_nodes: <p>The initial number of cache nodes that the cluster has.</p> <p>For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.</p> <p>If you need more than 40 nodes for your Memcached cluster, please fill out the ElastiCache Limit Increase Request form at <a href="http://aws.amazon.com/contact-us/elasticache-node-limit-request/">http://aws.amazon.com/contact-us/elasticache-node-limit-request/</a>.</p>
            cache_node_type: <p>The compute and memory capacity of the nodes in the node group (shard).</p> <p>The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.</p> <ul> <li> <p>General purpose:</p> <ul> <li> <p>Current generation: </p> <p> <b>M7g node types</b>: <code>cache.m7g.large</code>, <code>cache.m7g.xlarge</code>, <code>cache.m7g.2xlarge</code>, <code>cache.m7g.4xlarge</code>, <code>cache.m7g.8xlarge</code>, <code>cache.m7g.12xlarge</code>, <code>cache.m7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>M6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.m6g.large</code>, <code>cache.m6g.xlarge</code>, <code>cache.m6g.2xlarge</code>, <code>cache.m6g.4xlarge</code>, <code>cache.m6g.8xlarge</code>, <code>cache.m6g.12xlarge</code>, <code>cache.m6g.16xlarge</code> </p> <p> <b>M5 node types:</b> <code>cache.m5.large</code>, <code>cache.m5.xlarge</code>, <code>cache.m5.2xlarge</code>, <code>cache.m5.4xlarge</code>, <code>cache.m5.12xlarge</code>, <code>cache.m5.24xlarge</code> </p> <p> <b>M4 node types:</b> <code>cache.m4.large</code>, <code>cache.m4.xlarge</code>, <code>cache.m4.2xlarge</code>, <code>cache.m4.4xlarge</code>, <code>cache.m4.10xlarge</code> </p> <p> <b>T4g node types</b> (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): <code>cache.t4g.micro</code>, <code>cache.t4g.small</code>, <code>cache.t4g.medium</code> </p> <p> <b>T3 node types:</b> <code>cache.t3.micro</code>, <code>cache.t3.small</code>, <code>cache.t3.medium</code> </p> <p> <b>T2 node types:</b> <code>cache.t2.micro</code>, <code>cache.t2.small</code>, <code>cache.t2.medium</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>T1 node types:</b> <code>cache.t1.micro</code> </p> <p> <b>M1 node types:</b> <code>cache.m1.small</code>, <code>cache.m1.medium</code>, <code>cache.m1.large</code>, <code>cache.m1.xlarge</code> </p> <p> <b>M3 node types:</b> <code>cache.m3.medium</code>, <code>cache.m3.large</code>, <code>cache.m3.xlarge</code>, <code>cache.m3.2xlarge</code> </p> </li> </ul> </li> <li> <p>Compute optimized:</p> <ul> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>C1 node types:</b> <code>cache.c1.xlarge</code> </p> </li> </ul> </li> <li> <p>Memory optimized:</p> <ul> <li> <p>Current generation: </p> <p> <b>R7g node types</b>: <code>cache.r7g.large</code>, <code>cache.r7g.xlarge</code>, <code>cache.r7g.2xlarge</code>, <code>cache.r7g.4xlarge</code>, <code>cache.r7g.8xlarge</code>, <code>cache.r7g.12xlarge</code>, <code>cache.r7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>R6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.r6g.large</code>, <code>cache.r6g.xlarge</code>, <code>cache.r6g.2xlarge</code>, <code>cache.r6g.4xlarge</code>, <code>cache.r6g.8xlarge</code>, <code>cache.r6g.12xlarge</code>, <code>cache.r6g.16xlarge</code> </p> <p> <b>R5 node types:</b> <code>cache.r5.large</code>, <code>cache.r5.xlarge</code>, <code>cache.r5.2xlarge</code>, <code>cache.r5.4xlarge</code>, <code>cache.r5.12xlarge</code>, <code>cache.r5.24xlarge</code> </p> <p> <b>R4 node types:</b> <code>cache.r4.large</code>, <code>cache.r4.xlarge</code>, <code>cache.r4.2xlarge</code>, <code>cache.r4.4xlarge</code>, <code>cache.r4.8xlarge</code>, <code>cache.r4.16xlarge</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>M2 node types:</b> <code>cache.m2.xlarge</code>, <code>cache.m2.2xlarge</code>, <code>cache.m2.4xlarge</code> </p> <p> <b>R3 node types:</b> <code>cache.r3.large</code>, <code>cache.r3.xlarge</code>, <code>cache.r3.2xlarge</code>, <code>cache.r3.4xlarge</code>, <code>cache.r3.8xlarge</code> </p> </li> </ul> </li> </ul> <p> <b>Additional node type info</b> </p> <ul> <li> <p>All current generation instance types are created in Amazon VPC by default.</p> </li> <li> <p>Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.</p> </li> <li> <p>Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.</p> </li> <li> <p>The configuration variables <code>appendonly</code> and <code>appendfsync</code> are not supported on Valkey, or on Redis OSS version 2.8.22 and later.</p> </li> </ul>
            engine: <p>The name of the cache engine to be used for this cluster.</p> <p>Valid values for this parameter are: <code>memcached</code> | <code>redis</code> </p>
            engine_version: <p>The version number of the cache engine to be used for this cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.</p> <p> <b>Important:</b> You can upgrade to a newer engine version (see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement">Selecting a Cache Engine and Version</a>), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version. </p>
            cache_parameter_group_name: <p>The name of the parameter group to associate with this cluster. If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which has <code>cluster-enabled='yes'</code> when creating a cluster.</p>
            cache_subnet_group_name: <p>The name of the subnet group to be used for the cluster.</p> <p>Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).</p> <important> <p>If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.html">Subnets and Subnet Groups</a>.</p> </important>
            cache_security_group_names: <p>A list of security group names to associate with this cluster.</p> <p>Use this parameter only when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC).</p>
            security_group_ids: <p>One or more VPC security groups associated with the cluster.</p> <p>Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).</p>
            tags: <p>A list of tags to be added to this resource.</p>
            snapshot_arns: <p>A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Valkey or Redis OSS RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node group (shard). The Amazon S3 object name in the ARN cannot contain any commas.</p> <note> <p>This parameter is only valid if the <code>Engine</code> parameter is <code>redis</code>.</p> </note> <p>Example of an Amazon S3 ARN: <code>arn:aws:s3:::my_bucket/snapshot1.rdb</code> </p>
            snapshot_name: <p>The name of a Valkey or Redis OSS snapshot from which to restore data into the new node group (shard). The snapshot status changes to <code>restoring</code> while the new node group (shard) is being created.</p> <note> <p>This parameter is only valid if the <code>Engine</code> parameter is <code>redis</code>.</p> </note>
            preferred_maintenance_window: <p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. </p>
            port: <p>The port number on which each of the cache nodes accepts connections.</p>
            notification_topic_arn: <p>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.</p> <note> <p>The Amazon SNS topic owner must be the same as the cluster owner.</p> </note>
            auto_minor_version_upgrade: <p> If you are running Valkey 7.2 and above or Redis OSS engine version 6.0 and above, set this parameter to yes to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions. </p>
            snapshot_retention_limit: <p>The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set <code>SnapshotRetentionLimit</code> to 5, a snapshot taken today is retained for 5 days before being deleted.</p> <note> <p>This parameter is only valid if the <code>Engine</code> parameter is <code>redis</code>.</p> </note> <p>Default: 0 (i.e., automatic backups are disabled for this cache cluster).</p>
            snapshot_window: <p>The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).</p> <p>Example: <code>05:00-09:00</code> </p> <p>If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.</p> <note> <p>This parameter is only valid if the <code>Engine</code> parameter is <code>redis</code>.</p> </note>
            auth_token: <p> <b>Reserved parameter.</b> The password used to access a password protected server.</p> <p>Password constraints:</p> <ul> <li> <p>Must be only printable ASCII characters.</p> </li> <li> <p>Must be at least 16 characters and no more than 128 characters in length.</p> </li> <li> <p>The only permitted printable special characters are !, &, #, $, ^, <, >, and -. Other printable special characters cannot be used in the AUTH token.</p> </li> </ul> <p>For more information, see <a href="http://redis.io/commands/AUTH">AUTH password</a> at http://redis.io/commands/AUTH.</p>
            outpost_mode: <p>Specifies whether the nodes in the cluster are created in a single outpost or across multiple outposts.</p>
            preferred_outpost_arn: <p>The outpost ARN in which the cache cluster is created.</p>
            preferred_outpost_arns: <p>The outpost ARNs in which the cache cluster is created.</p>
            log_delivery_configurations: <p>Specifies the destination, format and type of the logs. </p>
            transit_encryption_enabled: <p>A flag that enables in-transit encryption when set to true.</p>
            network_type: <p>Must be either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>. </p>
            ip_discovery: <p>The network type you choose when modifying a cluster, either <code>ipv4</code> | <code>ipv6</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_already_exists_fault.CacheClusterAlreadyExistsFault: <p>You already have a cluster with the given identifier.</p>
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault: <p>The requested cache security group name does not refer to an existing cache security group.</p>
            capo_elasticache.errors.cache_subnet_group_not_found_fault.CacheSubnetGroupNotFoundFault: <p>The requested cache subnet group name does not refer to an existing cache subnet group.</p>
            capo_elasticache.errors.cluster_quota_for_customer_exceeded_fault.ClusterQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the allowed number of clusters per customer.</p>
            capo_elasticache.errors.insufficient_cache_cluster_capacity_fault.InsufficientCacheClusterCapacityFault: <p>The requested cache node type is not available in the specified Availability Zone. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ErrorMessages.html#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY">InsufficientCacheClusterCapacity</a> in the ElastiCache User Guide.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The VPC network is in an invalid state.</p>
            capo_elasticache.errors.node_quota_for_cluster_exceeded_fault.NodeQuotaForClusterExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache nodes in a single cluster.</p>
            capo_elasticache.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache nodes per customer.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateCacheCluster
            Creates a Memcached cluster with 2 nodes.

            >>> await client.create_cache_cluster(cache_cluster_id='my-memcached-cluster', az_mode='cross-az', num_cache_nodes=2, cache_node_type='cache.r3.large', engine='memcached', engine_version='1.4.24', cache_subnet_group_name='default', port=11211)
            CreateCacheCluster
            Creates a Redis cluster with 1 node.

            >>> await client.create_cache_cluster(cache_cluster_id='my-redis', preferred_availability_zone='us-east-1c', num_cache_nodes=1, cache_node_type='cache.r3.larage', engine='redis', engine_version='3.2.4', cache_subnet_group_name='default', port=6379, snapshot_retention_limit=7, auto_minor_version_upgrade=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.create_cache_cluster_message.CreateCacheClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.create_cache_cluster_result.CreateCacheClusterResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.create_cache_cluster

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.create_cache_cluster.async_create_cache_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.create_cache_cluster_message.CreateCacheClusterMessage = {}
        if cache_cluster_id is not None:
            input_["cache_cluster_id"] = cache_cluster_id
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if az_mode is not None:
            input_["az_mode"] = az_mode
        if preferred_availability_zone is not None:
            input_["preferred_availability_zone"] = preferred_availability_zone
        if preferred_availability_zones is not None:
            input_["preferred_availability_zones"] = preferred_availability_zones
        if num_cache_nodes is not None:
            input_["num_cache_nodes"] = num_cache_nodes
        if cache_node_type is not None:
            input_["cache_node_type"] = cache_node_type
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if cache_parameter_group_name is not None:
            input_["cache_parameter_group_name"] = cache_parameter_group_name
        if cache_subnet_group_name is not None:
            input_["cache_subnet_group_name"] = cache_subnet_group_name
        if cache_security_group_names is not None:
            input_["cache_security_group_names"] = cache_security_group_names
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if snapshot_arns is not None:
            input_["snapshot_arns"] = snapshot_arns
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if port is not None:
            input_["port"] = port
        if notification_topic_arn is not None:
            input_["notification_topic_arn"] = notification_topic_arn
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if snapshot_retention_limit is not None:
            input_["snapshot_retention_limit"] = snapshot_retention_limit
        if snapshot_window is not None:
            input_["snapshot_window"] = snapshot_window
        if auth_token is not None:
            input_["auth_token"] = auth_token
        if outpost_mode is not None:
            input_["outpost_mode"] = outpost_mode
        if preferred_outpost_arn is not None:
            input_["preferred_outpost_arn"] = preferred_outpost_arn
        if preferred_outpost_arns is not None:
            input_["preferred_outpost_arns"] = preferred_outpost_arns
        if log_delivery_configurations is not None:
            input_["log_delivery_configurations"] = log_delivery_configurations
        if transit_encryption_enabled is not None:
            input_["transit_encryption_enabled"] = transit_encryption_enabled
        if network_type is not None:
            input_["network_type"] = network_type
        if ip_discovery is not None:
            input_["ip_discovery"] = ip_discovery

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cache_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        cache_parameter_group_family: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        description: Optional["capo_elasticache.types.string.String"] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
    ) -> "capo_elasticache.types.create_cache_parameter_group_result.CreateCacheParameterGroupResult":
        """<p>Creates a new Amazon ElastiCache cache parameter group. An ElastiCache cache parameter group is a collection of parameters and their values that are applied to all of the nodes in any cluster or replication group using the CacheParameterGroup.</p> <p>A newly created CacheParameterGroup is an exact duplicate of the default parameter group for the CacheParameterGroupFamily. To customize the newly created CacheParameterGroup you can change the values of specific parameters. For more information, see:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheParameterGroup.html">ModifyCacheParameterGroup</a> in the ElastiCache API Reference.</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.html">Parameters and Parameter Groups</a> in the ElastiCache User Guide.</p> </li> </ul>

        Args:
            cache_parameter_group_name: <p>A user-specified name for the cache parameter group. This value is stored as a lowercase string.</p>
            cache_parameter_group_family: <p>The name of the cache parameter group family that the cache parameter group can be used with.</p> <p>Valid values are: <code>valkey8</code> | <code>valkey7</code> | <code>memcached1.4</code> | <code>memcached1.5</code> | <code>memcached1.6</code> | <code>redis2.6</code> | <code>redis2.8</code> | <code>redis3.2</code> | <code>redis4.0</code> | <code>redis5.0</code> | <code>redis6.x</code> | <code>redis7</code> </p>
            description: <p>A user-specified description for the cache parameter group.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_elasticache.errors.cache_parameter_group_already_exists_fault.CacheParameterGroupAlreadyExistsFault: <p>A cache parameter group with the requested name already exists.</p>
            capo_elasticache.errors.cache_parameter_group_quota_exceeded_fault.CacheParameterGroupQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of cache security groups.</p>
            capo_elasticache.errors.invalid_cache_parameter_group_state_fault.InvalidCacheParameterGroupStateFault: <p>The current state of the cache parameter group does not allow the requested operation to occur.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateCacheParameterGroup
            Creates the Amazon ElastiCache parameter group custom-redis2-8.

            >>> await client.create_cache_parameter_group(cache_parameter_group_name='custom-redis2-8', cache_parameter_group_family='redis2.8', description='Custom Redis 2.8 parameter group.')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.create_cache_parameter_group_message.CreateCacheParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.create_cache_parameter_group_result.CreateCacheParameterGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.create_cache_parameter_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.create_cache_parameter_group.async_create_cache_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.create_cache_parameter_group_message.CreateCacheParameterGroupMessage = {}
        if cache_parameter_group_name is not None:
            input_["cache_parameter_group_name"] = cache_parameter_group_name
        if cache_parameter_group_family is not None:
            input_["cache_parameter_group_family"] = cache_parameter_group_family
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

    async def create_cache_security_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_security_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        description: Optional["capo_elasticache.types.string.String"] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
    ) -> "capo_elasticache.types.create_cache_security_group_result.CreateCacheSecurityGroupResult":
        """<p>Creates a new cache security group. Use a cache security group to control access to one or more clusters.</p> <p>Cache security groups are only used when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC). If you are creating a cluster inside of a VPC, use a cache subnet group instead. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheSubnetGroup.html">CreateCacheSubnetGroup</a>.</p>

        Args:
            cache_security_group_name: <p>A name for the cache security group. This value is stored as a lowercase string.</p> <p>Constraints: Must contain no more than 255 alphanumeric characters. Cannot be the word "Default".</p> <p>Example: <code>mysecuritygroup</code> </p>
            description: <p>A description for the cache security group.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_elasticache.errors.cache_security_group_already_exists_fault.CacheSecurityGroupAlreadyExistsFault: <p>A cache security group with the specified name already exists.</p>
            capo_elasticache.errors.cache_security_group_quota_exceeded_fault.CacheSecurityGroupQuotaExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache security groups.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateCacheSecurityGroup
            Creates an ElastiCache security group. ElastiCache security groups are only for clusters not running in an AWS VPC.

            >>> await client.create_cache_security_group(cache_security_group_name='my-cache-sec-grp', description='Example ElastiCache security group.')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.create_cache_security_group_message.CreateCacheSecurityGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.create_cache_security_group_result.CreateCacheSecurityGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.create_cache_security_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.create_cache_security_group.async_create_cache_security_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.create_cache_security_group_message.CreateCacheSecurityGroupMessage = {}
        if cache_security_group_name is not None:
            input_["cache_security_group_name"] = cache_security_group_name
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

    async def create_cache_subnet_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_subnet_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        cache_subnet_group_description: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        subnet_ids: Optional[
            "capo_elasticache.types.subnet_identifier_list.SubnetIdentifierList"
        ] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
    ) -> "capo_elasticache.types.create_cache_subnet_group_result.CreateCacheSubnetGroupResult":
        """<p>Creates a new cache subnet group.</p> <p>Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).</p>

        Args:
            cache_subnet_group_name: <p>A name for the cache subnet group. This value is stored as a lowercase string.</p> <p>Constraints: Must contain no more than 255 alphanumeric characters or hyphens.</p> <p>Example: <code>mysubnetgroup</code> </p>
            cache_subnet_group_description: <p>A description for the cache subnet group.</p>
            subnet_ids: <p>A list of VPC subnet IDs for the cache subnet group.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_elasticache.errors.cache_subnet_group_already_exists_fault.CacheSubnetGroupAlreadyExistsFault: <p>The requested cache subnet group name is already in use by an existing cache subnet group.</p>
            capo_elasticache.errors.cache_subnet_group_quota_exceeded_fault.CacheSubnetGroupQuotaExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache subnet groups.</p>
            capo_elasticache.errors.cache_subnet_quota_exceeded_fault.CacheSubnetQuotaExceededFault: <p>The request cannot be processed because it would exceed the allowed number of subnets in a cache subnet group.</p>
            capo_elasticache.errors.invalid_subnet.InvalidSubnet: <p>An invalid subnet identifier was specified.</p>
            capo_elasticache.errors.subnet_not_allowed_fault.SubnetNotAllowedFault: <p>At least one subnet ID does not match the other subnet IDs. This mismatch typically occurs when a user sets one subnet ID to a regional Availability Zone and a different one to an outpost. Or when a user sets the subnet ID to an Outpost when not subscribed on this service.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateCacheSubnet
            Creates a new cache subnet group.

            >>> await client.create_cache_subnet_group(cache_subnet_group_name='my-sn-grp2', cache_subnet_group_description='Sample subnet group', subnet_ids=['subnet-6f28c982', 'subnet-bcd382f3', 'subnet-845b3e7c0'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.create_cache_subnet_group_message.CreateCacheSubnetGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.create_cache_subnet_group_result.CreateCacheSubnetGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.create_cache_subnet_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.create_cache_subnet_group.async_create_cache_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.create_cache_subnet_group_message.CreateCacheSubnetGroupMessage = {}
        if cache_subnet_group_name is not None:
            input_["cache_subnet_group_name"] = cache_subnet_group_name
        if cache_subnet_group_description is not None:
            input_["cache_subnet_group_description"] = cache_subnet_group_description
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

    async def create_global_replication_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        global_replication_group_id_suffix: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        global_replication_group_description: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        primary_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
    ) -> "capo_elasticache.types.create_global_replication_group_result.CreateGlobalReplicationGroupResult":
        """<p>Global Datastore offers fully managed, fast, reliable and secure cross-region replication. Using Global Datastore with Valkey or Redis OSS, you can create cross-region read replica clusters for ElastiCache to enable low-latency reads and disaster recovery across regions. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Redis-Global-Datastore.html">Replication Across Regions Using Global Datastore</a>. </p> <ul> <li> <p>The <b>GlobalReplicationGroupIdSuffix</b> is the name of the Global datastore.</p> </li> <li> <p>The <b>PrimaryReplicationGroupId</b> represents the name of the primary cluster that accepts writes and will replicate updates to the secondary cluster.</p> </li> </ul>

        Args:
            global_replication_group_id_suffix: <p>The suffix name of a Global datastore. Amazon ElastiCache automatically applies a prefix to the Global datastore ID when it is created. Each Amazon Region has its own prefix. For instance, a Global datastore ID created in the US-West-1 region will begin with "dsdfu" along with the suffix name you provide. The suffix, combined with the auto-generated prefix, guarantees uniqueness of the Global datastore name across multiple regions. </p> <p>For a full list of Amazon Regions and their respective Global datastore iD prefixes, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Redis-Global-Datastores-CLI.html">Using the Amazon CLI with Global datastores </a>.</p>
            global_replication_group_description: <p>Provides details of the Global datastore</p>
            primary_replication_group_id: <p>The name of the primary cluster that accepts writes and will replicate updates to the secondary cluster. This value is stored as a lowercase string.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_elasticache.errors.global_replication_group_already_exists_fault.GlobalReplicationGroupAlreadyExistsFault: <p>The Global datastore name already exists.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.create_global_replication_group_message.CreateGlobalReplicationGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.create_global_replication_group_result.CreateGlobalReplicationGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.create_global_replication_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.create_global_replication_group.async_create_global_replication_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.create_global_replication_group_message.CreateGlobalReplicationGroupMessage = {}
        if global_replication_group_id_suffix is not None:
            input_["global_replication_group_id_suffix"] = (
                global_replication_group_id_suffix
            )
        if global_replication_group_description is not None:
            input_["global_replication_group_description"] = (
                global_replication_group_description
            )
        if primary_replication_group_id is not None:
            input_["primary_replication_group_id"] = primary_replication_group_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_replication_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        replication_group_description: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        global_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        primary_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        automatic_failover_enabled: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        multi_az_enabled: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        num_cache_clusters: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        preferred_cache_cluster_a_zs: Optional[
            "capo_elasticache.types.availability_zones_list.AvailabilityZonesList"
        ] = None,
        num_node_groups: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        replicas_per_node_group: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        node_group_configuration: Optional[
            "capo_elasticache.types.node_group_configuration_list.NodeGroupConfigurationList"
        ] = None,
        cache_node_type: Optional["capo_elasticache.types.string.String"] = None,
        engine: Optional["capo_elasticache.types.string.String"] = None,
        engine_version: Optional["capo_elasticache.types.string.String"] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        cache_subnet_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        cache_security_group_names: Optional[
            "capo_elasticache.types.cache_security_group_name_list.CacheSecurityGroupNameList"
        ] = None,
        security_group_ids: Optional[
            "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
        ] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
        snapshot_arns: Optional[
            "capo_elasticache.types.snapshot_arns_list.SnapshotArnsList"
        ] = None,
        snapshot_name: Optional["capo_elasticache.types.string.String"] = None,
        preferred_maintenance_window: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        port: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        notification_topic_arn: Optional["capo_elasticache.types.string.String"] = None,
        auto_minor_version_upgrade: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        snapshot_retention_limit: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        snapshot_window: Optional["capo_elasticache.types.string.String"] = None,
        auth_token: Optional["capo_elasticache.types.string.String"] = None,
        transit_encryption_enabled: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        at_rest_encryption_enabled: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        kms_key_id: Optional["capo_elasticache.types.string.String"] = None,
        user_group_ids: Optional[
            "capo_elasticache.types.user_group_id_list_input.UserGroupIdListInput"
        ] = None,
        log_delivery_configurations: Optional[
            "capo_elasticache.types.log_delivery_configuration_request_list.LogDeliveryConfigurationRequestList"
        ] = None,
        data_tiering_enabled: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        network_type: Optional[
            "capo_elasticache.types.network_type.NetworkType"
        ] = None,
        ip_discovery: Optional[
            "capo_elasticache.types.ip_discovery.IpDiscovery"
        ] = None,
        transit_encryption_mode: Optional[
            "capo_elasticache.types.transit_encryption_mode.TransitEncryptionMode"
        ] = None,
        cluster_mode: Optional[
            "capo_elasticache.types.cluster_mode.ClusterMode"
        ] = None,
        serverless_cache_snapshot_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        durability: Optional["capo_elasticache.types.durability.Durability"] = None,
    ) -> "capo_elasticache.types.create_replication_group_result.CreateReplicationGroupResult":
        """<p>Creates a Valkey or Redis OSS (cluster mode disabled) or a Valkey or Redis OSS (cluster mode enabled) replication group.</p> <p>This API can be used to create a standalone regional replication group or a secondary replication group associated with a Global datastore.</p> <p>A Valkey or Redis OSS (cluster mode disabled) replication group is a collection of nodes, where one of the nodes is a read/write primary and the others are read-only replicas. Writes to the primary are asynchronously propagated to the replicas.</p> <p>A Valkey or Redis OSS cluster-mode enabled cluster is comprised of from 1 to 90 shards (API/CLI: node groups). Each shard has a primary node and up to 5 read-only replica nodes. The configuration can range from 90 shards and 0 replicas to 15 shards and 5 replicas, which is the maximum number or replicas allowed. </p> <p>The node or shard limit can be increased to a maximum of 500 per cluster if the Valkey or Redis OSS engine version is 5.0.6 or higher. For example, you can choose to configure a 500 node cluster that ranges between 83 shards (one primary and 5 replicas per shard) and 500 shards (single primary and no replicas). Make sure there are enough available IP addresses to accommodate the increase. Common pitfalls include the subnets in the subnet group have too small a CIDR range or the subnets are shared and heavily used by other clusters. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.Creating.html">Creating a Subnet Group</a>. For versions below 5.0.6, the limit is 250 per cluster.</p> <p>To request a limit increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">Amazon Service Limits</a> and choose the limit type <b>Nodes per cluster per instance type</b>. </p> <p>When a Valkey or Redis OSS (cluster mode disabled) replication group has been successfully created, you can add one or more read replicas to it, up to a total of 5 read replicas. If you need to increase or decrease the number of node groups (console: shards), you can use scaling. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Scaling.html">Scaling self-designed clusters</a> in the <i>ElastiCache User Guide</i>.</p> <note> <p>This operation is valid for Valkey and Redis OSS only.</p> </note>

        Args:
            replication_group_id: <p>The replication group identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>A name must contain from 1 to 40 alphanumeric characters or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>A name cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            replication_group_description: <p>A user-created description for the replication group.</p>
            global_replication_group_id: <p>The name of the Global datastore</p>
            primary_cluster_id: <p>The identifier of the cluster that serves as the primary for this replication group. This cluster must already exist and have a status of <code>available</code>.</p> <p>This parameter is not required if <code>NumCacheClusters</code>, <code>NumNodeGroups</code>, or <code>ReplicasPerNodeGroup</code> is specified.</p>
            automatic_failover_enabled: <p>Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.</p> <p> <code>AutomaticFailoverEnabled</code> must be enabled for Valkey or Redis OSS (cluster mode enabled) replication groups.</p> <p>Default: false</p>
            multi_az_enabled: <p>A flag indicating if you have Multi-AZ enabled to enhance fault tolerance. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html">Minimizing Downtime: Multi-AZ</a>.</p>
            num_cache_clusters: <p>The number of clusters this replication group initially has.</p> <p>This parameter is not used if there is more than one node group (shard). You should use <code>ReplicasPerNodeGroup</code> instead.</p> <p>If <code>AutomaticFailoverEnabled</code> is <code>true</code>, the value of this parameter must be at least 2. If <code>AutomaticFailoverEnabled</code> is <code>false</code> you can omit this parameter (it will default to 1), or you can explicitly set it to a value between 2 and 6.</p> <p>The maximum permitted value for <code>NumCacheClusters</code> is 6 (1 primary plus 5 replicas).</p>
            preferred_cache_cluster_a_zs: <p>A list of EC2 Availability Zones in which the replication group's clusters are created. The order of the Availability Zones in the list is the order in which clusters are allocated. The primary cluster is created in the first AZ in the list.</p> <p>This parameter is not used if there is more than one node group (shard). You should use <code>NodeGroupConfiguration</code> instead.</p> <note> <p>If you are creating your replication group in an Amazon VPC (recommended), you can only locate clusters in Availability Zones associated with the subnets in the selected subnet group.</p> <p>The number of Availability Zones listed must equal the value of <code>NumCacheClusters</code>.</p> </note> <p>Default: system chosen Availability Zones.</p>
            num_node_groups: <p>An optional parameter that specifies the number of node groups (shards) for this Valkey or Redis OSS (cluster mode enabled) replication group. For Valkey or Redis OSS (cluster mode disabled) either omit this parameter or set it to 1.</p> <p>Default: 1</p>
            replicas_per_node_group: <p>An optional parameter that specifies the number of replica nodes in each node group (shard). Valid values are 0 to 5.</p>
            node_group_configuration: <p>A list of node group (shard) configuration options. Each node group (shard) configuration has the following members: <code>PrimaryAvailabilityZone</code>, <code>ReplicaAvailabilityZones</code>, <code>ReplicaCount</code>, and <code>Slots</code>.</p> <p>If you're creating a Valkey or Redis OSS (cluster mode disabled) or a Valkey or Redis OSS (cluster mode enabled) replication group, you can use this parameter to individually configure each node group (shard), or you can omit this parameter. However, it is required when seeding a Valkey or Redis OSS (cluster mode enabled) cluster from a S3 rdb file. You must configure each node group (shard) using this parameter because you must specify the slots for each node group.</p>
            cache_node_type: <p>The compute and memory capacity of the nodes in the node group (shard).</p> <p>The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.</p> <ul> <li> <p>General purpose:</p> <ul> <li> <p>Current generation: </p> <p> <b>M7g node types</b>: <code>cache.m7g.large</code>, <code>cache.m7g.xlarge</code>, <code>cache.m7g.2xlarge</code>, <code>cache.m7g.4xlarge</code>, <code>cache.m7g.8xlarge</code>, <code>cache.m7g.12xlarge</code>, <code>cache.m7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>M6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.m6g.large</code>, <code>cache.m6g.xlarge</code>, <code>cache.m6g.2xlarge</code>, <code>cache.m6g.4xlarge</code>, <code>cache.m6g.8xlarge</code>, <code>cache.m6g.12xlarge</code>, <code>cache.m6g.16xlarge</code> </p> <p> <b>M5 node types:</b> <code>cache.m5.large</code>, <code>cache.m5.xlarge</code>, <code>cache.m5.2xlarge</code>, <code>cache.m5.4xlarge</code>, <code>cache.m5.12xlarge</code>, <code>cache.m5.24xlarge</code> </p> <p> <b>M4 node types:</b> <code>cache.m4.large</code>, <code>cache.m4.xlarge</code>, <code>cache.m4.2xlarge</code>, <code>cache.m4.4xlarge</code>, <code>cache.m4.10xlarge</code> </p> <p> <b>T4g node types</b> (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): <code>cache.t4g.micro</code>, <code>cache.t4g.small</code>, <code>cache.t4g.medium</code> </p> <p> <b>T3 node types:</b> <code>cache.t3.micro</code>, <code>cache.t3.small</code>, <code>cache.t3.medium</code> </p> <p> <b>T2 node types:</b> <code>cache.t2.micro</code>, <code>cache.t2.small</code>, <code>cache.t2.medium</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>T1 node types:</b> <code>cache.t1.micro</code> </p> <p> <b>M1 node types:</b> <code>cache.m1.small</code>, <code>cache.m1.medium</code>, <code>cache.m1.large</code>, <code>cache.m1.xlarge</code> </p> <p> <b>M3 node types:</b> <code>cache.m3.medium</code>, <code>cache.m3.large</code>, <code>cache.m3.xlarge</code>, <code>cache.m3.2xlarge</code> </p> </li> </ul> </li> <li> <p>Compute optimized:</p> <ul> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>C1 node types:</b> <code>cache.c1.xlarge</code> </p> </li> </ul> </li> <li> <p>Memory optimized:</p> <ul> <li> <p>Current generation: </p> <p> <b>R7g node types</b>: <code>cache.r7g.large</code>, <code>cache.r7g.xlarge</code>, <code>cache.r7g.2xlarge</code>, <code>cache.r7g.4xlarge</code>, <code>cache.r7g.8xlarge</code>, <code>cache.r7g.12xlarge</code>, <code>cache.r7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>R6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.r6g.large</code>, <code>cache.r6g.xlarge</code>, <code>cache.r6g.2xlarge</code>, <code>cache.r6g.4xlarge</code>, <code>cache.r6g.8xlarge</code>, <code>cache.r6g.12xlarge</code>, <code>cache.r6g.16xlarge</code> </p> <p> <b>R5 node types:</b> <code>cache.r5.large</code>, <code>cache.r5.xlarge</code>, <code>cache.r5.2xlarge</code>, <code>cache.r5.4xlarge</code>, <code>cache.r5.12xlarge</code>, <code>cache.r5.24xlarge</code> </p> <p> <b>R4 node types:</b> <code>cache.r4.large</code>, <code>cache.r4.xlarge</code>, <code>cache.r4.2xlarge</code>, <code>cache.r4.4xlarge</code>, <code>cache.r4.8xlarge</code>, <code>cache.r4.16xlarge</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>M2 node types:</b> <code>cache.m2.xlarge</code>, <code>cache.m2.2xlarge</code>, <code>cache.m2.4xlarge</code> </p> <p> <b>R3 node types:</b> <code>cache.r3.large</code>, <code>cache.r3.xlarge</code>, <code>cache.r3.2xlarge</code>, <code>cache.r3.4xlarge</code>, <code>cache.r3.8xlarge</code> </p> </li> </ul> </li> </ul> <p> <b>Additional node type info</b> </p> <ul> <li> <p>All current generation instance types are created in Amazon VPC by default.</p> </li> <li> <p>Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.</p> </li> <li> <p>Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.</p> </li> <li> <p>The configuration variables <code>appendonly</code> and <code>appendfsync</code> are not supported on Valkey, or on Redis OSS version 2.8.22 and later.</p> </li> </ul>
            engine: <p>The name of the cache engine to be used for the clusters in this replication group. The value must be set to <code>valkey</code> or <code>redis</code>.</p>
            engine_version: <p>The version number of the cache engine to be used for the clusters in this replication group. To view the supported cache engine versions, use the <code>DescribeCacheEngineVersions</code> operation.</p> <p> <b>Important:</b> You can upgrade to a newer engine version (see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement">Selecting a Cache Engine and Version</a>) in the <i>ElastiCache User Guide</i>, but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version. </p>
            cache_parameter_group_name: <p>The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.</p> <p>If you are running Valkey or Redis OSS version 3.2.4 or later, only one node group (shard), and want to use a default parameter group, we recommend that you specify the parameter group by name. </p> <ul> <li> <p>To create a Valkey or Redis OSS (cluster mode disabled) replication group, use <code>CacheParameterGroupName=default.redis3.2</code>.</p> </li> <li> <p>To create a Valkey or Redis OSS (cluster mode enabled) replication group, use <code>CacheParameterGroupName=default.redis3.2.cluster.on</code>.</p> </li> </ul>
            cache_subnet_group_name: <p>The name of the cache subnet group to be used for the replication group.</p> <important> <p>If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.html">Subnets and Subnet Groups</a>.</p> </important>
            cache_security_group_names: <p>A list of cache security group names to associate with this replication group.</p>
            security_group_ids: <p>One or more Amazon VPC security groups associated with this replication group.</p> <p>Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC).</p>
            tags: <p>A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key=<code>myKey</code>, Value=<code>myKeyValue</code>. You can include multiple tags as shown following: Key=<code>myKey</code>, Value=<code>myKeyValue</code> Key=<code>mySecondKey</code>, Value=<code>mySecondKeyValue</code>. Tags on replication groups will be replicated to all nodes.</p>
            snapshot_arns: <p>A list of Amazon Resource Names (ARN) that uniquely identify the Valkey or Redis OSS RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new replication group. The Amazon S3 object name in the ARN cannot contain any commas. The new replication group will have the number of node groups (console: shards) specified by the parameter <i>NumNodeGroups</i> or the number of node groups configured by <i>NodeGroupConfiguration</i> regardless of the number of ARNs specified here.</p> <p>Example of an Amazon S3 ARN: <code>arn:aws:s3:::my_bucket/snapshot1.rdb</code> </p>
            snapshot_name: <p>The name of a snapshot from which to restore data into the new replication group. The snapshot status changes to <code>restoring</code> while the new replication group is being created.</p>
            preferred_maintenance_window: <p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>
            port: <p>The port number on which each member of the replication group accepts connections.</p>
            notification_topic_arn: <p>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.</p> <note> <p>The Amazon SNS topic owner must be the same as the cluster owner.</p> </note>
            auto_minor_version_upgrade: <p> If you are running Valkey 7.2 and above or Redis OSS engine version 6.0 and above, set this parameter to yes to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions. </p>
            snapshot_retention_limit: <p>The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set <code>SnapshotRetentionLimit</code> to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p> <p>Default: 0 (i.e., automatic backups are disabled for this cluster).</p>
            snapshot_window: <p>The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).</p> <p>Example: <code>05:00-09:00</code> </p> <p>If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.</p>
            auth_token: <p> <b>Reserved parameter.</b> The password used to access a password protected server.</p> <p> <code>AuthToken</code> can be specified only on replication groups where <code>TransitEncryptionEnabled</code> is <code>true</code>.</p> <important> <p>For HIPAA compliance, you must specify <code>TransitEncryptionEnabled</code> as <code>true</code>, an <code>AuthToken</code>, and a <code>CacheSubnetGroup</code>.</p> </important> <p>Password constraints:</p> <ul> <li> <p>Must be only printable ASCII characters.</p> </li> <li> <p>Must be at least 16 characters and no more than 128 characters in length.</p> </li> <li> <p>The only permitted printable special characters are !, &, #, $, ^, <, >, and -. Other printable special characters cannot be used in the AUTH token.</p> </li> </ul> <p>For more information, see <a href="http://redis.io/commands/AUTH">AUTH password</a> at http://redis.io/commands/AUTH.</p>
            transit_encryption_enabled: <p>A flag that enables in-transit encryption when set to <code>true</code>.</p> <p>This parameter is valid only if the <code>Engine</code> parameter is <code>redis</code>, the <code>EngineVersion</code> parameter is <code>3.2.6</code>, <code>4.x</code> or later, and the cluster is being created in an Amazon VPC.</p> <p>If you enable in-transit encryption, you must also specify a value for <code>CacheSubnetGroup</code>.</p> <p> <b>Required:</b> Only available when creating a replication group in an Amazon VPC using Redis OSS version <code>3.2.6</code>, <code>4.x</code> or later.</p> <p>Default: <code>false</code> </p> <important> <p>For HIPAA compliance, you must specify <code>TransitEncryptionEnabled</code> as <code>true</code>, an <code>AuthToken</code>, and a <code>CacheSubnetGroup</code>.</p> </important>
            at_rest_encryption_enabled: <p>A flag that enables encryption at-rest on the replication group when set to <code>true</code>. In some cases, encryption at-rest may be enabled even when this value is false. Use <code>StorageEncryptionType</code> to view the effective encryption state of a cluster.</p> <p>You cannot modify the value of <code>AtRestEncryptionEnabled</code> after the replication group is created.</p> <p>Default: <code>true</code> when using Valkey, <code>false</code> when using Redis OSS</p>
            kms_key_id: <p>The ID of the KMS key used to encrypt the disk in the cluster.</p>
            user_group_ids: <p>The user group to associate with the replication group.</p>
            log_delivery_configurations: <p>Specifies the destination, format and type of the logs.</p>
            data_tiering_enabled: <p>Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html">Data tiering</a>.</p>
            network_type: <p>Must be either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>
            ip_discovery: <p>The network type you choose when creating a replication group, either <code>ipv4</code> | <code>ipv6</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>
            transit_encryption_mode: <p>A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.</p> <p>When setting <code>TransitEncryptionEnabled</code> to <code>true</code>, you can set your <code>TransitEncryptionMode</code> to <code>preferred</code> in the same request, to allow both encrypted and unencrypted connections at the same time. Once you migrate all your Valkey or Redis OSS clients to use encrypted connections you can modify the value to <code>required</code> to allow encrypted connections only.</p> <p>Setting <code>TransitEncryptionMode</code> to <code>required</code> is a two-step process that requires you to first set the <code>TransitEncryptionMode</code> to <code>preferred</code>, after that you can set <code>TransitEncryptionMode</code> to <code>required</code>.</p> <p>This process will not trigger the replacement of the replication group.</p>
            cluster_mode: <p>Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled.</p>
            serverless_cache_snapshot_name: <p>The name of the snapshot used to create a replication group. Available for Valkey, Redis OSS only.</p>
            durability: <p>Specifies the durability setting for the replication group. When set to <code>default</code>, the service determines the effective durability based on the engine version, cluster mode, and other parameters. The resolved setting is reflected in the <code>EffectiveDurability</code> property of the replication group. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/durability.html">Durability</a>.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault: <p>The requested cache security group name does not refer to an existing cache security group.</p>
            capo_elasticache.errors.cache_subnet_group_not_found_fault.CacheSubnetGroupNotFoundFault: <p>The requested cache subnet group name does not refer to an existing cache subnet group.</p>
            capo_elasticache.errors.cluster_quota_for_customer_exceeded_fault.ClusterQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the allowed number of clusters per customer.</p>
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.insufficient_cache_cluster_capacity_fault.InsufficientCacheClusterCapacityFault: <p>The requested cache node type is not available in the specified Availability Zone. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ErrorMessages.html#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY">InsufficientCacheClusterCapacity</a> in the ElastiCache User Guide.</p>
            capo_elasticache.errors.invalid_cache_cluster_state_fault.InvalidCacheClusterStateFault: <p>The requested cluster is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_global_replication_group_state_fault.InvalidGlobalReplicationGroupStateFault: <p>The Global datastore is not available or in primary-only state.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_user_group_state_fault.InvalidUserGroupStateFault: <p>The user group is not in an active state.</p>
            capo_elasticache.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The VPC network is in an invalid state.</p>
            capo_elasticache.errors.node_groups_per_replication_group_quota_exceeded_fault.NodeGroupsPerReplicationGroupQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum allowed number of node groups (shards) in a single replication group. The default maximum is 90</p>
            capo_elasticache.errors.node_quota_for_cluster_exceeded_fault.NodeQuotaForClusterExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache nodes in a single cluster.</p>
            capo_elasticache.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache nodes per customer.</p>
            capo_elasticache.errors.replication_group_already_exists_fault.ReplicationGroupAlreadyExistsFault: <p>The specified replication group already exists.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.user_group_not_found_fault.UserGroupNotFoundFault: <p>The user group was not found or does not exist</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateCacheReplicationGroup
            Creates a Redis replication group with 3 nodes.

            >>> await client.create_replication_group(replication_group_id='my-redis-rg', replication_group_description='A Redis replication group.', automatic_failover_enabled=True, num_cache_clusters=3, cache_node_type='cache.m3.medium', engine='redis', engine_version='2.8.24', snapshot_retention_limit=30)
            CreateReplicationGroup
            Creates a Redis (cluster mode enabled) replication group with two shards. One shard has one read replica node and the other shard has two read replicas.

            >>> await client.create_replication_group(replication_group_id='clustered-redis-rg', replication_group_description='A multi-sharded replication group', num_node_groups=2, node_group_configuration=[{'Slots': '0-8999', 'PrimaryAvailabilityZone': 'us-east-1c', 'ReplicaCount': 1, 'ReplicaAvailabilityZones': ['us-east-1b']}, {'Slots': '9000-16383', 'PrimaryAvailabilityZone': 'us-east-1a', 'ReplicaCount': 2, 'ReplicaAvailabilityZones': ['us-east-1a', 'us-east-1c']}], cache_node_type='cache.m3.medium', engine='redis', engine_version='3.2.4', cache_parameter_group_name='default.redis3.2.cluster.on', auto_minor_version_upgrade=True, snapshot_retention_limit=8)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.create_replication_group_message.CreateReplicationGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.create_replication_group_result.CreateReplicationGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.create_replication_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.create_replication_group.async_create_replication_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.create_replication_group_message.CreateReplicationGroupMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if replication_group_description is not None:
            input_["replication_group_description"] = replication_group_description
        if global_replication_group_id is not None:
            input_["global_replication_group_id"] = global_replication_group_id
        if primary_cluster_id is not None:
            input_["primary_cluster_id"] = primary_cluster_id
        if automatic_failover_enabled is not None:
            input_["automatic_failover_enabled"] = automatic_failover_enabled
        if multi_az_enabled is not None:
            input_["multi_az_enabled"] = multi_az_enabled
        if num_cache_clusters is not None:
            input_["num_cache_clusters"] = num_cache_clusters
        if preferred_cache_cluster_a_zs is not None:
            input_["preferred_cache_cluster_a_zs"] = preferred_cache_cluster_a_zs
        if num_node_groups is not None:
            input_["num_node_groups"] = num_node_groups
        if replicas_per_node_group is not None:
            input_["replicas_per_node_group"] = replicas_per_node_group
        if node_group_configuration is not None:
            input_["node_group_configuration"] = node_group_configuration
        if cache_node_type is not None:
            input_["cache_node_type"] = cache_node_type
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if cache_parameter_group_name is not None:
            input_["cache_parameter_group_name"] = cache_parameter_group_name
        if cache_subnet_group_name is not None:
            input_["cache_subnet_group_name"] = cache_subnet_group_name
        if cache_security_group_names is not None:
            input_["cache_security_group_names"] = cache_security_group_names
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if snapshot_arns is not None:
            input_["snapshot_arns"] = snapshot_arns
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if port is not None:
            input_["port"] = port
        if notification_topic_arn is not None:
            input_["notification_topic_arn"] = notification_topic_arn
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if snapshot_retention_limit is not None:
            input_["snapshot_retention_limit"] = snapshot_retention_limit
        if snapshot_window is not None:
            input_["snapshot_window"] = snapshot_window
        if auth_token is not None:
            input_["auth_token"] = auth_token
        if transit_encryption_enabled is not None:
            input_["transit_encryption_enabled"] = transit_encryption_enabled
        if at_rest_encryption_enabled is not None:
            input_["at_rest_encryption_enabled"] = at_rest_encryption_enabled
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if user_group_ids is not None:
            input_["user_group_ids"] = user_group_ids
        if log_delivery_configurations is not None:
            input_["log_delivery_configurations"] = log_delivery_configurations
        if data_tiering_enabled is not None:
            input_["data_tiering_enabled"] = data_tiering_enabled
        if network_type is not None:
            input_["network_type"] = network_type
        if ip_discovery is not None:
            input_["ip_discovery"] = ip_discovery
        if transit_encryption_mode is not None:
            input_["transit_encryption_mode"] = transit_encryption_mode
        if cluster_mode is not None:
            input_["cluster_mode"] = cluster_mode
        if serverless_cache_snapshot_name is not None:
            input_["serverless_cache_snapshot_name"] = serverless_cache_snapshot_name
        if durability is not None:
            input_["durability"] = durability

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_serverless_cache(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        serverless_cache_name: Optional["capo_elasticache.types.string.String"] = None,
        description: Optional["capo_elasticache.types.string.String"] = None,
        engine: Optional["capo_elasticache.types.string.String"] = None,
        major_engine_version: Optional["capo_elasticache.types.string.String"] = None,
        cache_usage_limits: Optional[
            "capo_elasticache.types.cache_usage_limits.CacheUsageLimits"
        ] = None,
        kms_key_id: Optional["capo_elasticache.types.string.String"] = None,
        security_group_ids: Optional[
            "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
        ] = None,
        snapshot_arns_to_restore: Optional[
            "capo_elasticache.types.snapshot_arns_list.SnapshotArnsList"
        ] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
        user_group_id: Optional["capo_elasticache.types.string.String"] = None,
        subnet_ids: Optional[
            "capo_elasticache.types.subnet_ids_list.SubnetIdsList"
        ] = None,
        snapshot_retention_limit: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        daily_snapshot_time: Optional["capo_elasticache.types.string.String"] = None,
        network_type: Optional[
            "capo_elasticache.types.network_type.NetworkType"
        ] = None,
        connection_type: Optional[
            "capo_elasticache.types.connection_type.ConnectionType"
        ] = None,
    ) -> "capo_elasticache.types.create_serverless_cache_response.CreateServerlessCacheResponse":
        """<p>Creates a serverless cache.</p>

        Args:
            serverless_cache_name: <p>User-provided identifier for the serverless cache. This parameter is stored as a lowercase string.</p>
            description: <p>User-provided description for the serverless cache. The default is NULL, i.e. if no description is provided then an empty string will be returned. The maximum length is 255 characters. </p>
            engine: <p>The name of the cache engine to be used for creating the serverless cache.</p>
            major_engine_version: <p>The version of the cache engine that will be used to create the serverless cache.</p>
            cache_usage_limits: <p>Sets the cache usage limits for storage and ElastiCache Processing Units for the cache.</p>
            kms_key_id: <p>ARN of the customer managed key for encrypting the data at rest. If no KMS key is provided, a default service key is used.</p>
            security_group_ids: <p>A list of the one or more VPC security groups to be associated with the serverless cache. The security group will authorize traffic access for the VPC end-point (private-link). If no other information is given this will be the VPC’s Default Security Group that is associated with the cluster VPC end-point.</p>
            snapshot_arns_to_restore: <p>The ARN(s) of the snapshot that the new serverless cache will be created from. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            tags: <p>The list of tags (key, value) pairs to be added to the serverless cache resource. Default is NULL.</p>
            user_group_id: <p>The identifier of the UserGroup to be associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL.</p>
            subnet_ids: <p>A list of the identifiers of the subnets where the VPC endpoint for the serverless cache will be deployed. All the subnetIds must belong to the same VPC.</p>
            snapshot_retention_limit: <p>The number of days for which ElastiCache retains automatic snapshots before deleting them. Available for Valkey, Redis OSS and Serverless Memcached only. The maximum value allowed is 35 days.</p>
            daily_snapshot_time: <p>The daily time that snapshots will be created from the new serverless cache. By default this number is populated with 0, i.e. no snapshots will be created on an automatic daily basis. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            network_type: <p>The IP protocol version used by the serverless cache. Must be either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. <code>ipv6</code> is only supported with IPv6-only subnets. If not specified, defaults to <code>ipv4</code>, unless all provided subnets are IPv6-only, in which case it defaults to <code>ipv6</code>. </p>
            connection_type: <p>The connection type for the serverless cache. Must be either <code>vpc</code> | <code>public</code>. Use <code>vpc</code> to access the cache through a VPC endpoint, or <code>public</code> to access the cache over the internet. If not specified, defaults to <code>vpc</code>. This value cannot be changed after the serverless cache is created. Setting this to <code>public</code> requires Valkey 9 or above.</p>

        Raises:
            capo_elasticache.errors.invalid_credentials_exception.InvalidCredentialsException: <p>You must enter valid credentials.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_serverless_cache_state_fault.InvalidServerlessCacheStateFault: <p>The account for these credentials is not currently active.</p>
            capo_elasticache.errors.invalid_user_group_state_fault.InvalidUserGroupStateFault: <p>The user group is not in an active state.</p>
            capo_elasticache.errors.serverless_cache_already_exists_fault.ServerlessCacheAlreadyExistsFault: <p>A serverless cache with this name already exists.</p>
            capo_elasticache.errors.serverless_cache_not_found_fault.ServerlessCacheNotFoundFault: <p>The serverless cache was not found or does not exist.</p>
            capo_elasticache.errors.serverless_cache_quota_for_customer_exceeded_fault.ServerlessCacheQuotaForCustomerExceededFault: <p>The number of serverless caches exceeds the customer quota.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.user_group_not_found_fault.UserGroupNotFoundFault: <p>The user group was not found or does not exist</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.create_serverless_cache_request.CreateServerlessCacheRequest]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.create_serverless_cache_response.CreateServerlessCacheResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.create_serverless_cache

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.create_serverless_cache.async_create_serverless_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.create_serverless_cache_request.CreateServerlessCacheRequest = {}
        if serverless_cache_name is not None:
            input_["serverless_cache_name"] = serverless_cache_name
        if description is not None:
            input_["description"] = description
        if engine is not None:
            input_["engine"] = engine
        if major_engine_version is not None:
            input_["major_engine_version"] = major_engine_version
        if cache_usage_limits is not None:
            input_["cache_usage_limits"] = cache_usage_limits
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if snapshot_arns_to_restore is not None:
            input_["snapshot_arns_to_restore"] = snapshot_arns_to_restore
        if tags is not None:
            input_["tags"] = tags
        if user_group_id is not None:
            input_["user_group_id"] = user_group_id
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if snapshot_retention_limit is not None:
            input_["snapshot_retention_limit"] = snapshot_retention_limit
        if daily_snapshot_time is not None:
            input_["daily_snapshot_time"] = daily_snapshot_time
        if network_type is not None:
            input_["network_type"] = network_type
        if connection_type is not None:
            input_["connection_type"] = connection_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_serverless_cache_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        serverless_cache_snapshot_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        serverless_cache_name: Optional["capo_elasticache.types.string.String"] = None,
        kms_key_id: Optional["capo_elasticache.types.string.String"] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
    ) -> "capo_elasticache.types.create_serverless_cache_snapshot_response.CreateServerlessCacheSnapshotResponse":
        """<p>This API creates a copy of an entire ServerlessCache at a specific moment in time. Available for Valkey, Redis OSS and Serverless Memcached only.</p>

        Args:
            serverless_cache_snapshot_name: <p>The name for the snapshot being created. Must be unique for the customer account. Available for Valkey, Redis OSS and Serverless Memcached only. Must be between 1 and 255 characters. This value is stored as a lowercase string.</p>
            serverless_cache_name: <p>The name of an existing serverless cache. The snapshot is created from this cache. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            kms_key_id: <p>The ID of the KMS key used to encrypt the snapshot. Available for Valkey, Redis OSS and Serverless Memcached only. Default: NULL</p>
            tags: <p>A list of tags to be added to the snapshot resource. A tag is a key-value pair. Available for Valkey, Redis OSS and Serverless Memcached only.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_serverless_cache_state_fault.InvalidServerlessCacheStateFault: <p>The account for these credentials is not currently active.</p>
            capo_elasticache.errors.serverless_cache_not_found_fault.ServerlessCacheNotFoundFault: <p>The serverless cache was not found or does not exist.</p>
            capo_elasticache.errors.serverless_cache_snapshot_already_exists_fault.ServerlessCacheSnapshotAlreadyExistsFault: <p>A serverless cache snapshot with this name already exists. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.serverless_cache_snapshot_quota_exceeded_fault.ServerlessCacheSnapshotQuotaExceededFault: <p>The number of serverless cache snapshots exceeds the customer snapshot quota. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.create_serverless_cache_snapshot_request.CreateServerlessCacheSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.create_serverless_cache_snapshot_response.CreateServerlessCacheSnapshotResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.create_serverless_cache_snapshot

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.create_serverless_cache_snapshot.async_create_serverless_cache_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.create_serverless_cache_snapshot_request.CreateServerlessCacheSnapshotRequest = {}
        if serverless_cache_snapshot_name is not None:
            input_["serverless_cache_snapshot_name"] = serverless_cache_snapshot_name
        if serverless_cache_name is not None:
            input_["serverless_cache_name"] = serverless_cache_name
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

    async def create_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        cache_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        snapshot_name: Optional["capo_elasticache.types.string.String"] = None,
        kms_key_id: Optional["capo_elasticache.types.string.String"] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
    ) -> "capo_elasticache.types.create_snapshot_result.CreateSnapshotResult":
        """<p>Creates a copy of an entire cluster or replication group at a specific moment in time.</p> <note> <p>This operation is valid for Valkey or Redis OSS only.</p> </note>

        Args:
            replication_group_id: <p>The identifier of an existing replication group. The snapshot is created from this replication group.</p>
            cache_cluster_id: <p>The identifier of an existing cluster. The snapshot is created from this cluster.</p>
            snapshot_name: <p>A name for the snapshot being created. This value is stored as a lowercase string.</p>
            kms_key_id: <p>The ID of the KMS key used to encrypt the snapshot.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.invalid_cache_cluster_state_fault.InvalidCacheClusterStateFault: <p>The requested cluster is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.snapshot_already_exists_fault.SnapshotAlreadyExistsFault: <p>You already have a snapshot with the given name.</p>
            capo_elasticache.errors.snapshot_feature_not_supported_fault.SnapshotFeatureNotSupportedFault: <p>You attempted one of the following operations:</p> <ul> <li> <p>Creating a snapshot of a Valkey or Redis OSS cluster running on a <code>cache.t1.micro</code> cache node.</p> </li> <li> <p>Creating a snapshot of a cluster that is running Memcached rather than Valkey or Redis OSS.</p> </li> </ul> <p>Neither of these are supported by ElastiCache.</p>
            capo_elasticache.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of snapshots.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateSnapshot - NonClustered Redis, 2 read-replicas
            Creates a snapshot of a non-clustered Redis cluster that has only three nodes, primary and two read-replicas. CacheClusterId must be a specific node in the cluster.

            >>> await client.create_snapshot(cache_cluster_id='threenoderedis-001', snapshot_name='snapshot-2')
            CreateSnapshot - NonClustered Redis, no read-replicas
            Creates a snapshot of a non-clustered Redis cluster that has only one node.

            >>> await client.create_snapshot(cache_cluster_id='onenoderedis', snapshot_name='snapshot-1')
            CreateSnapshot-clustered Redis
            Creates a snapshot of a clustered Redis cluster that has 2 shards, each with a primary and 4 read-replicas.

            >>> await client.create_snapshot(replication_group_id='clusteredredis', snapshot_name='snapshot-2x5')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.create_snapshot_message.CreateSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.create_snapshot_result.CreateSnapshotResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.create_snapshot

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.create_snapshot.async_create_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.create_snapshot_message.CreateSnapshotMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if cache_cluster_id is not None:
            input_["cache_cluster_id"] = cache_cluster_id
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
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

    async def create_user(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        user_id: Optional["capo_elasticache.types.user_id.UserId"] = None,
        user_name: Optional["capo_elasticache.types.user_name.UserName"] = None,
        engine: Optional["capo_elasticache.types.engine_type.EngineType"] = None,
        passwords: Optional[
            "capo_elasticache.types.password_list_input.PasswordListInput"
        ] = None,
        access_string: Optional[
            "capo_elasticache.types.access_string.AccessString"
        ] = None,
        no_password_required: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
        authentication_mode: Optional[
            "capo_elasticache.types.authentication_mode.AuthenticationMode"
        ] = None,
    ) -> "capo_elasticache.types.user.User":
        """<p>For Valkey engine version 7.2 onwards and Redis OSS 6.0 to 7.1: Creates a user. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.RBAC.html">Using Role Based Access Control (RBAC)</a>.</p>

        Args:
            user_id: <p>The ID of the user. This value is stored as a lowercase string.</p>
            user_name: <p>The username of the user.</p>
            engine: <p>The options are valkey or redis. </p>
            passwords: <p>Passwords used for this user. You can create up to two passwords for each user.</p>
            access_string: <p>Access permissions string used for this user.</p>
            no_password_required: <p>Indicates a password is not required for this user.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>
            authentication_mode: <p>Specifies how to authenticate the user.</p>

        Raises:
            capo_elasticache.errors.duplicate_user_name_fault.DuplicateUserNameFault: <p>A user with this username already exists.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.user_already_exists_fault.UserAlreadyExistsFault: <p>A user with this ID already exists.</p>
            capo_elasticache.errors.user_quota_exceeded_fault.UserQuotaExceededFault: <p>The quota of users has been exceeded.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.create_user_message.CreateUserMessage]",
        ) -> AsyncOperationResponse["capo_elasticache.types.user.User"]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.create_user

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.create_user.async_create_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.create_user_message.CreateUserMessage = {}
        if user_id is not None:
            input_["user_id"] = user_id
        if user_name is not None:
            input_["user_name"] = user_name
        if engine is not None:
            input_["engine"] = engine
        if passwords is not None:
            input_["passwords"] = passwords
        if access_string is not None:
            input_["access_string"] = access_string
        if no_password_required is not None:
            input_["no_password_required"] = no_password_required
        if tags is not None:
            input_["tags"] = tags
        if authentication_mode is not None:
            input_["authentication_mode"] = authentication_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_user_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        user_group_id: Optional["capo_elasticache.types.string.String"] = None,
        engine: Optional["capo_elasticache.types.engine_type.EngineType"] = None,
        user_ids: Optional[
            "capo_elasticache.types.user_id_list_input.UserIdListInput"
        ] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
    ) -> "capo_elasticache.types.user_group.UserGroup":
        """<p>For Valkey engine version 7.2 onwards and Redis OSS 6.0 to 7.1: Creates a user group. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.RBAC.html">Using Role Based Access Control (RBAC)</a> </p>

        Args:
            user_group_id: <p>The ID of the user group. This value is stored as a lowercase string.</p>
            engine: <p>Sets the engine listed in a user group. The options are valkey or redis.</p>
            user_ids: <p>The list of user IDs that belong to the user group.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted. Available for Valkey and Redis OSS only.</p>

        Raises:
            capo_elasticache.errors.default_user_required.DefaultUserRequired: <p>You must add default user to a user group.</p>
            capo_elasticache.errors.duplicate_user_name_fault.DuplicateUserNameFault: <p>A user with this username already exists.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.user_group_already_exists_fault.UserGroupAlreadyExistsFault: <p>The user group with this ID already exists.</p>
            capo_elasticache.errors.user_group_quota_exceeded_fault.UserGroupQuotaExceededFault: <p>The number of users exceeds the user group limit.</p>
            capo_elasticache.errors.user_not_found_fault.UserNotFoundFault: <p>The user does not exist or could not be found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.create_user_group_message.CreateUserGroupMessage]",
        ) -> AsyncOperationResponse["capo_elasticache.types.user_group.UserGroup"]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.create_user_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.create_user_group.async_create_user_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.create_user_group_message.CreateUserGroupMessage = {}
        if user_group_id is not None:
            input_["user_group_id"] = user_group_id
        if engine is not None:
            input_["engine"] = engine
        if user_ids is not None:
            input_["user_ids"] = user_ids
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def decrease_node_groups_in_global_replication_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        global_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        node_group_count: Optional["capo_elasticache.types.integer.Integer"] = None,
        global_node_groups_to_remove: Optional[
            "capo_elasticache.types.global_node_group_id_list.GlobalNodeGroupIdList"
        ] = None,
        global_node_groups_to_retain: Optional[
            "capo_elasticache.types.global_node_group_id_list.GlobalNodeGroupIdList"
        ] = None,
        apply_immediately: Optional["capo_elasticache.types.boolean.Boolean"] = None,
    ) -> "capo_elasticache.types.decrease_node_groups_in_global_replication_group_result.DecreaseNodeGroupsInGlobalReplicationGroupResult":
        """<p>Decreases the number of node groups in a Global datastore</p>

        Args:
            global_replication_group_id: <p>The name of the Global datastore</p>
            node_group_count: <p>The number of node groups (shards) that results from the modification of the shard configuration</p>
            global_node_groups_to_remove: <p>If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. GlobalNodeGroupsToRemove is a list of NodeGroupIds to remove from the cluster. ElastiCache will attempt to remove all node groups listed by GlobalNodeGroupsToRemove from the cluster. </p>
            global_node_groups_to_retain: <p>If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. GlobalNodeGroupsToRetain is a list of NodeGroupIds to retain from the cluster. ElastiCache will attempt to retain all node groups listed by GlobalNodeGroupsToRetain from the cluster. </p>
            apply_immediately: <p>Indicates that the shard reconfiguration process begins immediately. At present, the only permitted value for this parameter is true. </p>

        Raises:
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.invalid_global_replication_group_state_fault.InvalidGlobalReplicationGroupStateFault: <p>The Global datastore is not available or in primary-only state.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.decrease_node_groups_in_global_replication_group_message.DecreaseNodeGroupsInGlobalReplicationGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.decrease_node_groups_in_global_replication_group_result.DecreaseNodeGroupsInGlobalReplicationGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.decrease_node_groups_in_global_replication_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.decrease_node_groups_in_global_replication_group.async_decrease_node_groups_in_global_replication_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.decrease_node_groups_in_global_replication_group_message.DecreaseNodeGroupsInGlobalReplicationGroupMessage = {}
        if global_replication_group_id is not None:
            input_["global_replication_group_id"] = global_replication_group_id
        if node_group_count is not None:
            input_["node_group_count"] = node_group_count
        if global_node_groups_to_remove is not None:
            input_["global_node_groups_to_remove"] = global_node_groups_to_remove
        if global_node_groups_to_retain is not None:
            input_["global_node_groups_to_retain"] = global_node_groups_to_retain
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def decrease_replica_count(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        new_replica_count: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        replica_configuration: Optional[
            "capo_elasticache.types.replica_configuration_list.ReplicaConfigurationList"
        ] = None,
        replicas_to_remove: Optional[
            "capo_elasticache.types.remove_replicas_list.RemoveReplicasList"
        ] = None,
        apply_immediately: Optional["capo_elasticache.types.boolean.Boolean"] = None,
    ) -> "capo_elasticache.types.decrease_replica_count_result.DecreaseReplicaCountResult":
        """<p>Dynamically decreases the number of replicas in a Valkey or Redis OSS (cluster mode disabled) replication group or the number of replica nodes in one or more node groups (shards) of a Valkey or Redis OSS (cluster mode enabled) replication group. This operation is performed with no cluster down time.</p>

        Args:
            replication_group_id: <p>The id of the replication group from which you want to remove replica nodes.</p>
            new_replica_count: <p>The number of read replica nodes you want at the completion of this operation. For Valkey or Redis OSS (cluster mode disabled) replication groups, this is the number of replica nodes in the replication group. For Valkey or Redis OSS (cluster mode enabled) replication groups, this is the number of replica nodes in each of the replication group's node groups.</p> <p>The minimum number of replicas in a shard or replication group is:</p> <ul> <li> <p>Valkey or Redis OSS (cluster mode disabled)</p> <ul> <li> <p>If Multi-AZ is enabled: 1</p> </li> <li> <p>If Multi-AZ is not enabled: 0</p> </li> </ul> </li> <li> <p>Valkey or Redis OSS (cluster mode enabled): 0 (though you will not be able to failover to a replica if your primary node fails)</p> </li> </ul>
            replica_configuration: <p>A list of <code>ConfigureShard</code> objects that can be used to configure each shard in a Valkey or Redis OSS replication group. The <code>ConfigureShard</code> has three members: <code>NewReplicaCount</code>, <code>NodeGroupId</code>, and <code>PreferredAvailabilityZones</code>.</p>
            replicas_to_remove: <p>A list of the node ids to remove from the replication group or node group (shard).</p>
            apply_immediately: <p>If <code>True</code>, the number of replica nodes is decreased immediately. <code>ApplyImmediately=False</code> is not currently supported.</p>

        Raises:
            capo_elasticache.errors.cluster_quota_for_customer_exceeded_fault.ClusterQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the allowed number of clusters per customer.</p>
            capo_elasticache.errors.insufficient_cache_cluster_capacity_fault.InsufficientCacheClusterCapacityFault: <p>The requested cache node type is not available in the specified Availability Zone. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ErrorMessages.html#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY">InsufficientCacheClusterCapacity</a> in the ElastiCache User Guide.</p>
            capo_elasticache.errors.invalid_cache_cluster_state_fault.InvalidCacheClusterStateFault: <p>The requested cluster is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The VPC network is in an invalid state.</p>
            capo_elasticache.errors.node_groups_per_replication_group_quota_exceeded_fault.NodeGroupsPerReplicationGroupQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum allowed number of node groups (shards) in a single replication group. The default maximum is 90</p>
            capo_elasticache.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache nodes per customer.</p>
            capo_elasticache.errors.no_operation_fault.NoOperationFault: <p>The operation was not performed because no changes were required.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.decrease_replica_count_message.DecreaseReplicaCountMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.decrease_replica_count_result.DecreaseReplicaCountResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.decrease_replica_count

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.decrease_replica_count.async_decrease_replica_count(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.decrease_replica_count_message.DecreaseReplicaCountMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if new_replica_count is not None:
            input_["new_replica_count"] = new_replica_count
        if replica_configuration is not None:
            input_["replica_configuration"] = replica_configuration
        if replicas_to_remove is not None:
            input_["replicas_to_remove"] = replicas_to_remove
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cache_cluster(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        final_snapshot_identifier: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
    ) -> "capo_elasticache.types.delete_cache_cluster_result.DeleteCacheClusterResult":
        """<p>Deletes a previously provisioned cluster. <code>DeleteCacheCluster</code> deletes all associated cache nodes, node endpoints and the cluster itself. When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the cluster; you cannot cancel or revert this operation.</p> <p>This operation is not valid for:</p> <ul> <li> <p>Valkey or Redis OSS (cluster mode enabled) clusters</p> </li> <li> <p>Valkey or Redis OSS (cluster mode disabled) clusters</p> </li> <li> <p>A cluster that is the last read replica of a replication group</p> </li> <li> <p>A cluster that is the primary node of a replication group</p> </li> <li> <p>A node group (shard) that has Multi-AZ mode enabled</p> </li> <li> <p>A cluster from a Valkey or Redis OSS (cluster mode enabled) replication group</p> </li> <li> <p>A cluster that is not in the <code>available</code> state</p> </li> </ul>

        Args:
            cache_cluster_id: <p>The cluster identifier for the cluster to be deleted. This parameter is not case sensitive.</p>
            final_snapshot_identifier: <p>The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. ElastiCache creates the snapshot, and then deletes the cluster immediately afterward.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.invalid_cache_cluster_state_fault.InvalidCacheClusterStateFault: <p>The requested cluster is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.snapshot_already_exists_fault.SnapshotAlreadyExistsFault: <p>You already have a snapshot with the given name.</p>
            capo_elasticache.errors.snapshot_feature_not_supported_fault.SnapshotFeatureNotSupportedFault: <p>You attempted one of the following operations:</p> <ul> <li> <p>Creating a snapshot of a Valkey or Redis OSS cluster running on a <code>cache.t1.micro</code> cache node.</p> </li> <li> <p>Creating a snapshot of a cluster that is running Memcached rather than Valkey or Redis OSS.</p> </li> </ul> <p>Neither of these are supported by ElastiCache.</p>
            capo_elasticache.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of snapshots.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteCacheCluster
            Deletes an Amazon ElastiCache cluster.

            >>> await client.delete_cache_cluster(cache_cluster_id='my-memcached')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.delete_cache_cluster_message.DeleteCacheClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.delete_cache_cluster_result.DeleteCacheClusterResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.delete_cache_cluster

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.delete_cache_cluster.async_delete_cache_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.delete_cache_cluster_message.DeleteCacheClusterMessage = {}
        if cache_cluster_id is not None:
            input_["cache_cluster_id"] = cache_cluster_id
        if final_snapshot_identifier is not None:
            input_["final_snapshot_identifier"] = final_snapshot_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cache_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
    ) -> None:
        """<p>Deletes the specified cache parameter group. You cannot delete a cache parameter group if it is associated with any cache clusters. You cannot delete the default cache parameter groups in your account.</p>

        Args:
            cache_parameter_group_name: <p>The name of the cache parameter group to delete.</p> <note> <p>The specified cache security group must not be associated with any clusters.</p> </note>

        Raises:
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.invalid_cache_parameter_group_state_fault.InvalidCacheParameterGroupStateFault: <p>The current state of the cache parameter group does not allow the requested operation to occur.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteCacheParameterGroup
            Deletes the Amazon ElastiCache parameter group custom-mem1-4.

            >>> await client.delete_cache_parameter_group(cache_parameter_group_name='custom-mem1-4')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.delete_cache_parameter_group_message.DeleteCacheParameterGroupMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.delete_cache_parameter_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.delete_cache_parameter_group.async_delete_cache_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.delete_cache_parameter_group_message.DeleteCacheParameterGroupMessage = {}
        if cache_parameter_group_name is not None:
            input_["cache_parameter_group_name"] = cache_parameter_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cache_security_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_security_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
    ) -> None:
        """<p>Deletes a cache security group.</p> <note> <p>You cannot delete a cache security group if it is associated with any clusters.</p> </note>

        Args:
            cache_security_group_name: <p>The name of the cache security group to delete.</p> <note> <p>You cannot delete the default security group.</p> </note>

        Raises:
            capo_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault: <p>The requested cache security group name does not refer to an existing cache security group.</p>
            capo_elasticache.errors.invalid_cache_security_group_state_fault.InvalidCacheSecurityGroupStateFault: <p>The current state of the cache security group does not allow deletion.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteCacheSecurityGroup
            Deletes a cache security group.

            >>> await client.delete_cache_security_group(cache_security_group_name='my-sec-group')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.delete_cache_security_group_message.DeleteCacheSecurityGroupMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.delete_cache_security_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.delete_cache_security_group.async_delete_cache_security_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.delete_cache_security_group_message.DeleteCacheSecurityGroupMessage = {}
        if cache_security_group_name is not None:
            input_["cache_security_group_name"] = cache_security_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cache_subnet_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_subnet_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
    ) -> None:
        """<p>Deletes a cache subnet group.</p> <note> <p>You cannot delete a default cache subnet group or one that is associated with any clusters.</p> </note>

        Args:
            cache_subnet_group_name: <p>The name of the cache subnet group to delete.</p> <p>Constraints: Must contain no more than 255 alphanumeric characters or hyphens.</p>

        Raises:
            capo_elasticache.errors.cache_subnet_group_in_use.CacheSubnetGroupInUse: <p>The requested cache subnet group is currently in use.</p>
            capo_elasticache.errors.cache_subnet_group_not_found_fault.CacheSubnetGroupNotFoundFault: <p>The requested cache subnet group name does not refer to an existing cache subnet group.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteCacheSubnetGroup
            Deletes the Amazon ElastiCache subnet group my-subnet-group.

            >>> await client.delete_cache_subnet_group(cache_subnet_group_name='my-subnet-group')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.delete_cache_subnet_group_message.DeleteCacheSubnetGroupMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.delete_cache_subnet_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.delete_cache_subnet_group.async_delete_cache_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.delete_cache_subnet_group_message.DeleteCacheSubnetGroupMessage = {}
        if cache_subnet_group_name is not None:
            input_["cache_subnet_group_name"] = cache_subnet_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_global_replication_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        global_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        retain_primary_replication_group: Optional[
            "capo_elasticache.types.boolean.Boolean"
        ] = None,
    ) -> "capo_elasticache.types.delete_global_replication_group_result.DeleteGlobalReplicationGroupResult":
        """<p>Deleting a Global datastore is a two-step process: </p> <ul> <li> <p>First, you must <a>DisassociateGlobalReplicationGroup</a> to remove the secondary clusters in the Global datastore.</p> </li> <li> <p>Once the Global datastore contains only the primary cluster, you can use the <code>DeleteGlobalReplicationGroup</code> API to delete the Global datastore while retainining the primary cluster using <code>RetainPrimaryReplicationGroup=true</code>.</p> </li> </ul> <p>Since the Global Datastore has only a primary cluster, you can delete the Global Datastore while retaining the primary by setting <code>RetainPrimaryReplicationGroup=true</code>. The primary cluster is never deleted when deleting a Global Datastore. It can only be deleted when it no longer is associated with any Global Datastore.</p> <p>When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operation.</p>

        Args:
            global_replication_group_id: <p>The name of the Global datastore</p>
            retain_primary_replication_group: <p>The primary replication group is retained as a standalone replication group. </p>

        Raises:
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.invalid_global_replication_group_state_fault.InvalidGlobalReplicationGroupStateFault: <p>The Global datastore is not available or in primary-only state.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.delete_global_replication_group_message.DeleteGlobalReplicationGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.delete_global_replication_group_result.DeleteGlobalReplicationGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.delete_global_replication_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.delete_global_replication_group.async_delete_global_replication_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.delete_global_replication_group_message.DeleteGlobalReplicationGroupMessage = {}
        if global_replication_group_id is not None:
            input_["global_replication_group_id"] = global_replication_group_id
        if retain_primary_replication_group is not None:
            input_["retain_primary_replication_group"] = (
                retain_primary_replication_group
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_replication_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        retain_primary_cluster: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        final_snapshot_identifier: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
    ) -> "capo_elasticache.types.delete_replication_group_result.DeleteReplicationGroupResult":
        """<p>Deletes an existing replication group. By default, this operation deletes the entire replication group, including the primary/primaries and all of the read replicas. If the replication group has only one primary, you can optionally delete only the read replicas, while retaining the primary by setting <code>RetainPrimaryCluster=true</code>.</p> <p>When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operation.</p> <note> <ul> <li> <p> <code>CreateSnapshot</code> permission is required to create a final snapshot. Without this permission, the API call will fail with an <code>Access Denied</code> exception.</p> </li> <li> <p>This operation is valid for Redis OSS only.</p> </li> </ul> </note>

        Args:
            replication_group_id: <p>The identifier for the cluster to be deleted. This parameter is not case sensitive.</p>
            retain_primary_cluster: <p>If set to <code>true</code>, all of the read replicas are deleted, but the primary node is retained.</p>
            final_snapshot_identifier: <p>The name of a final node group (shard) snapshot. ElastiCache creates the snapshot from the primary node in the cluster, rather than one of the replicas; this is to ensure that it captures the freshest data. After the final snapshot is taken, the replication group is immediately deleted.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.snapshot_already_exists_fault.SnapshotAlreadyExistsFault: <p>You already have a snapshot with the given name.</p>
            capo_elasticache.errors.snapshot_feature_not_supported_fault.SnapshotFeatureNotSupportedFault: <p>You attempted one of the following operations:</p> <ul> <li> <p>Creating a snapshot of a Valkey or Redis OSS cluster running on a <code>cache.t1.micro</code> cache node.</p> </li> <li> <p>Creating a snapshot of a cluster that is running Memcached rather than Valkey or Redis OSS.</p> </li> </ul> <p>Neither of these are supported by ElastiCache.</p>
            capo_elasticache.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of snapshots.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteReplicationGroup
            Deletes the Amazon ElastiCache replication group my-redis-rg.

            >>> await client.delete_replication_group(replication_group_id='my-redis-rg', retain_primary_cluster=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.delete_replication_group_message.DeleteReplicationGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.delete_replication_group_result.DeleteReplicationGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.delete_replication_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.delete_replication_group.async_delete_replication_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.delete_replication_group_message.DeleteReplicationGroupMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if retain_primary_cluster is not None:
            input_["retain_primary_cluster"] = retain_primary_cluster
        if final_snapshot_identifier is not None:
            input_["final_snapshot_identifier"] = final_snapshot_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_serverless_cache(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        serverless_cache_name: Optional["capo_elasticache.types.string.String"] = None,
        final_snapshot_name: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.delete_serverless_cache_response.DeleteServerlessCacheResponse":
        """<p>Deletes a specified existing serverless cache.</p> <note> <p> <code>CreateServerlessCacheSnapshot</code> permission is required to create a final snapshot. Without this permission, the API call will fail with an <code>Access Denied</code> exception.</p> </note>

        Args:
            serverless_cache_name: <p>The identifier of the serverless cache to be deleted.</p>
            final_snapshot_name: <p>Name of the final snapshot to be taken before the serverless cache is deleted. Available for Valkey, Redis OSS and Serverless Memcached only. Default: NULL, i.e. a final snapshot is not taken.</p>

        Raises:
            capo_elasticache.errors.invalid_credentials_exception.InvalidCredentialsException: <p>You must enter valid credentials.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_serverless_cache_state_fault.InvalidServerlessCacheStateFault: <p>The account for these credentials is not currently active.</p>
            capo_elasticache.errors.serverless_cache_not_found_fault.ServerlessCacheNotFoundFault: <p>The serverless cache was not found or does not exist.</p>
            capo_elasticache.errors.serverless_cache_snapshot_already_exists_fault.ServerlessCacheSnapshotAlreadyExistsFault: <p>A serverless cache snapshot with this name already exists. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.delete_serverless_cache_request.DeleteServerlessCacheRequest]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.delete_serverless_cache_response.DeleteServerlessCacheResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.delete_serverless_cache

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.delete_serverless_cache.async_delete_serverless_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.delete_serverless_cache_request.DeleteServerlessCacheRequest = {}
        if serverless_cache_name is not None:
            input_["serverless_cache_name"] = serverless_cache_name
        if final_snapshot_name is not None:
            input_["final_snapshot_name"] = final_snapshot_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_serverless_cache_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        serverless_cache_snapshot_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
    ) -> "capo_elasticache.types.delete_serverless_cache_snapshot_response.DeleteServerlessCacheSnapshotResponse":
        """<p>Deletes an existing serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.</p>

        Args:
            serverless_cache_snapshot_name: <p>Idenfitier of the snapshot to be deleted. Available for Valkey, Redis OSS and Serverless Memcached only.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_serverless_cache_snapshot_state_fault.InvalidServerlessCacheSnapshotStateFault: <p>The state of the serverless cache snapshot was not received. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.serverless_cache_snapshot_not_found_fault.ServerlessCacheSnapshotNotFoundFault: <p>This serverless cache snapshot could not be found or does not exist. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.delete_serverless_cache_snapshot_request.DeleteServerlessCacheSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.delete_serverless_cache_snapshot_response.DeleteServerlessCacheSnapshotResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.delete_serverless_cache_snapshot

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.delete_serverless_cache_snapshot.async_delete_serverless_cache_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.delete_serverless_cache_snapshot_request.DeleteServerlessCacheSnapshotRequest = {}
        if serverless_cache_snapshot_name is not None:
            input_["serverless_cache_snapshot_name"] = serverless_cache_snapshot_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        snapshot_name: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.delete_snapshot_result.DeleteSnapshotResult":
        """<p>Deletes an existing snapshot. When you receive a successful response from this operation, ElastiCache immediately begins deleting the snapshot; you cannot cancel or revert this operation.</p> <note> <p>This operation is valid for Valkey or Redis OSS only.</p> </note>

        Args:
            snapshot_name: <p>The name of the snapshot to be deleted.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_snapshot_state_fault.InvalidSnapshotStateFault: <p>The current state of the snapshot does not allow the requested operation to occur.</p>
            capo_elasticache.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The requested snapshot name does not refer to an existing snapshot.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteSnapshot
            Deletes the Redis snapshot snapshot-20160822.

            >>> await client.delete_snapshot(snapshot_name='snapshot-20161212')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.delete_snapshot_message.DeleteSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.delete_snapshot_result.DeleteSnapshotResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.delete_snapshot

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.delete_snapshot.async_delete_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.delete_snapshot_message.DeleteSnapshotMessage = {}
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_user(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        user_id: Optional["capo_elasticache.types.user_id.UserId"] = None,
    ) -> "capo_elasticache.types.user.User":
        """<p>For Valkey engine version 7.2 onwards and Redis OSS 6.0 onwards: Deletes a user. The user will be removed from all user groups and in turn removed from all replication groups. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.RBAC.html">Using Role Based Access Control (RBAC)</a>. </p>

        Args:
            user_id: <p>The ID of the user.</p>

        Raises:
            capo_elasticache.errors.default_user_associated_to_user_group_fault.DefaultUserAssociatedToUserGroupFault: <p>The default user assigned to the user group.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_user_state_fault.InvalidUserStateFault: <p>The user is not in active state.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.user_not_found_fault.UserNotFoundFault: <p>The user does not exist or could not be found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.delete_user_message.DeleteUserMessage]",
        ) -> AsyncOperationResponse["capo_elasticache.types.user.User"]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.delete_user

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.delete_user.async_delete_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.delete_user_message.DeleteUserMessage = {}
        if user_id is not None:
            input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_user_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        user_group_id: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.user_group.UserGroup":
        """<p>For Valkey engine version 7.2 onwards and Redis OSS 6.0 onwards: Deletes a user group. The user group must first be disassociated from the replication group before it can be deleted. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.RBAC.html">Using Role Based Access Control (RBAC)</a>. </p>

        Args:
            user_group_id: <p>The ID of the user group.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_user_group_state_fault.InvalidUserGroupStateFault: <p>The user group is not in an active state.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.user_group_not_found_fault.UserGroupNotFoundFault: <p>The user group was not found or does not exist</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.delete_user_group_message.DeleteUserGroupMessage]",
        ) -> AsyncOperationResponse["capo_elasticache.types.user_group.UserGroup"]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.delete_user_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.delete_user_group.async_delete_user_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.delete_user_group_message.DeleteUserGroupMessage = {}
        if user_group_id is not None:
            input_["user_group_id"] = user_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_cache_clusters(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
        show_cache_node_info: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        show_cache_clusters_not_in_replication_groups: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_elasticache.types.cache_cluster_message.CacheClusterMessage":
        """<p>Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cache cluster if a cluster identifier is supplied.</p> <p>By default, abbreviated information about the clusters is returned. You can use the optional <i>ShowCacheNodeInfo</i> flag to retrieve detailed information about the cache nodes associated with the clusters. These details include the DNS address and port for the cache node endpoint.</p> <p>If the cluster is in the <i>creating</i> state, only cluster-level information is displayed until all of the nodes are successfully provisioned.</p> <p>If the cluster is in the <i>deleting</i> state, only cluster-level information is displayed.</p> <p>If cache nodes are currently being added to the cluster, node endpoint information and creation time for the additional nodes are not displayed until they are completely provisioned. When the cluster state is <i>available</i>, the cluster is ready for use.</p> <p>If cache nodes are currently being removed from the cluster, no endpoint information for the removed nodes is displayed.</p>

        Args:
            cache_cluster_id: <p>The user-supplied cluster identifier. If this parameter is specified, only information about that specific cluster is returned. This parameter isn't case sensitive.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>
            show_cache_node_info: <p>An optional flag that can be included in the <code>DescribeCacheCluster</code> request to retrieve information about the individual cache nodes.</p>
            show_cache_clusters_not_in_replication_groups: <p>An optional flag that can be included in the <code>DescribeCacheCluster</code> request to show only nodes (API/CLI: clusters) that are not members of a replication group. In practice, this means Memcached and single node Valkey or Redis OSS clusters.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeCacheClusters
            Lists the details for the cache cluster my-mem-cluster.

            >>> await client.describe_cache_clusters(cache_cluster_id='my-mem-cluster', show_cache_node_info=True)
            DescribeCacheClusters
            Lists the details for up to 50 cache clusters.

            >>> await client.describe_cache_clusters(cache_cluster_id='my-mem-cluster')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_cache_clusters_message.DescribeCacheClustersMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.cache_cluster_message.CacheClusterMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_clusters

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_clusters.async_describe_cache_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_cache_clusters_message.DescribeCacheClustersMessage = {}
        if cache_cluster_id is not None:
            input_["cache_cluster_id"] = cache_cluster_id
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if show_cache_node_info is not None:
            input_["show_cache_node_info"] = show_cache_node_info
        if show_cache_clusters_not_in_replication_groups is not None:
            input_["show_cache_clusters_not_in_replication_groups"] = (
                show_cache_clusters_not_in_replication_groups
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_cache_clusters(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
        show_cache_node_info: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        show_cache_clusters_not_in_replication_groups: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "AsyncIterator[capo_elasticache.types.cache_cluster.CacheCluster]":
        _token = marker
        while True:
            _response = await self.describe_cache_clusters(
                config_overrides=config_overrides,
                cache_cluster_id=cache_cluster_id,
                max_records=max_records,
                marker=_token,
                show_cache_node_info=show_cache_node_info,
                show_cache_clusters_not_in_replication_groups=show_cache_clusters_not_in_replication_groups,
            )
            _page = _resolve_path(_response, ("cache_clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_cache_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        engine: Optional["capo_elasticache.types.string.String"] = None,
        engine_version: Optional["capo_elasticache.types.string.String"] = None,
        cache_parameter_group_family: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
        default_only: Optional["capo_elasticache.types.boolean.Boolean"] = None,
    ) -> (
        "capo_elasticache.types.cache_engine_version_message.CacheEngineVersionMessage"
    ):
        """<p>Returns a list of the available cache engines and their versions.</p>

        Args:
            engine: <p>The cache engine to return. Valid values: <code>memcached</code> | <code>redis</code> </p>
            engine_version: <p>The cache engine version to return.</p> <p>Example: <code>1.4.14</code> </p>
            cache_parameter_group_family: <p>The name of a specific cache parameter group family to return details for.</p> <p>Valid values are: <code>memcached1.4</code> | <code>memcached1.5</code> | <code>memcached1.6</code> | <code>redis2.6</code> | <code>redis2.8</code> | <code>redis3.2</code> | <code>redis4.0</code> | <code>redis5.0</code> | <code>redis6.x</code> | <code>redis6.2</code> | <code>redis7</code> | <code>valkey7</code> </p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>
            default_only: <p>If <code>true</code>, specifies that only the default version of the specified engine or engine and major version combination is to be returned.</p>

        Raises:
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeCacheEngineVersions
            Lists the details for up to 25 Memcached and Redis cache engine versions.

            >>> await client.describe_cache_engine_versions()
            DescribeCacheEngineVersions
            Lists the details for up to 50 Redis cache engine versions.

            >>> await client.describe_cache_engine_versions(engine='redis', max_records=50, default_only=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_cache_engine_versions_message.DescribeCacheEngineVersionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.cache_engine_version_message.CacheEngineVersionMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_engine_versions

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_engine_versions.async_describe_cache_engine_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_cache_engine_versions_message.DescribeCacheEngineVersionsMessage = {}
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if cache_parameter_group_family is not None:
            input_["cache_parameter_group_family"] = cache_parameter_group_family
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if default_only is not None:
            input_["default_only"] = default_only

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_cache_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        engine: Optional["capo_elasticache.types.string.String"] = None,
        engine_version: Optional["capo_elasticache.types.string.String"] = None,
        cache_parameter_group_family: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
        default_only: Optional["capo_elasticache.types.boolean.Boolean"] = None,
    ) -> (
        "AsyncIterator[capo_elasticache.types.cache_engine_version.CacheEngineVersion]"
    ):
        _token = marker
        while True:
            _response = await self.describe_cache_engine_versions(
                config_overrides=config_overrides,
                engine=engine,
                engine_version=engine_version,
                cache_parameter_group_family=cache_parameter_group_family,
                max_records=max_records,
                marker=_token,
                default_only=default_only,
            )
            _page = _resolve_path(_response, ("cache_engine_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_cache_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.cache_parameter_groups_message.CacheParameterGroupsMessage":
        """<p>Returns a list of cache parameter group descriptions. If a cache parameter group name is specified, the list contains only the descriptions for that group.</p>

        Args:
            cache_parameter_group_name: <p>The name of a specific cache parameter group to return details for.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeCacheParameterGroups
            Returns a list of cache parameter group descriptions. If a cache parameter group name is specified, the list contains only the descriptions for that group.

            >>> await client.describe_cache_parameter_groups(cache_parameter_group_name='custom-mem1-4')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_cache_parameter_groups_message.DescribeCacheParameterGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.cache_parameter_groups_message.CacheParameterGroupsMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_parameter_groups

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_parameter_groups.async_describe_cache_parameter_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_cache_parameter_groups_message.DescribeCacheParameterGroupsMessage = {}
        if cache_parameter_group_name is not None:
            input_["cache_parameter_group_name"] = cache_parameter_group_name
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

    async def iter_describe_cache_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.cache_parameter_group.CacheParameterGroup]":
        _token = marker
        while True:
            _response = await self.describe_cache_parameter_groups(
                config_overrides=config_overrides,
                cache_parameter_group_name=cache_parameter_group_name,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("cache_parameter_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_cache_parameters(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        source: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.cache_parameter_group_details.CacheParameterGroupDetails":
        """<p>Returns the detailed parameter list for a particular cache parameter group.</p>

        Args:
            cache_parameter_group_name: <p>The name of a specific cache parameter group to return details for.</p>
            source: <p>The parameter types to return.</p> <p>Valid values: <code>user</code> | <code>system</code> | <code>engine-default</code> </p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeCacheParameters
            Lists up to 100 user parameter values for the parameter group custom.redis2.8.

            >>> await client.describe_cache_parameters(cache_parameter_group_name='custom-redis2-8', source='user', max_records=100)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_cache_parameters_message.DescribeCacheParametersMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.cache_parameter_group_details.CacheParameterGroupDetails"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_parameters

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_parameters.async_describe_cache_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_cache_parameters_message.DescribeCacheParametersMessage = {}
        if cache_parameter_group_name is not None:
            input_["cache_parameter_group_name"] = cache_parameter_group_name
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

    async def iter_describe_cache_parameters(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        source: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.parameter.Parameter]":
        _token = marker
        while True:
            _response = await self.describe_cache_parameters(
                config_overrides=config_overrides,
                cache_parameter_group_name=cache_parameter_group_name,
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

    async def describe_cache_security_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_security_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> (
        "capo_elasticache.types.cache_security_group_message.CacheSecurityGroupMessage"
    ):
        """<p>Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group. This applicable only when you have ElastiCache in Classic setup </p>

        Args:
            cache_security_group_name: <p>The name of the cache security group to return details for.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault: <p>The requested cache security group name does not refer to an existing cache security group.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeCacheSecurityGroups
            Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group.

            >>> await client.describe_cache_security_groups(cache_security_group_name='my-sec-group')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_cache_security_groups_message.DescribeCacheSecurityGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.cache_security_group_message.CacheSecurityGroupMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_security_groups

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_security_groups.async_describe_cache_security_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_cache_security_groups_message.DescribeCacheSecurityGroupsMessage = {}
        if cache_security_group_name is not None:
            input_["cache_security_group_name"] = cache_security_group_name
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

    async def iter_describe_cache_security_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_security_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> (
        "AsyncIterator[capo_elasticache.types.cache_security_group.CacheSecurityGroup]"
    ):
        _token = marker
        while True:
            _response = await self.describe_cache_security_groups(
                config_overrides=config_overrides,
                cache_security_group_name=cache_security_group_name,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("cache_security_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_cache_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_subnet_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.cache_subnet_group_message.CacheSubnetGroupMessage":
        """<p>Returns a list of cache subnet group descriptions. If a subnet group name is specified, the list contains only the description of that group. This is applicable only when you have ElastiCache in VPC setup. All ElastiCache clusters now launch in VPC by default. </p>

        Args:
            cache_subnet_group_name: <p>The name of the cache subnet group to return details for.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_elasticache.errors.cache_subnet_group_not_found_fault.CacheSubnetGroupNotFoundFault: <p>The requested cache subnet group name does not refer to an existing cache subnet group.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeCacheSubnetGroups
            Describes up to 25 cache subnet groups.

            >>> await client.describe_cache_subnet_groups(max_records=25)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_cache_subnet_groups_message.DescribeCacheSubnetGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.cache_subnet_group_message.CacheSubnetGroupMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_subnet_groups

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_cache_subnet_groups.async_describe_cache_subnet_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_cache_subnet_groups_message.DescribeCacheSubnetGroupsMessage = {}
        if cache_subnet_group_name is not None:
            input_["cache_subnet_group_name"] = cache_subnet_group_name
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

    async def iter_describe_cache_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_subnet_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.cache_subnet_group.CacheSubnetGroup]":
        _token = marker
        while True:
            _response = await self.describe_cache_subnet_groups(
                config_overrides=config_overrides,
                cache_subnet_group_name=cache_subnet_group_name,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("cache_subnet_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_engine_default_parameters(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_parameter_group_family: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.describe_engine_default_parameters_result.DescribeEngineDefaultParametersResult":
        """<p>Returns the default engine and system parameter information for the specified cache engine.</p>

        Args:
            cache_parameter_group_family: <p>The name of the cache parameter group family.</p> <p>Valid values are: <code>memcached1.4</code> | <code>memcached1.5</code> | <code>memcached1.6</code> | <code>redis2.6</code> | <code>redis2.8</code> | <code>redis3.2</code> | <code>redis4.0</code> | <code>redis5.0</code> | <code>redis6.x</code> | <code>redis6.2</code> | <code>redis7</code> </p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeEngineDefaultParameters
            Returns the default engine and system parameter information for the specified cache engine.

            >>> await client.describe_engine_default_parameters(cache_parameter_group_family='redis2.8', max_records=25)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_engine_default_parameters_message.DescribeEngineDefaultParametersMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.describe_engine_default_parameters_result.DescribeEngineDefaultParametersResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_engine_default_parameters

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_engine_default_parameters.async_describe_engine_default_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_engine_default_parameters_message.DescribeEngineDefaultParametersMessage = {}
        if cache_parameter_group_family is not None:
            input_["cache_parameter_group_family"] = cache_parameter_group_family
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

    async def iter_describe_engine_default_parameters(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_parameter_group_family: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.parameter.Parameter]":
        _token = marker
        while True:
            _response = await self.describe_engine_default_parameters(
                config_overrides=config_overrides,
                cache_parameter_group_family=cache_parameter_group_family,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("engine_defaults", "parameters"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("engine_defaults", "marker"))
            if not _token:
                break

    async def describe_events(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        source_identifier: Optional["capo_elasticache.types.string.String"] = None,
        source_type: Optional["capo_elasticache.types.source_type.SourceType"] = None,
        start_time: Optional["capo_elasticache.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_elasticache.types.t_stamp.TStamp"] = None,
        duration: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.events_message.EventsMessage":
        """<p>Returns events related to clusters, cache security groups, and cache parameter groups. You can obtain events specific to a particular cluster, cache security group, or cache parameter group by providing the name as a parameter.</p> <p>By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days' worth of events if necessary.</p>

        Args:
            source_identifier: <p>The identifier of the event source for which events are returned. If not specified, all sources are included in the response.</p>
            source_type: <p>The event source to retrieve events for. If no value is specified, all events are returned.</p>
            start_time: <p>The beginning of the time interval to retrieve events for, specified in ISO 8601 format.</p> <p> <b>Example:</b> 2017-03-30T07:03:49.555Z</p>
            end_time: <p>The end of the time interval for which to retrieve events, specified in ISO 8601 format.</p> <p> <b>Example:</b> 2017-03-30T07:03:49.555Z</p>
            duration: <p>The number of minutes worth of events to retrieve.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeEvents
            Describes all the cache-cluster events for the past 120 minutes.

            >>> await client.describe_events(source_type='cache-cluster', duration=360)
            DescribeEvents
            Describes all the replication-group events from 3:00P to 5:00P on November 11, 2016.

            >>> await client.describe_events(start_time='2016-12-22T15:00:00.000Z')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_events_message.DescribeEventsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.events_message.EventsMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_events

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_events.async_describe_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_events_message.DescribeEventsMessage = {}
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
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        source_identifier: Optional["capo_elasticache.types.string.String"] = None,
        source_type: Optional["capo_elasticache.types.source_type.SourceType"] = None,
        start_time: Optional["capo_elasticache.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_elasticache.types.t_stamp.TStamp"] = None,
        duration: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.event.Event]":
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

    async def describe_global_replication_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        global_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
        show_member_info: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_elasticache.types.describe_global_replication_groups_result.DescribeGlobalReplicationGroupsResult":
        """<p>Returns information about a particular global replication group. If no identifier is specified, returns information about all Global datastores. </p>

        Args:
            global_replication_group_id: <p>The name of the Global datastore</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved. </p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>
            show_member_info: <p>Returns the list of members that comprise the Global datastore.</p>

        Raises:
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_global_replication_groups_message.DescribeGlobalReplicationGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.describe_global_replication_groups_result.DescribeGlobalReplicationGroupsResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_global_replication_groups

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_global_replication_groups.async_describe_global_replication_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_global_replication_groups_message.DescribeGlobalReplicationGroupsMessage = {}
        if global_replication_group_id is not None:
            input_["global_replication_group_id"] = global_replication_group_id
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if show_member_info is not None:
            input_["show_member_info"] = show_member_info

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_global_replication_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        global_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
        show_member_info: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "AsyncIterator[capo_elasticache.types.global_replication_group.GlobalReplicationGroup]":
        _token = marker
        while True:
            _response = await self.describe_global_replication_groups(
                config_overrides=config_overrides,
                global_replication_group_id=global_replication_group_id,
                max_records=max_records,
                marker=_token,
                show_member_info=show_member_info,
            )
            _page = _resolve_path(_response, ("global_replication_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_replication_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.replication_group_message.ReplicationGroupMessage":
        """<p>Returns information about a particular replication group. If no identifier is specified, <code>DescribeReplicationGroups</code> returns information about all replication groups.</p> <note> <p>This operation is valid for Valkey or Redis OSS only.</p> </note>

        Args:
            replication_group_id: <p>The identifier for the replication group to be described. This parameter is not case sensitive.</p> <p>If you do not specify this parameter, information about all replication groups is returned.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeReplicationGroups
            Returns information about the replication group myreplgroup.

            >>> await client.describe_replication_groups()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_replication_groups_message.DescribeReplicationGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.replication_group_message.ReplicationGroupMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_replication_groups

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_replication_groups.async_describe_replication_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_replication_groups_message.DescribeReplicationGroupsMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
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

    async def iter_describe_replication_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.replication_group.ReplicationGroup]":
        _token = marker
        while True:
            _response = await self.describe_replication_groups(
                config_overrides=config_overrides,
                replication_group_id=replication_group_id,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("replication_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_reserved_cache_nodes(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        reserved_cache_node_id: Optional["capo_elasticache.types.string.String"] = None,
        reserved_cache_nodes_offering_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        cache_node_type: Optional["capo_elasticache.types.string.String"] = None,
        duration: Optional["capo_elasticache.types.string.String"] = None,
        product_description: Optional["capo_elasticache.types.string.String"] = None,
        offering_type: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.reserved_cache_node_message.ReservedCacheNodeMessage":
        """<p>Returns information about reserved cache nodes for this account, or about a specified reserved cache node.</p>

        Args:
            reserved_cache_node_id: <p>The reserved cache node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID.</p>
            reserved_cache_nodes_offering_id: <p>The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier.</p>
            cache_node_type: <p>The cache node type filter value. Use this parameter to show only those reservations matching the specified cache node type.</p> <p>The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.</p> <ul> <li> <p>General purpose:</p> <ul> <li> <p>Current generation: </p> <p> <b>M7g node types</b>: <code>cache.m7g.large</code>, <code>cache.m7g.xlarge</code>, <code>cache.m7g.2xlarge</code>, <code>cache.m7g.4xlarge</code>, <code>cache.m7g.8xlarge</code>, <code>cache.m7g.12xlarge</code>, <code>cache.m7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>M6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.m6g.large</code>, <code>cache.m6g.xlarge</code>, <code>cache.m6g.2xlarge</code>, <code>cache.m6g.4xlarge</code>, <code>cache.m6g.8xlarge</code>, <code>cache.m6g.12xlarge</code>, <code>cache.m6g.16xlarge</code> </p> <p> <b>M5 node types:</b> <code>cache.m5.large</code>, <code>cache.m5.xlarge</code>, <code>cache.m5.2xlarge</code>, <code>cache.m5.4xlarge</code>, <code>cache.m5.12xlarge</code>, <code>cache.m5.24xlarge</code> </p> <p> <b>M4 node types:</b> <code>cache.m4.large</code>, <code>cache.m4.xlarge</code>, <code>cache.m4.2xlarge</code>, <code>cache.m4.4xlarge</code>, <code>cache.m4.10xlarge</code> </p> <p> <b>T4g node types</b> (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): <code>cache.t4g.micro</code>, <code>cache.t4g.small</code>, <code>cache.t4g.medium</code> </p> <p> <b>T3 node types:</b> <code>cache.t3.micro</code>, <code>cache.t3.small</code>, <code>cache.t3.medium</code> </p> <p> <b>T2 node types:</b> <code>cache.t2.micro</code>, <code>cache.t2.small</code>, <code>cache.t2.medium</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>T1 node types:</b> <code>cache.t1.micro</code> </p> <p> <b>M1 node types:</b> <code>cache.m1.small</code>, <code>cache.m1.medium</code>, <code>cache.m1.large</code>, <code>cache.m1.xlarge</code> </p> <p> <b>M3 node types:</b> <code>cache.m3.medium</code>, <code>cache.m3.large</code>, <code>cache.m3.xlarge</code>, <code>cache.m3.2xlarge</code> </p> </li> </ul> </li> <li> <p>Compute optimized:</p> <ul> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>C1 node types:</b> <code>cache.c1.xlarge</code> </p> </li> </ul> </li> <li> <p>Memory optimized:</p> <ul> <li> <p>Current generation: </p> <p> <b>R7g node types</b>: <code>cache.r7g.large</code>, <code>cache.r7g.xlarge</code>, <code>cache.r7g.2xlarge</code>, <code>cache.r7g.4xlarge</code>, <code>cache.r7g.8xlarge</code>, <code>cache.r7g.12xlarge</code>, <code>cache.r7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>R6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.r6g.large</code>, <code>cache.r6g.xlarge</code>, <code>cache.r6g.2xlarge</code>, <code>cache.r6g.4xlarge</code>, <code>cache.r6g.8xlarge</code>, <code>cache.r6g.12xlarge</code>, <code>cache.r6g.16xlarge</code> </p> <p> <b>R5 node types:</b> <code>cache.r5.large</code>, <code>cache.r5.xlarge</code>, <code>cache.r5.2xlarge</code>, <code>cache.r5.4xlarge</code>, <code>cache.r5.12xlarge</code>, <code>cache.r5.24xlarge</code> </p> <p> <b>R4 node types:</b> <code>cache.r4.large</code>, <code>cache.r4.xlarge</code>, <code>cache.r4.2xlarge</code>, <code>cache.r4.4xlarge</code>, <code>cache.r4.8xlarge</code>, <code>cache.r4.16xlarge</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>M2 node types:</b> <code>cache.m2.xlarge</code>, <code>cache.m2.2xlarge</code>, <code>cache.m2.4xlarge</code> </p> <p> <b>R3 node types:</b> <code>cache.r3.large</code>, <code>cache.r3.xlarge</code>, <code>cache.r3.2xlarge</code>, <code>cache.r3.4xlarge</code>, <code>cache.r3.8xlarge</code> </p> </li> </ul> </li> </ul> <p> <b>Additional node type info</b> </p> <ul> <li> <p>All current generation instance types are created in Amazon VPC by default.</p> </li> <li> <p>Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.</p> </li> <li> <p>Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.</p> </li> <li> <p>The configuration variables <code>appendonly</code> and <code>appendfsync</code> are not supported on Valkey, or on Redis OSS version 2.8.22 and later.</p> </li> </ul>
            duration: <p>The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration.</p> <p>Valid Values: <code>1 | 3 | 31536000 | 94608000</code> </p>
            product_description: <p>The product description filter value. Use this parameter to show only those reservations matching the specified product description.</p>
            offering_type: <p>The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.</p> <p>Valid values: <code>"Light Utilization"|"Medium Utilization"|"Heavy Utilization"|"All Upfront"|"Partial Upfront"| "No Upfront"</code> </p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.reserved_cache_node_not_found_fault.ReservedCacheNodeNotFoundFault: <p>The requested reserved cache node was not found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeReservedCacheNodes
            Returns information about reserved cache nodes for this account, or about a specified reserved cache node. If the account has no reserved cache nodes, the operation returns an empty list, as shown here.

            >>> await client.describe_reserved_cache_nodes(max_records=25)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_reserved_cache_nodes_message.DescribeReservedCacheNodesMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.reserved_cache_node_message.ReservedCacheNodeMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_reserved_cache_nodes

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_reserved_cache_nodes.async_describe_reserved_cache_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_reserved_cache_nodes_message.DescribeReservedCacheNodesMessage = {}
        if reserved_cache_node_id is not None:
            input_["reserved_cache_node_id"] = reserved_cache_node_id
        if reserved_cache_nodes_offering_id is not None:
            input_["reserved_cache_nodes_offering_id"] = (
                reserved_cache_nodes_offering_id
            )
        if cache_node_type is not None:
            input_["cache_node_type"] = cache_node_type
        if duration is not None:
            input_["duration"] = duration
        if product_description is not None:
            input_["product_description"] = product_description
        if offering_type is not None:
            input_["offering_type"] = offering_type
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

    async def iter_describe_reserved_cache_nodes(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        reserved_cache_node_id: Optional["capo_elasticache.types.string.String"] = None,
        reserved_cache_nodes_offering_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        cache_node_type: Optional["capo_elasticache.types.string.String"] = None,
        duration: Optional["capo_elasticache.types.string.String"] = None,
        product_description: Optional["capo_elasticache.types.string.String"] = None,
        offering_type: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.reserved_cache_node.ReservedCacheNode]":
        _token = marker
        while True:
            _response = await self.describe_reserved_cache_nodes(
                config_overrides=config_overrides,
                reserved_cache_node_id=reserved_cache_node_id,
                reserved_cache_nodes_offering_id=reserved_cache_nodes_offering_id,
                cache_node_type=cache_node_type,
                duration=duration,
                product_description=product_description,
                offering_type=offering_type,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("reserved_cache_nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_reserved_cache_nodes_offerings(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        reserved_cache_nodes_offering_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        cache_node_type: Optional["capo_elasticache.types.string.String"] = None,
        duration: Optional["capo_elasticache.types.string.String"] = None,
        product_description: Optional["capo_elasticache.types.string.String"] = None,
        offering_type: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.reserved_cache_nodes_offering_message.ReservedCacheNodesOfferingMessage":
        """<p>Lists available reserved cache node offerings.</p>

        Args:
            reserved_cache_nodes_offering_id: <p>The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.</p> <p>Example: <code>438012d3-4052-4cc7-b2e3-8d3372e0e706</code> </p>
            cache_node_type: <p>The cache node type filter value. Use this parameter to show only the available offerings matching the specified cache node type.</p> <p>The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.</p> <ul> <li> <p>General purpose:</p> <ul> <li> <p>Current generation: </p> <p> <b>M7g node types</b>: <code>cache.m7g.large</code>, <code>cache.m7g.xlarge</code>, <code>cache.m7g.2xlarge</code>, <code>cache.m7g.4xlarge</code>, <code>cache.m7g.8xlarge</code>, <code>cache.m7g.12xlarge</code>, <code>cache.m7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>M6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.m6g.large</code>, <code>cache.m6g.xlarge</code>, <code>cache.m6g.2xlarge</code>, <code>cache.m6g.4xlarge</code>, <code>cache.m6g.8xlarge</code>, <code>cache.m6g.12xlarge</code>, <code>cache.m6g.16xlarge</code> </p> <p> <b>M5 node types:</b> <code>cache.m5.large</code>, <code>cache.m5.xlarge</code>, <code>cache.m5.2xlarge</code>, <code>cache.m5.4xlarge</code>, <code>cache.m5.12xlarge</code>, <code>cache.m5.24xlarge</code> </p> <p> <b>M4 node types:</b> <code>cache.m4.large</code>, <code>cache.m4.xlarge</code>, <code>cache.m4.2xlarge</code>, <code>cache.m4.4xlarge</code>, <code>cache.m4.10xlarge</code> </p> <p> <b>T4g node types</b> (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): <code>cache.t4g.micro</code>, <code>cache.t4g.small</code>, <code>cache.t4g.medium</code> </p> <p> <b>T3 node types:</b> <code>cache.t3.micro</code>, <code>cache.t3.small</code>, <code>cache.t3.medium</code> </p> <p> <b>T2 node types:</b> <code>cache.t2.micro</code>, <code>cache.t2.small</code>, <code>cache.t2.medium</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>T1 node types:</b> <code>cache.t1.micro</code> </p> <p> <b>M1 node types:</b> <code>cache.m1.small</code>, <code>cache.m1.medium</code>, <code>cache.m1.large</code>, <code>cache.m1.xlarge</code> </p> <p> <b>M3 node types:</b> <code>cache.m3.medium</code>, <code>cache.m3.large</code>, <code>cache.m3.xlarge</code>, <code>cache.m3.2xlarge</code> </p> </li> </ul> </li> <li> <p>Compute optimized:</p> <ul> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>C1 node types:</b> <code>cache.c1.xlarge</code> </p> </li> </ul> </li> <li> <p>Memory optimized:</p> <ul> <li> <p>Current generation: </p> <p> <b>R7g node types</b>: <code>cache.r7g.large</code>, <code>cache.r7g.xlarge</code>, <code>cache.r7g.2xlarge</code>, <code>cache.r7g.4xlarge</code>, <code>cache.r7g.8xlarge</code>, <code>cache.r7g.12xlarge</code>, <code>cache.r7g.16xlarge</code> </p> <note> <p>For region availability, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion">Supported Node Types</a> </p> </note> <p> <b>R6g node types</b> (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): <code>cache.r6g.large</code>, <code>cache.r6g.xlarge</code>, <code>cache.r6g.2xlarge</code>, <code>cache.r6g.4xlarge</code>, <code>cache.r6g.8xlarge</code>, <code>cache.r6g.12xlarge</code>, <code>cache.r6g.16xlarge</code> </p> <p> <b>R5 node types:</b> <code>cache.r5.large</code>, <code>cache.r5.xlarge</code>, <code>cache.r5.2xlarge</code>, <code>cache.r5.4xlarge</code>, <code>cache.r5.12xlarge</code>, <code>cache.r5.24xlarge</code> </p> <p> <b>R4 node types:</b> <code>cache.r4.large</code>, <code>cache.r4.xlarge</code>, <code>cache.r4.2xlarge</code>, <code>cache.r4.4xlarge</code>, <code>cache.r4.8xlarge</code>, <code>cache.r4.16xlarge</code> </p> </li> <li> <p>Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)</p> <p> <b>M2 node types:</b> <code>cache.m2.xlarge</code>, <code>cache.m2.2xlarge</code>, <code>cache.m2.4xlarge</code> </p> <p> <b>R3 node types:</b> <code>cache.r3.large</code>, <code>cache.r3.xlarge</code>, <code>cache.r3.2xlarge</code>, <code>cache.r3.4xlarge</code>, <code>cache.r3.8xlarge</code> </p> </li> </ul> </li> </ul> <p> <b>Additional node type info</b> </p> <ul> <li> <p>All current generation instance types are created in Amazon VPC by default.</p> </li> <li> <p>Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.</p> </li> <li> <p>Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.</p> </li> <li> <p>The configuration variables <code>appendonly</code> and <code>appendfsync</code> are not supported on Valkey, or on Redis OSS version 2.8.22 and later.</p> </li> </ul>
            duration: <p>Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.</p> <p>Valid Values: <code>1 | 3 | 31536000 | 94608000</code> </p>
            product_description: <p>The product description filter value. Use this parameter to show only the available offerings matching the specified product description.</p>
            offering_type: <p>The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.</p> <p>Valid Values: <code>"Light Utilization"|"Medium Utilization"|"Heavy Utilization" |"All Upfront"|"Partial Upfront"| "No Upfront"</code> </p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.reserved_cache_nodes_offering_not_found_fault.ReservedCacheNodesOfferingNotFoundFault: <p>The requested cache node offering does not exist.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeReseredCacheNodeOfferings
            Lists available reserved cache node offerings for cache.r3.large nodes with a 3 year commitment.

            >>> await client.describe_reserved_cache_nodes_offerings(reserved_cache_nodes_offering_id='', cache_node_type='cache.r3.large', duration='3', offering_type='Light Utilization', max_records=25)
            DescribeReseredCacheNodeOfferings
            Lists available reserved cache node offerings.

            >>> await client.describe_reserved_cache_nodes_offerings(max_records=20)
            DescribeReseredCacheNodeOfferings
            Lists available reserved cache node offerings.

            >>> await client.describe_reserved_cache_nodes_offerings(reserved_cache_nodes_offering_id='438012d3-4052-4cc7-b2e3-8d3372e0e706', cache_node_type='', duration='', product_description='', offering_type='', max_records=25, marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_reserved_cache_nodes_offerings_message.DescribeReservedCacheNodesOfferingsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.reserved_cache_nodes_offering_message.ReservedCacheNodesOfferingMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_reserved_cache_nodes_offerings

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_reserved_cache_nodes_offerings.async_describe_reserved_cache_nodes_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_reserved_cache_nodes_offerings_message.DescribeReservedCacheNodesOfferingsMessage = {}
        if reserved_cache_nodes_offering_id is not None:
            input_["reserved_cache_nodes_offering_id"] = (
                reserved_cache_nodes_offering_id
            )
        if cache_node_type is not None:
            input_["cache_node_type"] = cache_node_type
        if duration is not None:
            input_["duration"] = duration
        if product_description is not None:
            input_["product_description"] = product_description
        if offering_type is not None:
            input_["offering_type"] = offering_type
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

    async def iter_describe_reserved_cache_nodes_offerings(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        reserved_cache_nodes_offering_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        cache_node_type: Optional["capo_elasticache.types.string.String"] = None,
        duration: Optional["capo_elasticache.types.string.String"] = None,
        product_description: Optional["capo_elasticache.types.string.String"] = None,
        offering_type: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.reserved_cache_nodes_offering.ReservedCacheNodesOffering]":
        _token = marker
        while True:
            _response = await self.describe_reserved_cache_nodes_offerings(
                config_overrides=config_overrides,
                reserved_cache_nodes_offering_id=reserved_cache_nodes_offering_id,
                cache_node_type=cache_node_type,
                duration=duration,
                product_description=product_description,
                offering_type=offering_type,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("reserved_cache_nodes_offerings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_serverless_caches(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        serverless_cache_name: Optional["capo_elasticache.types.string.String"] = None,
        max_results: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.describe_serverless_caches_response.DescribeServerlessCachesResponse":
        """<p>Returns information about a specific serverless cache. If no identifier is specified, then the API returns information on all the serverless caches belonging to this Amazon Web Services account.</p>

        Args:
            serverless_cache_name: <p>The identifier for the serverless cache. If this parameter is specified, only information about that specific serverless cache is returned. Default: NULL</p>
            max_results: <p>The maximum number of records in the response. If more records exist than the specified max-records value, the next token is included in the response so that remaining results can be retrieved. The default is 50.</p>
            next_token: <p>An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxResults.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.serverless_cache_not_found_fault.ServerlessCacheNotFoundFault: <p>The serverless cache was not found or does not exist.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_serverless_caches_request.DescribeServerlessCachesRequest]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.describe_serverless_caches_response.DescribeServerlessCachesResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_serverless_caches

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_serverless_caches.async_describe_serverless_caches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_serverless_caches_request.DescribeServerlessCachesRequest = {}
        if serverless_cache_name is not None:
            input_["serverless_cache_name"] = serverless_cache_name
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

    async def iter_describe_serverless_caches(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        serverless_cache_name: Optional["capo_elasticache.types.string.String"] = None,
        max_results: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.serverless_cache.ServerlessCache]":
        _token = next_token
        while True:
            _response = await self.describe_serverless_caches(
                config_overrides=config_overrides,
                serverless_cache_name=serverless_cache_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("serverless_caches",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_serverless_cache_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        serverless_cache_name: Optional["capo_elasticache.types.string.String"] = None,
        serverless_cache_snapshot_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        snapshot_type: Optional["capo_elasticache.types.string.String"] = None,
        next_token: Optional["capo_elasticache.types.string.String"] = None,
        max_results: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_elasticache.types.describe_serverless_cache_snapshots_response.DescribeServerlessCacheSnapshotsResponse":
        """<p>Returns information about serverless cache snapshots. By default, this API lists all of the customer’s serverless cache snapshots. It can also describe a single serverless cache snapshot, or the snapshots associated with a particular serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.</p>

        Args:
            serverless_cache_name: <p>The identifier of serverless cache. If this parameter is specified, only snapshots associated with that specific serverless cache are described. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            serverless_cache_snapshot_name: <p>The identifier of the serverless cache’s snapshot. If this parameter is specified, only this snapshot is described. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            snapshot_type: <p>The type of snapshot that is being described. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            next_token: <p>An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by max-results. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified max-results value, a market is included in the response so that remaining results can be retrieved. Available for Valkey, Redis OSS and Serverless Memcached only.The default is 50. The Validation Constraints are a maximum of 50.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.serverless_cache_not_found_fault.ServerlessCacheNotFoundFault: <p>The serverless cache was not found or does not exist.</p>
            capo_elasticache.errors.serverless_cache_snapshot_not_found_fault.ServerlessCacheSnapshotNotFoundFault: <p>This serverless cache snapshot could not be found or does not exist. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_serverless_cache_snapshots_request.DescribeServerlessCacheSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.describe_serverless_cache_snapshots_response.DescribeServerlessCacheSnapshotsResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_serverless_cache_snapshots

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_serverless_cache_snapshots.async_describe_serverless_cache_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_serverless_cache_snapshots_request.DescribeServerlessCacheSnapshotsRequest = {}
        if serverless_cache_name is not None:
            input_["serverless_cache_name"] = serverless_cache_name
        if serverless_cache_snapshot_name is not None:
            input_["serverless_cache_snapshot_name"] = serverless_cache_snapshot_name
        if snapshot_type is not None:
            input_["snapshot_type"] = snapshot_type
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

    async def iter_describe_serverless_cache_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        serverless_cache_name: Optional["capo_elasticache.types.string.String"] = None,
        serverless_cache_snapshot_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        snapshot_type: Optional["capo_elasticache.types.string.String"] = None,
        next_token: Optional["capo_elasticache.types.string.String"] = None,
        max_results: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_elasticache.types.serverless_cache_snapshot.ServerlessCacheSnapshot]":
        _token = next_token
        while True:
            _response = await self.describe_serverless_cache_snapshots(
                config_overrides=config_overrides,
                serverless_cache_name=serverless_cache_name,
                serverless_cache_snapshot_name=serverless_cache_snapshot_name,
                snapshot_type=snapshot_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("serverless_cache_snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_service_updates(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        service_update_name: Optional["capo_elasticache.types.string.String"] = None,
        service_update_status: Optional[
            "capo_elasticache.types.service_update_status_list.ServiceUpdateStatusList"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.service_updates_message.ServiceUpdatesMessage":
        """<p>Returns details of the service updates</p>

        Args:
            service_update_name: <p>The unique ID of the service update</p>
            service_update_status: <p>The status of the service update</p>
            max_records: <p>The maximum number of records to include in the response</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.service_update_not_found_fault.ServiceUpdateNotFoundFault: <p>The service update doesn't exist</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_service_updates_message.DescribeServiceUpdatesMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.service_updates_message.ServiceUpdatesMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_service_updates

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_service_updates.async_describe_service_updates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_service_updates_message.DescribeServiceUpdatesMessage = {}
        if service_update_name is not None:
            input_["service_update_name"] = service_update_name
        if service_update_status is not None:
            input_["service_update_status"] = service_update_status
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

    async def iter_describe_service_updates(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        service_update_name: Optional["capo_elasticache.types.string.String"] = None,
        service_update_status: Optional[
            "capo_elasticache.types.service_update_status_list.ServiceUpdateStatusList"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.service_update.ServiceUpdate]":
        _token = marker
        while True:
            _response = await self.describe_service_updates(
                config_overrides=config_overrides,
                service_update_name=service_update_name,
                service_update_status=service_update_status,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("service_updates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        cache_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        snapshot_name: Optional["capo_elasticache.types.string.String"] = None,
        snapshot_source: Optional["capo_elasticache.types.string.String"] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        show_node_group_config: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_elasticache.types.describe_snapshots_list_message.DescribeSnapshotsListMessage":
        """<p>Returns information about cluster or replication group snapshots. By default, <code>DescribeSnapshots</code> lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots associated with a particular cache cluster.</p> <note> <p>This operation is valid for Valkey or Redis OSS only.</p> </note>

        Args:
            replication_group_id: <p>A user-supplied replication group identifier. If this parameter is specified, only snapshots associated with that specific replication group are described.</p>
            cache_cluster_id: <p>A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described.</p>
            snapshot_name: <p>A user-supplied name of the snapshot. If this parameter is specified, only this snapshot are described.</p>
            snapshot_source: <p>If set to <code>system</code>, the output shows snapshots that were automatically created by ElastiCache. If set to <code>user</code> the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 50</p> <p>Constraints: minimum 20; maximum 50.</p>
            show_node_group_config: <p>A Boolean value which if true, the node group (shard) configuration is included in the snapshot description.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The requested snapshot name does not refer to an existing snapshot.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeSnapshots
            Returns information about the snapshot mysnapshot. By default.

            >>> await client.describe_snapshots(snapshot_name='snapshot-20161212')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_snapshots_message.DescribeSnapshotsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.describe_snapshots_list_message.DescribeSnapshotsListMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_snapshots

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_snapshots.async_describe_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_snapshots_message.DescribeSnapshotsMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if cache_cluster_id is not None:
            input_["cache_cluster_id"] = cache_cluster_id
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
        if snapshot_source is not None:
            input_["snapshot_source"] = snapshot_source
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records
        if show_node_group_config is not None:
            input_["show_node_group_config"] = show_node_group_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        cache_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        snapshot_name: Optional["capo_elasticache.types.string.String"] = None,
        snapshot_source: Optional["capo_elasticache.types.string.String"] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        show_node_group_config: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "AsyncIterator[capo_elasticache.types.snapshot.Snapshot]":
        _token = marker
        while True:
            _response = await self.describe_snapshots(
                config_overrides=config_overrides,
                replication_group_id=replication_group_id,
                cache_cluster_id=cache_cluster_id,
                snapshot_name=snapshot_name,
                snapshot_source=snapshot_source,
                marker=_token,
                max_records=max_records,
                show_node_group_config=show_node_group_config,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_update_actions(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        service_update_name: Optional["capo_elasticache.types.string.String"] = None,
        replication_group_ids: Optional[
            "capo_elasticache.types.replication_group_id_list.ReplicationGroupIdList"
        ] = None,
        cache_cluster_ids: Optional[
            "capo_elasticache.types.cache_cluster_id_list.CacheClusterIdList"
        ] = None,
        engine: Optional["capo_elasticache.types.string.String"] = None,
        service_update_status: Optional[
            "capo_elasticache.types.service_update_status_list.ServiceUpdateStatusList"
        ] = None,
        service_update_time_range: Optional[
            "capo_elasticache.types.time_range_filter.TimeRangeFilter"
        ] = None,
        update_action_status: Optional[
            "capo_elasticache.types.update_action_status_list.UpdateActionStatusList"
        ] = None,
        show_node_level_update_status: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.update_actions_message.UpdateActionsMessage":
        """<p>Returns details of the update actions </p>

        Args:
            service_update_name: <p>The unique ID of the service update</p>
            replication_group_ids: <p>The replication group IDs</p>
            cache_cluster_ids: <p>The cache cluster IDs</p>
            engine: <p>The Elasticache engine to which the update applies. Either Valkey, Redis OSS or Memcached.</p>
            service_update_status: <p>The status of the service update</p>
            service_update_time_range: <p>The range of time specified to search for service updates that are in available status</p>
            update_action_status: <p>The status of the update action.</p>
            show_node_level_update_status: <p>Dictates whether to include node level update status in the response </p>
            max_records: <p>The maximum number of records to include in the response</p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_update_actions_message.DescribeUpdateActionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.update_actions_message.UpdateActionsMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_update_actions

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_update_actions.async_describe_update_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_update_actions_message.DescribeUpdateActionsMessage = {}
        if service_update_name is not None:
            input_["service_update_name"] = service_update_name
        if replication_group_ids is not None:
            input_["replication_group_ids"] = replication_group_ids
        if cache_cluster_ids is not None:
            input_["cache_cluster_ids"] = cache_cluster_ids
        if engine is not None:
            input_["engine"] = engine
        if service_update_status is not None:
            input_["service_update_status"] = service_update_status
        if service_update_time_range is not None:
            input_["service_update_time_range"] = service_update_time_range
        if update_action_status is not None:
            input_["update_action_status"] = update_action_status
        if show_node_level_update_status is not None:
            input_["show_node_level_update_status"] = show_node_level_update_status
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

    async def iter_describe_update_actions(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        service_update_name: Optional["capo_elasticache.types.string.String"] = None,
        replication_group_ids: Optional[
            "capo_elasticache.types.replication_group_id_list.ReplicationGroupIdList"
        ] = None,
        cache_cluster_ids: Optional[
            "capo_elasticache.types.cache_cluster_id_list.CacheClusterIdList"
        ] = None,
        engine: Optional["capo_elasticache.types.string.String"] = None,
        service_update_status: Optional[
            "capo_elasticache.types.service_update_status_list.ServiceUpdateStatusList"
        ] = None,
        service_update_time_range: Optional[
            "capo_elasticache.types.time_range_filter.TimeRangeFilter"
        ] = None,
        update_action_status: Optional[
            "capo_elasticache.types.update_action_status_list.UpdateActionStatusList"
        ] = None,
        show_node_level_update_status: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.update_action.UpdateAction]":
        _token = marker
        while True:
            _response = await self.describe_update_actions(
                config_overrides=config_overrides,
                service_update_name=service_update_name,
                replication_group_ids=replication_group_ids,
                cache_cluster_ids=cache_cluster_ids,
                engine=engine,
                service_update_status=service_update_status,
                service_update_time_range=service_update_time_range,
                update_action_status=update_action_status,
                show_node_level_update_status=show_node_level_update_status,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("update_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_user_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        user_group_id: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.describe_user_groups_result.DescribeUserGroupsResult":
        """<p>Returns a list of user groups.</p>

        Args:
            user_group_id: <p>The ID of the user group.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved. </p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords. ></p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.user_group_not_found_fault.UserGroupNotFoundFault: <p>The user group was not found or does not exist</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_user_groups_message.DescribeUserGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.describe_user_groups_result.DescribeUserGroupsResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_user_groups

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_user_groups.async_describe_user_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_user_groups_message.DescribeUserGroupsMessage = {}
        if user_group_id is not None:
            input_["user_group_id"] = user_group_id
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

    async def iter_describe_user_groups(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        user_group_id: Optional["capo_elasticache.types.string.String"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.user_group.UserGroup]":
        _token = marker
        while True:
            _response = await self.describe_user_groups(
                config_overrides=config_overrides,
                user_group_id=user_group_id,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("user_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_users(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        engine: Optional["capo_elasticache.types.engine_type.EngineType"] = None,
        user_id: Optional["capo_elasticache.types.user_id.UserId"] = None,
        filters: Optional["capo_elasticache.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.describe_users_result.DescribeUsersResult":
        """<p>Returns a list of users.</p>

        Args:
            engine: <p>The engine. </p>
            user_id: <p>The ID of the user.</p>
            filters: <p>Filter to determine the list of User IDs to return.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved. </p>
            marker: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords. ></p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.user_not_found_fault.UserNotFoundFault: <p>The user does not exist or could not be found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.describe_users_message.DescribeUsersMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.describe_users_result.DescribeUsersResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.describe_users

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.describe_users.async_describe_users(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.describe_users_message.DescribeUsersMessage = {}
        if engine is not None:
            input_["engine"] = engine
        if user_id is not None:
            input_["user_id"] = user_id
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_users(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        engine: Optional["capo_elasticache.types.engine_type.EngineType"] = None,
        user_id: Optional["capo_elasticache.types.user_id.UserId"] = None,
        filters: Optional["capo_elasticache.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "AsyncIterator[capo_elasticache.types.user.User]":
        _token = marker
        while True:
            _response = await self.describe_users(
                config_overrides=config_overrides,
                engine=engine,
                user_id=user_id,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def disassociate_global_replication_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        global_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        replication_group_region: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
    ) -> "capo_elasticache.types.disassociate_global_replication_group_result.DisassociateGlobalReplicationGroupResult":
        """<p>Remove a secondary cluster from the Global datastore using the Global datastore name. The secondary cluster will no longer receive updates from the primary cluster, but will remain as a standalone cluster in that Amazon region.</p>

        Args:
            global_replication_group_id: <p>The name of the Global datastore</p>
            replication_group_id: <p>The name of the secondary cluster you wish to remove from the Global datastore</p>
            replication_group_region: <p>The Amazon region of secondary cluster you wish to remove from the Global datastore</p>

        Raises:
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.invalid_global_replication_group_state_fault.InvalidGlobalReplicationGroupStateFault: <p>The Global datastore is not available or in primary-only state.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.disassociate_global_replication_group_message.DisassociateGlobalReplicationGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.disassociate_global_replication_group_result.DisassociateGlobalReplicationGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.disassociate_global_replication_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.disassociate_global_replication_group.async_disassociate_global_replication_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.disassociate_global_replication_group_message.DisassociateGlobalReplicationGroupMessage = {}
        if global_replication_group_id is not None:
            input_["global_replication_group_id"] = global_replication_group_id
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if replication_group_region is not None:
            input_["replication_group_region"] = replication_group_region

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_serverless_cache_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        serverless_cache_snapshot_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        s3_bucket_name: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.export_serverless_cache_snapshot_response.ExportServerlessCacheSnapshotResponse":
        """<p>Provides the functionality to export the serverless cache snapshot data to Amazon S3. Available for Valkey and Redis OSS only.</p>

        Args:
            serverless_cache_snapshot_name: <p>The identifier of the serverless cache snapshot to be exported to S3. Available for Valkey and Redis OSS only.</p>
            s3_bucket_name: <p>Name of the Amazon S3 bucket to export the snapshot to. The Amazon S3 bucket must also be in same region as the snapshot. Available for Valkey and Redis OSS only.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_serverless_cache_snapshot_state_fault.InvalidServerlessCacheSnapshotStateFault: <p>The state of the serverless cache snapshot was not received. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.serverless_cache_snapshot_not_found_fault.ServerlessCacheSnapshotNotFoundFault: <p>This serverless cache snapshot could not be found or does not exist. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.export_serverless_cache_snapshot_request.ExportServerlessCacheSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.export_serverless_cache_snapshot_response.ExportServerlessCacheSnapshotResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.export_serverless_cache_snapshot

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.export_serverless_cache_snapshot.async_export_serverless_cache_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.export_serverless_cache_snapshot_request.ExportServerlessCacheSnapshotRequest = {}
        if serverless_cache_snapshot_name is not None:
            input_["serverless_cache_snapshot_name"] = serverless_cache_snapshot_name
        if s3_bucket_name is not None:
            input_["s3_bucket_name"] = s3_bucket_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def failover_global_replication_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        global_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        primary_region: Optional["capo_elasticache.types.string.String"] = None,
        primary_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
    ) -> "capo_elasticache.types.failover_global_replication_group_result.FailoverGlobalReplicationGroupResult":
        """<p>Used to failover the primary region to a secondary region. The secondary region will become primary, and all other clusters will become secondary.</p>

        Args:
            global_replication_group_id: <p>The name of the Global datastore</p>
            primary_region: <p>The Amazon region of the primary cluster of the Global datastore</p>
            primary_replication_group_id: <p>The name of the primary replication group</p>

        Raises:
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.invalid_global_replication_group_state_fault.InvalidGlobalReplicationGroupStateFault: <p>The Global datastore is not available or in primary-only state.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.failover_global_replication_group_message.FailoverGlobalReplicationGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.failover_global_replication_group_result.FailoverGlobalReplicationGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.failover_global_replication_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.failover_global_replication_group.async_failover_global_replication_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.failover_global_replication_group_message.FailoverGlobalReplicationGroupMessage = {}
        if global_replication_group_id is not None:
            input_["global_replication_group_id"] = global_replication_group_id
        if primary_region is not None:
            input_["primary_region"] = primary_region
        if primary_replication_group_id is not None:
            input_["primary_replication_group_id"] = primary_replication_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def increase_node_groups_in_global_replication_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        global_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        node_group_count: Optional["capo_elasticache.types.integer.Integer"] = None,
        regional_configurations: Optional[
            "capo_elasticache.types.regional_configuration_list.RegionalConfigurationList"
        ] = None,
        apply_immediately: Optional["capo_elasticache.types.boolean.Boolean"] = None,
    ) -> "capo_elasticache.types.increase_node_groups_in_global_replication_group_result.IncreaseNodeGroupsInGlobalReplicationGroupResult":
        """<p>Increase the number of node groups in the Global datastore</p>

        Args:
            global_replication_group_id: <p>The name of the Global datastore</p>
            node_group_count: <p>Total number of node groups you want</p>
            regional_configurations: <p>Describes the replication group IDs, the Amazon regions where they are stored and the shard configuration for each that comprise the Global datastore</p>
            apply_immediately: <p>Indicates that the process begins immediately. At present, the only permitted value for this parameter is true.</p>

        Raises:
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.invalid_global_replication_group_state_fault.InvalidGlobalReplicationGroupStateFault: <p>The Global datastore is not available or in primary-only state.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.increase_node_groups_in_global_replication_group_message.IncreaseNodeGroupsInGlobalReplicationGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.increase_node_groups_in_global_replication_group_result.IncreaseNodeGroupsInGlobalReplicationGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.increase_node_groups_in_global_replication_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.increase_node_groups_in_global_replication_group.async_increase_node_groups_in_global_replication_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.increase_node_groups_in_global_replication_group_message.IncreaseNodeGroupsInGlobalReplicationGroupMessage = {}
        if global_replication_group_id is not None:
            input_["global_replication_group_id"] = global_replication_group_id
        if node_group_count is not None:
            input_["node_group_count"] = node_group_count
        if regional_configurations is not None:
            input_["regional_configurations"] = regional_configurations
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def increase_replica_count(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        new_replica_count: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        replica_configuration: Optional[
            "capo_elasticache.types.replica_configuration_list.ReplicaConfigurationList"
        ] = None,
        apply_immediately: Optional["capo_elasticache.types.boolean.Boolean"] = None,
    ) -> "capo_elasticache.types.increase_replica_count_result.IncreaseReplicaCountResult":
        """<p>Dynamically increases the number of replicas in a Valkey or Redis OSS (cluster mode disabled) replication group or the number of replica nodes in one or more node groups (shards) of a Valkey or Redis OSS (cluster mode enabled) replication group. This operation is performed with no cluster down time.</p>

        Args:
            replication_group_id: <p>The id of the replication group to which you want to add replica nodes.</p>
            new_replica_count: <p>The number of read replica nodes you want at the completion of this operation. For Valkey or Redis OSS (cluster mode disabled) replication groups, this is the number of replica nodes in the replication group. For Valkey or Redis OSS (cluster mode enabled) replication groups, this is the number of replica nodes in each of the replication group's node groups.</p>
            replica_configuration: <p>A list of <code>ConfigureShard</code> objects that can be used to configure each shard in a Valkey or Redis OSS (cluster mode enabled) replication group. The <code>ConfigureShard</code> has three members: <code>NewReplicaCount</code>, <code>NodeGroupId</code>, and <code>PreferredAvailabilityZones</code>.</p>
            apply_immediately: <p>If <code>True</code>, the number of replica nodes is increased immediately. <code>ApplyImmediately=False</code> is not currently supported.</p>

        Raises:
            capo_elasticache.errors.cluster_quota_for_customer_exceeded_fault.ClusterQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the allowed number of clusters per customer.</p>
            capo_elasticache.errors.insufficient_cache_cluster_capacity_fault.InsufficientCacheClusterCapacityFault: <p>The requested cache node type is not available in the specified Availability Zone. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ErrorMessages.html#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY">InsufficientCacheClusterCapacity</a> in the ElastiCache User Guide.</p>
            capo_elasticache.errors.invalid_cache_cluster_state_fault.InvalidCacheClusterStateFault: <p>The requested cluster is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_kms_key_fault.InvalidKMSKeyFault: <p>The KMS key supplied is not valid.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The VPC network is in an invalid state.</p>
            capo_elasticache.errors.node_groups_per_replication_group_quota_exceeded_fault.NodeGroupsPerReplicationGroupQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum allowed number of node groups (shards) in a single replication group. The default maximum is 90</p>
            capo_elasticache.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache nodes per customer.</p>
            capo_elasticache.errors.no_operation_fault.NoOperationFault: <p>The operation was not performed because no changes were required.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.increase_replica_count_message.IncreaseReplicaCountMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.increase_replica_count_result.IncreaseReplicaCountResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.increase_replica_count

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.increase_replica_count.async_increase_replica_count(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.increase_replica_count_message.IncreaseReplicaCountMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if new_replica_count is not None:
            input_["new_replica_count"] = new_replica_count
        if replica_configuration is not None:
            input_["replica_configuration"] = replica_configuration
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_allowed_node_type_modifications(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.allowed_node_type_modifications_message.AllowedNodeTypeModificationsMessage":
        """<p>Lists all available node types that you can scale with your cluster's replication group's current node type.</p> <p>When you use the <code>ModifyCacheCluster</code> or <code>ModifyReplicationGroup</code> operations to scale your cluster or replication group, the value of the <code>CacheNodeType</code> parameter must be one of the node types returned by this operation.</p>

        Args:
            cache_cluster_id: <p>The name of the cluster you want to scale up to a larger node instanced type. ElastiCache uses the cluster id to identify the current node type of this cluster and from that to create a list of node types you can scale up to.</p> <important> <p>You must provide a value for either the <code>CacheClusterId</code> or the <code>ReplicationGroupId</code>.</p> </important>
            replication_group_id: <p>The name of the replication group want to scale up to a larger node type. ElastiCache uses the replication group id to identify the current node type being used by this replication group, and from that to create a list of node types you can scale up to.</p> <important> <p>You must provide a value for either the <code>CacheClusterId</code> or the <code>ReplicationGroupId</code>.</p> </important>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListAllowedNodeTypeModifications
            Lists all available node types that you can scale your Redis cluster's or replication group's current node type up to.

            >>> await client.list_allowed_node_type_modifications(cache_cluster_id='mycluster')
            ListAllowedNodeTypeModifications
            Lists all available node types that you can scale your Redis cluster's or replication group's current node type up to.

            >>> await client.list_allowed_node_type_modifications(replication_group_id='myreplgroup')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.list_allowed_node_type_modifications_message.ListAllowedNodeTypeModificationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.allowed_node_type_modifications_message.AllowedNodeTypeModificationsMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.list_allowed_node_type_modifications

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.list_allowed_node_type_modifications.async_list_allowed_node_type_modifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.list_allowed_node_type_modifications_message.ListAllowedNodeTypeModificationsMessage = {}
        if cache_cluster_id is not None:
            input_["cache_cluster_id"] = cache_cluster_id
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        resource_name: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.tag_list_message.TagListMessage":
        """<p>Lists all tags currently on a named resource.</p> <p> A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your ElastiCache resources. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.ResourceLevelPermissions.html">Resource-level permissions</a>.</p> <p>If the cluster is not in the <i>available</i> state, <code>ListTagsForResource</code> returns an error.</p>

        Args:
            resource_name: <p>The Amazon Resource Name (ARN) of the resource for which you want the list of tags, for example <code>arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster</code> or <code>arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot</code>.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault: <p>The requested cache security group name does not refer to an existing cache security group.</p>
            capo_elasticache.errors.cache_subnet_group_not_found_fault.CacheSubnetGroupNotFoundFault: <p>The requested cache subnet group name does not refer to an existing cache subnet group.</p>
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.invalid_arn_fault.InvalidARNFault: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_serverless_cache_snapshot_state_fault.InvalidServerlessCacheSnapshotStateFault: <p>The state of the serverless cache snapshot was not received. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.invalid_serverless_cache_state_fault.InvalidServerlessCacheStateFault: <p>The account for these credentials is not currently active.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.reserved_cache_node_not_found_fault.ReservedCacheNodeNotFoundFault: <p>The requested reserved cache node was not found.</p>
            capo_elasticache.errors.serverless_cache_not_found_fault.ServerlessCacheNotFoundFault: <p>The serverless cache was not found or does not exist.</p>
            capo_elasticache.errors.serverless_cache_snapshot_not_found_fault.ServerlessCacheSnapshotNotFoundFault: <p>This serverless cache snapshot could not be found or does not exist. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The requested snapshot name does not refer to an existing snapshot.</p>
            capo_elasticache.errors.user_group_not_found_fault.UserGroupNotFoundFault: <p>The user group was not found or does not exist</p>
            capo_elasticache.errors.user_not_found_fault.UserNotFoundFault: <p>The user does not exist or could not be found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListTagsForResource
            Lists all cost allocation tags currently on the named resource. A cost allocation tag is a key-value pair where the key is case-sensitive and the value is optional. You can use cost allocation tags to categorize and track your AWS costs.

            >>> await client.list_tags_for_resource(resource_name='arn:aws:elasticache:us-west-2:<my-account-id>:cluster:mycluster')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.list_tags_for_resource_message.ListTagsForResourceMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.tag_list_message.TagListMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.list_tags_for_resource_message.ListTagsForResourceMessage = {}
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cache_cluster(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        num_cache_nodes: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        cache_node_ids_to_remove: Optional[
            "capo_elasticache.types.cache_node_ids_list.CacheNodeIdsList"
        ] = None,
        az_mode: Optional["capo_elasticache.types.az_mode.AZMode"] = None,
        new_availability_zones: Optional[
            "capo_elasticache.types.preferred_availability_zone_list.PreferredAvailabilityZoneList"
        ] = None,
        cache_security_group_names: Optional[
            "capo_elasticache.types.cache_security_group_name_list.CacheSecurityGroupNameList"
        ] = None,
        security_group_ids: Optional[
            "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
        ] = None,
        preferred_maintenance_window: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        notification_topic_arn: Optional["capo_elasticache.types.string.String"] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        notification_topic_status: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        apply_immediately: Optional["capo_elasticache.types.boolean.Boolean"] = None,
        engine: Optional["capo_elasticache.types.string.String"] = None,
        engine_version: Optional["capo_elasticache.types.string.String"] = None,
        auto_minor_version_upgrade: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        snapshot_retention_limit: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        snapshot_window: Optional["capo_elasticache.types.string.String"] = None,
        cache_node_type: Optional["capo_elasticache.types.string.String"] = None,
        auth_token: Optional["capo_elasticache.types.string.String"] = None,
        auth_token_update_strategy: Optional[
            "capo_elasticache.types.auth_token_update_strategy_type.AuthTokenUpdateStrategyType"
        ] = None,
        log_delivery_configurations: Optional[
            "capo_elasticache.types.log_delivery_configuration_request_list.LogDeliveryConfigurationRequestList"
        ] = None,
        ip_discovery: Optional[
            "capo_elasticache.types.ip_discovery.IpDiscovery"
        ] = None,
        scale_config: Optional[
            "capo_elasticache.types.scale_config.ScaleConfig"
        ] = None,
    ) -> "capo_elasticache.types.modify_cache_cluster_result.ModifyCacheClusterResult":
        """<p>Modifies the settings for a cluster. You can use this operation to change one or more cluster configuration parameters by specifying the parameters and the new values.</p>

        Args:
            cache_cluster_id: <p>The cluster identifier. This value is stored as a lowercase string.</p>
            num_cache_nodes: <p>The number of cache nodes that the cluster should have. If the value for <code>NumCacheNodes</code> is greater than the sum of the number of current cache nodes and the number of cache nodes pending creation (which may be zero), more nodes are added. If the value is less than the number of existing cache nodes, nodes are removed. If the value is equal to the number of current cache nodes, any pending add or remove requests are canceled.</p> <p>If you are removing cache nodes, you must use the <code>CacheNodeIdsToRemove</code> parameter to provide the IDs of the specific cache nodes to remove.</p> <p>For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.</p> <note> <p>Adding or removing Memcached cache nodes can be applied immediately or as a pending operation (see <code>ApplyImmediately</code>).</p> <p>A pending operation to modify the number of cache nodes in a cluster during its maintenance window, whether by adding or removing nodes in accordance with the scale out architecture, is not queued. The customer's latest request to add or remove nodes to the cluster overrides any previous pending operations to modify the number of cache nodes in the cluster. For example, a request to remove 2 nodes would override a previous pending operation to remove 3 nodes. Similarly, a request to add 2 nodes would override a previous pending operation to remove 3 nodes and vice versa. As Memcached cache nodes may now be provisioned in different Availability Zones with flexible cache node placement, a request to add nodes does not automatically override a previous pending operation to add nodes. The customer can modify the previous pending operation to add more nodes or explicitly cancel the pending request and retry the new request. To cancel pending operations to modify the number of cache nodes in a cluster, use the <code>ModifyCacheCluster</code> request and set <code>NumCacheNodes</code> equal to the number of cache nodes currently in the cluster.</p> </note>
            cache_node_ids_to_remove: <p>A list of cache node IDs to be removed. A node ID is a numeric identifier (0001, 0002, etc.). This parameter is only valid when <code>NumCacheNodes</code> is less than the existing number of cache nodes. The number of cache node IDs supplied in this parameter must match the difference between the existing number of cache nodes in the cluster or pending cache nodes, whichever is greater, and the value of <code>NumCacheNodes</code> in the request.</p> <p>For example: If you have 3 active cache nodes, 7 pending cache nodes, and the number of cache nodes in this <code>ModifyCacheCluster</code> call is 5, you must list 2 (7 - 5) cache node IDs to remove.</p>
            az_mode: <p>Specifies whether the new nodes in this Memcached cluster are all created in a single Availability Zone or created across multiple Availability Zones.</p> <p>Valid values: <code>single-az</code> | <code>cross-az</code>.</p> <p>This option is only supported for Memcached clusters.</p> <note> <p>You cannot specify <code>single-az</code> if the Memcached cluster already has cache nodes in different Availability Zones. If <code>cross-az</code> is specified, existing Memcached nodes remain in their current Availability Zone.</p> <p>Only newly created nodes are located in different Availability Zones. </p> </note>
            new_availability_zones: <note> <p>This option is only supported on Memcached clusters.</p> </note> <p>The list of Availability Zones where the new Memcached cache nodes are created.</p> <p>This parameter is only valid when <code>NumCacheNodes</code> in the request is greater than the sum of the number of active cache nodes and the number of cache nodes pending creation (which may be zero). The number of Availability Zones supplied in this list must match the cache nodes being added in this request.</p> <p>Scenarios:</p> <ul> <li> <p> <b>Scenario 1:</b> You have 3 active nodes and wish to add 2 nodes. Specify <code>NumCacheNodes=5</code> (3 + 2) and optionally specify two Availability Zones for the two new nodes.</p> </li> <li> <p> <b>Scenario 2:</b> You have 3 active nodes and 2 nodes pending creation (from the scenario 1 call) and want to add 1 more node. Specify <code>NumCacheNodes=6</code> ((3 + 2) + 1) and optionally specify an Availability Zone for the new node.</p> </li> <li> <p> <b>Scenario 3:</b> You want to cancel all pending operations. Specify <code>NumCacheNodes=3</code> to cancel all pending operations.</p> </li> </ul> <p>The Availability Zone placement of nodes pending creation cannot be modified. If you wish to cancel any nodes pending creation, add 0 nodes by setting <code>NumCacheNodes</code> to the number of current nodes.</p> <p>If <code>cross-az</code> is specified, existing Memcached nodes remain in their current Availability Zone. Only newly created nodes can be located in different Availability Zones. For guidance on how to move existing Memcached nodes to different Availability Zones, see the <b>Availability Zone Considerations</b> section of <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html">Cache Node Considerations for Memcached</a>.</p> <p> <b>Impact of new add/remove requests upon pending requests</b> </p> <ul> <li> <p>Scenario-1</p> <ul> <li> <p>Pending Action: Delete</p> </li> <li> <p>New Request: Delete</p> </li> <li> <p>Result: The new delete, pending or immediate, replaces the pending delete.</p> </li> </ul> </li> <li> <p>Scenario-2</p> <ul> <li> <p>Pending Action: Delete</p> </li> <li> <p>New Request: Create</p> </li> <li> <p>Result: The new create, pending or immediate, replaces the pending delete.</p> </li> </ul> </li> <li> <p>Scenario-3</p> <ul> <li> <p>Pending Action: Create</p> </li> <li> <p>New Request: Delete</p> </li> <li> <p>Result: The new delete, pending or immediate, replaces the pending create.</p> </li> </ul> </li> <li> <p>Scenario-4</p> <ul> <li> <p>Pending Action: Create</p> </li> <li> <p>New Request: Create</p> </li> <li> <p>Result: The new create is added to the pending create.</p> <important> <p> <b>Important:</b> If the new create request is <b>Apply Immediately - Yes</b>, all creates are performed immediately. If the new create request is <b>Apply Immediately - No</b>, all creates are pending.</p> </important> </li> </ul> </li> </ul>
            cache_security_group_names: <p>A list of cache security group names to authorize on this cluster. This change is asynchronously applied as soon as possible.</p> <p>You can use this parameter only with clusters that are created outside of an Amazon Virtual Private Cloud (Amazon VPC).</p> <p>Constraints: Must contain no more than 255 alphanumeric characters. Must not be "Default".</p>
            security_group_ids: <p>Specifies the VPC Security Groups associated with the cluster.</p> <p>This parameter can be used only with clusters that are created in an Amazon Virtual Private Cloud (Amazon VPC).</p>
            preferred_maintenance_window: <p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>
            notification_topic_arn: <p>The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.</p> <note> <p>The Amazon SNS topic owner must be same as the cluster owner.</p> </note>
            cache_parameter_group_name: <p>The name of the cache parameter group to apply to this cluster. This change is asynchronously applied as soon as possible for parameters when the <code>ApplyImmediately</code> parameter is specified as <code>true</code> for this request.</p>
            notification_topic_status: <p>The status of the Amazon SNS notification topic. Notifications are sent only if the status is <code>active</code>.</p> <p>Valid values: <code>active</code> | <code>inactive</code> </p>
            apply_immediately: <p>If <code>true</code>, this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the cluster.</p> <p>If <code>false</code>, changes to the cluster are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.</p> <important> <p>If you perform a <code>ModifyCacheCluster</code> before a pending modification is applied, the pending modification is replaced by the newer modification. However, a pending node-count increase on Memcached clusters cannot be superseded by a request to add fewer nodes. To change a pending node addition, first cancel it by setting <code>NumCacheNodes</code> equal to the current number of nodes in the cluster, then submit the new request. See the <code>NumCacheNodes</code> parameter for details on node scaling behavior.</p> </important> <p>Valid values: <code>true</code> | <code>false</code> </p> <p>Default: <code>false</code> </p>
            engine: <p>The engine type used by the cache cluster. The options are valkey, memcached or redis.</p>
            engine_version: <p>The upgraded version of the cache engine to be run on the cache nodes.</p> <p> <b>Important:</b> You can upgrade to a newer engine version (see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement">Selecting a Cache Engine and Version</a>), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster and create it anew with the earlier engine version. </p>
            auto_minor_version_upgrade: <p> If you are running Valkey 7.2 or Redis OSS engine version 6.0 or later, set this parameter to yes to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions. </p>
            snapshot_retention_limit: <p>The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set <code>SnapshotRetentionLimit</code> to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p> <note> <p>If the value of <code>SnapshotRetentionLimit</code> is set to zero (0), backups are turned off.</p> </note>
            snapshot_window: <p>The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster. </p>
            cache_node_type: <p>A valid cache node type that you want to scale this cluster up to.</p>
            auth_token: <p>Reserved parameter. The password used to access a password protected server. This parameter must be specified with the <code>auth-token-update</code> parameter. Password constraints:</p> <ul> <li> <p>Must be only printable ASCII characters</p> </li> <li> <p>Must be at least 16 characters and no more than 128 characters in length</p> </li> <li> <p>Cannot contain any of the following characters: '/', '"', or '@', '%'</p> </li> </ul> <p> For more information, see AUTH password at <a href="http://redis.io/commands/AUTH">AUTH</a>.</p>
            auth_token_update_strategy: <p>Specifies the strategy to use to update the AUTH token. This parameter must be specified with the <code>auth-token</code> parameter. Possible values:</p> <ul> <li> <p>ROTATE - default, if no update strategy is provided</p> </li> <li> <p>SET - allowed only after ROTATE</p> </li> <li> <p>DELETE - allowed only when transitioning to RBAC</p> </li> </ul> <p> For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html">Authenticating Users with AUTH</a> </p>
            log_delivery_configurations: <p>Specifies the destination, format and type of the logs.</p>
            ip_discovery: <p>The network type you choose when modifying a cluster, either <code>ipv4</code> | <code>ipv6</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>
            scale_config: <p>Configures horizontal or vertical scaling for Memcached clusters, specifying the scaling percentage and interval.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault: <p>The requested cache security group name does not refer to an existing cache security group.</p>
            capo_elasticache.errors.insufficient_cache_cluster_capacity_fault.InsufficientCacheClusterCapacityFault: <p>The requested cache node type is not available in the specified Availability Zone. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ErrorMessages.html#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY">InsufficientCacheClusterCapacity</a> in the ElastiCache User Guide.</p>
            capo_elasticache.errors.invalid_cache_cluster_state_fault.InvalidCacheClusterStateFault: <p>The requested cluster is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_cache_security_group_state_fault.InvalidCacheSecurityGroupStateFault: <p>The current state of the cache security group does not allow deletion.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The VPC network is in an invalid state.</p>
            capo_elasticache.errors.node_quota_for_cluster_exceeded_fault.NodeQuotaForClusterExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache nodes in a single cluster.</p>
            capo_elasticache.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache nodes per customer.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ModifyCacheCluster
            Copies a snapshot to a specified name.

            >>> await client.modify_cache_cluster(cache_cluster_id='redis-cluster', apply_immediately=True, snapshot_retention_limit=14)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.modify_cache_cluster_message.ModifyCacheClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.modify_cache_cluster_result.ModifyCacheClusterResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.modify_cache_cluster

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.modify_cache_cluster.async_modify_cache_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.modify_cache_cluster_message.ModifyCacheClusterMessage = {}
        if cache_cluster_id is not None:
            input_["cache_cluster_id"] = cache_cluster_id
        if num_cache_nodes is not None:
            input_["num_cache_nodes"] = num_cache_nodes
        if cache_node_ids_to_remove is not None:
            input_["cache_node_ids_to_remove"] = cache_node_ids_to_remove
        if az_mode is not None:
            input_["az_mode"] = az_mode
        if new_availability_zones is not None:
            input_["new_availability_zones"] = new_availability_zones
        if cache_security_group_names is not None:
            input_["cache_security_group_names"] = cache_security_group_names
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if notification_topic_arn is not None:
            input_["notification_topic_arn"] = notification_topic_arn
        if cache_parameter_group_name is not None:
            input_["cache_parameter_group_name"] = cache_parameter_group_name
        if notification_topic_status is not None:
            input_["notification_topic_status"] = notification_topic_status
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if snapshot_retention_limit is not None:
            input_["snapshot_retention_limit"] = snapshot_retention_limit
        if snapshot_window is not None:
            input_["snapshot_window"] = snapshot_window
        if cache_node_type is not None:
            input_["cache_node_type"] = cache_node_type
        if auth_token is not None:
            input_["auth_token"] = auth_token
        if auth_token_update_strategy is not None:
            input_["auth_token_update_strategy"] = auth_token_update_strategy
        if log_delivery_configurations is not None:
            input_["log_delivery_configurations"] = log_delivery_configurations
        if ip_discovery is not None:
            input_["ip_discovery"] = ip_discovery
        if scale_config is not None:
            input_["scale_config"] = scale_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cache_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        parameter_name_values: Optional[
            "capo_elasticache.types.parameter_name_value_list.ParameterNameValueList"
        ] = None,
    ) -> "capo_elasticache.types.cache_parameter_group_name_message.CacheParameterGroupNameMessage":
        """<p>Modifies the parameters of a cache parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.</p>

        Args:
            cache_parameter_group_name: <p>The name of the cache parameter group to modify.</p>
            parameter_name_values: <p>An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be modified per request.</p>

        Raises:
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.invalid_cache_parameter_group_state_fault.InvalidCacheParameterGroupStateFault: <p>The current state of the cache parameter group does not allow the requested operation to occur.</p>
            capo_elasticache.errors.invalid_global_replication_group_state_fault.InvalidGlobalReplicationGroupStateFault: <p>The Global datastore is not available or in primary-only state.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ModifyCacheParameterGroup
            Modifies one or more parameter values in the specified parameter group. You cannot modify any default parameter group.

            >>> await client.modify_cache_parameter_group(cache_parameter_group_name='custom-mem1-4', parameter_name_values=[{'ParameterName': 'binding_protocol', 'ParameterValue': 'ascii'}, {'ParameterName': 'chunk_size', 'ParameterValue': '96'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.modify_cache_parameter_group_message.ModifyCacheParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.cache_parameter_group_name_message.CacheParameterGroupNameMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.modify_cache_parameter_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.modify_cache_parameter_group.async_modify_cache_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.modify_cache_parameter_group_message.ModifyCacheParameterGroupMessage = {}
        if cache_parameter_group_name is not None:
            input_["cache_parameter_group_name"] = cache_parameter_group_name
        if parameter_name_values is not None:
            input_["parameter_name_values"] = parameter_name_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_cache_subnet_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_subnet_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        cache_subnet_group_description: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        subnet_ids: Optional[
            "capo_elasticache.types.subnet_identifier_list.SubnetIdentifierList"
        ] = None,
    ) -> "capo_elasticache.types.modify_cache_subnet_group_result.ModifyCacheSubnetGroupResult":
        """<p>Modifies an existing cache subnet group.</p>

        Args:
            cache_subnet_group_name: <p>The name for the cache subnet group. This value is stored as a lowercase string.</p> <p>Constraints: Must contain no more than 255 alphanumeric characters or hyphens.</p> <p>Example: <code>mysubnetgroup</code> </p>
            cache_subnet_group_description: <p>A description of the cache subnet group.</p>
            subnet_ids: <p>The EC2 subnet IDs for the cache subnet group.</p>

        Raises:
            capo_elasticache.errors.cache_subnet_group_not_found_fault.CacheSubnetGroupNotFoundFault: <p>The requested cache subnet group name does not refer to an existing cache subnet group.</p>
            capo_elasticache.errors.cache_subnet_quota_exceeded_fault.CacheSubnetQuotaExceededFault: <p>The request cannot be processed because it would exceed the allowed number of subnets in a cache subnet group.</p>
            capo_elasticache.errors.invalid_subnet.InvalidSubnet: <p>An invalid subnet identifier was specified.</p>
            capo_elasticache.errors.subnet_in_use.SubnetInUse: <p>The requested subnet is being used by another cache subnet group.</p>
            capo_elasticache.errors.subnet_not_allowed_fault.SubnetNotAllowedFault: <p>At least one subnet ID does not match the other subnet IDs. This mismatch typically occurs when a user sets one subnet ID to a regional Availability Zone and a different one to an outpost. Or when a user sets the subnet ID to an Outpost when not subscribed on this service.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ModifyCacheSubnetGroup
            Modifies an existing ElastiCache subnet group.

            >>> await client.modify_cache_subnet_group(cache_subnet_group_name='my-sn-grp', subnet_ids=['subnet-bcde2345'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.modify_cache_subnet_group_message.ModifyCacheSubnetGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.modify_cache_subnet_group_result.ModifyCacheSubnetGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.modify_cache_subnet_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.modify_cache_subnet_group.async_modify_cache_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.modify_cache_subnet_group_message.ModifyCacheSubnetGroupMessage = {}
        if cache_subnet_group_name is not None:
            input_["cache_subnet_group_name"] = cache_subnet_group_name
        if cache_subnet_group_description is not None:
            input_["cache_subnet_group_description"] = cache_subnet_group_description
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_global_replication_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        global_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        apply_immediately: Optional["capo_elasticache.types.boolean.Boolean"] = None,
        cache_node_type: Optional["capo_elasticache.types.string.String"] = None,
        engine: Optional["capo_elasticache.types.string.String"] = None,
        engine_version: Optional["capo_elasticache.types.string.String"] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        global_replication_group_description: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        automatic_failover_enabled: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_elasticache.types.modify_global_replication_group_result.ModifyGlobalReplicationGroupResult":
        """<p>Modifies the settings for a Global datastore.</p>

        Args:
            global_replication_group_id: <p>The name of the Global datastore</p>
            apply_immediately: <p>This parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible. Modifications to Global Replication Groups cannot be requested to be applied in PreferredMaintenceWindow. </p>
            cache_node_type: <p>A valid cache node type that you want to scale this Global datastore to.</p>
            engine: <p>Modifies the engine listed in a global replication group message. The options are valkey, memcached or redis.</p>
            engine_version: <p>The upgraded version of the cache engine to be run on the clusters in the Global datastore. </p>
            cache_parameter_group_name: <p>The name of the cache parameter group to use with the Global datastore. It must be compatible with the major engine version used by the Global datastore.</p>
            global_replication_group_description: <p>A description of the Global datastore</p>
            automatic_failover_enabled: <p>Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure. </p>

        Raises:
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.invalid_global_replication_group_state_fault.InvalidGlobalReplicationGroupStateFault: <p>The Global datastore is not available or in primary-only state.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.modify_global_replication_group_message.ModifyGlobalReplicationGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.modify_global_replication_group_result.ModifyGlobalReplicationGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.modify_global_replication_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.modify_global_replication_group.async_modify_global_replication_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.modify_global_replication_group_message.ModifyGlobalReplicationGroupMessage = {}
        if global_replication_group_id is not None:
            input_["global_replication_group_id"] = global_replication_group_id
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately
        if cache_node_type is not None:
            input_["cache_node_type"] = cache_node_type
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if cache_parameter_group_name is not None:
            input_["cache_parameter_group_name"] = cache_parameter_group_name
        if global_replication_group_description is not None:
            input_["global_replication_group_description"] = (
                global_replication_group_description
            )
        if automatic_failover_enabled is not None:
            input_["automatic_failover_enabled"] = automatic_failover_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_replication_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        replication_group_description: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        primary_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        snapshotting_cluster_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        automatic_failover_enabled: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        multi_az_enabled: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        node_group_id: Optional["capo_elasticache.types.string.String"] = None,
        cache_security_group_names: Optional[
            "capo_elasticache.types.cache_security_group_name_list.CacheSecurityGroupNameList"
        ] = None,
        security_group_ids: Optional[
            "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
        ] = None,
        preferred_maintenance_window: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        notification_topic_arn: Optional["capo_elasticache.types.string.String"] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        notification_topic_status: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        apply_immediately: Optional["capo_elasticache.types.boolean.Boolean"] = None,
        engine: Optional["capo_elasticache.types.string.String"] = None,
        engine_version: Optional["capo_elasticache.types.string.String"] = None,
        auto_minor_version_upgrade: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        snapshot_retention_limit: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        snapshot_window: Optional["capo_elasticache.types.string.String"] = None,
        cache_node_type: Optional["capo_elasticache.types.string.String"] = None,
        auth_token: Optional["capo_elasticache.types.string.String"] = None,
        auth_token_update_strategy: Optional[
            "capo_elasticache.types.auth_token_update_strategy_type.AuthTokenUpdateStrategyType"
        ] = None,
        user_group_ids_to_add: Optional[
            "capo_elasticache.types.user_group_id_list.UserGroupIdList"
        ] = None,
        user_group_ids_to_remove: Optional[
            "capo_elasticache.types.user_group_id_list.UserGroupIdList"
        ] = None,
        remove_user_groups: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        log_delivery_configurations: Optional[
            "capo_elasticache.types.log_delivery_configuration_request_list.LogDeliveryConfigurationRequestList"
        ] = None,
        ip_discovery: Optional[
            "capo_elasticache.types.ip_discovery.IpDiscovery"
        ] = None,
        transit_encryption_enabled: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        transit_encryption_mode: Optional[
            "capo_elasticache.types.transit_encryption_mode.TransitEncryptionMode"
        ] = None,
        cluster_mode: Optional[
            "capo_elasticache.types.cluster_mode.ClusterMode"
        ] = None,
        durability: Optional["capo_elasticache.types.durability.Durability"] = None,
    ) -> "capo_elasticache.types.modify_replication_group_result.ModifyReplicationGroupResult":
        """<p>Modifies the settings for a replication group. This is limited to Valkey and Redis OSS 7 and above.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/scaling-redis-cluster-mode-enabled.html">Scaling for Valkey or Redis OSS (cluster mode enabled)</a> in the ElastiCache User Guide</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyReplicationGroupShardConfiguration.html">ModifyReplicationGroupShardConfiguration</a> in the ElastiCache API Reference</p> </li> </ul> <note> <p>This operation is valid for Valkey or Redis OSS only.</p> </note>

        Args:
            replication_group_id: <p>The identifier of the replication group to modify.</p>
            replication_group_description: <p>A description for the replication group. Maximum length is 255 characters.</p>
            primary_cluster_id: <p>For replication groups with a single primary, if this parameter is specified, ElastiCache promotes the specified cluster in the specified replication group to the primary role. The nodes of all other clusters in the replication group are read replicas.</p>
            snapshotting_cluster_id: <p>The cluster ID that is used as the daily snapshot source for the replication group. This parameter cannot be set for Valkey or Redis OSS (cluster mode enabled) replication groups.</p>
            automatic_failover_enabled: <p>Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure.</p> <p>Valid values: <code>true</code> | <code>false</code> </p>
            multi_az_enabled: <p>A flag to indicate MultiAZ is enabled.</p>
            node_group_id: <p>Deprecated. This parameter is not used.</p>
            cache_security_group_names: <p>A list of cache security group names to authorize for the clusters in this replication group. This change is asynchronously applied as soon as possible.</p> <p>This parameter can be used only with replication group containing clusters running outside of an Amazon Virtual Private Cloud (Amazon VPC).</p> <p>Constraints: Must contain no more than 255 alphanumeric characters. Must not be <code>Default</code>.</p>
            security_group_ids: <p>Specifies the VPC Security Groups associated with the clusters in the replication group.</p> <p>This parameter can be used only with replication group containing clusters running in an Amazon Virtual Private Cloud (Amazon VPC).</p>
            preferred_maintenance_window: <p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>
            notification_topic_arn: <p>The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.</p> <note> <p>The Amazon SNS topic owner must be same as the replication group owner. </p> </note>
            cache_parameter_group_name: <p>The name of the cache parameter group to apply to all of the clusters in this replication group. This change is asynchronously applied as soon as possible for parameters when the <code>ApplyImmediately</code> parameter is specified as <code>true</code> for this request.</p>
            notification_topic_status: <p>The status of the Amazon SNS notification topic for the replication group. Notifications are sent only if the status is <code>active</code>.</p> <p>Valid values: <code>active</code> | <code>inactive</code> </p>
            apply_immediately: <p>If <code>true</code>, this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the replication group.</p> <p>If <code>false</code>, changes to the nodes in the replication group are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.</p> <p>Valid values: <code>true</code> | <code>false</code> </p> <p>Default: <code>false</code> </p>
            engine: <p>Modifies the engine listed in a replication group message. The options are valkey, memcached or redis.</p>
            engine_version: <p>The upgraded version of the cache engine to be run on the clusters in the replication group.</p> <p> <b>Important:</b> You can upgrade to a newer engine version (see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement">Selecting a Cache Engine and Version</a>), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing replication group and create it anew with the earlier engine version. </p>
            auto_minor_version_upgrade: <p> If you are running Valkey or Redis OSS engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions. </p>
            snapshot_retention_limit: <p>The number of days for which ElastiCache retains automatic node group (shard) snapshots before deleting them. For example, if you set <code>SnapshotRetentionLimit</code> to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p> <p> <b>Important</b> If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.</p>
            snapshot_window: <p>The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of the node group (shard) specified by <code>SnapshottingClusterId</code>.</p> <p>Example: <code>05:00-09:00</code> </p> <p>If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.</p>
            cache_node_type: <p>A valid cache node type that you want to scale this replication group to.</p>
            auth_token: <p>Reserved parameter. The password used to access a password protected server. This parameter must be specified with the <code>auth-token-update-strategy </code> parameter. Password constraints:</p> <ul> <li> <p>Must be only printable ASCII characters</p> </li> <li> <p>Must be at least 16 characters and no more than 128 characters in length</p> </li> <li> <p>Cannot contain any of the following characters: '/', '"', or '@', '%'</p> </li> </ul> <p> For more information, see AUTH password at <a href="http://redis.io/commands/AUTH">AUTH</a>.</p>
            auth_token_update_strategy: <p>Specifies the strategy to use to update the AUTH token. This parameter must be specified with the <code>auth-token</code> parameter. Possible values:</p> <ul> <li> <p>ROTATE - default, if no update strategy is provided</p> </li> <li> <p>SET - allowed only after ROTATE</p> </li> <li> <p>DELETE - allowed only when transitioning to RBAC</p> </li> </ul> <p> For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html">Authenticating Users with AUTH</a> </p>
            user_group_ids_to_add: <p>The ID of the user group you are associating with the replication group.</p>
            user_group_ids_to_remove: <p>The ID of the user group to disassociate from the replication group, meaning the users in the group no longer can access the replication group.</p>
            remove_user_groups: <p>Removes the user group associated with this replication group.</p>
            log_delivery_configurations: <p>Specifies the destination, format and type of the logs.</p>
            ip_discovery: <p>The network type you choose when modifying a cluster, either <code>ipv4</code> | <code>ipv6</code>. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the <a href="http://aws.amazon.com/ec2/nitro/">Nitro system</a>.</p>
            transit_encryption_enabled: <p>A flag that enables in-transit encryption when set to true. If you are enabling in-transit encryption for an existing cluster, you must also set <code>TransitEncryptionMode</code> to <code>preferred</code>.</p>
            transit_encryption_mode: <p>A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.</p> <p>You must set <code>TransitEncryptionEnabled</code> to <code>true</code>, for your existing cluster, and set <code>TransitEncryptionMode</code> to <code>preferred</code> in the same request to allow both encrypted and unencrypted connections at the same time. Once you migrate all your Valkey or Redis OSS clients to use encrypted connections you can set the value to <code>required</code> to allow encrypted connections only.</p> <p>Setting <code>TransitEncryptionMode</code> to <code>required</code> is a two-step process that requires you to first set the <code>TransitEncryptionMode</code> to <code>preferred</code>, after that you can set <code>TransitEncryptionMode</code> to <code>required</code>. </p>
            cluster_mode: <p>Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled.</p>
            durability: <p>Specifies the durability setting for the replication group. Use this parameter to change the durability mode of an existing replication group, for example from <code>sync</code> to <code>async</code> or vice versa. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/durability.html">Durability</a>.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault: <p>The requested cache security group name does not refer to an existing cache security group.</p>
            capo_elasticache.errors.insufficient_cache_cluster_capacity_fault.InsufficientCacheClusterCapacityFault: <p>The requested cache node type is not available in the specified Availability Zone. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ErrorMessages.html#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY">InsufficientCacheClusterCapacity</a> in the ElastiCache User Guide.</p>
            capo_elasticache.errors.invalid_cache_cluster_state_fault.InvalidCacheClusterStateFault: <p>The requested cluster is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_cache_security_group_state_fault.InvalidCacheSecurityGroupStateFault: <p>The current state of the cache security group does not allow deletion.</p>
            capo_elasticache.errors.invalid_kms_key_fault.InvalidKMSKeyFault: <p>The KMS key supplied is not valid.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_user_group_state_fault.InvalidUserGroupStateFault: <p>The user group is not in an active state.</p>
            capo_elasticache.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The VPC network is in an invalid state.</p>
            capo_elasticache.errors.node_quota_for_cluster_exceeded_fault.NodeQuotaForClusterExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache nodes in a single cluster.</p>
            capo_elasticache.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache nodes per customer.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.user_group_not_found_fault.UserGroupNotFoundFault: <p>The user group was not found or does not exist</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ModifyReplicationGroup

            >>> await client.modify_replication_group(replication_group_id='my-redis-rg', replication_group_description='Modified replication group', snapshotting_cluster_id='my-redis-rg-001', apply_immediately=True, snapshot_retention_limit=30)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.modify_replication_group_message.ModifyReplicationGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.modify_replication_group_result.ModifyReplicationGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.modify_replication_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.modify_replication_group.async_modify_replication_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.modify_replication_group_message.ModifyReplicationGroupMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if replication_group_description is not None:
            input_["replication_group_description"] = replication_group_description
        if primary_cluster_id is not None:
            input_["primary_cluster_id"] = primary_cluster_id
        if snapshotting_cluster_id is not None:
            input_["snapshotting_cluster_id"] = snapshotting_cluster_id
        if automatic_failover_enabled is not None:
            input_["automatic_failover_enabled"] = automatic_failover_enabled
        if multi_az_enabled is not None:
            input_["multi_az_enabled"] = multi_az_enabled
        if node_group_id is not None:
            input_["node_group_id"] = node_group_id
        if cache_security_group_names is not None:
            input_["cache_security_group_names"] = cache_security_group_names
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if notification_topic_arn is not None:
            input_["notification_topic_arn"] = notification_topic_arn
        if cache_parameter_group_name is not None:
            input_["cache_parameter_group_name"] = cache_parameter_group_name
        if notification_topic_status is not None:
            input_["notification_topic_status"] = notification_topic_status
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if snapshot_retention_limit is not None:
            input_["snapshot_retention_limit"] = snapshot_retention_limit
        if snapshot_window is not None:
            input_["snapshot_window"] = snapshot_window
        if cache_node_type is not None:
            input_["cache_node_type"] = cache_node_type
        if auth_token is not None:
            input_["auth_token"] = auth_token
        if auth_token_update_strategy is not None:
            input_["auth_token_update_strategy"] = auth_token_update_strategy
        if user_group_ids_to_add is not None:
            input_["user_group_ids_to_add"] = user_group_ids_to_add
        if user_group_ids_to_remove is not None:
            input_["user_group_ids_to_remove"] = user_group_ids_to_remove
        if remove_user_groups is not None:
            input_["remove_user_groups"] = remove_user_groups
        if log_delivery_configurations is not None:
            input_["log_delivery_configurations"] = log_delivery_configurations
        if ip_discovery is not None:
            input_["ip_discovery"] = ip_discovery
        if transit_encryption_enabled is not None:
            input_["transit_encryption_enabled"] = transit_encryption_enabled
        if transit_encryption_mode is not None:
            input_["transit_encryption_mode"] = transit_encryption_mode
        if cluster_mode is not None:
            input_["cluster_mode"] = cluster_mode
        if durability is not None:
            input_["durability"] = durability

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_replication_group_shard_configuration(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        node_group_count: Optional["capo_elasticache.types.integer.Integer"] = None,
        apply_immediately: Optional["capo_elasticache.types.boolean.Boolean"] = None,
        resharding_configuration: Optional[
            "capo_elasticache.types.resharding_configuration_list.ReshardingConfigurationList"
        ] = None,
        node_groups_to_remove: Optional[
            "capo_elasticache.types.node_groups_to_remove_list.NodeGroupsToRemoveList"
        ] = None,
        node_groups_to_retain: Optional[
            "capo_elasticache.types.node_groups_to_retain_list.NodeGroupsToRetainList"
        ] = None,
    ) -> "capo_elasticache.types.modify_replication_group_shard_configuration_result.ModifyReplicationGroupShardConfigurationResult":
        """<p>Modifies a replication group's shards (node groups) by allowing you to add shards, remove shards, or rebalance the keyspaces among existing shards.</p>

        Args:
            replication_group_id: <p>The name of the Valkey or Redis OSS (cluster mode enabled) cluster (replication group) on which the shards are to be configured.</p>
            node_group_count: <p>The number of node groups (shards) that results from the modification of the shard configuration.</p>
            apply_immediately: <p>Indicates that the shard reconfiguration process begins immediately. At present, the only permitted value for this parameter is <code>true</code>.</p> <p>Value: true</p>
            resharding_configuration: <p>Specifies the preferred availability zones for each node group in the cluster. If the value of <code>NodeGroupCount</code> is greater than the current number of node groups (shards), you can use this parameter to specify the preferred availability zones of the cluster's shards. If you omit this parameter ElastiCache selects availability zones for you.</p> <p>You can specify this parameter only if the value of <code>NodeGroupCount</code> is greater than the current number of node groups (shards).</p>
            node_groups_to_remove: <p>If the value of <code>NodeGroupCount</code> is less than the current number of node groups (shards), then either <code>NodeGroupsToRemove</code> or <code>NodeGroupsToRetain</code> is required. <code>NodeGroupsToRemove</code> is a list of <code>NodeGroupId</code>s to remove from the cluster.</p> <p>ElastiCache will attempt to remove all node groups listed by <code>NodeGroupsToRemove</code> from the cluster.</p>
            node_groups_to_retain: <p>If the value of <code>NodeGroupCount</code> is less than the current number of node groups (shards), then either <code>NodeGroupsToRemove</code> or <code>NodeGroupsToRetain</code> is required. <code>NodeGroupsToRetain</code> is a list of <code>NodeGroupId</code>s to retain in the cluster.</p> <p>ElastiCache will attempt to remove all node groups except those listed by <code>NodeGroupsToRetain</code> from the cluster.</p>

        Raises:
            capo_elasticache.errors.insufficient_cache_cluster_capacity_fault.InsufficientCacheClusterCapacityFault: <p>The requested cache node type is not available in the specified Availability Zone. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ErrorMessages.html#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY">InsufficientCacheClusterCapacity</a> in the ElastiCache User Guide.</p>
            capo_elasticache.errors.invalid_cache_cluster_state_fault.InvalidCacheClusterStateFault: <p>The requested cluster is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_kms_key_fault.InvalidKMSKeyFault: <p>The KMS key supplied is not valid.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The VPC network is in an invalid state.</p>
            capo_elasticache.errors.node_groups_per_replication_group_quota_exceeded_fault.NodeGroupsPerReplicationGroupQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum allowed number of node groups (shards) in a single replication group. The default maximum is 90</p>
            capo_elasticache.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the allowed number of cache nodes per customer.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.modify_replication_group_shard_configuration_message.ModifyReplicationGroupShardConfigurationMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.modify_replication_group_shard_configuration_result.ModifyReplicationGroupShardConfigurationResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.modify_replication_group_shard_configuration

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.modify_replication_group_shard_configuration.async_modify_replication_group_shard_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.modify_replication_group_shard_configuration_message.ModifyReplicationGroupShardConfigurationMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if node_group_count is not None:
            input_["node_group_count"] = node_group_count
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately
        if resharding_configuration is not None:
            input_["resharding_configuration"] = resharding_configuration
        if node_groups_to_remove is not None:
            input_["node_groups_to_remove"] = node_groups_to_remove
        if node_groups_to_retain is not None:
            input_["node_groups_to_retain"] = node_groups_to_retain

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_serverless_cache(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        serverless_cache_name: Optional["capo_elasticache.types.string.String"] = None,
        description: Optional["capo_elasticache.types.string.String"] = None,
        cache_usage_limits: Optional[
            "capo_elasticache.types.cache_usage_limits.CacheUsageLimits"
        ] = None,
        remove_user_group: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        user_group_id: Optional["capo_elasticache.types.string.String"] = None,
        security_group_ids: Optional[
            "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
        ] = None,
        snapshot_retention_limit: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        daily_snapshot_time: Optional["capo_elasticache.types.string.String"] = None,
        engine: Optional["capo_elasticache.types.string.String"] = None,
        major_engine_version: Optional["capo_elasticache.types.string.String"] = None,
    ) -> "capo_elasticache.types.modify_serverless_cache_response.ModifyServerlessCacheResponse":
        """<p>This API modifies the attributes of a serverless cache.</p>

        Args:
            serverless_cache_name: <p>User-provided identifier for the serverless cache to be modified.</p>
            description: <p>User provided description for the serverless cache. Default = NULL, i.e. the existing description is not removed/modified. The description has a maximum length of 255 characters.</p>
            cache_usage_limits: <p>Modify the cache usage limit for the serverless cache.</p>
            remove_user_group: <p>The identifier of the UserGroup to be removed from association with the Valkey and Redis OSS serverless cache. Available for Valkey and Redis OSS only. Default is NULL.</p>
            user_group_id: <p>The identifier of the UserGroup to be associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL - the existing UserGroup is not removed.</p>
            security_group_ids: <p>The new list of VPC security groups to be associated with the serverless cache. Populating this list means the current VPC security groups will be removed. This security group is used to authorize traffic access for the VPC end-point (private-link). Default = NULL - the existing list of VPC security groups is not removed.</p>
            snapshot_retention_limit: <p>The number of days for which Elasticache retains automatic snapshots before deleting them. Available for Valkey, Redis OSS and Serverless Memcached only. Default = NULL, i.e. the existing snapshot-retention-limit will not be removed or modified. The maximum value allowed is 35 days.</p>
            daily_snapshot_time: <p>The daily time during which Elasticache begins taking a daily snapshot of the serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only. The default is NULL, i.e. the existing snapshot time configured for the cluster is not removed.</p>
            engine: <p>Modifies the engine listed in a serverless cache request. The options are valkey, memcached or redis.</p>
            major_engine_version: <p>Modifies the engine vesion listed in a serverless cache request. </p>

        Raises:
            capo_elasticache.errors.invalid_credentials_exception.InvalidCredentialsException: <p>You must enter valid credentials.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_serverless_cache_state_fault.InvalidServerlessCacheStateFault: <p>The account for these credentials is not currently active.</p>
            capo_elasticache.errors.invalid_user_group_state_fault.InvalidUserGroupStateFault: <p>The user group is not in an active state.</p>
            capo_elasticache.errors.serverless_cache_not_found_fault.ServerlessCacheNotFoundFault: <p>The serverless cache was not found or does not exist.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.user_group_not_found_fault.UserGroupNotFoundFault: <p>The user group was not found or does not exist</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.modify_serverless_cache_request.ModifyServerlessCacheRequest]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.modify_serverless_cache_response.ModifyServerlessCacheResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.modify_serverless_cache

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.modify_serverless_cache.async_modify_serverless_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.modify_serverless_cache_request.ModifyServerlessCacheRequest = {}
        if serverless_cache_name is not None:
            input_["serverless_cache_name"] = serverless_cache_name
        if description is not None:
            input_["description"] = description
        if cache_usage_limits is not None:
            input_["cache_usage_limits"] = cache_usage_limits
        if remove_user_group is not None:
            input_["remove_user_group"] = remove_user_group
        if user_group_id is not None:
            input_["user_group_id"] = user_group_id
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if snapshot_retention_limit is not None:
            input_["snapshot_retention_limit"] = snapshot_retention_limit
        if daily_snapshot_time is not None:
            input_["daily_snapshot_time"] = daily_snapshot_time
        if engine is not None:
            input_["engine"] = engine
        if major_engine_version is not None:
            input_["major_engine_version"] = major_engine_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_user(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        user_id: Optional["capo_elasticache.types.user_id.UserId"] = None,
        access_string: Optional[
            "capo_elasticache.types.access_string.AccessString"
        ] = None,
        append_access_string: Optional[
            "capo_elasticache.types.access_string.AccessString"
        ] = None,
        passwords: Optional[
            "capo_elasticache.types.password_list_input.PasswordListInput"
        ] = None,
        no_password_required: Optional[
            "capo_elasticache.types.boolean_optional.BooleanOptional"
        ] = None,
        authentication_mode: Optional[
            "capo_elasticache.types.authentication_mode.AuthenticationMode"
        ] = None,
        engine: Optional["capo_elasticache.types.engine_type.EngineType"] = None,
    ) -> "capo_elasticache.types.user.User":
        """<p>Changes user password(s) and/or access string.</p>

        Args:
            user_id: <p>The ID of the user.</p>
            access_string: <p>Access permissions string used for this user.</p>
            append_access_string: <p>Adds additional user permissions to the access string.</p>
            passwords: <p>The passwords belonging to the user. You are allowed up to two.</p>
            no_password_required: <p>Indicates no password is required for the user.</p>
            authentication_mode: <p>Specifies how to authenticate the user.</p>
            engine: <p>Modifies the engine listed for a user. The options are valkey or redis.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_user_state_fault.InvalidUserStateFault: <p>The user is not in active state.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.user_not_found_fault.UserNotFoundFault: <p>The user does not exist or could not be found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.modify_user_message.ModifyUserMessage]",
        ) -> AsyncOperationResponse["capo_elasticache.types.user.User"]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.modify_user

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.modify_user.async_modify_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.modify_user_message.ModifyUserMessage = {}
        if user_id is not None:
            input_["user_id"] = user_id
        if access_string is not None:
            input_["access_string"] = access_string
        if append_access_string is not None:
            input_["append_access_string"] = append_access_string
        if passwords is not None:
            input_["passwords"] = passwords
        if no_password_required is not None:
            input_["no_password_required"] = no_password_required
        if authentication_mode is not None:
            input_["authentication_mode"] = authentication_mode
        if engine is not None:
            input_["engine"] = engine

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_user_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        user_group_id: Optional["capo_elasticache.types.string.String"] = None,
        user_ids_to_add: Optional[
            "capo_elasticache.types.user_id_list_input.UserIdListInput"
        ] = None,
        user_ids_to_remove: Optional[
            "capo_elasticache.types.user_id_list_input.UserIdListInput"
        ] = None,
        engine: Optional["capo_elasticache.types.engine_type.EngineType"] = None,
    ) -> "capo_elasticache.types.user_group.UserGroup":
        """<p>Changes the list of users that belong to the user group.</p>

        Args:
            user_group_id: <p>The ID of the user group.</p>
            user_ids_to_add: <p>The list of user IDs to add to the user group.</p>
            user_ids_to_remove: <p>The list of user IDs to remove from the user group.</p>
            engine: <p>Modifies the engine listed in a user group. The options are valkey or redis.</p>

        Raises:
            capo_elasticache.errors.default_user_required.DefaultUserRequired: <p>You must add default user to a user group.</p>
            capo_elasticache.errors.duplicate_user_name_fault.DuplicateUserNameFault: <p>A user with this username already exists.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_user_group_state_fault.InvalidUserGroupStateFault: <p>The user group is not in an active state.</p>
            capo_elasticache.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_elasticache.errors.user_group_not_found_fault.UserGroupNotFoundFault: <p>The user group was not found or does not exist</p>
            capo_elasticache.errors.user_not_found_fault.UserNotFoundFault: <p>The user does not exist or could not be found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.modify_user_group_message.ModifyUserGroupMessage]",
        ) -> AsyncOperationResponse["capo_elasticache.types.user_group.UserGroup"]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.modify_user_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.modify_user_group.async_modify_user_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.modify_user_group_message.ModifyUserGroupMessage = {}
        if user_group_id is not None:
            input_["user_group_id"] = user_group_id
        if user_ids_to_add is not None:
            input_["user_ids_to_add"] = user_ids_to_add
        if user_ids_to_remove is not None:
            input_["user_ids_to_remove"] = user_ids_to_remove
        if engine is not None:
            input_["engine"] = engine

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def purchase_reserved_cache_nodes_offering(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        reserved_cache_nodes_offering_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        reserved_cache_node_id: Optional["capo_elasticache.types.string.String"] = None,
        cache_node_count: Optional[
            "capo_elasticache.types.integer_optional.IntegerOptional"
        ] = None,
        tags: Optional["capo_elasticache.types.tag_list.TagList"] = None,
    ) -> "capo_elasticache.types.purchase_reserved_cache_nodes_offering_result.PurchaseReservedCacheNodesOfferingResult":
        """<p>Allows you to purchase a reserved cache node offering. Reserved nodes are not eligible for cancellation and are non-refundable. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/reserved-nodes.html">Managing Costs with Reserved Nodes</a>.</p>

        Args:
            reserved_cache_nodes_offering_id: <p>The ID of the reserved cache node offering to purchase.</p> <p>Example: <code>438012d3-4052-4cc7-b2e3-8d3372e0e706</code> </p>
            reserved_cache_node_id: <p>A customer-specified identifier to track this reservation.</p> <note> <p>The Reserved Cache Node ID is an unique customer-specified identifier to track this reservation. If this parameter is not specified, ElastiCache automatically generates an identifier for the reservation.</p> </note> <p>Example: myreservationID</p>
            cache_node_count: <p>The number of cache node instances to reserve.</p> <p>Default: <code>1</code> </p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.reserved_cache_node_already_exists_fault.ReservedCacheNodeAlreadyExistsFault: <p>You already have a reservation with the given identifier.</p>
            capo_elasticache.errors.reserved_cache_node_quota_exceeded_fault.ReservedCacheNodeQuotaExceededFault: <p>The request cannot be processed because it would exceed the user's cache node quota.</p>
            capo_elasticache.errors.reserved_cache_nodes_offering_not_found_fault.ReservedCacheNodesOfferingNotFoundFault: <p>The requested cache node offering does not exist.</p>
            capo_elasticache.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            PurchaseReservedCacheNodesOfferings
            Allows you to purchase a reserved cache node offering.

            >>> await client.purchase_reserved_cache_nodes_offering(reserved_cache_nodes_offering_id='1ef01f5b-94ff-433f-a530-61a56bfc8e7a')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.purchase_reserved_cache_nodes_offering_message.PurchaseReservedCacheNodesOfferingMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.purchase_reserved_cache_nodes_offering_result.PurchaseReservedCacheNodesOfferingResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.purchase_reserved_cache_nodes_offering

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.purchase_reserved_cache_nodes_offering.async_purchase_reserved_cache_nodes_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.purchase_reserved_cache_nodes_offering_message.PurchaseReservedCacheNodesOfferingMessage = {}
        if reserved_cache_nodes_offering_id is not None:
            input_["reserved_cache_nodes_offering_id"] = (
                reserved_cache_nodes_offering_id
            )
        if reserved_cache_node_id is not None:
            input_["reserved_cache_node_id"] = reserved_cache_node_id
        if cache_node_count is not None:
            input_["cache_node_count"] = cache_node_count
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def rebalance_slots_in_global_replication_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        global_replication_group_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        apply_immediately: Optional["capo_elasticache.types.boolean.Boolean"] = None,
    ) -> "capo_elasticache.types.rebalance_slots_in_global_replication_group_result.RebalanceSlotsInGlobalReplicationGroupResult":
        """<p>Redistribute slots to ensure uniform distribution across existing shards in the cluster.</p>

        Args:
            global_replication_group_id: <p>The name of the Global datastore</p>
            apply_immediately: <p>If <code>True</code>, redistribution is applied immediately.</p>

        Raises:
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.invalid_global_replication_group_state_fault.InvalidGlobalReplicationGroupStateFault: <p>The Global datastore is not available or in primary-only state.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.rebalance_slots_in_global_replication_group_message.RebalanceSlotsInGlobalReplicationGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.rebalance_slots_in_global_replication_group_result.RebalanceSlotsInGlobalReplicationGroupResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.rebalance_slots_in_global_replication_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.rebalance_slots_in_global_replication_group.async_rebalance_slots_in_global_replication_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.rebalance_slots_in_global_replication_group_message.RebalanceSlotsInGlobalReplicationGroupMessage = {}
        if global_replication_group_id is not None:
            input_["global_replication_group_id"] = global_replication_group_id
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reboot_cache_cluster(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_cluster_id: Optional["capo_elasticache.types.string.String"] = None,
        cache_node_ids_to_reboot: Optional[
            "capo_elasticache.types.cache_node_ids_list.CacheNodeIdsList"
        ] = None,
    ) -> "capo_elasticache.types.reboot_cache_cluster_result.RebootCacheClusterResult":
        """<p>Reboots some, or all, of the cache nodes within a provisioned cluster. This operation applies any modified cache parameter groups to the cluster. The reboot operation takes place as soon as possible, and results in a momentary outage to the cluster. During the reboot, the cluster status is set to REBOOTING.</p> <p>The reboot causes the contents of the cache (for each cache node being rebooted) to be lost.</p> <p>When the reboot is complete, a cluster event is created.</p> <p>Rebooting a cluster is currently supported on Memcached, Valkey and Redis OSS (cluster mode disabled) clusters. Rebooting is not supported on Valkey or Redis OSS (cluster mode enabled) clusters.</p> <p>If you make changes to parameters that require a Valkey or Redis OSS (cluster mode enabled) cluster reboot for the changes to be applied, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/nodes.rebooting.html">Rebooting a Cluster</a> for an alternate process.</p>

        Args:
            cache_cluster_id: <p>The cluster identifier. This parameter is stored as a lowercase string.</p>
            cache_node_ids_to_reboot: <p>A list of cache node IDs to reboot. A node ID is a numeric identifier (0001, 0002, etc.). To reboot an entire cluster, specify all of the cache node IDs.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.invalid_cache_cluster_state_fault.InvalidCacheClusterStateFault: <p>The requested cluster is not in the <code>available</code> state.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            RebootCacheCluster
            Reboots the specified nodes in the names cluster.

            >>> await client.reboot_cache_cluster(cache_cluster_id='custom-mem1-4  ', cache_node_ids_to_reboot=['0001', '0002'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.reboot_cache_cluster_message.RebootCacheClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.reboot_cache_cluster_result.RebootCacheClusterResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.reboot_cache_cluster

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.reboot_cache_cluster.async_reboot_cache_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.reboot_cache_cluster_message.RebootCacheClusterMessage = {}
        if cache_cluster_id is not None:
            input_["cache_cluster_id"] = cache_cluster_id
        if cache_node_ids_to_reboot is not None:
            input_["cache_node_ids_to_reboot"] = cache_node_ids_to_reboot

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_tags_from_resource(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        resource_name: Optional["capo_elasticache.types.string.String"] = None,
        tag_keys: Optional["capo_elasticache.types.key_list.KeyList"] = None,
    ) -> "capo_elasticache.types.tag_list_message.TagListMessage":
        """<p>Removes the tags identified by the <code>TagKeys</code> list from the named resource. A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your ElastiCache resources. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. For more information, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.ResourceLevelPermissions.html">Resource-level permissions</a>.</p>

        Args:
            resource_name: <p>The Amazon Resource Name (ARN) of the resource from which you want the tags removed, for example <code>arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster</code> or <code>arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot</code>.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Service Namespaces</a>.</p>
            tag_keys: <p>A list of <code>TagKeys</code> identifying the tags you want removed from the named resource.</p>

        Raises:
            capo_elasticache.errors.cache_cluster_not_found_fault.CacheClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing cluster.</p>
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault: <p>The requested cache security group name does not refer to an existing cache security group.</p>
            capo_elasticache.errors.cache_subnet_group_not_found_fault.CacheSubnetGroupNotFoundFault: <p>The requested cache subnet group name does not refer to an existing cache subnet group.</p>
            capo_elasticache.errors.global_replication_group_not_found_fault.GlobalReplicationGroupNotFoundFault: <p>The Global datastore does not exist</p>
            capo_elasticache.errors.invalid_arn_fault.InvalidARNFault: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_serverless_cache_snapshot_state_fault.InvalidServerlessCacheSnapshotStateFault: <p>The state of the serverless cache snapshot was not received. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.invalid_serverless_cache_state_fault.InvalidServerlessCacheStateFault: <p>The account for these credentials is not currently active.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.reserved_cache_node_not_found_fault.ReservedCacheNodeNotFoundFault: <p>The requested reserved cache node was not found.</p>
            capo_elasticache.errors.serverless_cache_not_found_fault.ServerlessCacheNotFoundFault: <p>The serverless cache was not found or does not exist.</p>
            capo_elasticache.errors.serverless_cache_snapshot_not_found_fault.ServerlessCacheSnapshotNotFoundFault: <p>This serverless cache snapshot could not be found or does not exist. Available for Valkey, Redis OSS and Serverless Memcached only.</p>
            capo_elasticache.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The requested snapshot name does not refer to an existing snapshot.</p>
            capo_elasticache.errors.tag_not_found_fault.TagNotFoundFault: <p>The requested tag was not found on this resource.</p>
            capo_elasticache.errors.user_group_not_found_fault.UserGroupNotFoundFault: <p>The user group was not found or does not exist</p>
            capo_elasticache.errors.user_not_found_fault.UserNotFoundFault: <p>The user does not exist or could not be found.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            RemoveTagsFromResource
            Removes tags identified by a list of tag keys from the list of tags on the specified resource.

            >>> await client.remove_tags_from_resource(resource_name='arn:aws:elasticache:us-east-1:1234567890:cluster:my-mem-cluster', tag_keys=['A', 'C', 'E'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.remove_tags_from_resource_message.RemoveTagsFromResourceMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.tag_list_message.TagListMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.remove_tags_from_resource

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.remove_tags_from_resource.async_remove_tags_from_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.remove_tags_from_resource_message.RemoveTagsFromResourceMessage = {}
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

    async def reset_cache_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_parameter_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        reset_all_parameters: Optional["capo_elasticache.types.boolean.Boolean"] = None,
        parameter_name_values: Optional[
            "capo_elasticache.types.parameter_name_value_list.ParameterNameValueList"
        ] = None,
    ) -> "capo_elasticache.types.cache_parameter_group_name_message.CacheParameterGroupNameMessage":
        """<p>Modifies the parameters of a cache parameter group to the engine or system default value. You can reset specific parameters by submitting a list of parameter names. To reset the entire cache parameter group, specify the <code>ResetAllParameters</code> and <code>CacheParameterGroupName</code> parameters.</p>

        Args:
            cache_parameter_group_name: <p>The name of the cache parameter group to reset.</p>
            reset_all_parameters: <p>If <code>true</code>, all parameters in the cache parameter group are reset to their default values. If <code>false</code>, only the parameters listed by <code>ParameterNameValues</code> are reset to their default values.</p> <p>Valid values: <code>true</code> | <code>false</code> </p>
            parameter_name_values: <p>An array of parameter names to reset to their default values. If <code>ResetAllParameters</code> is <code>true</code>, do not use <code>ParameterNameValues</code>. If <code>ResetAllParameters</code> is <code>false</code>, you must specify the name of at least one parameter to reset.</p>

        Raises:
            capo_elasticache.errors.cache_parameter_group_not_found_fault.CacheParameterGroupNotFoundFault: <p>The requested cache parameter group name does not refer to an existing cache parameter group.</p>
            capo_elasticache.errors.invalid_cache_parameter_group_state_fault.InvalidCacheParameterGroupStateFault: <p>The current state of the cache parameter group does not allow the requested operation to occur.</p>
            capo_elasticache.errors.invalid_global_replication_group_state_fault.InvalidGlobalReplicationGroupStateFault: <p>The Global datastore is not available or in primary-only state.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ResetCacheParameterGroup
            Modifies the parameters of a cache parameter group to the engine or system default value.

            >>> await client.reset_cache_parameter_group(cache_parameter_group_name='custom-mem1-4', reset_all_parameters=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.reset_cache_parameter_group_message.ResetCacheParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.cache_parameter_group_name_message.CacheParameterGroupNameMessage"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.reset_cache_parameter_group

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.reset_cache_parameter_group.async_reset_cache_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.reset_cache_parameter_group_message.ResetCacheParameterGroupMessage = {}
        if cache_parameter_group_name is not None:
            input_["cache_parameter_group_name"] = cache_parameter_group_name
        if reset_all_parameters is not None:
            input_["reset_all_parameters"] = reset_all_parameters
        if parameter_name_values is not None:
            input_["parameter_name_values"] = parameter_name_values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def revoke_cache_security_group_ingress(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        cache_security_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        ec2_security_group_name: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
        ec2_security_group_owner_id: Optional[
            "capo_elasticache.types.string.String"
        ] = None,
    ) -> "capo_elasticache.types.revoke_cache_security_group_ingress_result.RevokeCacheSecurityGroupIngressResult":
        """<p>Revokes ingress from a cache security group. Use this operation to disallow access from an Amazon EC2 security group that had been previously authorized.</p>

        Args:
            cache_security_group_name: <p>The name of the cache security group to revoke ingress from.</p>
            ec2_security_group_name: <p>The name of the Amazon EC2 security group to revoke access from.</p>
            ec2_security_group_owner_id: <p>The Amazon account number of the Amazon EC2 security group owner. Note that this is not the same thing as an Amazon access key ID - you must provide a valid Amazon account number for this parameter.</p>

        Raises:
            capo_elasticache.errors.authorization_not_found_fault.AuthorizationNotFoundFault: <p>The specified Amazon EC2 security group is not authorized for the specified cache security group.</p>
            capo_elasticache.errors.cache_security_group_not_found_fault.CacheSecurityGroupNotFoundFault: <p>The requested cache security group name does not refer to an existing cache security group.</p>
            capo_elasticache.errors.invalid_cache_security_group_state_fault.InvalidCacheSecurityGroupStateFault: <p>The current state of the cache security group does not allow deletion.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeCacheSecurityGroups
            Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group.

            >>> await client.revoke_cache_security_group_ingress(cache_security_group_name='my-sec-grp', ec2_security_group_name='my-ec2-sec-grp', ec2_security_group_owner_id='1234567890')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.revoke_cache_security_group_ingress_message.RevokeCacheSecurityGroupIngressMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.revoke_cache_security_group_ingress_result.RevokeCacheSecurityGroupIngressResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.revoke_cache_security_group_ingress

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.revoke_cache_security_group_ingress.async_revoke_cache_security_group_ingress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.revoke_cache_security_group_ingress_message.RevokeCacheSecurityGroupIngressMessage = {}
        if cache_security_group_name is not None:
            input_["cache_security_group_name"] = cache_security_group_name
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

    async def start_migration(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        customer_node_endpoint_list: Optional[
            "capo_elasticache.types.customer_node_endpoint_list.CustomerNodeEndpointList"
        ] = None,
    ) -> "capo_elasticache.types.start_migration_response.StartMigrationResponse":
        """<p>Start the migration of data.</p>

        Args:
            replication_group_id: <p>The ID of the replication group to which data should be migrated.</p>
            customer_node_endpoint_list: <p>List of endpoints from which data should be migrated. For Valkey or Redis OSS (cluster mode disabled), the list should have only one element.</p>

        Raises:
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.replication_group_already_under_migration_fault.ReplicationGroupAlreadyUnderMigrationFault: <p>The targeted replication group is not available. </p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.start_migration_message.StartMigrationMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.start_migration_response.StartMigrationResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.start_migration

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.start_migration.async_start_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.start_migration_message.StartMigrationMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if customer_node_endpoint_list is not None:
            input_["customer_node_endpoint_list"] = customer_node_endpoint_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def test_failover(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        node_group_id: Optional[
            "capo_elasticache.types.allowed_node_group_id.AllowedNodeGroupId"
        ] = None,
    ) -> "capo_elasticache.types.test_failover_result.TestFailoverResult":
        """<p>Represents the input of a <code>TestFailover</code> operation which tests automatic failover on a specified node group (called shard in the console) in a replication group (called cluster in the console).</p> <p>This API is designed for testing the behavior of your application in case of ElastiCache failover. It is not designed to be an operational tool for initiating a failover to overcome a problem you may have with the cluster. Moreover, in certain conditions such as large-scale operational events, Amazon may block this API. </p> <p class="title"> <b>Note the following</b> </p> <ul> <li> <p>A customer can use this operation to test automatic failover on up to 15 shards (called node groups in the ElastiCache API and Amazon CLI) in any rolling 24-hour period.</p> </li> <li> <p>If calling this operation on shards in different clusters (called replication groups in the API and CLI), the calls can be made concurrently.</p> <p> </p> </li> <li> <p>If calling this operation multiple times on different shards in the same Valkey or Redis OSS (cluster mode enabled) replication group, the first node replacement must complete before a subsequent call can be made.</p> </li> <li> <p>To determine whether the node replacement is complete you can check Events using the Amazon ElastiCache console, the Amazon CLI, or the ElastiCache API. Look for the following automatic failover related events, listed here in order of occurrance:</p> <ol> <li> <p>Replication group message: <code>Test Failover API called for node group <node-group-id></code> </p> </li> <li> <p>Cache cluster message: <code>Failover from primary node <primary-node-id> to replica node <node-id> completed</code> </p> </li> <li> <p>Replication group message: <code>Failover from primary node <primary-node-id> to replica node <node-id> completed</code> </p> </li> <li> <p>Cache cluster message: <code>Recovering cache nodes <node-id></code> </p> </li> <li> <p>Cache cluster message: <code>Finished recovery for cache nodes <node-id></code> </p> </li> </ol> <p>For more information see:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ECEvents.Viewing.html">Viewing ElastiCache Events</a> in the <i>ElastiCache User Guide</i> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeEvents.html">DescribeEvents</a> in the ElastiCache API Reference</p> </li> </ul> </li> </ul> <p>Also see, <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html#auto-failover-test">Testing Multi-AZ </a> in the <i>ElastiCache User Guide</i>.</p>

        Args:
            replication_group_id: <p>The name of the replication group (console: cluster) whose automatic failover is being tested by this operation.</p>
            node_group_id: <p>The name of the node group (called shard in the console) in this replication group on which automatic failover is to be tested. You may test automatic failover on up to 15 node groups in any rolling 24-hour period.</p>

        Raises:
            capo_elasticache.errors.api_call_rate_for_customer_exceeded_fault.APICallRateForCustomerExceededFault: <p>The customer has exceeded the allowed rate of API calls.</p>
            capo_elasticache.errors.invalid_cache_cluster_state_fault.InvalidCacheClusterStateFault: <p>The requested cluster is not in the <code>available</code> state.</p>
            capo_elasticache.errors.invalid_kms_key_fault.InvalidKMSKeyFault: <p>The KMS key supplied is not valid.</p>
            capo_elasticache.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.node_group_not_found_fault.NodeGroupNotFoundFault: <p>The node group specified by the <code>NodeGroupId</code> parameter could not be found. Please verify that the node group exists and that you spelled the <code>NodeGroupId</code> value correctly.</p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.test_failover_not_available_fault.TestFailoverNotAvailableFault: <p>The <code>TestFailover</code> action is not available.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.test_failover_message.TestFailoverMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.test_failover_result.TestFailoverResult"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.test_failover

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.test_failover.async_test_failover(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.test_failover_message.TestFailoverMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if node_group_id is not None:
            input_["node_group_id"] = node_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def test_migration(
        self,
        *,
        config_overrides: Optional[AsyncElastiCacheClientConfig] = None,
        replication_group_id: Optional["capo_elasticache.types.string.String"] = None,
        customer_node_endpoint_list: Optional[
            "capo_elasticache.types.customer_node_endpoint_list.CustomerNodeEndpointList"
        ] = None,
    ) -> "capo_elasticache.types.test_migration_response.TestMigrationResponse":
        """<p> Async API to test connection between source and target replication group. </p>

        Args:
            replication_group_id: <p> The ID of the replication group to which data is to be migrated. </p>
            customer_node_endpoint_list: <p> List of endpoints from which data should be migrated. List should have only one element. </p>

        Raises:
            capo_elasticache.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_elasticache.errors.invalid_replication_group_state_fault.InvalidReplicationGroupStateFault: <p>The requested replication group is not in the <code>available</code> state.</p>
            capo_elasticache.errors.replication_group_already_under_migration_fault.ReplicationGroupAlreadyUnderMigrationFault: <p>The targeted replication group is not available. </p>
            capo_elasticache.errors.replication_group_not_found_fault.ReplicationGroupNotFoundFault: <p>The specified replication group does not exist.</p>
            capo_elasticache.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elasticache.types.test_migration_message.TestMigrationMessage]",
        ) -> AsyncOperationResponse[
            "capo_elasticache.types.test_migration_response.TestMigrationResponse"
        ]:
            import capo_elasticache._operations.amazon_elasti_cache_v9.test_migration

            (
                output,
                http_response,
            ) = await capo_elasticache._operations.amazon_elasti_cache_v9.test_migration.async_test_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticache.types.test_migration_message.TestMigrationMessage = {}
        if replication_group_id is not None:
            input_["replication_group_id"] = replication_group_id
        if customer_node_endpoint_list is not None:
            input_["customer_node_endpoint_list"] = customer_node_endpoint_list

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
