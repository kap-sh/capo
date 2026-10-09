"""Generated from Smithy shape ``com.amazonaws.memorydb#AmazonMemoryDB``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_memorydb._auth._signers
import capo_memorydb._auth._sigv4
from capo_memorydb._auth._identity import Credentials
from capo_memorydb._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_memorydb._auth._zapros_handler import AuthMiddleware
from capo_memorydb._pagination import resolve_path as _resolve_path
from capo_memorydb._services._aws_config import aaws_config
from capo_memorydb._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_memorydb.types.access_string
    import capo_memorydb.types.acl
    import capo_memorydb.types.acl_name
    import capo_memorydb.types.authentication_mode
    import capo_memorydb.types.batch_update_cluster_request
    import capo_memorydb.types.batch_update_cluster_response
    import capo_memorydb.types.boolean
    import capo_memorydb.types.boolean_optional
    import capo_memorydb.types.cluster
    import capo_memorydb.types.cluster_name_list
    import capo_memorydb.types.copy_snapshot_request
    import capo_memorydb.types.copy_snapshot_response
    import capo_memorydb.types.create_acl_request
    import capo_memorydb.types.create_acl_response
    import capo_memorydb.types.create_cluster_request
    import capo_memorydb.types.create_cluster_response
    import capo_memorydb.types.create_multi_region_cluster_request
    import capo_memorydb.types.create_multi_region_cluster_response
    import capo_memorydb.types.create_parameter_group_request
    import capo_memorydb.types.create_parameter_group_response
    import capo_memorydb.types.create_snapshot_request
    import capo_memorydb.types.create_snapshot_response
    import capo_memorydb.types.create_subnet_group_request
    import capo_memorydb.types.create_subnet_group_response
    import capo_memorydb.types.create_user_request
    import capo_memorydb.types.create_user_response
    import capo_memorydb.types.delete_acl_request
    import capo_memorydb.types.delete_acl_response
    import capo_memorydb.types.delete_cluster_request
    import capo_memorydb.types.delete_cluster_response
    import capo_memorydb.types.delete_multi_region_cluster_request
    import capo_memorydb.types.delete_multi_region_cluster_response
    import capo_memorydb.types.delete_parameter_group_request
    import capo_memorydb.types.delete_parameter_group_response
    import capo_memorydb.types.delete_snapshot_request
    import capo_memorydb.types.delete_snapshot_response
    import capo_memorydb.types.delete_subnet_group_request
    import capo_memorydb.types.delete_subnet_group_response
    import capo_memorydb.types.delete_user_request
    import capo_memorydb.types.delete_user_response
    import capo_memorydb.types.describe_ac_ls_request
    import capo_memorydb.types.describe_ac_ls_response
    import capo_memorydb.types.describe_clusters_request
    import capo_memorydb.types.describe_clusters_response
    import capo_memorydb.types.describe_engine_versions_request
    import capo_memorydb.types.describe_engine_versions_response
    import capo_memorydb.types.describe_events_request
    import capo_memorydb.types.describe_events_response
    import capo_memorydb.types.describe_multi_region_clusters_request
    import capo_memorydb.types.describe_multi_region_clusters_response
    import capo_memorydb.types.describe_multi_region_parameter_groups_request
    import capo_memorydb.types.describe_multi_region_parameter_groups_response
    import capo_memorydb.types.describe_multi_region_parameters_request
    import capo_memorydb.types.describe_multi_region_parameters_response
    import capo_memorydb.types.describe_parameter_groups_request
    import capo_memorydb.types.describe_parameter_groups_response
    import capo_memorydb.types.describe_parameters_request
    import capo_memorydb.types.describe_parameters_response
    import capo_memorydb.types.describe_reserved_nodes_offerings_request
    import capo_memorydb.types.describe_reserved_nodes_offerings_response
    import capo_memorydb.types.describe_reserved_nodes_request
    import capo_memorydb.types.describe_reserved_nodes_response
    import capo_memorydb.types.describe_service_updates_request
    import capo_memorydb.types.describe_service_updates_response
    import capo_memorydb.types.describe_snapshots_request
    import capo_memorydb.types.describe_snapshots_response
    import capo_memorydb.types.describe_subnet_groups_request
    import capo_memorydb.types.describe_subnet_groups_response
    import capo_memorydb.types.describe_users_request
    import capo_memorydb.types.describe_users_response
    import capo_memorydb.types.engine_version_info
    import capo_memorydb.types.event
    import capo_memorydb.types.failover_shard_request
    import capo_memorydb.types.failover_shard_response
    import capo_memorydb.types.filter_list
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.ip_discovery
    import capo_memorydb.types.key_list
    import capo_memorydb.types.kms_key_id
    import capo_memorydb.types.list_allowed_multi_region_cluster_updates_request
    import capo_memorydb.types.list_allowed_multi_region_cluster_updates_response
    import capo_memorydb.types.list_allowed_node_type_updates_request
    import capo_memorydb.types.list_allowed_node_type_updates_response
    import capo_memorydb.types.list_tags_request
    import capo_memorydb.types.list_tags_response
    import capo_memorydb.types.multi_region_cluster
    import capo_memorydb.types.network_type
    import capo_memorydb.types.parameter
    import capo_memorydb.types.parameter_group
    import capo_memorydb.types.parameter_name_list
    import capo_memorydb.types.parameter_name_value_list
    import capo_memorydb.types.purchase_reserved_nodes_offering_request
    import capo_memorydb.types.purchase_reserved_nodes_offering_response
    import capo_memorydb.types.replica_configuration_request
    import capo_memorydb.types.reserved_node
    import capo_memorydb.types.reserved_nodes_offering
    import capo_memorydb.types.reset_parameter_group_request
    import capo_memorydb.types.reset_parameter_group_response
    import capo_memorydb.types.security_group_ids_list
    import capo_memorydb.types.service_update
    import capo_memorydb.types.service_update_request
    import capo_memorydb.types.service_update_status_list
    import capo_memorydb.types.shard_configuration_request
    import capo_memorydb.types.snapshot
    import capo_memorydb.types.snapshot_arns_list
    import capo_memorydb.types.source_type
    import capo_memorydb.types.string
    import capo_memorydb.types.subnet_group
    import capo_memorydb.types.subnet_identifier_list
    import capo_memorydb.types.t_stamp
    import capo_memorydb.types.tag_list
    import capo_memorydb.types.tag_resource_request
    import capo_memorydb.types.tag_resource_response
    import capo_memorydb.types.target_bucket
    import capo_memorydb.types.untag_resource_request
    import capo_memorydb.types.untag_resource_response
    import capo_memorydb.types.update_acl_request
    import capo_memorydb.types.update_acl_response
    import capo_memorydb.types.update_cluster_request
    import capo_memorydb.types.update_cluster_response
    import capo_memorydb.types.update_multi_region_cluster_request
    import capo_memorydb.types.update_multi_region_cluster_response
    import capo_memorydb.types.update_parameter_group_request
    import capo_memorydb.types.update_parameter_group_response
    import capo_memorydb.types.update_strategy
    import capo_memorydb.types.update_subnet_group_request
    import capo_memorydb.types.update_subnet_group_response
    import capo_memorydb.types.update_user_request
    import capo_memorydb.types.update_user_response
    import capo_memorydb.types.user
    import capo_memorydb.types.user_name
    import capo_memorydb.types.user_name_list_input


class AsyncMemoryDBClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncMemoryDBClient:
    """A client for the ``MemoryDB`` service.

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
        self._config = AsyncMemoryDBClientConfig(
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
        self, config_overrides: Optional[AsyncMemoryDBClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMemoryDBClientConfig = config_overrides or {}
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

    async def batch_update_cluster(
        self,
        cluster_names: "capo_memorydb.types.cluster_name_list.ClusterNameList",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        service_update: Optional[
            "capo_memorydb.types.service_update_request.ServiceUpdateRequest"
        ] = None,
    ) -> "capo_memorydb.types.batch_update_cluster_response.BatchUpdateClusterResponse":
        """<p>Apply the service update to a list of clusters supplied. For more information on service updates and applying them, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/managing-updates.html#applying-updates">Applying the service updates</a>.</p>

        Args:
            cluster_names: <p>The cluster names to apply the updates.</p>
            service_update: <p>The unique ID of the service update</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.service_update_not_found_fault.ServiceUpdateNotFoundFault: <p>The specified service update does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.batch_update_cluster_request.BatchUpdateClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.batch_update_cluster_response.BatchUpdateClusterResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.batch_update_cluster

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.batch_update_cluster.async_batch_update_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.batch_update_cluster_request.BatchUpdateClusterRequest = {
            "cluster_names": cluster_names
        }
        if service_update is not None:
            input_["service_update"] = service_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def copy_snapshot(
        self,
        source_snapshot_name: "capo_memorydb.types.string.String",
        target_snapshot_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        target_bucket: Optional[
            "capo_memorydb.types.target_bucket.TargetBucket"
        ] = None,
        kms_key_id: Optional["capo_memorydb.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_memorydb.types.tag_list.TagList"] = None,
    ) -> "capo_memorydb.types.copy_snapshot_response.CopySnapshotResponse":
        """<p>Makes a copy of an existing snapshot.</p>

        Args:
            source_snapshot_name: <p>The name of an existing snapshot from which to make a copy.</p>
            target_snapshot_name: <p>A name for the snapshot copy. MemoryDB does not permit overwriting a snapshot, therefore this name must be unique within its context - MemoryDB or an Amazon S3 bucket if exporting.</p>
            target_bucket: <p>The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access. When using this parameter to export a snapshot, be sure MemoryDB has the needed permissions to this S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/snapshots-exporting.html">Step 2: Grant MemoryDB Access to Your Amazon S3 Bucket</a>. </p>
            kms_key_id: <p>The ID of the KMS key used to encrypt the target snapshot.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.invalid_snapshot_state_fault.InvalidSnapshotStateFault: <p>The snapshot is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.snapshot_already_exists_fault.SnapshotAlreadyExistsFault: <p>A snapshot with the specified name already exists.</p>
            capo_memorydb.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The specified snapshot does not exist.</p>
            capo_memorydb.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of snapshots allowed.</p>
            capo_memorydb.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would exceed the maximum number of tags allowed per resource.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.copy_snapshot_request.CopySnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.copy_snapshot_response.CopySnapshotResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.copy_snapshot

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.copy_snapshot.async_copy_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.copy_snapshot_request.CopySnapshotRequest = {
            "source_snapshot_name": source_snapshot_name,
            "target_snapshot_name": target_snapshot_name,
        }
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

    async def create_acl(
        self,
        acl_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        user_names: Optional[
            "capo_memorydb.types.user_name_list_input.UserNameListInput"
        ] = None,
        tags: Optional["capo_memorydb.types.tag_list.TagList"] = None,
    ) -> "capo_memorydb.types.create_acl_response.CreateACLResponse":
        """<p>Creates an Access Control List. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html">Authenticating users with Access Contol Lists (ACLs)</a>.</p>

        Args:
            acl_name: <p>The name of the Access Control List.</p>
            user_names: <p>The list of users that belong to the Access Control List.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_memorydb.errors.acl_already_exists_fault.ACLAlreadyExistsFault: <p>An ACL with the specified name already exists.</p>
            capo_memorydb.errors.acl_quota_exceeded_fault.ACLQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of ACLs allowed.</p>
            capo_memorydb.errors.default_user_required.DefaultUserRequired: <p>A default user is required and must be specified.</p>
            capo_memorydb.errors.duplicate_user_name_fault.DuplicateUserNameFault: <p>A user with the specified name already exists.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would exceed the maximum number of tags allowed per resource.</p>
            capo_memorydb.errors.user_not_found_fault.UserNotFoundFault: <p>The specified user does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.create_acl_request.CreateACLRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.create_acl_response.CreateACLResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.create_acl

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.create_acl.async_create_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.create_acl_request.CreateACLRequest = {
            "acl_name": acl_name
        }
        if user_names is not None:
            input_["user_names"] = user_names
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cluster(
        self,
        cluster_name: "capo_memorydb.types.string.String",
        node_type: "capo_memorydb.types.string.String",
        acl_name: "capo_memorydb.types.acl_name.ACLName",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        multi_region_cluster_name: Optional["capo_memorydb.types.string.String"] = None,
        parameter_group_name: Optional["capo_memorydb.types.string.String"] = None,
        description: Optional["capo_memorydb.types.string.String"] = None,
        num_shards: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        num_replicas_per_shard: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        subnet_group_name: Optional["capo_memorydb.types.string.String"] = None,
        security_group_ids: Optional[
            "capo_memorydb.types.security_group_ids_list.SecurityGroupIdsList"
        ] = None,
        maintenance_window: Optional["capo_memorydb.types.string.String"] = None,
        port: Optional["capo_memorydb.types.integer_optional.IntegerOptional"] = None,
        sns_topic_arn: Optional["capo_memorydb.types.string.String"] = None,
        tls_enabled: Optional[
            "capo_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
        kms_key_id: Optional["capo_memorydb.types.string.String"] = None,
        snapshot_arns: Optional[
            "capo_memorydb.types.snapshot_arns_list.SnapshotArnsList"
        ] = None,
        snapshot_name: Optional["capo_memorydb.types.string.String"] = None,
        snapshot_retention_limit: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        tags: Optional["capo_memorydb.types.tag_list.TagList"] = None,
        snapshot_window: Optional["capo_memorydb.types.string.String"] = None,
        engine: Optional["capo_memorydb.types.string.String"] = None,
        engine_version: Optional["capo_memorydb.types.string.String"] = None,
        auto_minor_version_upgrade: Optional[
            "capo_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
        data_tiering: Optional[
            "capo_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
        network_type: Optional["capo_memorydb.types.network_type.NetworkType"] = None,
        ip_discovery: Optional["capo_memorydb.types.ip_discovery.IpDiscovery"] = None,
    ) -> "capo_memorydb.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates a cluster. All nodes in the cluster run the same protocol-compliant engine software.</p>

        Args:
            cluster_name: <p>The name of the cluster. This value must be unique as it also serves as the cluster identifier.</p>
            node_type: <p>The compute and memory capacity of the nodes in the cluster.</p>
            multi_region_cluster_name: <p>The name of the multi-Region cluster to be created.</p>
            parameter_group_name: <p>The name of the parameter group associated with the cluster.</p>
            description: <p>An optional description of the cluster.</p>
            num_shards: <p>The number of shards the cluster will contain. The default value is 1. </p>
            num_replicas_per_shard: <p>The number of replicas to apply to each shard. The default value is 1. The maximum is 5. </p>
            subnet_group_name: <p>The name of the subnet group to be used for the cluster.</p>
            security_group_ids: <p>A list of security group names to associate with this cluster.</p>
            maintenance_window: <p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>
            port: <p>The port number on which each of the nodes accepts connections.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.</p>
            tls_enabled: <p>A flag to enable in-transit encryption on the cluster.</p>
            kms_key_id: <p>The ID of the KMS key used to encrypt the cluster.</p>
            snapshot_arns: <p>A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new cluster. The Amazon S3 object name in the ARN cannot contain any commas.</p>
            snapshot_name: <p>The name of a snapshot from which to restore data into the new cluster. The snapshot status changes to restoring while the new cluster is being created.</p>
            snapshot_retention_limit: <p>The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p>
            tags: <p>A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key=myKey, Value=myKeyValue. You can include multiple tags as shown following: Key=myKey, Value=myKeyValue Key=mySecondKey, Value=mySecondKeyValue.</p>
            snapshot_window: <p>The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard.</p> <p> Example: 05:00-09:00</p> <p> If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.</p>
            acl_name: <p>The name of the Access Control List to associate with the cluster.</p>
            engine: <p>The name of the engine to be used for the cluster.</p>
            engine_version: <p>The version number of the Redis OSS engine to be used for the cluster.</p>
            auto_minor_version_upgrade: <p>When set to true, the cluster will automatically receive minor engine version upgrades after launch.</p>
            data_tiering: <p>Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see <a href="https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html">Data tiering</a>.</p>
            network_type: <p>Specifies the IP address type for the cluster. Valid values are 'ipv4', 'ipv6', or 'dual_stack'. When set to 'ipv4', the cluster will only be accessible via IPv4 addresses. When set to 'ipv6', the cluster will only be accessible via IPv6 addresses. When set to 'dual_stack', the cluster will be accessible via both IPv4 and IPv6 addresses. If not specified, the default is 'ipv4'.</p>
            ip_discovery: <p>The mechanism for discovering IP addresses for the cluster discovery protocol. Valid values are 'ipv4' or 'ipv6'. When set to 'ipv4', cluster discovery functions such as cluster slots, cluster shards, and cluster nodes return IPv4 addresses for cluster nodes. When set to 'ipv6', the cluster discovery functions return IPv6 addresses for cluster nodes. The value must be compatible with the NetworkType parameter. If not specified, the default is 'ipv4'.</p>

        Raises:
            capo_memorydb.errors.acl_not_found_fault.ACLNotFoundFault: <p>The specified ACL does not exist.</p>
            capo_memorydb.errors.cluster_already_exists_fault.ClusterAlreadyExistsFault: <p>A cluster with the specified name already exists.</p>
            capo_memorydb.errors.cluster_quota_for_customer_exceeded_fault.ClusterQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the maximum number of clusters allowed for this customer.</p>
            capo_memorydb.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault: <p>The cluster does not have sufficient capacity to perform the requested operation.</p>
            capo_memorydb.errors.invalid_acl_state_fault.InvalidACLStateFault: <p>The ACL is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_credentials_exception.InvalidCredentialsException: <p>The provided credentials are not valid.</p>
            capo_memorydb.errors.invalid_multi_region_cluster_state_fault.InvalidMultiRegionClusterStateFault: <p>The requested operation cannot be performed on the multi-Region cluster in its current state.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The VPC network is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.multi_region_cluster_not_found_fault.MultiRegionClusterNotFoundFault: <p>The specified multi-Region cluster does not exist.</p>
            capo_memorydb.errors.node_quota_for_cluster_exceeded_fault.NodeQuotaForClusterExceededFault: <p>The request cannot be processed because it would exceed the maximum number of nodes allowed for this cluster.</p>
            capo_memorydb.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the maximum number of nodes allowed for this customer.</p>
            capo_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.shards_per_cluster_quota_exceeded_fault.ShardsPerClusterQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of shards allowed per cluster.</p>
            capo_memorydb.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault: <p>The specified subnet group does not exist.</p>
            capo_memorydb.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would exceed the maximum number of tags allowed per resource.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.create_cluster_request.CreateClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.create_cluster_response.CreateClusterResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.create_cluster

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.create_cluster_request.CreateClusterRequest = {
            "cluster_name": cluster_name,
            "node_type": node_type,
            "acl_name": acl_name,
        }
        if multi_region_cluster_name is not None:
            input_["multi_region_cluster_name"] = multi_region_cluster_name
        if parameter_group_name is not None:
            input_["parameter_group_name"] = parameter_group_name
        if description is not None:
            input_["description"] = description
        if num_shards is not None:
            input_["num_shards"] = num_shards
        if num_replicas_per_shard is not None:
            input_["num_replicas_per_shard"] = num_replicas_per_shard
        if subnet_group_name is not None:
            input_["subnet_group_name"] = subnet_group_name
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window
        if port is not None:
            input_["port"] = port
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if tls_enabled is not None:
            input_["tls_enabled"] = tls_enabled
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if snapshot_arns is not None:
            input_["snapshot_arns"] = snapshot_arns
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
        if snapshot_retention_limit is not None:
            input_["snapshot_retention_limit"] = snapshot_retention_limit
        if tags is not None:
            input_["tags"] = tags
        if snapshot_window is not None:
            input_["snapshot_window"] = snapshot_window
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if data_tiering is not None:
            input_["data_tiering"] = data_tiering
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

    async def create_multi_region_cluster(
        self,
        multi_region_cluster_name_suffix: "capo_memorydb.types.string.String",
        node_type: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        description: Optional["capo_memorydb.types.string.String"] = None,
        engine: Optional["capo_memorydb.types.string.String"] = None,
        engine_version: Optional["capo_memorydb.types.string.String"] = None,
        multi_region_parameter_group_name: Optional[
            "capo_memorydb.types.string.String"
        ] = None,
        num_shards: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        tls_enabled: Optional[
            "capo_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
        tags: Optional["capo_memorydb.types.tag_list.TagList"] = None,
    ) -> "capo_memorydb.types.create_multi_region_cluster_response.CreateMultiRegionClusterResponse":
        """<p>Creates a new multi-Region cluster.</p>

        Args:
            multi_region_cluster_name_suffix: <p>A suffix to be added to the Multi-Region cluster name. Amazon MemoryDB automatically applies a prefix to the Multi-Region cluster Name when it is created. Each Amazon Region has its own prefix. For instance, a Multi-Region cluster Name created in the US-West-1 region will begin with "virxk", along with the suffix name you provide. The suffix guarantees uniqueness of the Multi-Region cluster name across multiple regions.</p>
            description: <p>A description for the multi-Region cluster.</p>
            engine: <p>The name of the engine to be used for the multi-Region cluster.</p>
            engine_version: <p>The version of the engine to be used for the multi-Region cluster.</p>
            node_type: <p>The node type to be used for the multi-Region cluster.</p>
            multi_region_parameter_group_name: <p>The name of the multi-Region parameter group to be associated with the cluster.</p>
            num_shards: <p>The number of shards for the multi-Region cluster.</p>
            tls_enabled: <p>Whether to enable TLS encryption for the multi-Region cluster.</p>
            tags: <p>A list of tags to be applied to the multi-Region cluster.</p>

        Raises:
            capo_memorydb.errors.cluster_quota_for_customer_exceeded_fault.ClusterQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the maximum number of clusters allowed for this customer.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.multi_region_cluster_already_exists_fault.MultiRegionClusterAlreadyExistsFault: <p>A multi-Region cluster with the specified name already exists.</p>
            capo_memorydb.errors.multi_region_parameter_group_not_found_fault.MultiRegionParameterGroupNotFoundFault: <p>The specified multi-Region parameter group does not exist.</p>
            capo_memorydb.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would exceed the maximum number of tags allowed per resource.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.create_multi_region_cluster_request.CreateMultiRegionClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.create_multi_region_cluster_response.CreateMultiRegionClusterResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.create_multi_region_cluster

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.create_multi_region_cluster.async_create_multi_region_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.create_multi_region_cluster_request.CreateMultiRegionClusterRequest = {
            "multi_region_cluster_name_suffix": multi_region_cluster_name_suffix,
            "node_type": node_type,
        }
        if description is not None:
            input_["description"] = description
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if multi_region_parameter_group_name is not None:
            input_["multi_region_parameter_group_name"] = (
                multi_region_parameter_group_name
            )
        if num_shards is not None:
            input_["num_shards"] = num_shards
        if tls_enabled is not None:
            input_["tls_enabled"] = tls_enabled
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_parameter_group(
        self,
        parameter_group_name: "capo_memorydb.types.string.String",
        family: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        description: Optional["capo_memorydb.types.string.String"] = None,
        tags: Optional["capo_memorydb.types.tag_list.TagList"] = None,
    ) -> "capo_memorydb.types.create_parameter_group_response.CreateParameterGroupResponse":
        """<p>Creates a new MemoryDB parameter group. A parameter group is a collection of parameters and their values that are applied to all of the nodes in any cluster. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/parametergroups.html">Configuring engine parameters using parameter groups</a>. </p>

        Args:
            parameter_group_name: <p>The name of the parameter group.</p>
            family: <p>The name of the parameter group family that the parameter group can be used with.</p>
            description: <p>An optional description of the parameter group.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_group_state_fault.InvalidParameterGroupStateFault: <p>The parameter group is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.parameter_group_already_exists_fault.ParameterGroupAlreadyExistsFault: <p>A parameter group with the specified name already exists.</p>
            capo_memorydb.errors.parameter_group_quota_exceeded_fault.ParameterGroupQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of parameter groups allowed.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would exceed the maximum number of tags allowed per resource.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.create_parameter_group_request.CreateParameterGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.create_parameter_group_response.CreateParameterGroupResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.create_parameter_group

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.create_parameter_group.async_create_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.create_parameter_group_request.CreateParameterGroupRequest = {
            "parameter_group_name": parameter_group_name,
            "family": family,
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

    async def create_snapshot(
        self,
        cluster_name: "capo_memorydb.types.string.String",
        snapshot_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        kms_key_id: Optional["capo_memorydb.types.string.String"] = None,
        tags: Optional["capo_memorydb.types.tag_list.TagList"] = None,
    ) -> "capo_memorydb.types.create_snapshot_response.CreateSnapshotResponse":
        """<p>Creates a copy of an entire cluster at a specific moment in time.</p>

        Args:
            cluster_name: <p>The snapshot is created from this cluster.</p>
            snapshot_name: <p>A name for the snapshot being created.</p>
            kms_key_id: <p>The ID of the KMS key used to encrypt the snapshot.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_memorydb.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The specified cluster does not exist.</p>
            capo_memorydb.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The cluster is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.snapshot_already_exists_fault.SnapshotAlreadyExistsFault: <p>A snapshot with the specified name already exists.</p>
            capo_memorydb.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of snapshots allowed.</p>
            capo_memorydb.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would exceed the maximum number of tags allowed per resource.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.create_snapshot_request.CreateSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.create_snapshot_response.CreateSnapshotResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.create_snapshot

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.create_snapshot.async_create_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.create_snapshot_request.CreateSnapshotRequest = {
            "cluster_name": cluster_name,
            "snapshot_name": snapshot_name,
        }
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

    async def create_subnet_group(
        self,
        subnet_group_name: "capo_memorydb.types.string.String",
        subnet_ids: "capo_memorydb.types.subnet_identifier_list.SubnetIdentifierList",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        description: Optional["capo_memorydb.types.string.String"] = None,
        tags: Optional["capo_memorydb.types.tag_list.TagList"] = None,
    ) -> "capo_memorydb.types.create_subnet_group_response.CreateSubnetGroupResponse":
        """<p>Creates a subnet group. A subnet group is a collection of subnets (typically private) that you can designate for your clusters running in an Amazon Virtual Private Cloud (VPC) environment. When you create a cluster in an Amazon VPC, you must specify a subnet group. MemoryDB uses that subnet group to choose a subnet and IP addresses within that subnet to associate with your nodes. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/subnetgroups.html">Subnets and subnet groups</a>.</p>

        Args:
            subnet_group_name: <p>The name of the subnet group.</p>
            description: <p>A description for the subnet group.</p>
            subnet_ids: <p>A list of VPC subnet IDs for the subnet group.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_memorydb.errors.invalid_subnet.InvalidSubnet: <p>The specified subnet is not valid.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.subnet_group_already_exists_fault.SubnetGroupAlreadyExistsFault: <p>A subnet group with the specified name already exists.</p>
            capo_memorydb.errors.subnet_group_quota_exceeded_fault.SubnetGroupQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of subnet groups allowed.</p>
            capo_memorydb.errors.subnet_not_allowed_fault.SubnetNotAllowedFault: <p>The specified subnet is not allowed for this operation.</p>
            capo_memorydb.errors.subnet_quota_exceeded_fault.SubnetQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of subnets allowed.</p>
            capo_memorydb.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would exceed the maximum number of tags allowed per resource.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.create_subnet_group_request.CreateSubnetGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.create_subnet_group_response.CreateSubnetGroupResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.create_subnet_group

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.create_subnet_group.async_create_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.create_subnet_group_request.CreateSubnetGroupRequest = {
            "subnet_group_name": subnet_group_name,
            "subnet_ids": subnet_ids,
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

    async def create_user(
        self,
        user_name: "capo_memorydb.types.user_name.UserName",
        authentication_mode: "capo_memorydb.types.authentication_mode.AuthenticationMode",
        access_string: "capo_memorydb.types.access_string.AccessString",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        tags: Optional["capo_memorydb.types.tag_list.TagList"] = None,
    ) -> "capo_memorydb.types.create_user_response.CreateUserResponse":
        """<p>Creates a MemoryDB user. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html">Authenticating users with Access Contol Lists (ACLs)</a>.</p>

        Args:
            user_name: <p>The name of the user. This value must be unique as it also serves as the user identifier.</p>
            authentication_mode: <p>Denotes the user's authentication properties, such as whether it requires a password to authenticate.</p>
            access_string: <p>Access permissions string used for this user.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_memorydb.errors.duplicate_user_name_fault.DuplicateUserNameFault: <p>A user with the specified name already exists.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would exceed the maximum number of tags allowed per resource.</p>
            capo_memorydb.errors.user_already_exists_fault.UserAlreadyExistsFault: <p>A user with the specified name already exists.</p>
            capo_memorydb.errors.user_quota_exceeded_fault.UserQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of users allowed.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.create_user_request.CreateUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.create_user_response.CreateUserResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.create_user

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.create_user.async_create_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.create_user_request.CreateUserRequest = {
            "user_name": user_name,
            "authentication_mode": authentication_mode,
            "access_string": access_string,
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

    async def delete_acl(
        self,
        acl_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.delete_acl_response.DeleteACLResponse":
        """<p>Deletes an Access Control List. The ACL must first be disassociated from the cluster before it can be deleted. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/clusters.acls.html">Authenticating users with Access Contol Lists (ACLs)</a>.</p>

        Args:
            acl_name: <p>The name of the Access Control List to delete.</p>

        Raises:
            capo_memorydb.errors.acl_not_found_fault.ACLNotFoundFault: <p>The specified ACL does not exist.</p>
            capo_memorydb.errors.invalid_acl_state_fault.InvalidACLStateFault: <p>The ACL is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.delete_acl_request.DeleteACLRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.delete_acl_response.DeleteACLResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.delete_acl

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.delete_acl.async_delete_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.delete_acl_request.DeleteACLRequest = {
            "acl_name": acl_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster(
        self,
        cluster_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        multi_region_cluster_name: Optional["capo_memorydb.types.string.String"] = None,
        final_snapshot_name: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes a cluster. It also deletes all associated nodes and node endpoints.</p> <note> <p> <code>CreateSnapshot</code> permission is required to create a final snapshot. Without this permission, the API call will fail with an <code>Access Denied</code> exception.</p> </note>

        Args:
            cluster_name: <p>The name of the cluster to be deleted</p>
            multi_region_cluster_name: <p>The name of the multi-Region cluster to be deleted.</p>
            final_snapshot_name: <p>The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.</p>

        Raises:
            capo_memorydb.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The specified cluster does not exist.</p>
            capo_memorydb.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The cluster is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.snapshot_already_exists_fault.SnapshotAlreadyExistsFault: <p>A snapshot with the specified name already exists.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.delete_cluster

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.delete_cluster_request.DeleteClusterRequest = {
            "cluster_name": cluster_name
        }
        if multi_region_cluster_name is not None:
            input_["multi_region_cluster_name"] = multi_region_cluster_name
        if final_snapshot_name is not None:
            input_["final_snapshot_name"] = final_snapshot_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_multi_region_cluster(
        self,
        multi_region_cluster_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.delete_multi_region_cluster_response.DeleteMultiRegionClusterResponse":
        """<p>Deletes an existing multi-Region cluster.</p>

        Args:
            multi_region_cluster_name: <p>The name of the multi-Region cluster to be deleted.</p>

        Raises:
            capo_memorydb.errors.invalid_multi_region_cluster_state_fault.InvalidMultiRegionClusterStateFault: <p>The requested operation cannot be performed on the multi-Region cluster in its current state.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.multi_region_cluster_not_found_fault.MultiRegionClusterNotFoundFault: <p>The specified multi-Region cluster does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.delete_multi_region_cluster_request.DeleteMultiRegionClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.delete_multi_region_cluster_response.DeleteMultiRegionClusterResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.delete_multi_region_cluster

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.delete_multi_region_cluster.async_delete_multi_region_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.delete_multi_region_cluster_request.DeleteMultiRegionClusterRequest = {
            "multi_region_cluster_name": multi_region_cluster_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_parameter_group(
        self,
        parameter_group_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.delete_parameter_group_response.DeleteParameterGroupResponse":
        """<p>Deletes the specified parameter group. You cannot delete a parameter group if it is associated with any clusters. You cannot delete the default parameter groups in your account.</p>

        Args:
            parameter_group_name: <p>The name of the parameter group to delete.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_group_state_fault.InvalidParameterGroupStateFault: <p>The parameter group is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.delete_parameter_group_request.DeleteParameterGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.delete_parameter_group_response.DeleteParameterGroupResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.delete_parameter_group

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.delete_parameter_group.async_delete_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.delete_parameter_group_request.DeleteParameterGroupRequest = {
            "parameter_group_name": parameter_group_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_snapshot(
        self,
        snapshot_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.delete_snapshot_response.DeleteSnapshotResponse":
        """<p>Deletes an existing snapshot. When you receive a successful response from this operation, MemoryDB immediately begins deleting the snapshot; you cannot cancel or revert this operation.</p>

        Args:
            snapshot_name: <p>The name of the snapshot to delete.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.invalid_snapshot_state_fault.InvalidSnapshotStateFault: <p>The snapshot is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The specified snapshot does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.delete_snapshot_request.DeleteSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.delete_snapshot_response.DeleteSnapshotResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.delete_snapshot

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.delete_snapshot.async_delete_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.delete_snapshot_request.DeleteSnapshotRequest = {
            "snapshot_name": snapshot_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_subnet_group(
        self,
        subnet_group_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.delete_subnet_group_response.DeleteSubnetGroupResponse":
        """<p>Deletes a subnet group. You cannot delete a default subnet group or one that is associated with any clusters.</p>

        Args:
            subnet_group_name: <p>The name of the subnet group to delete.</p>

        Raises:
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.subnet_group_in_use_fault.SubnetGroupInUseFault: <p>The subnet group is currently in use and cannot be deleted.</p>
            capo_memorydb.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault: <p>The specified subnet group does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.delete_subnet_group_request.DeleteSubnetGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.delete_subnet_group_response.DeleteSubnetGroupResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.delete_subnet_group

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.delete_subnet_group.async_delete_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.delete_subnet_group_request.DeleteSubnetGroupRequest = {
            "subnet_group_name": subnet_group_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_user(
        self,
        user_name: "capo_memorydb.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.delete_user_response.DeleteUserResponse":
        """<p>Deletes a user. The user will be removed from all ACLs and in turn removed from all clusters.</p>

        Args:
            user_name: <p>The name of the user to delete</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.invalid_user_state_fault.InvalidUserStateFault: <p>The user is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.user_not_found_fault.UserNotFoundFault: <p>The specified user does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.delete_user_request.DeleteUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.delete_user_response.DeleteUserResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.delete_user

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.delete_user.async_delete_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.delete_user_request.DeleteUserRequest = {
            "user_name": user_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_ac_ls(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        acl_name: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.describe_ac_ls_response.DescribeACLsResponse":
        """<p>Returns a list of ACLs.</p>

        Args:
            acl_name: <p>The name of the ACL.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_memorydb.errors.acl_not_found_fault.ACLNotFoundFault: <p>The specified ACL does not exist.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_ac_ls_request.DescribeACLsRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_ac_ls_response.DescribeACLsResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_ac_ls

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_ac_ls.async_describe_ac_ls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_ac_ls_request.DescribeACLsRequest = {}
        if acl_name is not None:
            input_["acl_name"] = acl_name
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

    async def iter_describe_ac_ls(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        acl_name: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[capo_memorydb.types.acl.ACL]":
        _token = next_token
        while True:
            _response = await self.describe_ac_ls(
                config_overrides=config_overrides,
                acl_name=acl_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ac_ls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_clusters(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        cluster_name: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
        show_shard_details: Optional[
            "capo_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_memorydb.types.describe_clusters_response.DescribeClustersResponse":
        """<p>Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cluster if a cluster name is supplied.</p>

        Args:
            cluster_name: <p>The name of the cluster.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
            show_shard_details: <p>An optional flag that can be included in the request to retrieve information about the individual shard(s).</p>

        Raises:
            capo_memorydb.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The specified cluster does not exist.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_clusters_request.DescribeClustersRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_clusters_response.DescribeClustersResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_clusters

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_clusters.async_describe_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_clusters_request.DescribeClustersRequest = {}
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if show_shard_details is not None:
            input_["show_shard_details"] = show_shard_details

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
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        cluster_name: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
        show_shard_details: Optional[
            "capo_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "AsyncIterator[capo_memorydb.types.cluster.Cluster]":
        _token = next_token
        while True:
            _response = await self.describe_clusters(
                config_overrides=config_overrides,
                cluster_name=cluster_name,
                max_results=max_results,
                next_token=_token,
                show_shard_details=show_shard_details,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        engine: Optional["capo_memorydb.types.string.String"] = None,
        engine_version: Optional["capo_memorydb.types.string.String"] = None,
        parameter_group_family: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
        default_only: Optional["capo_memorydb.types.boolean.Boolean"] = None,
    ) -> "capo_memorydb.types.describe_engine_versions_response.DescribeEngineVersionsResponse":
        """<p>Returns a list of the available Redis OSS engine versions.</p>

        Args:
            engine: <p>The name of the engine for which to list available versions.</p>
            engine_version: <p>The Redis OSS engine version</p>
            parameter_group_family: <p>The name of a specific parameter group family to return details for.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
            default_only: <p>If true, specifies that only the default version of the specified engine or engine and major version combination is to be returned.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_engine_versions_request.DescribeEngineVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_engine_versions_response.DescribeEngineVersionsResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_engine_versions

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_engine_versions.async_describe_engine_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_engine_versions_request.DescribeEngineVersionsRequest = {}
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if parameter_group_family is not None:
            input_["parameter_group_family"] = parameter_group_family
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if default_only is not None:
            input_["default_only"] = default_only

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        engine: Optional["capo_memorydb.types.string.String"] = None,
        engine_version: Optional["capo_memorydb.types.string.String"] = None,
        parameter_group_family: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
        default_only: Optional["capo_memorydb.types.boolean.Boolean"] = None,
    ) -> "AsyncIterator[capo_memorydb.types.engine_version_info.EngineVersionInfo]":
        _token = next_token
        while True:
            _response = await self.describe_engine_versions(
                config_overrides=config_overrides,
                engine=engine,
                engine_version=engine_version,
                parameter_group_family=parameter_group_family,
                max_results=max_results,
                next_token=_token,
                default_only=default_only,
            )
            _page = _resolve_path(_response, ("engine_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_events(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        source_name: Optional["capo_memorydb.types.string.String"] = None,
        source_type: Optional["capo_memorydb.types.source_type.SourceType"] = None,
        start_time: Optional["capo_memorydb.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_memorydb.types.t_stamp.TStamp"] = None,
        duration: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.describe_events_response.DescribeEventsResponse":
        """<p>Returns events related to clusters, security groups, and parameter groups. You can obtain events specific to a particular cluster, security group, or parameter group by providing the name as a parameter. By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days' worth of events if necessary.</p>

        Args:
            source_name: <p>The identifier of the event source for which events are returned. If not specified, all sources are included in the response.</p>
            source_type: <p>The event source to retrieve events for. If no value is specified, all events are returned.</p>
            start_time: <p>The beginning of the time interval to retrieve events for, specified in ISO 8601 format. Example: 2017-03-30T07:03:49.555Z</p>
            end_time: <p>The end of the time interval for which to retrieve events, specified in ISO 8601 format. Example: 2017-03-30T07:03:49.555Z</p>
            duration: <p>The number of minutes worth of events to retrieve.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_events_request.DescribeEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_events_response.DescribeEventsResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_events

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_events.async_describe_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_events_request.DescribeEventsRequest = {}
        if source_name is not None:
            input_["source_name"] = source_name
        if source_type is not None:
            input_["source_type"] = source_type
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if duration is not None:
            input_["duration"] = duration
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

    async def iter_describe_events(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        source_name: Optional["capo_memorydb.types.string.String"] = None,
        source_type: Optional["capo_memorydb.types.source_type.SourceType"] = None,
        start_time: Optional["capo_memorydb.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_memorydb.types.t_stamp.TStamp"] = None,
        duration: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[capo_memorydb.types.event.Event]":
        _token = next_token
        while True:
            _response = await self.describe_events(
                config_overrides=config_overrides,
                source_name=source_name,
                source_type=source_type,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_multi_region_clusters(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        multi_region_cluster_name: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
        show_cluster_details: Optional[
            "capo_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_memorydb.types.describe_multi_region_clusters_response.DescribeMultiRegionClustersResponse":
        """<p>Returns details about one or more multi-Region clusters.</p>

        Args:
            multi_region_cluster_name: <p>The name of a specific multi-Region cluster to describe.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A token to specify where to start paginating.</p>
            show_cluster_details: <p>Details about the multi-Region cluster.</p>

        Raises:
            capo_memorydb.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The specified cluster does not exist.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.multi_region_cluster_not_found_fault.MultiRegionClusterNotFoundFault: <p>The specified multi-Region cluster does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_multi_region_clusters_request.DescribeMultiRegionClustersRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_multi_region_clusters_response.DescribeMultiRegionClustersResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_multi_region_clusters

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_multi_region_clusters.async_describe_multi_region_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_multi_region_clusters_request.DescribeMultiRegionClustersRequest = {}
        if multi_region_cluster_name is not None:
            input_["multi_region_cluster_name"] = multi_region_cluster_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if show_cluster_details is not None:
            input_["show_cluster_details"] = show_cluster_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_multi_region_clusters(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        multi_region_cluster_name: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
        show_cluster_details: Optional[
            "capo_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "AsyncIterator[capo_memorydb.types.multi_region_cluster.MultiRegionCluster]":
        _token = next_token
        while True:
            _response = await self.describe_multi_region_clusters(
                config_overrides=config_overrides,
                multi_region_cluster_name=multi_region_cluster_name,
                max_results=max_results,
                next_token=_token,
                show_cluster_details=show_cluster_details,
            )
            _page = _resolve_path(_response, ("multi_region_clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_multi_region_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        multi_region_parameter_group_name: Optional[
            "capo_memorydb.types.string.String"
        ] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.describe_multi_region_parameter_groups_response.DescribeMultiRegionParameterGroupsResponse":
        """<p>Returns a list of multi-region parameter groups.</p>

        Args:
            multi_region_parameter_group_name: <p>The request for information on a specific multi-region parameter group.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.multi_region_parameter_group_not_found_fault.MultiRegionParameterGroupNotFoundFault: <p>The specified multi-Region parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_multi_region_parameter_groups_request.DescribeMultiRegionParameterGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_multi_region_parameter_groups_response.DescribeMultiRegionParameterGroupsResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_multi_region_parameter_groups

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_multi_region_parameter_groups.async_describe_multi_region_parameter_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_multi_region_parameter_groups_request.DescribeMultiRegionParameterGroupsRequest = {}
        if multi_region_parameter_group_name is not None:
            input_["multi_region_parameter_group_name"] = (
                multi_region_parameter_group_name
            )
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

    async def describe_multi_region_parameters(
        self,
        multi_region_parameter_group_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        source: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.describe_multi_region_parameters_response.DescribeMultiRegionParametersResponse":
        """<p>Returns the detailed parameter list for a particular multi-region parameter group.</p>

        Args:
            multi_region_parameter_group_name: <p>The name of the multi-region parameter group to return details for.</p>
            source: <p>The parameter types to return. Valid values: user | system | engine-default</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.multi_region_parameter_group_not_found_fault.MultiRegionParameterGroupNotFoundFault: <p>The specified multi-Region parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_multi_region_parameters_request.DescribeMultiRegionParametersRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_multi_region_parameters_response.DescribeMultiRegionParametersResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_multi_region_parameters

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_multi_region_parameters.async_describe_multi_region_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_multi_region_parameters_request.DescribeMultiRegionParametersRequest = {
            "multi_region_parameter_group_name": multi_region_parameter_group_name
        }
        if source is not None:
            input_["source"] = source
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

    async def describe_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        parameter_group_name: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.describe_parameter_groups_response.DescribeParameterGroupsResponse":
        """<p>Returns a list of parameter group descriptions. If a parameter group name is specified, the list contains only the descriptions for that group.</p>

        Args:
            parameter_group_name: <p>The name of a specific parameter group to return details for.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_parameter_groups_request.DescribeParameterGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_parameter_groups_response.DescribeParameterGroupsResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_parameter_groups

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_parameter_groups.async_describe_parameter_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_parameter_groups_request.DescribeParameterGroupsRequest = {}
        if parameter_group_name is not None:
            input_["parameter_group_name"] = parameter_group_name
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

    async def iter_describe_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        parameter_group_name: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[capo_memorydb.types.parameter_group.ParameterGroup]":
        _token = next_token
        while True:
            _response = await self.describe_parameter_groups(
                config_overrides=config_overrides,
                parameter_group_name=parameter_group_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("parameter_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_parameters(
        self,
        parameter_group_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.describe_parameters_response.DescribeParametersResponse":
        """<p>Returns the detailed parameter list for a particular parameter group.</p>

        Args:
            parameter_group_name: <p>he name of a specific parameter group to return details for.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_parameters_request.DescribeParametersRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_parameters_response.DescribeParametersResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_parameters

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_parameters.async_describe_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_parameters_request.DescribeParametersRequest = {
            "parameter_group_name": parameter_group_name
        }
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

    async def iter_describe_parameters(
        self,
        parameter_group_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[capo_memorydb.types.parameter.Parameter]":
        _token = next_token
        while True:
            _response = await self.describe_parameters(
                parameter_group_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("parameters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_reserved_nodes(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        reservation_id: Optional["capo_memorydb.types.string.String"] = None,
        reserved_nodes_offering_id: Optional[
            "capo_memorydb.types.string.String"
        ] = None,
        node_type: Optional["capo_memorydb.types.string.String"] = None,
        duration: Optional["capo_memorydb.types.string.String"] = None,
        offering_type: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.describe_reserved_nodes_response.DescribeReservedNodesResponse":
        """<p>Returns information about reserved nodes for this account, or about a specified reserved node.</p>

        Args:
            reservation_id: <p>The reserved node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID.</p>
            reserved_nodes_offering_id: <p>The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier.</p>
            node_type: <p>The node type filter value. Use this parameter to show only those reservations matching the specified node type. For more information, see <a href="https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reserved.html#reserved-nodes-supported">Supported node types</a>.</p>
            duration: <p>The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration.</p>
            offering_type: <p>The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type. Valid values: "All Upfront"|"Partial Upfront"| "No Upfront"</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.reserved_node_not_found_fault.ReservedNodeNotFoundFault: <p>The requested node does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_reserved_nodes_request.DescribeReservedNodesRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_reserved_nodes_response.DescribeReservedNodesResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_reserved_nodes

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_reserved_nodes.async_describe_reserved_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_reserved_nodes_request.DescribeReservedNodesRequest = {}
        if reservation_id is not None:
            input_["reservation_id"] = reservation_id
        if reserved_nodes_offering_id is not None:
            input_["reserved_nodes_offering_id"] = reserved_nodes_offering_id
        if node_type is not None:
            input_["node_type"] = node_type
        if duration is not None:
            input_["duration"] = duration
        if offering_type is not None:
            input_["offering_type"] = offering_type
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

    async def iter_describe_reserved_nodes(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        reservation_id: Optional["capo_memorydb.types.string.String"] = None,
        reserved_nodes_offering_id: Optional[
            "capo_memorydb.types.string.String"
        ] = None,
        node_type: Optional["capo_memorydb.types.string.String"] = None,
        duration: Optional["capo_memorydb.types.string.String"] = None,
        offering_type: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[capo_memorydb.types.reserved_node.ReservedNode]":
        _token = next_token
        while True:
            _response = await self.describe_reserved_nodes(
                config_overrides=config_overrides,
                reservation_id=reservation_id,
                reserved_nodes_offering_id=reserved_nodes_offering_id,
                node_type=node_type,
                duration=duration,
                offering_type=offering_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("reserved_nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_reserved_nodes_offerings(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        reserved_nodes_offering_id: Optional[
            "capo_memorydb.types.string.String"
        ] = None,
        node_type: Optional["capo_memorydb.types.string.String"] = None,
        duration: Optional["capo_memorydb.types.string.String"] = None,
        offering_type: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.describe_reserved_nodes_offerings_response.DescribeReservedNodesOfferingsResponse":
        """<p>Lists available reserved node offerings.</p>

        Args:
            reserved_nodes_offering_id: <p>The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.</p>
            node_type: <p>The node type for the reserved nodes. For more information, see <a href="https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reserved.html#reserved-nodes-supported">Supported node types</a>.</p>
            duration: <p>Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.</p>
            offering_type: <p>The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type. Valid values: "All Upfront"|"Partial Upfront"| "No Upfront"</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.reserved_nodes_offering_not_found_fault.ReservedNodesOfferingNotFoundFault: <p>The requested node offering does not exist. </p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_reserved_nodes_offerings_request.DescribeReservedNodesOfferingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_reserved_nodes_offerings_response.DescribeReservedNodesOfferingsResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_reserved_nodes_offerings

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_reserved_nodes_offerings.async_describe_reserved_nodes_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_reserved_nodes_offerings_request.DescribeReservedNodesOfferingsRequest = {}
        if reserved_nodes_offering_id is not None:
            input_["reserved_nodes_offering_id"] = reserved_nodes_offering_id
        if node_type is not None:
            input_["node_type"] = node_type
        if duration is not None:
            input_["duration"] = duration
        if offering_type is not None:
            input_["offering_type"] = offering_type
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

    async def iter_describe_reserved_nodes_offerings(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        reserved_nodes_offering_id: Optional[
            "capo_memorydb.types.string.String"
        ] = None,
        node_type: Optional["capo_memorydb.types.string.String"] = None,
        duration: Optional["capo_memorydb.types.string.String"] = None,
        offering_type: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[capo_memorydb.types.reserved_nodes_offering.ReservedNodesOffering]":
        _token = next_token
        while True:
            _response = await self.describe_reserved_nodes_offerings(
                config_overrides=config_overrides,
                reserved_nodes_offering_id=reserved_nodes_offering_id,
                node_type=node_type,
                duration=duration,
                offering_type=offering_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("reserved_nodes_offerings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_service_updates(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        service_update_name: Optional["capo_memorydb.types.string.String"] = None,
        cluster_names: Optional[
            "capo_memorydb.types.cluster_name_list.ClusterNameList"
        ] = None,
        status: Optional[
            "capo_memorydb.types.service_update_status_list.ServiceUpdateStatusList"
        ] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.describe_service_updates_response.DescribeServiceUpdatesResponse":
        """<p>Returns details of the service updates.</p>

        Args:
            service_update_name: <p>The unique ID of the service update to describe.</p>
            cluster_names: <p>The list of cluster names to identify service updates to apply.</p>
            status: <p>The status(es) of the service updates to filter on.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_service_updates_request.DescribeServiceUpdatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_service_updates_response.DescribeServiceUpdatesResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_service_updates

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_service_updates.async_describe_service_updates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_service_updates_request.DescribeServiceUpdatesRequest = {}
        if service_update_name is not None:
            input_["service_update_name"] = service_update_name
        if cluster_names is not None:
            input_["cluster_names"] = cluster_names
        if status is not None:
            input_["status"] = status
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

    async def iter_describe_service_updates(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        service_update_name: Optional["capo_memorydb.types.string.String"] = None,
        cluster_names: Optional[
            "capo_memorydb.types.cluster_name_list.ClusterNameList"
        ] = None,
        status: Optional[
            "capo_memorydb.types.service_update_status_list.ServiceUpdateStatusList"
        ] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[capo_memorydb.types.service_update.ServiceUpdate]":
        _token = next_token
        while True:
            _response = await self.describe_service_updates(
                config_overrides=config_overrides,
                service_update_name=service_update_name,
                cluster_names=cluster_names,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_updates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        cluster_name: Optional["capo_memorydb.types.string.String"] = None,
        snapshot_name: Optional["capo_memorydb.types.string.String"] = None,
        source: Optional["capo_memorydb.types.string.String"] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        show_detail: Optional[
            "capo_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_memorydb.types.describe_snapshots_response.DescribeSnapshotsResponse":
        """<p>Returns information about cluster snapshots. By default, DescribeSnapshots lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots associated with a particular cluster.</p>

        Args:
            cluster_name: <p>A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described.</p>
            snapshot_name: <p>A user-supplied name of the snapshot. If this parameter is specified, only this named snapshot is described.</p>
            source: <p>If set to system, the output shows snapshots that were automatically created by MemoryDB. If set to user the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            show_detail: <p>A Boolean value which if true, the shard configuration is included in the snapshot description.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The specified snapshot does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_snapshots_request.DescribeSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_snapshots_response.DescribeSnapshotsResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_snapshots

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_snapshots.async_describe_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_snapshots_request.DescribeSnapshotsRequest = {}
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
        if source is not None:
            input_["source"] = source
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if show_detail is not None:
            input_["show_detail"] = show_detail

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
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        cluster_name: Optional["capo_memorydb.types.string.String"] = None,
        snapshot_name: Optional["capo_memorydb.types.string.String"] = None,
        source: Optional["capo_memorydb.types.string.String"] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        show_detail: Optional[
            "capo_memorydb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "AsyncIterator[capo_memorydb.types.snapshot.Snapshot]":
        _token = next_token
        while True:
            _response = await self.describe_snapshots(
                config_overrides=config_overrides,
                cluster_name=cluster_name,
                snapshot_name=snapshot_name,
                source=source,
                next_token=_token,
                max_results=max_results,
                show_detail=show_detail,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        subnet_group_name: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.describe_subnet_groups_response.DescribeSubnetGroupsResponse":
        """<p>Returns a list of subnet group descriptions. If a subnet group name is specified, the list contains only the description of that group.</p>

        Args:
            subnet_group_name: <p>The name of the subnet group to return details for.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault: <p>The specified subnet group does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_subnet_groups_request.DescribeSubnetGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_subnet_groups_response.DescribeSubnetGroupsResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_subnet_groups

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_subnet_groups.async_describe_subnet_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_subnet_groups_request.DescribeSubnetGroupsRequest = {}
        if subnet_group_name is not None:
            input_["subnet_group_name"] = subnet_group_name
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

    async def iter_describe_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        subnet_group_name: Optional["capo_memorydb.types.string.String"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[capo_memorydb.types.subnet_group.SubnetGroup]":
        _token = next_token
        while True:
            _response = await self.describe_subnet_groups(
                config_overrides=config_overrides,
                subnet_group_name=subnet_group_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("subnet_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_users(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        user_name: Optional["capo_memorydb.types.user_name.UserName"] = None,
        filters: Optional["capo_memorydb.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "capo_memorydb.types.describe_users_response.DescribeUsersResponse":
        """<p>Returns a list of users.</p>

        Args:
            user_name: <p>The name of the user.</p>
            filters: <p>Filter to determine the list of users to return.</p>
            max_results: <p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.user_not_found_fault.UserNotFoundFault: <p>The specified user does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.describe_users_request.DescribeUsersRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.describe_users_response.DescribeUsersResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.describe_users

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.describe_users.async_describe_users(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.describe_users_request.DescribeUsersRequest = {}
        if user_name is not None:
            input_["user_name"] = user_name
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_users(
        self,
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        user_name: Optional["capo_memorydb.types.user_name.UserName"] = None,
        filters: Optional["capo_memorydb.types.filter_list.FilterList"] = None,
        max_results: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional["capo_memorydb.types.string.String"] = None,
    ) -> "AsyncIterator[capo_memorydb.types.user.User]":
        _token = next_token
        while True:
            _response = await self.describe_users(
                config_overrides=config_overrides,
                user_name=user_name,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def failover_shard(
        self,
        cluster_name: "capo_memorydb.types.string.String",
        shard_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.failover_shard_response.FailoverShardResponse":
        """<p>Used to failover a shard. This API is designed for testing the behavior of your application in case of MemoryDB failover. It is not designed to be used as a production-level tool for initiating a failover to overcome a problem you may have with the cluster. Moreover, in certain conditions such as large scale operational events, Amazon may block this API. </p>

        Args:
            cluster_name: <p>The cluster being failed over.</p>
            shard_name: <p>The name of the shard.</p>

        Raises:
            capo_memorydb.errors.api_call_rate_for_customer_exceeded_fault.APICallRateForCustomerExceededFault: <p>The customer has exceeded the maximum number of API requests allowed per time period.</p>
            capo_memorydb.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The specified cluster does not exist.</p>
            capo_memorydb.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The cluster is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_kms_key_fault.InvalidKMSKeyFault: <p>The specified KMS key is not valid or accessible.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.shard_not_found_fault.ShardNotFoundFault: <p>The specified shard does not exist.</p>
            capo_memorydb.errors.test_failover_not_available_fault.TestFailoverNotAvailableFault: <p>Test failover is not available for this cluster configuration.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.failover_shard_request.FailoverShardRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.failover_shard_response.FailoverShardResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.failover_shard

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.failover_shard.async_failover_shard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.failover_shard_request.FailoverShardRequest = {
            "cluster_name": cluster_name,
            "shard_name": shard_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_allowed_multi_region_cluster_updates(
        self,
        multi_region_cluster_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.list_allowed_multi_region_cluster_updates_response.ListAllowedMultiRegionClusterUpdatesResponse":
        """<p>Lists the allowed updates for a multi-Region cluster.</p>

        Args:
            multi_region_cluster_name: <p>The name of the multi-Region cluster.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.multi_region_cluster_not_found_fault.MultiRegionClusterNotFoundFault: <p>The specified multi-Region cluster does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.list_allowed_multi_region_cluster_updates_request.ListAllowedMultiRegionClusterUpdatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.list_allowed_multi_region_cluster_updates_response.ListAllowedMultiRegionClusterUpdatesResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.list_allowed_multi_region_cluster_updates

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.list_allowed_multi_region_cluster_updates.async_list_allowed_multi_region_cluster_updates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.list_allowed_multi_region_cluster_updates_request.ListAllowedMultiRegionClusterUpdatesRequest = {
            "multi_region_cluster_name": multi_region_cluster_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_allowed_node_type_updates(
        self,
        cluster_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.list_allowed_node_type_updates_response.ListAllowedNodeTypeUpdatesResponse":
        """<p>Lists all available node types that you can scale to from your cluster's current node type. When you use the UpdateCluster operation to scale your cluster, the value of the NodeType parameter must be one of the node types returned by this operation.</p>

        Args:
            cluster_name: <p>The name of the cluster you want to scale. MemoryDB uses the cluster name to identify the current node type being used by this cluster, and from that to create a list of node types you can scale up to.</p>

        Raises:
            capo_memorydb.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The specified cluster does not exist.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.list_allowed_node_type_updates_request.ListAllowedNodeTypeUpdatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.list_allowed_node_type_updates_response.ListAllowedNodeTypeUpdatesResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.list_allowed_node_type_updates

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.list_allowed_node_type_updates.async_list_allowed_node_type_updates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.list_allowed_node_type_updates_request.ListAllowedNodeTypeUpdatesRequest = {
            "cluster_name": cluster_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags(
        self,
        resource_arn: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.list_tags_response.ListTagsResponse":
        """<p>Lists all tags currently on a named resource. A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track your MemoryDB resources. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html">Tagging your MemoryDB resources</a>.</p> <p>When you add or remove tags from multi region clusters, you might not immediately see the latest effective tags in the ListTags API response due to it being eventually consistent specifically for multi region clusters. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html">Tagging your MemoryDB resources</a>.</p> <p></p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want the list of tags.</p>

        Raises:
            capo_memorydb.errors.acl_not_found_fault.ACLNotFoundFault: <p>The specified ACL does not exist.</p>
            capo_memorydb.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The specified cluster does not exist.</p>
            capo_memorydb.errors.invalid_arn_fault.InvalidARNFault: <p>The specified Amazon Resource Name (ARN) is not valid.</p>
            capo_memorydb.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The cluster is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.multi_region_cluster_not_found_fault.MultiRegionClusterNotFoundFault: <p>The specified multi-Region cluster does not exist.</p>
            capo_memorydb.errors.multi_region_parameter_group_not_found_fault.MultiRegionParameterGroupNotFoundFault: <p>The specified multi-Region parameter group does not exist.</p>
            capo_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The specified snapshot does not exist.</p>
            capo_memorydb.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault: <p>The specified subnet group does not exist.</p>
            capo_memorydb.errors.user_not_found_fault.UserNotFoundFault: <p>The specified user does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.list_tags_request.ListTagsRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.list_tags_response.ListTagsResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.list_tags

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.list_tags.async_list_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.list_tags_request.ListTagsRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def purchase_reserved_nodes_offering(
        self,
        reserved_nodes_offering_id: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        reservation_id: Optional["capo_memorydb.types.string.String"] = None,
        node_count: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        tags: Optional["capo_memorydb.types.tag_list.TagList"] = None,
    ) -> "capo_memorydb.types.purchase_reserved_nodes_offering_response.PurchaseReservedNodesOfferingResponse":
        """<p>Allows you to purchase a reserved node offering. Reserved nodes are not eligible for cancellation and are non-refundable.</p>

        Args:
            reserved_nodes_offering_id: <p>The ID of the reserved node offering to purchase.</p>
            reservation_id: <p>A customer-specified identifier to track this reservation.</p>
            node_count: <p>The number of node instances to reserve.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.reserved_node_already_exists_fault.ReservedNodeAlreadyExistsFault: <p>You already have a reservation with the given identifier.</p>
            capo_memorydb.errors.reserved_node_quota_exceeded_fault.ReservedNodeQuotaExceededFault: <p>The request cannot be processed because it would exceed the user's node quota.</p>
            capo_memorydb.errors.reserved_nodes_offering_not_found_fault.ReservedNodesOfferingNotFoundFault: <p>The requested node offering does not exist. </p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would exceed the maximum number of tags allowed per resource.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.purchase_reserved_nodes_offering_request.PurchaseReservedNodesOfferingRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.purchase_reserved_nodes_offering_response.PurchaseReservedNodesOfferingResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.purchase_reserved_nodes_offering

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.purchase_reserved_nodes_offering.async_purchase_reserved_nodes_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.purchase_reserved_nodes_offering_request.PurchaseReservedNodesOfferingRequest = {
            "reserved_nodes_offering_id": reserved_nodes_offering_id
        }
        if reservation_id is not None:
            input_["reservation_id"] = reservation_id
        if node_count is not None:
            input_["node_count"] = node_count
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_parameter_group(
        self,
        parameter_group_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        all_parameters: Optional["capo_memorydb.types.boolean.Boolean"] = None,
        parameter_names: Optional[
            "capo_memorydb.types.parameter_name_list.ParameterNameList"
        ] = None,
    ) -> (
        "capo_memorydb.types.reset_parameter_group_response.ResetParameterGroupResponse"
    ):
        """<p>Modifies the parameters of a parameter group to the engine or system default value. You can reset specific parameters by submitting a list of parameter names. To reset the entire parameter group, specify the AllParameters and ParameterGroupName parameters.</p>

        Args:
            parameter_group_name: <p>The name of the parameter group to reset.</p>
            all_parameters: <p>If true, all parameters in the parameter group are reset to their default values. If false, only the parameters listed by ParameterNames are reset to their default values.</p>
            parameter_names: <p>An array of parameter names to reset to their default values. If AllParameters is true, do not use ParameterNames. If AllParameters is false, you must specify the name of at least one parameter to reset.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_group_state_fault.InvalidParameterGroupStateFault: <p>The parameter group is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.reset_parameter_group_request.ResetParameterGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.reset_parameter_group_response.ResetParameterGroupResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.reset_parameter_group

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.reset_parameter_group.async_reset_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.reset_parameter_group_request.ResetParameterGroupRequest = {
            "parameter_group_name": parameter_group_name
        }
        if all_parameters is not None:
            input_["all_parameters"] = all_parameters
        if parameter_names is not None:
            input_["parameter_names"] = parameter_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_memorydb.types.string.String",
        tags: "capo_memorydb.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.tag_resource_response.TagResourceResponse":
        """<p> Use this operation to add tags to a resource. A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your MemoryDB resources. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html">Tagging your MemoryDB resources</a>.</p> <p>When you add tags to multi region clusters, you might not immediately see the latest effective tags in the ListTags API response due to it being eventually consistent specifically for multi region clusters. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html">Tagging your MemoryDB resources</a>.</p> <p>You can specify cost-allocation tags for your MemoryDB resources, Amazon generates a cost allocation report as a comma-separated value (CSV) file with your usage and costs aggregated by your tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging.html">Using Cost Allocation Tags</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which the tags are to be added.</p>
            tags: <p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>

        Raises:
            capo_memorydb.errors.acl_not_found_fault.ACLNotFoundFault: <p>The specified ACL does not exist.</p>
            capo_memorydb.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The specified cluster does not exist.</p>
            capo_memorydb.errors.invalid_arn_fault.InvalidARNFault: <p>The specified Amazon Resource Name (ARN) is not valid.</p>
            capo_memorydb.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The cluster is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.multi_region_cluster_not_found_fault.MultiRegionClusterNotFoundFault: <p>The specified multi-Region cluster does not exist.</p>
            capo_memorydb.errors.multi_region_parameter_group_not_found_fault.MultiRegionParameterGroupNotFoundFault: <p>The specified multi-Region parameter group does not exist.</p>
            capo_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The specified snapshot does not exist.</p>
            capo_memorydb.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault: <p>The specified subnet group does not exist.</p>
            capo_memorydb.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>The request cannot be processed because it would exceed the maximum number of tags allowed per resource.</p>
            capo_memorydb.errors.user_not_found_fault.UserNotFoundFault: <p>The specified user does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.tag_resource

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_memorydb.types.string.String",
        tag_keys: "capo_memorydb.types.key_list.KeyList",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.untag_resource_response.UntagResourceResponse":
        """<p>Use this operation to remove tags on a resource. A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your MemoryDB resources. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html">Tagging your MemoryDB resources</a>.</p> <p>When you remove tags from multi region clusters, you might not immediately see the latest effective tags in the ListTags API response due to it being eventually consistent specifically for multi region clusters. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/Tagging-Resources.html">Tagging your MemoryDB resources</a>.</p> <p>You can specify cost-allocation tags for your MemoryDB resources, Amazon generates a cost allocation report as a comma-separated value (CSV) file with your usage and costs aggregated by your tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging.html">Using Cost Allocation Tags</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which the tags are to be removed.</p>
            tag_keys: <p>The list of keys of the tags that are to be removed.</p>

        Raises:
            capo_memorydb.errors.acl_not_found_fault.ACLNotFoundFault: <p>The specified ACL does not exist.</p>
            capo_memorydb.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The specified cluster does not exist.</p>
            capo_memorydb.errors.invalid_arn_fault.InvalidARNFault: <p>The specified Amazon Resource Name (ARN) is not valid.</p>
            capo_memorydb.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The cluster is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.multi_region_cluster_not_found_fault.MultiRegionClusterNotFoundFault: <p>The specified multi-Region cluster does not exist.</p>
            capo_memorydb.errors.multi_region_parameter_group_not_found_fault.MultiRegionParameterGroupNotFoundFault: <p>The specified multi-Region parameter group does not exist.</p>
            capo_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.snapshot_not_found_fault.SnapshotNotFoundFault: <p>The specified snapshot does not exist.</p>
            capo_memorydb.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault: <p>The specified subnet group does not exist.</p>
            capo_memorydb.errors.tag_not_found_fault.TagNotFoundFault: <p>The specified tag does not exist.</p>
            capo_memorydb.errors.user_not_found_fault.UserNotFoundFault: <p>The specified user does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.untag_resource

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_acl(
        self,
        acl_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        user_names_to_add: Optional[
            "capo_memorydb.types.user_name_list_input.UserNameListInput"
        ] = None,
        user_names_to_remove: Optional[
            "capo_memorydb.types.user_name_list_input.UserNameListInput"
        ] = None,
    ) -> "capo_memorydb.types.update_acl_response.UpdateACLResponse":
        """<p>Changes the list of users that belong to the Access Control List.</p>

        Args:
            acl_name: <p>The name of the Access Control List.</p>
            user_names_to_add: <p>The list of users to add to the Access Control List.</p>
            user_names_to_remove: <p>The list of users to remove from the Access Control List.</p>

        Raises:
            capo_memorydb.errors.acl_not_found_fault.ACLNotFoundFault: <p>The specified ACL does not exist.</p>
            capo_memorydb.errors.default_user_required.DefaultUserRequired: <p>A default user is required and must be specified.</p>
            capo_memorydb.errors.duplicate_user_name_fault.DuplicateUserNameFault: <p>A user with the specified name already exists.</p>
            capo_memorydb.errors.invalid_acl_state_fault.InvalidACLStateFault: <p>The ACL is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.user_not_found_fault.UserNotFoundFault: <p>The specified user does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.update_acl_request.UpdateACLRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.update_acl_response.UpdateACLResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.update_acl

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.update_acl.async_update_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.update_acl_request.UpdateACLRequest = {
            "acl_name": acl_name
        }
        if user_names_to_add is not None:
            input_["user_names_to_add"] = user_names_to_add
        if user_names_to_remove is not None:
            input_["user_names_to_remove"] = user_names_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_cluster(
        self,
        cluster_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        description: Optional["capo_memorydb.types.string.String"] = None,
        security_group_ids: Optional[
            "capo_memorydb.types.security_group_ids_list.SecurityGroupIdsList"
        ] = None,
        maintenance_window: Optional["capo_memorydb.types.string.String"] = None,
        sns_topic_arn: Optional["capo_memorydb.types.string.String"] = None,
        sns_topic_status: Optional["capo_memorydb.types.string.String"] = None,
        parameter_group_name: Optional["capo_memorydb.types.string.String"] = None,
        snapshot_window: Optional["capo_memorydb.types.string.String"] = None,
        snapshot_retention_limit: Optional[
            "capo_memorydb.types.integer_optional.IntegerOptional"
        ] = None,
        node_type: Optional["capo_memorydb.types.string.String"] = None,
        engine: Optional["capo_memorydb.types.string.String"] = None,
        engine_version: Optional["capo_memorydb.types.string.String"] = None,
        replica_configuration: Optional[
            "capo_memorydb.types.replica_configuration_request.ReplicaConfigurationRequest"
        ] = None,
        shard_configuration: Optional[
            "capo_memorydb.types.shard_configuration_request.ShardConfigurationRequest"
        ] = None,
        acl_name: Optional["capo_memorydb.types.acl_name.ACLName"] = None,
        ip_discovery: Optional["capo_memorydb.types.ip_discovery.IpDiscovery"] = None,
    ) -> "capo_memorydb.types.update_cluster_response.UpdateClusterResponse":
        """<p>Modifies the settings for a cluster. You can use this operation to change one or more cluster configuration settings by specifying the settings and the new values.</p>

        Args:
            cluster_name: <p>The name of the cluster to update.</p>
            description: <p>The description of the cluster to update.</p>
            security_group_ids: <p>The SecurityGroupIds to update.</p>
            maintenance_window: <p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>
            sns_topic_arn: <p>The SNS topic ARN to update.</p>
            sns_topic_status: <p>The status of the Amazon SNS notification topic. Notifications are sent only if the status is active.</p>
            parameter_group_name: <p>The name of the parameter group to update.</p>
            snapshot_window: <p>The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your cluster.</p>
            snapshot_retention_limit: <p>The number of days for which MemoryDB retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p>
            node_type: <p>A valid node type that you want to scale this cluster up or down to.</p>
            engine: <p>The name of the engine to be used for the cluster.</p>
            engine_version: <p>The upgraded version of the engine to be run on the nodes. You can upgrade to a newer engine version, but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster and create it anew with the earlier engine version.</p>
            replica_configuration: <p>The number of replicas that will reside in each shard.</p>
            shard_configuration: <p>The number of shards in the cluster.</p>
            acl_name: <p>The Access Control List that is associated with the cluster.</p>
            ip_discovery: <p>The mechanism for discovering IP addresses for the cluster discovery protocol. Valid values are 'ipv4' or 'ipv6'. When set to 'ipv4', cluster discovery functions such as cluster slots, cluster shards, and cluster nodes will return IPv4 addresses for cluster nodes. When set to 'ipv6', the cluster discovery functions return IPv6 addresses for cluster nodes. The value must be compatible with the NetworkType parameter. If not specified, the default is 'ipv4'.</p>

        Raises:
            capo_memorydb.errors.acl_not_found_fault.ACLNotFoundFault: <p>The specified ACL does not exist.</p>
            capo_memorydb.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The specified cluster does not exist.</p>
            capo_memorydb.errors.cluster_quota_for_customer_exceeded_fault.ClusterQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the maximum number of clusters allowed for this customer.</p>
            capo_memorydb.errors.invalid_acl_state_fault.InvalidACLStateFault: <p>The ACL is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The cluster is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_kms_key_fault.InvalidKMSKeyFault: <p>The specified KMS key is not valid or accessible.</p>
            capo_memorydb.errors.invalid_node_state_fault.InvalidNodeStateFault: <p>The node is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The VPC network is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.node_quota_for_cluster_exceeded_fault.NodeQuotaForClusterExceededFault: <p>The request cannot be processed because it would exceed the maximum number of nodes allowed for this cluster.</p>
            capo_memorydb.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault: <p>The request cannot be processed because it would exceed the maximum number of nodes allowed for this customer.</p>
            capo_memorydb.errors.no_operation_fault.NoOperationFault: <p>The requested operation would result in no changes.</p>
            capo_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.shards_per_cluster_quota_exceeded_fault.ShardsPerClusterQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of shards allowed per cluster.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.update_cluster_request.UpdateClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.update_cluster

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.update_cluster.async_update_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.update_cluster_request.UpdateClusterRequest = {
            "cluster_name": cluster_name
        }
        if description is not None:
            input_["description"] = description
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if sns_topic_status is not None:
            input_["sns_topic_status"] = sns_topic_status
        if parameter_group_name is not None:
            input_["parameter_group_name"] = parameter_group_name
        if snapshot_window is not None:
            input_["snapshot_window"] = snapshot_window
        if snapshot_retention_limit is not None:
            input_["snapshot_retention_limit"] = snapshot_retention_limit
        if node_type is not None:
            input_["node_type"] = node_type
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if replica_configuration is not None:
            input_["replica_configuration"] = replica_configuration
        if shard_configuration is not None:
            input_["shard_configuration"] = shard_configuration
        if acl_name is not None:
            input_["acl_name"] = acl_name
        if ip_discovery is not None:
            input_["ip_discovery"] = ip_discovery

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_multi_region_cluster(
        self,
        multi_region_cluster_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        node_type: Optional["capo_memorydb.types.string.String"] = None,
        description: Optional["capo_memorydb.types.string.String"] = None,
        engine_version: Optional["capo_memorydb.types.string.String"] = None,
        shard_configuration: Optional[
            "capo_memorydb.types.shard_configuration_request.ShardConfigurationRequest"
        ] = None,
        multi_region_parameter_group_name: Optional[
            "capo_memorydb.types.string.String"
        ] = None,
        update_strategy: Optional[
            "capo_memorydb.types.update_strategy.UpdateStrategy"
        ] = None,
    ) -> "capo_memorydb.types.update_multi_region_cluster_response.UpdateMultiRegionClusterResponse":
        """<p>Updates the configuration of an existing multi-Region cluster.</p>

        Args:
            multi_region_cluster_name: <p>The name of the multi-Region cluster to be updated.</p>
            node_type: <p>The new node type to be used for the multi-Region cluster.</p>
            description: <p>A new description for the multi-Region cluster.</p>
            engine_version: <p>The new engine version to be used for the multi-Region cluster.</p>
            multi_region_parameter_group_name: <p>The new multi-Region parameter group to be associated with the cluster.</p>
            update_strategy: <p>The strategy to use for the update operation. Supported values are "coordinated" or "uncoordinated".</p>

        Raises:
            capo_memorydb.errors.invalid_multi_region_cluster_state_fault.InvalidMultiRegionClusterStateFault: <p>The requested operation cannot be performed on the multi-Region cluster in its current state.</p>
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.multi_region_cluster_not_found_fault.MultiRegionClusterNotFoundFault: <p>The specified multi-Region cluster does not exist.</p>
            capo_memorydb.errors.multi_region_parameter_group_not_found_fault.MultiRegionParameterGroupNotFoundFault: <p>The specified multi-Region parameter group does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.update_multi_region_cluster_request.UpdateMultiRegionClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.update_multi_region_cluster_response.UpdateMultiRegionClusterResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.update_multi_region_cluster

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.update_multi_region_cluster.async_update_multi_region_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.update_multi_region_cluster_request.UpdateMultiRegionClusterRequest = {
            "multi_region_cluster_name": multi_region_cluster_name
        }
        if node_type is not None:
            input_["node_type"] = node_type
        if description is not None:
            input_["description"] = description
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if shard_configuration is not None:
            input_["shard_configuration"] = shard_configuration
        if multi_region_parameter_group_name is not None:
            input_["multi_region_parameter_group_name"] = (
                multi_region_parameter_group_name
            )
        if update_strategy is not None:
            input_["update_strategy"] = update_strategy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_parameter_group(
        self,
        parameter_group_name: "capo_memorydb.types.string.String",
        parameter_name_values: "capo_memorydb.types.parameter_name_value_list.ParameterNameValueList",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
    ) -> "capo_memorydb.types.update_parameter_group_response.UpdateParameterGroupResponse":
        """<p>Updates the parameters of a parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.</p>

        Args:
            parameter_group_name: <p>The name of the parameter group to update.</p>
            parameter_name_values: <p>An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be updated per request.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_group_state_fault.InvalidParameterGroupStateFault: <p>The parameter group is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.update_parameter_group_request.UpdateParameterGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.update_parameter_group_response.UpdateParameterGroupResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.update_parameter_group

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.update_parameter_group.async_update_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.update_parameter_group_request.UpdateParameterGroupRequest = {
            "parameter_group_name": parameter_group_name,
            "parameter_name_values": parameter_name_values,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_subnet_group(
        self,
        subnet_group_name: "capo_memorydb.types.string.String",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        description: Optional["capo_memorydb.types.string.String"] = None,
        subnet_ids: Optional[
            "capo_memorydb.types.subnet_identifier_list.SubnetIdentifierList"
        ] = None,
    ) -> "capo_memorydb.types.update_subnet_group_response.UpdateSubnetGroupResponse":
        """<p>Updates a subnet group. For more information, see <a href="https://docs.aws.amazon.com/MemoryDB/latest/devguide/ubnetGroups.Modifying.html">Updating a subnet group</a> </p>

        Args:
            subnet_group_name: <p>The name of the subnet group</p>
            description: <p>A description of the subnet group</p>
            subnet_ids: <p>The EC2 subnet IDs for the subnet group.</p>

        Raises:
            capo_memorydb.errors.invalid_subnet.InvalidSubnet: <p>The specified subnet is not valid.</p>
            capo_memorydb.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The required service-linked role was not found.</p>
            capo_memorydb.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault: <p>The specified subnet group does not exist.</p>
            capo_memorydb.errors.subnet_in_use.SubnetInUse: <p>The subnet is currently in use and cannot be deleted.</p>
            capo_memorydb.errors.subnet_not_allowed_fault.SubnetNotAllowedFault: <p>The specified subnet is not allowed for this operation.</p>
            capo_memorydb.errors.subnet_quota_exceeded_fault.SubnetQuotaExceededFault: <p>The request cannot be processed because it would exceed the maximum number of subnets allowed.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.update_subnet_group_request.UpdateSubnetGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.update_subnet_group_response.UpdateSubnetGroupResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.update_subnet_group

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.update_subnet_group.async_update_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.update_subnet_group_request.UpdateSubnetGroupRequest = {
            "subnet_group_name": subnet_group_name
        }
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

    async def update_user(
        self,
        user_name: "capo_memorydb.types.user_name.UserName",
        *,
        config_overrides: Optional[AsyncMemoryDBClientConfig] = None,
        authentication_mode: Optional[
            "capo_memorydb.types.authentication_mode.AuthenticationMode"
        ] = None,
        access_string: Optional[
            "capo_memorydb.types.access_string.AccessString"
        ] = None,
    ) -> "capo_memorydb.types.update_user_response.UpdateUserResponse":
        """<p>Changes user password(s) and/or access string.</p>

        Args:
            user_name: <p>The name of the user</p>
            authentication_mode: <p>Denotes the user's authentication properties, such as whether it requires a password to authenticate.</p>
            access_string: <p>Access permissions string used for this user.</p>

        Raises:
            capo_memorydb.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>The specified parameter combination is not valid.</p>
            capo_memorydb.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The specified parameter value is not valid.</p>
            capo_memorydb.errors.invalid_user_state_fault.InvalidUserStateFault: <p>The user is not in a valid state for the requested operation.</p>
            capo_memorydb.errors.user_not_found_fault.UserNotFoundFault: <p>The specified user does not exist.</p>
            capo_memorydb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_memorydb.types.update_user_request.UpdateUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_memorydb.types.update_user_response.UpdateUserResponse"
        ]:
            import capo_memorydb._operations.amazon_memory_db.update_user

            (
                output,
                http_response,
            ) = await capo_memorydb._operations.amazon_memory_db.update_user.async_update_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_memorydb.types.update_user_request.UpdateUserRequest = {
            "user_name": user_name
        }
        if authentication_mode is not None:
            input_["authentication_mode"] = authentication_mode
        if access_string is not None:
            input_["access_string"] = access_string

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
