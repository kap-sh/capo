"""Generated from Smithy shape ``com.amazonaws.dax#AmazonDAXV3``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_dax._auth._signers
import capo_dax._auth._sigv4
from capo_dax._auth._identity import Credentials
from capo_dax._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_dax._auth._zapros_handler import AuthMiddleware
from capo_dax._services._aws_config import aws_config
from capo_dax._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_dax.types.availability_zone_list
    import capo_dax.types.cluster_endpoint_encryption_type
    import capo_dax.types.cluster_name_list
    import capo_dax.types.create_cluster_request
    import capo_dax.types.create_cluster_response
    import capo_dax.types.create_parameter_group_request
    import capo_dax.types.create_parameter_group_response
    import capo_dax.types.create_subnet_group_request
    import capo_dax.types.create_subnet_group_response
    import capo_dax.types.decrease_replication_factor_request
    import capo_dax.types.decrease_replication_factor_response
    import capo_dax.types.delete_cluster_request
    import capo_dax.types.delete_cluster_response
    import capo_dax.types.delete_parameter_group_request
    import capo_dax.types.delete_parameter_group_response
    import capo_dax.types.delete_subnet_group_request
    import capo_dax.types.delete_subnet_group_response
    import capo_dax.types.describe_clusters_request
    import capo_dax.types.describe_clusters_response
    import capo_dax.types.describe_default_parameters_request
    import capo_dax.types.describe_default_parameters_response
    import capo_dax.types.describe_events_request
    import capo_dax.types.describe_events_response
    import capo_dax.types.describe_parameter_groups_request
    import capo_dax.types.describe_parameter_groups_response
    import capo_dax.types.describe_parameters_request
    import capo_dax.types.describe_parameters_response
    import capo_dax.types.describe_subnet_groups_request
    import capo_dax.types.describe_subnet_groups_response
    import capo_dax.types.increase_replication_factor_request
    import capo_dax.types.increase_replication_factor_response
    import capo_dax.types.integer
    import capo_dax.types.integer_optional
    import capo_dax.types.key_list
    import capo_dax.types.list_tags_request
    import capo_dax.types.list_tags_response
    import capo_dax.types.network_type
    import capo_dax.types.node_identifier_list
    import capo_dax.types.parameter_group_name_list
    import capo_dax.types.parameter_name_value_list
    import capo_dax.types.reboot_node_request
    import capo_dax.types.reboot_node_response
    import capo_dax.types.security_group_identifier_list
    import capo_dax.types.source_type
    import capo_dax.types.sse_specification
    import capo_dax.types.string
    import capo_dax.types.subnet_group_name_list
    import capo_dax.types.subnet_identifier_list
    import capo_dax.types.t_stamp
    import capo_dax.types.tag_list
    import capo_dax.types.tag_resource_request
    import capo_dax.types.tag_resource_response
    import capo_dax.types.untag_resource_request
    import capo_dax.types.untag_resource_response
    import capo_dax.types.update_cluster_request
    import capo_dax.types.update_cluster_response
    import capo_dax.types.update_parameter_group_request
    import capo_dax.types.update_parameter_group_response
    import capo_dax.types.update_subnet_group_request
    import capo_dax.types.update_subnet_group_response


class DAXClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class DAXClient:
    """A client for the ``DAX`` service.

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
        self._config = DAXClientConfig(
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
        self, config_overrides: Optional[DAXClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DAXClientConfig = config_overrides or {}
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

    def create_cluster(
        self,
        cluster_name: "capo_dax.types.string.String",
        node_type: "capo_dax.types.string.String",
        replication_factor: "capo_dax.types.integer.Integer",
        iam_role_arn: "capo_dax.types.string.String",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        description: Optional["capo_dax.types.string.String"] = None,
        availability_zones: Optional[
            "capo_dax.types.availability_zone_list.AvailabilityZoneList"
        ] = None,
        subnet_group_name: Optional["capo_dax.types.string.String"] = None,
        security_group_ids: Optional[
            "capo_dax.types.security_group_identifier_list.SecurityGroupIdentifierList"
        ] = None,
        preferred_maintenance_window: Optional["capo_dax.types.string.String"] = None,
        notification_topic_arn: Optional["capo_dax.types.string.String"] = None,
        parameter_group_name: Optional["capo_dax.types.string.String"] = None,
        tags: Optional["capo_dax.types.tag_list.TagList"] = None,
        sse_specification: Optional[
            "capo_dax.types.sse_specification.SSESpecification"
        ] = None,
        cluster_endpoint_encryption_type: Optional[
            "capo_dax.types.cluster_endpoint_encryption_type.ClusterEndpointEncryptionType"
        ] = None,
        network_type: Optional["capo_dax.types.network_type.NetworkType"] = None,
    ) -> "capo_dax.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates a DAX cluster. All nodes in the cluster run the same DAX caching software.</p>

        Args:
            cluster_name: <p>The cluster identifier. This parameter is stored as a lowercase string.</p> <p> <b>Constraints:</b> </p> <ul> <li> <p>A name must contain from 1 to 20 alphanumeric characters or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>A name cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            node_type: <p>The compute and memory capacity of the nodes in the cluster.</p>
            description: <p>A description of the cluster.</p>
            replication_factor: <p>The number of nodes in the DAX cluster. A replication factor of 1 will create a single-node cluster, without any read replicas. For additional fault tolerance, you can create a multiple node cluster with one or more read replicas. To do this, set <code>ReplicationFactor</code> to a number between 3 (one primary and two read replicas) and 10 (one primary and nine read replicas). <code>If the AvailabilityZones</code> parameter is provided, its length must equal the <code>ReplicationFactor</code>.</p> <note> <p>Amazon Web Services recommends that you have at least two read replicas per cluster.</p> </note>
            availability_zones: <p>The Availability Zones (AZs) in which the cluster nodes will reside after the cluster has been created or updated. If provided, the length of this list must equal the <code>ReplicationFactor</code> parameter. If you omit this parameter, DAX will spread the nodes across Availability Zones for the highest availability.</p>
            subnet_group_name: <p>The name of the subnet group to be used for the replication group.</p> <important> <p>DAX clusters can only run in an Amazon VPC environment. All of the subnets that you specify in a subnet group must exist in the same VPC.</p> </important>
            security_group_ids: <p>A list of security group IDs to be assigned to each node in the DAX cluster. (Each of the security group ID is system-generated.)</p> <p>If this parameter is not specified, DAX assigns the default VPC security group to each node.</p>
            preferred_maintenance_window: <p>Specifies the weekly time range during which maintenance on the DAX cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:05:00-sun:09:00</code> </p> <note> <p>If you don't specify a preferred maintenance window when you create or modify a cache cluster, DAX assigns a 60-minute maintenance window on a randomly selected day of the week.</p> </note>
            notification_topic_arn: <p>The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications will be sent.</p> <note> <p>The Amazon SNS topic owner must be same as the DAX cluster owner.</p> </note>
            iam_role_arn: <p>A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role's permissions to access DynamoDB on your behalf.</p>
            parameter_group_name: <p>The parameter group to be associated with the DAX cluster.</p>
            tags: <p>A set of tags to associate with the DAX cluster. </p>
            sse_specification: <p>Represents the settings used to enable server-side encryption on the cluster.</p>
            cluster_endpoint_encryption_type: <p>The type of encryption the cluster's endpoint should support. Values are:</p> <ul> <li> <p> <code>NONE</code> for no encryption</p> </li> <li> <p> <code>TLS</code> for Transport Layer Security</p> </li> </ul>
            network_type: <p>Specifies the IP protocol(s) the cluster uses for network communications. Values are:</p> <ul> <li> <p> <code>ipv4</code> - The cluster is accessible only through IPv4 addresses</p> </li> <li> <p> <code>ipv6</code> - The cluster is accessible only through IPv6 addresses</p> </li> <li> <p> <code>dual_stack</code> - The cluster is accessible through both IPv4 and IPv6 addresses.</p> </li> </ul> <note> <p>If no explicit <code>NetworkType</code> is provided, the network type is derived based on the subnet group's configuration.</p> </note>

        Raises:
            capo_dax.errors.cluster_already_exists_fault.ClusterAlreadyExistsFault: <p>You already have a DAX cluster with the given identifier.</p>
            capo_dax.errors.cluster_quota_for_customer_exceeded_fault.ClusterQuotaForCustomerExceededFault: <p>You have attempted to exceed the maximum number of DAX clusters for your Amazon Web Services account.</p>
            capo_dax.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault: <p>There are not enough system resources to create the cluster you requested (or to resize an already-existing cluster). </p>
            capo_dax.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The requested DAX cluster is not in the <i>available</i> state.</p>
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_group_state_fault.InvalidParameterGroupStateFault: <p>One or more parameters in a parameter group are in an invalid state.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The VPC network is in an invalid state.</p>
            capo_dax.errors.node_quota_for_cluster_exceeded_fault.NodeQuotaForClusterExceededFault: <p>You have attempted to exceed the maximum number of nodes for a DAX cluster.</p>
            capo_dax.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault: <p>You have attempted to exceed the maximum number of nodes for your Amazon Web Services account.</p>
            capo_dax.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached the maximum number of x509 certificates that can be created for encrypted clusters in a 30 day period. Contact Amazon Web Services customer support to discuss options for continuing to create encrypted clusters.</p>
            capo_dax.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault: <p>The requested subnet group name does not refer to an existing subnet group.</p>
            capo_dax.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>You have exceeded the maximum number of tags for this DAX cluster.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.create_cluster_request.CreateClusterRequest]",
        ) -> OperationResponse[
            "capo_dax.types.create_cluster_response.CreateClusterResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.create_cluster

            output, http_response = (
                capo_dax._operations.amazon_daxv3.create_cluster.create_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.create_cluster_request.CreateClusterRequest = {
            "cluster_name": cluster_name,
            "node_type": node_type,
            "replication_factor": replication_factor,
            "iam_role_arn": iam_role_arn,
        }
        if description is not None:
            input_["description"] = description
        if availability_zones is not None:
            input_["availability_zones"] = availability_zones
        if subnet_group_name is not None:
            input_["subnet_group_name"] = subnet_group_name
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if notification_topic_arn is not None:
            input_["notification_topic_arn"] = notification_topic_arn
        if parameter_group_name is not None:
            input_["parameter_group_name"] = parameter_group_name
        if tags is not None:
            input_["tags"] = tags
        if sse_specification is not None:
            input_["sse_specification"] = sse_specification
        if cluster_endpoint_encryption_type is not None:
            input_["cluster_endpoint_encryption_type"] = (
                cluster_endpoint_encryption_type
            )
        if network_type is not None:
            input_["network_type"] = network_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_parameter_group(
        self,
        parameter_group_name: "capo_dax.types.string.String",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        description: Optional["capo_dax.types.string.String"] = None,
    ) -> "capo_dax.types.create_parameter_group_response.CreateParameterGroupResponse":
        """<p>Creates a new parameter group. A parameter group is a collection of parameters that you apply to all of the nodes in a DAX cluster.</p>

        Args:
            parameter_group_name: <p>The name of the parameter group to apply to all of the clusters in this replication group.</p>
            description: <p>A description of the parameter group.</p>

        Raises:
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_group_state_fault.InvalidParameterGroupStateFault: <p>One or more parameters in a parameter group are in an invalid state.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.parameter_group_already_exists_fault.ParameterGroupAlreadyExistsFault: <p>The specified parameter group already exists.</p>
            capo_dax.errors.parameter_group_quota_exceeded_fault.ParameterGroupQuotaExceededFault: <p>You have attempted to exceed the maximum number of parameter groups.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.create_parameter_group_request.CreateParameterGroupRequest]",
        ) -> OperationResponse[
            "capo_dax.types.create_parameter_group_response.CreateParameterGroupResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.create_parameter_group

            output, http_response = (
                capo_dax._operations.amazon_daxv3.create_parameter_group.create_parameter_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.create_parameter_group_request.CreateParameterGroupRequest = {
            "parameter_group_name": parameter_group_name
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_subnet_group(
        self,
        subnet_group_name: "capo_dax.types.string.String",
        subnet_ids: "capo_dax.types.subnet_identifier_list.SubnetIdentifierList",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        description: Optional["capo_dax.types.string.String"] = None,
    ) -> "capo_dax.types.create_subnet_group_response.CreateSubnetGroupResponse":
        """<p>Creates a new subnet group.</p>

        Args:
            subnet_group_name: <p>A name for the subnet group. This value is stored as a lowercase string. </p>
            description: <p>A description for the subnet group</p>
            subnet_ids: <p>A list of VPC subnet IDs for the subnet group.</p>

        Raises:
            capo_dax.errors.invalid_subnet.InvalidSubnet: <p>An invalid subnet identifier was specified.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.subnet_group_already_exists_fault.SubnetGroupAlreadyExistsFault: <p>The specified subnet group already exists.</p>
            capo_dax.errors.subnet_group_quota_exceeded_fault.SubnetGroupQuotaExceededFault: <p>The request cannot be processed because it would exceed the allowed number of subnets in a subnet group.</p>
            capo_dax.errors.subnet_not_allowed_fault.SubnetNotAllowedFault: <p>The specified subnet can't be used for the requested network type. This error occurs when either there aren't enough subnets of the required network type to create the cluster, or when you try to use a subnet that doesn't support the requested network type (for example, trying to create a dual-stack cluster with a subnet that doesn't have IPv6 CIDR). </p>
            capo_dax.errors.subnet_quota_exceeded_fault.SubnetQuotaExceededFault: <p>The request cannot be processed because it would exceed the allowed number of subnets in a subnet group.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.create_subnet_group_request.CreateSubnetGroupRequest]",
        ) -> OperationResponse[
            "capo_dax.types.create_subnet_group_response.CreateSubnetGroupResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.create_subnet_group

            output, http_response = (
                capo_dax._operations.amazon_daxv3.create_subnet_group.create_subnet_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.create_subnet_group_request.CreateSubnetGroupRequest = {
            "subnet_group_name": subnet_group_name,
            "subnet_ids": subnet_ids,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def decrease_replication_factor(
        self,
        cluster_name: "capo_dax.types.string.String",
        new_replication_factor: "capo_dax.types.integer.Integer",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        availability_zones: Optional[
            "capo_dax.types.availability_zone_list.AvailabilityZoneList"
        ] = None,
        node_ids_to_remove: Optional[
            "capo_dax.types.node_identifier_list.NodeIdentifierList"
        ] = None,
    ) -> "capo_dax.types.decrease_replication_factor_response.DecreaseReplicationFactorResponse":
        """<p>Removes one or more nodes from a DAX cluster.</p> <note> <p>You cannot use <code>DecreaseReplicationFactor</code> to remove the last node in a DAX cluster. If you need to do this, use <code>DeleteCluster</code> instead.</p> </note>

        Args:
            cluster_name: <p>The name of the DAX cluster from which you want to remove nodes.</p>
            new_replication_factor: <p>The new number of nodes for the DAX cluster.</p>
            availability_zones: <p>The Availability Zone(s) from which to remove nodes.</p>
            node_ids_to_remove: <p>The unique identifiers of the nodes to be removed from the cluster.</p>

        Raises:
            capo_dax.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing DAX cluster.</p>
            capo_dax.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The requested DAX cluster is not in the <i>available</i> state.</p>
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.node_not_found_fault.NodeNotFoundFault: <p>None of the nodes in the cluster have the given node ID.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.decrease_replication_factor_request.DecreaseReplicationFactorRequest]",
        ) -> OperationResponse[
            "capo_dax.types.decrease_replication_factor_response.DecreaseReplicationFactorResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.decrease_replication_factor

            output, http_response = (
                capo_dax._operations.amazon_daxv3.decrease_replication_factor.decrease_replication_factor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.decrease_replication_factor_request.DecreaseReplicationFactorRequest = {
            "cluster_name": cluster_name,
            "new_replication_factor": new_replication_factor,
        }
        if availability_zones is not None:
            input_["availability_zones"] = availability_zones
        if node_ids_to_remove is not None:
            input_["node_ids_to_remove"] = node_ids_to_remove

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cluster(
        self,
        cluster_name: "capo_dax.types.string.String",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
    ) -> "capo_dax.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes a previously provisioned DAX cluster. <i>DeleteCluster</i> deletes all associated nodes, node endpoints and the DAX cluster itself. When you receive a successful response from this action, DAX immediately begins deleting the cluster; you cannot cancel or revert this action.</p>

        Args:
            cluster_name: <p>The name of the cluster to be deleted.</p>

        Raises:
            capo_dax.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing DAX cluster.</p>
            capo_dax.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The requested DAX cluster is not in the <i>available</i> state.</p>
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> OperationResponse[
            "capo_dax.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.delete_cluster

            output, http_response = (
                capo_dax._operations.amazon_daxv3.delete_cluster.delete_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.delete_cluster_request.DeleteClusterRequest = {
            "cluster_name": cluster_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_parameter_group(
        self,
        parameter_group_name: "capo_dax.types.string.String",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
    ) -> "capo_dax.types.delete_parameter_group_response.DeleteParameterGroupResponse":
        """<p>Deletes the specified parameter group. You cannot delete a parameter group if it is associated with any DAX clusters.</p>

        Args:
            parameter_group_name: <p>The name of the parameter group to delete.</p>

        Raises:
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_group_state_fault.InvalidParameterGroupStateFault: <p>One or more parameters in a parameter group are in an invalid state.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.delete_parameter_group_request.DeleteParameterGroupRequest]",
        ) -> OperationResponse[
            "capo_dax.types.delete_parameter_group_response.DeleteParameterGroupResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.delete_parameter_group

            output, http_response = (
                capo_dax._operations.amazon_daxv3.delete_parameter_group.delete_parameter_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.delete_parameter_group_request.DeleteParameterGroupRequest = {
            "parameter_group_name": parameter_group_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_subnet_group(
        self,
        subnet_group_name: "capo_dax.types.string.String",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
    ) -> "capo_dax.types.delete_subnet_group_response.DeleteSubnetGroupResponse":
        """<p>Deletes a subnet group.</p> <note> <p>You cannot delete a subnet group if it is associated with any DAX clusters.</p> </note>

        Args:
            subnet_group_name: <p>The name of the subnet group to delete.</p>

        Raises:
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.subnet_group_in_use_fault.SubnetGroupInUseFault: <p>The specified subnet group is currently in use.</p>
            capo_dax.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault: <p>The requested subnet group name does not refer to an existing subnet group.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.delete_subnet_group_request.DeleteSubnetGroupRequest]",
        ) -> OperationResponse[
            "capo_dax.types.delete_subnet_group_response.DeleteSubnetGroupResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.delete_subnet_group

            output, http_response = (
                capo_dax._operations.amazon_daxv3.delete_subnet_group.delete_subnet_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.delete_subnet_group_request.DeleteSubnetGroupRequest = {
            "subnet_group_name": subnet_group_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_clusters(
        self,
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        cluster_names: Optional[
            "capo_dax.types.cluster_name_list.ClusterNameList"
        ] = None,
        max_results: Optional["capo_dax.types.integer_optional.IntegerOptional"] = None,
        next_token: Optional["capo_dax.types.string.String"] = None,
    ) -> "capo_dax.types.describe_clusters_response.DescribeClustersResponse":
        """<p>Returns information about all provisioned DAX clusters if no cluster identifier is specified, or about a specific DAX cluster if a cluster identifier is supplied.</p> <p>If the cluster is in the CREATING state, only cluster level information will be displayed until all of the nodes are successfully provisioned.</p> <p>If the cluster is in the DELETING state, only cluster level information will be displayed.</p> <p>If nodes are currently being added to the DAX cluster, node endpoint information and creation time for the additional nodes will not be displayed until they are completely provisioned. When the DAX cluster state is <i>available</i>, the cluster is ready for use.</p> <p>If nodes are currently being removed from the DAX cluster, no endpoint information for the removed nodes is displayed.</p>

        Args:
            cluster_names: <p>The names of the DAX clusters being described.</p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p> <p>The value for <code>MaxResults</code> must be between 20 and 100.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by <code>MaxResults</code>.</p>

        Raises:
            capo_dax.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing DAX cluster.</p>
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.describe_clusters_request.DescribeClustersRequest]",
        ) -> OperationResponse[
            "capo_dax.types.describe_clusters_response.DescribeClustersResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.describe_clusters

            output, http_response = (
                capo_dax._operations.amazon_daxv3.describe_clusters.describe_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.describe_clusters_request.DescribeClustersRequest = {}
        if cluster_names is not None:
            input_["cluster_names"] = cluster_names
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

    def describe_default_parameters(
        self,
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        max_results: Optional["capo_dax.types.integer_optional.IntegerOptional"] = None,
        next_token: Optional["capo_dax.types.string.String"] = None,
    ) -> "capo_dax.types.describe_default_parameters_response.DescribeDefaultParametersResponse":
        """<p>Returns the default system parameter information for the DAX caching software.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p> <p>The value for <code>MaxResults</code> must be between 20 and 100.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by <code>MaxResults</code>.</p>

        Raises:
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.describe_default_parameters_request.DescribeDefaultParametersRequest]",
        ) -> OperationResponse[
            "capo_dax.types.describe_default_parameters_response.DescribeDefaultParametersResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.describe_default_parameters

            output, http_response = (
                capo_dax._operations.amazon_daxv3.describe_default_parameters.describe_default_parameters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.describe_default_parameters_request.DescribeDefaultParametersRequest = {}
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

    def describe_events(
        self,
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        source_name: Optional["capo_dax.types.string.String"] = None,
        source_type: Optional["capo_dax.types.source_type.SourceType"] = None,
        start_time: Optional["capo_dax.types.t_stamp.TStamp"] = None,
        end_time: Optional["capo_dax.types.t_stamp.TStamp"] = None,
        duration: Optional["capo_dax.types.integer_optional.IntegerOptional"] = None,
        max_results: Optional["capo_dax.types.integer_optional.IntegerOptional"] = None,
        next_token: Optional["capo_dax.types.string.String"] = None,
    ) -> "capo_dax.types.describe_events_response.DescribeEventsResponse":
        """<p>Returns events related to DAX clusters and parameter groups. You can obtain events specific to a particular DAX cluster or parameter group by providing the name as a parameter.</p> <p>By default, only the events occurring within the last 24 hours are returned; however, you can retrieve up to 14 days' worth of events if necessary.</p>

        Args:
            source_name: <p>The identifier of the event source for which events will be returned. If not specified, then all sources are included in the response.</p>
            source_type: <p>The event source to retrieve events for. If no value is specified, all events are returned.</p>
            start_time: <p>The beginning of the time interval to retrieve events for, specified in ISO 8601 format.</p>
            end_time: <p>The end of the time interval for which to retrieve events, specified in ISO 8601 format.</p>
            duration: <p>The number of minutes' worth of events to retrieve.</p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p> <p>The value for <code>MaxResults</code> must be between 20 and 100.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by <code>MaxResults</code>.</p>

        Raises:
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.describe_events_request.DescribeEventsRequest]",
        ) -> OperationResponse[
            "capo_dax.types.describe_events_response.DescribeEventsResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.describe_events

            output, http_response = (
                capo_dax._operations.amazon_daxv3.describe_events.describe_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.describe_events_request.DescribeEventsRequest = {}
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_parameter_groups(
        self,
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        parameter_group_names: Optional[
            "capo_dax.types.parameter_group_name_list.ParameterGroupNameList"
        ] = None,
        max_results: Optional["capo_dax.types.integer_optional.IntegerOptional"] = None,
        next_token: Optional["capo_dax.types.string.String"] = None,
    ) -> "capo_dax.types.describe_parameter_groups_response.DescribeParameterGroupsResponse":
        """<p>Returns a list of parameter group descriptions. If a parameter group name is specified, the list will contain only the descriptions for that group.</p>

        Args:
            parameter_group_names: <p>The names of the parameter groups.</p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p> <p>The value for <code>MaxResults</code> must be between 20 and 100.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by <code>MaxResults</code>.</p>

        Raises:
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.describe_parameter_groups_request.DescribeParameterGroupsRequest]",
        ) -> OperationResponse[
            "capo_dax.types.describe_parameter_groups_response.DescribeParameterGroupsResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.describe_parameter_groups

            output, http_response = (
                capo_dax._operations.amazon_daxv3.describe_parameter_groups.describe_parameter_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.describe_parameter_groups_request.DescribeParameterGroupsRequest = {}
        if parameter_group_names is not None:
            input_["parameter_group_names"] = parameter_group_names
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

    def describe_parameters(
        self,
        parameter_group_name: "capo_dax.types.string.String",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        source: Optional["capo_dax.types.string.String"] = None,
        max_results: Optional["capo_dax.types.integer_optional.IntegerOptional"] = None,
        next_token: Optional["capo_dax.types.string.String"] = None,
    ) -> "capo_dax.types.describe_parameters_response.DescribeParametersResponse":
        """<p>Returns the detailed parameter list for a particular parameter group.</p>

        Args:
            parameter_group_name: <p>The name of the parameter group.</p>
            source: <p>How the parameter is defined. For example, <code>system</code> denotes a system-defined parameter.</p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p> <p>The value for <code>MaxResults</code> must be between 20 and 100.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by <code>MaxResults</code>.</p>

        Raises:
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.describe_parameters_request.DescribeParametersRequest]",
        ) -> OperationResponse[
            "capo_dax.types.describe_parameters_response.DescribeParametersResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.describe_parameters

            output, http_response = (
                capo_dax._operations.amazon_daxv3.describe_parameters.describe_parameters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.describe_parameters_request.DescribeParametersRequest = {
            "parameter_group_name": parameter_group_name
        }
        if source is not None:
            input_["source"] = source
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

    def describe_subnet_groups(
        self,
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        subnet_group_names: Optional[
            "capo_dax.types.subnet_group_name_list.SubnetGroupNameList"
        ] = None,
        max_results: Optional["capo_dax.types.integer_optional.IntegerOptional"] = None,
        next_token: Optional["capo_dax.types.string.String"] = None,
    ) -> "capo_dax.types.describe_subnet_groups_response.DescribeSubnetGroupsResponse":
        """<p>Returns a list of subnet group descriptions. If a subnet group name is specified, the list will contain only the description of that group.</p>

        Args:
            subnet_group_names: <p>The name of the subnet group.</p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p> <p>The value for <code>MaxResults</code> must be between 20 and 100.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by <code>MaxResults</code>.</p>

        Raises:
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault: <p>The requested subnet group name does not refer to an existing subnet group.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.describe_subnet_groups_request.DescribeSubnetGroupsRequest]",
        ) -> OperationResponse[
            "capo_dax.types.describe_subnet_groups_response.DescribeSubnetGroupsResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.describe_subnet_groups

            output, http_response = (
                capo_dax._operations.amazon_daxv3.describe_subnet_groups.describe_subnet_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.describe_subnet_groups_request.DescribeSubnetGroupsRequest = {}
        if subnet_group_names is not None:
            input_["subnet_group_names"] = subnet_group_names
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

    def increase_replication_factor(
        self,
        cluster_name: "capo_dax.types.string.String",
        new_replication_factor: "capo_dax.types.integer.Integer",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        availability_zones: Optional[
            "capo_dax.types.availability_zone_list.AvailabilityZoneList"
        ] = None,
    ) -> "capo_dax.types.increase_replication_factor_response.IncreaseReplicationFactorResponse":
        """<p>Adds one or more nodes to a DAX cluster.</p>

        Args:
            cluster_name: <p>The name of the DAX cluster that will receive additional nodes.</p>
            new_replication_factor: <p>The new number of nodes for the DAX cluster.</p>
            availability_zones: <p>The Availability Zones (AZs) in which the cluster nodes will be created. All nodes belonging to the cluster are placed in these Availability Zones. Use this parameter if you want to distribute the nodes across multiple AZs.</p>

        Raises:
            capo_dax.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing DAX cluster.</p>
            capo_dax.errors.insufficient_cluster_capacity_fault.InsufficientClusterCapacityFault: <p>There are not enough system resources to create the cluster you requested (or to resize an already-existing cluster). </p>
            capo_dax.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The requested DAX cluster is not in the <i>available</i> state.</p>
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.invalid_vpc_network_state_fault.InvalidVPCNetworkStateFault: <p>The VPC network is in an invalid state.</p>
            capo_dax.errors.node_quota_for_cluster_exceeded_fault.NodeQuotaForClusterExceededFault: <p>You have attempted to exceed the maximum number of nodes for a DAX cluster.</p>
            capo_dax.errors.node_quota_for_customer_exceeded_fault.NodeQuotaForCustomerExceededFault: <p>You have attempted to exceed the maximum number of nodes for your Amazon Web Services account.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.increase_replication_factor_request.IncreaseReplicationFactorRequest]",
        ) -> OperationResponse[
            "capo_dax.types.increase_replication_factor_response.IncreaseReplicationFactorResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.increase_replication_factor

            output, http_response = (
                capo_dax._operations.amazon_daxv3.increase_replication_factor.increase_replication_factor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.increase_replication_factor_request.IncreaseReplicationFactorRequest = {
            "cluster_name": cluster_name,
            "new_replication_factor": new_replication_factor,
        }
        if availability_zones is not None:
            input_["availability_zones"] = availability_zones

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags(
        self,
        resource_name: "capo_dax.types.string.String",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        next_token: Optional["capo_dax.types.string.String"] = None,
    ) -> "capo_dax.types.list_tags_response.ListTagsResponse":
        """<p>List all of the tags for a DAX cluster. You can call <code>ListTags</code> up to 10 times per second, per account.</p>

        Args:
            resource_name: <p>The name of the DAX resource to which the tags belong.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token.</p>

        Raises:
            capo_dax.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing DAX cluster.</p>
            capo_dax.errors.invalid_arn_fault.InvalidARNFault: <p>The Amazon Resource Name (ARN) supplied in the request is not valid.</p>
            capo_dax.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The requested DAX cluster is not in the <i>available</i> state.</p>
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.list_tags_request.ListTagsRequest]",
        ) -> OperationResponse["capo_dax.types.list_tags_response.ListTagsResponse"]:
            import capo_dax._operations.amazon_daxv3.list_tags

            output, http_response = (
                capo_dax._operations.amazon_daxv3.list_tags.list_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.list_tags_request.ListTagsRequest = {
            "resource_name": resource_name
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reboot_node(
        self,
        cluster_name: "capo_dax.types.string.String",
        node_id: "capo_dax.types.string.String",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
    ) -> "capo_dax.types.reboot_node_response.RebootNodeResponse":
        """<p>Reboots a single node of a DAX cluster. The reboot action takes place as soon as possible. During the reboot, the node status is set to REBOOTING.</p> <note> <p> <code>RebootNode</code> restarts the DAX engine process and does not remove the contents of the cache.</p> </note>

        Args:
            cluster_name: <p>The name of the DAX cluster containing the node to be rebooted.</p>
            node_id: <p>The system-assigned ID of the node to be rebooted.</p>

        Raises:
            capo_dax.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing DAX cluster.</p>
            capo_dax.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The requested DAX cluster is not in the <i>available</i> state.</p>
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.node_not_found_fault.NodeNotFoundFault: <p>None of the nodes in the cluster have the given node ID.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.reboot_node_request.RebootNodeRequest]",
        ) -> OperationResponse[
            "capo_dax.types.reboot_node_response.RebootNodeResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.reboot_node

            output, http_response = (
                capo_dax._operations.amazon_daxv3.reboot_node.reboot_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.reboot_node_request.RebootNodeRequest = {
            "cluster_name": cluster_name,
            "node_id": node_id,
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
        resource_name: "capo_dax.types.string.String",
        tags: "capo_dax.types.tag_list.TagList",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
    ) -> "capo_dax.types.tag_resource_response.TagResourceResponse":
        """<p>Associates a set of tags with a DAX resource. You can call <code>TagResource</code> up to 5 times per second, per account. </p>

        Args:
            resource_name: <p>The name of the DAX resource to which tags should be added.</p>
            tags: <p>The tags to be assigned to the DAX resource. </p>

        Raises:
            capo_dax.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing DAX cluster.</p>
            capo_dax.errors.invalid_arn_fault.InvalidARNFault: <p>The Amazon Resource Name (ARN) supplied in the request is not valid.</p>
            capo_dax.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The requested DAX cluster is not in the <i>available</i> state.</p>
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.tag_quota_per_resource_exceeded.TagQuotaPerResourceExceeded: <p>You have exceeded the maximum number of tags for this DAX cluster.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_dax.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.tag_resource

            output, http_response = (
                capo_dax._operations.amazon_daxv3.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.tag_resource_request.TagResourceRequest = {
            "resource_name": resource_name,
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
        resource_name: "capo_dax.types.string.String",
        tag_keys: "capo_dax.types.key_list.KeyList",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
    ) -> "capo_dax.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the association of tags from a DAX resource. You can call <code>UntagResource</code> up to 5 times per second, per account. </p>

        Args:
            resource_name: <p>The name of the DAX resource from which the tags should be removed.</p>
            tag_keys: <p>A list of tag keys. If the DAX cluster has any tags with these keys, then the tags are removed from the cluster.</p>

        Raises:
            capo_dax.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing DAX cluster.</p>
            capo_dax.errors.invalid_arn_fault.InvalidARNFault: <p>The Amazon Resource Name (ARN) supplied in the request is not valid.</p>
            capo_dax.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The requested DAX cluster is not in the <i>available</i> state.</p>
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.tag_not_found_fault.TagNotFoundFault: <p>The tag does not exist.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_dax.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.untag_resource

            output, http_response = (
                capo_dax._operations.amazon_daxv3.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.untag_resource_request.UntagResourceRequest = {
            "resource_name": resource_name,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cluster(
        self,
        cluster_name: "capo_dax.types.string.String",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        description: Optional["capo_dax.types.string.String"] = None,
        preferred_maintenance_window: Optional["capo_dax.types.string.String"] = None,
        notification_topic_arn: Optional["capo_dax.types.string.String"] = None,
        notification_topic_status: Optional["capo_dax.types.string.String"] = None,
        parameter_group_name: Optional["capo_dax.types.string.String"] = None,
        security_group_ids: Optional[
            "capo_dax.types.security_group_identifier_list.SecurityGroupIdentifierList"
        ] = None,
    ) -> "capo_dax.types.update_cluster_response.UpdateClusterResponse":
        """<p>Modifies the settings for a DAX cluster. You can use this action to change one or more cluster configuration parameters by specifying the parameters and the new values.</p>

        Args:
            cluster_name: <p>The name of the DAX cluster to be modified.</p>
            description: <p>A description of the changes being made to the cluster.</p>
            preferred_maintenance_window: <p>A range of time when maintenance of DAX cluster software will be performed. For example: <code>sun:01:00-sun:09:00</code>. Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.</p>
            notification_topic_arn: <p>The Amazon Resource Name (ARN) that identifies the topic.</p>
            notification_topic_status: <p>The current state of the topic. A value of “active” means that notifications will be sent to the topic. A value of “inactive” means that notifications will not be sent to the topic.</p>
            parameter_group_name: <p>The name of a parameter group for this cluster.</p>
            security_group_ids: <p>A list of user-specified security group IDs to be assigned to each node in the DAX cluster. If this parameter is not specified, DAX assigns the default VPC security group to each node.</p>

        Raises:
            capo_dax.errors.cluster_not_found_fault.ClusterNotFoundFault: <p>The requested cluster ID does not refer to an existing DAX cluster.</p>
            capo_dax.errors.invalid_cluster_state_fault.InvalidClusterStateFault: <p>The requested DAX cluster is not in the <i>available</i> state.</p>
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_group_state_fault.InvalidParameterGroupStateFault: <p>One or more parameters in a parameter group are in an invalid state.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.update_cluster_request.UpdateClusterRequest]",
        ) -> OperationResponse[
            "capo_dax.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.update_cluster

            output, http_response = (
                capo_dax._operations.amazon_daxv3.update_cluster.update_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.update_cluster_request.UpdateClusterRequest = {
            "cluster_name": cluster_name
        }
        if description is not None:
            input_["description"] = description
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if notification_topic_arn is not None:
            input_["notification_topic_arn"] = notification_topic_arn
        if notification_topic_status is not None:
            input_["notification_topic_status"] = notification_topic_status
        if parameter_group_name is not None:
            input_["parameter_group_name"] = parameter_group_name
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_parameter_group(
        self,
        parameter_group_name: "capo_dax.types.string.String",
        parameter_name_values: "capo_dax.types.parameter_name_value_list.ParameterNameValueList",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
    ) -> "capo_dax.types.update_parameter_group_response.UpdateParameterGroupResponse":
        """<p>Modifies the parameters of a parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.</p>

        Args:
            parameter_group_name: <p>The name of the parameter group.</p>
            parameter_name_values: <p>An array of name-value pairs for the parameters in the group. Each element in the array represents a single parameter.</p> <note> <p> <code>record-ttl-millis</code> and <code>query-ttl-millis</code> are the only supported parameter names. For more details, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.cluster-management.custom-settings.ttl">Configuring TTL Settings</a>.</p> </note>

        Raises:
            capo_dax.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more incompatible parameters were specified.</p>
            capo_dax.errors.invalid_parameter_group_state_fault.InvalidParameterGroupStateFault: <p>One or more parameters in a parameter group are in an invalid state.</p>
            capo_dax.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value for a parameter is invalid.</p>
            capo_dax.errors.parameter_group_not_found_fault.ParameterGroupNotFoundFault: <p>The specified parameter group does not exist.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.update_parameter_group_request.UpdateParameterGroupRequest]",
        ) -> OperationResponse[
            "capo_dax.types.update_parameter_group_response.UpdateParameterGroupResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.update_parameter_group

            output, http_response = (
                capo_dax._operations.amazon_daxv3.update_parameter_group.update_parameter_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.update_parameter_group_request.UpdateParameterGroupRequest = {
            "parameter_group_name": parameter_group_name,
            "parameter_name_values": parameter_name_values,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_subnet_group(
        self,
        subnet_group_name: "capo_dax.types.string.String",
        *,
        config_overrides: Optional[DAXClientConfig] = None,
        description: Optional["capo_dax.types.string.String"] = None,
        subnet_ids: Optional[
            "capo_dax.types.subnet_identifier_list.SubnetIdentifierList"
        ] = None,
    ) -> "capo_dax.types.update_subnet_group_response.UpdateSubnetGroupResponse":
        """<p>Modifies an existing subnet group.</p>

        Args:
            subnet_group_name: <p>The name of the subnet group.</p>
            description: <p>A description of the subnet group.</p>
            subnet_ids: <p>A list of subnet IDs in the subnet group.</p>

        Raises:
            capo_dax.errors.invalid_subnet.InvalidSubnet: <p>An invalid subnet identifier was specified.</p>
            capo_dax.errors.service_linked_role_not_found_fault.ServiceLinkedRoleNotFoundFault: <p>The specified service linked role (SLR) was not found.</p>
            capo_dax.errors.subnet_group_not_found_fault.SubnetGroupNotFoundFault: <p>The requested subnet group name does not refer to an existing subnet group.</p>
            capo_dax.errors.subnet_in_use.SubnetInUse: <p>The requested subnet is being used by another subnet group.</p>
            capo_dax.errors.subnet_not_allowed_fault.SubnetNotAllowedFault: <p>The specified subnet can't be used for the requested network type. This error occurs when either there aren't enough subnets of the required network type to create the cluster, or when you try to use a subnet that doesn't support the requested network type (for example, trying to create a dual-stack cluster with a subnet that doesn't have IPv6 CIDR). </p>
            capo_dax.errors.subnet_quota_exceeded_fault.SubnetQuotaExceededFault: <p>The request cannot be processed because it would exceed the allowed number of subnets in a subnet group.</p>
            capo_dax.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dax.types.update_subnet_group_request.UpdateSubnetGroupRequest]",
        ) -> OperationResponse[
            "capo_dax.types.update_subnet_group_response.UpdateSubnetGroupResponse"
        ]:
            import capo_dax._operations.amazon_daxv3.update_subnet_group

            output, http_response = (
                capo_dax._operations.amazon_daxv3.update_subnet_group.update_subnet_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dax.types.update_subnet_group_request.UpdateSubnetGroupRequest = {
            "subnet_group_name": subnet_group_name
        }
        if description is not None:
            input_["description"] = description
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids

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
