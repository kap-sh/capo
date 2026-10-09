"""Generated from Smithy shape ``com.amazonaws.docdb#AmazonRDSv19``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_docdb._auth._signers
import capo_docdb._auth._sigv4
from capo_docdb._auth._identity import Credentials
from capo_docdb._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_docdb._auth._zapros_handler import AuthMiddleware
from capo_docdb._pagination import resolve_path as _resolve_path
from capo_docdb._services._aws_config import aws_config
from capo_docdb._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_docdb.types.add_source_identifier_to_subscription_message
    import capo_docdb.types.add_source_identifier_to_subscription_result
    import capo_docdb.types.add_tags_to_resource_message
    import capo_docdb.types.apply_pending_maintenance_action_message
    import capo_docdb.types.apply_pending_maintenance_action_result
    import capo_docdb.types.attribute_value_list
    import capo_docdb.types.availability_zones
    import capo_docdb.types.boolean
    import capo_docdb.types.boolean_optional
    import capo_docdb.types.certificate
    import capo_docdb.types.certificate_message
    import capo_docdb.types.cloudwatch_logs_export_configuration
    import capo_docdb.types.copy_db_cluster_parameter_group_message
    import capo_docdb.types.copy_db_cluster_parameter_group_result
    import capo_docdb.types.copy_db_cluster_snapshot_message
    import capo_docdb.types.copy_db_cluster_snapshot_result
    import capo_docdb.types.create_db_cluster_message
    import capo_docdb.types.create_db_cluster_parameter_group_message
    import capo_docdb.types.create_db_cluster_parameter_group_result
    import capo_docdb.types.create_db_cluster_result
    import capo_docdb.types.create_db_cluster_snapshot_message
    import capo_docdb.types.create_db_cluster_snapshot_result
    import capo_docdb.types.create_db_instance_message
    import capo_docdb.types.create_db_instance_result
    import capo_docdb.types.create_db_subnet_group_message
    import capo_docdb.types.create_db_subnet_group_result
    import capo_docdb.types.create_event_subscription_message
    import capo_docdb.types.create_event_subscription_result
    import capo_docdb.types.create_global_cluster_message
    import capo_docdb.types.create_global_cluster_result
    import capo_docdb.types.db_cluster
    import capo_docdb.types.db_cluster_identifier
    import capo_docdb.types.db_cluster_message
    import capo_docdb.types.db_cluster_parameter_group
    import capo_docdb.types.db_cluster_parameter_group_details
    import capo_docdb.types.db_cluster_parameter_group_name_message
    import capo_docdb.types.db_cluster_parameter_groups_message
    import capo_docdb.types.db_cluster_snapshot
    import capo_docdb.types.db_cluster_snapshot_message
    import capo_docdb.types.db_engine_version
    import capo_docdb.types.db_engine_version_message
    import capo_docdb.types.db_instance
    import capo_docdb.types.db_instance_message
    import capo_docdb.types.db_subnet_group
    import capo_docdb.types.db_subnet_group_message
    import capo_docdb.types.delete_db_cluster_message
    import capo_docdb.types.delete_db_cluster_parameter_group_message
    import capo_docdb.types.delete_db_cluster_result
    import capo_docdb.types.delete_db_cluster_snapshot_message
    import capo_docdb.types.delete_db_cluster_snapshot_result
    import capo_docdb.types.delete_db_instance_message
    import capo_docdb.types.delete_db_instance_result
    import capo_docdb.types.delete_db_subnet_group_message
    import capo_docdb.types.delete_event_subscription_message
    import capo_docdb.types.delete_event_subscription_result
    import capo_docdb.types.delete_global_cluster_message
    import capo_docdb.types.delete_global_cluster_result
    import capo_docdb.types.describe_certificates_message
    import capo_docdb.types.describe_db_cluster_parameter_groups_message
    import capo_docdb.types.describe_db_cluster_parameters_message
    import capo_docdb.types.describe_db_cluster_snapshot_attributes_message
    import capo_docdb.types.describe_db_cluster_snapshot_attributes_result
    import capo_docdb.types.describe_db_cluster_snapshots_message
    import capo_docdb.types.describe_db_clusters_message
    import capo_docdb.types.describe_db_engine_versions_message
    import capo_docdb.types.describe_db_instances_message
    import capo_docdb.types.describe_db_subnet_groups_message
    import capo_docdb.types.describe_engine_default_cluster_parameters_message
    import capo_docdb.types.describe_engine_default_cluster_parameters_result
    import capo_docdb.types.describe_event_categories_message
    import capo_docdb.types.describe_event_subscriptions_message
    import capo_docdb.types.describe_events_message
    import capo_docdb.types.describe_global_clusters_message
    import capo_docdb.types.describe_orderable_db_instance_options_message
    import capo_docdb.types.describe_pending_maintenance_actions_message
    import capo_docdb.types.event
    import capo_docdb.types.event_categories_list
    import capo_docdb.types.event_categories_message
    import capo_docdb.types.event_subscription
    import capo_docdb.types.event_subscriptions_message
    import capo_docdb.types.events_message
    import capo_docdb.types.failover_db_cluster_message
    import capo_docdb.types.failover_db_cluster_result
    import capo_docdb.types.failover_global_cluster_message
    import capo_docdb.types.failover_global_cluster_result
    import capo_docdb.types.filter_list
    import capo_docdb.types.global_cluster
    import capo_docdb.types.global_cluster_identifier
    import capo_docdb.types.global_clusters_message
    import capo_docdb.types.integer_optional
    import capo_docdb.types.key_list
    import capo_docdb.types.list_tags_for_resource_message
    import capo_docdb.types.log_type_list
    import capo_docdb.types.modify_db_cluster_message
    import capo_docdb.types.modify_db_cluster_parameter_group_message
    import capo_docdb.types.modify_db_cluster_result
    import capo_docdb.types.modify_db_cluster_snapshot_attribute_message
    import capo_docdb.types.modify_db_cluster_snapshot_attribute_result
    import capo_docdb.types.modify_db_instance_message
    import capo_docdb.types.modify_db_instance_result
    import capo_docdb.types.modify_db_subnet_group_message
    import capo_docdb.types.modify_db_subnet_group_result
    import capo_docdb.types.modify_event_subscription_message
    import capo_docdb.types.modify_event_subscription_result
    import capo_docdb.types.modify_global_cluster_message
    import capo_docdb.types.modify_global_cluster_result
    import capo_docdb.types.orderable_db_instance_option
    import capo_docdb.types.orderable_db_instance_options_message
    import capo_docdb.types.parameter
    import capo_docdb.types.parameters_list
    import capo_docdb.types.pending_maintenance_actions_message
    import capo_docdb.types.reboot_db_instance_message
    import capo_docdb.types.reboot_db_instance_result
    import capo_docdb.types.remove_from_global_cluster_message
    import capo_docdb.types.remove_from_global_cluster_result
    import capo_docdb.types.remove_source_identifier_from_subscription_message
    import capo_docdb.types.remove_source_identifier_from_subscription_result
    import capo_docdb.types.remove_tags_from_resource_message
    import capo_docdb.types.reset_db_cluster_parameter_group_message
    import capo_docdb.types.resource_pending_maintenance_actions
    import capo_docdb.types.restore_db_cluster_from_snapshot_message
    import capo_docdb.types.restore_db_cluster_from_snapshot_result
    import capo_docdb.types.restore_db_cluster_to_point_in_time_message
    import capo_docdb.types.restore_db_cluster_to_point_in_time_result
    import capo_docdb.types.serverless_v2_scaling_configuration
    import capo_docdb.types.source_ids_list
    import capo_docdb.types.source_type
    import capo_docdb.types.start_db_cluster_message
    import capo_docdb.types.start_db_cluster_result
    import capo_docdb.types.stop_db_cluster_message
    import capo_docdb.types.stop_db_cluster_result
    import capo_docdb.types.string
    import capo_docdb.types.subnet_identifier_list
    import capo_docdb.types.switchover_global_cluster_message
    import capo_docdb.types.switchover_global_cluster_result
    import capo_docdb.types.t_stamp
    import capo_docdb.types.tag_list
    import capo_docdb.types.tag_list_message
    import capo_docdb.types.vpc_security_group_id_list


class DocDBClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class DocDBClient:
    """A client for the ``DocDB`` service.

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
        self._config = DocDBClientConfig(
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
        self, config_overrides: Optional[DocDBClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DocDBClientConfig = config_overrides or {}
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

    def add_source_identifier_to_subscription(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        subscription_name: Optional["capo_docdb.types.string.String"] = None,
        source_identifier: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.add_source_identifier_to_subscription_result.AddSourceIdentifierToSubscriptionResult":
        """<p>Adds a source identifier to an existing event notification subscription.</p>

        Args:
            subscription_name: <p>The name of the Amazon DocumentDB event notification subscription that you want to add a source identifier to.</p>
            source_identifier: <p>The identifier of the event source to be added:</p> <ul> <li> <p>If the source type is an instance, a <code>DBInstanceIdentifier</code> must be provided.</p> </li> <li> <p>If the source type is a security group, a <code>DBSecurityGroupName</code> must be provided.</p> </li> <li> <p>If the source type is a parameter group, a <code>DBParameterGroupName</code> must be provided.</p> </li> <li> <p>If the source type is a snapshot, a <code>DBSnapshotIdentifier</code> must be provided.</p> </li> </ul>

        Raises:
            capo_docdb.errors.source_not_found_fault.SourceNotFoundFault: <p>The requested source could not be found. </p>
            capo_docdb.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>The subscription name does not exist. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.add_source_identifier_to_subscription_message.AddSourceIdentifierToSubscriptionMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.add_source_identifier_to_subscription_result.AddSourceIdentifierToSubscriptionResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.add_source_identifier_to_subscription

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.add_source_identifier_to_subscription.add_source_identifier_to_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.add_source_identifier_to_subscription_message.AddSourceIdentifierToSubscriptionMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if source_identifier is not None:
            input_["source_identifier"] = source_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_tags_to_resource(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        resource_name: Optional["capo_docdb.types.string.String"] = None,
        tags: Optional["capo_docdb.types.tag_list.TagList"] = None,
    ) -> None:
        """<p>Adds metadata tags to an Amazon DocumentDB resource. You can use these tags with cost allocation reporting to track costs that are associated with Amazon DocumentDB resources or in a <code>Condition</code> statement in an Identity and Access Management (IAM) policy for Amazon DocumentDB.</p>

        Args:
            resource_name: <p>The Amazon DocumentDB resource that the tags are added to. This value is an Amazon Resource Name .</p>
            tags: <p>The tags to be assigned to the Amazon DocumentDB resource.</p>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <code>DBInstanceIdentifier</code> doesn't refer to an existing instance. </p>
            capo_docdb.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault: <p> <code>DBSnapshotIdentifier</code> doesn't refer to an existing snapshot. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.add_tags_to_resource_message.AddTagsToResourceMessage]",
        ) -> OperationResponse[None]:
            import capo_docdb._operations.amazon_rd_sv19.add_tags_to_resource

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.add_tags_to_resource.add_tags_to_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.add_tags_to_resource_message.AddTagsToResourceMessage = {}
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

    def apply_pending_maintenance_action(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        resource_identifier: Optional["capo_docdb.types.string.String"] = None,
        apply_action: Optional["capo_docdb.types.string.String"] = None,
        opt_in_type: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.apply_pending_maintenance_action_result.ApplyPendingMaintenanceActionResult":
        """<p>Applies a pending maintenance action to a resource (for example, to an Amazon DocumentDB instance).</p>

        Args:
            resource_identifier: <p>The Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to.</p>
            apply_action: <p>The pending maintenance action to apply to this resource.</p> <p>Valid values: <code>system-update</code>, <code>db-upgrade</code> </p>
            opt_in_type: <p>A value that specifies the type of opt-in request or undoes an opt-in request. An opt-in request of type <code>immediate</code> can't be undone.</p> <p>Valid values:</p> <ul> <li> <p> <code>immediate</code> - Apply the maintenance action immediately.</p> </li> <li> <p> <code>next-maintenance</code> - Apply the maintenance action during the next maintenance window for the resource. </p> </li> <li> <p> <code>undo-opt-in</code> - Cancel any existing <code>next-maintenance</code> opt-in requests.</p> </li> </ul>

        Raises:
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p> The specified instance isn't in the <i>available</i> state. </p>
            capo_docdb.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The specified resource ID was not found.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.apply_pending_maintenance_action_message.ApplyPendingMaintenanceActionMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.apply_pending_maintenance_action_result.ApplyPendingMaintenanceActionResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.apply_pending_maintenance_action

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.apply_pending_maintenance_action.apply_pending_maintenance_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.apply_pending_maintenance_action_message.ApplyPendingMaintenanceActionMessage = {}
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if apply_action is not None:
            input_["apply_action"] = apply_action
        if opt_in_type is not None:
            input_["opt_in_type"] = opt_in_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def copy_db_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        source_db_cluster_parameter_group_identifier: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        target_db_cluster_parameter_group_identifier: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        target_db_cluster_parameter_group_description: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        tags: Optional["capo_docdb.types.tag_list.TagList"] = None,
    ) -> "capo_docdb.types.copy_db_cluster_parameter_group_result.CopyDBClusterParameterGroupResult":
        """<p>Copies the specified cluster parameter group.</p>

        Args:
            source_db_cluster_parameter_group_identifier: <p>The identifier or Amazon Resource Name (ARN) for the source cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid cluster parameter group.</p> </li> <li> <p>If the source cluster parameter group is in the same Amazon Web Services Region as the copy, specify a valid parameter group identifier; for example, <code>my-db-cluster-param-group</code>, or a valid ARN.</p> </li> <li> <p>If the source parameter group is in a different Amazon Web Services Region than the copy, specify a valid cluster parameter group ARN; for example, <code>arn:aws:rds:us-east-1:123456789012:sample-cluster:sample-parameter-group</code>.</p> </li> </ul>
            target_db_cluster_parameter_group_identifier: <p>The identifier for the copied cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Cannot be null, empty, or blank.</p> </li> <li> <p>Must contain from 1 to 255 letters, numbers, or hyphens. </p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens. </p> </li> </ul> <p>Example: <code>my-cluster-param-group1</code> </p>
            target_db_cluster_parameter_group_description: <p>A description for the copied cluster parameter group.</p>
            tags: <p>The tags that are to be assigned to the parameter group.</p>

        Raises:
            capo_docdb.errors.db_parameter_group_already_exists_fault.DBParameterGroupAlreadyExistsFault: <p>A parameter group with the same name already exists.</p>
            capo_docdb.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <code>DBParameterGroupName</code> doesn't refer to an existing parameter group. </p>
            capo_docdb.errors.db_parameter_group_quota_exceeded_fault.DBParameterGroupQuotaExceededFault: <p>This request would cause you to exceed the allowed number of parameter groups.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.copy_db_cluster_parameter_group_message.CopyDBClusterParameterGroupMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.copy_db_cluster_parameter_group_result.CopyDBClusterParameterGroupResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.copy_db_cluster_parameter_group

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.copy_db_cluster_parameter_group.copy_db_cluster_parameter_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.copy_db_cluster_parameter_group_message.CopyDBClusterParameterGroupMessage = {}
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def copy_db_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        source_db_cluster_snapshot_identifier: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        target_db_cluster_snapshot_identifier: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        kms_key_id: Optional["capo_docdb.types.string.String"] = None,
        pre_signed_url: Optional["capo_docdb.types.string.String"] = None,
        copy_tags: Optional["capo_docdb.types.boolean_optional.BooleanOptional"] = None,
        tags: Optional["capo_docdb.types.tag_list.TagList"] = None,
    ) -> "capo_docdb.types.copy_db_cluster_snapshot_result.CopyDBClusterSnapshotResult":
        """<p>Copies a snapshot of a cluster.</p> <p>To copy a cluster snapshot from a shared manual cluster snapshot, <code>SourceDBClusterSnapshotIdentifier</code> must be the Amazon Resource Name (ARN) of the shared cluster snapshot. You can only copy a shared DB cluster snapshot, whether encrypted or not, in the same Amazon Web Services Region.</p> <p>To cancel the copy operation after it is in progress, delete the target cluster snapshot identified by <code>TargetDBClusterSnapshotIdentifier</code> while that cluster snapshot is in the <i>copying</i> status.</p>

        Args:
            source_db_cluster_snapshot_identifier: <p>The identifier of the cluster snapshot to copy. This parameter is not case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid cluster snapshot in the <i>available</i> state.</p> </li> <li> <p>If the source cluster snapshot is in the same Amazon Web Services Region as the copy, specify a valid snapshot identifier.</p> </li> <li> <p>If the source cluster snapshot is in a different Amazon Web Services Region or owned by another Amazon Web Services account, specify the snapshot ARN.</p> </li> </ul> <p>Example: <code>my-cluster-snapshot1</code> </p>
            target_db_cluster_snapshot_identifier: <p>The identifier of the new cluster snapshot to create from the source cluster snapshot. This parameter is not case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens. </p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens. </p> </li> </ul> <p>Example: <code>my-cluster-snapshot2</code> </p>
            kms_key_id: <p>The KMS key ID for an encrypted cluster snapshot. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key. </p> <p>If you copy an encrypted cluster snapshot from your Amazon Web Services account, you can specify a value for <code>KmsKeyId</code> to encrypt the copy with a new KMS encryption key. If you don't specify a value for <code>KmsKeyId</code>, then the copy of the cluster snapshot is encrypted with the same KMS key as the source cluster snapshot.</p> <p>If you copy an encrypted cluster snapshot that is shared from another Amazon Web Services account, then you must specify a value for <code>KmsKeyId</code>.</p> <p>To copy an encrypted cluster snapshot to another Amazon Web Services Region, set <code>KmsKeyId</code> to the KMS key ID that you want to use to encrypt the copy of the cluster snapshot in the destination Region. KMS encryption keys are specific to the Amazon Web Services Region that they are created in, and you can't use encryption keys from one Amazon Web Services Region in another Amazon Web Services Region.</p> <p>If you copy an unencrypted cluster snapshot and specify a value for the <code>KmsKeyId</code> parameter, an error is returned.</p>
            pre_signed_url: <p>The URL that contains a Signature Version 4 signed request for the<code>CopyDBClusterSnapshot</code> API action in the Amazon Web Services Region that contains the source cluster snapshot to copy. You must use the <code>PreSignedUrl</code> parameter when copying a cluster snapshot from another Amazon Web Services Region.</p> <p>If you are using an Amazon Web Services SDK tool or the CLI, you can specify <code>SourceRegion</code> (or <code>--source-region</code> for the CLI) instead of specifying <code>PreSignedUrl</code> manually. Specifying <code>SourceRegion</code> autogenerates a pre-signed URL that is a valid request for the operation that can be executed in the source Amazon Web Services Region.</p> <p>The presigned URL must be a valid request for the <code>CopyDBClusterSnapshot</code> API action that can be executed in the source Amazon Web Services Region that contains the cluster snapshot to be copied. The presigned URL request must contain the following parameter values:</p> <ul> <li> <p> <code>SourceRegion</code> - The ID of the region that contains the snapshot to be copied.</p> </li> <li> <p> <code>SourceDBClusterSnapshotIdentifier</code> - The identifier for the the encrypted cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source Amazon Web Services Region. For example, if you are copying an encrypted cluster snapshot from the us-east-1 Amazon Web Services Region, then your <code>SourceDBClusterSnapshotIdentifier</code> looks something like the following: <code>arn:aws:rds:us-east-1:12345678012:sample-cluster:sample-cluster-snapshot</code>.</p> </li> <li> <p> <code>TargetDBClusterSnapshotIdentifier</code> - The identifier for the new cluster snapshot to be created. This parameter isn't case sensitive.</p> </li> </ul>
            copy_tags: <p>Set to <code>true</code> to copy all tags from the source cluster snapshot to the target cluster snapshot, and otherwise <code>false</code>. The default is <code>false</code>.</p>
            tags: <p>The tags to be assigned to the cluster snapshot.</p>

        Raises:
            capo_docdb.errors.db_cluster_snapshot_already_exists_fault.DBClusterSnapshotAlreadyExistsFault: <p>You already have a cluster snapshot with the given identifier.</p>
            capo_docdb.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <code>DBClusterSnapshotIdentifier</code> doesn't refer to an existing cluster snapshot. </p>
            capo_docdb.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The provided value isn't a valid cluster snapshot state.</p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>An error occurred when accessing an KMS key.</p>
            capo_docdb.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>The request would cause you to exceed the allowed number of snapshots.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.copy_db_cluster_snapshot_message.CopyDBClusterSnapshotMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.copy_db_cluster_snapshot_result.CopyDBClusterSnapshotResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.copy_db_cluster_snapshot

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.copy_db_cluster_snapshot.copy_db_cluster_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.copy_db_cluster_snapshot_message.CopyDBClusterSnapshotMessage = {}
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_db_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        availability_zones: Optional[
            "capo_docdb.types.availability_zones.AvailabilityZones"
        ] = None,
        backup_retention_period: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_docdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        db_subnet_group_name: Optional["capo_docdb.types.string.String"] = None,
        engine: Optional["capo_docdb.types.string.String"] = None,
        engine_version: Optional["capo_docdb.types.string.String"] = None,
        port: Optional["capo_docdb.types.integer_optional.IntegerOptional"] = None,
        master_username: Optional["capo_docdb.types.string.String"] = None,
        master_user_password: Optional["capo_docdb.types.string.String"] = None,
        preferred_backup_window: Optional["capo_docdb.types.string.String"] = None,
        preferred_maintenance_window: Optional["capo_docdb.types.string.String"] = None,
        tags: Optional["capo_docdb.types.tag_list.TagList"] = None,
        storage_encrypted: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        kms_key_id: Optional["capo_docdb.types.string.String"] = None,
        pre_signed_url: Optional["capo_docdb.types.string.String"] = None,
        enable_cloudwatch_logs_exports: Optional[
            "capo_docdb.types.log_type_list.LogTypeList"
        ] = None,
        deletion_protection: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        global_cluster_identifier: Optional[
            "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        storage_type: Optional["capo_docdb.types.string.String"] = None,
        serverless_v2_scaling_configuration: Optional[
            "capo_docdb.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
        ] = None,
        manage_master_user_password: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        master_user_secret_kms_key_id: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        network_type: Optional["capo_docdb.types.string.String"] = None,
        copy_tags_to_snapshot: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_docdb.types.create_db_cluster_result.CreateDBClusterResult":
        """<p>Creates a new Amazon DocumentDB cluster.</p>

        Args:
            availability_zones: <p>A list of Amazon EC2 Availability Zones that instances in the cluster can be created in.</p>
            backup_retention_period: <p>The number of days for which automated backups are retained. You must specify a minimum value of 1.</p> <p>Default: 1</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 1 to 35.</p> </li> </ul>
            db_cluster_identifier: <p>The cluster identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens. </p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens. </p> </li> </ul> <p>Example: <code>my-cluster</code> </p>
            db_cluster_parameter_group_name: <p>The name of the cluster parameter group to associate with this cluster.</p>
            vpc_security_group_ids: <p>A list of EC2 VPC security groups to associate with this cluster. </p>
            db_subnet_group_name: <p>A subnet group to associate with this cluster.</p> <p>Constraints: Must match the name of an existing <code>DBSubnetGroup</code>. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>
            engine: <p>The name of the database engine to be used for this cluster.</p> <p>Valid values: <code>docdb</code> </p>
            engine_version: <p>The version number of the database engine to use. The <code>--engine-version</code> will default to the latest major engine version. For production workloads, we recommend explicitly declaring this parameter with the intended major engine version.</p>
            port: <p>The port number on which the instances in the cluster accept connections.</p>
            master_username: <p>The name of the master user for the cluster.</p> <p>Constraints:</p> <ul> <li> <p>Must be from 1 to 63 letters or numbers.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot be a reserved word for the chosen database engine. </p> </li> </ul>
            master_user_password: <p>The password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@).</p> <p>Constraints: Must contain from 8 to 100 characters.</p>
            preferred_backup_window: <p>The daily time range during which automated backups are created if automated backups are enabled using the <code>BackupRetentionPeriod</code> parameter. </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. </p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window. </p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>
            preferred_maintenance_window: <p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p>Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.</p> <p>Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p>Constraints: Minimum 30-minute window.</p>
            tags: <p>The tags to be assigned to the cluster.</p>
            storage_encrypted: <p>Specifies whether the cluster is encrypted.</p>
            kms_key_id: <p>The KMS key identifier for an encrypted cluster.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon Web Services account that owns the KMS encryption key that is used to encrypt the new cluster, you can use the KMS key alias instead of the ARN for the KMS encryption key.</p> <p>If an encryption key is not specified in <code>KmsKeyId</code>: </p> <ul> <li> <p>If the <code>StorageEncrypted</code> parameter is <code>true</code>, Amazon DocumentDB uses your default encryption key. </p> </li> </ul> <p>KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Regions.</p>
            pre_signed_url: <p>Not currently supported. </p>
            enable_cloudwatch_logs_exports: <p>A list of log types that need to be enabled for exporting to Amazon CloudWatch Logs. You can enable audit logs or profiler logs. For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/event-auditing.html"> Auditing Amazon DocumentDB Events</a> and <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/profiling.html"> Profiling Amazon DocumentDB Operations</a>. </p>
            deletion_protection: <p>Specifies whether this cluster can be deleted. If <code>DeletionProtection</code> is enabled, the cluster cannot be deleted unless it is modified and <code>DeletionProtection</code> is disabled. <code>DeletionProtection</code> protects clusters from being accidentally deleted.</p>
            global_cluster_identifier: <p>The cluster identifier of the new global cluster.</p>
            storage_type: <p>The storage type to associate with the DB cluster.</p> <p>For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the <i>Amazon DocumentDB Developer Guide</i>.</p> <p>Valid values for storage type - <code>standard | iopt1</code> </p> <p>Default value is <code>standard </code> </p> <note> <p>When you create an Amazon DocumentDB cluster with the storage type set to <code>iopt1</code>, the storage type is returned in the response. The storage type isn't returned when you set it to <code>standard</code>.</p> </note>
            serverless_v2_scaling_configuration: <p>Contains the scaling configuration of an Amazon DocumentDB Serverless cluster.</p>
            manage_master_user_password: <p>Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.</p> <p>Constraint: You can't manage the master user password with Amazon Web Services Secrets Manager if <code>MasterUserPassword</code> is specified.</p>
            master_user_secret_kms_key_id: <p>The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager. This setting is valid only if the master user password is managed by Amazon DocumentDB in Amazon Web Services Secrets Manager for the DB cluster.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>If you don't specify <code>MasterUserSecretKmsKeyId</code>, then the <code>aws/secretsmanager</code> KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the <code>aws/secretsmanager</code> KMS key to encrypt the secret, and you must use a customer managed KMS key.</p> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>
            network_type: <p>The network type of the cluster.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/vpc-clusters.html">DocumentDB clusters in a VPC</a> in the Amazon DocumentDB Developer Guide.</p> <p>Valid Values: <code>IPV4</code> | <code>DUAL</code> </p>
            copy_tags_to_snapshot: <p>Specifies whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.</p>

        Raises:
            capo_docdb.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault: <p>You already have a cluster with the given identifier.</p>
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.db_cluster_parameter_group_not_found_fault.DBClusterParameterGroupNotFoundFault: <p> <code>DBClusterParameterGroupName</code> doesn't refer to an existing cluster parameter group. </p>
            capo_docdb.errors.db_cluster_quota_exceeded_fault.DBClusterQuotaExceededFault: <p>The cluster can't be created because you have reached the maximum allowed quota of clusters.</p>
            capo_docdb.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <code>DBInstanceIdentifier</code> doesn't refer to an existing instance. </p>
            capo_docdb.errors.db_subnet_group_does_not_cover_enough_a_zs.DBSubnetGroupDoesNotCoverEnoughAZs: <p>Subnets in the subnet group should cover at least two Availability Zones unless there is only one Availability Zone.</p>
            capo_docdb.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <code>DBSubnetGroupName</code> doesn't refer to an existing subnet group. </p>
            capo_docdb.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global cluster.</p>
            capo_docdb.errors.insufficient_storage_cluster_capacity_fault.InsufficientStorageClusterCapacityFault: <p>There is not enough storage available for the current action. You might be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available. </p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p> The specified instance isn't in the <i>available</i> state. </p>
            capo_docdb.errors.invalid_db_subnet_group_state_fault.InvalidDBSubnetGroupStateFault: <p>The subnet group can't be deleted because it's in use.</p>
            capo_docdb.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The requested operation can't be performed while the cluster is in this state.</p>
            capo_docdb.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is not valid, or multiple subnets were requested that are not all in a common virtual private cloud (VPC).</p>
            capo_docdb.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The subnet group doesn't cover all Availability Zones after it is created because of changes that were made.</p>
            capo_docdb.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>An error occurred when accessing an KMS key.</p>
            capo_docdb.errors.network_type_not_supported.NetworkTypeNotSupported: <p>The network type is not supported by either <code>DBSubnetGroup</code> or the DB engine version.</p>
            capo_docdb.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>The request would cause you to exceed the allowed amount of storage available across all instances.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.create_db_cluster_message.CreateDBClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.create_db_cluster_result.CreateDBClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.create_db_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.create_db_cluster.create_db_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.create_db_cluster_message.CreateDBClusterMessage = {}
        if availability_zones is not None:
            input_["availability_zones"] = availability_zones
        if backup_retention_period is not None:
            input_["backup_retention_period"] = backup_retention_period
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
        if preferred_backup_window is not None:
            input_["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if tags is not None:
            input_["tags"] = tags
        if storage_encrypted is not None:
            input_["storage_encrypted"] = storage_encrypted
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if pre_signed_url is not None:
            input_["pre_signed_url"] = pre_signed_url
        if enable_cloudwatch_logs_exports is not None:
            input_["enable_cloudwatch_logs_exports"] = enable_cloudwatch_logs_exports
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if serverless_v2_scaling_configuration is not None:
            input_["serverless_v2_scaling_configuration"] = (
                serverless_v2_scaling_configuration
            )
        if manage_master_user_password is not None:
            input_["manage_master_user_password"] = manage_master_user_password
        if master_user_secret_kms_key_id is not None:
            input_["master_user_secret_kms_key_id"] = master_user_secret_kms_key_id
        if network_type is not None:
            input_["network_type"] = network_type
        if copy_tags_to_snapshot is not None:
            input_["copy_tags_to_snapshot"] = copy_tags_to_snapshot

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_db_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        db_parameter_group_family: Optional["capo_docdb.types.string.String"] = None,
        description: Optional["capo_docdb.types.string.String"] = None,
        tags: Optional["capo_docdb.types.tag_list.TagList"] = None,
    ) -> "capo_docdb.types.create_db_cluster_parameter_group_result.CreateDBClusterParameterGroupResult":
        """<p>Creates a new cluster parameter group.</p> <p>Parameters in a cluster parameter group apply to all of the instances in a cluster.</p> <p>A cluster parameter group is initially created with the default parameters for the database engine used by instances in the cluster. In Amazon DocumentDB, you cannot make modifications directly to the <code>default.docdb3.6</code> cluster parameter group. If your Amazon DocumentDB cluster is using the default cluster parameter group and you want to modify a value in it, you must first <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_group-create.html"> create a new parameter group</a> or <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_group-copy.html"> copy an existing parameter group</a>, modify it, and then apply the modified parameter group to your cluster. For the new cluster parameter group and associated settings to take effect, you must then reboot the instances in the cluster without failover. For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_group-modify.html"> Modifying Amazon DocumentDB Cluster Parameter Groups</a>. </p>

        Args:
            db_cluster_parameter_group_name: <p>The name of the cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must not match the name of an existing <code>DBClusterParameterGroup</code>.</p> </li> </ul> <note> <p>This value is stored as a lowercase string.</p> </note>
            db_parameter_group_family: <p>The cluster parameter group family name.</p>
            description: <p>The description for the cluster parameter group.</p>
            tags: <p>The tags to be assigned to the cluster parameter group.</p>

        Raises:
            capo_docdb.errors.db_parameter_group_already_exists_fault.DBParameterGroupAlreadyExistsFault: <p>A parameter group with the same name already exists.</p>
            capo_docdb.errors.db_parameter_group_quota_exceeded_fault.DBParameterGroupQuotaExceededFault: <p>This request would cause you to exceed the allowed number of parameter groups.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.create_db_cluster_parameter_group_message.CreateDBClusterParameterGroupMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.create_db_cluster_parameter_group_result.CreateDBClusterParameterGroupResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.create_db_cluster_parameter_group

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.create_db_cluster_parameter_group.create_db_cluster_parameter_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.create_db_cluster_parameter_group_message.CreateDBClusterParameterGroupMessage = {}
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if db_parameter_group_family is not None:
            input_["db_parameter_group_family"] = db_parameter_group_family
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

    def create_db_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        tags: Optional["capo_docdb.types.tag_list.TagList"] = None,
    ) -> "capo_docdb.types.create_db_cluster_snapshot_result.CreateDBClusterSnapshotResult":
        """<p>Creates a snapshot of a cluster. </p>

        Args:
            db_cluster_snapshot_identifier: <p>The identifier of the cluster snapshot. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens. </p> </li> </ul> <p>Example: <code>my-cluster-snapshot1</code> </p>
            db_cluster_identifier: <p>The identifier of the cluster to create a snapshot for. This parameter is not case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing <code>DBCluster</code>.</p> </li> </ul> <p>Example: <code>my-cluster</code> </p>
            tags: <p>The tags to be assigned to the cluster snapshot.</p>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.db_cluster_snapshot_already_exists_fault.DBClusterSnapshotAlreadyExistsFault: <p>You already have a cluster snapshot with the given identifier.</p>
            capo_docdb.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The provided value isn't a valid cluster snapshot state.</p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>The request would cause you to exceed the allowed number of snapshots.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.create_db_cluster_snapshot_message.CreateDBClusterSnapshotMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.create_db_cluster_snapshot_result.CreateDBClusterSnapshotResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.create_db_cluster_snapshot

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.create_db_cluster_snapshot.create_db_cluster_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.create_db_cluster_snapshot_message.CreateDBClusterSnapshotMessage = {}
        if db_cluster_snapshot_identifier is not None:
            input_["db_cluster_snapshot_identifier"] = db_cluster_snapshot_identifier
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_db_instance(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_instance_identifier: Optional["capo_docdb.types.string.String"] = None,
        db_instance_class: Optional["capo_docdb.types.string.String"] = None,
        engine: Optional["capo_docdb.types.string.String"] = None,
        availability_zone: Optional["capo_docdb.types.string.String"] = None,
        preferred_maintenance_window: Optional["capo_docdb.types.string.String"] = None,
        auto_minor_version_upgrade: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        tags: Optional["capo_docdb.types.tag_list.TagList"] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        copy_tags_to_snapshot: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        promotion_tier: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        enable_performance_insights: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        performance_insights_kms_key_id: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        ca_certificate_identifier: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.create_db_instance_result.CreateDBInstanceResult":
        """<p>Creates a new instance.</p>

        Args:
            db_instance_identifier: <p>The instance identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>mydbinstance</code> </p>
            db_instance_class: <p>The compute and memory capacity of the instance; for example, <code>db.r5.large</code>. </p>
            engine: <p>The name of the database engine to be used for this instance.</p> <p>Valid value: <code>docdb</code> </p>
            availability_zone: <p>The Amazon EC2 Availability Zone that the instance is created in. </p> <p>Default: A random, system-chosen Availability Zone in the endpoint's Amazon Web Services Region.</p> <p>Example: <code>us-east-1d</code> </p>
            preferred_maintenance_window: <p>The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p> Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week. </p> <p>Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p>Constraints: Minimum 30-minute window.</p>
            auto_minor_version_upgrade: <p>This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.</p> <p>Default: <code>false</code> </p>
            tags: <p>The tags to be assigned to the instance. You can assign up to 10 tags to an instance.</p>
            db_cluster_identifier: <p>The identifier of the cluster that the instance will belong to.</p>
            copy_tags_to_snapshot: <p>A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.</p>
            promotion_tier: <p>A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.</p> <p>Default: 1</p> <p>Valid values: 0-15</p>
            enable_performance_insights: <p>A value that indicates whether to enable Performance Insights for the DB Instance. For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/performance-insights.html">Using Amazon Performance Insights</a>.</p>
            performance_insights_kms_key_id: <p>The KMS key identifier for encryption of Performance Insights data.</p> <p>The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you do not specify a value for PerformanceInsightsKMSKeyId, then Amazon DocumentDB uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services region.</p>
            ca_certificate_identifier: <p>The CA certificate identifier to use for the DB instance's server certificate.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/ca_cert_rotation.html">Updating Your Amazon DocumentDB TLS Certificates</a> and <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/security.encryption.ssl.html"> Encrypting Data in Transit</a> in the <i>Amazon DocumentDB Developer Guide</i>.</p>

        Raises:
            capo_docdb.errors.authorization_not_found_fault.AuthorizationNotFoundFault: <p>The specified CIDR IP or Amazon EC2 security group isn't authorized for the specified security group.</p> <p>Amazon DocumentDB also might not be authorized to perform necessary actions on your behalf using IAM.</p>
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.db_instance_already_exists_fault.DBInstanceAlreadyExistsFault: <p>You already have a instance with the given identifier.</p>
            capo_docdb.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <code>DBParameterGroupName</code> doesn't refer to an existing parameter group. </p>
            capo_docdb.errors.db_security_group_not_found_fault.DBSecurityGroupNotFoundFault: <p> <code>DBSecurityGroupName</code> doesn't refer to an existing security group. </p>
            capo_docdb.errors.db_subnet_group_does_not_cover_enough_a_zs.DBSubnetGroupDoesNotCoverEnoughAZs: <p>Subnets in the subnet group should cover at least two Availability Zones unless there is only one Availability Zone.</p>
            capo_docdb.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <code>DBSubnetGroupName</code> doesn't refer to an existing subnet group. </p>
            capo_docdb.errors.instance_quota_exceeded_fault.InstanceQuotaExceededFault: <p>The request would cause you to exceed the allowed number of instances.</p>
            capo_docdb.errors.insufficient_db_instance_capacity_fault.InsufficientDBInstanceCapacityFault: <p>The specified instance class isn't available in the specified Availability Zone.</p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is not valid, or multiple subnets were requested that are not all in a common virtual private cloud (VPC).</p>
            capo_docdb.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The subnet group doesn't cover all Availability Zones after it is created because of changes that were made.</p>
            capo_docdb.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>An error occurred when accessing an KMS key.</p>
            capo_docdb.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>The request would cause you to exceed the allowed amount of storage available across all instances.</p>
            capo_docdb.errors.storage_type_not_supported_fault.StorageTypeNotSupportedFault: <p>Storage of the specified <code>StorageType</code> can't be associated with the DB instance. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.create_db_instance_message.CreateDBInstanceMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.create_db_instance_result.CreateDBInstanceResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.create_db_instance

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.create_db_instance.create_db_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.create_db_instance_message.CreateDBInstanceMessage = {}
        if db_instance_identifier is not None:
            input_["db_instance_identifier"] = db_instance_identifier
        if db_instance_class is not None:
            input_["db_instance_class"] = db_instance_class
        if engine is not None:
            input_["engine"] = engine
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if tags is not None:
            input_["tags"] = tags
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if copy_tags_to_snapshot is not None:
            input_["copy_tags_to_snapshot"] = copy_tags_to_snapshot
        if promotion_tier is not None:
            input_["promotion_tier"] = promotion_tier
        if enable_performance_insights is not None:
            input_["enable_performance_insights"] = enable_performance_insights
        if performance_insights_kms_key_id is not None:
            input_["performance_insights_kms_key_id"] = performance_insights_kms_key_id
        if ca_certificate_identifier is not None:
            input_["ca_certificate_identifier"] = ca_certificate_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_db_subnet_group(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_subnet_group_name: Optional["capo_docdb.types.string.String"] = None,
        db_subnet_group_description: Optional["capo_docdb.types.string.String"] = None,
        subnet_ids: Optional[
            "capo_docdb.types.subnet_identifier_list.SubnetIdentifierList"
        ] = None,
        tags: Optional["capo_docdb.types.tag_list.TagList"] = None,
    ) -> "capo_docdb.types.create_db_subnet_group_result.CreateDBSubnetGroupResult":
        """<p>Creates a new subnet group. subnet groups must contain at least one subnet in at least two Availability Zones in the Amazon Web Services Region.</p>

        Args:
            db_subnet_group_name: <p>The name for the subnet group. This value is stored as a lowercase string.</p> <p>Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>
            db_subnet_group_description: <p>The description for the subnet group.</p>
            subnet_ids: <p>The Amazon EC2 subnet IDs for the subnet group.</p>
            tags: <p>The tags to be assigned to the subnet group.</p>

        Raises:
            capo_docdb.errors.db_subnet_group_already_exists_fault.DBSubnetGroupAlreadyExistsFault: <p> <code>DBSubnetGroupName</code> is already being used by an existing subnet group. </p>
            capo_docdb.errors.db_subnet_group_does_not_cover_enough_a_zs.DBSubnetGroupDoesNotCoverEnoughAZs: <p>Subnets in the subnet group should cover at least two Availability Zones unless there is only one Availability Zone.</p>
            capo_docdb.errors.db_subnet_group_quota_exceeded_fault.DBSubnetGroupQuotaExceededFault: <p>The request would cause you to exceed the allowed number of subnet groups.</p>
            capo_docdb.errors.db_subnet_quota_exceeded_fault.DBSubnetQuotaExceededFault: <p>The request would cause you to exceed the allowed number of subnets in a subnet group.</p>
            capo_docdb.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is not valid, or multiple subnets were requested that are not all in a common virtual private cloud (VPC).</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.create_db_subnet_group_message.CreateDBSubnetGroupMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.create_db_subnet_group_result.CreateDBSubnetGroupResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.create_db_subnet_group

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.create_db_subnet_group.create_db_subnet_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.create_db_subnet_group_message.CreateDBSubnetGroupMessage = {}
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name
        if db_subnet_group_description is not None:
            input_["db_subnet_group_description"] = db_subnet_group_description
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_event_subscription(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        subscription_name: Optional["capo_docdb.types.string.String"] = None,
        sns_topic_arn: Optional["capo_docdb.types.string.String"] = None,
        source_type: Optional["capo_docdb.types.string.String"] = None,
        event_categories: Optional[
            "capo_docdb.types.event_categories_list.EventCategoriesList"
        ] = None,
        source_ids: Optional["capo_docdb.types.source_ids_list.SourceIdsList"] = None,
        enabled: Optional["capo_docdb.types.boolean_optional.BooleanOptional"] = None,
        tags: Optional["capo_docdb.types.tag_list.TagList"] = None,
    ) -> "capo_docdb.types.create_event_subscription_result.CreateEventSubscriptionResult":
        """<p>Creates an Amazon DocumentDB event notification subscription. This action requires a topic Amazon Resource Name (ARN) created by using the Amazon DocumentDB console, the Amazon SNS console, or the Amazon SNS API. To obtain an ARN with Amazon SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the Amazon SNS console.</p> <p>You can specify the type of source (<code>SourceType</code>) that you want to be notified of. You can also provide a list of Amazon DocumentDB sources (<code>SourceIds</code>) that trigger the events, and you can provide a list of event categories (<code>EventCategories</code>) for events that you want to be notified of. For example, you can specify <code>SourceType = db-instance</code>, <code>SourceIds = mydbinstance1, mydbinstance2</code> and <code>EventCategories = Availability, Backup</code>.</p> <p>If you specify both the <code>SourceType</code> and <code>SourceIds</code> (such as <code>SourceType = db-instance</code> and <code>SourceIdentifier = myDBInstance1</code>), you are notified of all the <code>db-instance</code> events for the specified source. If you specify a <code>SourceType</code> but do not specify a <code>SourceIdentifier</code>, you receive notice of the events for that source type for all your Amazon DocumentDB sources. If you do not specify either the <code>SourceType</code> or the <code>SourceIdentifier</code>, you are notified of events generated from all Amazon DocumentDB sources belonging to your customer account.</p>

        Args:
            subscription_name: <p>The name of the subscription.</p> <p>Constraints: The name must be fewer than 255 characters.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) of the SNS topic created for event notification. Amazon SNS creates the ARN when you create a topic and subscribe to it.</p>
            source_type: <p>The type of source that is generating the events. For example, if you want to be notified of events generated by an instance, you would set this parameter to <code>db-instance</code>. If this value is not specified, all events are returned.</p> <p>Valid values: <code>db-instance</code>, <code>db-cluster</code>, <code>db-parameter-group</code>, <code>db-security-group</code>, <code>db-cluster-snapshot</code> </p>
            event_categories: <p> A list of event categories for a <code>SourceType</code> that you want to subscribe to. </p>
            source_ids: <p>The list of identifiers of the event sources for which events are returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.</p> <p>Constraints:</p> <ul> <li> <p>If <code>SourceIds</code> are provided, <code>SourceType</code> must also be provided.</p> </li> <li> <p>If the source type is an instance, a <code>DBInstanceIdentifier</code> must be provided.</p> </li> <li> <p>If the source type is a security group, a <code>DBSecurityGroupName</code> must be provided.</p> </li> <li> <p>If the source type is a parameter group, a <code>DBParameterGroupName</code> must be provided.</p> </li> <li> <p>If the source type is a snapshot, a <code>DBSnapshotIdentifier</code> must be provided.</p> </li> </ul>
            enabled: <p> A Boolean value; set to <code>true</code> to activate the subscription, set to <code>false</code> to create the subscription but not active it. </p>
            tags: <p>The tags to be assigned to the event subscription.</p>

        Raises:
            capo_docdb.errors.event_subscription_quota_exceeded_fault.EventSubscriptionQuotaExceededFault: <p>You have reached the maximum number of event subscriptions. </p>
            capo_docdb.errors.sns_invalid_topic_fault.SNSInvalidTopicFault: <p>Amazon SNS has responded that there is a problem with the specified topic. </p>
            capo_docdb.errors.sns_no_authorization_fault.SNSNoAuthorizationFault: <p>You do not have permission to publish to the SNS topic Amazon Resource Name (ARN). </p>
            capo_docdb.errors.sns_topic_arn_not_found_fault.SNSTopicArnNotFoundFault: <p>The SNS topic Amazon Resource Name (ARN) does not exist. </p>
            capo_docdb.errors.source_not_found_fault.SourceNotFoundFault: <p>The requested source could not be found. </p>
            capo_docdb.errors.subscription_already_exist_fault.SubscriptionAlreadyExistFault: <p>The provided subscription name already exists. </p>
            capo_docdb.errors.subscription_category_not_found_fault.SubscriptionCategoryNotFoundFault: <p>The provided category does not exist. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.create_event_subscription_message.CreateEventSubscriptionMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.create_event_subscription_result.CreateEventSubscriptionResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.create_event_subscription

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.create_event_subscription.create_event_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.create_event_subscription_message.CreateEventSubscriptionMessage = {}
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_global_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        source_db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        engine: Optional["capo_docdb.types.string.String"] = None,
        engine_version: Optional["capo_docdb.types.string.String"] = None,
        deletion_protection: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        database_name: Optional["capo_docdb.types.string.String"] = None,
        storage_encrypted: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_docdb.types.create_global_cluster_result.CreateGlobalClusterResult":
        """<p>Creates an Amazon DocumentDB global cluster that can span multiple multiple Amazon Web Services Regions. The global cluster contains one primary cluster with read-write capability, and up-to 10 read-only secondary clusters. Global clusters uses storage-based fast replication across regions with latencies less than one second, using dedicated infrastructure with no impact to your workload’s performance.</p> <p></p> <p>You can create a global cluster that is initially empty, and then add a primary and a secondary to it. Or you can specify an existing cluster during the create operation, and this cluster becomes the primary of the global cluster. </p> <note> <p>This action only applies to Amazon DocumentDB clusters.</p> </note>

        Args:
            global_cluster_identifier: <p>The cluster identifier of the new global cluster.</p>
            source_db_cluster_identifier: <p>The Amazon Resource Name (ARN) to use as the primary cluster of the global cluster. This parameter is optional.</p>
            engine: <p>The name of the database engine to be used for this cluster.</p>
            engine_version: <p>The engine version of the global cluster.</p>
            deletion_protection: <p>The deletion protection setting for the new global cluster. The global cluster can't be deleted when deletion protection is enabled. </p>
            database_name: <p>The name for your database of up to 64 alpha-numeric characters. If you do not provide a name, Amazon DocumentDB will not create a database in the global cluster you are creating.</p>
            storage_encrypted: <p>The storage encryption setting for the new global cluster. </p>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.global_cluster_already_exists_fault.GlobalClusterAlreadyExistsFault: <p>The <code>GlobalClusterIdentifier</code> already exists. Choose a new global cluster identifier (unique name) to create a new global cluster. </p>
            capo_docdb.errors.global_cluster_quota_exceeded_fault.GlobalClusterQuotaExceededFault: <p>The number of global clusters for this account is already at the maximum allowed.</p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.create_global_cluster_message.CreateGlobalClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.create_global_cluster_result.CreateGlobalClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.create_global_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.create_global_cluster.create_global_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.create_global_cluster_message.CreateGlobalClusterMessage = {}
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
        if storage_encrypted is not None:
            input_["storage_encrypted"] = storage_encrypted

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_db_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        skip_final_snapshot: Optional["capo_docdb.types.boolean.Boolean"] = None,
        final_db_snapshot_identifier: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.delete_db_cluster_result.DeleteDBClusterResult":
        """<p>Deletes a previously provisioned cluster. When you delete a cluster, all automated backups for that cluster are deleted and can't be recovered. Manual DB cluster snapshots of the specified cluster are not deleted.</p> <p></p>

        Args:
            db_cluster_identifier: <p>The cluster identifier for the cluster to be deleted. This parameter isn't case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match an existing <code>DBClusterIdentifier</code>.</p> </li> </ul>
            skip_final_snapshot: <p> Determines whether a final cluster snapshot is created before the cluster is deleted. If <code>true</code> is specified, no cluster snapshot is created. If <code>false</code> is specified, a cluster snapshot is created before the DB cluster is deleted. </p> <note> <p>If <code>SkipFinalSnapshot</code> is <code>false</code>, you must specify a <code>FinalDBSnapshotIdentifier</code> parameter.</p> </note> <p>Default: <code>false</code> </p>
            final_db_snapshot_identifier: <p> The cluster snapshot identifier of the new cluster snapshot created when <code>SkipFinalSnapshot</code> is set to <code>false</code>. </p> <note> <p> Specifying this parameter and also setting the <code>SkipFinalShapshot</code> parameter to <code>true</code> results in an error. </p> </note> <p>Constraints:</p> <ul> <li> <p>Must be from 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.db_cluster_snapshot_already_exists_fault.DBClusterSnapshotAlreadyExistsFault: <p>You already have a cluster snapshot with the given identifier.</p>
            capo_docdb.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The provided value isn't a valid cluster snapshot state.</p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>The request would cause you to exceed the allowed number of snapshots.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.delete_db_cluster_message.DeleteDBClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.delete_db_cluster_result.DeleteDBClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.delete_db_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.delete_db_cluster.delete_db_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.delete_db_cluster_message.DeleteDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if skip_final_snapshot is not None:
            input_["skip_final_snapshot"] = skip_final_snapshot
        if final_db_snapshot_identifier is not None:
            input_["final_db_snapshot_identifier"] = final_db_snapshot_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_db_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_docdb.types.string.String"
        ] = None,
    ) -> None:
        """<p>Deletes a specified cluster parameter group. The cluster parameter group to be deleted can't be associated with any clusters.</p>

        Args:
            db_cluster_parameter_group_name: <p>The name of the cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must be the name of an existing cluster parameter group.</p> </li> <li> <p>You can't delete a default cluster parameter group.</p> </li> <li> <p>Cannot be associated with any clusters.</p> </li> </ul>

        Raises:
            capo_docdb.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <code>DBParameterGroupName</code> doesn't refer to an existing parameter group. </p>
            capo_docdb.errors.invalid_db_parameter_group_state_fault.InvalidDBParameterGroupStateFault: <p>The parameter group is in use, or it is in a state that is not valid. If you are trying to delete the parameter group, you can't delete it when the parameter group is in this state.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.delete_db_cluster_parameter_group_message.DeleteDBClusterParameterGroupMessage]",
        ) -> OperationResponse[None]:
            import capo_docdb._operations.amazon_rd_sv19.delete_db_cluster_parameter_group

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.delete_db_cluster_parameter_group.delete_db_cluster_parameter_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.delete_db_cluster_parameter_group_message.DeleteDBClusterParameterGroupMessage = {}
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_db_cluster_snapshot(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_docdb.types.string.String"
        ] = None,
    ) -> "capo_docdb.types.delete_db_cluster_snapshot_result.DeleteDBClusterSnapshotResult":
        """<p>Deletes a cluster snapshot. If the snapshot is being copied, the copy operation is terminated.</p> <note> <p>The cluster snapshot must be in the <code>available</code> state to be deleted.</p> </note>

        Args:
            db_cluster_snapshot_identifier: <p>The identifier of the cluster snapshot to delete.</p> <p>Constraints: Must be the name of an existing cluster snapshot in the <code>available</code> state.</p>

        Raises:
            capo_docdb.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <code>DBClusterSnapshotIdentifier</code> doesn't refer to an existing cluster snapshot. </p>
            capo_docdb.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The provided value isn't a valid cluster snapshot state.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.delete_db_cluster_snapshot_message.DeleteDBClusterSnapshotMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.delete_db_cluster_snapshot_result.DeleteDBClusterSnapshotResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.delete_db_cluster_snapshot

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.delete_db_cluster_snapshot.delete_db_cluster_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.delete_db_cluster_snapshot_message.DeleteDBClusterSnapshotMessage = {}
        if db_cluster_snapshot_identifier is not None:
            input_["db_cluster_snapshot_identifier"] = db_cluster_snapshot_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_db_instance(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_instance_identifier: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.delete_db_instance_result.DeleteDBInstanceResult":
        """<p>Deletes a previously provisioned instance.</p>

        Args:
            db_instance_identifier: <p>The instance identifier for the instance to be deleted. This parameter isn't case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the name of an existing instance.</p> </li> </ul>

        Raises:
            capo_docdb.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <code>DBInstanceIdentifier</code> doesn't refer to an existing instance. </p>
            capo_docdb.errors.db_snapshot_already_exists_fault.DBSnapshotAlreadyExistsFault: <p> <code>DBSnapshotIdentifier</code> is already being used by an existing snapshot. </p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p> The specified instance isn't in the <i>available</i> state. </p>
            capo_docdb.errors.snapshot_quota_exceeded_fault.SnapshotQuotaExceededFault: <p>The request would cause you to exceed the allowed number of snapshots.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.delete_db_instance_message.DeleteDBInstanceMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.delete_db_instance_result.DeleteDBInstanceResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.delete_db_instance

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.delete_db_instance.delete_db_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.delete_db_instance_message.DeleteDBInstanceMessage = {}
        if db_instance_identifier is not None:
            input_["db_instance_identifier"] = db_instance_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_db_subnet_group(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_subnet_group_name: Optional["capo_docdb.types.string.String"] = None,
    ) -> None:
        """<p>Deletes a subnet group.</p> <note> <p>The specified database subnet group must not be associated with any DB instances.</p> </note>

        Args:
            db_subnet_group_name: <p>The name of the database subnet group to delete.</p> <note> <p>You can't delete the default subnet group.</p> </note> <p>Constraints:</p> <p>Must match the name of an existing <code>DBSubnetGroup</code>. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>

        Raises:
            capo_docdb.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <code>DBSubnetGroupName</code> doesn't refer to an existing subnet group. </p>
            capo_docdb.errors.invalid_db_subnet_group_state_fault.InvalidDBSubnetGroupStateFault: <p>The subnet group can't be deleted because it's in use.</p>
            capo_docdb.errors.invalid_db_subnet_state_fault.InvalidDBSubnetStateFault: <p> The subnet isn't in the <i>available</i> state. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.delete_db_subnet_group_message.DeleteDBSubnetGroupMessage]",
        ) -> OperationResponse[None]:
            import capo_docdb._operations.amazon_rd_sv19.delete_db_subnet_group

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.delete_db_subnet_group.delete_db_subnet_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.delete_db_subnet_group_message.DeleteDBSubnetGroupMessage = {}
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event_subscription(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        subscription_name: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.delete_event_subscription_result.DeleteEventSubscriptionResult":
        """<p>Deletes an Amazon DocumentDB event notification subscription.</p>

        Args:
            subscription_name: <p>The name of the Amazon DocumentDB event notification subscription that you want to delete.</p>

        Raises:
            capo_docdb.errors.invalid_event_subscription_state_fault.InvalidEventSubscriptionStateFault: <p>Someone else might be modifying a subscription. Wait a few seconds, and try again.</p>
            capo_docdb.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>The subscription name does not exist. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.delete_event_subscription_message.DeleteEventSubscriptionMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.delete_event_subscription_result.DeleteEventSubscriptionResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.delete_event_subscription

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.delete_event_subscription.delete_event_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.delete_event_subscription_message.DeleteEventSubscriptionMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_global_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
    ) -> "capo_docdb.types.delete_global_cluster_result.DeleteGlobalClusterResult":
        """<p>Deletes a global cluster. The primary and secondary clusters must already be detached or deleted before attempting to delete a global cluster.</p> <note> <p>This action only applies to Amazon DocumentDB clusters.</p> </note>

        Args:
            global_cluster_identifier: <p>The cluster identifier of the global cluster being deleted.</p>

        Raises:
            capo_docdb.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global cluster.</p>
            capo_docdb.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The requested operation can't be performed while the cluster is in this state.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.delete_global_cluster_message.DeleteGlobalClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.delete_global_cluster_result.DeleteGlobalClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.delete_global_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.delete_global_cluster.delete_global_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.delete_global_cluster_message.DeleteGlobalClusterMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_certificates(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        certificate_identifier: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.certificate_message.CertificateMessage":
        """<p>Returns a list of certificate authority (CA) certificates provided by Amazon DocumentDB for this Amazon Web Services account.</p>

        Args:
            certificate_identifier: <p>The user-supplied certificate identifier. If this parameter is specified, information for only the specified certificate is returned. If this parameter is omitted, a list of up to <code>MaxRecords</code> certificates is returned. This parameter is not case sensitive.</p> <p>Constraints</p> <ul> <li> <p>Must match an existing <code>CertificateIdentifier</code>.</p> </li> </ul>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints:</p> <ul> <li> <p>Minimum: 20</p> </li> <li> <p>Maximum: 100</p> </li> </ul>
            marker: <p>An optional pagination token provided by a previous <code>DescribeCertificates</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_docdb.errors.certificate_not_found_fault.CertificateNotFoundFault: <p> <code>CertificateIdentifier</code> doesn't refer to an existing certificate. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_certificates_message.DescribeCertificatesMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.certificate_message.CertificateMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_certificates

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_certificates.describe_certificates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_certificates_message.DescribeCertificatesMessage = {}
        if certificate_identifier is not None:
            input_["certificate_identifier"] = certificate_identifier
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_certificates(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        certificate_identifier: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "Iterator[capo_docdb.types.certificate.Certificate]":
        _token = marker
        while True:
            _response = self.describe_certificates(
                config_overrides=config_overrides,
                certificate_identifier=certificate_identifier,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("certificates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_db_cluster_parameter_groups(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.db_cluster_parameter_groups_message.DBClusterParameterGroupsMessage":
        """<p>Returns a list of <code>DBClusterParameterGroup</code> descriptions. If a <code>DBClusterParameterGroupName</code> parameter is specified, the list contains only the description of the specified cluster parameter group. </p>

        Args:
            db_cluster_parameter_group_name: <p>The name of a specific cluster parameter group to return details for.</p> <p>Constraints:</p> <ul> <li> <p>If provided, must match the name of an existing <code>DBClusterParameterGroup</code>.</p> </li> </ul>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_docdb.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <code>DBParameterGroupName</code> doesn't refer to an existing parameter group. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_db_cluster_parameter_groups_message.DescribeDBClusterParameterGroupsMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.db_cluster_parameter_groups_message.DBClusterParameterGroupsMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_db_cluster_parameter_groups

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_db_cluster_parameter_groups.describe_db_cluster_parameter_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_db_cluster_parameter_groups_message.DescribeDBClusterParameterGroupsMessage = {}
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_db_cluster_parameter_groups(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> (
        "Iterator[capo_docdb.types.db_cluster_parameter_group.DBClusterParameterGroup]"
    ):
        _token = marker
        while True:
            _response = self.describe_db_cluster_parameter_groups(
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

    def describe_db_cluster_parameters(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        source: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.db_cluster_parameter_group_details.DBClusterParameterGroupDetails":
        """<p>Returns the detailed parameter list for a particular cluster parameter group.</p>

        Args:
            db_cluster_parameter_group_name: <p>The name of a specific cluster parameter group to return parameter details for.</p> <p>Constraints:</p> <ul> <li> <p>If provided, must match the name of an existing <code>DBClusterParameterGroup</code>.</p> </li> </ul>
            source: <p> A value that indicates to return only parameters for a specific source. Parameter sources can be <code>engine</code>, <code>service</code>, or <code>customer</code>. </p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_docdb.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <code>DBParameterGroupName</code> doesn't refer to an existing parameter group. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_db_cluster_parameters_message.DescribeDBClusterParametersMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.db_cluster_parameter_group_details.DBClusterParameterGroupDetails"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_db_cluster_parameters

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_db_cluster_parameters.describe_db_cluster_parameters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_db_cluster_parameters_message.DescribeDBClusterParametersMessage = {}
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_db_cluster_parameters(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        source: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "Iterator[capo_docdb.types.parameter.Parameter]":
        _token = marker
        while True:
            _response = self.describe_db_cluster_parameters(
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

    def describe_db_clusters(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.db_cluster_message.DBClusterMessage":
        """<p>Returns information about provisioned Amazon DocumentDB clusters. This API operation supports pagination. For certain management features such as cluster and instance lifecycle management, Amazon DocumentDB leverages operational technology that is shared with Amazon RDS and Amazon Neptune. Use the <code>filterName=engine,Values=docdb</code> filter parameter to return only Amazon DocumentDB clusters.</p>

        Args:
            db_cluster_identifier: <p>The user-provided cluster identifier. If this parameter is specified, information from only the specific cluster is returned. This parameter isn't case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If provided, must match an existing <code>DBClusterIdentifier</code>.</p> </li> </ul>
            filters: <p>A filter that specifies one or more clusters to describe.</p> <p>Supported filters:</p> <ul> <li> <p> <code>db-cluster-id</code> - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list only includes information about the clusters identified by these ARNs.</p> </li> </ul>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_db_clusters_message.DescribeDBClustersMessage]",
        ) -> OperationResponse["capo_docdb.types.db_cluster_message.DBClusterMessage"]:
            import capo_docdb._operations.amazon_rd_sv19.describe_db_clusters

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_db_clusters.describe_db_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_db_clusters_message.DescribeDBClustersMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_db_clusters(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "Iterator[capo_docdb.types.db_cluster.DBCluster]":
        _token = marker
        while True:
            _response = self.describe_db_clusters(
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

    def describe_db_cluster_snapshot_attributes(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_docdb.types.string.String"
        ] = None,
    ) -> "capo_docdb.types.describe_db_cluster_snapshot_attributes_result.DescribeDBClusterSnapshotAttributesResult":
        """<p>Returns a list of cluster snapshot attribute names and values for a manual DB cluster snapshot.</p> <p>When you share snapshots with other Amazon Web Services accounts, <code>DescribeDBClusterSnapshotAttributes</code> returns the <code>restore</code> attribute and a list of IDs for the Amazon Web Services accounts that are authorized to copy or restore the manual cluster snapshot. If <code>all</code> is included in the list of values for the <code>restore</code> attribute, then the manual cluster snapshot is public and can be copied or restored by all Amazon Web Services accounts.</p>

        Args:
            db_cluster_snapshot_identifier: <p>The identifier for the cluster snapshot to describe the attributes for.</p>

        Raises:
            capo_docdb.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <code>DBClusterSnapshotIdentifier</code> doesn't refer to an existing cluster snapshot. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_db_cluster_snapshot_attributes_message.DescribeDBClusterSnapshotAttributesMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.describe_db_cluster_snapshot_attributes_result.DescribeDBClusterSnapshotAttributesResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_db_cluster_snapshot_attributes

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_db_cluster_snapshot_attributes.describe_db_cluster_snapshot_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_db_cluster_snapshot_attributes_message.DescribeDBClusterSnapshotAttributesMessage = {}
        if db_cluster_snapshot_identifier is not None:
            input_["db_cluster_snapshot_identifier"] = db_cluster_snapshot_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_db_cluster_snapshots(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        snapshot_type: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
        include_shared: Optional["capo_docdb.types.boolean.Boolean"] = None,
        include_public: Optional["capo_docdb.types.boolean.Boolean"] = None,
    ) -> "capo_docdb.types.db_cluster_snapshot_message.DBClusterSnapshotMessage":
        """<p>Returns information about cluster snapshots. This API operation supports pagination.</p>

        Args:
            db_cluster_identifier: <p>The ID of the cluster to retrieve the list of cluster snapshots for. This parameter can't be used with the <code>DBClusterSnapshotIdentifier</code> parameter. This parameter is not case sensitive. </p> <p>Constraints:</p> <ul> <li> <p>If provided, must match the identifier of an existing <code>DBCluster</code>.</p> </li> </ul>
            db_cluster_snapshot_identifier: <p>A specific cluster snapshot identifier to describe. This parameter can't be used with the <code>DBClusterIdentifier</code> parameter. This value is stored as a lowercase string. </p> <p>Constraints:</p> <ul> <li> <p>If provided, must match the identifier of an existing <code>DBClusterSnapshot</code>.</p> </li> <li> <p>If this identifier is for an automated snapshot, the <code>SnapshotType</code> parameter must also be specified.</p> </li> </ul>
            snapshot_type: <p>The type of cluster snapshots to be returned. You can specify one of the following values:</p> <ul> <li> <p> <code>automated</code> - Return all cluster snapshots that Amazon DocumentDB has automatically created for your Amazon Web Services account.</p> </li> <li> <p> <code>manual</code> - Return all cluster snapshots that you have manually created for your Amazon Web Services account.</p> </li> <li> <p> <code>shared</code> - Return all manual cluster snapshots that have been shared to your Amazon Web Services account.</p> </li> <li> <p> <code>public</code> - Return all cluster snapshots that have been marked as public.</p> </li> </ul> <p>If you don't specify a <code>SnapshotType</code> value, then both automated and manual cluster snapshots are returned. You can include shared cluster snapshots with these results by setting the <code>IncludeShared</code> parameter to <code>true</code>. You can include public cluster snapshots with these results by setting the<code>IncludePublic</code> parameter to <code>true</code>.</p> <p>The <code>IncludeShared</code> and <code>IncludePublic</code> parameters don't apply for <code>SnapshotType</code> values of <code>manual</code> or <code>automated</code>. The <code>IncludePublic</code> parameter doesn't apply when <code>SnapshotType</code> is set to <code>shared</code>. The <code>IncludeShared</code> parameter doesn't apply when <code>SnapshotType</code> is set to <code>public</code>.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>
            include_shared: <p>Set to <code>true</code> to include shared manual cluster snapshots from other Amazon Web Services accounts that this Amazon Web Services account has been given permission to copy or restore, and otherwise <code>false</code>. The default is <code>false</code>.</p>
            include_public: <p>Set to <code>true</code> to include manual cluster snapshots that are public and can be copied or restored by any Amazon Web Services account, and otherwise <code>false</code>. The default is <code>false</code>.</p>

        Raises:
            capo_docdb.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <code>DBClusterSnapshotIdentifier</code> doesn't refer to an existing cluster snapshot. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_db_cluster_snapshots_message.DescribeDBClusterSnapshotsMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.db_cluster_snapshot_message.DBClusterSnapshotMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_db_cluster_snapshots

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_db_cluster_snapshots.describe_db_cluster_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_db_cluster_snapshots_message.DescribeDBClusterSnapshotsMessage = {}
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_db_cluster_snapshots(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        snapshot_type: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
        include_shared: Optional["capo_docdb.types.boolean.Boolean"] = None,
        include_public: Optional["capo_docdb.types.boolean.Boolean"] = None,
    ) -> "Iterator[capo_docdb.types.db_cluster_snapshot.DBClusterSnapshot]":
        _token = marker
        while True:
            _response = self.describe_db_cluster_snapshots(
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

    def describe_db_engine_versions(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        engine: Optional["capo_docdb.types.string.String"] = None,
        engine_version: Optional["capo_docdb.types.string.String"] = None,
        db_parameter_group_family: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
        default_only: Optional["capo_docdb.types.boolean.Boolean"] = None,
        list_supported_character_sets: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        list_supported_timezones: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_docdb.types.db_engine_version_message.DBEngineVersionMessage":
        """<p>Returns a list of the available engines.</p>

        Args:
            engine: <p>The database engine to return.</p>
            engine_version: <p>The database engine version to return.</p> <p>Example: <code>3.6.0</code> </p>
            db_parameter_group_family: <p>The name of a specific parameter group family to return details for.</p> <p>Constraints:</p> <ul> <li> <p>If provided, must match an existing <code>DBParameterGroupFamily</code>.</p> </li> </ul>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>
            default_only: <p>Indicates that only the default version of the specified engine or engine and major version combination is returned.</p>
            list_supported_character_sets: <p>If this parameter is specified and the requested engine supports the <code>CharacterSetName</code> parameter for <code>CreateDBInstance</code>, the response includes a list of supported character sets for each engine version. </p>
            list_supported_timezones: <p>If this parameter is specified and the requested engine supports the <code>TimeZone</code> parameter for <code>CreateDBInstance</code>, the response includes a list of supported time zones for each engine version. </p>

        Raises:
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_db_engine_versions_message.DescribeDBEngineVersionsMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.db_engine_version_message.DBEngineVersionMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_db_engine_versions

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_db_engine_versions.describe_db_engine_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_db_engine_versions_message.DescribeDBEngineVersionsMessage = {}
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_db_engine_versions(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        engine: Optional["capo_docdb.types.string.String"] = None,
        engine_version: Optional["capo_docdb.types.string.String"] = None,
        db_parameter_group_family: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
        default_only: Optional["capo_docdb.types.boolean.Boolean"] = None,
        list_supported_character_sets: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        list_supported_timezones: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "Iterator[capo_docdb.types.db_engine_version.DBEngineVersion]":
        _token = marker
        while True:
            _response = self.describe_db_engine_versions(
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

    def describe_db_instances(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_instance_identifier: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.db_instance_message.DBInstanceMessage":
        """<p>Returns information about provisioned Amazon DocumentDB instances. This API supports pagination.</p>

        Args:
            db_instance_identifier: <p>The user-provided instance identifier. If this parameter is specified, information from only the specific instance is returned. This parameter isn't case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>If provided, must match the identifier of an existing <code>DBInstance</code>.</p> </li> </ul>
            filters: <p>A filter that specifies one or more instances to describe.</p> <p>Supported filters:</p> <ul> <li> <p> <code>db-cluster-id</code> - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list includes only the information about the instances that are associated with the clusters that are identified by these ARNs.</p> </li> <li> <p> <code>db-instance-id</code> - Accepts instance identifiers and instance ARNs. The results list includes only the information about the instances that are identified by these ARNs.</p> </li> </ul>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_docdb.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <code>DBInstanceIdentifier</code> doesn't refer to an existing instance. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_db_instances_message.DescribeDBInstancesMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.db_instance_message.DBInstanceMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_db_instances

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_db_instances.describe_db_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_db_instances_message.DescribeDBInstancesMessage = {}
        if db_instance_identifier is not None:
            input_["db_instance_identifier"] = db_instance_identifier
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_db_instances(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_instance_identifier: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "Iterator[capo_docdb.types.db_instance.DBInstance]":
        _token = marker
        while True:
            _response = self.describe_db_instances(
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

    def describe_db_subnet_groups(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_subnet_group_name: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.db_subnet_group_message.DBSubnetGroupMessage":
        """<p>Returns a list of <code>DBSubnetGroup</code> descriptions. If a <code>DBSubnetGroupName</code> is specified, the list will contain only the descriptions of the specified <code>DBSubnetGroup</code>.</p>

        Args:
            db_subnet_group_name: <p>The name of the subnet group to return details for.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_docdb.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <code>DBSubnetGroupName</code> doesn't refer to an existing subnet group. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_db_subnet_groups_message.DescribeDBSubnetGroupsMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.db_subnet_group_message.DBSubnetGroupMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_db_subnet_groups

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_db_subnet_groups.describe_db_subnet_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_db_subnet_groups_message.DescribeDBSubnetGroupsMessage = {}
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_db_subnet_groups(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_subnet_group_name: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "Iterator[capo_docdb.types.db_subnet_group.DBSubnetGroup]":
        _token = marker
        while True:
            _response = self.describe_db_subnet_groups(
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

    def describe_engine_default_cluster_parameters(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_parameter_group_family: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.describe_engine_default_cluster_parameters_result.DescribeEngineDefaultClusterParametersResult":
        """<p>Returns the default engine and system parameter information for the cluster database engine.</p>

        Args:
            db_parameter_group_family: <p>The name of the cluster parameter group family to return the engine parameter information for.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_engine_default_cluster_parameters_message.DescribeEngineDefaultClusterParametersMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.describe_engine_default_cluster_parameters_result.DescribeEngineDefaultClusterParametersResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_engine_default_cluster_parameters

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_engine_default_cluster_parameters.describe_engine_default_cluster_parameters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_engine_default_cluster_parameters_message.DescribeEngineDefaultClusterParametersMessage = {}
        if db_parameter_group_family is not None:
            input_["db_parameter_group_family"] = db_parameter_group_family
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_event_categories(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        source_type: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
    ) -> "capo_docdb.types.event_categories_message.EventCategoriesMessage":
        """<p>Displays a list of categories for all event source types, or, if specified, for a specified source type. </p>

        Args:
            source_type: <p>The type of source that is generating the events.</p> <p>Valid values: <code>db-instance</code>, <code>db-parameter-group</code>, <code>db-security-group</code> </p>
            filters: <p>This parameter is not currently supported.</p>

        Raises:
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_event_categories_message.DescribeEventCategoriesMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.event_categories_message.EventCategoriesMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_event_categories

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_event_categories.describe_event_categories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_event_categories_message.DescribeEventCategoriesMessage = {}
        if source_type is not None:
            input_["source_type"] = source_type
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_events(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        source_identifier: Optional["capo_docdb.types.string.String"] = None,
        source_type: Optional["capo_docdb.types.source_type.SourceType"] = None,
        start_time: Optional["capo_docdb.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_docdb.types.t_stamp.TStamp"] = None,
        duration: Optional["capo_docdb.types.integer_optional.IntegerOptional"] = None,
        event_categories: Optional[
            "capo_docdb.types.event_categories_list.EventCategoriesList"
        ] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.events_message.EventsMessage":
        """<p>Returns events related to instances, security groups, snapshots, and DB parameter groups for the past 14 days. You can obtain events specific to a particular DB instance, security group, snapshot, or parameter group by providing the name as a parameter. By default, the events of the past hour are returned.</p>

        Args:
            source_identifier: <p>The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.</p> <p>Constraints:</p> <ul> <li> <p>If <code>SourceIdentifier</code> is provided, <code>SourceType</code> must also be provided.</p> </li> <li> <p>If the source type is <code>DBInstance</code>, a <code>DBInstanceIdentifier</code> must be provided.</p> </li> <li> <p>If the source type is <code>DBSecurityGroup</code>, a <code>DBSecurityGroupName</code> must be provided.</p> </li> <li> <p>If the source type is <code>DBParameterGroup</code>, a <code>DBParameterGroupName</code> must be provided.</p> </li> <li> <p>If the source type is <code>DBSnapshot</code>, a <code>DBSnapshotIdentifier</code> must be provided.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            source_type: <p>The event source to retrieve events for. If no value is specified, all events are returned.</p>
            start_time: <p> The beginning of the time interval to retrieve events for, specified in ISO 8601 format. </p> <p>Example: 2009-07-08T18:00Z</p>
            end_time: <p> The end of the time interval for which to retrieve events, specified in ISO 8601 format. </p> <p>Example: 2009-07-08T18:00Z</p>
            duration: <p>The number of minutes to retrieve events for.</p> <p>Default: 60</p>
            event_categories: <p>A list of event categories that trigger notifications for an event notification subscription.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_events_message.DescribeEventsMessage]",
        ) -> OperationResponse["capo_docdb.types.events_message.EventsMessage"]:
            import capo_docdb._operations.amazon_rd_sv19.describe_events

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_events.describe_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_events_message.DescribeEventsMessage = {}
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_events(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        source_identifier: Optional["capo_docdb.types.string.String"] = None,
        source_type: Optional["capo_docdb.types.source_type.SourceType"] = None,
        start_time: Optional["capo_docdb.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_docdb.types.t_stamp.TStamp"] = None,
        duration: Optional["capo_docdb.types.integer_optional.IntegerOptional"] = None,
        event_categories: Optional[
            "capo_docdb.types.event_categories_list.EventCategoriesList"
        ] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "Iterator[capo_docdb.types.event.Event]":
        _token = marker
        while True:
            _response = self.describe_events(
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

    def describe_event_subscriptions(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        subscription_name: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.event_subscriptions_message.EventSubscriptionsMessage":
        """<p>Lists all the subscription descriptions for a customer account. The description for a subscription includes <code>SubscriptionName</code>, <code>SNSTopicARN</code>, <code>CustomerID</code>, <code>SourceType</code>, <code>SourceID</code>, <code>CreationTime</code>, and <code>Status</code>.</p> <p>If you specify a <code>SubscriptionName</code>, lists the description for that subscription.</p>

        Args:
            subscription_name: <p>The name of the Amazon DocumentDB event notification subscription that you want to describe.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_docdb.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>The subscription name does not exist. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_event_subscriptions_message.DescribeEventSubscriptionsMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.event_subscriptions_message.EventSubscriptionsMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_event_subscriptions

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_event_subscriptions.describe_event_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_event_subscriptions_message.DescribeEventSubscriptionsMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_event_subscriptions(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        subscription_name: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "Iterator[capo_docdb.types.event_subscription.EventSubscription]":
        _token = marker
        while True:
            _response = self.describe_event_subscriptions(
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

    def describe_global_clusters(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.global_clusters_message.GlobalClustersMessage":
        """<p>Returns information about Amazon DocumentDB global clusters. This API supports pagination.</p> <note> <p>This action only applies to Amazon DocumentDB clusters.</p> </note>

        Args:
            global_cluster_identifier: <p>The user-supplied cluster identifier. If this parameter is specified, information from only the specific cluster is returned. This parameter isn't case-sensitive.</p>
            filters: <p>A filter that specifies one or more global DB clusters to describe.</p> <p>Supported filters: <code>db-cluster-id</code> accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list will only include information about the clusters identified by these ARNs.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results. </p>
            marker: <p>An optional pagination token provided by a previous <code>DescribeGlobalClusters</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_docdb.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global cluster.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_global_clusters_message.DescribeGlobalClustersMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.global_clusters_message.GlobalClustersMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_global_clusters

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_global_clusters.describe_global_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_global_clusters_message.DescribeGlobalClustersMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_global_clusters(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "Iterator[capo_docdb.types.global_cluster.GlobalCluster]":
        _token = marker
        while True:
            _response = self.describe_global_clusters(
                config_overrides=config_overrides,
                global_cluster_identifier=global_cluster_identifier,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            _page = _resolve_path(_response, ("global_clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_orderable_db_instance_options(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        engine: Optional["capo_docdb.types.string.String"] = None,
        engine_version: Optional["capo_docdb.types.string.String"] = None,
        db_instance_class: Optional["capo_docdb.types.string.String"] = None,
        license_model: Optional["capo_docdb.types.string.String"] = None,
        vpc: Optional["capo_docdb.types.boolean_optional.BooleanOptional"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.orderable_db_instance_options_message.OrderableDBInstanceOptionsMessage":
        """<p>Returns a list of orderable instance options for the specified engine.</p>

        Args:
            engine: <p>The name of the engine to retrieve instance options for.</p>
            engine_version: <p>The engine version filter value. Specify this parameter to show only the available offerings that match the specified engine version.</p>
            db_instance_class: <p>The instance class filter value. Specify this parameter to show only the available offerings that match the specified instance class.</p>
            license_model: <p>The license model filter value. Specify this parameter to show only the available offerings that match the specified license model.</p>
            vpc: <p>The virtual private cloud (VPC) filter value. Specify this parameter to show only the available VPC or non-VPC offerings.</p>
            filters: <p>This parameter is not currently supported.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_orderable_db_instance_options_message.DescribeOrderableDBInstanceOptionsMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.orderable_db_instance_options_message.OrderableDBInstanceOptionsMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_orderable_db_instance_options

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_orderable_db_instance_options.describe_orderable_db_instance_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_orderable_db_instance_options_message.DescribeOrderableDBInstanceOptionsMessage = {}
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_orderable_db_instance_options(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        engine: Optional["capo_docdb.types.string.String"] = None,
        engine_version: Optional["capo_docdb.types.string.String"] = None,
        db_instance_class: Optional["capo_docdb.types.string.String"] = None,
        license_model: Optional["capo_docdb.types.string.String"] = None,
        vpc: Optional["capo_docdb.types.boolean_optional.BooleanOptional"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
    ) -> "Iterator[capo_docdb.types.orderable_db_instance_option.OrderableDBInstanceOption]":
        _token = marker
        while True:
            _response = self.describe_orderable_db_instance_options(
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

    def describe_pending_maintenance_actions(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        resource_identifier: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_docdb.types.pending_maintenance_actions_message.PendingMaintenanceActionsMessage":
        """<p>Returns a list of resources (for example, instances) that have at least one pending maintenance action.</p>

        Args:
            resource_identifier: <p>The ARN of a resource to return pending maintenance actions for.</p>
            filters: <p>A filter that specifies one or more resources to return pending maintenance actions for.</p> <p>Supported filters:</p> <ul> <li> <p> <code>db-cluster-id</code> - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list includes only pending maintenance actions for the clusters identified by these ARNs.</p> </li> <li> <p> <code>db-instance-id</code> - Accepts instance identifiers and instance ARNs. The results list includes only pending maintenance actions for the DB instances identified by these ARNs.</p> </li> </ul>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>

        Raises:
            capo_docdb.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The specified resource ID was not found.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.describe_pending_maintenance_actions_message.DescribePendingMaintenanceActionsMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.pending_maintenance_actions_message.PendingMaintenanceActionsMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.describe_pending_maintenance_actions

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.describe_pending_maintenance_actions.describe_pending_maintenance_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.describe_pending_maintenance_actions_message.DescribePendingMaintenanceActionsMessage = {}
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if filters is not None:
            input_["filters"] = filters
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_pending_maintenance_actions(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        resource_identifier: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
        marker: Optional["capo_docdb.types.string.String"] = None,
        max_records: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "Iterator[capo_docdb.types.resource_pending_maintenance_actions.ResourcePendingMaintenanceActions]":
        _token = marker
        while True:
            _response = self.describe_pending_maintenance_actions(
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

    def failover_db_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        target_db_instance_identifier: Optional[
            "capo_docdb.types.string.String"
        ] = None,
    ) -> "capo_docdb.types.failover_db_cluster_result.FailoverDBClusterResult":
        """<p>Forces a failover for a cluster.</p> <p>A failover for a cluster promotes one of the Amazon DocumentDB replicas (read-only instances) in the cluster to be the primary instance (the cluster writer).</p> <p>If the primary instance fails, Amazon DocumentDB automatically fails over to an Amazon DocumentDB replica, if one exists. You can force a failover when you want to simulate a failure of a primary instance for testing.</p>

        Args:
            db_cluster_identifier: <p>A cluster identifier to force a failover for. This parameter is not case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing <code>DBCluster</code>.</p> </li> </ul>
            target_db_instance_identifier: <p>The name of the instance to promote to the primary instance.</p> <p>You must specify the instance identifier for an Amazon DocumentDB replica in the cluster. For example, <code>mydbcluster-replica1</code>.</p>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p> The specified instance isn't in the <i>available</i> state. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.failover_db_cluster_message.FailoverDBClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.failover_db_cluster_result.FailoverDBClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.failover_db_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.failover_db_cluster.failover_db_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.failover_db_cluster_message.FailoverDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier
        if target_db_instance_identifier is not None:
            input_["target_db_instance_identifier"] = target_db_instance_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def failover_global_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        target_db_cluster_identifier: Optional[
            "capo_docdb.types.db_cluster_identifier.DBClusterIdentifier"
        ] = None,
        allow_data_loss: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        switchover: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_docdb.types.failover_global_cluster_result.FailoverGlobalClusterResult":
        """<p>Promotes the specified secondary DB cluster to be the primary DB cluster in the global cluster when failing over a global cluster occurs.</p> <p>Use this operation to respond to an unplanned event, such as a regional disaster in the primary region. Failing over can result in a loss of write transaction data that wasn't replicated to the chosen secondary before the failover event occurred. However, the recovery process that promotes a DB instance on the chosen seconday DB cluster to be the primary writer DB instance guarantees that the data is in a transactionally consistent state.</p>

        Args:
            global_cluster_identifier: <p>The identifier of the Amazon DocumentDB global cluster to apply this operation. The identifier is the unique key assigned by the user when the cluster is created. In other words, it's the name of the global cluster.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing global cluster.</p> </li> <li> <p>Minimum length of 1. Maximum length of 255.</p> </li> </ul> <p>Pattern: <code>[A-Za-z][0-9A-Za-z-:._]*</code> </p>
            target_db_cluster_identifier: <p>The identifier of the secondary Amazon DocumentDB cluster that you want to promote to the primary for the global cluster. Use the Amazon Resource Name (ARN) for the identifier so that Amazon DocumentDB can locate the cluster in its Amazon Web Services region.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing secondary cluster.</p> </li> <li> <p>Minimum length of 1. Maximum length of 255.</p> </li> </ul> <p>Pattern: <code>[A-Za-z][0-9A-Za-z-:._]*</code> </p>
            allow_data_loss: <p>Specifies whether to allow data loss for this global cluster operation. Allowing data loss triggers a global failover operation.</p> <p>If you don't specify <code>AllowDataLoss</code>, the global cluster operation defaults to a switchover.</p> <p>Constraints:</p> <ul> <li> <p>Can't be specified together with the <code>Switchover</code> parameter.</p> </li> </ul>
            switchover: <p>Specifies whether to switch over this global database cluster.</p> <p>Constraints:</p> <ul> <li> <p>Can't be specified together with the <code>AllowDataLoss</code> parameter.</p> </li> </ul>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global cluster.</p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The requested operation can't be performed while the cluster is in this state.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.failover_global_cluster_message.FailoverGlobalClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.failover_global_cluster_result.FailoverGlobalClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.failover_global_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.failover_global_cluster.failover_global_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.failover_global_cluster_message.FailoverGlobalClusterMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if target_db_cluster_identifier is not None:
            input_["target_db_cluster_identifier"] = target_db_cluster_identifier
        if allow_data_loss is not None:
            input_["allow_data_loss"] = allow_data_loss
        if switchover is not None:
            input_["switchover"] = switchover

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        resource_name: Optional["capo_docdb.types.string.String"] = None,
        filters: Optional["capo_docdb.types.filter_list.FilterList"] = None,
    ) -> "capo_docdb.types.tag_list_message.TagListMessage":
        """<p>Lists all tags on an Amazon DocumentDB resource.</p>

        Args:
            resource_name: <p>The Amazon DocumentDB resource with tags to be listed. This value is an Amazon Resource Name (ARN).</p>
            filters: <p>This parameter is not currently supported.</p>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <code>DBInstanceIdentifier</code> doesn't refer to an existing instance. </p>
            capo_docdb.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault: <p> <code>DBSnapshotIdentifier</code> doesn't refer to an existing snapshot. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.list_tags_for_resource_message.ListTagsForResourceMessage]",
        ) -> OperationResponse["capo_docdb.types.tag_list_message.TagListMessage"]:
            import capo_docdb._operations.amazon_rd_sv19.list_tags_for_resource

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.list_tags_for_resource_message.ListTagsForResourceMessage = {}
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_db_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        new_db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        apply_immediately: Optional["capo_docdb.types.boolean.Boolean"] = None,
        backup_retention_period: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_docdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        port: Optional["capo_docdb.types.integer_optional.IntegerOptional"] = None,
        master_user_password: Optional["capo_docdb.types.string.String"] = None,
        preferred_backup_window: Optional["capo_docdb.types.string.String"] = None,
        preferred_maintenance_window: Optional["capo_docdb.types.string.String"] = None,
        cloudwatch_logs_export_configuration: Optional[
            "capo_docdb.types.cloudwatch_logs_export_configuration.CloudwatchLogsExportConfiguration"
        ] = None,
        engine_version: Optional["capo_docdb.types.string.String"] = None,
        allow_major_version_upgrade: Optional[
            "capo_docdb.types.boolean.Boolean"
        ] = None,
        deletion_protection: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        storage_type: Optional["capo_docdb.types.string.String"] = None,
        serverless_v2_scaling_configuration: Optional[
            "capo_docdb.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
        ] = None,
        manage_master_user_password: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        master_user_secret_kms_key_id: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        rotate_master_user_password: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        network_type: Optional["capo_docdb.types.string.String"] = None,
        copy_tags_to_snapshot: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_docdb.types.modify_db_cluster_result.ModifyDBClusterResult":
        """<p>Modifies a setting for an Amazon DocumentDB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. </p>

        Args:
            db_cluster_identifier: <p>The cluster identifier for the cluster that is being modified. This parameter is not case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing <code>DBCluster</code>.</p> </li> </ul>
            new_db_cluster_identifier: <p>The new cluster identifier for the cluster when renaming a cluster. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster2</code> </p>
            apply_immediately: <p>A value that specifies whether the changes in this request and any pending changes are asynchronously applied as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the cluster. If this parameter is set to <code>false</code>, changes to the cluster are applied during the next maintenance window.</p> <p>The <code>ApplyImmediately</code> parameter affects only the <code>NewDBClusterIdentifier</code> and <code>MasterUserPassword</code> values. If you set this parameter value to <code>false</code>, the changes to the <code>NewDBClusterIdentifier</code> and <code>MasterUserPassword</code> values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the <code>ApplyImmediately</code> parameter.</p> <p>Default: <code>false</code> </p>
            backup_retention_period: <p>The number of days for which automated backups are retained. You must specify a minimum value of 1.</p> <p>Default: 1</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 1 to 35.</p> </li> </ul>
            db_cluster_parameter_group_name: <p>The name of the cluster parameter group to use for the cluster.</p>
            vpc_security_group_ids: <p>A list of virtual private cloud (VPC) security groups that the cluster will belong to.</p>
            port: <p>The port number on which the cluster accepts connections.</p> <p>Constraints: Must be a value from <code>1150</code> to <code>65535</code>. </p> <p>Default: The same port as the original cluster.</p>
            master_user_password: <p>The password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@).</p> <p>Constraints: Must contain from 8 to 100 characters.</p>
            preferred_backup_window: <p>The daily time range during which automated backups are created if automated backups are enabled, using the <code>BackupRetentionPeriod</code> parameter. </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. </p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>
            preferred_maintenance_window: <p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p>Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week. </p> <p>Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p>Constraints: Minimum 30-minute window.</p>
            cloudwatch_logs_export_configuration: <p>The configuration setting for the log types to be enabled for export to Amazon CloudWatch Logs for a specific instance or cluster. The <code>EnableLogTypes</code> and <code>DisableLogTypes</code> arrays determine which logs are exported (or not exported) to CloudWatch Logs.</p>
            engine_version: <p>The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless <code>ApplyImmediately</code> is enabled.</p> <p>To list all of the available engine versions for Amazon DocumentDB use the following command:</p> <p> <code>aws docdb describe-db-engine-versions --engine docdb --query "DBEngineVersions[].EngineVersion"</code> </p>
            allow_major_version_upgrade: <p>A value that indicates whether major version upgrades are allowed.</p> <p>Constraints:</p> <ul> <li> <p>You must allow major version upgrades when specifying a value for the <code>EngineVersion</code> parameter that is a different major version than the cluster's current version.</p> </li> <li> <p>Since some parameters are version specific, changing them requires executing a new <code>ModifyDBCluster</code> API call after the in-place MVU completes.</p> </li> </ul> <note> <p>Performing an MVU directly impacts the following parameters:</p> <ul> <li> <p> <code>MasterUserPassword</code> </p> </li> <li> <p> <code>NewDBClusterIdentifier</code> </p> </li> <li> <p> <code>VpcSecurityGroupIds</code> </p> </li> <li> <p> <code>Port</code> </p> </li> </ul> </note>
            deletion_protection: <p>Specifies whether this cluster can be deleted. If <code>DeletionProtection</code> is enabled, the cluster cannot be deleted unless it is modified and <code>DeletionProtection</code> is disabled. <code>DeletionProtection</code> protects clusters from being accidentally deleted.</p>
            storage_type: <p>The storage type to associate with the DB cluster.</p> <p>For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the <i>Amazon DocumentDB Developer Guide</i>.</p> <p>Valid values for storage type - <code>standard | iopt1</code> </p> <p>Default value is <code>standard </code> </p>
            serverless_v2_scaling_configuration: <p>Contains the scaling configuration of an Amazon DocumentDB Serverless cluster.</p>
            manage_master_user_password: <p>Specifies whether to manage the master user password with Amazon Web Services Secrets Manager. If the cluster doesn't manage the master user password with Amazon Web Services Secrets Manager, you can turn on this management. In this case, you can't specify <code>MasterUserPassword</code>. If the cluster already manages the master user password with Amazon Web Services Secrets Manager, and you specify that the master user password is not managed with Amazon Web Services Secrets Manager, then you must specify <code>MasterUserPassword</code>. In this case, Amazon DocumentDB deletes the secret and uses the new password for the master user specified by <code>MasterUserPassword</code>.</p>
            master_user_secret_kms_key_id: <p>The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.</p> <p>This setting is valid only if both of the following conditions are met:</p> <ul> <li> <p>The cluster doesn't manage the master user password in Amazon Web Services Secrets Manager. If the cluster already manages the master user password in Amazon Web Services Secrets Manager, you can't change the KMS key that is used to encrypt the secret.</p> </li> <li> <p>You are enabling <code>ManageMasterUserPassword</code> to manage the master user password in Amazon Web Services Secrets Manager. If you are turning on <code>ManageMasterUserPassword</code> and don't specify <code>MasterUserSecretKmsKeyId</code>, then the <code>aws/secretsmanager</code> KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the <code>aws/secretsmanager</code> KMS key to encrypt the secret, and you must use a customer managed KMS key.</p> </li> </ul> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>
            rotate_master_user_password: <p>Specifies whether to rotate the secret managed by Amazon Web Services Secrets Manager for the master user password.</p> <p>This setting is valid only if the master user password is managed by Amazon DocumentDB in Amazon Web Services Secrets Manager for the cluster. The secret value contains the updated password.</p> <p>Constraint: You must apply the change immediately when rotating the master user password.</p>
            network_type: <p>The network type of the cluster.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/vpc-clusters.html">DocumentDB clusters in a VPC</a> in the Amazon DocumentDB Developer Guide.</p> <p>Valid Values: <code>IPV4</code> | <code>DUAL</code> </p>
            copy_tags_to_snapshot: <p>Specifies whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.</p>

        Raises:
            capo_docdb.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault: <p>You already have a cluster with the given identifier.</p>
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.db_cluster_parameter_group_not_found_fault.DBClusterParameterGroupNotFoundFault: <p> <code>DBClusterParameterGroupName</code> doesn't refer to an existing cluster parameter group. </p>
            capo_docdb.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <code>DBSubnetGroupName</code> doesn't refer to an existing subnet group. </p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p> The specified instance isn't in the <i>available</i> state. </p>
            capo_docdb.errors.invalid_db_security_group_state_fault.InvalidDBSecurityGroupStateFault: <p>The state of the security group doesn't allow deletion.</p>
            capo_docdb.errors.invalid_db_subnet_group_state_fault.InvalidDBSubnetGroupStateFault: <p>The subnet group can't be deleted because it's in use.</p>
            capo_docdb.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is not valid, or multiple subnets were requested that are not all in a common virtual private cloud (VPC).</p>
            capo_docdb.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The subnet group doesn't cover all Availability Zones after it is created because of changes that were made.</p>
            capo_docdb.errors.network_type_not_supported.NetworkTypeNotSupported: <p>The network type is not supported by either <code>DBSubnetGroup</code> or the DB engine version.</p>
            capo_docdb.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>The request would cause you to exceed the allowed amount of storage available across all instances.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.modify_db_cluster_message.ModifyDBClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.modify_db_cluster_result.ModifyDBClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.modify_db_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.modify_db_cluster.modify_db_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.modify_db_cluster_message.ModifyDBClusterMessage = {}
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
        if preferred_backup_window is not None:
            input_["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if cloudwatch_logs_export_configuration is not None:
            input_["cloudwatch_logs_export_configuration"] = (
                cloudwatch_logs_export_configuration
            )
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if allow_major_version_upgrade is not None:
            input_["allow_major_version_upgrade"] = allow_major_version_upgrade
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if serverless_v2_scaling_configuration is not None:
            input_["serverless_v2_scaling_configuration"] = (
                serverless_v2_scaling_configuration
            )
        if manage_master_user_password is not None:
            input_["manage_master_user_password"] = manage_master_user_password
        if master_user_secret_kms_key_id is not None:
            input_["master_user_secret_kms_key_id"] = master_user_secret_kms_key_id
        if rotate_master_user_password is not None:
            input_["rotate_master_user_password"] = rotate_master_user_password
        if network_type is not None:
            input_["network_type"] = network_type
        if copy_tags_to_snapshot is not None:
            input_["copy_tags_to_snapshot"] = copy_tags_to_snapshot

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_db_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        parameters: Optional["capo_docdb.types.parameters_list.ParametersList"] = None,
    ) -> "capo_docdb.types.db_cluster_parameter_group_name_message.DBClusterParameterGroupNameMessage":
        """<p> Modifies the parameters of a cluster parameter group. To modify more than one parameter, submit a list of the following: <code>ParameterName</code>, <code>ParameterValue</code>, and <code>ApplyMethod</code>. A maximum of 20 parameters can be modified in a single request. </p> <note> <p>Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot or maintenance window before the change can take effect.</p> </note> <important> <p>After you create a cluster parameter group, you should wait at least 5 minutes before creating your first cluster that uses that cluster parameter group as the default parameter group. This allows Amazon DocumentDB to fully complete the create action before the parameter group is used as the default for a new cluster. This step is especially important for parameters that are critical when creating the default database for a cluster, such as the character set for the default database defined by the <code>character_set_database</code> parameter.</p> </important>

        Args:
            db_cluster_parameter_group_name: <p>The name of the cluster parameter group to modify.</p>
            parameters: <p>A list of parameters in the cluster parameter group to modify.</p>

        Raises:
            capo_docdb.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <code>DBParameterGroupName</code> doesn't refer to an existing parameter group. </p>
            capo_docdb.errors.invalid_db_parameter_group_state_fault.InvalidDBParameterGroupStateFault: <p>The parameter group is in use, or it is in a state that is not valid. If you are trying to delete the parameter group, you can't delete it when the parameter group is in this state.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.modify_db_cluster_parameter_group_message.ModifyDBClusterParameterGroupMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.db_cluster_parameter_group_name_message.DBClusterParameterGroupNameMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.modify_db_cluster_parameter_group

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.modify_db_cluster_parameter_group.modify_db_cluster_parameter_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.modify_db_cluster_parameter_group_message.ModifyDBClusterParameterGroupMessage = {}
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_db_cluster_snapshot_attribute(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_snapshot_identifier: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        attribute_name: Optional["capo_docdb.types.string.String"] = None,
        values_to_add: Optional[
            "capo_docdb.types.attribute_value_list.AttributeValueList"
        ] = None,
        values_to_remove: Optional[
            "capo_docdb.types.attribute_value_list.AttributeValueList"
        ] = None,
    ) -> "capo_docdb.types.modify_db_cluster_snapshot_attribute_result.ModifyDBClusterSnapshotAttributeResult":
        """<p>Adds an attribute and values to, or removes an attribute and values from, a manual cluster snapshot.</p> <p>To share a manual cluster snapshot with other Amazon Web Services accounts, specify <code>restore</code> as the <code>AttributeName</code>, and use the <code>ValuesToAdd</code> parameter to add a list of IDs of the Amazon Web Services accounts that are authorized to restore the manual cluster snapshot. Use the value <code>all</code> to make the manual cluster snapshot public, which means that it can be copied or restored by all Amazon Web Services accounts. Do not add the <code>all</code> value for any manual cluster snapshots that contain private information that you don't want available to all Amazon Web Services accounts. If a manual cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized Amazon Web Services account IDs for the <code>ValuesToAdd</code> parameter. You can't use <code>all</code> as a value for that parameter in this case.</p>

        Args:
            db_cluster_snapshot_identifier: <p>The identifier for the cluster snapshot to modify the attributes for.</p>
            attribute_name: <p>The name of the cluster snapshot attribute to modify.</p> <p>To manage authorization for other Amazon Web Services accounts to copy or restore a manual cluster snapshot, set this value to <code>restore</code>.</p>
            values_to_add: <p>A list of cluster snapshot attributes to add to the attribute specified by <code>AttributeName</code>.</p> <p>To authorize other Amazon Web Services accounts to copy or restore a manual cluster snapshot, set this list to include one or more Amazon Web Services account IDs. To make the manual cluster snapshot restorable by any Amazon Web Services account, set it to <code>all</code>. Do not add the <code>all</code> value for any manual cluster snapshots that contain private information that you don't want to be available to all Amazon Web Services accounts.</p>
            values_to_remove: <p>A list of cluster snapshot attributes to remove from the attribute specified by <code>AttributeName</code>.</p> <p>To remove authorization for other Amazon Web Services accounts to copy or restore a manual cluster snapshot, set this list to include one or more Amazon Web Services account identifiers. To remove authorization for any Amazon Web Services account to copy or restore the cluster snapshot, set it to <code>all</code> . If you specify <code>all</code>, an Amazon Web Services account whose account ID is explicitly added to the <code>restore</code> attribute can still copy or restore a manual cluster snapshot.</p>

        Raises:
            capo_docdb.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <code>DBClusterSnapshotIdentifier</code> doesn't refer to an existing cluster snapshot. </p>
            capo_docdb.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The provided value isn't a valid cluster snapshot state.</p>
            capo_docdb.errors.shared_snapshot_quota_exceeded_fault.SharedSnapshotQuotaExceededFault: <p>You have exceeded the maximum number of accounts that you can share a manual DB snapshot with. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.modify_db_cluster_snapshot_attribute_message.ModifyDBClusterSnapshotAttributeMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.modify_db_cluster_snapshot_attribute_result.ModifyDBClusterSnapshotAttributeResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.modify_db_cluster_snapshot_attribute

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.modify_db_cluster_snapshot_attribute.modify_db_cluster_snapshot_attribute(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.modify_db_cluster_snapshot_attribute_message.ModifyDBClusterSnapshotAttributeMessage = {}
        if db_cluster_snapshot_identifier is not None:
            input_["db_cluster_snapshot_identifier"] = db_cluster_snapshot_identifier
        if attribute_name is not None:
            input_["attribute_name"] = attribute_name
        if values_to_add is not None:
            input_["values_to_add"] = values_to_add
        if values_to_remove is not None:
            input_["values_to_remove"] = values_to_remove

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_db_instance(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_instance_identifier: Optional["capo_docdb.types.string.String"] = None,
        db_instance_class: Optional["capo_docdb.types.string.String"] = None,
        apply_immediately: Optional["capo_docdb.types.boolean.Boolean"] = None,
        preferred_maintenance_window: Optional["capo_docdb.types.string.String"] = None,
        auto_minor_version_upgrade: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        new_db_instance_identifier: Optional["capo_docdb.types.string.String"] = None,
        ca_certificate_identifier: Optional["capo_docdb.types.string.String"] = None,
        copy_tags_to_snapshot: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        promotion_tier: Optional[
            "capo_docdb.types.integer_optional.IntegerOptional"
        ] = None,
        enable_performance_insights: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        performance_insights_kms_key_id: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        certificate_rotation_restart: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_docdb.types.modify_db_instance_result.ModifyDBInstanceResult":
        """<p>Modifies settings for an instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.</p>

        Args:
            db_instance_identifier: <p>The instance identifier. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing <code>DBInstance</code>.</p> </li> </ul>
            db_instance_class: <p>The new compute and memory capacity of the instance; for example, <code>db.r5.large</code>. Not all instance classes are available in all Amazon Web Services Regions. </p> <p>If you modify the instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless <code>ApplyImmediately</code> is specified as <code>true</code> for this request. </p> <p>Default: Uses existing setting.</p>
            apply_immediately: <p>Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the instance. </p> <p> If this parameter is set to <code>false</code>, changes to the instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next reboot.</p> <p>Default: <code>false</code> </p>
            preferred_maintenance_window: <p>The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesn't result in an outage except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, changing this parameter causes a reboot of the instance. If you are moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure that pending changes are applied.</p> <p>Default: Uses existing setting.</p> <p>Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p>Constraints: Must be at least 30 minutes.</p>
            auto_minor_version_upgrade: <p>This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.</p>
            new_db_instance_identifier: <p> The new instance identifier for the instance when renaming an instance. When you change the instance identifier, an instance reboot occurs immediately if you set <code>Apply Immediately</code> to <code>true</code>. It occurs during the next maintenance window if you set <code>Apply Immediately</code> to <code>false</code>. This value is stored as a lowercase string. </p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>mydbinstance</code> </p>
            ca_certificate_identifier: <p>Indicates the certificate that needs to be associated with the instance.</p>
            copy_tags_to_snapshot: <p>A value that indicates whether to copy all tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.</p>
            promotion_tier: <p>A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.</p> <p>Default: 1</p> <p>Valid values: 0-15</p>
            enable_performance_insights: <p>A value that indicates whether to enable Performance Insights for the DB Instance. For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/performance-insights.html">Using Amazon Performance Insights</a>.</p>
            performance_insights_kms_key_id: <p>The KMS key identifier for encryption of Performance Insights data.</p> <p>The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you do not specify a value for PerformanceInsightsKMSKeyId, then Amazon DocumentDB uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services region.</p>
            certificate_rotation_restart: <p>Specifies whether the DB instance is restarted when you rotate your SSL/TLS certificate.</p> <p>By default, the DB instance is restarted when you rotate your SSL/TLS certificate. The certificate is not updated until the DB instance is restarted.</p> <important> <p>Set this parameter only if you are <i>not</i> using SSL/TLS to connect to the DB instance.</p> </important> <p>If you are using SSL/TLS to connect to the DB instance, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/ca_cert_rotation.html">Updating Your Amazon DocumentDB TLS Certificates</a> and <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/security.encryption.ssl.html"> Encrypting Data in Transit</a> in the <i>Amazon DocumentDB Developer Guide</i>.</p>

        Raises:
            capo_docdb.errors.authorization_not_found_fault.AuthorizationNotFoundFault: <p>The specified CIDR IP or Amazon EC2 security group isn't authorized for the specified security group.</p> <p>Amazon DocumentDB also might not be authorized to perform necessary actions on your behalf using IAM.</p>
            capo_docdb.errors.certificate_not_found_fault.CertificateNotFoundFault: <p> <code>CertificateIdentifier</code> doesn't refer to an existing certificate. </p>
            capo_docdb.errors.db_instance_already_exists_fault.DBInstanceAlreadyExistsFault: <p>You already have a instance with the given identifier.</p>
            capo_docdb.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <code>DBInstanceIdentifier</code> doesn't refer to an existing instance. </p>
            capo_docdb.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <code>DBParameterGroupName</code> doesn't refer to an existing parameter group. </p>
            capo_docdb.errors.db_security_group_not_found_fault.DBSecurityGroupNotFoundFault: <p> <code>DBSecurityGroupName</code> doesn't refer to an existing security group. </p>
            capo_docdb.errors.db_upgrade_dependency_failure_fault.DBUpgradeDependencyFailureFault: <p>The upgrade failed because a resource that the depends on can't be modified.</p>
            capo_docdb.errors.insufficient_db_instance_capacity_fault.InsufficientDBInstanceCapacityFault: <p>The specified instance class isn't available in the specified Availability Zone.</p>
            capo_docdb.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p> The specified instance isn't in the <i>available</i> state. </p>
            capo_docdb.errors.invalid_db_security_group_state_fault.InvalidDBSecurityGroupStateFault: <p>The state of the security group doesn't allow deletion.</p>
            capo_docdb.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The subnet group doesn't cover all Availability Zones after it is created because of changes that were made.</p>
            capo_docdb.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>The request would cause you to exceed the allowed amount of storage available across all instances.</p>
            capo_docdb.errors.storage_type_not_supported_fault.StorageTypeNotSupportedFault: <p>Storage of the specified <code>StorageType</code> can't be associated with the DB instance. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.modify_db_instance_message.ModifyDBInstanceMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.modify_db_instance_result.ModifyDBInstanceResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.modify_db_instance

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.modify_db_instance.modify_db_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.modify_db_instance_message.ModifyDBInstanceMessage = {}
        if db_instance_identifier is not None:
            input_["db_instance_identifier"] = db_instance_identifier
        if db_instance_class is not None:
            input_["db_instance_class"] = db_instance_class
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if new_db_instance_identifier is not None:
            input_["new_db_instance_identifier"] = new_db_instance_identifier
        if ca_certificate_identifier is not None:
            input_["ca_certificate_identifier"] = ca_certificate_identifier
        if copy_tags_to_snapshot is not None:
            input_["copy_tags_to_snapshot"] = copy_tags_to_snapshot
        if promotion_tier is not None:
            input_["promotion_tier"] = promotion_tier
        if enable_performance_insights is not None:
            input_["enable_performance_insights"] = enable_performance_insights
        if performance_insights_kms_key_id is not None:
            input_["performance_insights_kms_key_id"] = performance_insights_kms_key_id
        if certificate_rotation_restart is not None:
            input_["certificate_rotation_restart"] = certificate_rotation_restart

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_db_subnet_group(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_subnet_group_name: Optional["capo_docdb.types.string.String"] = None,
        db_subnet_group_description: Optional["capo_docdb.types.string.String"] = None,
        subnet_ids: Optional[
            "capo_docdb.types.subnet_identifier_list.SubnetIdentifierList"
        ] = None,
    ) -> "capo_docdb.types.modify_db_subnet_group_result.ModifyDBSubnetGroupResult":
        """<p>Modifies an existing subnet group. subnet groups must contain at least one subnet in at least two Availability Zones in the Amazon Web Services Region.</p>

        Args:
            db_subnet_group_name: <p>The name for the subnet group. This value is stored as a lowercase string. You can't modify the default subnet group. </p> <p>Constraints: Must match the name of an existing <code>DBSubnetGroup</code>. Must not be default.</p> <p>Example: <code>mySubnetgroup</code> </p>
            db_subnet_group_description: <p>The description for the subnet group.</p>
            subnet_ids: <p>The Amazon EC2 subnet IDs for the subnet group.</p>

        Raises:
            capo_docdb.errors.db_subnet_group_does_not_cover_enough_a_zs.DBSubnetGroupDoesNotCoverEnoughAZs: <p>Subnets in the subnet group should cover at least two Availability Zones unless there is only one Availability Zone.</p>
            capo_docdb.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <code>DBSubnetGroupName</code> doesn't refer to an existing subnet group. </p>
            capo_docdb.errors.db_subnet_quota_exceeded_fault.DBSubnetQuotaExceededFault: <p>The request would cause you to exceed the allowed number of subnets in a subnet group.</p>
            capo_docdb.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is not valid, or multiple subnets were requested that are not all in a common virtual private cloud (VPC).</p>
            capo_docdb.errors.subnet_already_in_use.SubnetAlreadyInUse: <p>The subnet is already in use in the Availability Zone.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.modify_db_subnet_group_message.ModifyDBSubnetGroupMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.modify_db_subnet_group_result.ModifyDBSubnetGroupResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.modify_db_subnet_group

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.modify_db_subnet_group.modify_db_subnet_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.modify_db_subnet_group_message.ModifyDBSubnetGroupMessage = {}
        if db_subnet_group_name is not None:
            input_["db_subnet_group_name"] = db_subnet_group_name
        if db_subnet_group_description is not None:
            input_["db_subnet_group_description"] = db_subnet_group_description
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_event_subscription(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        subscription_name: Optional["capo_docdb.types.string.String"] = None,
        sns_topic_arn: Optional["capo_docdb.types.string.String"] = None,
        source_type: Optional["capo_docdb.types.string.String"] = None,
        event_categories: Optional[
            "capo_docdb.types.event_categories_list.EventCategoriesList"
        ] = None,
        enabled: Optional["capo_docdb.types.boolean_optional.BooleanOptional"] = None,
    ) -> "capo_docdb.types.modify_event_subscription_result.ModifyEventSubscriptionResult":
        """<p>Modifies an existing Amazon DocumentDB event notification subscription.</p>

        Args:
            subscription_name: <p>The name of the Amazon DocumentDB event notification subscription.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.</p>
            source_type: <p>The type of source that is generating the events. For example, if you want to be notified of events generated by an instance, set this parameter to <code>db-instance</code>. If this value is not specified, all events are returned.</p> <p>Valid values: <code>db-instance</code>, <code>db-parameter-group</code>, <code>db-security-group</code> </p>
            event_categories: <p> A list of event categories for a <code>SourceType</code> that you want to subscribe to.</p>
            enabled: <p> A Boolean value; set to <code>true</code> to activate the subscription. </p>

        Raises:
            capo_docdb.errors.event_subscription_quota_exceeded_fault.EventSubscriptionQuotaExceededFault: <p>You have reached the maximum number of event subscriptions. </p>
            capo_docdb.errors.sns_invalid_topic_fault.SNSInvalidTopicFault: <p>Amazon SNS has responded that there is a problem with the specified topic. </p>
            capo_docdb.errors.sns_no_authorization_fault.SNSNoAuthorizationFault: <p>You do not have permission to publish to the SNS topic Amazon Resource Name (ARN). </p>
            capo_docdb.errors.sns_topic_arn_not_found_fault.SNSTopicArnNotFoundFault: <p>The SNS topic Amazon Resource Name (ARN) does not exist. </p>
            capo_docdb.errors.subscription_category_not_found_fault.SubscriptionCategoryNotFoundFault: <p>The provided category does not exist. </p>
            capo_docdb.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>The subscription name does not exist. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.modify_event_subscription_message.ModifyEventSubscriptionMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.modify_event_subscription_result.ModifyEventSubscriptionResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.modify_event_subscription

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.modify_event_subscription.modify_event_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.modify_event_subscription_message.ModifyEventSubscriptionMessage = {}
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_global_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        new_global_cluster_identifier: Optional[
            "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        deletion_protection: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_docdb.types.modify_global_cluster_result.ModifyGlobalClusterResult":
        """<p>Modify a setting for an Amazon DocumentDB global cluster. You can change one or more configuration parameters (for example: deletion protection), or the global cluster identifier by specifying these parameters and the new values in the request.</p> <note> <p>This action only applies to Amazon DocumentDB clusters.</p> </note>

        Args:
            global_cluster_identifier: <p>The identifier for the global cluster being modified. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing global cluster.</p> </li> </ul>
            new_global_cluster_identifier: <p>The new identifier for a global cluster when you modify a global cluster. This value is stored as a lowercase string.</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens</p> <p>The first character must be a letter</p> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-cluster2</code> </p>
            deletion_protection: <p>Indicates if the global cluster has deletion protection enabled. The global cluster can't be deleted when deletion protection is enabled. </p>

        Raises:
            capo_docdb.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global cluster.</p>
            capo_docdb.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The requested operation can't be performed while the cluster is in this state.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.modify_global_cluster_message.ModifyGlobalClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.modify_global_cluster_result.ModifyGlobalClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.modify_global_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.modify_global_cluster.modify_global_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.modify_global_cluster_message.ModifyGlobalClusterMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if new_global_cluster_identifier is not None:
            input_["new_global_cluster_identifier"] = new_global_cluster_identifier
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reboot_db_instance(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_instance_identifier: Optional["capo_docdb.types.string.String"] = None,
        force_failover: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_docdb.types.reboot_db_instance_result.RebootDBInstanceResult":
        """<p>You might need to reboot your instance, usually for maintenance reasons. For example, if you make certain changes, or if you change the cluster parameter group that is associated with the instance, you must reboot the instance for the changes to take effect. </p> <p>Rebooting an instance restarts the database engine service. Rebooting an instance results in a momentary outage, during which the instance status is set to <i>rebooting</i>. </p>

        Args:
            db_instance_identifier: <p>The instance identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing <code>DBInstance</code>.</p> </li> </ul>
            force_failover: <p> When <code>true</code>, the reboot is conducted through a Multi-AZ failover. </p> <p>Constraint: You can't specify <code>true</code> if the instance is not configured for Multi-AZ.</p>

        Raises:
            capo_docdb.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <code>DBInstanceIdentifier</code> doesn't refer to an existing instance. </p>
            capo_docdb.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p> The specified instance isn't in the <i>available</i> state. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.reboot_db_instance_message.RebootDBInstanceMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.reboot_db_instance_result.RebootDBInstanceResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.reboot_db_instance

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.reboot_db_instance.reboot_db_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.reboot_db_instance_message.RebootDBInstanceMessage = {}
        if db_instance_identifier is not None:
            input_["db_instance_identifier"] = db_instance_identifier
        if force_failover is not None:
            input_["force_failover"] = force_failover

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_from_global_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.remove_from_global_cluster_result.RemoveFromGlobalClusterResult":
        """<p>Detaches an Amazon DocumentDB secondary cluster from a global cluster. The cluster becomes a standalone cluster with read-write capability instead of being read-only and receiving data from a primary in a different region. </p> <note> <p>This action only applies to Amazon DocumentDB clusters.</p> </note>

        Args:
            global_cluster_identifier: <p>The cluster identifier to detach from the Amazon DocumentDB global cluster. </p>
            db_cluster_identifier: <p>The Amazon Resource Name (ARN) identifying the cluster that was detached from the Amazon DocumentDB global cluster. </p>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global cluster.</p>
            capo_docdb.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The requested operation can't be performed while the cluster is in this state.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.remove_from_global_cluster_message.RemoveFromGlobalClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.remove_from_global_cluster_result.RemoveFromGlobalClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.remove_from_global_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.remove_from_global_cluster.remove_from_global_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.remove_from_global_cluster_message.RemoveFromGlobalClusterMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_source_identifier_from_subscription(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        subscription_name: Optional["capo_docdb.types.string.String"] = None,
        source_identifier: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.remove_source_identifier_from_subscription_result.RemoveSourceIdentifierFromSubscriptionResult":
        """<p>Removes a source identifier from an existing Amazon DocumentDB event notification subscription.</p>

        Args:
            subscription_name: <p>The name of the Amazon DocumentDB event notification subscription that you want to remove a source identifier from.</p>
            source_identifier: <p> The source identifier to be removed from the subscription, such as the instance identifier for an instance, or the name of a security group. </p>

        Raises:
            capo_docdb.errors.source_not_found_fault.SourceNotFoundFault: <p>The requested source could not be found. </p>
            capo_docdb.errors.subscription_not_found_fault.SubscriptionNotFoundFault: <p>The subscription name does not exist. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.remove_source_identifier_from_subscription_message.RemoveSourceIdentifierFromSubscriptionMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.remove_source_identifier_from_subscription_result.RemoveSourceIdentifierFromSubscriptionResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.remove_source_identifier_from_subscription

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.remove_source_identifier_from_subscription.remove_source_identifier_from_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.remove_source_identifier_from_subscription_message.RemoveSourceIdentifierFromSubscriptionMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if source_identifier is not None:
            input_["source_identifier"] = source_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_tags_from_resource(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        resource_name: Optional["capo_docdb.types.string.String"] = None,
        tag_keys: Optional["capo_docdb.types.key_list.KeyList"] = None,
    ) -> None:
        """<p>Removes metadata tags from an Amazon DocumentDB resource.</p>

        Args:
            resource_name: <p>The Amazon DocumentDB resource that the tags are removed from. This value is an Amazon Resource Name (ARN).</p>
            tag_keys: <p>The tag key (name) of the tag to be removed.</p>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.db_instance_not_found_fault.DBInstanceNotFoundFault: <p> <code>DBInstanceIdentifier</code> doesn't refer to an existing instance. </p>
            capo_docdb.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault: <p> <code>DBSnapshotIdentifier</code> doesn't refer to an existing snapshot. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.remove_tags_from_resource_message.RemoveTagsFromResourceMessage]",
        ) -> OperationResponse[None]:
            import capo_docdb._operations.amazon_rd_sv19.remove_tags_from_resource

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.remove_tags_from_resource.remove_tags_from_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.remove_tags_from_resource_message.RemoveTagsFromResourceMessage = {}
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reset_db_cluster_parameter_group(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        reset_all_parameters: Optional["capo_docdb.types.boolean.Boolean"] = None,
        parameters: Optional["capo_docdb.types.parameters_list.ParametersList"] = None,
    ) -> "capo_docdb.types.db_cluster_parameter_group_name_message.DBClusterParameterGroupNameMessage":
        """<p> Modifies the parameters of a cluster parameter group to the default value. To reset specific parameters, submit a list of the following: <code>ParameterName</code> and <code>ApplyMethod</code>. To reset the entire cluster parameter group, specify the <code>DBClusterParameterGroupName</code> and <code>ResetAllParameters</code> parameters. </p> <p> When you reset the entire group, dynamic parameters are updated immediately and static parameters are set to <code>pending-reboot</code> to take effect on the next DB instance reboot.</p>

        Args:
            db_cluster_parameter_group_name: <p>The name of the cluster parameter group to reset.</p>
            reset_all_parameters: <p>A value that is set to <code>true</code> to reset all parameters in the cluster parameter group to their default values, and <code>false</code> otherwise. You can't use this parameter if there is a list of parameter names specified for the <code>Parameters</code> parameter.</p>
            parameters: <p>A list of parameter names in the cluster parameter group to reset to the default values. You can't use this parameter if the <code>ResetAllParameters</code> parameter is set to <code>true</code>.</p>

        Raises:
            capo_docdb.errors.db_parameter_group_not_found_fault.DBParameterGroupNotFoundFault: <p> <code>DBParameterGroupName</code> doesn't refer to an existing parameter group. </p>
            capo_docdb.errors.invalid_db_parameter_group_state_fault.InvalidDBParameterGroupStateFault: <p>The parameter group is in use, or it is in a state that is not valid. If you are trying to delete the parameter group, you can't delete it when the parameter group is in this state.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.reset_db_cluster_parameter_group_message.ResetDBClusterParameterGroupMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.db_cluster_parameter_group_name_message.DBClusterParameterGroupNameMessage"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.reset_db_cluster_parameter_group

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.reset_db_cluster_parameter_group.reset_db_cluster_parameter_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.reset_db_cluster_parameter_group_message.ResetDBClusterParameterGroupMessage = {}
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if reset_all_parameters is not None:
            input_["reset_all_parameters"] = reset_all_parameters
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_db_cluster_from_snapshot(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        availability_zones: Optional[
            "capo_docdb.types.availability_zones.AvailabilityZones"
        ] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        snapshot_identifier: Optional["capo_docdb.types.string.String"] = None,
        engine: Optional["capo_docdb.types.string.String"] = None,
        engine_version: Optional["capo_docdb.types.string.String"] = None,
        port: Optional["capo_docdb.types.integer_optional.IntegerOptional"] = None,
        db_subnet_group_name: Optional["capo_docdb.types.string.String"] = None,
        vpc_security_group_ids: Optional[
            "capo_docdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        tags: Optional["capo_docdb.types.tag_list.TagList"] = None,
        kms_key_id: Optional["capo_docdb.types.string.String"] = None,
        enable_cloudwatch_logs_exports: Optional[
            "capo_docdb.types.log_type_list.LogTypeList"
        ] = None,
        deletion_protection: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        db_cluster_parameter_group_name: Optional[
            "capo_docdb.types.string.String"
        ] = None,
        serverless_v2_scaling_configuration: Optional[
            "capo_docdb.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
        ] = None,
        storage_type: Optional["capo_docdb.types.string.String"] = None,
        network_type: Optional["capo_docdb.types.string.String"] = None,
        copy_tags_to_snapshot: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_docdb.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult":
        """<p>Creates a new cluster from a snapshot or cluster snapshot.</p> <p>If a snapshot is specified, the target cluster is created from the source DB snapshot with a default configuration and default security group.</p> <p>If a cluster snapshot is specified, the target cluster is created from the source cluster restore point with the same configuration as the original source DB cluster, except that the new cluster is created with the default security group.</p>

        Args:
            availability_zones: <p>Provides the list of Amazon EC2 Availability Zones that instances in the restored DB cluster can be created in.</p>
            db_cluster_identifier: <p>The name of the cluster to create from the snapshot or cluster snapshot. This parameter isn't case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-snapshot-id</code> </p>
            snapshot_identifier: <p>The identifier for the snapshot or cluster snapshot to restore from.</p> <p>You can use either the name or the Amazon Resource Name (ARN) to specify a cluster snapshot. However, you can use only the ARN to specify a snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing snapshot.</p> </li> </ul>
            engine: <p>The database engine to use for the new cluster.</p> <p>Default: The same as source.</p> <p>Constraint: Must be compatible with the engine of the source.</p>
            engine_version: <p>The version of the database engine to use for the new cluster.</p>
            port: <p>The port number on which the new cluster accepts connections.</p> <p>Constraints: Must be a value from <code>1150</code> to <code>65535</code>.</p> <p>Default: The same port as the original cluster.</p>
            db_subnet_group_name: <p>The name of the subnet group to use for the new cluster.</p> <p>Constraints: If provided, must match the name of an existing <code>DBSubnetGroup</code>.</p> <p>Example: <code>mySubnetgroup</code> </p>
            vpc_security_group_ids: <p>A list of virtual private cloud (VPC) security groups that the new cluster will belong to.</p>
            tags: <p>The tags to be assigned to the restored cluster.</p>
            kms_key_id: <p>The KMS key identifier to use when restoring an encrypted cluster from a DB snapshot or cluster snapshot.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a cluster with the same Amazon Web Services account that owns the KMS encryption key used to encrypt the new cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.</p> <p>If you do not specify a value for the <code>KmsKeyId</code> parameter, then the following occurs:</p> <ul> <li> <p>If the snapshot or cluster snapshot in <code>SnapshotIdentifier</code> is encrypted, then the restored cluster is encrypted using the KMS key that was used to encrypt the snapshot or the cluster snapshot.</p> </li> <li> <p>If the snapshot or the cluster snapshot in <code>SnapshotIdentifier</code> is not encrypted, then the restored DB cluster is not encrypted.</p> </li> </ul>
            enable_cloudwatch_logs_exports: <p>A list of log types that must be enabled for exporting to Amazon CloudWatch Logs.</p>
            deletion_protection: <p>Specifies whether this cluster can be deleted. If <code>DeletionProtection</code> is enabled, the cluster cannot be deleted unless it is modified and <code>DeletionProtection</code> is disabled. <code>DeletionProtection</code> protects clusters from being accidentally deleted.</p>
            db_cluster_parameter_group_name: <p>The name of the DB cluster parameter group to associate with this DB cluster.</p> <p> <i>Type:</i> String. <i>Required:</i> No.</p> <p>If this argument is omitted, the default DB cluster parameter group is used. If supplied, must match the name of an existing default DB cluster parameter group. The string must consist of from 1 to 255 letters, numbers or hyphens. Its first character must be a letter, and it cannot end with a hyphen or contain two consecutive hyphens.</p>
            serverless_v2_scaling_configuration: <p>Contains the scaling configuration of an Amazon DocumentDB Serverless cluster.</p>
            storage_type: <p>The storage type to associate with the DB cluster.</p> <p>For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the <i>Amazon DocumentDB Developer Guide</i>.</p> <p>Valid values for storage type - <code>standard | iopt1</code> </p> <p>Default value is <code>standard </code> </p>
            network_type: <p>The network type of the cluster.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/vpc-clusters.html">DocumentDB clusters in a VPC</a> in the Amazon DocumentDB Developer Guide.</p> <p>Valid Values: <code>IPV4</code> | <code>DUAL</code> </p>
            copy_tags_to_snapshot: <p>Specifies whether to copy all tags from the restored DB cluster to snapshots of the restored DB cluster. The default is not to copy them.</p>

        Raises:
            capo_docdb.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault: <p>You already have a cluster with the given identifier.</p>
            capo_docdb.errors.db_cluster_quota_exceeded_fault.DBClusterQuotaExceededFault: <p>The cluster can't be created because you have reached the maximum allowed quota of clusters.</p>
            capo_docdb.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <code>DBClusterSnapshotIdentifier</code> doesn't refer to an existing cluster snapshot. </p>
            capo_docdb.errors.db_snapshot_not_found_fault.DBSnapshotNotFoundFault: <p> <code>DBSnapshotIdentifier</code> doesn't refer to an existing snapshot. </p>
            capo_docdb.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <code>DBSubnetGroupName</code> doesn't refer to an existing subnet group. </p>
            capo_docdb.errors.insufficient_db_cluster_capacity_fault.InsufficientDBClusterCapacityFault: <p>The cluster doesn't have enough capacity for the current operation.</p>
            capo_docdb.errors.insufficient_storage_cluster_capacity_fault.InsufficientStorageClusterCapacityFault: <p>There is not enough storage available for the current action. You might be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available. </p>
            capo_docdb.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The provided value isn't a valid cluster snapshot state.</p>
            capo_docdb.errors.invalid_db_snapshot_state_fault.InvalidDBSnapshotStateFault: <p>The state of the snapshot doesn't allow deletion.</p>
            capo_docdb.errors.invalid_restore_fault.InvalidRestoreFault: <p>You cannot restore from a virtual private cloud (VPC) backup to a non-VPC DB instance.</p>
            capo_docdb.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is not valid, or multiple subnets were requested that are not all in a common virtual private cloud (VPC).</p>
            capo_docdb.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The subnet group doesn't cover all Availability Zones after it is created because of changes that were made.</p>
            capo_docdb.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>An error occurred when accessing an KMS key.</p>
            capo_docdb.errors.network_type_not_supported.NetworkTypeNotSupported: <p>The network type is not supported by either <code>DBSubnetGroup</code> or the DB engine version.</p>
            capo_docdb.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>The request would cause you to exceed the allowed amount of storage available across all instances.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.restore_db_cluster_from_snapshot_message.RestoreDBClusterFromSnapshotMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.restore_db_cluster_from_snapshot_result.RestoreDBClusterFromSnapshotResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.restore_db_cluster_from_snapshot

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.restore_db_cluster_from_snapshot.restore_db_cluster_from_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.restore_db_cluster_from_snapshot_message.RestoreDBClusterFromSnapshotMessage = {}
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
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if enable_cloudwatch_logs_exports is not None:
            input_["enable_cloudwatch_logs_exports"] = enable_cloudwatch_logs_exports
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if db_cluster_parameter_group_name is not None:
            input_["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if serverless_v2_scaling_configuration is not None:
            input_["serverless_v2_scaling_configuration"] = (
                serverless_v2_scaling_configuration
            )
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if network_type is not None:
            input_["network_type"] = network_type
        if copy_tags_to_snapshot is not None:
            input_["copy_tags_to_snapshot"] = copy_tags_to_snapshot

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_db_cluster_to_point_in_time(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        restore_type: Optional["capo_docdb.types.string.String"] = None,
        source_db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
        restore_to_time: Optional["capo_docdb.types.t_stamp.TStamp"] = None,
        use_latest_restorable_time: Optional["capo_docdb.types.boolean.Boolean"] = None,
        port: Optional["capo_docdb.types.integer_optional.IntegerOptional"] = None,
        db_subnet_group_name: Optional["capo_docdb.types.string.String"] = None,
        vpc_security_group_ids: Optional[
            "capo_docdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        tags: Optional["capo_docdb.types.tag_list.TagList"] = None,
        kms_key_id: Optional["capo_docdb.types.string.String"] = None,
        enable_cloudwatch_logs_exports: Optional[
            "capo_docdb.types.log_type_list.LogTypeList"
        ] = None,
        deletion_protection: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
        serverless_v2_scaling_configuration: Optional[
            "capo_docdb.types.serverless_v2_scaling_configuration.ServerlessV2ScalingConfiguration"
        ] = None,
        storage_type: Optional["capo_docdb.types.string.String"] = None,
        network_type: Optional["capo_docdb.types.string.String"] = None,
        copy_tags_to_snapshot: Optional[
            "capo_docdb.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_docdb.types.restore_db_cluster_to_point_in_time_result.RestoreDBClusterToPointInTimeResult":
        """<p>Restores a cluster to an arbitrary point in time. Users can restore to any point in time before <code>LatestRestorableTime</code> for up to <code>BackupRetentionPeriod</code> days. The target cluster is created from the source cluster with the same configuration as the original cluster, except that the new cluster is created with the default security group. </p>

        Args:
            db_cluster_identifier: <p>The name of the new cluster to be created.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            restore_type: <p>The type of restore to be performed. You can specify one of the following values:</p> <ul> <li> <p> <code>full-copy</code> - The new DB cluster is restored as a full copy of the source DB cluster.</p> </li> <li> <p> <code>copy-on-write</code> - The new DB cluster is restored as a clone of the source DB cluster.</p> </li> </ul> <p>Constraints: You can't specify <code>copy-on-write</code> if the engine version of the source DB cluster is earlier than 1.11.</p> <p>If you don't specify a <code>RestoreType</code> value, then the new DB cluster is restored as a full copy of the source DB cluster.</p>
            source_db_cluster_identifier: <p>The identifier of the source cluster from which to restore.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing <code>DBCluster</code>.</p> </li> </ul>
            restore_to_time: <p>The date and time to restore the cluster to.</p> <p>Valid values: A time in Universal Coordinated Time (UTC) format.</p> <p>Constraints:</p> <ul> <li> <p>Must be before the latest restorable time for the instance.</p> </li> <li> <p>Must be specified if the <code>UseLatestRestorableTime</code> parameter is not provided.</p> </li> <li> <p>Cannot be specified if the <code>UseLatestRestorableTime</code> parameter is <code>true</code>.</p> </li> <li> <p>Cannot be specified if the <code>RestoreType</code> parameter is <code>copy-on-write</code>.</p> </li> </ul> <p>Example: <code>2015-03-07T23:45:00Z</code> </p>
            use_latest_restorable_time: <p>A value that is set to <code>true</code> to restore the cluster to the latest restorable backup time, and <code>false</code> otherwise. </p> <p>Default: <code>false</code> </p> <p>Constraints: Cannot be specified if the <code>RestoreToTime</code> parameter is provided.</p>
            port: <p>The port number on which the new cluster accepts connections.</p> <p>Constraints: Must be a value from <code>1150</code> to <code>65535</code>. </p> <p>Default: The default port for the engine.</p>
            db_subnet_group_name: <p>The subnet group name to use for the new cluster.</p> <p>Constraints: If provided, must match the name of an existing <code>DBSubnetGroup</code>.</p> <p>Example: <code>mySubnetgroup</code> </p>
            vpc_security_group_ids: <p>A list of VPC security groups that the new cluster belongs to.</p>
            tags: <p>The tags to be assigned to the restored cluster.</p>
            kms_key_id: <p>The KMS key identifier to use when restoring an encrypted cluster from an encrypted cluster.</p> <p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a cluster with the same Amazon Web Services account that owns the KMS encryption key used to encrypt the new cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.</p> <p>You can restore to a new cluster and encrypt the new cluster with an KMS key that is different from the KMS key used to encrypt the source cluster. The new DB cluster is encrypted with the KMS key identified by the <code>KmsKeyId</code> parameter.</p> <p>If you do not specify a value for the <code>KmsKeyId</code> parameter, then the following occurs:</p> <ul> <li> <p>If the cluster is encrypted, then the restored cluster is encrypted using the KMS key that was used to encrypt the source cluster.</p> </li> <li> <p>If the cluster is not encrypted, then the restored cluster is not encrypted.</p> </li> </ul> <p>If <code>DBClusterIdentifier</code> refers to a cluster that is not encrypted, then the restore request is rejected.</p>
            enable_cloudwatch_logs_exports: <p>A list of log types that must be enabled for exporting to Amazon CloudWatch Logs.</p>
            deletion_protection: <p>Specifies whether this cluster can be deleted. If <code>DeletionProtection</code> is enabled, the cluster cannot be deleted unless it is modified and <code>DeletionProtection</code> is disabled. <code>DeletionProtection</code> protects clusters from being accidentally deleted.</p>
            serverless_v2_scaling_configuration: <p>Contains the scaling configuration of an Amazon DocumentDB Serverless cluster.</p>
            storage_type: <p>The storage type to associate with the DB cluster.</p> <p>For information on storage types for Amazon DocumentDB clusters, see Cluster storage configurations in the <i>Amazon DocumentDB Developer Guide</i>.</p> <p>Valid values for storage type - <code>standard | iopt1</code> </p> <p>Default value is <code>standard </code> </p>
            network_type: <p>The network type of the cluster.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the cluster. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/vpc-clusters.html">DocumentDB clusters in a VPC</a> in the Amazon DocumentDB Developer Guide.</p> <p>Valid Values: <code>IPV4</code> | <code>DUAL</code> </p>
            copy_tags_to_snapshot: <p>Specifies whether to copy all tags from the restored DB cluster to snapshots of the restored DB cluster. The default is not to copy them.</p>

        Raises:
            capo_docdb.errors.db_cluster_already_exists_fault.DBClusterAlreadyExistsFault: <p>You already have a cluster with the given identifier.</p>
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.db_cluster_quota_exceeded_fault.DBClusterQuotaExceededFault: <p>The cluster can't be created because you have reached the maximum allowed quota of clusters.</p>
            capo_docdb.errors.db_cluster_snapshot_not_found_fault.DBClusterSnapshotNotFoundFault: <p> <code>DBClusterSnapshotIdentifier</code> doesn't refer to an existing cluster snapshot. </p>
            capo_docdb.errors.db_subnet_group_not_found_fault.DBSubnetGroupNotFoundFault: <p> <code>DBSubnetGroupName</code> doesn't refer to an existing subnet group. </p>
            capo_docdb.errors.insufficient_db_cluster_capacity_fault.InsufficientDBClusterCapacityFault: <p>The cluster doesn't have enough capacity for the current operation.</p>
            capo_docdb.errors.insufficient_storage_cluster_capacity_fault.InsufficientStorageClusterCapacityFault: <p>There is not enough storage available for the current action. You might be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available. </p>
            capo_docdb.errors.invalid_db_cluster_snapshot_state_fault.InvalidDBClusterSnapshotStateFault: <p>The provided value isn't a valid cluster snapshot state.</p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.invalid_db_snapshot_state_fault.InvalidDBSnapshotStateFault: <p>The state of the snapshot doesn't allow deletion.</p>
            capo_docdb.errors.invalid_restore_fault.InvalidRestoreFault: <p>You cannot restore from a virtual private cloud (VPC) backup to a non-VPC DB instance.</p>
            capo_docdb.errors.invalid_subnet.InvalidSubnet: <p>The requested subnet is not valid, or multiple subnets were requested that are not all in a common virtual private cloud (VPC).</p>
            capo_docdb.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The subnet group doesn't cover all Availability Zones after it is created because of changes that were made.</p>
            capo_docdb.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>An error occurred when accessing an KMS key.</p>
            capo_docdb.errors.network_type_not_supported.NetworkTypeNotSupported: <p>The network type is not supported by either <code>DBSubnetGroup</code> or the DB engine version.</p>
            capo_docdb.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>The request would cause you to exceed the allowed amount of storage available across all instances.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.restore_db_cluster_to_point_in_time_message.RestoreDBClusterToPointInTimeMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.restore_db_cluster_to_point_in_time_result.RestoreDBClusterToPointInTimeResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.restore_db_cluster_to_point_in_time

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.restore_db_cluster_to_point_in_time.restore_db_cluster_to_point_in_time(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.restore_db_cluster_to_point_in_time_message.RestoreDBClusterToPointInTimeMessage = {}
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
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if enable_cloudwatch_logs_exports is not None:
            input_["enable_cloudwatch_logs_exports"] = enable_cloudwatch_logs_exports
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
        if copy_tags_to_snapshot is not None:
            input_["copy_tags_to_snapshot"] = copy_tags_to_snapshot

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_db_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.start_db_cluster_result.StartDBClusterResult":
        """<p>Restarts the stopped cluster that is specified by <code>DBClusterIdentifier</code>. For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/db-cluster-stop-start.html">Stopping and Starting an Amazon DocumentDB Cluster</a>.</p>

        Args:
            db_cluster_identifier: <p>The identifier of the cluster to restart. Example: <code>docdb-2019-05-28-15-24-52</code> </p>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p> The specified instance isn't in the <i>available</i> state. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.start_db_cluster_message.StartDBClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.start_db_cluster_result.StartDBClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.start_db_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.start_db_cluster.start_db_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.start_db_cluster_message.StartDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_db_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        db_cluster_identifier: Optional["capo_docdb.types.string.String"] = None,
    ) -> "capo_docdb.types.stop_db_cluster_result.StopDBClusterResult":
        """<p>Stops the running cluster that is specified by <code>DBClusterIdentifier</code>. The cluster must be in the <i>available</i> state. For more information, see <a href="https://docs.aws.amazon.com/documentdb/latest/devguide/db-cluster-stop-start.html">Stopping and Starting an Amazon DocumentDB Cluster</a>.</p>

        Args:
            db_cluster_identifier: <p>The identifier of the cluster to stop. Example: <code>docdb-2019-05-28-15-24-52</code> </p>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.invalid_db_instance_state_fault.InvalidDBInstanceStateFault: <p> The specified instance isn't in the <i>available</i> state. </p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.stop_db_cluster_message.StopDBClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.stop_db_cluster_result.StopDBClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.stop_db_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.stop_db_cluster.stop_db_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.stop_db_cluster_message.StopDBClusterMessage = {}
        if db_cluster_identifier is not None:
            input_["db_cluster_identifier"] = db_cluster_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def switchover_global_cluster(
        self,
        *,
        config_overrides: Optional[DocDBClientConfig] = None,
        global_cluster_identifier: Optional[
            "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
        ] = None,
        target_db_cluster_identifier: Optional[
            "capo_docdb.types.db_cluster_identifier.DBClusterIdentifier"
        ] = None,
    ) -> "capo_docdb.types.switchover_global_cluster_result.SwitchoverGlobalClusterResult":
        """<p>Switches over the specified secondary Amazon DocumentDB cluster to be the new primary Amazon DocumentDB cluster in the global database cluster.</p>

        Args:
            global_cluster_identifier: <p>The identifier of the Amazon DocumentDB global database cluster to switch over. The identifier is the unique key assigned by the user when the cluster is created. In other words, it's the name of the global cluster. This parameter isn’t case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing global cluster (Amazon DocumentDB global database).</p> </li> <li> <p>Minimum length of 1. Maximum length of 255.</p> </li> </ul> <p>Pattern: <code>[A-Za-z][0-9A-Za-z-:._]*</code> </p>
            target_db_cluster_identifier: <p>The identifier of the secondary Amazon DocumentDB cluster to promote to the new primary for the global database cluster. Use the Amazon Resource Name (ARN) for the identifier so that Amazon DocumentDB can locate the cluster in its Amazon Web Services region.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing secondary cluster.</p> </li> <li> <p>Minimum length of 1. Maximum length of 255.</p> </li> </ul> <p>Pattern: <code>[A-Za-z][0-9A-Za-z-:._]*</code> </p>

        Raises:
            capo_docdb.errors.db_cluster_not_found_fault.DBClusterNotFoundFault: <p> <code>DBClusterIdentifier</code> doesn't refer to an existing cluster. </p>
            capo_docdb.errors.global_cluster_not_found_fault.GlobalClusterNotFoundFault: <p>The <code>GlobalClusterIdentifier</code> doesn't refer to an existing global cluster.</p>
            capo_docdb.errors.invalid_db_cluster_state_fault.InvalidDBClusterStateFault: <p>The cluster isn't in a valid state.</p>
            capo_docdb.errors.invalid_global_cluster_state_fault.InvalidGlobalClusterStateFault: <p>The requested operation can't be performed while the cluster is in this state.</p>
            capo_docdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_docdb.types.switchover_global_cluster_message.SwitchoverGlobalClusterMessage]",
        ) -> OperationResponse[
            "capo_docdb.types.switchover_global_cluster_result.SwitchoverGlobalClusterResult"
        ]:
            import capo_docdb._operations.amazon_rd_sv19.switchover_global_cluster

            output, http_response = (
                capo_docdb._operations.amazon_rd_sv19.switchover_global_cluster.switchover_global_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_docdb.types.switchover_global_cluster_message.SwitchoverGlobalClusterMessage = {}
        if global_cluster_identifier is not None:
            input_["global_cluster_identifier"] = global_cluster_identifier
        if target_db_cluster_identifier is not None:
            input_["target_db_cluster_identifier"] = target_db_cluster_identifier

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
