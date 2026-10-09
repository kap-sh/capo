"""Generated from Smithy shape ``com.amazonaws.neptune#AmazonRDSv19``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_neptune._auth._signers
import capo_neptune._auth._sigv4
from capo_neptune._auth._identity import Credentials
from capo_neptune._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_neptune._auth._zapros_handler import AuthMiddleware
from capo_neptune._pagination import resolve_path as _resolve_path
from capo_neptune._services._aws_config import aaws_config
from capo_neptune._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_neptune.types.add_role_to_db_cluster_message
    import capo_neptune.types.add_source_identifier_to_subscription_message
    import capo_neptune.types.add_source_identifier_to_subscription_result
    import capo_neptune.types.add_tags_to_resource_message
    import capo_neptune.types.apply_pending_maintenance_action_message
    import capo_neptune.types.apply_pending_maintenance_action_result
    import capo_neptune.types.attribute_value_list
    import capo_neptune.types.availability_zones
    import capo_neptune.types.boolean
    import capo_neptune.types.boolean_optional
    import capo_neptune.types.cloudwatch_logs_export_configuration
    import capo_neptune.types.copy_db_cluster_parameter_group_message
    import capo_neptune.types.copy_db_cluster_parameter_group_result
    import capo_neptune.types.copy_db_cluster_snapshot_message
    import capo_neptune.types.copy_db_cluster_snapshot_result
    import capo_neptune.types.copy_db_parameter_group_message
    import capo_neptune.types.copy_db_parameter_group_result
    import capo_neptune.types.create_db_cluster_endpoint_message
    import capo_neptune.types.create_db_cluster_endpoint_output
    import capo_neptune.types.create_db_cluster_message
    import capo_neptune.types.create_db_cluster_parameter_group_message
    import capo_neptune.types.create_db_cluster_parameter_group_result
    import capo_neptune.types.create_db_cluster_result
    import capo_neptune.types.create_db_cluster_snapshot_message
    import capo_neptune.types.create_db_cluster_snapshot_result
    import capo_neptune.types.create_db_instance_message
    import capo_neptune.types.create_db_instance_result
    import capo_neptune.types.create_db_parameter_group_message
    import capo_neptune.types.create_db_parameter_group_result
    import capo_neptune.types.create_db_subnet_group_message
    import capo_neptune.types.create_db_subnet_group_result
    import capo_neptune.types.create_event_subscription_message
    import capo_neptune.types.create_event_subscription_result
    import capo_neptune.types.create_global_cluster_message
    import capo_neptune.types.create_global_cluster_result
    import capo_neptune.types.db_cluster
    import capo_neptune.types.db_cluster_endpoint
    import capo_neptune.types.db_cluster_endpoint_message
    import capo_neptune.types.db_cluster_message
    import capo_neptune.types.db_cluster_parameter_group
    import capo_neptune.types.db_cluster_parameter_group_details
    import capo_neptune.types.db_cluster_parameter_group_name_message
    import capo_neptune.types.db_cluster_parameter_groups_message
    import capo_neptune.types.db_cluster_snapshot
    import capo_neptune.types.db_cluster_snapshot_message
    import capo_neptune.types.db_engine_version
    import capo_neptune.types.db_engine_version_message
    import capo_neptune.types.db_instance
    import capo_neptune.types.db_instance_message
    import capo_neptune.types.db_parameter_group
    import capo_neptune.types.db_parameter_group_details
    import capo_neptune.types.db_parameter_group_name_message
    import capo_neptune.types.db_parameter_groups_message
    import capo_neptune.types.db_security_group_name_list
    import capo_neptune.types.db_subnet_group
    import capo_neptune.types.db_subnet_group_message
    import capo_neptune.types.delete_db_cluster_endpoint_message
    import capo_neptune.types.delete_db_cluster_endpoint_output
    import capo_neptune.types.delete_db_cluster_message
    import capo_neptune.types.delete_db_cluster_parameter_group_message
    import capo_neptune.types.delete_db_cluster_result
    import capo_neptune.types.delete_db_cluster_snapshot_message
    import capo_neptune.types.delete_db_cluster_snapshot_result
    import capo_neptune.types.delete_db_instance_message
    import capo_neptune.types.delete_db_instance_result
    import capo_neptune.types.delete_db_parameter_group_message
    import capo_neptune.types.delete_db_subnet_group_message
    import capo_neptune.types.delete_event_subscription_message
    import capo_neptune.types.delete_event_subscription_result
    import capo_neptune.types.delete_global_cluster_message
    import capo_neptune.types.delete_global_cluster_result
    import capo_neptune.types.describe_db_cluster_endpoints_message
    import capo_neptune.types.describe_db_cluster_parameter_groups_message
    import capo_neptune.types.describe_db_cluster_parameters_message
    import capo_neptune.types.describe_db_cluster_snapshot_attributes_message
    import capo_neptune.types.describe_db_cluster_snapshot_attributes_result
    import capo_neptune.types.describe_db_cluster_snapshots_message
    import capo_neptune.types.describe_db_clusters_message
    import capo_neptune.types.describe_db_engine_versions_message
    import capo_neptune.types.describe_db_instances_message
    import capo_neptune.types.describe_db_parameter_groups_message
    import capo_neptune.types.describe_db_parameters_message
    import capo_neptune.types.describe_db_subnet_groups_message
    import capo_neptune.types.describe_engine_default_cluster_parameters_message
    import capo_neptune.types.describe_engine_default_cluster_parameters_result
    import capo_neptune.types.describe_engine_default_parameters_message
    import capo_neptune.types.describe_engine_default_parameters_result
    import capo_neptune.types.describe_event_categories_message
    import capo_neptune.types.describe_event_subscriptions_message
    import capo_neptune.types.describe_events_message
    import capo_neptune.types.describe_global_clusters_message
    import capo_neptune.types.describe_orderable_db_instance_options_message
    import capo_neptune.types.describe_pending_maintenance_actions_message
    import capo_neptune.types.describe_valid_db_instance_modifications_message
    import capo_neptune.types.describe_valid_db_instance_modifications_result
    import capo_neptune.types.event
    import capo_neptune.types.event_categories_list
    import capo_neptune.types.event_categories_message
    import capo_neptune.types.event_subscription
    import capo_neptune.types.event_subscriptions_message
    import capo_neptune.types.events_message
    import capo_neptune.types.failover_db_cluster_message
    import capo_neptune.types.failover_db_cluster_result
    import capo_neptune.types.failover_global_cluster_message
    import capo_neptune.types.failover_global_cluster_result
    import capo_neptune.types.filter_list
    import capo_neptune.types.global_cluster
    import capo_neptune.types.global_cluster_identifier
    import capo_neptune.types.global_clusters_message
    import capo_neptune.types.integer_optional
    import capo_neptune.types.key_list
    import capo_neptune.types.list_tags_for_resource_message
    import capo_neptune.types.log_type_list
    import capo_neptune.types.modify_db_cluster_endpoint_message
    import capo_neptune.types.modify_db_cluster_endpoint_output
    import capo_neptune.types.modify_db_cluster_message
    import capo_neptune.types.modify_db_cluster_parameter_group_message
    import capo_neptune.types.modify_db_cluster_result
    import capo_neptune.types.modify_db_cluster_snapshot_attribute_message
    import capo_neptune.types.modify_db_cluster_snapshot_attribute_result
    import capo_neptune.types.modify_db_instance_message
    import capo_neptune.types.modify_db_instance_result
    import capo_neptune.types.modify_db_parameter_group_message
    import capo_neptune.types.modify_db_subnet_group_message
    import capo_neptune.types.modify_db_subnet_group_result
    import capo_neptune.types.modify_event_subscription_message
    import capo_neptune.types.modify_event_subscription_result
    import capo_neptune.types.modify_global_cluster_message
    import capo_neptune.types.modify_global_cluster_result
    import capo_neptune.types.orderable_db_instance_option
    import capo_neptune.types.orderable_db_instance_options_message
    import capo_neptune.types.parameter
    import capo_neptune.types.parameters_list
    import capo_neptune.types.pending_maintenance_actions_message
    import capo_neptune.types.promote_read_replica_db_cluster_message
    import capo_neptune.types.promote_read_replica_db_cluster_result
    import capo_neptune.types.reboot_db_instance_message
    import capo_neptune.types.reboot_db_instance_result
    import capo_neptune.types.remove_from_global_cluster_message
    import capo_neptune.types.remove_from_global_cluster_result
    import capo_neptune.types.remove_role_from_db_cluster_message
    import capo_neptune.types.remove_source_identifier_from_subscription_message
    import capo_neptune.types.remove_source_identifier_from_subscription_result
    import capo_neptune.types.remove_tags_from_resource_message
    import capo_neptune.types.reset_db_cluster_parameter_group_message
    import capo_neptune.types.reset_db_parameter_group_message
    import capo_neptune.types.resource_pending_maintenance_actions
    import capo_neptune.types.restore_db_cluster_from_snapshot_message
    import capo_neptune.types.restore_db_cluster_from_snapshot_result
    import capo_neptune.types.restore_db_cluster_to_point_in_time_message
    import capo_neptune.types.restore_db_cluster_to_point_in_time_result
    import capo_neptune.types.sensitive_string
    import capo_neptune.types.serverless_v2_scaling_configuration
    import capo_neptune.types.source_ids_list
    import capo_neptune.types.source_type
    import capo_neptune.types.start_db_cluster_message
    import capo_neptune.types.start_db_cluster_result
    import capo_neptune.types.stop_db_cluster_message
    import capo_neptune.types.stop_db_cluster_result
    import capo_neptune.types.string
    import capo_neptune.types.string_list
    import capo_neptune.types.subnet_identifier_list
    import capo_neptune.types.switchover_global_cluster_message
    import capo_neptune.types.switchover_global_cluster_result
    import capo_neptune.types.t_stamp
    import capo_neptune.types.tag_list
    import capo_neptune.types.tag_list_message
    import capo_neptune.types.vpc_security_group_id_list


class AsyncNeptuneClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncNeptuneClient:
    """A client for the ``Neptune`` service.

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
        self._config = AsyncNeptuneClientConfig(
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
        self, config_overrides: Optional[AsyncNeptuneClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncNeptuneClientConfig = config_overrides or {}
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

    async def add_role_to_db_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        role_arn: Optional["capo_neptune.types.string.String"] = None,
        feature_name: Optional["capo_neptune.types.string.String"] = None,
    ) -> None:
        """<p>Associates an Identity and Access Management (IAM) role with an Neptune DB cluster.</p>

        Args:
            db_cluster_identifier: <p>The name of the DB cluster to associate the IAM role with.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to associate with the Neptune DB cluster, for example <code>arn:aws:iam::123456789012:role/NeptuneAccessRole</code>.</p>
            feature_name: <p>The name of the feature for the Neptune DB cluster that the IAM role is to be associated with. For the list of supported feature names, see <a>DBEngineVersion</a>.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_cluster_role_already_exists_fault.DBClusterRoleAlreadyExistsFault: <p>The specified IAM role Amazon Resource Name (ARN) is already associated with the specified DB cluster.</p>
            capo_neptune.errors.db_cluster_role_quota_exceeded_fault.DBClusterRoleQuotaExceededFault: <p>You have exceeded the maximum number of IAM roles that can be associated with the specified DB cluster.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.add_role_to_db_cluster_message.AddRoleToDBClusterMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_neptune._operations.amazon_rd_sv19.add_role_to_db_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.add_role_to_db_cluster.async_add_role_to_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.add_role_to_db_cluster_message.AddRoleToDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if feature_name is not None:
            input_["feature_name"] = feature_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_source_identifier_to_subscription(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        subscription_name: Optional["capo_neptune.types.string.String"] = None,
        source_identifier: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.add_source_identifier_to_subscription_result.AddSourceIdentifierToSubscriptionResult":
        """<p>Adds a source identifier to an existing event notification subscription.</p>

        Args:
            subscription_name: <p>The name of the event notification subscription you want to add a source identifier to.</p>
            source_identifier: <p>The identifier of the event source to be added.</p> <p>Constraints:</p> <ul> <li> <p>If the source type is a DB instance, then a <code>DBInstanceIdentifier</code> must be supplied.</p> </li> <li> <p>If the source type is a DB security group, a <code>DBSecurityGroupName</code> must be supplied.</p> </li> <li> <p>If the source type is a DB parameter group, a <code>DBParameterGroupName</code> must be supplied.</p> </li> <li> <p>If the source type is a DB snapshot, a <code>DBSnapshotIdentifier</code> must be supplied.</p> </li> </ul>

        Raises:
            capo_neptune.errors.source_not_found_fault.SourceNotFoundFault: <p>The source could not be found.</p>
            capo_neptune.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>The designated subscription could not be found.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.add_source_identifier_to_subscription_message.AddSourceIdentifierToSubscriptionMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.add_source_identifier_to_subscription_result.AddSourceIdentifierToSubscriptionResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.add_source_identifier_to_subscription

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.add_source_identifier_to_subscription.async_add_source_identifier_to_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.add_source_identifier_to_subscription_message.AddSourceIdentifierToSubscriptionMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if source_identifier is not None:
            input_["source_identifier"] = source_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_tags_to_resource(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        resource_name: Optional["capo_neptune.types.string.String"] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
    ) -> None:
        """<p>Adds metadata tags to an Amazon Neptune resource. These tags can also be used with cost allocation reporting to track cost associated with Amazon Neptune resources, or used in a Condition statement in an IAM policy for Amazon Neptune.</p>

        Args:
            resource_name: <p>The Amazon Neptune resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href="https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing"> Constructing an Amazon Resource Name (ARN)</a>.</p>
            tags: <p>The tags to be assigned to the Amazon Neptune resource.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <i>DBInstanceIdentifier</i> does not refer to an existing DB instance.</p>
            capo_neptune.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault: <p> <i>DBSnapshotIdentifier</i> does not refer to an existing DB snapshot.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.add_tags_to_resource_message.AddTagsToResourceMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_neptune._operations.amazon_rd_sv19.add_tags_to_resource

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.add_tags_to_resource.async_add_tags_to_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.add_tags_to_resource_message.AddTagsToResourceMessage = {}
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

    async def apply_pending_maintenance_action(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        resource_identifier: Optional["capo_neptune.types.string.String"] = None,
        apply_action: Optional["capo_neptune.types.string.String"] = None,
        opt_in_type: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.apply_pending_maintenance_action_result.ApplyPendingMaintenanceActionResult":
        """<p>Applies a pending maintenance action to a resource (for example, to a DB instance).</p>

        Args:
            resource_identifier: <p>The Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to. For information about creating an ARN, see <a href="https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing"> Constructing an Amazon Resource Name (ARN)</a>.</p>
            apply_action: <p>The pending maintenance action to apply to this resource.</p> <p>Valid values: <code>system-update</code>, <code>db-upgrade</code> </p>
            opt_in_type: <p>A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type <code>immediate</code> can't be undone.</p> <p>Valid values:</p> <ul> <li> <p> <code>immediate</code> - Apply the maintenance action immediately.</p> </li> <li> <p> <code>next-maintenance</code> - Apply the maintenance action during the next maintenance window for the resource.</p> </li> <li> <p> <code>undo-opt-in</code> - Cancel any existing <code>next-maintenance</code> opt-in requests.</p> </li> </ul>

        Raises:
            capo_neptune.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The specified resource ID was not found.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.apply_pending_maintenance_action_message.ApplyPendingMaintenanceActionMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.apply_pending_maintenance_action_result.ApplyPendingMaintenanceActionResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.apply_pending_maintenance_action

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.apply_pending_maintenance_action.async_apply_pending_maintenance_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.apply_pending_maintenance_action_message.ApplyPendingMaintenanceActionMessage = {}
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if apply_action is not None:
            input_["apply_action"] = apply_action
        if opt_in_type is not None:
            input_["opt_in_type"] = opt_in_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def copy_db_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        source_db_cluster_parameter_group_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        target_db_cluster_parameter_group_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        target_db_cluster_parameter_group_description: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
    ) -> "capo_neptune.types.copy_db_cluster_parameter_group_result.CopyDBClusterParameterGroupResult":
        """<p>Copies the specified DB cluster parameter group.</p>

        Args:
            source_db_cluster_parameter_group_identifier: <p>The identifier or Amazon Resource Name (ARN) for the source DB cluster parameter group. For information about creating an ARN, see <a href="https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing"> Constructing an Amazon Resource Name (ARN)</a>.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid DB cluster parameter group.</p> </li> <li> <p>Must specify a valid DB cluster parameter group identifier, for example <code>my-db-cluster-param-group</code>, or a valid ARN.</p> </li> <li> <p>The source DB cluster parameter group must be in the same Amazon Region as the copy. Neptune does not support cross-Region copying of parameter groups.</p> </li> </ul>
            target_db_cluster_parameter_group_identifier: <p>The identifier for the copied DB cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Cannot be null, empty, or blank</p> </li> <li> <p>Must contain from 1 to 255 letters, numbers, or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-cluster-param-group1</code> </p>
            target_db_cluster_parameter_group_description: <p>A description for the copied DB cluster parameter group.</p>
            tags: <p>The tags to be assigned to the copied DB cluster parameter group.</p>

        Raises:
            capo_neptune.errors.db_parameter_group_already_exists_fault.DBParameterGroupAlreadyExistsFault: <p>A DB parameter group with the same name exists.</p>
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.db_parameter_group_quota_exceeded_fault.DBParameterGroupQuotaExceededFault: <p>Request would result in user exceeding the allowed number of DB parameter groups.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.copy_db_cluster_parameter_group_message.CopyDBClusterParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.copy_db_cluster_parameter_group_result.CopyDBClusterParameterGroupResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.copy_db_cluster_parameter_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.copy_db_cluster_parameter_group.async_copy_db_cluster_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.copy_db_cluster_parameter_group_message.CopyDBClusterParameterGroupMessage = {}
        if source_db_cluster_parameter_group_identifier is not None:
            input_["source_db_cluster_parameter_group_identifier"] = (
                source_db_cluster_parameter_group_identifier
            )
        if target_db_cluster_parameter_group_identifier is not None:
            input_["target_db_cluster_parameter_group_identifier"] = (
                target_db_cluster_parameter_group_identifier
            )
        if target_db_cluster_parameter_group_description is not None:
            input_["target_db_cluster_parameter_group_description"] = (
                target_db_cluster_parameter_group_description
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

    async def copy_db_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        source_db_cluster_snapshot_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        target_db_cluster_snapshot_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        kms_key_id: Optional["capo_neptune.types.string.String"] = None,
        pre_signed_url: Optional["capo_neptune.types.string.String"] = None,
        copy_tags: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
    ) -> (
        "capo_neptune.types.copy_db_cluster_snapshot_result.CopyDBClusterSnapshotResult"
    ):
        """<p>Copies a snapshot of a DB cluster.</p> <p>To copy a DB cluster snapshot from a shared manual DB cluster snapshot, <code>SourceDBClusterSnapshotIdentifier</code> must be the Amazon Resource Name (ARN) of the shared DB cluster snapshot.</p>

        Args:
            source_db_cluster_snapshot_identifier: <p>The identifier of the DB cluster snapshot to copy. This parameter is not case-sensitive. If the source DB cluster snapshot is in a different region or owned by another account, specify the snapshot ARN.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid system snapshot in the "available" state.</p> </li> <li> <p>Specify a valid DB snapshot identifier.</p> </li> </ul> <p>Example: <code>my-cluster-snapshot1</code> </p>
            target_db_cluster_snapshot_identifier: <p>The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter is not case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster-snapshot2</code> </p>
            kms_key_id: <p>The Amazon KMS key ID for an encrypted DB cluster snapshot. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.</p> <p>If you copy an encrypted DB cluster snapshot from your Amazon account, you can specify a value for <code>KmsKeyId</code> to encrypt the copy with a new KMS encryption key. If you don't specify a value for <code>KmsKeyId</code>, then the copy of the DB cluster snapshot is encrypted with the same KMS key as the source DB cluster snapshot.</p> <p>If you copy an encrypted DB cluster snapshot that is shared from another Amazon account, then you must specify a value for <code>KmsKeyId</code>.</p> <p> KMS encryption keys are specific to the Amazon Region that they are created in, and you can't use encryption keys from one Amazon Region in another Amazon Region.</p> <p>You cannot encrypt an unencrypted DB cluster snapshot when you copy it. If you try to copy an unencrypted DB cluster snapshot and specify a value for the KmsKeyId parameter, an error is returned.</p>
            pre_signed_url: <p>Not currently supported.</p>
            copy_tags: <p>True to copy all tags from the source DB cluster snapshot to the target DB cluster snapshot, and otherwise false. The default is false.</p>
            tags: <p>The tags to assign to the new DB cluster snapshot copy.</p>

        Raises:
            capo_neptune.errors.db_cluster_snapshot_already_exists_fault.DBClusterSnapshotAlreadyExistsFault: <p>User already has a DB cluster snapshot with the given identifier.</p>
            capo_neptune.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <i>DBClusterSnapshotIdentifier</i> does not refer to an existing DB cluster snapshot.</p>
            capo_neptune.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The supplied value is not a valid DB cluster snapshot state.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>Error accessing KMS key.</p>
            capo_neptune.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>Request would result in user exceeding the allowed number of DB snapshots.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.copy_db_cluster_snapshot_message.CopyDBClusterSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.copy_db_cluster_snapshot_result.CopyDBClusterSnapshotResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.copy_db_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.copy_db_cluster_snapshot.async_copy_db_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.copy_db_cluster_snapshot_message.CopyDBClusterSnapshotMessage = {}
        if source_db_cluster_snapshot_identifier is not None:
            input_["source_db_cluster_snapshot_identifier"] = (
                source_db_cluster_snapshot_identifier
            )
        if target_db_cluster_snapshot_identifier is not None:
            input_["target_db_cluster_snapshot_identifier"] = (
                target_db_cluster_snapshot_identifier
            )
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if pre_signed_url is not None:
            input_["pre_signed_url"] = pre_signed_url
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def copy_db_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        source_db_parameter_group_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        target_db_parameter_group_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        target_db_parameter_group_description: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
    ) -> "capo_neptune.types.copy_db_parameter_group_result.CopyDBParameterGroupResult":
        """<p>Copies the specified DB parameter group.</p>

        Args:
            source_db_parameter_group_identifier: <p>The identifier or ARN for the source DB parameter group. For information about creating an ARN, see <a href="https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing"> Constructing an Amazon Resource Name (ARN)</a>.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid DB parameter group.</p> </li> <li> <p>Must specify a valid DB parameter group identifier, for example <code>my-db-param-group</code>, or a valid ARN.</p> </li> <li> <p>The source DB parameter group must be in the same Amazon Region as the copy. Neptune does not support cross-Region copying of parameter groups.</p> </li> </ul>
            target_db_parameter_group_identifier: <p>The identifier for the copied DB parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Cannot be null, empty, or blank.</p> </li> <li> <p>Must contain from 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-db-parameter-group</code> </p>
            target_db_parameter_group_description: <p>A description for the copied DB parameter group.</p>
            tags: <p>The tags to be assigned to the copied DB parameter group.</p>

        Raises:
            capo_neptune.errors.db_parameter_group_already_exists_fault.DBParameterGroupAlreadyExistsFault: <p>A DB parameter group with the same name exists.</p>
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.db_parameter_group_quota_exceeded_fault.DBParameterGroupQuotaExceededFault: <p>Request would result in user exceeding the allowed number of DB parameter groups.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.copy_db_parameter_group_message.CopyDBParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.copy_db_parameter_group_result.CopyDBParameterGroupResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.copy_db_parameter_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.copy_db_parameter_group.async_copy_db_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.copy_db_parameter_group_message.CopyDBParameterGroupMessage = {}
        if source_db_parameter_group_identifier is not None:
            input_["source_db_parameter_group_identifier"] = (
                source_db_parameter_group_identifier
            )
        if target_db_parameter_group_identifier is not None:
            input_["target_db_parameter_group_identifier"] = (
                target_db_parameter_group_identifier
            )
        if target_db_parameter_group_description is not None:
            input_["target_db_parameter_group_description"] = (
                target_db_parameter_group_description
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

    async def create_db_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        availability_zones: Optional[
            "capo_neptune.types.availability_zones.AvailabilityZones"
        ] = None,
        backup_retention_period: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        character_set_name: Optional["capo_neptune.types.string.String"] = None,
        copy_tags_to_snapshot: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        database_name: Optional["capo_neptune.types.string.String"] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_neptune.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        db_subnet_group_name: Optional["capo_neptune.types.string.String"] = None,
        engine: Optional["capo_neptune.types.string.String"] = None,
        engine_version: Optional["capo_neptune.types.string.String"] = None,
        port: Optional["capo_neptune.types.integer_optional.IntegerOptional"] = None,
        master_username: Optional["capo_neptune.types.string.String"] = None,
        master_user_password: Optional["capo_neptune.types.string.String"] = None,
        option_group_name: Optional["capo_neptune.types.string.String"] = None,
        preferred_backup_window: Optional["capo_neptune.types.string.String"] = None,
        preferred_maintenance_window: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        replication_source_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
        storage_encrypted: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        kms_key_id: Optional["capo_neptune.types.string.String"] = None,
        pre_signed_url: Optional["capo_neptune.types.string.String"] = None,
        enable_iam_database_authentication: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        enable_cloudwatch_logs_exports: Optional[
            "capo_neptune.types.log_type_list.LogTypeList"
        ] = None,
        deletion_protection: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        serverless_v2_scaling_configuration: Optional[
            "capo_neptune.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
        ] = None,
        global_cluster_identifier: Optional[
            "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        storage_type: Optional["capo_neptune.types.string.String"] = None,
        network_type: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.create_db_cluster_result.CreateDBClusterResult":
        """<p>Creates a new Amazon Neptune DB cluster.</p> <p>You can use the <code>ReplicationSourceIdentifier</code> parameter to create the DB cluster as a Read Replica of another DB cluster or Amazon Neptune DB instance.</p> <p>Note that when you create a new cluster using <code>CreateDBCluster</code> directly, deletion protection is disabled by default (when you create a new production cluster in the console, deletion protection is enabled by default). You can only delete a DB cluster if its <code>DeletionProtection</code> field is set to <code>false</code>.</p>

        Args:
            availability_zones: <p>A list of EC2 Availability Zones that instances in the DB cluster can be created in.</p>
            backup_retention_period: <p>The number of days for which automated backups are retained. You must specify a minimum value of 1.</p> <p>Default: 1</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 1 to 35</p> </li> </ul>
            character_set_name: <p> <i>(Not supported by Neptune)</i> </p>
            copy_tags_to_snapshot: <p> <i>If set to <code>true</code>, tags are copied to any snapshot of the DB cluster that is created.</i> </p>
            database_name: <p>Not supported by Neptune.</p>
            db_cluster_identifier: <p>The DB cluster identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster1</code> </p>
            db_cluster_parameter_group_name: <p> The name of the DB cluster parameter group to associate with this DB cluster. If this argument is omitted, the default is used.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBClusterParameterGroup.</p> </li> </ul>
            vpc_security_group_ids: <p>A list of EC2 VPC security groups to associate with this DB cluster.</p>
            db_subnet_group_name: <p>A DB subnet group to associate with this DB cluster.</p> <p>Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>
            engine: <p>The name of the database engine to be used for this DB cluster.</p> <p>Valid Values: <code>neptune</code> </p>
            engine_version: <p>The version number of the database engine to use for the new DB cluster.</p> <p>Example: <code>1.2.1.0</code> </p>
            port: <p>The port number on which the instances in the DB cluster accept connections.</p> <p> Default: <code>8182</code> </p>
            master_username: <p>Not supported by Neptune.</p>
            master_user_password: <p>Not supported by Neptune.</p>
            option_group_name: <p> <i>(Not supported by Neptune)</i> </p>
            preferred_backup_window: <p>The daily time range during which automated backups are created if automated backups are enabled using the <code>BackupRetentionPeriod</code> parameter.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region. To see the time blocks available, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-maintaining.html#manage-console-maintaining-window">Neptune Maintenance Window</a> in the <i>Amazon Neptune User Guide.</i> </p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>
            preferred_maintenance_window: <p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p>Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region, occurring on a random day of the week. To see the time blocks available, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-maintaining.html#manage-console-maintaining-window">Neptune Maintenance Window</a> in the <i>Amazon Neptune User Guide.</i> </p> <p>Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.</p> <p>Constraints: Minimum 30-minute window.</p>
            replication_source_identifier: <p>The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.</p>
            tags: <p>The tags to assign to the new DB cluster.</p>
            storage_encrypted: <p>Specifies whether the DB cluster is encrypted.</p>
            kms_key_id: <p>The Amazon KMS key identifier for an encrypted DB cluster.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB cluster with the same Amazon account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.</p> <p>If an encryption key is not specified in <code>KmsKeyId</code>:</p> <ul> <li> <p>If <code>ReplicationSourceIdentifier</code> identifies an encrypted source, then Amazon Neptune will use the encryption key used to encrypt the source. Otherwise, Amazon Neptune will use your default encryption key.</p> </li> <li> <p>If the <code>StorageEncrypted</code> parameter is true and <code>ReplicationSourceIdentifier</code> is not specified, then Amazon Neptune will use your default encryption key.</p> </li> </ul> <p>Amazon KMS creates the default encryption key for your Amazon account. Your Amazon account has a different default encryption key for each Amazon Region.</p> <p>If you create a Read Replica of an encrypted DB cluster in another Amazon Region, you must set <code>KmsKeyId</code> to a KMS key ID that is valid in the destination Amazon Region. This key is used to encrypt the Read Replica in that Amazon Region.</p>
            pre_signed_url: <p>This parameter is not currently supported.</p>
            enable_iam_database_authentication: <p>If set to <code>true</code>, enables Amazon Identity and Access Management (IAM) authentication for the entire DB cluster (this cannot be set at an instance level).</p> <p>Default: <code>false</code>.</p>
            enable_cloudwatch_logs_exports: <p>A list of the log types that this DB cluster should export to CloudWatch Logs. Valid log types are: <code>audit</code> (to publish audit logs) and <code>slowquery</code> (to publish slow-query logs). See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html">Publishing Neptune logs to Amazon CloudWatch logs</a>.</p>
            deletion_protection: <p>A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is enabled.</p>
            serverless_v2_scaling_configuration: <p>Contains the scaling configuration of a Neptune Serverless DB cluster.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html">Using Amazon Neptune Serverless</a> in the <i>Amazon Neptune User Guide</i>.</p>
            global_cluster_identifier: <p>The ID of the Neptune global database to which this new DB cluster should be added.</p>
            storage_type: <p>The storage type for the new DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <b> <code>standard</code> </b> – ( <i>the default</i> ) Configures cost-effective database storage for applications with moderate to small I/O usage. When set to <code>standard</code>, the storage type is not returned in the response.</p> </li> <li> <p> <b> <code>iopt1</code> </b> – Enables <a href="https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage">I/O-Optimized storage</a> that's designed to meet the needs of I/O-intensive graph workloads that require predictable pricing with low I/O latency and consistent I/O throughput.</p> <p>Neptune I/O-Optimized storage is only available starting with engine release 1.3.0.0.</p> </li> </ul>
            network_type: <p>The network type of the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <b> <code>IPV4</code> </b> – ( <i>the default</i> ) The DB cluster uses only IPv4 addresses for communication.</p> </li> <li> <p> <b> <code>DUAL</code> </b> – The DB cluster uses both IPv4 and IPv6 addresses for communication. The DB subnet group associated with the cluster must support IPv6.</p> </li> </ul>

        Raises:
            capo_neptune.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault: <p>User already has a DB cluster with the given identifier.</p>
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_cluster_parameter_group_not_found_fault.DBClusterParameterGroupNotFoundFault: <p> <i>DBClusterParameterGroupName</i> does not refer to an existing DB Cluster parameter group.</p>
            capo_neptune.errors.db_cluster_quota_exceeded_fault.DBClusterQuotaExceededFault: <p>User attempted to create a new DB cluster and the user has already reached the maximum allowed DB cluster quota.</p>
            capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <i>DBInstanceIdentifier</i> does not refer to an existing DB instance.</p>
            capo_neptune.errors.db_subnet_group_does_not_cover_enough_a_zs.DBSubnetGroupDoesNotCoverEnoughAZs: <p>Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.</p>
            capo_neptune.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <i>DBSubnetGroupName</i> does not refer to an existing DB subnet group.</p>
            capo_neptune.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global database cluster. </p>
            capo_neptune.errors.insufficient_storage_cluster_capacity_fault.InsufficientStorageClusterCapacityFault: <p>There is insufficient storage available for the current action. You may be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.invalid_db_subnet_group_state_fault.InvalidDBSubnetGroupStateFault: <p>The DB subnet group cannot be deleted because it is in use.</p>
            capo_neptune.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The global cluster is in an invalid state and can't perform the requested operation. </p>
            capo_neptune.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.</p>
            capo_neptune.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>DB subnet group does not cover all Availability Zones after it is created because users' change.</p>
            capo_neptune.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>Error accessing KMS key.</p>
            capo_neptune.errors.network_type_not_supported_fault.NetworkTypeNotSupportedFault: <p>The specified <i>NetworkType</i> is not supported for the DB cluster, DB subnet group, or orderable DB instance option.</p>
            capo_neptune.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>Request would result in user exceeding the allowed amount of storage available across all DB instances.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.create_db_cluster_message.CreateDBClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.create_db_cluster_result.CreateDBClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.create_db_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.create_db_cluster.async_create_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.create_db_cluster_message.CreateDBClusterMessage = {}
        if availability_zones is not None:
            input_["availability_zones"] = availability_zones
        if backup_retention_period is not None:
            input_["backup_retention_period"] = backup_retention_period
        if character_set_name is not None:
            input_["character_set_name"] = character_set_name
        if copy_tags_to_snapshot is not None:
            input_["copy_tags_to_snapshot"] = copy_tags_to_snapshot
        if database_name is not None:
            input_["database_name"] = database_name
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if port is not None:
            input_["port"] = port
        if master_username is not None:
            input_["master_username"] = master_username
        if master_user_password is not None:
            input_["master_user_password"] = master_user_password
        if option_group_name is not None:
            input_["option_group_name"] = option_group_name
        if preferred_backup_window is not None:
            input_["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if replication_source_identifier is not None:
            input_["replication_source_identifier"] = replication_source_identifier
        if tags is not None:
            input_["tags"] = tags
        if storage_encrypted is not None:
            input_["storage_encrypted"] = storage_encrypted
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if pre_signed_url is not None:
            input_["pre_signed_url"] = pre_signed_url
        if enable_iam_database_authentication is not None:
            input_["enable_iam_database_authentication"] = (
                enable_iam_database_authentication
            )
        if enable_cloudwatch_logs_exports is not None:
            input_["enable_cloudwatch_logs_exports"] = enable_cloudwatch_logs_exports
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if serverless_v2_scaling_configuration is not None:
            input_["serverless_v2_scaling_configuration"] = (
                serverless_v2_scaling_configuration
            )
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if network_type is not None:
            input_["network_type"] = network_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_db_cluster_endpoint(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        db_cluster_endpoint_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        endpoint_type: Optional["capo_neptune.types.string.String"] = None,
        static_members: Optional["capo_neptune.types.string_list.StringList"] = None,
        excluded_members: Optional["capo_neptune.types.string_list.StringList"] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
    ) -> "capo_neptune.types.create_db_cluster_endpoint_output.CreateDBClusterEndpointOutput":
        """<p>Creates a new custom endpoint and associates it with an Amazon Neptune DB cluster.</p>

        Args:
            db_cluster_identifier: <p>The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.</p>
            db_cluster_endpoint_identifier: <p>The identifier to use for the new endpoint. This parameter is stored as a lowercase string.</p>
            endpoint_type: <p>The type of the endpoint. One of: <code>READER</code>, <code>WRITER</code>, <code>ANY</code>.</p>
            static_members: <p>List of DB instance identifiers that are part of the custom endpoint group.</p>
            excluded_members: <p>List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.</p>
            tags: <p>The tags to be assigned to the Amazon Neptune resource.</p>

        Raises:
            capo_neptune.errors.db_cluster_endpoint_already_exists_fault.DBClusterEndpointAlreadyExistsFault: <p>The specified custom endpoint cannot be created because it already exists.</p>
            capo_neptune.errors.db_cluster_endpoint_quota_exceeded_fault.DBClusterEndpointQuotaExceededFault: <p>The cluster already has the maximum number of custom endpoints.</p>
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <i>DBInstanceIdentifier</i> does not refer to an existing DB instance.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.create_db_cluster_endpoint_message.CreateDBClusterEndpointMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.create_db_cluster_endpoint_output.CreateDBClusterEndpointOutput"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.create_db_cluster_endpoint

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.create_db_cluster_endpoint.async_create_db_cluster_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.create_db_cluster_endpoint_message.CreateDBClusterEndpointMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if db_cluster_endpoint_identifier is not None:
            input_["db_cluster_endpoint_identifier"] = db_cluster_endpoint_identifier
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
        if static_members is not None:
            input_["static_members"] = static_members
        if excluded_members is not None:
            input_["excluded_members"] = excluded_members
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_db_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        db_parameter_group_family: Optional["capo_neptune.types.string.String"] = None,
        description: Optional["capo_neptune.types.string.String"] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
    ) -> "capo_neptune.types.create_db_cluster_parameter_group_result.CreateDBClusterParameterGroupResult":
        """<p>Creates a new DB cluster parameter group.</p> <p>Parameters in a DB cluster parameter group apply to all of the instances in a DB cluster.</p> <p> A DB cluster parameter group is initially created with the default parameters for the database engine used by instances in the DB cluster. To provide custom values for any of the parameters, you must modify the group after creating it using <a>ModifyDBClusterParameterGroup</a>. Once you've created a DB cluster parameter group, you need to associate it with your DB cluster using <a>ModifyDBCluster</a>. When you associate a new DB cluster parameter group with a running DB cluster, you need to reboot the DB instances in the DB cluster without failover for the new DB cluster parameter group and associated settings to take effect.</p> <important> <p>After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the DB cluster parameter group is used as the default for a new DB cluster. This is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the <code>character_set_database</code> parameter. You can use the <i>Parameter Groups</i> option of the <a href="https://console.aws.amazon.com/rds/">Amazon Neptune console</a> or the <a>DescribeDBClusterParameters</a> command to verify that your DB cluster parameter group has been created or modified.</p> </important>

        Args:
            db_cluster_parameter_group_name: <p>The name of the DB cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must match the name of an existing DBClusterParameterGroup.</p> </li> </ul> <note> <p>This value is stored as a lowercase string.</p> </note>
            db_parameter_group_family: <p>The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.</p>
            description: <p>The description for the DB cluster parameter group.</p>
            tags: <p>The tags to be assigned to the new DB cluster parameter group.</p>

        Raises:
            capo_neptune.errors.db_parameter_group_already_exists_fault.DBParameterGroupAlreadyExistsFault: <p>A DB parameter group with the same name exists.</p>
            capo_neptune.errors.db_parameter_group_quota_exceeded_fault.DBParameterGroupQuotaExceededFault: <p>Request would result in user exceeding the allowed number of DB parameter groups.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.create_db_cluster_parameter_group_message.CreateDBClusterParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.create_db_cluster_parameter_group_result.CreateDBClusterParameterGroupResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.create_db_cluster_parameter_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.create_db_cluster_parameter_group.async_create_db_cluster_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.create_db_cluster_parameter_group_message.CreateDBClusterParameterGroupMessage = {}
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if db_parameter_group_family is not None:
            input_["db_parameter_group_family"] = db_parameter_group_family
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

    async def create_db_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
    ) -> "capo_neptune.types.create_db_cluster_snapshot_result.CreateDBClusterSnapshotResult":
        """<p>Creates a snapshot of a DB cluster.</p>

        Args:
            db_cluster_snapshot_identifier: <p>The identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster1-snapshot1</code> </p>
            db_cluster_identifier: <p>The identifier of the DB cluster to create a snapshot for. This parameter is not case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBCluster.</p> </li> </ul> <p>Example: <code>my-cluster1</code> </p>
            tags: <p>The tags to be assigned to the DB cluster snapshot.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_cluster_snapshot_already_exists_fault.DBClusterSnapshotAlreadyExistsFault: <p>User already has a DB cluster snapshot with the given identifier.</p>
            capo_neptune.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The supplied value is not a valid DB cluster snapshot state.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>Request would result in user exceeding the allowed number of DB snapshots.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.create_db_cluster_snapshot_message.CreateDBClusterSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.create_db_cluster_snapshot_result.CreateDBClusterSnapshotResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.create_db_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.create_db_cluster_snapshot.async_create_db_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.create_db_cluster_snapshot_message.CreateDBClusterSnapshotMessage = {}
        if db_cluster_snapshot_identifier is not None:
            input_["db_cluster_snapshot_identifier"] = db_cluster_snapshot_identifier
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_db_instance(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_name: Optional["capo_neptune.types.string.String"] = None,
        db_instance_identifier: Optional["capo_neptune.types.string.String"] = None,
        allocated_storage: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        db_instance_class: Optional["capo_neptune.types.string.String"] = None,
        engine: Optional["capo_neptune.types.string.String"] = None,
        master_username: Optional["capo_neptune.types.string.String"] = None,
        master_user_password: Optional["capo_neptune.types.string.String"] = None,
        db_security_groups: Optional[
            "capo_neptune.types.db_security_group_name_list.DBSecurityGroupNameList"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_neptune.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        availability_zone: Optional["capo_neptune.types.string.String"] = None,
        db_subnet_group_name: Optional["capo_neptune.types.string.String"] = None,
        preferred_maintenance_window: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        db_parameter_group_name: Optional["capo_neptune.types.string.String"] = None,
        backup_retention_period: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        preferred_backup_window: Optional["capo_neptune.types.string.String"] = None,
        port: Optional["capo_neptune.types.integer_optional.IntegerOptional"] = None,
        multi_az: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        engine_version: Optional["capo_neptune.types.string.String"] = None,
        auto_minor_version_upgrade: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        license_model: Optional["capo_neptune.types.string.String"] = None,
        iops: Optional["capo_neptune.types.integer_optional.IntegerOptional"] = None,
        option_group_name: Optional["capo_neptune.types.string.String"] = None,
        character_set_name: Optional["capo_neptune.types.string.String"] = None,
        publicly_accessible: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        storage_type: Optional["capo_neptune.types.string.String"] = None,
        tde_credential_arn: Optional["capo_neptune.types.string.String"] = None,
        tde_credential_password: Optional[
            "capo_neptune.types.sensitive_string.SensitiveString"
        ] = None,
        storage_encrypted: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        kms_key_id: Optional["capo_neptune.types.string.String"] = None,
        domain: Optional["capo_neptune.types.string.String"] = None,
        copy_tags_to_snapshot: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        monitoring_interval: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        monitoring_role_arn: Optional["capo_neptune.types.string.String"] = None,
        domain_iam_role_name: Optional["capo_neptune.types.string.String"] = None,
        promotion_tier: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        timezone: Optional["capo_neptune.types.string.String"] = None,
        enable_iam_database_authentication: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        enable_performance_insights: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        performance_insights_kms_key_id: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        enable_cloudwatch_logs_exports: Optional[
            "capo_neptune.types.log_type_list.LogTypeList"
        ] = None,
        deletion_protection: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_neptune.types.create_db_instance_result.CreateDBInstanceResult":
        """<p>Creates a new DB instance.</p>

        Args:
            db_name: <p>Not supported.</p>
            db_instance_identifier: <p>The DB instance identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>mydbinstance</code> </p>
            allocated_storage: <p>Not supported by Neptune.</p>
            db_instance_class: <p>The compute and memory capacity of the DB instance, for example, <code>db.m4.large</code>. Not all DB instance classes are available in all Amazon Regions.</p>
            engine: <p>The name of the database engine to be used for this instance.</p> <p>Valid Values: <code>neptune</code> </p>
            master_username: <p>Not supported by Neptune.</p>
            master_user_password: <p>Not supported by Neptune.</p>
            db_security_groups: <p>A list of DB security groups to associate with this DB instance.</p> <p>Default: The default DB security group for the database engine.</p>
            vpc_security_group_ids: <p>A list of EC2 VPC security groups to associate with this DB instance.</p> <p>Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see <a>CreateDBCluster</a>.</p> <p>Default: The default EC2 VPC security group for the DB subnet group's VPC.</p>
            availability_zone: <p> The EC2 Availability Zone that the DB instance is created in</p> <p>Default: A random, system-chosen Availability Zone in the endpoint's Amazon Region.</p> <p> Example: <code>us-east-1d</code> </p> <p> Constraint: The AvailabilityZone parameter can't be specified if the MultiAZ parameter is set to <code>true</code>. The specified Availability Zone must be in the same Amazon Region as the current endpoint.</p>
            db_subnet_group_name: <p>A DB subnet group to associate with this DB instance.</p> <p>If there is no DB subnet group, then it is a non-VPC DB instance.</p>
            preferred_maintenance_window: <p>The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p> Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region, occurring on a random day of the week.</p> <p>Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.</p> <p>Constraints: Minimum 30-minute window.</p>
            db_parameter_group_name: <p>The name of the DB parameter group to associate with this DB instance. If this argument is omitted, the default DBParameterGroup for the specified engine is used.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul>
            backup_retention_period: <p>The number of days for which automated backups are retained.</p> <p>Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see <a>CreateDBCluster</a>.</p> <p>Default: 1</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 0 to 35</p> </li> <li> <p>Cannot be set to 0 if the DB instance is a source to Read Replicas</p> </li> </ul>
            preferred_backup_window: <p> The daily time range during which automated backups are created.</p> <p>Not applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see <a>CreateDBCluster</a>.</p>
            port: <p>The port number on which the database accepts connections.</p> <p>Not applicable. The port is managed by the DB cluster. For more information, see <a>CreateDBCluster</a>.</p> <p> Default: <code>8182</code> </p> <p>Type: Integer</p>
            multi_az: <p>Specifies if the DB instance is a Multi-AZ deployment. You can't set the AvailabilityZone parameter if the MultiAZ parameter is set to true.</p>
            engine_version: <p>The version number of the database engine to use. Currently, setting this parameter has no effect.</p>
            auto_minor_version_upgrade: <p>Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window.</p> <p>Default: <code>true</code> </p>
            license_model: <p>License model information for this DB instance.</p> <p> Valid values: <code>license-included</code> | <code>bring-your-own-license</code> | <code>general-public-license</code> </p>
            iops: <p>The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.</p>
            option_group_name: <p> <i>(Not supported by Neptune)</i> </p>
            character_set_name: <p> <i>(Not supported by Neptune)</i> </p>
            publicly_accessible: <p>Indicates whether the DB instance is publicly accessible.</p> <p>When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.</p> <p>When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.</p>
            tags: <p>The tags to assign to the new instance.</p>
            db_cluster_identifier: <p>The identifier of the DB cluster that the instance will belong to.</p> <p>For information on creating a DB cluster, see <a>CreateDBCluster</a>.</p> <p>Type: String</p>
            storage_type: <p>Not applicable. In Neptune the storage type is managed at the DB Cluster level.</p>
            tde_credential_arn: <p>The ARN from the key store with which to associate the instance for TDE encryption.</p>
            tde_credential_password: <p>The password for the given ARN from the key store in order to access the device.</p>
            storage_encrypted: <p>Specifies whether the DB instance is encrypted.</p> <p>Not applicable. The encryption for DB instances is managed by the DB cluster. For more information, see <a>CreateDBCluster</a>.</p> <p>Default: false</p>
            kms_key_id: <p>The Amazon KMS key identifier for an encrypted DB instance.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB instance with the same Amazon account that owns the KMS encryption key used to encrypt the new DB instance, then you can use the KMS key alias instead of the ARN for the KMS encryption key.</p> <p>Not applicable. The KMS key identifier is managed by the DB cluster. For more information, see <a>CreateDBCluster</a>.</p> <p>If the <code>StorageEncrypted</code> parameter is true, and you do not specify a value for the <code>KmsKeyId</code> parameter, then Amazon Neptune will use your default encryption key. Amazon KMS creates the default encryption key for your Amazon account. Your Amazon account has a different default encryption key for each Amazon Region.</p>
            domain: <p>Specify the Active Directory Domain to create the instance in.</p>
            copy_tags_to_snapshot: <p>True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.</p>
            monitoring_interval: <p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.</p> <p>If <code>MonitoringRoleArn</code> is specified, then you must also set <code>MonitoringInterval</code> to a value other than 0.</p> <p>Valid Values: <code>0, 1, 5, 10, 15, 30, 60</code> </p>
            monitoring_role_arn: <p>The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, <code>arn:aws:iam:123456789012:role/emaccess</code>.</p> <p>If <code>MonitoringInterval</code> is set to a value other than 0, then you must supply a <code>MonitoringRoleArn</code> value.</p>
            domain_iam_role_name: <p>Specify the name of the IAM role to be used when making API calls to the Directory Service.</p>
            promotion_tier: <p>A value that specifies the order in which an Read Replica is promoted to the primary instance after a failure of the existing primary instance. </p> <p>Default: 1</p> <p>Valid Values: 0 - 15</p>
            timezone: <p>The time zone of the DB instance.</p>
            enable_iam_database_authentication: <p>Not supported by Neptune (ignored).</p>
            enable_performance_insights: <p> <i>(Not supported by Neptune)</i> </p>
            performance_insights_kms_key_id: <p> <i>(Not supported by Neptune)</i> </p>
            enable_cloudwatch_logs_exports: <p>The list of log types that need to be enabled for exporting to CloudWatch Logs.</p>
            deletion_protection: <p>A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-delete.html">Deleting a DB Instance</a>.</p> <p>DB instances in a DB cluster can be deleted even when deletion protection is enabled in their parent DB cluster.</p>

        Raises:
            capo_neptune.errors.authorization_not_found_fault.AuthorizationNotFoundFault: <p>Specified CIDRIP or EC2 security group is not authorized for the specified DB security group.</p> <p>Neptune may not also be authorized via IAM to perform necessary actions on your behalf.</p>
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_instance_already_exists_fault.DBInstanceAlreadyExistsFault: <p>User already has a DB instance with the given identifier.</p>
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.db_security_group_not_found_fault.DBSecurityGroupNotFoundFault: <p> <i>DBSecurityGroupName</i> does not refer to an existing DB security group.</p>
            capo_neptune.errors.db_subnet_group_does_not_cover_enough_a_zs.DBSubnetGroupDoesNotCoverEnoughAZs: <p>Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.</p>
            capo_neptune.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <i>DBSubnetGroupName</i> does not refer to an existing DB subnet group.</p>
            capo_neptune.errors.domain_not_found_fault.DomainNotFoundFault: <p> <i>Domain</i> does not refer to an existing Active Directory Domain.</p>
            capo_neptune.errors.instance_quota_exceeded_fault.InstanceQuotaExceededFault: <p>Request would result in user exceeding the allowed number of DB instances.</p>
            capo_neptune.errors.insufficient_db_instance_capacity_fault.InsufficientDBInstanceCapacityFault: <p>Specified DB instance class is not available in the specified Availability Zone.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.</p>
            capo_neptune.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>DB subnet group does not cover all Availability Zones after it is created because users' change.</p>
            capo_neptune.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>Error accessing KMS key.</p>
            capo_neptune.errors.option_group_not_found_fault.OptionGroupNotFoundFault: <p>The designated option group could not be found.</p>
            capo_neptune.errors.provisioned_iops_not_available_in_az_fault.ProvisionedIopsNotAvailableInAZFault: <p>Provisioned IOPS not available in the specified Availability Zone.</p>
            capo_neptune.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>Request would result in user exceeding the allowed amount of storage available across all DB instances.</p>
            capo_neptune.errors.storage_type_not_supported_fault.StorageTypeNotSupportedFault: <p> <i>StorageType</i> specified cannot be associated with the DB Instance.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.create_db_instance_message.CreateDBInstanceMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.create_db_instance_result.CreateDBInstanceResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.create_db_instance

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.create_db_instance.async_create_db_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.create_db_instance_message.CreateDBInstanceMessage = {}
        if db_name is not None:
            input_["db_name"] = db_name
        if db_instance_identifier is not None:
            input_["db_instance_identifier"] = db_instance_identifier
        if allocated_storage is not None:
            input_["allocated_storage"] = allocated_storage
        if db_instance_class is not None:
            input_["db_instance_class"] = db_instance_class
        if engine is not None:
            input_["engine"] = engine
        if master_username is not None:
            input_["master_username"] = master_username
        if master_user_password is not None:
            input_["master_user_password"] = master_user_password
        if db_security_groups is not None:
            input_["db_security_groups"] = db_security_groups
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if db_parameter_group_name is not None:
            input_["db_parameter_group_name"] = db_parameter_group_name
        if backup_retention_period is not None:
            input_["backup_retention_period"] = backup_retention_period
        if preferred_backup_window is not None:
            input_["preferred_backup_window"] = preferred_backup_window
        if port is not None:
            input_["port"] = port
        if multi_az is not None:
            input_["multi_az"] = multi_az
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if license_model is not None:
            input_["license_model"] = license_model
        if iops is not None:
            input_["iops"] = iops
        if option_group_name is not None:
            input_["option_group_name"] = option_group_name
        if character_set_name is not None:
            input_["character_set_name"] = character_set_name
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if tags is not None:
            input_["tags"] = tags
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if tde_credential_arn is not None:
            input_["tde_credential_arn"] = tde_credential_arn
        if tde_credential_password is not None:
            input_["tde_credential_password"] = tde_credential_password
        if storage_encrypted is not None:
            input_["storage_encrypted"] = storage_encrypted
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if domain is not None:
            input_["domain"] = domain
        if copy_tags_to_snapshot is not None:
            input_["copy_tags_to_snapshot"] = copy_tags_to_snapshot
        if monitoring_interval is not None:
            input_["monitoring_interval"] = monitoring_interval
        if monitoring_role_arn is not None:
            input_["monitoring_role_arn"] = monitoring_role_arn
        if domain_iam_role_name is not None:
            input_["domain_iam_role_name"] = domain_iam_role_name
        if promotion_tier is not None:
            input_["promotion_tier"] = promotion_tier
        if timezone is not None:
            input_["timezone"] = timezone
        if enable_iam_database_authentication is not None:
            input_["enable_iam_database_authentication"] = (
                enable_iam_database_authentication
            )
        if enable_performance_insights is not None:
            input_["enable_performance_insights"] = enable_performance_insights
        if performance_insights_kms_key_id is not None:
            input_["performance_insights_kms_key_id"] = performance_insights_kms_key_id
        if enable_cloudwatch_logs_exports is not None:
            input_["enable_cloudwatch_logs_exports"] = enable_cloudwatch_logs_exports
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_db_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_parameter_group_name: Optional["capo_neptune.types.string.String"] = None,
        db_parameter_group_family: Optional["capo_neptune.types.string.String"] = None,
        description: Optional["capo_neptune.types.string.String"] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
    ) -> "capo_neptune.types.create_db_parameter_group_result.CreateDBParameterGroupResult":
        """<p>Creates a new DB parameter group.</p> <p>A DB parameter group is initially created with the default parameters for the database engine used by the DB instance. To provide custom values for any of the parameters, you must modify the group after creating it using <i>ModifyDBParameterGroup</i>. Once you've created a DB parameter group, you need to associate it with your DB instance using <i>ModifyDBInstance</i>. When you associate a new DB parameter group with a running DB instance, you need to reboot the DB instance without failover for the new DB parameter group and associated settings to take effect.</p> <important> <p>After you create a DB parameter group, you should wait at least 5 minutes before creating your first DB instance that uses that DB parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the parameter group is used as the default for a new DB instance. This is especially important for parameters that are critical when creating the default database for a DB instance, such as the character set for the default database defined by the <code>character_set_database</code> parameter. You can use the <i>Parameter Groups</i> option of the Amazon Neptune console or the <i>DescribeDBParameters</i> command to verify that your DB parameter group has been created or modified.</p> </important>

        Args:
            db_parameter_group_name: <p>The name of the DB parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <note> <p>This value is stored as a lowercase string.</p> </note>
            db_parameter_group_family: <p>The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a database engine and engine version compatible with that DB parameter group family.</p>
            description: <p>The description for the DB parameter group.</p>
            tags: <p>The tags to be assigned to the new DB parameter group.</p>

        Raises:
            capo_neptune.errors.db_parameter_group_already_exists_fault.DBParameterGroupAlreadyExistsFault: <p>A DB parameter group with the same name exists.</p>
            capo_neptune.errors.db_parameter_group_quota_exceeded_fault.DBParameterGroupQuotaExceededFault: <p>Request would result in user exceeding the allowed number of DB parameter groups.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.create_db_parameter_group_message.CreateDBParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.create_db_parameter_group_result.CreateDBParameterGroupResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.create_db_parameter_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.create_db_parameter_group.async_create_db_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.create_db_parameter_group_message.CreateDBParameterGroupMessage = {}
        if db_parameter_group_name is not None:
            input_["db_parameter_group_name"] = db_parameter_group_name
        if db_parameter_group_family is not None:
            input_["db_parameter_group_family"] = db_parameter_group_family
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

    async def create_db_subnet_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_subnet_group_name: Optional["capo_neptune.types.string.String"] = None,
        db_subnet_group_description: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        subnet_ids: Optional[
            "capo_neptune.types.subnet_identifier_list.SubnetIdentifierList"
        ] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
    ) -> "capo_neptune.types.create_db_subnet_group_result.CreateDBSubnetGroupResult":
        """<p>Creates a new DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the Amazon Region.</p>

        Args:
            db_subnet_group_name: <p>The name for the DB subnet group. This value is stored as a lowercase string.</p> <p>Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>
            db_subnet_group_description: <p>The description for the DB subnet group.</p>
            subnet_ids: <p>The EC2 Subnet IDs for the DB subnet group.</p>
            tags: <p>The tags to be assigned to the new DB subnet group.</p>

        Raises:
            capo_neptune.errors.db_subnet_group_already_exists_fault.DBSubnetGroupAlreadyExistsFault: <p> <i>DBSubnetGroupName</i> is already used by an existing DB subnet group.</p>
            capo_neptune.errors.db_subnet_group_does_not_cover_enough_a_zs.DBSubnetGroupDoesNotCoverEnoughAZs: <p>Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.</p>
            capo_neptune.errors.db_subnet_group_quota_exceeded_fault.DBSubnetGroupQuotaExceededFault: <p>Request would result in user exceeding the allowed number of DB subnet groups.</p>
            capo_neptune.errors.db_subnet_quota_exceeded_fault.DBSubnetQuotaExceededFault: <p>Request would result in user exceeding the allowed number of subnets in a DB subnet groups.</p>
            capo_neptune.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.create_db_subnet_group_message.CreateDBSubnetGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.create_db_subnet_group_result.CreateDBSubnetGroupResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.create_db_subnet_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.create_db_subnet_group.async_create_db_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.create_db_subnet_group_message.CreateDBSubnetGroupMessage = {}
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name
        if db_subnet_group_description is not None:
            input_["db_subnet_group_description"] = db_subnet_group_description
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

    async def create_event_subscription(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        subscription_name: Optional["capo_neptune.types.string.String"] = None,
        sns_topic_arn: Optional["capo_neptune.types.string.String"] = None,
        source_type: Optional["capo_neptune.types.string.String"] = None,
        event_categories: Optional[
            "capo_neptune.types.event_categories_list.EventCategoriesList"
        ] = None,
        source_ids: Optional["capo_neptune.types.source_ids_list.SourceIdsList"] = None,
        enabled: Optional["capo_neptune.types.boolean_optional.BooleanOptional"] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
    ) -> "capo_neptune.types.create_event_subscription_result.CreateEventSubscriptionResult":
        """<p>Creates an event notification subscription. This action requires a topic ARN (Amazon Resource Name) created by either the Neptune console, the SNS console, or the SNS API. To obtain an ARN with SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.</p> <p>You can specify the type of source (SourceType) you want to be notified of, provide a list of Neptune sources (SourceIds) that triggers the events, and provide a list of event categories (EventCategories) for events you want to be notified of. For example, you can specify SourceType = db-instance, SourceIds = mydbinstance1, mydbinstance2 and EventCategories = Availability, Backup.</p> <p>If you specify both the SourceType and SourceIds, such as SourceType = db-instance and SourceIdentifier = myDBInstance1, you are notified of all the db-instance events for the specified source. If you specify a SourceType but do not specify a SourceIdentifier, you receive notice of the events for that source type for all your Neptune sources. If you do not specify either the SourceType nor the SourceIdentifier, you are notified of events generated from all Neptune sources belonging to your customer account.</p>

        Args:
            subscription_name: <p>The name of the subscription.</p> <p>Constraints: The name must be less than 255 characters.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.</p>
            source_type: <p>The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.</p> <p>Valid values: <code>db-instance</code> | <code>db-cluster</code> | <code>db-parameter-group</code> | <code>db-security-group</code> | <code>db-snapshot</code> | <code>db-cluster-snapshot</code> </p>
            event_categories: <p> A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType by using the <b>DescribeEventCategories</b> action.</p>
            source_ids: <p>The list of identifiers of the event sources for which events are returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.</p> <p>Constraints:</p> <ul> <li> <p>If SourceIds are supplied, SourceType must also be provided.</p> </li> <li> <p>If the source type is a DB instance, then a <code>DBInstanceIdentifier</code> must be supplied.</p> </li> <li> <p>If the source type is a DB security group, a <code>DBSecurityGroupName</code> must be supplied.</p> </li> <li> <p>If the source type is a DB parameter group, a <code>DBParameterGroupName</code> must be supplied.</p> </li> <li> <p>If the source type is a DB snapshot, a <code>DBSnapshotIdentifier</code> must be supplied.</p> </li> </ul>
            enabled: <p> A Boolean value; set to <b>true</b> to activate the subscription, set to <b>false</b> to create the subscription but not activate it.</p>
            tags: <p>The tags to be applied to the new event subscription.</p>

        Raises:
            capo_neptune.errors.event_subscription_quota_exceeded_fault.EventSubscriptionQuotaExceededFault: <p>You have exceeded the number of events you can subscribe to.</p>
            capo_neptune.errors.sns_invalid_topic_fault.SNSInvalidTopicFault: <p>The SNS topic is invalid.</p>
            capo_neptune.errors.sns_no_authorization_fault.SNSNoAuthorizationFault: <p>There is no SNS authorization.</p>
            capo_neptune.errors.sns_topic_arn_not_found_fault.SNSTopicArnNotFoundFault: <p>The ARN of the SNS topic could not be found.</p>
            capo_neptune.errors.source_not_found_fault.SourceNotFoundFault: <p>The source could not be found.</p>
            capo_neptune.errors.subscription_already_exist_fault.SubscriptionAlreadyExistFault: <p>This subscription already exists.</p>
            capo_neptune.errors.subscription_category_not_found_fault.SubscriptionCategoryNotFoundFault: <p>The designated subscription category could not be found.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.create_event_subscription_message.CreateEventSubscriptionMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.create_event_subscription_result.CreateEventSubscriptionResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.create_event_subscription

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.create_event_subscription.async_create_event_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.create_event_subscription_message.CreateEventSubscriptionMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if source_type is not None:
            input_["source_type"] = source_type
        if event_categories is not None:
            input_["event_categories"] = event_categories
        if source_ids is not None:
            input_["source_ids"] = source_ids
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

    async def create_global_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        source_db_cluster_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        engine: Optional["capo_neptune.types.string.String"] = None,
        engine_version: Optional["capo_neptune.types.string.String"] = None,
        deletion_protection: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        database_name: Optional["capo_neptune.types.string.String"] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
        storage_encrypted: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_neptune.types.create_global_cluster_result.CreateGlobalClusterResult":
        """<p>Creates a Neptune global database spread across multiple Amazon Regions. The global database contains a single primary cluster with read-write capability, and read-only secondary clusters that receive data from the primary cluster through high-speed replication performed by the Neptune storage subsystem.</p> <p>You can create a global database that is initially empty, and then add a primary cluster and secondary clusters to it, or you can specify an existing Neptune cluster during the create operation to become the primary cluster of the global database.</p>

        Args:
            global_cluster_identifier: <p>The cluster identifier of the new global database cluster.</p>
            source_db_cluster_identifier: <p>(<i>Optional</i>) The Amazon Resource Name (ARN) of an existing Neptune DB cluster to use as the primary cluster of the new global database.</p>
            engine: <p>The name of the database engine to be used in the global database.</p> <p>Valid values: <code>neptune</code> </p>
            engine_version: <p>The Neptune engine version to be used by the global database.</p> <p>Valid values: <code>1.2.0.0</code> or above.</p>
            deletion_protection: <p>The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.</p>
            database_name: <p>The name for the new global database (up to 64 alpha-numeric characters).</p>
            tags: <p>Tags to assign to the global cluster.</p>
            storage_encrypted: <p>The storage encryption setting for the new global database cluster.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.global_cluster_already_exists_fault.GlobalClusterAlreadyExistsFault: <p>The <code>GlobalClusterIdentifier</code> already exists. Choose a new global database identifier (unique name) to create a new global database cluster.</p>
            capo_neptune.errors.global_cluster_quota_exceeded_fault.GlobalClusterQuotaExceededFault: <p>The number of global database clusters for this account is already at the maximum allowed.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.create_global_cluster_message.CreateGlobalClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.create_global_cluster_result.CreateGlobalClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.create_global_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.create_global_cluster.async_create_global_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.create_global_cluster_message.CreateGlobalClusterMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if source_db_cluster_identifier is not None:
            input_["source_db_cluster_identifier"] = source_db_cluster_identifier
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if database_name is not None:
            input_["database_name"] = database_name
        if tags is not None:
            input_["tags"] = tags
        if storage_encrypted is not None:
            input_["storage_encrypted"] = storage_encrypted

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_db_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        skip_final_snapshot: Optional["capo_neptune.types.boolean.Boolean"] = None,
        final_db_snapshot_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
    ) -> "capo_neptune.types.delete_db_cluster_result.DeleteDBClusterResult":
        """<p>The DeleteDBCluster action deletes a previously provisioned DB cluster. When you delete a DB cluster, all automated backups for that DB cluster are deleted and can't be recovered. Manual DB cluster snapshots of the specified DB cluster are not deleted.</p> <p>Note that the DB Cluster cannot be deleted if deletion protection is enabled. To delete it, you must first set its <code>DeletionProtection</code> field to <code>False</code>.</p>

        Args:
            db_cluster_identifier: <p>The DB cluster identifier for the DB cluster to be deleted. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match an existing DBClusterIdentifier.</p> </li> </ul>
            skip_final_snapshot: <p> Determines whether a final DB cluster snapshot is created before the DB cluster is deleted. If <code>true</code> is specified, no DB cluster snapshot is created. If <code>false</code> is specified, a DB cluster snapshot is created before the DB cluster is deleted.</p> <note> <p>You must specify a <code>FinalDBSnapshotIdentifier</code> parameter if <code>SkipFinalSnapshot</code> is <code>false</code>.</p> </note> <p>Default: <code>false</code> </p>
            final_db_snapshot_identifier: <p> The DB cluster snapshot identifier of the new DB cluster snapshot created when <code>SkipFinalSnapshot</code> is set to <code>false</code>.</p> <note> <p> Specifying this parameter and also setting the <code>SkipFinalSnapshot</code> parameter to true results in an error.</p> </note> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_cluster_snapshot_already_exists_fault.DBClusterSnapshotAlreadyExistsFault: <p>User already has a DB cluster snapshot with the given identifier.</p>
            capo_neptune.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The supplied value is not a valid DB cluster snapshot state.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>Request would result in user exceeding the allowed number of DB snapshots.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.delete_db_cluster_message.DeleteDBClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.delete_db_cluster_result.DeleteDBClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.delete_db_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.delete_db_cluster.async_delete_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.delete_db_cluster_message.DeleteDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if skip_final_snapshot is not None:
            input_["skip_final_snapshot"] = skip_final_snapshot
        if final_db_snapshot_identifier is not None:
            input_["final_db_snapshot_identifier"] = final_db_snapshot_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_db_cluster_endpoint(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_endpoint_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
    ) -> "capo_neptune.types.delete_db_cluster_endpoint_output.DeleteDBClusterEndpointOutput":
        """<p>Deletes a custom endpoint and removes it from an Amazon Neptune DB cluster.</p>

        Args:
            db_cluster_endpoint_identifier: <p>The identifier associated with the custom endpoint. This parameter is stored as a lowercase string.</p>

        Raises:
            capo_neptune.errors.db_cluster_endpoint_not_found_fault.DBClusterEndpointNotFoundFault: <p>The specified custom endpoint doesn't exist.</p>
            capo_neptune.errors.invalid_db_cluster_endpoint_state_fault.InvalidDBClusterEndpointStateFault: <p>The requested operation cannot be performed on the endpoint while the endpoint is in this state.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.delete_db_cluster_endpoint_message.DeleteDBClusterEndpointMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.delete_db_cluster_endpoint_output.DeleteDBClusterEndpointOutput"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.delete_db_cluster_endpoint

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.delete_db_cluster_endpoint.async_delete_db_cluster_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.delete_db_cluster_endpoint_message.DeleteDBClusterEndpointMessage = {}
        if db_cluster_endpoint_identifier is not None:
            input_["db_cluster_endpoint_identifier"] = db_cluster_endpoint_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_db_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
    ) -> None:
        """<p>Deletes a specified DB cluster parameter group. The DB cluster parameter group to be deleted can't be associated with any DB clusters.</p>

        Args:
            db_cluster_parameter_group_name: <p>The name of the DB cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must be the name of an existing DB cluster parameter group.</p> </li> <li> <p>You can't delete a default DB cluster parameter group.</p> </li> <li> <p>Cannot be associated with any DB clusters.</p> </li> </ul>

        Raises:
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.invalid_db_parameter_group_state_fault.InvalidDBParameterGroupStateFault: <p>The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you cannot delete it when the parameter group is in this state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.delete_db_cluster_parameter_group_message.DeleteDBClusterParameterGroupMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_neptune._operations.amazon_rd_sv19.delete_db_cluster_parameter_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.delete_db_cluster_parameter_group.async_delete_db_cluster_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.delete_db_cluster_parameter_group_message.DeleteDBClusterParameterGroupMessage = {}
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_db_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
    ) -> "capo_neptune.types.delete_db_cluster_snapshot_result.DeleteDBClusterSnapshotResult":
        """<p>Deletes a DB cluster snapshot. If the snapshot is being copied, the copy operation is terminated.</p> <note> <p>The DB cluster snapshot must be in the <code>available</code> state to be deleted.</p> </note>

        Args:
            db_cluster_snapshot_identifier: <p>The identifier of the DB cluster snapshot to delete.</p> <p>Constraints: Must be the name of an existing DB cluster snapshot in the <code>available</code> state.</p>

        Raises:
            capo_neptune.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <i>DBClusterSnapshotIdentifier</i> does not refer to an existing DB cluster snapshot.</p>
            capo_neptune.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The supplied value is not a valid DB cluster snapshot state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.delete_db_cluster_snapshot_message.DeleteDBClusterSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.delete_db_cluster_snapshot_result.DeleteDBClusterSnapshotResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.delete_db_cluster_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.delete_db_cluster_snapshot.async_delete_db_cluster_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.delete_db_cluster_snapshot_message.DeleteDBClusterSnapshotMessage = {}
        if db_cluster_snapshot_identifier is not None:
            input_["db_cluster_snapshot_identifier"] = db_cluster_snapshot_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_db_instance(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_instance_identifier: Optional["capo_neptune.types.string.String"] = None,
        skip_final_snapshot: Optional["capo_neptune.types.boolean.Boolean"] = None,
        final_db_snapshot_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
    ) -> "capo_neptune.types.delete_db_instance_result.DeleteDBInstanceResult":
        """<p>The DeleteDBInstance action deletes a previously provisioned DB instance. When you delete a DB instance, all automated backups for that instance are deleted and can't be recovered. Manual DB snapshots of the DB instance to be deleted by <code>DeleteDBInstance</code> are not deleted.</p> <p> If you request a final DB snapshot the status of the Amazon Neptune DB instance is <code>deleting</code> until the DB snapshot is created. The API action <code>DescribeDBInstance</code> is used to monitor the status of this operation. The action can't be canceled or reverted once submitted.</p> <p>Note that when a DB instance is in a failure state and has a status of <code>failed</code>, <code>incompatible-restore</code>, or <code>incompatible-network</code>, you can only delete it when the <code>SkipFinalSnapshot</code> parameter is set to <code>true</code>.</p> <p>You can't delete a DB instance if it is the only instance in the DB cluster, or if it has deletion protection enabled.</p>

        Args:
            db_instance_identifier: <p>The DB instance identifier for the DB instance to be deleted. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the name of an existing DB instance.</p> </li> </ul>
            skip_final_snapshot: <p> Determines whether a final DB snapshot is created before the DB instance is deleted. If <code>true</code> is specified, no DBSnapshot is created. If <code>false</code> is specified, a DB snapshot is created before the DB instance is deleted.</p> <p>Note that when a DB instance is in a failure state and has a status of 'failed', 'incompatible-restore', or 'incompatible-network', it can only be deleted when the SkipFinalSnapshot parameter is set to "true".</p> <p>Specify <code>true</code> when deleting a Read Replica.</p> <note> <p>The FinalDBSnapshotIdentifier parameter must be specified if SkipFinalSnapshot is <code>false</code>.</p> </note> <p>Default: <code>false</code> </p>
            final_db_snapshot_identifier: <p> The DBSnapshotIdentifier of the new DBSnapshot created when SkipFinalSnapshot is set to <code>false</code>.</p> <note> <p>Specifying this parameter and also setting the SkipFinalSnapshot parameter to true results in an error.</p> </note> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters or numbers.</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> <li> <p>Cannot be specified when deleting a Read Replica.</p> </li> </ul>

        Raises:
            capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <i>DBInstanceIdentifier</i> does not refer to an existing DB instance.</p>
            capo_neptune.errors.db_snapshot_already_exists_fault.DBSnapshotAlreadyExistsFault: <p> <i>DBSnapshotIdentifier</i> is already used by an existing snapshot.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>Request would result in user exceeding the allowed number of DB snapshots.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.delete_db_instance_message.DeleteDBInstanceMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.delete_db_instance_result.DeleteDBInstanceResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.delete_db_instance

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.delete_db_instance.async_delete_db_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.delete_db_instance_message.DeleteDBInstanceMessage = {}
        if db_instance_identifier is not None:
            input_["db_instance_identifier"] = db_instance_identifier
        if skip_final_snapshot is not None:
            input_["skip_final_snapshot"] = skip_final_snapshot
        if final_db_snapshot_identifier is not None:
            input_["final_db_snapshot_identifier"] = final_db_snapshot_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_db_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_parameter_group_name: Optional["capo_neptune.types.string.String"] = None,
    ) -> None:
        """<p>Deletes a specified DBParameterGroup. The DBParameterGroup to be deleted can't be associated with any DB instances.</p>

        Args:
            db_parameter_group_name: <p>The name of the DB parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must be the name of an existing DB parameter group</p> </li> <li> <p>You can't delete a default DB parameter group</p> </li> <li> <p>Cannot be associated with any DB instances</p> </li> </ul>

        Raises:
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.invalid_db_parameter_group_state_fault.InvalidDBParameterGroupStateFault: <p>The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you cannot delete it when the parameter group is in this state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.delete_db_parameter_group_message.DeleteDBParameterGroupMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_neptune._operations.amazon_rd_sv19.delete_db_parameter_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.delete_db_parameter_group.async_delete_db_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.delete_db_parameter_group_message.DeleteDBParameterGroupMessage = {}
        if db_parameter_group_name is not None:
            input_["db_parameter_group_name"] = db_parameter_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_db_subnet_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_subnet_group_name: Optional["capo_neptune.types.string.String"] = None,
    ) -> None:
        """<p>Deletes a DB subnet group.</p> <note> <p>The specified database subnet group must not be associated with any DB instances.</p> </note>

        Args:
            db_subnet_group_name: <p>The name of the database subnet group to delete.</p> <note> <p>You can't delete the default subnet group.</p> </note> <p>Constraints:</p> <p>Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>

        Raises:
            capo_neptune.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <i>DBSubnetGroupName</i> does not refer to an existing DB subnet group.</p>
            capo_neptune.errors.invalid_db_subnet_group_state_fault.InvalidDBSubnetGroupStateFault: <p>The DB subnet group cannot be deleted because it is in use.</p>
            capo_neptune.errors.invalid_db_subnet_state_fault.InvalidDBSubnetStateFault: <p>The DB subnet is not in the <i>available</i> state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.delete_db_subnet_group_message.DeleteDBSubnetGroupMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_neptune._operations.amazon_rd_sv19.delete_db_subnet_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.delete_db_subnet_group.async_delete_db_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.delete_db_subnet_group_message.DeleteDBSubnetGroupMessage = {}
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name

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
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        subscription_name: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.delete_event_subscription_result.DeleteEventSubscriptionResult":
        """<p>Deletes an event notification subscription.</p>

        Args:
            subscription_name: <p>The name of the event notification subscription you want to delete.</p>

        Raises:
            capo_neptune.errors.invalid_event_subscription_state_fault.InvalidEventSubscriptionStateFault: <p>The event subscription is in an invalid state.</p>
            capo_neptune.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>The designated subscription could not be found.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.delete_event_subscription_message.DeleteEventSubscriptionMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.delete_event_subscription_result.DeleteEventSubscriptionResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.delete_event_subscription

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.delete_event_subscription.async_delete_event_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.delete_event_subscription_message.DeleteEventSubscriptionMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_global_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
    ) -> "capo_neptune.types.delete_global_cluster_result.DeleteGlobalClusterResult":
        """<p>Deletes a global database. The primary and all secondary clusters must already be detached or deleted first.</p>

        Args:
            global_cluster_identifier: <p>The cluster identifier of the global database cluster being deleted.</p>

        Raises:
            capo_neptune.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global database cluster. </p>
            capo_neptune.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The global cluster is in an invalid state and can't perform the requested operation. </p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.delete_global_cluster_message.DeleteGlobalClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.delete_global_cluster_result.DeleteGlobalClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.delete_global_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.delete_global_cluster.async_delete_global_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.delete_global_cluster_message.DeleteGlobalClusterMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_db_cluster_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        db_cluster_endpoint_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.db_cluster_endpoint_message.DBClusterEndpointMessage":
        """<p>Returns information about endpoints for an Amazon Neptune DB cluster.</p> <note> <p>This operation can also return information for Amazon RDS clusters and Amazon DocDB clusters.</p> </note>

        Args:
            db_cluster_identifier: <p>The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.</p>
            db_cluster_endpoint_identifier: <p>The identifier of the endpoint to describe. This parameter is stored as a lowercase string.</p>
            filters: <p>A set of name-value pairs that define which endpoints to include in the output. The filters are specified as name-value pairs, in the format <code>Name=<i>endpoint_type</i>,Values=<i>endpoint_type1</i>,<i>endpoint_type2</i>,...</code>. <code>Name</code> can be one of: <code>db-cluster-endpoint-type</code>, <code>db-cluster-endpoint-custom-type</code>, <code>db-cluster-endpoint-id</code>, <code>db-cluster-endpoint-status</code>. <code>Values</code> for the <code> db-cluster-endpoint-type</code> filter can be one or more of: <code>reader</code>, <code>writer</code>, <code>custom</code>. <code>Values</code> for the <code>db-cluster-endpoint-custom-type</code> filter can be one or more of: <code>reader</code>, <code>any</code>. <code>Values</code> for the <code>db-cluster-endpoint-status</code> filter can be one or more of: <code>available</code>, <code>creating</code>, <code>deleting</code>, <code>inactive</code>, <code>modifying</code>. </p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous <code>DescribeDBClusterEndpoints</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_db_cluster_endpoints_message.DescribeDBClusterEndpointsMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_cluster_endpoint_message.DBClusterEndpointMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_db_cluster_endpoints

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_db_cluster_endpoints.async_describe_db_cluster_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_db_cluster_endpoints_message.DescribeDBClusterEndpointsMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if db_cluster_endpoint_identifier is not None:
            input_["db_cluster_endpoint_identifier"] = db_cluster_endpoint_identifier
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

    async def iter_describe_db_cluster_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        db_cluster_endpoint_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.db_cluster_endpoint.DBClusterEndpoint]":
        _token = marker
        while True:
            _response = await self.describe_db_cluster_endpoints(
                config_overrides=config_overrides,
                db_cluster_identifier=db_cluster_identifier,
                db_cluster_endpoint_identifier=db_cluster_endpoint_identifier,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("db_cluster_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_db_cluster_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.db_cluster_parameter_groups_message.DBClusterParameterGroupsMessage":
        """<p> Returns a list of <code>DBClusterParameterGroup</code> descriptions. If a <code>DBClusterParameterGroupName</code> parameter is specified, the list will contain only the description of the specified DB cluster parameter group.</p>

        Args:
            db_cluster_parameter_group_name: <p>The name of a specific DB cluster parameter group to return details for.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBClusterParameterGroup.</p> </li> </ul>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous <code>DescribeDBClusterParameterGroups</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_db_cluster_parameter_groups_message.DescribeDBClusterParameterGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_cluster_parameter_groups_message.DBClusterParameterGroupsMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_db_cluster_parameter_groups

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_db_cluster_parameter_groups.async_describe_db_cluster_parameter_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_db_cluster_parameter_groups_message.DescribeDBClusterParameterGroupsMessage = {}
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
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

    async def iter_describe_db_cluster_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.db_cluster_parameter_group.DBClusterParameterGroup]":
        _token = marker
        while True:
            _response = await self.describe_db_cluster_parameter_groups(
                config_overrides=config_overrides,
                db_cluster_parameter_group_name=db_cluster_parameter_group_name,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("db_cluster_parameter_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_db_cluster_parameters(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        source: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.db_cluster_parameter_group_details.DBClusterParameterGroupDetails":
        """<p>Returns the detailed parameter list for a particular DB cluster parameter group.</p>

        Args:
            db_cluster_parameter_group_name: <p>The name of a specific DB cluster parameter group to return parameter details for.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBClusterParameterGroup.</p> </li> </ul>
            source: <p> A value that indicates to return only parameters for a specific source. Parameter sources can be <code>engine</code>, <code>service</code>, or <code>customer</code>.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous <code>DescribeDBClusterParameters</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_db_cluster_parameters_message.DescribeDBClusterParametersMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_cluster_parameter_group_details.DBClusterParameterGroupDetails"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_db_cluster_parameters

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_db_cluster_parameters.async_describe_db_cluster_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_db_cluster_parameters_message.DescribeDBClusterParametersMessage = {}
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if source is not None:
            input_["source"] = source
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

    async def iter_describe_db_cluster_parameters(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        source: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.parameter.Parameter]":
        _token = marker
        while True:
            _response = await self.describe_db_cluster_parameters(
                config_overrides=config_overrides,
                db_cluster_parameter_group_name=db_cluster_parameter_group_name,
                source=source,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("parameters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_db_clusters(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.db_cluster_message.DBClusterMessage":
        """<p>Returns information about provisioned DB clusters, and supports pagination.</p> <note> <p>This operation can also return information for Amazon RDS clusters and Amazon DocDB clusters.</p> </note>

        Args:
            db_cluster_identifier: <p>The user-supplied DB cluster identifier. If this parameter is specified, information from only the specific DB cluster is returned. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match an existing DBClusterIdentifier.</p> </li> </ul>
            filters: <p>A filter that specifies one or more DB clusters to describe.</p> <p>Supported filters:</p> <ul> <li> <p> <code>db-cluster-id</code> - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB clusters identified by these ARNs.</p> </li> <li> <p> <code>engine</code> - Accepts an engine name (such as <code>neptune</code>), and restricts the results list to DB clusters created by that engine.</p> </li> </ul> <p>For example, to invoke this API from the Amazon CLI and filter so that only Neptune DB clusters are returned, you could use the following command:</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous <a>DescribeDBClusters</a> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_db_clusters_message.DescribeDBClustersMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_cluster_message.DBClusterMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_db_clusters

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_db_clusters.async_describe_db_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_db_clusters_message.DescribeDBClustersMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
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

    async def iter_describe_db_clusters(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.db_cluster.DBCluster]":
        _token = marker
        while True:
            _response = await self.describe_db_clusters(
                config_overrides=config_overrides,
                db_cluster_identifier=db_cluster_identifier,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("db_clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_db_cluster_snapshot_attributes(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
    ) -> "capo_neptune.types.describe_db_cluster_snapshot_attributes_result.DescribeDBClusterSnapshotAttributesResult":
        """<p>Returns a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot.</p> <p>When sharing snapshots with other Amazon accounts, <code>DescribeDBClusterSnapshotAttributes</code> returns the <code>restore</code> attribute and a list of IDs for the Amazon accounts that are authorized to copy or restore the manual DB cluster snapshot. If <code>all</code> is included in the list of values for the <code>restore</code> attribute, then the manual DB cluster snapshot is public and can be copied or restored by all Amazon accounts.</p> <p>To add or remove access for an Amazon account to copy or restore a manual DB cluster snapshot, or to make the manual DB cluster snapshot public or private, use the <a>ModifyDBClusterSnapshotAttribute</a> API action.</p>

        Args:
            db_cluster_snapshot_identifier: <p>The identifier for the DB cluster snapshot to describe the attributes for.</p>

        Raises:
            capo_neptune.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <i>DBClusterSnapshotIdentifier</i> does not refer to an existing DB cluster snapshot.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_db_cluster_snapshot_attributes_message.DescribeDBClusterSnapshotAttributesMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.describe_db_cluster_snapshot_attributes_result.DescribeDBClusterSnapshotAttributesResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_db_cluster_snapshot_attributes

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_db_cluster_snapshot_attributes.async_describe_db_cluster_snapshot_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_db_cluster_snapshot_attributes_message.DescribeDBClusterSnapshotAttributesMessage = {}
        if db_cluster_snapshot_identifier is not None:
            input_["db_cluster_snapshot_identifier"] = db_cluster_snapshot_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_db_cluster_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        snapshot_type: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
        include_shared: Optional["capo_neptune.types.boolean.Boolean"] = None,
        include_public: Optional["capo_neptune.types.boolean.Boolean"] = None,
    ) -> "capo_neptune.types.db_cluster_snapshot_message.DBClusterSnapshotMessage":
        """<p>Returns information about DB cluster snapshots. This API action supports pagination.</p>

        Args:
            db_cluster_identifier: <p>The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter can't be used in conjunction with the <code>DBClusterSnapshotIdentifier</code> parameter. This parameter is not case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the identifier of an existing DBCluster.</p> </li> </ul>
            db_cluster_snapshot_identifier: <p>A specific DB cluster snapshot identifier to describe. This parameter can't be used in conjunction with the <code>DBClusterIdentifier</code> parameter. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the identifier of an existing DBClusterSnapshot.</p> </li> <li> <p>If this identifier is for an automated snapshot, the <code>SnapshotType</code> parameter must also be specified.</p> </li> </ul>
            snapshot_type: <p>The type of DB cluster snapshots to be returned. You can specify one of the following values:</p> <ul> <li> <p> <code>automated</code> - Return all DB cluster snapshots that have been automatically taken by Amazon Neptune for my Amazon account.</p> </li> <li> <p> <code>manual</code> - Return all DB cluster snapshots that have been taken by my Amazon account.</p> </li> <li> <p> <code>shared</code> - Return all manual DB cluster snapshots that have been shared to my Amazon account.</p> </li> <li> <p> <code>public</code> - Return all DB cluster snapshots that have been marked as public.</p> </li> </ul> <p>If you don't specify a <code>SnapshotType</code> value, then both automated and manual DB cluster snapshots are returned. You can include shared DB cluster snapshots with these results by setting the <code>IncludeShared</code> parameter to <code>true</code>. You can include public DB cluster snapshots with these results by setting the <code>IncludePublic</code> parameter to <code>true</code>.</p> <p>The <code>IncludeShared</code> and <code>IncludePublic</code> parameters don't apply for <code>SnapshotType</code> values of <code>manual</code> or <code>automated</code>. The <code>IncludePublic</code> parameter doesn't apply when <code>SnapshotType</code> is set to <code>shared</code>. The <code>IncludeShared</code> parameter doesn't apply when <code>SnapshotType</code> is set to <code>public</code>.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous <code>DescribeDBClusterSnapshots</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>
            include_shared: <p>True to include shared manual DB cluster snapshots from other Amazon accounts that this Amazon account has been given permission to copy or restore, and otherwise false. The default is <code>false</code>.</p> <p>You can give an Amazon account permission to restore a manual DB cluster snapshot from another Amazon account by the <a>ModifyDBClusterSnapshotAttribute</a> API action.</p>
            include_public: <p>True to include manual DB cluster snapshots that are public and can be copied or restored by any Amazon account, and otherwise false. The default is <code>false</code>. The default is false.</p> <p>You can share a manual DB cluster snapshot as public by using the <a>ModifyDBClusterSnapshotAttribute</a> API action.</p>

        Raises:
            capo_neptune.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <i>DBClusterSnapshotIdentifier</i> does not refer to an existing DB cluster snapshot.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_db_cluster_snapshots_message.DescribeDBClusterSnapshotsMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_cluster_snapshot_message.DBClusterSnapshotMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_db_cluster_snapshots

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_db_cluster_snapshots.async_describe_db_cluster_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_db_cluster_snapshots_message.DescribeDBClusterSnapshotsMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if db_cluster_snapshot_identifier is not None:
            input_["db_cluster_snapshot_identifier"] = db_cluster_snapshot_identifier
        if snapshot_type is not None:
            input_["snapshot_type"] = snapshot_type
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if include_shared is not None:
            input_["include_shared"] = include_shared
        if include_public is not None:
            input_["include_public"] = include_public

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_db_cluster_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        snapshot_type: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
        include_shared: Optional["capo_neptune.types.boolean.Boolean"] = None,
        include_public: Optional["capo_neptune.types.boolean.Boolean"] = None,
    ) -> "AsyncIterator[capo_neptune.types.db_cluster_snapshot.DBClusterSnapshot]":
        _token = marker
        while True:
            _response = await self.describe_db_cluster_snapshots(
                config_overrides=config_overrides,
                db_cluster_identifier=db_cluster_identifier,
                db_cluster_snapshot_identifier=db_cluster_snapshot_identifier,
                snapshot_type=snapshot_type,
                filters=filters,
                max_records=max_records,
                marker=_token,
                include_shared=include_shared,
                include_public=include_public,
            )
            _page = _resolve_path(_response, ("db_cluster_snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_db_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        engine: Optional["capo_neptune.types.string.String"] = None,
        engine_version: Optional["capo_neptune.types.string.String"] = None,
        db_parameter_group_family: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
        default_only: Optional["capo_neptune.types.boolean.Boolean"] = None,
        list_supported_character_sets: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        list_supported_timezones: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_neptune.types.db_engine_version_message.DBEngineVersionMessage":
        """<p>Returns a list of the available DB engines.</p>

        Args:
            engine: <p>The database engine to return.</p>
            engine_version: <p>The database engine version to return.</p> <p>Example: <code>5.1.49</code> </p>
            db_parameter_group_family: <p>The name of a specific DB parameter group family to return details for.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match an existing DBParameterGroupFamily.</p> </li> </ul>
            filters: <p>Not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more than the <code>MaxRecords</code> value is available, a pagination token called a marker is included in the response so that the following results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>
            default_only: <p>Indicates that only the default version of the specified engine or engine and major version combination is returned.</p>
            list_supported_character_sets: <p>If this parameter is specified and the requested engine supports the <code>CharacterSetName</code> parameter for <code>CreateDBInstance</code>, the response includes a list of supported character sets for each engine version.</p>
            list_supported_timezones: <p>If this parameter is specified and the requested engine supports the <code>TimeZone</code> parameter for <code>CreateDBInstance</code>, the response includes a list of supported time zones for each engine version.</p>

        Raises:
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_db_engine_versions_message.DescribeDBEngineVersionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_engine_version_message.DBEngineVersionMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_db_engine_versions

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_db_engine_versions.async_describe_db_engine_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_db_engine_versions_message.DescribeDBEngineVersionsMessage = {}
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if db_parameter_group_family is not None:
            input_["db_parameter_group_family"] = db_parameter_group_family
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if default_only is not None:
            input_["default_only"] = default_only
        if list_supported_character_sets is not None:
            input_["list_supported_character_sets"] = list_supported_character_sets
        if list_supported_timezones is not None:
            input_["list_supported_timezones"] = list_supported_timezones

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_db_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        engine: Optional["capo_neptune.types.string.String"] = None,
        engine_version: Optional["capo_neptune.types.string.String"] = None,
        db_parameter_group_family: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
        default_only: Optional["capo_neptune.types.boolean.Boolean"] = None,
        list_supported_character_sets: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        list_supported_timezones: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "AsyncIterator[capo_neptune.types.db_engine_version.DBEngineVersion]":
        _token = marker
        while True:
            _response = await self.describe_db_engine_versions(
                config_overrides=config_overrides,
                engine=engine,
                engine_version=engine_version,
                db_parameter_group_family=db_parameter_group_family,
                filters=filters,
                max_records=max_records,
                marker=_token,
                default_only=default_only,
                list_supported_character_sets=list_supported_character_sets,
                list_supported_timezones=list_supported_timezones,
            )
            _page = _resolve_path(_response, ("db_engine_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_db_instances(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_instance_identifier: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.db_instance_message.DBInstanceMessage":
        """<p>Returns information about provisioned instances, and supports pagination.</p> <note> <p>This operation can also return information for Amazon RDS instances and Amazon DocDB instances.</p> </note>

        Args:
            db_instance_identifier: <p>The user-supplied instance identifier. If this parameter is specified, information from only the specific DB instance is returned. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the identifier of an existing DBInstance.</p> </li> </ul>
            filters: <p>A filter that specifies one or more DB instances to describe.</p> <p>Supported filters:</p> <ul> <li> <p> <code>db-cluster-id</code> - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB instances associated with the DB clusters identified by these ARNs.</p> </li> <li> <p> <code>engine</code> - Accepts an engine name (such as <code>neptune</code>), and restricts the results list to DB instances created by that engine.</p> </li> </ul> <p>For example, to invoke this API from the Amazon CLI and filter so that only Neptune DB instances are returned, you could use the following command:</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous <code>DescribeDBInstances</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <i>DBInstanceIdentifier</i> does not refer to an existing DB instance.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_db_instances_message.DescribeDBInstancesMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_instance_message.DBInstanceMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_db_instances

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_db_instances.async_describe_db_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_db_instances_message.DescribeDBInstancesMessage = {}
        if db_instance_identifier is not None:
            input_["db_instance_identifier"] = db_instance_identifier
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

    async def iter_describe_db_instances(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_instance_identifier: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.db_instance.DBInstance]":
        _token = marker
        while True:
            _response = await self.describe_db_instances(
                config_overrides=config_overrides,
                db_instance_identifier=db_instance_identifier,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("db_instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_db_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_parameter_group_name: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.db_parameter_groups_message.DBParameterGroupsMessage":
        """<p>Returns a list of <code>DBParameterGroup</code> descriptions. If a <code>DBParameterGroupName</code> is specified, the list will contain only the description of the specified DB parameter group.</p>

        Args:
            db_parameter_group_name: <p>The name of a specific DB parameter group to return details for.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBClusterParameterGroup.</p> </li> </ul>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous <code>DescribeDBParameterGroups</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_db_parameter_groups_message.DescribeDBParameterGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_parameter_groups_message.DBParameterGroupsMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_db_parameter_groups

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_db_parameter_groups.async_describe_db_parameter_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_db_parameter_groups_message.DescribeDBParameterGroupsMessage = {}
        if db_parameter_group_name is not None:
            input_["db_parameter_group_name"] = db_parameter_group_name
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

    async def iter_describe_db_parameter_groups(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_parameter_group_name: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.db_parameter_group.DBParameterGroup]":
        _token = marker
        while True:
            _response = await self.describe_db_parameter_groups(
                config_overrides=config_overrides,
                db_parameter_group_name=db_parameter_group_name,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("db_parameter_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_db_parameters(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_parameter_group_name: Optional["capo_neptune.types.string.String"] = None,
        source: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.db_parameter_group_details.DBParameterGroupDetails":
        """<p>Returns the detailed parameter list for a particular DB parameter group.</p>

        Args:
            db_parameter_group_name: <p>The name of a specific DB parameter group to return details for.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBParameterGroup.</p> </li> </ul>
            source: <p>The parameter types to return.</p> <p>Default: All parameter types returned</p> <p>Valid Values: <code>user | system | engine-default</code> </p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous <code>DescribeDBParameters</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_db_parameters_message.DescribeDBParametersMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_parameter_group_details.DBParameterGroupDetails"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_db_parameters

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_db_parameters.async_describe_db_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_db_parameters_message.DescribeDBParametersMessage = {}
        if db_parameter_group_name is not None:
            input_["db_parameter_group_name"] = db_parameter_group_name
        if source is not None:
            input_["source"] = source
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

    async def iter_describe_db_parameters(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_parameter_group_name: Optional["capo_neptune.types.string.String"] = None,
        source: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.parameter.Parameter]":
        _token = marker
        while True:
            _response = await self.describe_db_parameters(
                config_overrides=config_overrides,
                db_parameter_group_name=db_parameter_group_name,
                source=source,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("parameters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_db_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_subnet_group_name: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.db_subnet_group_message.DBSubnetGroupMessage":
        """<p>Returns a list of DBSubnetGroup descriptions. If a DBSubnetGroupName is specified, the list will contain only the descriptions of the specified DBSubnetGroup.</p> <p>For an overview of CIDR ranges, go to the <a href="http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">Wikipedia Tutorial</a>.</p>

        Args:
            db_subnet_group_name: <p>The name of the DB subnet group to return details for.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous DescribeDBSubnetGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_neptune.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <i>DBSubnetGroupName</i> does not refer to an existing DB subnet group.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_db_subnet_groups_message.DescribeDBSubnetGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_subnet_group_message.DBSubnetGroupMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_db_subnet_groups

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_db_subnet_groups.async_describe_db_subnet_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_db_subnet_groups_message.DescribeDBSubnetGroupsMessage = {}
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name
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

    async def iter_describe_db_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_subnet_group_name: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.db_subnet_group.DBSubnetGroup]":
        _token = marker
        while True:
            _response = await self.describe_db_subnet_groups(
                config_overrides=config_overrides,
                db_subnet_group_name=db_subnet_group_name,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("db_subnet_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_engine_default_cluster_parameters(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_parameter_group_family: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.describe_engine_default_cluster_parameters_result.DescribeEngineDefaultClusterParametersResult":
        """<p>Returns the default engine and system parameter information for the cluster database engine.</p>

        Args:
            db_parameter_group_family: <p>The name of the DB cluster parameter group family to return engine parameter information for.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous <code>DescribeEngineDefaultClusterParameters</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_engine_default_cluster_parameters_message.DescribeEngineDefaultClusterParametersMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.describe_engine_default_cluster_parameters_result.DescribeEngineDefaultClusterParametersResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_engine_default_cluster_parameters

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_engine_default_cluster_parameters.async_describe_engine_default_cluster_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_engine_default_cluster_parameters_message.DescribeEngineDefaultClusterParametersMessage = {}
        if db_parameter_group_family is not None:
            input_["db_parameter_group_family"] = db_parameter_group_family
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

    async def describe_engine_default_parameters(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_parameter_group_family: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.describe_engine_default_parameters_result.DescribeEngineDefaultParametersResult":
        """<p>Returns the default engine and system parameter information for the specified database engine.</p>

        Args:
            db_parameter_group_family: <p>The name of the DB parameter group family.</p>
            filters: <p>Not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous <code>DescribeEngineDefaultParameters</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_engine_default_parameters_message.DescribeEngineDefaultParametersMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.describe_engine_default_parameters_result.DescribeEngineDefaultParametersResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_engine_default_parameters

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_engine_default_parameters.async_describe_engine_default_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_engine_default_parameters_message.DescribeEngineDefaultParametersMessage = {}
        if db_parameter_group_family is not None:
            input_["db_parameter_group_family"] = db_parameter_group_family
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

    async def iter_describe_engine_default_parameters(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_parameter_group_family: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.parameter.Parameter]":
        _token = marker
        while True:
            _response = await self.describe_engine_default_parameters(
                config_overrides=config_overrides,
                db_parameter_group_family=db_parameter_group_family,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("engine_defaults", "parameters"))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("engine_defaults", "marker"))
            if not _token:
                break

    async def describe_event_categories(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        source_type: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
    ) -> "capo_neptune.types.event_categories_message.EventCategoriesMessage":
        """<p>Displays a list of categories for all event source types, or, if specified, for a specified source type.</p>

        Args:
            source_type: <p>The type of source that is generating the events.</p> <p>Valid values: db-instance | db-parameter-group | db-security-group | db-snapshot</p>
            filters: <p>This parameter is not currently supported.</p>

        Raises:
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_event_categories_message.DescribeEventCategoriesMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.event_categories_message.EventCategoriesMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_event_categories

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_event_categories.async_describe_event_categories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_event_categories_message.DescribeEventCategoriesMessage = {}
        if source_type is not None:
            input_["source_type"] = source_type
        if filters is not None:
            input_["filters"] = filters

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
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        source_identifier: Optional["capo_neptune.types.string.String"] = None,
        source_type: Optional["capo_neptune.types.source_type.SourceType"] = None,
        start_time: Optional["capo_neptune.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_neptune.types.t_stamp.TStamp"] = None,
        duration: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        event_categories: Optional[
            "capo_neptune.types.event_categories_list.EventCategoriesList"
        ] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.events_message.EventsMessage":
        """<p>Returns events related to DB instances, DB security groups, DB snapshots, and DB parameter groups for the past 14 days. Events specific to a particular DB instance, DB security group, database snapshot, or DB parameter group can be obtained by providing the name as a parameter. By default, the past hour of events are returned.</p>

        Args:
            source_identifier: <p>The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.</p> <p>Constraints:</p> <ul> <li> <p>If SourceIdentifier is supplied, SourceType must also be provided.</p> </li> <li> <p>If the source type is <code>DBInstance</code>, then a <code>DBInstanceIdentifier</code> must be supplied.</p> </li> <li> <p>If the source type is <code>DBSecurityGroup</code>, a <code>DBSecurityGroupName</code> must be supplied.</p> </li> <li> <p>If the source type is <code>DBParameterGroup</code>, a <code>DBParameterGroupName</code> must be supplied.</p> </li> <li> <p>If the source type is <code>DBSnapshot</code>, a <code>DBSnapshotIdentifier</code> must be supplied.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            source_type: <p>The event source to retrieve events for. If no value is specified, all events are returned.</p>
            start_time: <p> The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO8601 Wikipedia page.</a> </p> <p>Example: 2009-07-08T18:00Z</p>
            end_time: <p> The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the <a href="http://en.wikipedia.org/wiki/ISO_8601">ISO8601 Wikipedia page.</a> </p> <p>Example: 2009-07-08T18:00Z</p>
            duration: <p>The number of minutes to retrieve events for.</p> <p>Default: 60</p>
            event_categories: <p>A list of event categories that trigger notifications for a event notification subscription.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous DescribeEvents request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_events_message.DescribeEventsMessage]",
        ) -> AsyncOperationResponse["capo_neptune.types.events_message.EventsMessage"]:
            import capo_neptune._operations.amazon_rd_sv19.describe_events

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_events.async_describe_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_events_message.DescribeEventsMessage = {}
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
        if event_categories is not None:
            input_["event_categories"] = event_categories
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

    async def iter_describe_events(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        source_identifier: Optional["capo_neptune.types.string.String"] = None,
        source_type: Optional["capo_neptune.types.source_type.SourceType"] = None,
        start_time: Optional["capo_neptune.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_neptune.types.t_stamp.TStamp"] = None,
        duration: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        event_categories: Optional[
            "capo_neptune.types.event_categories_list.EventCategoriesList"
        ] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.event.Event]":
        _token = marker
        while True:
            _response = await self.describe_events(
                config_overrides=config_overrides,
                source_identifier=source_identifier,
                source_type=source_type,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                event_categories=event_categories,
                filters=filters,
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
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        subscription_name: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.event_subscriptions_message.EventSubscriptionsMessage":
        """<p>Lists all the subscription descriptions for a customer account. The description for a subscription includes SubscriptionName, SNSTopicARN, CustomerID, SourceType, SourceID, CreationTime, and Status.</p> <p>If you specify a SubscriptionName, lists the description for that subscription.</p>

        Args:
            subscription_name: <p>The name of the event notification subscription you want to describe.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code> .</p>

        Raises:
            capo_neptune.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>The designated subscription could not be found.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_event_subscriptions_message.DescribeEventSubscriptionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.event_subscriptions_message.EventSubscriptionsMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_event_subscriptions

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_event_subscriptions.async_describe_event_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_event_subscriptions_message.DescribeEventSubscriptionsMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
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

    async def iter_describe_event_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        subscription_name: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.event_subscription.EventSubscription]":
        _token = marker
        while True:
            _response = await self.describe_event_subscriptions(
                config_overrides=config_overrides,
                subscription_name=subscription_name,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("event_subscriptions_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_global_clusters(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.global_clusters_message.GlobalClustersMessage":
        """<p>Returns information about Neptune global database clusters. This API supports pagination.</p>

        Args:
            global_cluster_identifier: <p>The user-supplied DB cluster identifier. If this parameter is specified, only information about the specified DB cluster is returned. This parameter is not case-sensitive.</p> <p>Constraints: If supplied, must match an existing DB cluster identifier.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination marker token is included in the response that you can use to retrieve the remaining results.</p> <p>Default: <code>100</code> </p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>(<i>Optional</i>) A pagination token returned by a previous call to <code>DescribeGlobalClusters</code>. If this parameter is specified, the response will only include records beyond the marker, up to the number specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_neptune.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global database cluster. </p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_global_clusters_message.DescribeGlobalClustersMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.global_clusters_message.GlobalClustersMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_global_clusters

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_global_clusters.async_describe_global_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_global_clusters_message.DescribeGlobalClustersMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
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

    async def iter_describe_global_clusters(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.global_cluster.GlobalCluster]":
        _token = marker
        while True:
            _response = await self.describe_global_clusters(
                config_overrides=config_overrides,
                global_cluster_identifier=global_cluster_identifier,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("global_clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_orderable_db_instance_options(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        engine: Optional["capo_neptune.types.string.String"] = None,
        engine_version: Optional["capo_neptune.types.string.String"] = None,
        db_instance_class: Optional["capo_neptune.types.string.String"] = None,
        license_model: Optional["capo_neptune.types.string.String"] = None,
        vpc: Optional["capo_neptune.types.boolean_optional.BooleanOptional"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.orderable_db_instance_options_message.OrderableDBInstanceOptionsMessage":
        """<p>Returns a list of orderable DB instance options for the specified engine.</p>

        Args:
            engine: <p>The name of the engine to retrieve DB instance options for.</p>
            engine_version: <p>The engine version filter value. Specify this parameter to show only the available offerings matching the specified engine version.</p>
            db_instance_class: <p>The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.</p>
            license_model: <p>The license model filter value. Specify this parameter to show only the available offerings matching the specified license model.</p>
            vpc: <p>The VPC filter value. Specify this parameter to show only the available VPC or non-VPC offerings.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code> .</p>

        Raises:
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_orderable_db_instance_options_message.DescribeOrderableDBInstanceOptionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.orderable_db_instance_options_message.OrderableDBInstanceOptionsMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_orderable_db_instance_options

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_orderable_db_instance_options.async_describe_orderable_db_instance_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_orderable_db_instance_options_message.DescribeOrderableDBInstanceOptionsMessage = {}
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if db_instance_class is not None:
            input_["db_instance_class"] = db_instance_class
        if license_model is not None:
            input_["license_model"] = license_model
        if vpc is not None:
            input_["vpc"] = vpc
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

    async def iter_describe_orderable_db_instance_options(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        engine: Optional["capo_neptune.types.string.String"] = None,
        engine_version: Optional["capo_neptune.types.string.String"] = None,
        db_instance_class: Optional["capo_neptune.types.string.String"] = None,
        license_model: Optional["capo_neptune.types.string.String"] = None,
        vpc: Optional["capo_neptune.types.boolean_optional.BooleanOptional"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
    ) -> "AsyncIterator[capo_neptune.types.orderable_db_instance_option.OrderableDBInstanceOption]":
        _token = marker
        while True:
            _response = await self.describe_orderable_db_instance_options(
                config_overrides=config_overrides,
                engine=engine,
                engine_version=engine_version,
                db_instance_class=db_instance_class,
                license_model=license_model,
                vpc=vpc,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("orderable_db_instance_options",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_pending_maintenance_actions(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        resource_identifier: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_neptune.types.pending_maintenance_actions_message.PendingMaintenanceActionsMessage":
        """<p>Returns a list of resources (for example, DB instances) that have at least one pending maintenance action.</p>

        Args:
            resource_identifier: <p>The ARN of a resource to return pending maintenance actions for.</p>
            filters: <p>A filter that specifies one or more resources to return pending maintenance actions for.</p> <p>Supported filters:</p> <ul> <li> <p> <code>db-cluster-id</code> - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include pending maintenance actions for the DB clusters identified by these ARNs.</p> </li> <li> <p> <code>db-instance-id</code> - Accepts DB instance identifiers and DB instance ARNs. The results list will only include pending maintenance actions for the DB instances identified by these ARNs.</p> </li> </ul>
            marker: <p> An optional pagination token provided by a previous <code>DescribePendingMaintenanceActions</code> request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by <code>MaxRecords</code>.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>

        Raises:
            capo_neptune.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The specified resource ID was not found.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_pending_maintenance_actions_message.DescribePendingMaintenanceActionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.pending_maintenance_actions_message.PendingMaintenanceActionsMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_pending_maintenance_actions

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_pending_maintenance_actions.async_describe_pending_maintenance_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_pending_maintenance_actions_message.DescribePendingMaintenanceActionsMessage = {}
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
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

    async def iter_describe_pending_maintenance_actions(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        resource_identifier: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
        marker: Optional["capo_neptune.types.string.String"] = None,
        max_records: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_neptune.types.resource_pending_maintenance_actions.ResourcePendingMaintenanceActions]":
        _token = marker
        while True:
            _response = await self.describe_pending_maintenance_actions(
                config_overrides=config_overrides,
                resource_identifier=resource_identifier,
                filters=filters,
                marker=_token,
                max_records=max_records,
            )
            _page = _resolve_path(_response, ("pending_maintenance_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_valid_db_instance_modifications(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_instance_identifier: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.describe_valid_db_instance_modifications_result.DescribeValidDBInstanceModificationsResult":
        """<p>You can call <a>DescribeValidDBInstanceModifications</a> to learn what modifications you can make to your DB instance. You can use this information when you call <a>ModifyDBInstance</a>.</p>

        Args:
            db_instance_identifier: <p>The customer identifier or the ARN of your DB instance.</p>

        Raises:
            capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <i>DBInstanceIdentifier</i> does not refer to an existing DB instance.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.describe_valid_db_instance_modifications_message.DescribeValidDBInstanceModificationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.describe_valid_db_instance_modifications_result.DescribeValidDBInstanceModificationsResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.describe_valid_db_instance_modifications

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.describe_valid_db_instance_modifications.async_describe_valid_db_instance_modifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.describe_valid_db_instance_modifications_message.DescribeValidDBInstanceModificationsMessage = {}
        if db_instance_identifier is not None:
            input_["db_instance_identifier"] = db_instance_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def failover_db_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        target_db_instance_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
    ) -> "capo_neptune.types.failover_db_cluster_result.FailoverDBClusterResult":
        """<p>Forces a failover for a DB cluster.</p> <p>A failover for a DB cluster promotes one of the Read Replicas (read-only instances) in the DB cluster to be the primary instance (the cluster writer).</p> <p>Amazon Neptune will automatically fail over to a Read Replica, if one exists, when the primary instance fails. You can force a failover when you want to simulate a failure of a primary instance for testing. Because each instance in a DB cluster has its own endpoint address, you will need to clean up and re-establish any existing connections that use those endpoint addresses when the failover is complete.</p>

        Args:
            db_cluster_identifier: <p>A DB cluster identifier to force a failover for. This parameter is not case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBCluster.</p> </li> </ul>
            target_db_instance_identifier: <p>The name of the instance to promote to the primary instance.</p> <p>You must specify the instance identifier for an Read Replica in the DB cluster. For example, <code>mydbcluster-replica1</code>.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.failover_db_cluster_message.FailoverDBClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.failover_db_cluster_result.FailoverDBClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.failover_db_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.failover_db_cluster.async_failover_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.failover_db_cluster_message.FailoverDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if target_db_instance_identifier is not None:
            input_["target_db_instance_identifier"] = target_db_instance_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def failover_global_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        target_db_cluster_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        allow_data_loss: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        switchover: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> (
        "capo_neptune.types.failover_global_cluster_result.FailoverGlobalClusterResult"
    ):
        """<p>Initiates the failover process for a Neptune global database.</p> <p>A failover for a Neptune global database promotes one of secondary read-only DB clusters to be the primary DB cluster and demotes the primary DB cluster to being a secondary (read-only) DB cluster. In other words, the role of the current primary DB cluster and the selected target secondary DB cluster are switched. The selected secondary DB cluster assumes full read/write capabilities for the Neptune global database.</p> <note> <p>This action applies <b>only</b> to Neptune global databases. This action is only intended for use on healthy Neptune global databases with healthy Neptune DB clusters and no region-wide outages, to test disaster recovery scenarios or to reconfigure the global database topology.</p> </note>

        Args:
            global_cluster_identifier: <p>Identifier of the Neptune global database that should be failed over. The identifier is the unique key assigned by the user when the Neptune global database was created. In other words, it's the name of the global database that you want to fail over.</p> <p>Constraints: Must match the identifier of an existing Neptune global database.</p>
            target_db_cluster_identifier: <p>The Amazon Resource Name (ARN) of the secondary Neptune DB cluster that you want to promote to primary for the global database.</p>
            allow_data_loss: <p>Specifies whether to allow data loss for this global database cluster operation. Allowing data loss triggers a global failover operation.</p> <p>If you don't specify <code>AllowDataLoss</code>, the global database cluster operation defaults to a switchover.</p> <p>Constraints: Can't be specified together with the <code>Switchover</code> parameter.</p>
            switchover: <p>Specifies whether to switch over this global database cluster.</p> <p>Constraints: Can't be specified together with the <code>AllowDataLoss</code> parameter.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global database cluster. </p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The global cluster is in an invalid state and can't perform the requested operation. </p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.failover_global_cluster_message.FailoverGlobalClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.failover_global_cluster_result.FailoverGlobalClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.failover_global_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.failover_global_cluster.async_failover_global_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.failover_global_cluster_message.FailoverGlobalClusterMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if target_db_cluster_identifier is not None:
            input_["target_db_cluster_identifier"] = target_db_cluster_identifier
        if allow_data_loss is not None:
            input_["allow_data_loss"] = allow_data_loss
        if switchover is not None:
            input_["switchover"] = switchover

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
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        resource_name: Optional["capo_neptune.types.string.String"] = None,
        filters: Optional["capo_neptune.types.filter_list.FilterList"] = None,
    ) -> "capo_neptune.types.tag_list_message.TagListMessage":
        """<p>Lists all tags on an Amazon Neptune resource.</p>

        Args:
            resource_name: <p>The Amazon Neptune resource with tags to be listed. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href="https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing"> Constructing an Amazon Resource Name (ARN)</a>.</p>
            filters: <p>This parameter is not currently supported.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <i>DBInstanceIdentifier</i> does not refer to an existing DB instance.</p>
            capo_neptune.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault: <p> <i>DBSnapshotIdentifier</i> does not refer to an existing DB snapshot.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.list_tags_for_resource_message.ListTagsForResourceMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.tag_list_message.TagListMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.list_tags_for_resource_message.ListTagsForResourceMessage = {}
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_db_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        new_db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        apply_immediately: Optional["capo_neptune.types.boolean.Boolean"] = None,
        backup_retention_period: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_neptune.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        port: Optional["capo_neptune.types.integer_optional.IntegerOptional"] = None,
        master_user_password: Optional["capo_neptune.types.string.String"] = None,
        option_group_name: Optional["capo_neptune.types.string.String"] = None,
        preferred_backup_window: Optional["capo_neptune.types.string.String"] = None,
        preferred_maintenance_window: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        enable_iam_database_authentication: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        cloudwatch_logs_export_configuration: Optional[
            "capo_neptune.types.cloudwatch_logs_export_configuration.CloudwatchLogsExportConfiguration"
        ] = None,
        engine_version: Optional["capo_neptune.types.string.String"] = None,
        allow_major_version_upgrade: Optional[
            "capo_neptune.types.boolean.Boolean"
        ] = None,
        db_instance_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        deletion_protection: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        copy_tags_to_snapshot: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        serverless_v2_scaling_configuration: Optional[
            "capo_neptune.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
        ] = None,
        storage_type: Optional["capo_neptune.types.string.String"] = None,
        network_type: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.modify_db_cluster_result.ModifyDBClusterResult":
        """<p>Modify a setting for a DB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.</p>

        Args:
            db_cluster_identifier: <p>The DB cluster identifier for the cluster being modified. This parameter is not case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBCluster.</p> </li> </ul>
            new_db_cluster_identifier: <p>The new DB cluster identifier for the DB cluster when renaming a DB cluster. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens</p> </li> <li> <p>The first character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-cluster2</code> </p>
            apply_immediately: <p>A value that specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the DB cluster. If this parameter is set to <code>false</code>, changes to the DB cluster are applied during the next maintenance window.</p> <p>The <code>ApplyImmediately</code> parameter only affects <code>NewDBClusterIdentifier</code> values. If you set the <code>ApplyImmediately</code> parameter value to false, then changes to <code>NewDBClusterIdentifier</code> values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the <code>ApplyImmediately</code> parameter.</p> <p>Default: <code>false</code> </p>
            backup_retention_period: <p>The number of days for which automated backups are retained. You must specify a minimum value of 1.</p> <p>Default: 1</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 1 to 35</p> </li> </ul>
            db_cluster_parameter_group_name: <p>The name of the DB cluster parameter group to use for the DB cluster.</p>
            vpc_security_group_ids: <p>A list of VPC security groups that the DB cluster will belong to.</p>
            port: <p>The port number on which the DB cluster accepts connections.</p> <p>Constraints: Value must be <code>1150-65535</code> </p> <p>Default: The same port as the original DB cluster.</p>
            master_user_password: <p>Not supported by Neptune.</p>
            option_group_name: <p> <i>Not supported by Neptune.</i> </p>
            preferred_backup_window: <p>The daily time range during which automated backups are created if automated backups are enabled, using the <code>BackupRetentionPeriod</code> parameter.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>
            preferred_maintenance_window: <p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p>Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region, occurring on a random day of the week.</p> <p>Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.</p> <p>Constraints: Minimum 30-minute window.</p>
            enable_iam_database_authentication: <p>True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.</p> <p>Default: <code>false</code> </p>
            cloudwatch_logs_export_configuration: <p>The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB cluster. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html#cloudwatch-logs-cli">Using the CLI to publish Neptune audit logs to CloudWatch Logs</a>.</p>
            engine_version: <p>The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless the <code>ApplyImmediately</code> parameter is set to true.</p> <p>For a list of valid engine versions, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases.html">Engine Releases for Amazon Neptune</a>, or call <a>DescribeDBEngineVersions</a>.</p>
            allow_major_version_upgrade: <p>A value that indicates whether upgrades between different major versions are allowed.</p> <p>Constraints: You must set the allow-major-version-upgrade flag when providing an <code>EngineVersion</code> parameter that uses a different major version than the DB cluster's current version.</p>
            db_instance_parameter_group_name: <p>The name of the DB parameter group to apply to all instances of the DB cluster. </p> <note> <p>When you apply a parameter group using <code>DBInstanceParameterGroupName</code>, parameter changes aren't applied during the next maintenance window but instead are applied immediately.</p> </note> <p>Default: The existing name setting</p> <p>Constraints:</p> <ul> <li> <p>The DB parameter group must be in the same DB parameter group family as the target DB cluster version.</p> </li> <li> <p>The <code>DBInstanceParameterGroupName</code> parameter is only valid in combination with the <code>AllowMajorVersionUpgrade</code> parameter.</p> </li> </ul>
            deletion_protection: <p>A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.</p>
            copy_tags_to_snapshot: <p> <i>If set to <code>true</code>, tags are copied to any snapshot of the DB cluster that is created.</i> </p>
            serverless_v2_scaling_configuration: <p>Contains the scaling configuration of a Neptune Serverless DB cluster.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html">Using Amazon Neptune Serverless</a> in the <i>Amazon Neptune User Guide</i>.</p>
            storage_type: <p>The storage type to associate with the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <b> <code>standard</code> </b> – ( <i>the default</i> ) Configures cost-effective database storage for applications with moderate to small I/O usage.</p> </li> <li> <p> <b> <code>iopt1</code> </b> – Enables <a href="https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage">I/O-Optimized storage</a> that's designed to meet the needs of I/O-intensive graph workloads that require predictable pricing with low I/O latency and consistent I/O throughput.</p> <p>Neptune I/O-Optimized storage is only available starting with engine release 1.3.0.0.</p> </li> </ul>
            network_type: <p>The network type of the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <b> <code>IPV4</code> </b> – The DB cluster uses only IPv4 addresses for communication.</p> </li> <li> <p> <b> <code>DUAL</code> </b> – The DB cluster uses both IPv4 and IPv6 addresses for communication. The DB subnet group associated with the cluster must support IPv6.</p> </li> </ul>

        Raises:
            capo_neptune.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault: <p>User already has a DB cluster with the given identifier.</p>
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_cluster_parameter_group_not_found_fault.DBClusterParameterGroupNotFoundFault: <p> <i>DBClusterParameterGroupName</i> does not refer to an existing DB Cluster parameter group.</p>
            capo_neptune.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <i>DBSubnetGroupName</i> does not refer to an existing DB subnet group.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.invalid_db_security_group_state_fault.InvalidDBSecurityGroupStateFault: <p>The state of the DB security group does not allow deletion.</p>
            capo_neptune.errors.invalid_db_subnet_group_state_fault.InvalidDBSubnetGroupStateFault: <p>The DB subnet group cannot be deleted because it is in use.</p>
            capo_neptune.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.</p>
            capo_neptune.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>DB subnet group does not cover all Availability Zones after it is created because users' change.</p>
            capo_neptune.errors.network_type_not_supported_fault.NetworkTypeNotSupportedFault: <p>The specified <i>NetworkType</i> is not supported for the DB cluster, DB subnet group, or orderable DB instance option.</p>
            capo_neptune.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>Request would result in user exceeding the allowed amount of storage available across all DB instances.</p>
            capo_neptune.errors.storage_type_not_supported_fault.StorageTypeNotSupportedFault: <p> <i>StorageType</i> specified cannot be associated with the DB Instance.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.modify_db_cluster_message.ModifyDBClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.modify_db_cluster_result.ModifyDBClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.modify_db_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.modify_db_cluster.async_modify_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.modify_db_cluster_message.ModifyDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if new_db_cluster_identifier is not None:
            input_["new_db_cluster_identifier"] = new_db_cluster_identifier
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately
        if backup_retention_period is not None:
            input_["backup_retention_period"] = backup_retention_period
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if port is not None:
            input_["port"] = port
        if master_user_password is not None:
            input_["master_user_password"] = master_user_password
        if option_group_name is not None:
            input_["option_group_name"] = option_group_name
        if preferred_backup_window is not None:
            input_["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if enable_iam_database_authentication is not None:
            input_["enable_iam_database_authentication"] = (
                enable_iam_database_authentication
            )
        if cloudwatch_logs_export_configuration is not None:
            input_["cloudwatch_logs_export_configuration"] = (
                cloudwatch_logs_export_configuration
            )
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if allow_major_version_upgrade is not None:
            input_["allow_major_version_upgrade"] = allow_major_version_upgrade
        if db_instance_parameter_group_name is not None:
            input_["db_instance_parameter_group_name"] = (
                db_instance_parameter_group_name
            )
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if copy_tags_to_snapshot is not None:
            input_["copy_tags_to_snapshot"] = copy_tags_to_snapshot
        if serverless_v2_scaling_configuration is not None:
            input_["serverless_v2_scaling_configuration"] = (
                serverless_v2_scaling_configuration
            )
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if network_type is not None:
            input_["network_type"] = network_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_db_cluster_endpoint(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_endpoint_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        endpoint_type: Optional["capo_neptune.types.string.String"] = None,
        static_members: Optional["capo_neptune.types.string_list.StringList"] = None,
        excluded_members: Optional["capo_neptune.types.string_list.StringList"] = None,
    ) -> "capo_neptune.types.modify_db_cluster_endpoint_output.ModifyDBClusterEndpointOutput":
        """<p>Modifies the properties of an endpoint in an Amazon Neptune DB cluster.</p>

        Args:
            db_cluster_endpoint_identifier: <p>The identifier of the endpoint to modify. This parameter is stored as a lowercase string.</p>
            endpoint_type: <p>The type of the endpoint. One of: <code>READER</code>, <code>WRITER</code>, <code>ANY</code>.</p>
            static_members: <p>List of DB instance identifiers that are part of the custom endpoint group.</p>
            excluded_members: <p>List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.</p>

        Raises:
            capo_neptune.errors.db_cluster_endpoint_not_found_fault.DBClusterEndpointNotFoundFault: <p>The specified custom endpoint doesn't exist.</p>
            capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <i>DBInstanceIdentifier</i> does not refer to an existing DB instance.</p>
            capo_neptune.errors.invalid_db_cluster_endpoint_state_fault.InvalidDBClusterEndpointStateFault: <p>The requested operation cannot be performed on the endpoint while the endpoint is in this state.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.modify_db_cluster_endpoint_message.ModifyDBClusterEndpointMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.modify_db_cluster_endpoint_output.ModifyDBClusterEndpointOutput"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.modify_db_cluster_endpoint

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.modify_db_cluster_endpoint.async_modify_db_cluster_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.modify_db_cluster_endpoint_message.ModifyDBClusterEndpointMessage = {}
        if db_cluster_endpoint_identifier is not None:
            input_["db_cluster_endpoint_identifier"] = db_cluster_endpoint_identifier
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
        if static_members is not None:
            input_["static_members"] = static_members
        if excluded_members is not None:
            input_["excluded_members"] = excluded_members

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_db_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        parameters: Optional[
            "capo_neptune.types.parameters_list.ParametersList"
        ] = None,
    ) -> "capo_neptune.types.db_cluster_parameter_group_name_message.DBClusterParameterGroupNameMessage":
        """<p> Modifies the parameters of a DB cluster parameter group. To modify more than one parameter, submit a list of the following: <code>ParameterName</code>, <code>ParameterValue</code>, and <code>ApplyMethod</code>. A maximum of 20 parameters can be modified in a single request.</p> <note> <p>Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot without failover to the DB cluster associated with the parameter group before the change can take effect.</p> </note> <important> <p>After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the parameter group is used as the default for a new DB cluster. This is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the <code>character_set_database</code> parameter. You can use the <i>Parameter Groups</i> option of the Amazon Neptune console or the <a>DescribeDBClusterParameters</a> command to verify that your DB cluster parameter group has been created or modified.</p> </important>

        Args:
            db_cluster_parameter_group_name: <p>The name of the DB cluster parameter group to modify.</p>
            parameters: <p>A list of parameters in the DB cluster parameter group to modify.</p>

        Raises:
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.invalid_db_parameter_group_state_fault.InvalidDBParameterGroupStateFault: <p>The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you cannot delete it when the parameter group is in this state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.modify_db_cluster_parameter_group_message.ModifyDBClusterParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_cluster_parameter_group_name_message.DBClusterParameterGroupNameMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.modify_db_cluster_parameter_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.modify_db_cluster_parameter_group.async_modify_db_cluster_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.modify_db_cluster_parameter_group_message.ModifyDBClusterParameterGroupMessage = {}
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_db_cluster_snapshot_attribute(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        attribute_name: Optional["capo_neptune.types.string.String"] = None,
        values_to_add: Optional[
            "capo_neptune.types.attribute_value_list.AttributeValueList"
        ] = None,
        values_to_remove: Optional[
            "capo_neptune.types.attribute_value_list.AttributeValueList"
        ] = None,
    ) -> "capo_neptune.types.modify_db_cluster_snapshot_attribute_result.ModifyDBClusterSnapshotAttributeResult":
        """<p>Adds an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot.</p> <p>To share a manual DB cluster snapshot with other Amazon accounts, specify <code>restore</code> as the <code>AttributeName</code> and use the <code>ValuesToAdd</code> parameter to add a list of IDs of the Amazon accounts that are authorized to restore the manual DB cluster snapshot. Use the value <code>all</code> to make the manual DB cluster snapshot public, which means that it can be copied or restored by all Amazon accounts. Do not add the <code>all</code> value for any manual DB cluster snapshots that contain private information that you don't want available to all Amazon accounts. If a manual DB cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized Amazon account IDs for the <code>ValuesToAdd</code> parameter. You can't use <code>all</code> as a value for that parameter in this case.</p> <p>To view which Amazon accounts have access to copy or restore a manual DB cluster snapshot, or whether a manual DB cluster snapshot public or private, use the <a>DescribeDBClusterSnapshotAttributes</a> API action.</p>

        Args:
            db_cluster_snapshot_identifier: <p>The identifier for the DB cluster snapshot to modify the attributes for.</p>
            attribute_name: <p>The name of the DB cluster snapshot attribute to modify.</p> <p>To manage authorization for other Amazon accounts to copy or restore a manual DB cluster snapshot, set this value to <code>restore</code>.</p>
            values_to_add: <p>A list of DB cluster snapshot attributes to add to the attribute specified by <code>AttributeName</code>.</p> <p>To authorize other Amazon accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more Amazon account IDs, or <code>all</code> to make the manual DB cluster snapshot restorable by any Amazon account. Do not add the <code>all</code> value for any manual DB cluster snapshots that contain private information that you don't want available to all Amazon accounts.</p>
            values_to_remove: <p>A list of DB cluster snapshot attributes to remove from the attribute specified by <code>AttributeName</code>.</p> <p>To remove authorization for other Amazon accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more Amazon account identifiers, or <code>all</code> to remove authorization for any Amazon account to copy or restore the DB cluster snapshot. If you specify <code>all</code>, an Amazon account whose account ID is explicitly added to the <code>restore</code> attribute can still copy or restore a manual DB cluster snapshot.</p>

        Raises:
            capo_neptune.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <i>DBClusterSnapshotIdentifier</i> does not refer to an existing DB cluster snapshot.</p>
            capo_neptune.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The supplied value is not a valid DB cluster snapshot state.</p>
            capo_neptune.errors.shared_snapshot_quota_exceeded_fault.SharedSnapshotQuotaExceededFault: <p>You have exceeded the maximum number of accounts that you can share a manual DB snapshot with.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.modify_db_cluster_snapshot_attribute_message.ModifyDBClusterSnapshotAttributeMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.modify_db_cluster_snapshot_attribute_result.ModifyDBClusterSnapshotAttributeResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.modify_db_cluster_snapshot_attribute

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.modify_db_cluster_snapshot_attribute.async_modify_db_cluster_snapshot_attribute(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.modify_db_cluster_snapshot_attribute_message.ModifyDBClusterSnapshotAttributeMessage = {}
        if db_cluster_snapshot_identifier is not None:
            input_["db_cluster_snapshot_identifier"] = db_cluster_snapshot_identifier
        if attribute_name is not None:
            input_["attribute_name"] = attribute_name
        if values_to_add is not None:
            input_["values_to_add"] = values_to_add
        if values_to_remove is not None:
            input_["values_to_remove"] = values_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_db_instance(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_instance_identifier: Optional["capo_neptune.types.string.String"] = None,
        allocated_storage: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        db_instance_class: Optional["capo_neptune.types.string.String"] = None,
        db_subnet_group_name: Optional["capo_neptune.types.string.String"] = None,
        db_security_groups: Optional[
            "capo_neptune.types.db_security_group_name_list.DBSecurityGroupNameList"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_neptune.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        apply_immediately: Optional["capo_neptune.types.boolean.Boolean"] = None,
        master_user_password: Optional["capo_neptune.types.string.String"] = None,
        db_parameter_group_name: Optional["capo_neptune.types.string.String"] = None,
        backup_retention_period: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        preferred_backup_window: Optional["capo_neptune.types.string.String"] = None,
        preferred_maintenance_window: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        multi_az: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        engine_version: Optional["capo_neptune.types.string.String"] = None,
        allow_major_version_upgrade: Optional[
            "capo_neptune.types.boolean.Boolean"
        ] = None,
        auto_minor_version_upgrade: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        license_model: Optional["capo_neptune.types.string.String"] = None,
        iops: Optional["capo_neptune.types.integer_optional.IntegerOptional"] = None,
        option_group_name: Optional["capo_neptune.types.string.String"] = None,
        new_db_instance_identifier: Optional["capo_neptune.types.string.String"] = None,
        storage_type: Optional["capo_neptune.types.string.String"] = None,
        tde_credential_arn: Optional["capo_neptune.types.string.String"] = None,
        tde_credential_password: Optional[
            "capo_neptune.types.sensitive_string.SensitiveString"
        ] = None,
        ca_certificate_identifier: Optional["capo_neptune.types.string.String"] = None,
        domain: Optional["capo_neptune.types.string.String"] = None,
        copy_tags_to_snapshot: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        monitoring_interval: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        db_port_number: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        publicly_accessible: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        monitoring_role_arn: Optional["capo_neptune.types.string.String"] = None,
        domain_iam_role_name: Optional["capo_neptune.types.string.String"] = None,
        promotion_tier: Optional[
            "capo_neptune.types.integer_optional.IntegerOptional"
        ] = None,
        enable_iam_database_authentication: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        enable_performance_insights: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        performance_insights_kms_key_id: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        cloudwatch_logs_export_configuration: Optional[
            "capo_neptune.types.cloudwatch_logs_export_configuration.CloudwatchLogsExportConfiguration"
        ] = None,
        deletion_protection: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_neptune.types.modify_db_instance_result.ModifyDBInstanceResult":
        """<p>Modifies settings for a DB instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. To learn what modifications you can make to your DB instance, call <a>DescribeValidDBInstanceModifications</a> before you call <a>ModifyDBInstance</a>.</p>

        Args:
            db_instance_identifier: <p>The DB instance identifier. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBInstance.</p> </li> </ul>
            allocated_storage: <p>Not supported by Neptune.</p>
            db_instance_class: <p>The new compute and memory capacity of the DB instance, for example, <code>db.m4.large</code>. Not all DB instance classes are available in all Amazon Regions.</p> <p>If you modify the DB instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless <code>ApplyImmediately</code> is specified as <code>true</code> for this request.</p> <p>Default: Uses existing setting</p>
            db_subnet_group_name: <p>The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC.</p> <p>Changing the subnet group causes an outage during the change. The change is applied during the next maintenance window, unless you specify <code>true</code> for the <code>ApplyImmediately</code> parameter.</p> <p>Constraints: If supplied, must match the name of an existing DBSubnetGroup.</p> <p>Example: <code>mySubnetGroup</code> </p>
            db_security_groups: <p>A list of DB security groups to authorize on this DB instance. Changing this setting doesn't result in an outage and the change is asynchronously applied as soon as possible.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match existing DBSecurityGroups.</p> </li> </ul>
            vpc_security_group_ids: <p>A list of EC2 VPC security groups to authorize on this DB instance. This change is asynchronously applied as soon as possible.</p> <p>Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see <a>ModifyDBCluster</a>.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match existing VpcSecurityGroupIds.</p> </li> </ul>
            apply_immediately: <p>Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the DB instance.</p> <p> If this parameter is set to <code>false</code>, changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next call to <a>RebootDBInstance</a>, or the next failure reboot.</p> <p>Default: <code>false</code> </p>
            master_user_password: <p>Not supported by Neptune.</p>
            db_parameter_group_name: <p>The name of the DB parameter group to apply to the DB instance. Changing this setting doesn't result in an outage. The parameter group name itself is changed immediately, but the actual parameter changes are not applied until you reboot the instance without failover. The db instance will NOT be rebooted automatically and the parameter changes will NOT be applied during the next maintenance window.</p> <p>Default: Uses existing setting</p> <p>Constraints: The DB parameter group must be in the same DB parameter group family as this DB instance.</p>
            backup_retention_period: <p>Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see <a>ModifyDBCluster</a>.</p> <p>Default: Uses existing setting</p>
            preferred_backup_window: <p> The daily time range during which automated backups are created if automated backups are enabled.</p> <p>Not applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see <a>ModifyDBCluster</a>.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format hh24:mi-hh24:mi</p> </li> <li> <p>Must be in Universal Time Coordinated (UTC)</p> </li> <li> <p>Must not conflict with the preferred maintenance window</p> </li> <li> <p>Must be at least 30 minutes</p> </li> </ul>
            preferred_maintenance_window: <p>The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesn't result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, then changing this parameter will cause a reboot of the DB instance. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.</p> <p>Default: Uses existing setting</p> <p>Format: ddd:hh24:mi-ddd:hh24:mi</p> <p>Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun</p> <p>Constraints: Must be at least 30 minutes</p>
            multi_az: <p>Specifies if the DB instance is a Multi-AZ deployment. Changing this parameter doesn't result in an outage and the change is applied during the next maintenance window unless the <code>ApplyImmediately</code> parameter is set to <code>true</code> for this request.</p>
            engine_version: <p>The version number of the database engine to upgrade to. Currently, setting this parameter has no effect. To upgrade your database engine to the most recent release, use the <a>ApplyPendingMaintenanceAction</a> API.</p>
            allow_major_version_upgrade: <p>Indicates that major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.</p>
            auto_minor_version_upgrade: <p> Indicates that minor version upgrades are applied automatically to the DB instance during the maintenance window. Changing this parameter doesn't result in an outage except in the following case and the change is asynchronously applied as soon as possible. An outage will result if this parameter is set to <code>true</code> during the maintenance window, and a newer minor version is available, and Neptune has enabled auto patching for that engine version.</p>
            license_model: <p>Not supported by Neptune.</p>
            iops: <p>The new Provisioned IOPS (I/O operations per second) value for the instance.</p> <p>Changing this setting doesn't result in an outage and the change is applied during the next maintenance window unless the <code>ApplyImmediately</code> parameter is set to <code>true</code> for this request.</p> <p>Default: Uses existing setting</p>
            option_group_name: <p> <i>(Not supported by Neptune)</i> </p>
            new_db_instance_identifier: <p> The new DB instance identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot will occur immediately if you set <code>Apply Immediately</code> to true, or will occur during the next maintenance window if <code>Apply Immediately</code> to false. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>mydbinstance</code> </p>
            storage_type: <p>Not applicable. In Neptune the storage type is managed at the DB Cluster level.</p>
            tde_credential_arn: <p>The ARN from the key store with which to associate the instance for TDE encryption.</p>
            tde_credential_password: <p>The password for the given ARN from the key store in order to access the device.</p>
            ca_certificate_identifier: <p>Indicates the certificate that needs to be associated with the instance.</p>
            domain: <p>Not supported.</p>
            copy_tags_to_snapshot: <p>True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.</p>
            monitoring_interval: <p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.</p> <p>If <code>MonitoringRoleArn</code> is specified, then you must also set <code>MonitoringInterval</code> to a value other than 0.</p> <p>Valid Values: <code>0, 1, 5, 10, 15, 30, 60</code> </p>
            db_port_number: <p>The port number on which the database accepts connections.</p> <p>The value of the <code>DBPortNumber</code> parameter must not match any of the port values specified for options in the option group for the DB instance.</p> <p>Your database will restart when you change the <code>DBPortNumber</code> value regardless of the value of the <code>ApplyImmediately</code> parameter.</p> <p> Default: <code>8182</code> </p>
            publicly_accessible: <p>Indicates whether the DB instance is publicly accessible.</p> <p>When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.</p> <p>When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.</p>
            monitoring_role_arn: <p>The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, <code>arn:aws:iam:123456789012:role/emaccess</code>.</p> <p>If <code>MonitoringInterval</code> is set to a value other than 0, then you must supply a <code>MonitoringRoleArn</code> value.</p>
            domain_iam_role_name: <p>Not supported</p>
            promotion_tier: <p>A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.</p> <p>Default: 1</p> <p>Valid Values: 0 - 15</p>
            enable_iam_database_authentication: <p>True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.</p> <p>You can enable IAM database authentication for the following database engines</p> <p>Not applicable. Mapping Amazon IAM accounts to database accounts is managed by the DB cluster. For more information, see <a>ModifyDBCluster</a>.</p> <p>Default: <code>false</code> </p>
            enable_performance_insights: <p> <i>(Not supported by Neptune)</i> </p>
            performance_insights_kms_key_id: <p> <i>(Not supported by Neptune)</i> </p>
            cloudwatch_logs_export_configuration: <p>The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB instance or DB cluster.</p>
            deletion_protection: <p>A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-delete.html">Deleting a DB Instance</a>.</p>

        Raises:
            capo_neptune.errors.authorization_not_found_fault.AuthorizationNotFoundFault: <p>Specified CIDRIP or EC2 security group is not authorized for the specified DB security group.</p> <p>Neptune may not also be authorized via IAM to perform necessary actions on your behalf.</p>
            capo_neptune.errors.certificate_not_found_fault.CertificateNotFoundFault: <p> <i>CertificateIdentifier</i> does not refer to an existing certificate.</p>
            capo_neptune.errors.db_instance_already_exists_fault.DBInstanceAlreadyExistsFault: <p>User already has a DB instance with the given identifier.</p>
            capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <i>DBInstanceIdentifier</i> does not refer to an existing DB instance.</p>
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.db_security_group_not_found_fault.DBSecurityGroupNotFoundFault: <p> <i>DBSecurityGroupName</i> does not refer to an existing DB security group.</p>
            capo_neptune.errors.db_upgrade_dependency_failure_fault.DBUpgradeDependencyFailureFault: <p>The DB upgrade failed because a resource the DB depends on could not be modified.</p>
            capo_neptune.errors.domain_not_found_fault.DomainNotFoundFault: <p> <i>Domain</i> does not refer to an existing Active Directory Domain.</p>
            capo_neptune.errors.insufficient_db_instance_capacity_fault.InsufficientDBInstanceCapacityFault: <p>Specified DB instance class is not available in the specified Availability Zone.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.invalid_db_security_group_state_fault.InvalidDBSecurityGroupStateFault: <p>The state of the DB security group does not allow deletion.</p>
            capo_neptune.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>DB subnet group does not cover all Availability Zones after it is created because users' change.</p>
            capo_neptune.errors.option_group_not_found_fault.OptionGroupNotFoundFault: <p>The designated option group could not be found.</p>
            capo_neptune.errors.provisioned_iops_not_available_in_az_fault.ProvisionedIopsNotAvailableInAZFault: <p>Provisioned IOPS not available in the specified Availability Zone.</p>
            capo_neptune.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>Request would result in user exceeding the allowed amount of storage available across all DB instances.</p>
            capo_neptune.errors.storage_type_not_supported_fault.StorageTypeNotSupportedFault: <p> <i>StorageType</i> specified cannot be associated with the DB Instance.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.modify_db_instance_message.ModifyDBInstanceMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.modify_db_instance_result.ModifyDBInstanceResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.modify_db_instance

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.modify_db_instance.async_modify_db_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.modify_db_instance_message.ModifyDBInstanceMessage = {}
        if db_instance_identifier is not None:
            input_["db_instance_identifier"] = db_instance_identifier
        if allocated_storage is not None:
            input_["allocated_storage"] = allocated_storage
        if db_instance_class is not None:
            input_["db_instance_class"] = db_instance_class
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name
        if db_security_groups is not None:
            input_["db_security_groups"] = db_security_groups
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately
        if master_user_password is not None:
            input_["master_user_password"] = master_user_password
        if db_parameter_group_name is not None:
            input_["db_parameter_group_name"] = db_parameter_group_name
        if backup_retention_period is not None:
            input_["backup_retention_period"] = backup_retention_period
        if preferred_backup_window is not None:
            input_["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if multi_az is not None:
            input_["multi_az"] = multi_az
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if allow_major_version_upgrade is not None:
            input_["allow_major_version_upgrade"] = allow_major_version_upgrade
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if license_model is not None:
            input_["license_model"] = license_model
        if iops is not None:
            input_["iops"] = iops
        if option_group_name is not None:
            input_["option_group_name"] = option_group_name
        if new_db_instance_identifier is not None:
            input_["new_db_instance_identifier"] = new_db_instance_identifier
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if tde_credential_arn is not None:
            input_["tde_credential_arn"] = tde_credential_arn
        if tde_credential_password is not None:
            input_["tde_credential_password"] = tde_credential_password
        if ca_certificate_identifier is not None:
            input_["ca_certificate_identifier"] = ca_certificate_identifier
        if domain is not None:
            input_["domain"] = domain
        if copy_tags_to_snapshot is not None:
            input_["copy_tags_to_snapshot"] = copy_tags_to_snapshot
        if monitoring_interval is not None:
            input_["monitoring_interval"] = monitoring_interval
        if db_port_number is not None:
            input_["db_port_number"] = db_port_number
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if monitoring_role_arn is not None:
            input_["monitoring_role_arn"] = monitoring_role_arn
        if domain_iam_role_name is not None:
            input_["domain_iam_role_name"] = domain_iam_role_name
        if promotion_tier is not None:
            input_["promotion_tier"] = promotion_tier
        if enable_iam_database_authentication is not None:
            input_["enable_iam_database_authentication"] = (
                enable_iam_database_authentication
            )
        if enable_performance_insights is not None:
            input_["enable_performance_insights"] = enable_performance_insights
        if performance_insights_kms_key_id is not None:
            input_["performance_insights_kms_key_id"] = performance_insights_kms_key_id
        if cloudwatch_logs_export_configuration is not None:
            input_["cloudwatch_logs_export_configuration"] = (
                cloudwatch_logs_export_configuration
            )
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_db_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_parameter_group_name: Optional["capo_neptune.types.string.String"] = None,
        parameters: Optional[
            "capo_neptune.types.parameters_list.ParametersList"
        ] = None,
    ) -> (
        "capo_neptune.types.db_parameter_group_name_message.DBParameterGroupNameMessage"
    ):
        """<p>Modifies the parameters of a DB parameter group. To modify more than one parameter, submit a list of the following: <code>ParameterName</code>, <code>ParameterValue</code>, and <code>ApplyMethod</code>. A maximum of 20 parameters can be modified in a single request.</p> <note> <p>Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot without failover to the DB instance associated with the parameter group before the change can take effect.</p> </note> <important> <p>After you modify a DB parameter group, you should wait at least 5 minutes before creating your first DB instance that uses that DB parameter group as the default parameter group. This allows Amazon Neptune to fully complete the modify action before the parameter group is used as the default for a new DB instance. This is especially important for parameters that are critical when creating the default database for a DB instance, such as the character set for the default database defined by the <code>character_set_database</code> parameter. You can use the <i>Parameter Groups</i> option of the Amazon Neptune console or the <i>DescribeDBParameters</i> command to verify that your DB parameter group has been created or modified.</p> </important>

        Args:
            db_parameter_group_name: <p>The name of the DB parameter group.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBParameterGroup.</p> </li> </ul>
            parameters: <p>An array of parameter names, values, and the apply method for the parameter update. At least one parameter name, value, and apply method must be supplied; subsequent arguments are optional. A maximum of 20 parameters can be modified in a single request.</p> <p>Valid Values (for the application method): <code>immediate | pending-reboot</code> </p> <note> <p>You can use the immediate value with dynamic parameters only. You can use the pending-reboot value for both dynamic and static parameters, and changes are applied when you reboot the DB instance without failover.</p> </note>

        Raises:
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.invalid_db_parameter_group_state_fault.InvalidDBParameterGroupStateFault: <p>The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you cannot delete it when the parameter group is in this state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.modify_db_parameter_group_message.ModifyDBParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_parameter_group_name_message.DBParameterGroupNameMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.modify_db_parameter_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.modify_db_parameter_group.async_modify_db_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.modify_db_parameter_group_message.ModifyDBParameterGroupMessage = {}
        if db_parameter_group_name is not None:
            input_["db_parameter_group_name"] = db_parameter_group_name
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_db_subnet_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_subnet_group_name: Optional["capo_neptune.types.string.String"] = None,
        db_subnet_group_description: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        subnet_ids: Optional[
            "capo_neptune.types.subnet_identifier_list.SubnetIdentifierList"
        ] = None,
    ) -> "capo_neptune.types.modify_db_subnet_group_result.ModifyDBSubnetGroupResult":
        """<p>Modifies an existing DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the Amazon Region.</p>

        Args:
            db_subnet_group_name: <p>The name for the DB subnet group. This value is stored as a lowercase string. You can't modify the default subnet group.</p> <p>Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>
            db_subnet_group_description: <p>The description for the DB subnet group.</p>
            subnet_ids: <p>The EC2 subnet IDs for the DB subnet group.</p>

        Raises:
            capo_neptune.errors.db_subnet_group_does_not_cover_enough_a_zs.DBSubnetGroupDoesNotCoverEnoughAZs: <p>Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.</p>
            capo_neptune.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <i>DBSubnetGroupName</i> does not refer to an existing DB subnet group.</p>
            capo_neptune.errors.db_subnet_quota_exceeded_fault.DBSubnetQuotaExceededFault: <p>Request would result in user exceeding the allowed number of subnets in a DB subnet groups.</p>
            capo_neptune.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.</p>
            capo_neptune.errors.subnet_already_in_use.SubnetAlreadyInUse: <p>The DB subnet is already in use in the Availability Zone.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.modify_db_subnet_group_message.ModifyDBSubnetGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.modify_db_subnet_group_result.ModifyDBSubnetGroupResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.modify_db_subnet_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.modify_db_subnet_group.async_modify_db_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.modify_db_subnet_group_message.ModifyDBSubnetGroupMessage = {}
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name
        if db_subnet_group_description is not None:
            input_["db_subnet_group_description"] = db_subnet_group_description
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids

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
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        subscription_name: Optional["capo_neptune.types.string.String"] = None,
        sns_topic_arn: Optional["capo_neptune.types.string.String"] = None,
        source_type: Optional["capo_neptune.types.string.String"] = None,
        event_categories: Optional[
            "capo_neptune.types.event_categories_list.EventCategoriesList"
        ] = None,
        enabled: Optional["capo_neptune.types.boolean_optional.BooleanOptional"] = None,
    ) -> "capo_neptune.types.modify_event_subscription_result.ModifyEventSubscriptionResult":
        """<p>Modifies an existing event notification subscription. Note that you can't modify the source identifiers using this call; to change source identifiers for a subscription, use the <a>AddSourceIdentifierToSubscription</a> and <a>RemoveSourceIdentifierFromSubscription</a> calls.</p> <p>You can see a list of the event categories for a given SourceType by using the <b>DescribeEventCategories</b> action.</p>

        Args:
            subscription_name: <p>The name of the event notification subscription.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.</p>
            source_type: <p>The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.</p> <p>Valid values: db-instance | db-parameter-group | db-security-group | db-snapshot</p>
            event_categories: <p> A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType by using the <b>DescribeEventCategories</b> action.</p>
            enabled: <p> A Boolean value; set to <b>true</b> to activate the subscription.</p>

        Raises:
            capo_neptune.errors.event_subscription_quota_exceeded_fault.EventSubscriptionQuotaExceededFault: <p>You have exceeded the number of events you can subscribe to.</p>
            capo_neptune.errors.sns_invalid_topic_fault.SNSInvalidTopicFault: <p>The SNS topic is invalid.</p>
            capo_neptune.errors.sns_no_authorization_fault.SNSNoAuthorizationFault: <p>There is no SNS authorization.</p>
            capo_neptune.errors.sns_topic_arn_not_found_fault.SNSTopicArnNotFoundFault: <p>The ARN of the SNS topic could not be found.</p>
            capo_neptune.errors.subscription_category_not_found_fault.SubscriptionCategoryNotFoundFault: <p>The designated subscription category could not be found.</p>
            capo_neptune.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>The designated subscription could not be found.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.modify_event_subscription_message.ModifyEventSubscriptionMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.modify_event_subscription_result.ModifyEventSubscriptionResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.modify_event_subscription

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.modify_event_subscription.async_modify_event_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.modify_event_subscription_message.ModifyEventSubscriptionMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if source_type is not None:
            input_["source_type"] = source_type
        if event_categories is not None:
            input_["event_categories"] = event_categories
        if enabled is not None:
            input_["enabled"] = enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_global_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        new_global_cluster_identifier: Optional[
            "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        deletion_protection: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        engine_version: Optional["capo_neptune.types.string.String"] = None,
        allow_major_version_upgrade: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_neptune.types.modify_global_cluster_result.ModifyGlobalClusterResult":
        """<p>Modify a setting for an Amazon Neptune global cluster. You can change one or more database configuration parameters by specifying these parameters and their new values in the request.</p>

        Args:
            global_cluster_identifier: <p>The DB cluster identifier for the global cluster being modified. This parameter is not case-sensitive.</p> <p>Constraints: Must match the identifier of an existing global database cluster.</p>
            new_global_cluster_identifier: <p>A new cluster identifier to assign to the global database. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-cluster2</code> </p>
            deletion_protection: <p>Indicates whether the global database has deletion protection enabled. The global database cannot be deleted when deletion protection is enabled.</p>
            engine_version: <p>The version number of the database engine to which you want to upgrade. Changing this parameter will result in an outage. The change is applied during the next maintenance window unless <code>ApplyImmediately</code> is enabled.</p> <p>To list all of the available Neptune engine versions, use the following command:</p>
            allow_major_version_upgrade: <p>A value that indicates whether major version upgrades are allowed.</p> <p>Constraints: You must allow major version upgrades if you specify a value for the <code>EngineVersion</code> parameter that is a different major version than the DB cluster's current version.</p> <p>If you upgrade the major version of a global database, the cluster and DB instance parameter groups are set to the default parameter groups for the new version, so you will need to apply any custom parameter groups after completing the upgrade.</p>

        Raises:
            capo_neptune.errors.global_cluster_already_exists_fault.GlobalClusterAlreadyExistsFault: <p>The <code>GlobalClusterIdentifier</code> already exists. Choose a new global database identifier (unique name) to create a new global database cluster.</p>
            capo_neptune.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global database cluster. </p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The global cluster is in an invalid state and can't perform the requested operation. </p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.modify_global_cluster_message.ModifyGlobalClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.modify_global_cluster_result.ModifyGlobalClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.modify_global_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.modify_global_cluster.async_modify_global_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.modify_global_cluster_message.ModifyGlobalClusterMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if new_global_cluster_identifier is not None:
            input_["new_global_cluster_identifier"] = new_global_cluster_identifier
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if allow_major_version_upgrade is not None:
            input_["allow_major_version_upgrade"] = allow_major_version_upgrade

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def promote_read_replica_db_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.promote_read_replica_db_cluster_result.PromoteReadReplicaDBClusterResult":
        """<p>Not supported.</p>

        Args:
            db_cluster_identifier: <p>Not supported.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.promote_read_replica_db_cluster_message.PromoteReadReplicaDBClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.promote_read_replica_db_cluster_result.PromoteReadReplicaDBClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.promote_read_replica_db_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.promote_read_replica_db_cluster.async_promote_read_replica_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.promote_read_replica_db_cluster_message.PromoteReadReplicaDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reboot_db_instance(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_instance_identifier: Optional["capo_neptune.types.string.String"] = None,
        force_failover: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_neptune.types.reboot_db_instance_result.RebootDBInstanceResult":
        """<p>You might need to reboot your DB instance, usually for maintenance reasons. For example, if you make certain modifications, or if you change the DB parameter group associated with the DB instance, you must reboot the instance for the changes to take effect.</p> <p>Rebooting a DB instance restarts the database engine service. Rebooting a DB instance results in a momentary outage, during which the DB instance status is set to rebooting.</p>

        Args:
            db_instance_identifier: <p>The DB instance identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBInstance.</p> </li> </ul>
            force_failover: <p> When <code>true</code>, the reboot is conducted through a MultiAZ failover.</p> <p>Constraint: You can't specify <code>true</code> if the instance is not configured for MultiAZ.</p>

        Raises:
            capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <i>DBInstanceIdentifier</i> does not refer to an existing DB instance.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.reboot_db_instance_message.RebootDBInstanceMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.reboot_db_instance_result.RebootDBInstanceResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.reboot_db_instance

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.reboot_db_instance.async_reboot_db_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.reboot_db_instance_message.RebootDBInstanceMessage = {}
        if db_instance_identifier is not None:
            input_["db_instance_identifier"] = db_instance_identifier
        if force_failover is not None:
            input_["force_failover"] = force_failover

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_from_global_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.remove_from_global_cluster_result.RemoveFromGlobalClusterResult":
        """<p>Detaches a Neptune DB cluster from a Neptune global database. A secondary cluster becomes a normal standalone cluster with read-write capability instead of being read-only, and no longer receives data from the primary cluster.</p>

        Args:
            global_cluster_identifier: <p>The identifier of the Neptune global database from which to detach the specified Neptune DB cluster.</p>
            db_cluster_identifier: <p>The Amazon Resource Name (ARN) identifying the cluster to be detached from the Neptune global database cluster.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global database cluster. </p>
            capo_neptune.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The global cluster is in an invalid state and can't perform the requested operation. </p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.remove_from_global_cluster_message.RemoveFromGlobalClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.remove_from_global_cluster_result.RemoveFromGlobalClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.remove_from_global_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.remove_from_global_cluster.async_remove_from_global_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.remove_from_global_cluster_message.RemoveFromGlobalClusterMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_role_from_db_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        role_arn: Optional["capo_neptune.types.string.String"] = None,
        feature_name: Optional["capo_neptune.types.string.String"] = None,
    ) -> None:
        """<p>Disassociates an Identity and Access Management (IAM) role from a DB cluster.</p>

        Args:
            db_cluster_identifier: <p>The name of the DB cluster to disassociate the IAM role from.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to disassociate from the DB cluster, for example <code>arn:aws:iam::123456789012:role/NeptuneAccessRole</code>.</p>
            feature_name: <p>The name of the feature for the DB cluster that the IAM role is to be disassociated from. For the list of supported feature names, see <a>DescribeDBEngineVersions</a>.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_cluster_role_not_found_fault.DBClusterRoleNotFoundFault: <p>The specified IAM role Amazon Resource Name (ARN) is not associated with the specified DB cluster.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.remove_role_from_db_cluster_message.RemoveRoleFromDBClusterMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_neptune._operations.amazon_rd_sv19.remove_role_from_db_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.remove_role_from_db_cluster.async_remove_role_from_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.remove_role_from_db_cluster_message.RemoveRoleFromDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if feature_name is not None:
            input_["feature_name"] = feature_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_source_identifier_from_subscription(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        subscription_name: Optional["capo_neptune.types.string.String"] = None,
        source_identifier: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.remove_source_identifier_from_subscription_result.RemoveSourceIdentifierFromSubscriptionResult":
        """<p>Removes a source identifier from an existing event notification subscription.</p>

        Args:
            subscription_name: <p>The name of the event notification subscription you want to remove a source identifier from.</p>
            source_identifier: <p> The source identifier to be removed from the subscription, such as the <b>DB instance identifier</b> for a DB instance or the name of a security group.</p>

        Raises:
            capo_neptune.errors.source_not_found_fault.SourceNotFoundFault: <p>The source could not be found.</p>
            capo_neptune.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>The designated subscription could not be found.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.remove_source_identifier_from_subscription_message.RemoveSourceIdentifierFromSubscriptionMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.remove_source_identifier_from_subscription_result.RemoveSourceIdentifierFromSubscriptionResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.remove_source_identifier_from_subscription

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.remove_source_identifier_from_subscription.async_remove_source_identifier_from_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.remove_source_identifier_from_subscription_message.RemoveSourceIdentifierFromSubscriptionMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if source_identifier is not None:
            input_["source_identifier"] = source_identifier

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
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        resource_name: Optional["capo_neptune.types.string.String"] = None,
        tag_keys: Optional["capo_neptune.types.key_list.KeyList"] = None,
    ) -> None:
        """<p>Removes metadata tags from an Amazon Neptune resource.</p>

        Args:
            resource_name: <p>The Amazon Neptune resource that the tags are removed from. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href="https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing"> Constructing an Amazon Resource Name (ARN)</a>.</p>
            tag_keys: <p>The tag key (name) of the tag to be removed.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <i>DBInstanceIdentifier</i> does not refer to an existing DB instance.</p>
            capo_neptune.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault: <p> <i>DBSnapshotIdentifier</i> does not refer to an existing DB snapshot.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.remove_tags_from_resource_message.RemoveTagsFromResourceMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_neptune._operations.amazon_rd_sv19.remove_tags_from_resource

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.remove_tags_from_resource.async_remove_tags_from_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.remove_tags_from_resource_message.RemoveTagsFromResourceMessage = {}
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

    async def reset_db_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        reset_all_parameters: Optional["capo_neptune.types.boolean.Boolean"] = None,
        parameters: Optional[
            "capo_neptune.types.parameters_list.ParametersList"
        ] = None,
    ) -> "capo_neptune.types.db_cluster_parameter_group_name_message.DBClusterParameterGroupNameMessage":
        """<p> Modifies the parameters of a DB cluster parameter group to the default value. To reset specific parameters submit a list of the following: <code>ParameterName</code> and <code>ApplyMethod</code>. To reset the entire DB cluster parameter group, specify the <code>DBClusterParameterGroupName</code> and <code>ResetAllParameters</code> parameters.</p> <p> When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to <code>pending-reboot</code> to take effect on the next DB instance restart or <a>RebootDBInstance</a> request. You must call <a>RebootDBInstance</a> for every DB instance in your DB cluster that you want the updated static parameter to apply to.</p>

        Args:
            db_cluster_parameter_group_name: <p>The name of the DB cluster parameter group to reset.</p>
            reset_all_parameters: <p>A value that is set to <code>true</code> to reset all parameters in the DB cluster parameter group to their default values, and <code>false</code> otherwise. You can't use this parameter if there is a list of parameter names specified for the <code>Parameters</code> parameter.</p>
            parameters: <p>A list of parameter names in the DB cluster parameter group to reset to the default values. You can't use this parameter if the <code>ResetAllParameters</code> parameter is set to <code>true</code>.</p>

        Raises:
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.invalid_db_parameter_group_state_fault.InvalidDBParameterGroupStateFault: <p>The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you cannot delete it when the parameter group is in this state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.reset_db_cluster_parameter_group_message.ResetDBClusterParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_cluster_parameter_group_name_message.DBClusterParameterGroupNameMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.reset_db_cluster_parameter_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.reset_db_cluster_parameter_group.async_reset_db_cluster_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.reset_db_cluster_parameter_group_message.ResetDBClusterParameterGroupMessage = {}
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
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

    async def reset_db_parameter_group(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_parameter_group_name: Optional["capo_neptune.types.string.String"] = None,
        reset_all_parameters: Optional["capo_neptune.types.boolean.Boolean"] = None,
        parameters: Optional[
            "capo_neptune.types.parameters_list.ParametersList"
        ] = None,
    ) -> (
        "capo_neptune.types.db_parameter_group_name_message.DBParameterGroupNameMessage"
    ):
        """<p>Modifies the parameters of a DB parameter group to the engine/system default value. To reset specific parameters, provide a list of the following: <code>ParameterName</code> and <code>ApplyMethod</code>. To reset the entire DB parameter group, specify the <code>DBParameterGroup</code> name and <code>ResetAllParameters</code> parameters. When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to <code>pending-reboot</code> to take effect on the next DB instance restart or <code>RebootDBInstance</code> request.</p>

        Args:
            db_parameter_group_name: <p>The name of the DB parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must match the name of an existing DBParameterGroup.</p> </li> </ul>
            reset_all_parameters: <p>Specifies whether (<code>true</code>) or not (<code>false</code>) to reset all parameters in the DB parameter group to default values.</p> <p>Default: <code>true</code> </p>
            parameters: <p>To reset the entire DB parameter group, specify the <code>DBParameterGroup</code> name and <code>ResetAllParameters</code> parameters. To reset specific parameters, provide a list of the following: <code>ParameterName</code> and <code>ApplyMethod</code>. A maximum of 20 parameters can be modified in a single request.</p> <p>Valid Values (for Apply method): <code>pending-reboot</code> </p>

        Raises:
            capo_neptune.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <i>DBParameterGroupName</i> does not refer to an existing DB parameter group.</p>
            capo_neptune.errors.invalid_db_parameter_group_state_fault.InvalidDBParameterGroupStateFault: <p>The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you cannot delete it when the parameter group is in this state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.reset_db_parameter_group_message.ResetDBParameterGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.db_parameter_group_name_message.DBParameterGroupNameMessage"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.reset_db_parameter_group

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.reset_db_parameter_group.async_reset_db_parameter_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.reset_db_parameter_group_message.ResetDBParameterGroupMessage = {}
        if db_parameter_group_name is not None:
            input_["db_parameter_group_name"] = db_parameter_group_name
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

    async def restore_db_cluster_from_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        availability_zones: Optional[
            "capo_neptune.types.availability_zones.AvailabilityZones"
        ] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        snapshot_identifier: Optional["capo_neptune.types.string.String"] = None,
        engine: Optional["capo_neptune.types.string.String"] = None,
        engine_version: Optional["capo_neptune.types.string.String"] = None,
        port: Optional["capo_neptune.types.integer_optional.IntegerOptional"] = None,
        db_subnet_group_name: Optional["capo_neptune.types.string.String"] = None,
        database_name: Optional["capo_neptune.types.string.String"] = None,
        option_group_name: Optional["capo_neptune.types.string.String"] = None,
        vpc_security_group_ids: Optional[
            "capo_neptune.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
        kms_key_id: Optional["capo_neptune.types.string.String"] = None,
        enable_iam_database_authentication: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        enable_cloudwatch_logs_exports: Optional[
            "capo_neptune.types.log_type_list.LogTypeList"
        ] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        deletion_protection: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        copy_tags_to_snapshot: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        serverless_v2_scaling_configuration: Optional[
            "capo_neptune.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
        ] = None,
        storage_type: Optional["capo_neptune.types.string.String"] = None,
        network_type: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult":
        """<p>Creates a new DB cluster from a DB snapshot or DB cluster snapshot.</p> <p>If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.</p> <p>If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.</p>

        Args:
            availability_zones: <p>Provides the list of EC2 Availability Zones that instances in the restored DB cluster can be created in.</p>
            db_cluster_identifier: <p>The name of the DB cluster to create from the DB snapshot or DB cluster snapshot. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-snapshot-id</code> </p>
            snapshot_identifier: <p>The identifier for the DB snapshot or DB cluster snapshot to restore from.</p> <p>You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing Snapshot.</p> </li> </ul>
            engine: <p>The database engine to use for the new DB cluster.</p> <p>Default: The same as source</p> <p>Constraint: Must be compatible with the engine of the source</p>
            engine_version: <p>The version of the database engine to use for the new DB cluster.</p>
            port: <p>The port number on which the new DB cluster accepts connections.</p> <p>Constraints: Value must be <code>1150-65535</code> </p> <p>Default: The same port as the original DB cluster.</p>
            db_subnet_group_name: <p>The name of the DB subnet group to use for the new DB cluster.</p> <p>Constraints: If supplied, must match the name of an existing DBSubnetGroup.</p> <p>Example: <code>mySubnetgroup</code> </p>
            database_name: <p>Not supported.</p>
            option_group_name: <p> <i>(Not supported by Neptune)</i> </p>
            vpc_security_group_ids: <p>A list of VPC security groups that the new DB cluster will belong to.</p>
            tags: <p>The tags to be assigned to the restored DB cluster.</p>
            kms_key_id: <p>The Amazon KMS key identifier to use when restoring an encrypted DB cluster from a DB snapshot or DB cluster snapshot.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same Amazon account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.</p> <p>If you do not specify a value for the <code>KmsKeyId</code> parameter, then the following will occur:</p> <ul> <li> <p>If the DB snapshot or DB cluster snapshot in <code>SnapshotIdentifier</code> is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the DB snapshot or DB cluster snapshot.</p> </li> <li> <p>If the DB snapshot or DB cluster snapshot in <code>SnapshotIdentifier</code> is not encrypted, then the restored DB cluster is not encrypted.</p> </li> </ul>
            enable_iam_database_authentication: <p>True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.</p> <p>Default: <code>false</code> </p>
            enable_cloudwatch_logs_exports: <p>The list of logs that the restored DB cluster is to export to Amazon CloudWatch Logs.</p>
            db_cluster_parameter_group_name: <p>The name of the DB cluster parameter group to associate with the new DB cluster.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBClusterParameterGroup.</p> </li> </ul>
            deletion_protection: <p>A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled. </p>
            copy_tags_to_snapshot: <p> <i>If set to <code>true</code>, tags are copied to any snapshot of the restored DB cluster that is created.</i> </p>
            serverless_v2_scaling_configuration: <p>Contains the scaling configuration of a Neptune Serverless DB cluster.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html">Using Amazon Neptune Serverless</a> in the <i>Amazon Neptune User Guide</i>.</p>
            storage_type: <p>Specifies the storage type to be associated with the DB cluster.</p> <p>Valid values: <code>standard</code>, <code>iopt1</code> </p> <p>Default: <code>standard</code> </p>
            network_type: <p>The network type of the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <b> <code>IPV4</code> </b> – ( <i>the default</i> ) The DB cluster uses only IPv4 addresses for communication.</p> </li> <li> <p> <b> <code>DUAL</code> </b> – The DB cluster uses both IPv4 and IPv6 addresses for communication. The DB subnet group associated with the cluster must support IPv6.</p> </li> </ul>

        Raises:
            capo_neptune.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault: <p>User already has a DB cluster with the given identifier.</p>
            capo_neptune.errors.db_cluster_parameter_group_not_found_fault.DBClusterParameterGroupNotFoundFault: <p> <i>DBClusterParameterGroupName</i> does not refer to an existing DB Cluster parameter group.</p>
            capo_neptune.errors.db_cluster_quota_exceeded_fault.DBClusterQuotaExceededFault: <p>User attempted to create a new DB cluster and the user has already reached the maximum allowed DB cluster quota.</p>
            capo_neptune.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <i>DBClusterSnapshotIdentifier</i> does not refer to an existing DB cluster snapshot.</p>
            capo_neptune.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault: <p> <i>DBSnapshotIdentifier</i> does not refer to an existing DB snapshot.</p>
            capo_neptune.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <i>DBSubnetGroupName</i> does not refer to an existing DB subnet group.</p>
            capo_neptune.errors.insufficient_db_cluster_capacity_fault.InsufficientDBClusterCapacityFault: <p>The DB cluster does not have enough capacity for the current operation.</p>
            capo_neptune.errors.insufficient_storage_cluster_capacity_fault.InsufficientStorageClusterCapacityFault: <p>There is insufficient storage available for the current action. You may be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available.</p>
            capo_neptune.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The supplied value is not a valid DB cluster snapshot state.</p>
            capo_neptune.errors.invalid_db_snapshot_state_fault.InvalidDBSnapshotStateFault: <p>The state of the DB snapshot does not allow deletion.</p>
            capo_neptune.errors.invalid_restore_fault.InvalidRestoreFault: <p>Cannot restore from vpc backup to non-vpc DB instance.</p>
            capo_neptune.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.</p>
            capo_neptune.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>DB subnet group does not cover all Availability Zones after it is created because users' change.</p>
            capo_neptune.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>Error accessing KMS key.</p>
            capo_neptune.errors.network_type_not_supported_fault.NetworkTypeNotSupportedFault: <p>The specified <i>NetworkType</i> is not supported for the DB cluster, DB subnet group, or orderable DB instance option.</p>
            capo_neptune.errors.option_group_not_found_fault.OptionGroupNotFoundFault: <p>The designated option group could not be found.</p>
            capo_neptune.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>Request would result in user exceeding the allowed amount of storage available across all DB instances.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.restore_db_cluster_from_snapshot_message.RestoreDBClusterFromSnapshotMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.restore_db_cluster_from_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.restore_db_cluster_from_snapshot.async_restore_db_cluster_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.restore_db_cluster_from_snapshot_message.RestoreDBClusterFromSnapshotMessage = {}
        if availability_zones is not None:
            input_["availability_zones"] = availability_zones
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if snapshot_identifier is not None:
            input_["snapshot_identifier"] = snapshot_identifier
        if engine is not None:
            input_["engine"] = engine
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if port is not None:
            input_["port"] = port
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name
        if database_name is not None:
            input_["database_name"] = database_name
        if option_group_name is not None:
            input_["option_group_name"] = option_group_name
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if enable_iam_database_authentication is not None:
            input_["enable_iam_database_authentication"] = (
                enable_iam_database_authentication
            )
        if enable_cloudwatch_logs_exports is not None:
            input_["enable_cloudwatch_logs_exports"] = enable_cloudwatch_logs_exports
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if copy_tags_to_snapshot is not None:
            input_["copy_tags_to_snapshot"] = copy_tags_to_snapshot
        if serverless_v2_scaling_configuration is not None:
            input_["serverless_v2_scaling_configuration"] = (
                serverless_v2_scaling_configuration
            )
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if network_type is not None:
            input_["network_type"] = network_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_db_cluster_to_point_in_time(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
        restore_type: Optional["capo_neptune.types.string.String"] = None,
        source_db_cluster_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        restore_to_time: Optional["capo_neptune.types.t_stamp.TStamp"] = None,
        use_latest_restorable_time: Optional[
            "capo_neptune.types.boolean.Boolean"
        ] = None,
        port: Optional["capo_neptune.types.integer_optional.IntegerOptional"] = None,
        db_subnet_group_name: Optional["capo_neptune.types.string.String"] = None,
        option_group_name: Optional["capo_neptune.types.string.String"] = None,
        vpc_security_group_ids: Optional[
            "capo_neptune.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        tags: Optional["capo_neptune.types.tag_list.TagList"] = None,
        kms_key_id: Optional["capo_neptune.types.string.String"] = None,
        enable_iam_database_authentication: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        enable_cloudwatch_logs_exports: Optional[
            "capo_neptune.types.log_type_list.LogTypeList"
        ] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_neptune.types.string.String"
        ] = None,
        deletion_protection: Optional[
            "capo_neptune.types.boolean_optional.BooleanOptional"
        ] = None,
        serverless_v2_scaling_configuration: Optional[
            "capo_neptune.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
        ] = None,
        storage_type: Optional["capo_neptune.types.string.String"] = None,
        network_type: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.restore_db_cluster_to_point_in_time_result.RestoreDBClusterToPointInTimeResult":
        """<p>Restores a DB cluster to an arbitrary point in time. Users can restore to any point in time before <code>LatestRestorableTime</code> for up to <code>BackupRetentionPeriod</code> days. The target DB cluster is created from the source DB cluster with the same configuration as the original DB cluster, except that the new DB cluster is created with the default DB security group.</p> <note> <p>This action only restores the DB cluster, not the DB instances for that DB cluster. You must invoke the <a>CreateDBInstance</a> action to create DB instances for the restored DB cluster, specifying the identifier of the restored DB cluster in <code>DBClusterIdentifier</code>. You can create DB instances only after the <code>RestoreDBClusterToPointInTime</code> action has completed and the DB cluster is available.</p> </note>

        Args:
            db_cluster_identifier: <p>The name of the new DB cluster to be created.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul>
            restore_type: <p>The type of restore to be performed. You can specify one of the following values:</p> <ul> <li> <p> <code>full-copy</code> - The new DB cluster is restored as a full copy of the source DB cluster.</p> </li> <li> <p> <code>copy-on-write</code> - The new DB cluster is restored as a clone of the source DB cluster.</p> </li> </ul> <p>If you don't specify a <code>RestoreType</code> value, then the new DB cluster is restored as a full copy of the source DB cluster.</p>
            source_db_cluster_identifier: <p>The identifier of the source DB cluster from which to restore.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBCluster.</p> </li> </ul>
            restore_to_time: <p>The date and time to restore the DB cluster to.</p> <p>Valid Values: Value must be a time in Universal Coordinated Time (UTC) format</p> <p>Constraints:</p> <ul> <li> <p>Must be before the latest restorable time for the DB instance</p> </li> <li> <p>Must be specified if <code>UseLatestRestorableTime</code> parameter is not provided</p> </li> <li> <p>Cannot be specified if <code>UseLatestRestorableTime</code> parameter is true</p> </li> <li> <p>Cannot be specified if <code>RestoreType</code> parameter is <code>copy-on-write</code> </p> </li> </ul> <p>Example: <code>2015-03-07T23:45:00Z</code> </p>
            use_latest_restorable_time: <p>A value that is set to <code>true</code> to restore the DB cluster to the latest restorable backup time, and <code>false</code> otherwise.</p> <p>Default: <code>false</code> </p> <p>Constraints: Cannot be specified if <code>RestoreToTime</code> parameter is provided.</p>
            port: <p>The port number on which the new DB cluster accepts connections.</p> <p>Constraints: Value must be <code>1150-65535</code> </p> <p>Default: The same port as the original DB cluster.</p>
            db_subnet_group_name: <p>The DB subnet group name to use for the new DB cluster.</p> <p>Constraints: If supplied, must match the name of an existing DBSubnetGroup.</p> <p>Example: <code>mySubnetgroup</code> </p>
            option_group_name: <p> <i>(Not supported by Neptune)</i> </p>
            vpc_security_group_ids: <p>A list of VPC security groups that the new DB cluster belongs to.</p>
            tags: <p>The tags to be applied to the restored DB cluster.</p>
            kms_key_id: <p>The Amazon KMS key identifier to use when restoring an encrypted DB cluster from an encrypted DB cluster.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same Amazon account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.</p> <p>You can restore to a new DB cluster and encrypt the new DB cluster with a KMS key that is different than the KMS key used to encrypt the source DB cluster. The new DB cluster is encrypted with the KMS key identified by the <code>KmsKeyId</code> parameter.</p> <p>If you do not specify a value for the <code>KmsKeyId</code> parameter, then the following will occur:</p> <ul> <li> <p>If the DB cluster is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the source DB cluster.</p> </li> <li> <p>If the DB cluster is not encrypted, then the restored DB cluster is not encrypted.</p> </li> </ul> <p>If <code>DBClusterIdentifier</code> refers to a DB cluster that is not encrypted, then the restore request is rejected.</p>
            enable_iam_database_authentication: <p>True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.</p> <p>Default: <code>false</code> </p>
            enable_cloudwatch_logs_exports: <p>The list of logs that the restored DB cluster is to export to CloudWatch Logs.</p>
            db_cluster_parameter_group_name: <p>The name of the DB cluster parameter group to associate with the new DB cluster.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match the name of an existing DBClusterParameterGroup.</p> </li> </ul>
            deletion_protection: <p>A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled. </p>
            serverless_v2_scaling_configuration: <p>Contains the scaling configuration of a Neptune Serverless DB cluster.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html">Using Amazon Neptune Serverless</a> in the <i>Amazon Neptune User Guide</i>.</p>
            storage_type: <p>Specifies the storage type to be associated with the DB cluster.</p> <p>Valid values: <code>standard</code>, <code>iopt1</code> </p> <p>Default: <code>standard</code> </p>
            network_type: <p>The network type of the DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <b> <code>IPV4</code> </b> – ( <i>the default</i> ) The DB cluster uses only IPv4 addresses for communication.</p> </li> <li> <p> <b> <code>DUAL</code> </b> – The DB cluster uses both IPv4 and IPv6 addresses for communication. The DB subnet group associated with the cluster must support IPv6.</p> </li> </ul>

        Raises:
            capo_neptune.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault: <p>User already has a DB cluster with the given identifier.</p>
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.db_cluster_parameter_group_not_found_fault.DBClusterParameterGroupNotFoundFault: <p> <i>DBClusterParameterGroupName</i> does not refer to an existing DB Cluster parameter group.</p>
            capo_neptune.errors.db_cluster_quota_exceeded_fault.DBClusterQuotaExceededFault: <p>User attempted to create a new DB cluster and the user has already reached the maximum allowed DB cluster quota.</p>
            capo_neptune.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <i>DBClusterSnapshotIdentifier</i> does not refer to an existing DB cluster snapshot.</p>
            capo_neptune.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <i>DBSubnetGroupName</i> does not refer to an existing DB subnet group.</p>
            capo_neptune.errors.insufficient_db_cluster_capacity_fault.InsufficientDBClusterCapacityFault: <p>The DB cluster does not have enough capacity for the current operation.</p>
            capo_neptune.errors.insufficient_storage_cluster_capacity_fault.InsufficientStorageClusterCapacityFault: <p>There is insufficient storage available for the current action. You may be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available.</p>
            capo_neptune.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The supplied value is not a valid DB cluster snapshot state.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_db_snapshot_state_fault.InvalidDBSnapshotStateFault: <p>The state of the DB snapshot does not allow deletion.</p>
            capo_neptune.errors.invalid_restore_fault.InvalidRestoreFault: <p>Cannot restore from vpc backup to non-vpc DB instance.</p>
            capo_neptune.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.</p>
            capo_neptune.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>DB subnet group does not cover all Availability Zones after it is created because users' change.</p>
            capo_neptune.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>Error accessing KMS key.</p>
            capo_neptune.errors.network_type_not_supported_fault.NetworkTypeNotSupportedFault: <p>The specified <i>NetworkType</i> is not supported for the DB cluster, DB subnet group, or orderable DB instance option.</p>
            capo_neptune.errors.option_group_not_found_fault.OptionGroupNotFoundFault: <p>The designated option group could not be found.</p>
            capo_neptune.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>Request would result in user exceeding the allowed amount of storage available across all DB instances.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.restore_db_cluster_to_point_in_time_message.RestoreDBClusterToPointInTimeMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.restore_db_cluster_to_point_in_time_result.RestoreDBClusterToPointInTimeResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.restore_db_cluster_to_point_in_time

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.restore_db_cluster_to_point_in_time.async_restore_db_cluster_to_point_in_time(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.restore_db_cluster_to_point_in_time_message.RestoreDBClusterToPointInTimeMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if restore_type is not None:
            input_["restore_type"] = restore_type
        if source_db_cluster_identifier is not None:
            input_["source_db_cluster_identifier"] = source_db_cluster_identifier
        if restore_to_time is not None:
            input_["restore_to_time"] = restore_to_time
        if use_latest_restorable_time is not None:
            input_["use_latest_restorable_time"] = use_latest_restorable_time
        if port is not None:
            input_["port"] = port
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name
        if option_group_name is not None:
            input_["option_group_name"] = option_group_name
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if enable_iam_database_authentication is not None:
            input_["enable_iam_database_authentication"] = (
                enable_iam_database_authentication
            )
        if enable_cloudwatch_logs_exports is not None:
            input_["enable_cloudwatch_logs_exports"] = enable_cloudwatch_logs_exports
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if serverless_v2_scaling_configuration is not None:
            input_["serverless_v2_scaling_configuration"] = (
                serverless_v2_scaling_configuration
            )
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if network_type is not None:
            input_["network_type"] = network_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_db_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.start_db_cluster_result.StartDBClusterResult":
        """<p>Starts an Amazon Neptune DB cluster that was stopped using the Amazon console, the Amazon CLI stop-db-cluster command, or the StopDBCluster API.</p>

        Args:
            db_cluster_identifier: <p>The DB cluster identifier of the Neptune DB cluster to be started. This parameter is stored as a lowercase string.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.start_db_cluster_message.StartDBClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.start_db_cluster_result.StartDBClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.start_db_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.start_db_cluster.async_start_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.start_db_cluster_message.StartDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_db_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        db_cluster_identifier: Optional["capo_neptune.types.string.String"] = None,
    ) -> "capo_neptune.types.stop_db_cluster_result.StopDBClusterResult":
        """<p>Stops an Amazon Neptune DB cluster. When you stop a DB cluster, Neptune retains the DB cluster's metadata, including its endpoints and DB parameter groups.</p> <p>Neptune also retains the transaction logs so you can do a point-in-time restore if necessary.</p>

        Args:
            db_cluster_identifier: <p>The DB cluster identifier of the Neptune DB cluster to be stopped. This parameter is stored as a lowercase string.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p>The specified DB instance is not in the <i>available</i> state.</p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.stop_db_cluster_message.StopDBClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.stop_db_cluster_result.StopDBClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.stop_db_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.stop_db_cluster.async_stop_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.stop_db_cluster_message.StopDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def switchover_global_cluster(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        target_db_cluster_identifier: Optional[
            "capo_neptune.types.string.String"
        ] = None,
    ) -> "capo_neptune.types.switchover_global_cluster_result.SwitchoverGlobalClusterResult":
        """<p>Switches over the specified secondary DB cluster to be the new primary DB cluster in the global database cluster. Switchover operations were previously called "managed planned failovers."</p> <p>Promotes the specified secondary cluster to assume full read/write capabilities and demotes the current primary cluster to a secondary (read-only) cluster, maintaining the original replication topology. All secondary clusters are synchronized with the primary at the beginning of the process so the new primary continues operations for the global database without losing any data. Your database is unavailable for a short time while the primary and selected secondary clusters are assuming their new roles.</p> <note> <p>This operation is intended for controlled environments, for operations such as "regional rotation" or to fall back to the original primary after a global database failover.</p> </note>

        Args:
            global_cluster_identifier: <p>The identifier of the global database cluster to switch over. This parameter isn't case-sensitive.</p> <p>Constraints: Must match the identifier of an existing global database cluster.</p>
            target_db_cluster_identifier: <p>The Amazon Resource Name (ARN) of the secondary Neptune DB cluster that you want to promote to primary for the global database.</p>

        Raises:
            capo_neptune.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <i>DBClusterIdentifier</i> does not refer to an existing DB cluster.</p>
            capo_neptune.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global database cluster. </p>
            capo_neptune.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The DB cluster is not in a valid state.</p>
            capo_neptune.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The global cluster is in an invalid state and can't perform the requested operation. </p>
            capo_neptune.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune.types.switchover_global_cluster_message.SwitchoverGlobalClusterMessage]",
        ) -> AsyncOperationResponse[
            "capo_neptune.types.switchover_global_cluster_result.SwitchoverGlobalClusterResult"
        ]:
            import capo_neptune._operations.amazon_rd_sv19.switchover_global_cluster

            (
                output,
                http_response,
            ) = await capo_neptune._operations.amazon_rd_sv19.switchover_global_cluster.async_switchover_global_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_neptune.types.switchover_global_cluster_message.SwitchoverGlobalClusterMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if target_db_cluster_identifier is not None:
            input_["target_db_cluster_identifier"] = target_db_cluster_identifier

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
