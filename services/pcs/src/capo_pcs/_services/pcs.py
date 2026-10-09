"""Generated from Smithy shape ``com.amazonaws.pcs#AWSParallelComputingService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_pcs._auth._signers
import capo_pcs._auth._sigv4
from capo_pcs._auth._identity import Credentials
from capo_pcs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_pcs._auth._zapros_handler import AuthMiddleware
from capo_pcs._pagination import resolve_path as _resolve_path
from capo_pcs._resources.aws_parallel_computing_service.cluster_resource import (
    ClusterResource,
)
from capo_pcs._services._aws_config import aws_config
from capo_pcs._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_pcs.types.ami_id
    import capo_pcs.types.arn
    import capo_pcs.types.bootstrap_id
    import capo_pcs.types.cluster_identifier
    import capo_pcs.types.cluster_name
    import capo_pcs.types.cluster_slurm_configuration_request
    import capo_pcs.types.cluster_summary
    import capo_pcs.types.compute_node_group_configuration_list
    import capo_pcs.types.compute_node_group_identifier
    import capo_pcs.types.compute_node_group_name
    import capo_pcs.types.compute_node_group_slurm_configuration_request
    import capo_pcs.types.compute_node_group_summary
    import capo_pcs.types.create_cluster_request
    import capo_pcs.types.create_cluster_response
    import capo_pcs.types.create_compute_node_group_request
    import capo_pcs.types.create_compute_node_group_response
    import capo_pcs.types.create_queue_request
    import capo_pcs.types.create_queue_response
    import capo_pcs.types.custom_launch_template
    import capo_pcs.types.delete_cluster_request
    import capo_pcs.types.delete_cluster_response
    import capo_pcs.types.delete_compute_node_group_request
    import capo_pcs.types.delete_compute_node_group_response
    import capo_pcs.types.delete_queue_request
    import capo_pcs.types.delete_queue_response
    import capo_pcs.types.get_cluster_request
    import capo_pcs.types.get_cluster_response
    import capo_pcs.types.get_compute_node_group_request
    import capo_pcs.types.get_compute_node_group_response
    import capo_pcs.types.get_queue_request
    import capo_pcs.types.get_queue_response
    import capo_pcs.types.instance_list
    import capo_pcs.types.instance_profile_arn
    import capo_pcs.types.list_clusters_request
    import capo_pcs.types.list_clusters_response
    import capo_pcs.types.list_compute_node_groups_request
    import capo_pcs.types.list_compute_node_groups_response
    import capo_pcs.types.list_queues_request
    import capo_pcs.types.list_queues_response
    import capo_pcs.types.list_tags_for_resource_request
    import capo_pcs.types.list_tags_for_resource_response
    import capo_pcs.types.max_results
    import capo_pcs.types.networking_request
    import capo_pcs.types.node_lifecycle_actions_request
    import capo_pcs.types.purchase_option
    import capo_pcs.types.queue_identifier
    import capo_pcs.types.queue_name
    import capo_pcs.types.queue_slurm_configuration_request
    import capo_pcs.types.queue_summary
    import capo_pcs.types.register_compute_node_group_instance_request
    import capo_pcs.types.register_compute_node_group_instance_response
    import capo_pcs.types.request_tag_map
    import capo_pcs.types.sb_client_token
    import capo_pcs.types.scaling_configuration_request
    import capo_pcs.types.scheduler_request
    import capo_pcs.types.size
    import capo_pcs.types.spot_options
    import capo_pcs.types.string_list
    import capo_pcs.types.tag_keys
    import capo_pcs.types.tag_resource_request
    import capo_pcs.types.tag_resource_response
    import capo_pcs.types.untag_resource_request
    import capo_pcs.types.untag_resource_response
    import capo_pcs.types.update_cluster_request
    import capo_pcs.types.update_cluster_response
    import capo_pcs.types.update_cluster_slurm_configuration_request
    import capo_pcs.types.update_compute_node_group_request
    import capo_pcs.types.update_compute_node_group_response
    import capo_pcs.types.update_compute_node_group_slurm_configuration_request
    import capo_pcs.types.update_node_lifecycle_actions_request
    import capo_pcs.types.update_queue_request
    import capo_pcs.types.update_queue_response
    import capo_pcs.types.update_queue_slurm_configuration_request
    import capo_pcs.types.update_scheduler_request


class PCSClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class PCSClient:
    """A client for the ``PCS`` service.

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
        self._config = PCSClientConfig(
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
        self.cluster_resource = ClusterResource(self)

    def operation_options(
        self, config_overrides: Optional[PCSClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PCSClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_pcs.types.arn.Arn",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> "capo_pcs.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of all tags on an PCS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>

        Raises:
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.list_tags_for_resource

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_pcs.types.arn.Arn",
        tags: "capo_pcs.types.request_tag_map.RequestTagMap",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> "capo_pcs.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or edits tags on an PCS resource. Each tag consists of a tag key and a tag value. The tag key and tag value are case-sensitive strings. The tag value can be an empty (null) string. To add a tag, specify a new tag key and a tag value. To edit a tag, specify an existing tag key and a new tag value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>

        Raises:
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. To learn how to increase your service quota, see <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i> </p> <p> <u>Examples</u> </p> <ul> <li> <p>The max number of clusters or queues has been reached for the account.</p> </li> <li> <p>The max number of compute node groups has been reached for the associated cluster.</p> </li> <li> <p>The total of <code>maxInstances</code> across all compute node groups has been reached for associated cluster.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.tag_resource

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_pcs.types.arn.Arn",
        tag_keys: "capo_pcs.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> "capo_pcs.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes tags from an PCS resource. To delete a tag, specify the tag key and the Amazon Resource Name (ARN) of the PCS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>1 or more tag keys to remove from the resource. Specify only tag keys and not tag values.</p>

        Raises:
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.untag_resource

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.untag_resource_request.UntagResourceRequest = {
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

    def create_cluster(
        self,
        cluster_name: "capo_pcs.types.cluster_name.ClusterName",
        scheduler: "capo_pcs.types.scheduler_request.SchedulerRequest",
        size: "capo_pcs.types.size.Size",
        networking: "capo_pcs.types.networking_request.NetworkingRequest",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        slurm_configuration: Optional[
            "capo_pcs.types.cluster_slurm_configuration_request.ClusterSlurmConfigurationRequest"
        ] = None,
        client_token: Optional["capo_pcs.types.sb_client_token.SBClientToken"] = None,
        tags: Optional["capo_pcs.types.request_tag_map.RequestTagMap"] = None,
    ) -> "capo_pcs.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates a cluster in your account. PCS creates the cluster controller in a service-owned account. The cluster controller communicates with the cluster resources in your account. The subnets and security groups for the cluster must already exist before you use this API action.</p> <note> <p>It takes time for PCS to create the cluster. The cluster is in a <code>Creating</code> state until it is ready to use. There can only be 1 cluster in a <code>Creating</code> state per Amazon Web Services Region per Amazon Web Services account. <code>CreateCluster</code> fails with a <code>ServiceQuotaExceededException</code> if there is already a cluster in a <code>Creating</code> state.</p> </note>

        Args:
            cluster_name: <p>A name to identify the cluster. Example: <code>MyCluster</code> </p>
            scheduler: <p>The cluster management and job scheduling software associated with the cluster.</p>
            size: <p>A value that determines the maximum number of compute nodes in the cluster and the maximum number of jobs (active and queued).</p> <ul> <li> <p> <code>SMALL</code>: 32 compute nodes and 256 jobs</p> </li> <li> <p> <code>MEDIUM</code>: 512 compute nodes and 8192 jobs</p> </li> <li> <p> <code>LARGE</code>: 2048 compute nodes and 16,384 jobs</p> </li> </ul>
            networking: <p>The networking configuration used to set up the cluster's control plane.</p>
            slurm_configuration: <p>Additional options related to the Slurm scheduler.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>
            tags: <p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. To learn how to increase your service quota, see <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i> </p> <p> <u>Examples</u> </p> <ul> <li> <p>The max number of clusters or queues has been reached for the account.</p> </li> <li> <p>The max number of compute node groups has been reached for the associated cluster.</p> </li> <li> <p>The total of <code>maxInstances</code> across all compute node groups has been reached for associated cluster.</p> </li> </ul>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.create_cluster_request.CreateClusterRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.create_cluster_response.CreateClusterResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.create_cluster

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.create_cluster.create_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.create_cluster_request.CreateClusterRequest = {
            "cluster_name": cluster_name,
            "scheduler": scheduler,
            "size": size,
            "networking": networking,
        }
        if slurm_configuration is not None:
            input_["slurm_configuration"] = slurm_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cluster(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        client_token: Optional["capo_pcs.types.sb_client_token.SBClientToken"] = None,
        slurm_configuration: Optional[
            "capo_pcs.types.update_cluster_slurm_configuration_request.UpdateClusterSlurmConfigurationRequest"
        ] = None,
        scheduler: Optional[
            "capo_pcs.types.update_scheduler_request.UpdateSchedulerRequest"
        ] = None,
    ) -> "capo_pcs.types.update_cluster_response.UpdateClusterResponse":
        """<p>Updates a cluster configuration. You can update the scheduler version, modify scheduler settings, and update accounting configuration for an existing cluster. For more information about updating the scheduler version, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_version_update.html">Updating the scheduler version on a cluster</a> in the <i>PCS User Guide</i>. </p> <note> <p>You can only update clusters that are in <code>ACTIVE</code>, <code>UPDATE_FAILED</code>, or <code>SUSPENDED</code> state. All associated resources (queues and compute node groups) must be in <code>ACTIVE</code> state before you can update the cluster.</p> </note>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to update.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>
            slurm_configuration: <p>Additional options related to the Slurm scheduler.</p>
            scheduler: <p>The scheduler configuration to update for the cluster. Use this to update the scheduler version. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_version_update.html">Updating the scheduler version on a cluster</a> in the <i>PCS User Guide</i>.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.update_cluster_request.UpdateClusterRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.update_cluster

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.update_cluster.update_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.update_cluster_request.UpdateClusterRequest = {
            "cluster_identifier": cluster_identifier
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if slurm_configuration is not None:
            input_["slurm_configuration"] = slurm_configuration
        if scheduler is not None:
            input_["scheduler"] = scheduler

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cluster(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        client_token: Optional["capo_pcs.types.sb_client_token.SBClientToken"] = None,
    ) -> "capo_pcs.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes a cluster and all its linked resources. You must delete all queues and compute node groups associated with the cluster before you can delete the cluster.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.delete_cluster

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.delete_cluster.delete_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.delete_cluster_request.DeleteClusterRequest = {
            "cluster_identifier": cluster_identifier
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cluster(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> "capo_pcs.types.get_cluster_response.GetClusterResponse":
        """<p>Returns detailed information about a running cluster in your account. This API action provides networking information, endpoint information for communication with the scheduler, and provisioning status.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.get_cluster_request.GetClusterRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.get_cluster_response.GetClusterResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.get_cluster

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.get_cluster.get_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.get_cluster_request.GetClusterRequest = {
            "cluster_identifier": cluster_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_compute_node_group_instance(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        bootstrap_id: "capo_pcs.types.bootstrap_id.BootstrapId",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> "capo_pcs.types.register_compute_node_group_instance_response.RegisterComputeNodeGroupInstanceResponse":
        """<important> <p>This API action isn't intended for you to use.</p> </important> <p>PCS uses this API action to register the compute nodes it launches in your account.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to register the compute node group instance in.</p>
            bootstrap_id: <p>The client-generated token to allow for retries.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.register_compute_node_group_instance_request.RegisterComputeNodeGroupInstanceRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.register_compute_node_group_instance_response.RegisterComputeNodeGroupInstanceResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.register_compute_node_group_instance

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.register_compute_node_group_instance.register_compute_node_group_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.register_compute_node_group_instance_request.RegisterComputeNodeGroupInstanceRequest = {
            "cluster_identifier": cluster_identifier,
            "bootstrap_id": bootstrap_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_clusters(
        self,
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional["capo_pcs.types.max_results.MaxResults"] = None,
    ) -> "capo_pcs.types.list_clusters_response.ListClustersResponse":
        """<p>Returns a list of running clusters in your account.</p>

        Args:
            next_token: <p>The value of <code>nextToken</code> is a unique pagination token for each page of results returned. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token returns an <code>HTTP 400 InvalidToken</code> error.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 10 results, and the maximum allowed page size is 100 results. A value of 0 uses the default.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.list_clusters_request.ListClustersRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.list_clusters_response.ListClustersResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.list_clusters

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.list_clusters.list_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.list_clusters_request.ListClustersRequest = {}
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

    def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional["capo_pcs.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_pcs.types.cluster_summary.ClusterSummary]":
        _token = next_token
        while True:
            _response = self.list_clusters(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_compute_node_group(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        compute_node_group_name: "capo_pcs.types.compute_node_group_name.ComputeNodeGroupName",
        subnet_ids: "capo_pcs.types.string_list.StringList",
        custom_launch_template: "capo_pcs.types.custom_launch_template.CustomLaunchTemplate",
        iam_instance_profile_arn: "capo_pcs.types.instance_profile_arn.InstanceProfileArn",
        scaling_configuration: "capo_pcs.types.scaling_configuration_request.ScalingConfigurationRequest",
        instance_configs: "capo_pcs.types.instance_list.InstanceList",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        ami_id: Optional["capo_pcs.types.ami_id.AmiId"] = None,
        purchase_option: Optional[
            "capo_pcs.types.purchase_option.PurchaseOption"
        ] = None,
        spot_options: Optional["capo_pcs.types.spot_options.SpotOptions"] = None,
        slurm_configuration: Optional[
            "capo_pcs.types.compute_node_group_slurm_configuration_request.ComputeNodeGroupSlurmConfigurationRequest"
        ] = None,
        node_lifecycle_actions: Optional[
            "capo_pcs.types.node_lifecycle_actions_request.NodeLifecycleActionsRequest"
        ] = None,
        client_token: Optional["capo_pcs.types.sb_client_token.SBClientToken"] = None,
        tags: Optional["capo_pcs.types.request_tag_map.RequestTagMap"] = None,
    ) -> "capo_pcs.types.create_compute_node_group_response.CreateComputeNodeGroupResponse":
        """<p>Creates a managed set of compute nodes. You associate a compute node group with a cluster through 1 or more PCS queues or as part of the login fleet. A compute node group includes the definition of the compute properties and lifecycle management. PCS uses the information you provide to this API action to launch compute nodes in your account. You can only specify subnets in the same Amazon VPC as your cluster. You receive billing charges for the compute nodes that PCS launches in your account. You must already have a launch template before you call this API. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html">Launch an instance from a launch template</a> in the <i>Amazon Elastic Compute Cloud User Guide for Linux Instances</i>.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to create a compute node group in.</p>
            compute_node_group_name: <p>A name to identify the cluster. Example: <code>MyCluster</code> </p>
            ami_id: <p> The ID of the Amazon Machine Image (AMI) that PCS uses to launch compute nodes (Amazon EC2 instances). If you don't provide this value, PCS uses the AMI ID specified in the custom launch template.</p>
            subnet_ids: <p>The list of subnet IDs where the compute node group launches instances. Subnets must be in the same VPC as the cluster.</p>
            purchase_option: <p>Specifies how EC2 instances are purchased on your behalf. PCS supports On-Demand Instances, Spot Instances, Interruptible Capacity Reservations, On-Demand Capacity Reservations, and Amazon EC2 Capacity Blocks for ML. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html">Amazon EC2 billing and purchasing options</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. For more information about PCS support for Capacity Blocks, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks.html">Using Amazon EC2 Capacity Blocks for ML with PCS</a> in the <i>PCS User Guide</i>. For more information about PCS support for interruptible capacity reservations, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-iodcr.html">Using I-ODCRs with PCS</a> in the <i>PCS User Guide</i>. Choose On-Demand if you plan to use an On-Demand Capacity Reservation (ODCR). For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-odcr.html">Using ODCRs with PCS</a>. If you don't provide this option, it defaults to On-Demand.</p>
            iam_instance_profile_arn: <p>The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have the <code>pcs:RegisterComputeNodeGroupInstance</code> permission and the role name must start with <code>AWSPCS</code> or must have the path <code>/aws-pcs/</code>. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles.html">IAM instance profiles for PCS</a> in the <i>PCS User Guide</i>.</p>
            scaling_configuration: <p>Specifies the boundaries of the compute node group auto scaling.</p>
            instance_configs: <p>A list of EC2 instance configurations that PCS can provision in the compute node group.</p>
            slurm_configuration: <p>Additional options related to the Slurm scheduler.</p>
            node_lifecycle_actions: <p>The lifecycle actions to run on compute nodes in the compute node group. Use lifecycle actions to run custom scripts at defined stages of a compute node's lifecycle, such as when a compute node finishes bootstrapping or becomes ready to accept jobs.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>
            tags: <p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. To learn how to increase your service quota, see <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i> </p> <p> <u>Examples</u> </p> <ul> <li> <p>The max number of clusters or queues has been reached for the account.</p> </li> <li> <p>The max number of compute node groups has been reached for the associated cluster.</p> </li> <li> <p>The total of <code>maxInstances</code> across all compute node groups has been reached for associated cluster.</p> </li> </ul>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.create_compute_node_group_request.CreateComputeNodeGroupRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.create_compute_node_group_response.CreateComputeNodeGroupResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.create_compute_node_group

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.create_compute_node_group.create_compute_node_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.create_compute_node_group_request.CreateComputeNodeGroupRequest = {
            "cluster_identifier": cluster_identifier,
            "compute_node_group_name": compute_node_group_name,
            "subnet_ids": subnet_ids,
            "custom_launch_template": custom_launch_template,
            "iam_instance_profile_arn": iam_instance_profile_arn,
            "scaling_configuration": scaling_configuration,
            "instance_configs": instance_configs,
        }
        if ami_id is not None:
            input_["ami_id"] = ami_id
        if purchase_option is not None:
            input_["purchase_option"] = purchase_option
        if spot_options is not None:
            input_["spot_options"] = spot_options
        if slurm_configuration is not None:
            input_["slurm_configuration"] = slurm_configuration
        if node_lifecycle_actions is not None:
            input_["node_lifecycle_actions"] = node_lifecycle_actions
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_compute_node_group(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        compute_node_group_identifier: "capo_pcs.types.compute_node_group_identifier.ComputeNodeGroupIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        ami_id: Optional["capo_pcs.types.ami_id.AmiId"] = None,
        subnet_ids: Optional["capo_pcs.types.string_list.StringList"] = None,
        custom_launch_template: Optional[
            "capo_pcs.types.custom_launch_template.CustomLaunchTemplate"
        ] = None,
        purchase_option: Optional[
            "capo_pcs.types.purchase_option.PurchaseOption"
        ] = None,
        spot_options: Optional["capo_pcs.types.spot_options.SpotOptions"] = None,
        scaling_configuration: Optional[
            "capo_pcs.types.scaling_configuration_request.ScalingConfigurationRequest"
        ] = None,
        iam_instance_profile_arn: Optional[
            "capo_pcs.types.instance_profile_arn.InstanceProfileArn"
        ] = None,
        slurm_configuration: Optional[
            "capo_pcs.types.update_compute_node_group_slurm_configuration_request.UpdateComputeNodeGroupSlurmConfigurationRequest"
        ] = None,
        node_lifecycle_actions: Optional[
            "capo_pcs.types.update_node_lifecycle_actions_request.UpdateNodeLifecycleActionsRequest"
        ] = None,
        client_token: Optional["capo_pcs.types.sb_client_token.SBClientToken"] = None,
    ) -> "capo_pcs.types.update_compute_node_group_response.UpdateComputeNodeGroupResponse":
        """<p>Updates a compute node group. You can update many of the fields related to your compute node group including the configurations for networking, compute nodes, and settings specific to your scheduler (such as Slurm).</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster of the compute node group.</p>
            compute_node_group_identifier: <p>The name or ID of the compute node group.</p>
            ami_id: <p>The ID of the Amazon Machine Image (AMI) that PCS uses to launch instances. If not provided, PCS uses the AMI ID specified in the custom launch template.</p>
            subnet_ids: <p>The list of subnet IDs where the compute node group provisions instances. The subnets must be in the same VPC as the cluster.</p>
            purchase_option: <p>Specifies how EC2 instances are purchased on your behalf. PCS supports On-Demand Instances, Spot Instances, Interruptible Capacity Reservations, On-Demand Capacity Reservations, and Amazon EC2 Capacity Blocks for ML. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html">Amazon EC2 billing and purchasing options</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. For more information about PCS support for Capacity Blocks, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks.html">Using Amazon EC2 Capacity Blocks for ML with PCS</a> in the <i>PCS User Guide</i>. For more information about PCS support for interruptible capacity reservations, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-iodcr.html">Using I-ODCRs with PCS</a> in the <i>PCS User Guide</i>. Choose On-Demand if you plan to use an On-Demand Capacity Reservation (ODCR). For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-odcr.html">Using ODCRs with PCS</a>. If you don't provide this option, it defaults to On-Demand.</p>
            scaling_configuration: <p>Specifies the boundaries of the compute node group auto scaling.</p>
            iam_instance_profile_arn: <p>The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have the <code>pcs:RegisterComputeNodeGroupInstance</code> permission and the role name must start with <code>AWSPCS</code> or must have the path <code>/aws-pcs/</code>. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles.html">IAM instance profiles for PCS</a> in the <i>PCS User Guide</i>.</p>
            slurm_configuration: <p>Additional options related to the Slurm scheduler.</p>
            node_lifecycle_actions: <p>The lifecycle actions to run on compute nodes in the compute node group. Use lifecycle actions to run custom scripts at defined stages of a compute node's lifecycle, such as when a compute node finishes bootstrapping or becomes ready to accept jobs.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. To learn how to increase your service quota, see <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i> </p> <p> <u>Examples</u> </p> <ul> <li> <p>The max number of clusters or queues has been reached for the account.</p> </li> <li> <p>The max number of compute node groups has been reached for the associated cluster.</p> </li> <li> <p>The total of <code>maxInstances</code> across all compute node groups has been reached for associated cluster.</p> </li> </ul>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.update_compute_node_group_request.UpdateComputeNodeGroupRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.update_compute_node_group_response.UpdateComputeNodeGroupResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.update_compute_node_group

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.update_compute_node_group.update_compute_node_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.update_compute_node_group_request.UpdateComputeNodeGroupRequest = {
            "cluster_identifier": cluster_identifier,
            "compute_node_group_identifier": compute_node_group_identifier,
        }
        if ami_id is not None:
            input_["ami_id"] = ami_id
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if custom_launch_template is not None:
            input_["custom_launch_template"] = custom_launch_template
        if purchase_option is not None:
            input_["purchase_option"] = purchase_option
        if spot_options is not None:
            input_["spot_options"] = spot_options
        if scaling_configuration is not None:
            input_["scaling_configuration"] = scaling_configuration
        if iam_instance_profile_arn is not None:
            input_["iam_instance_profile_arn"] = iam_instance_profile_arn
        if slurm_configuration is not None:
            input_["slurm_configuration"] = slurm_configuration
        if node_lifecycle_actions is not None:
            input_["node_lifecycle_actions"] = node_lifecycle_actions
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_compute_node_group(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        compute_node_group_identifier: "capo_pcs.types.compute_node_group_identifier.ComputeNodeGroupIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        client_token: Optional["capo_pcs.types.sb_client_token.SBClientToken"] = None,
    ) -> "capo_pcs.types.delete_compute_node_group_response.DeleteComputeNodeGroupResponse":
        """<p>Deletes a compute node group. You must delete all queues associated with the compute node group first.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster of the compute node group.</p>
            compute_node_group_identifier: <p>The name or ID of the compute node group to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.delete_compute_node_group_request.DeleteComputeNodeGroupRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.delete_compute_node_group_response.DeleteComputeNodeGroupResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.delete_compute_node_group

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.delete_compute_node_group.delete_compute_node_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.delete_compute_node_group_request.DeleteComputeNodeGroupRequest = {
            "cluster_identifier": cluster_identifier,
            "compute_node_group_identifier": compute_node_group_identifier,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_compute_node_group(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        compute_node_group_identifier: "capo_pcs.types.compute_node_group_identifier.ComputeNodeGroupIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> "capo_pcs.types.get_compute_node_group_response.GetComputeNodeGroupResponse":
        """<p>Returns detailed information about a compute node group. This API action provides networking information, EC2 instance type, compute node group status, and scheduler (such as Slurm) configuration.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster.</p>
            compute_node_group_identifier: <p>The name or ID of the compute node group.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.get_compute_node_group_request.GetComputeNodeGroupRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.get_compute_node_group_response.GetComputeNodeGroupResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.get_compute_node_group

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.get_compute_node_group.get_compute_node_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.get_compute_node_group_request.GetComputeNodeGroupRequest = {
            "cluster_identifier": cluster_identifier,
            "compute_node_group_identifier": compute_node_group_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_compute_node_groups(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional["capo_pcs.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_pcs.types.list_compute_node_groups_response.ListComputeNodeGroupsResponse"
    ):
        """<p>Returns a list of all compute node groups associated with a cluster.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to list compute node groups for.</p>
            next_token: <p>The value of <code>nextToken</code> is a unique pagination token for each page of results returned. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token returns an <code>HTTP 400 InvalidToken</code> error.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 10 results, and the maximum allowed page size is 100 results. A value of 0 uses the default.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.list_compute_node_groups_request.ListComputeNodeGroupsRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.list_compute_node_groups_response.ListComputeNodeGroupsResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.list_compute_node_groups

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.list_compute_node_groups.list_compute_node_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.list_compute_node_groups_request.ListComputeNodeGroupsRequest = {
            "cluster_identifier": cluster_identifier
        }
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

    def iter_list_compute_node_groups(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional["capo_pcs.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_pcs.types.compute_node_group_summary.ComputeNodeGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_compute_node_groups(
                cluster_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("compute_node_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_queue(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        queue_name: "capo_pcs.types.queue_name.QueueName",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        compute_node_group_configurations: Optional[
            "capo_pcs.types.compute_node_group_configuration_list.ComputeNodeGroupConfigurationList"
        ] = None,
        slurm_configuration: Optional[
            "capo_pcs.types.queue_slurm_configuration_request.QueueSlurmConfigurationRequest"
        ] = None,
        client_token: Optional["capo_pcs.types.sb_client_token.SBClientToken"] = None,
        tags: Optional["capo_pcs.types.request_tag_map.RequestTagMap"] = None,
    ) -> "capo_pcs.types.create_queue_response.CreateQueueResponse":
        """<p>Creates a job queue. You must associate 1 or more compute node groups with the queue. You can associate 1 compute node group with multiple queues.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster for which to create a queue.</p>
            queue_name: <p>A name to identify the queue.</p>
            compute_node_group_configurations: <p>The list of compute node group configurations to associate with the queue. Queues assign jobs to associated compute node groups.</p>
            slurm_configuration: <p>Additional options related to the Slurm scheduler.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>
            tags: <p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. To learn how to increase your service quota, see <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i> </p> <p> <u>Examples</u> </p> <ul> <li> <p>The max number of clusters or queues has been reached for the account.</p> </li> <li> <p>The max number of compute node groups has been reached for the associated cluster.</p> </li> <li> <p>The total of <code>maxInstances</code> across all compute node groups has been reached for associated cluster.</p> </li> </ul>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.create_queue_request.CreateQueueRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.create_queue_response.CreateQueueResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.create_queue

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.create_queue.create_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.create_queue_request.CreateQueueRequest = {
            "cluster_identifier": cluster_identifier,
            "queue_name": queue_name,
        }
        if compute_node_group_configurations is not None:
            input_["compute_node_group_configurations"] = (
                compute_node_group_configurations
            )
        if slurm_configuration is not None:
            input_["slurm_configuration"] = slurm_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_queue(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        queue_identifier: "capo_pcs.types.queue_identifier.QueueIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        compute_node_group_configurations: Optional[
            "capo_pcs.types.compute_node_group_configuration_list.ComputeNodeGroupConfigurationList"
        ] = None,
        slurm_configuration: Optional[
            "capo_pcs.types.update_queue_slurm_configuration_request.UpdateQueueSlurmConfigurationRequest"
        ] = None,
        client_token: Optional["capo_pcs.types.sb_client_token.SBClientToken"] = None,
    ) -> "capo_pcs.types.update_queue_response.UpdateQueueResponse":
        """<p>Updates the compute node group configuration of a queue. Use this API to change the compute node groups that the queue can send jobs to.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster of the queue.</p>
            queue_identifier: <p>The name or ID of the queue.</p>
            compute_node_group_configurations: <p>The list of compute node group configurations to associate with the queue. Queues assign jobs to associated compute node groups.</p>
            slurm_configuration: <p>Additional options related to the Slurm scheduler.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. To learn how to increase your service quota, see <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i> </p> <p> <u>Examples</u> </p> <ul> <li> <p>The max number of clusters or queues has been reached for the account.</p> </li> <li> <p>The max number of compute node groups has been reached for the associated cluster.</p> </li> <li> <p>The total of <code>maxInstances</code> across all compute node groups has been reached for associated cluster.</p> </li> </ul>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.update_queue_request.UpdateQueueRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.update_queue_response.UpdateQueueResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.update_queue

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.update_queue.update_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.update_queue_request.UpdateQueueRequest = {
            "cluster_identifier": cluster_identifier,
            "queue_identifier": queue_identifier,
        }
        if compute_node_group_configurations is not None:
            input_["compute_node_group_configurations"] = (
                compute_node_group_configurations
            )
        if slurm_configuration is not None:
            input_["slurm_configuration"] = slurm_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_queue(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        queue_identifier: "capo_pcs.types.queue_identifier.QueueIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        client_token: Optional["capo_pcs.types.sb_client_token.SBClientToken"] = None,
    ) -> "capo_pcs.types.delete_queue_response.DeleteQueueResponse":
        """<p>Deletes a job queue. If the compute node group associated with this queue isn't associated with any other queues, PCS terminates all the compute nodes for this queue.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster of the queue.</p>
            queue_identifier: <p>The name or ID of the queue to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.delete_queue_request.DeleteQueueRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.delete_queue_response.DeleteQueueResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.delete_queue

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.delete_queue.delete_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.delete_queue_request.DeleteQueueRequest = {
            "cluster_identifier": cluster_identifier,
            "queue_identifier": queue_identifier,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_queue(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        queue_identifier: "capo_pcs.types.queue_identifier.QueueIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> "capo_pcs.types.get_queue_response.GetQueueResponse":
        """<p>Returns detailed information about a queue. The information includes the compute node groups that the queue uses to schedule jobs.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster of the queue.</p>
            queue_identifier: <p>The name or ID of the queue.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.get_queue_request.GetQueueRequest]",
        ) -> OperationResponse["capo_pcs.types.get_queue_response.GetQueueResponse"]:
            import capo_pcs._operations.aws_parallel_computing_service.get_queue

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.get_queue.get_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.get_queue_request.GetQueueRequest = {
            "cluster_identifier": cluster_identifier,
            "queue_identifier": queue_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_queues(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional["capo_pcs.types.max_results.MaxResults"] = None,
    ) -> "capo_pcs.types.list_queues_response.ListQueuesResponse":
        """<p>Returns a list of all queues associated with a cluster.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to list queues for.</p>
            next_token: <p>The value of <code>nextToken</code> is a unique pagination token for each page of results returned. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token returns an <code>HTTP 400 InvalidToken</code> error.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 10 results, and the maximum allowed page size is 100 results. A value of 0 uses the default.</p>

        Raises:
            capo_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            capo_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            capo_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            capo_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            capo_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            capo_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            capo_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pcs.types.list_queues_request.ListQueuesRequest]",
        ) -> OperationResponse[
            "capo_pcs.types.list_queues_response.ListQueuesResponse"
        ]:
            import capo_pcs._operations.aws_parallel_computing_service.list_queues

            output, http_response = (
                capo_pcs._operations.aws_parallel_computing_service.list_queues.list_queues(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pcs.types.list_queues_request.ListQueuesRequest = {
            "cluster_identifier": cluster_identifier
        }
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

    def iter_list_queues(
        self,
        cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional["capo_pcs.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_pcs.types.queue_summary.QueueSummary]":
        _token = next_token
        while True:
            _response = self.list_queues(
                cluster_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("queues",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
