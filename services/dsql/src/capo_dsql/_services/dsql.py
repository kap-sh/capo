"""Generated from Smithy shape ``com.amazonaws.dsql#DSQL``."""

import time
import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_dsql._auth._signers
import capo_dsql._auth._sigv4
from capo_dsql._auth._identity import Credentials
from capo_dsql._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_dsql._auth._zapros_handler import AuthMiddleware
from capo_dsql._pagination import resolve_path as _resolve_path
from capo_dsql._resources.dsql.cluster import Cluster
from capo_dsql._resources.dsql.stream import Stream
from capo_dsql._services._aws_config import aws_config
from capo_dsql._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)
from capo_dsql.errors import ServiceError, WaiterTimeoutError

if TYPE_CHECKING:
    import capo_dsql.types.arn
    import capo_dsql.types.bypass_policy_lockout_safety_check
    import capo_dsql.types.client_token
    import capo_dsql.types.cluster_id
    import capo_dsql.types.cluster_summary
    import capo_dsql.types.create_cluster_input
    import capo_dsql.types.create_cluster_output
    import capo_dsql.types.create_stream_input
    import capo_dsql.types.create_stream_output
    import capo_dsql.types.delete_cluster_input
    import capo_dsql.types.delete_cluster_output
    import capo_dsql.types.delete_cluster_policy_input
    import capo_dsql.types.delete_cluster_policy_output
    import capo_dsql.types.delete_stream_input
    import capo_dsql.types.delete_stream_output
    import capo_dsql.types.deletion_protection_enabled
    import capo_dsql.types.get_cluster_input
    import capo_dsql.types.get_cluster_output
    import capo_dsql.types.get_cluster_policy_input
    import capo_dsql.types.get_cluster_policy_output
    import capo_dsql.types.get_stream_input
    import capo_dsql.types.get_stream_output
    import capo_dsql.types.get_vpc_endpoint_service_name_input
    import capo_dsql.types.get_vpc_endpoint_service_name_output
    import capo_dsql.types.kms_encryption_key
    import capo_dsql.types.list_clusters_input
    import capo_dsql.types.list_clusters_output
    import capo_dsql.types.list_streams_input
    import capo_dsql.types.list_streams_output
    import capo_dsql.types.list_tags_for_resource_input
    import capo_dsql.types.list_tags_for_resource_output
    import capo_dsql.types.max_results
    import capo_dsql.types.multi_region_properties
    import capo_dsql.types.next_token
    import capo_dsql.types.policy_document
    import capo_dsql.types.policy_version
    import capo_dsql.types.put_cluster_policy_input
    import capo_dsql.types.put_cluster_policy_output
    import capo_dsql.types.stream_format
    import capo_dsql.types.stream_id
    import capo_dsql.types.stream_ordering
    import capo_dsql.types.stream_summary
    import capo_dsql.types.tag_key_list
    import capo_dsql.types.tag_map
    import capo_dsql.types.tag_resource_input
    import capo_dsql.types.target_definition
    import capo_dsql.types.untag_resource_input
    import capo_dsql.types.update_cluster_input
    import capo_dsql.types.update_cluster_output


class DSQLClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class DSQLClient:
    """A client for the ``DSQL`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = DSQLClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.cluster = Cluster(self)
        self.stream = Stream(self)

    def operation_options(
        self, config_overrides: Optional[DSQLClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DSQLClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_dsql.types.arn.Arn",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> "capo_dsql.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists all of the tags for a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which you want to list the tags.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List Tags For Resource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:dsql:us-east-1:111111222222:cluster/kiqenqglxyl2snyvkvnj2c3s2e')
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_dsql.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_dsql._operations.dsql.list_tags_for_resource

            output, http_response = (
                capo_dsql._operations.dsql.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.list_tags_for_resource_input.ListTagsForResourceInput = {
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
        resource_arn: "capo_dsql.types.arn.Arn",
        tags: "capo_dsql.types.tag_map.TagMap",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> None:
        """<p>Tags a resource with a map of key and value pairs.</p>

        Args:
            resource_arn: <p>The ARN of the resource that you want to tag.</p>
            tags: <p>A map of key and value pairs to use to tag your resource.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Tag Resource

            >>> client.tag_resource(resource_arn='arn:aws:dsql:us-east-1:111111222222:cluster/kiqenqglxyl2snyvkvnj2c3s2e', tags={'MyKey': 'MyValue'})
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[None]:
            import capo_dsql._operations.dsql.tag_resource

            output, http_response = (
                capo_dsql._operations.dsql.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_dsql.types.arn.Arn",
        tag_keys: "capo_dsql.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> None:
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource from which to remove tags.</p>
            tag_keys: <p>The array of keys of the tags that you want to remove.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Untag Resource

            >>> client.untag_resource(resource_arn='arn:aws:dsql:us-east-1:111111222222:cluster/kiqenqglxyl2snyvkvnj2c3s2e', tag_keys=['MyKeyA', 'MyKeyB'])
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[None]:
            import capo_dsql._operations.dsql.untag_resource

            output, http_response = (
                capo_dsql._operations.dsql.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.untag_resource_input.UntagResourceInput = {
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
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        deletion_protection_enabled: Optional[
            "capo_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
        ] = None,
        kms_encryption_key: Optional[
            "capo_dsql.types.kms_encryption_key.KmsEncryptionKey"
        ] = None,
        tags: Optional["capo_dsql.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_dsql.types.client_token.ClientToken"] = None,
        multi_region_properties: Optional[
            "capo_dsql.types.multi_region_properties.MultiRegionProperties"
        ] = None,
        policy: Optional["capo_dsql.types.policy_document.PolicyDocument"] = None,
        bypass_policy_lockout_safety_check: Optional[
            "capo_dsql.types.bypass_policy_lockout_safety_check.BypassPolicyLockoutSafetyCheck"
        ] = None,
    ) -> "capo_dsql.types.create_cluster_output.CreateClusterOutput":
        """<p>The CreateCluster API allows you to create both single-Region clusters and multi-Region clusters. With the addition of the <i>multiRegionProperties</i> parameter, you can create a cluster with witness Region support and establish peer relationships with clusters in other Regions during creation.</p> <note> <p>Creating multi-Region clusters requires additional IAM permissions beyond those needed for single-Region clusters, as detailed in the <b>Required permissions</b> section below.</p> </note> <p> <b>Required permissions</b> </p> <dl> <dt>dsql:CreateCluster</dt> <dd> <p>Required to create a cluster.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </dd> <dt>dsql:TagResource</dt> <dd> <p>Permission to add tags to a resource.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </dd> <dt>dsql:PutMultiRegionProperties</dt> <dd> <p>Permission to configure multi-Region properties for a cluster.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </dd> <dt>dsql:AddPeerCluster</dt> <dd> <p>When specifying <code>multiRegionProperties.clusters</code>, permission to add peer clusters.</p> <p>Resources:</p> <ul> <li> <p>Local cluster: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> </li> <li> <p>Each peer cluster: exact ARN of each specified peer cluster</p> </li> </ul> </dd> <dt>dsql:PutWitnessRegion</dt> <dd> <p>When specifying <code>multiRegionProperties.witnessRegion</code>, permission to set a witness Region. This permission is checked both in the cluster Region and in the witness Region.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/*</code> </p> <p>Condition Keys: <code>dsql:WitnessRegion</code> (matching the specified witness region)</p> </dd> </dl> <important> <ul> <li> <p>The witness Region specified in <code>multiRegionProperties.witnessRegion</code> cannot be the same as the cluster's Region.</p> </li> </ul> </important>

        Args:
            deletion_protection_enabled: <p>If enabled, you can't delete your cluster. You must first disable this property before you can delete your cluster.</p>
            kms_encryption_key: <p>The KMS key that encrypts and protects the data on your cluster. You can specify the ARN, ID, or alias of an existing key or have Amazon Web Services create a default key for you.</p>
            tags: <p>A map of key and value pairs to use to tag your cluster.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>
            multi_region_properties: <p>The configuration settings when creating a multi-Region cluster, including the witness region and linked cluster properties.</p>
            policy: <p>An optional resource-based policy document in JSON format that defines access permissions for the cluster.</p>
            bypass_policy_lockout_safety_check: <p>An optional field that controls whether to bypass the lockout prevention check. When set to true, this parameter allows you to apply a policy that might lock you out of the cluster. Use with caution.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_dsql.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create Cluster

            >>> client.create_cluster(deletion_protection_enabled=False, tags={'MyKey': 'MyValue'})
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.create_cluster_input.CreateClusterInput]",
        ) -> OperationResponse[
            "capo_dsql.types.create_cluster_output.CreateClusterOutput"
        ]:
            import capo_dsql._operations.dsql.create_cluster

            output, http_response = (
                capo_dsql._operations.dsql.create_cluster.create_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.create_cluster_input.CreateClusterInput = {}
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if kms_encryption_key is not None:
            input_["kms_encryption_key"] = kms_encryption_key
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if multi_region_properties is not None:
            input_["multi_region_properties"] = multi_region_properties
        if policy is not None:
            input_["policy"] = policy
        if bypass_policy_lockout_safety_check is not None:
            input_["bypass_policy_lockout_safety_check"] = (
                bypass_policy_lockout_safety_check
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cluster(
        self,
        identifier: "capo_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> "capo_dsql.types.get_cluster_output.GetClusterOutput":
        """<p>Retrieves information about a cluster.</p>

        Args:
            identifier: <p>The ID of the cluster to retrieve.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get Cluster

            >>> client.get_cluster(identifier='kiqenqglxyl2snyvkvnj2c3s2e')
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.get_cluster_input.GetClusterInput]",
        ) -> OperationResponse["capo_dsql.types.get_cluster_output.GetClusterOutput"]:
            import capo_dsql._operations.dsql.get_cluster

            output, http_response = capo_dsql._operations.dsql.get_cluster.get_cluster(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.get_cluster_input.GetClusterInput = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def wait_until_cluster_not_exists(
        self,
        identifier: "capo_dsql.types.cluster_id.ClusterId",
        *,
        max_wait_time: float,
        min_delay: float = 2,
        max_delay: float = 120,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> ServiceError:
        """Wait until a Cluster is gone

        Args:
            identifier: <p>The ID of the cluster to retrieve.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_dsql.types.get_cluster_output.GetClusterOutput | None" = (
                None
            )
            op_error: ServiceError | None = None
            try:
                op_output = self.get_cluster(  # noqa: F841
                    identifier, config_overrides=config_overrides
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("cluster_not_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            time.sleep(delay)
            attempt += 1

    def update_cluster(
        self,
        identifier: "capo_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        deletion_protection_enabled: Optional[
            "capo_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
        ] = None,
        kms_encryption_key: Optional[
            "capo_dsql.types.kms_encryption_key.KmsEncryptionKey"
        ] = None,
        client_token: Optional["capo_dsql.types.client_token.ClientToken"] = None,
        multi_region_properties: Optional[
            "capo_dsql.types.multi_region_properties.MultiRegionProperties"
        ] = None,
    ) -> "capo_dsql.types.update_cluster_output.UpdateClusterOutput":
        """<p>The <i>UpdateCluster</i> API allows you to modify both single-Region and multi-Region cluster configurations. With the <i>multiRegionProperties</i> parameter, you can add or modify witness Region support and manage peer relationships with clusters in other Regions.</p> <note> <p>Note that updating multi-Region clusters requires additional IAM permissions beyond those needed for standard cluster updates, as detailed in the Permissions section.</p> </note> <p> <b>Required permissions</b> </p> <dl> <dt>dsql:UpdateCluster</dt> <dd> <p>Permission to update a DSQL cluster.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </dd> </dl> <dl> <dt>dsql:PutMultiRegionProperties</dt> <dd> <p>Permission to configure multi-Region properties for a cluster.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </dd> </dl> <dl> <dt>dsql:GetCluster</dt> <dd> <p>Permission to retrieve cluster information.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </dd> <dt>dsql:AddPeerCluster</dt> <dd> <p>Permission to add peer clusters.</p> <p>Resources:</p> <ul> <li> <p>Local cluster: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> </li> <li> <p>Each peer cluster: exact ARN of each specified peer cluster</p> </li> </ul> </dd> <dt>dsql:RemovePeerCluster</dt> <dd> <p>Permission to remove peer clusters. The <i>dsql:RemovePeerCluster</i> permission uses a wildcard ARN pattern to simplify permission management during updates.</p> <p>Resources: <code>arn:aws:dsql:*:<i>account-id</i>:cluster/*</code> </p> </dd> </dl> <dl> <dt>dsql:PutWitnessRegion</dt> <dd> <p>Permission to set a witness Region.</p> <p>Resources: <code>arn:aws:dsql:<i>region</i>:<i>account-id</i>:cluster/<i>cluster-id</i> </code> </p> <p>Condition Keys: dsql:WitnessRegion (matching the specified witness Region)</p> <p> <b>This permission is checked both in the cluster Region and in the witness Region.</b> </p> </dd> </dl> <important> <ul> <li> <p>The witness region specified in <code>multiRegionProperties.witnessRegion</code> cannot be the same as the cluster's Region.</p> </li> <li> <p>When updating clusters with peer relationships, permissions are checked for both adding and removing peers.</p> </li> <li> <p>The <code>dsql:RemovePeerCluster</code> permission uses a wildcard ARN pattern to simplify permission management during updates.</p> </li> </ul> </important>

        Args:
            identifier: <p>The ID of the cluster you want to update.</p>
            deletion_protection_enabled: <p>Specifies whether to enable deletion protection in your cluster.</p>
            kms_encryption_key: <p>The KMS key that encrypts and protects the data on your cluster. You can specify the ARN, ID, or alias of an existing key or have Amazon Web Services create a default key for you.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully. The subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>
            multi_region_properties: <p>The new multi-Region cluster configuration settings to be applied during an update operation.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update Cluster

            >>> client.update_cluster(identifier='kiqenqglxyl2snyvkvnj2c3s2e', deletion_protection_enabled=False)
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.update_cluster_input.UpdateClusterInput]",
        ) -> OperationResponse[
            "capo_dsql.types.update_cluster_output.UpdateClusterOutput"
        ]:
            import capo_dsql._operations.dsql.update_cluster

            output, http_response = (
                capo_dsql._operations.dsql.update_cluster.update_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.update_cluster_input.UpdateClusterInput = {
            "identifier": identifier
        }
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if kms_encryption_key is not None:
            input_["kms_encryption_key"] = kms_encryption_key
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if multi_region_properties is not None:
            input_["multi_region_properties"] = multi_region_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cluster(
        self,
        identifier: "capo_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        client_token: Optional["capo_dsql.types.client_token.ClientToken"] = None,
    ) -> "capo_dsql.types.delete_cluster_output.DeleteClusterOutput":
        """<p>Deletes a cluster in Amazon Aurora DSQL.</p>

        Args:
            identifier: <p>The ID of the cluster to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully. The subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete Cluster

            >>> client.delete_cluster(identifier='kiqenqglxyl2snyvkvnj2c3s2e')
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.delete_cluster_input.DeleteClusterInput]",
        ) -> OperationResponse[
            "capo_dsql.types.delete_cluster_output.DeleteClusterOutput"
        ]:
            import capo_dsql._operations.dsql.delete_cluster

            output, http_response = (
                capo_dsql._operations.dsql.delete_cluster.delete_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.delete_cluster_input.DeleteClusterInput = {
            "identifier": identifier
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

    def list_clusters(
        self,
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        max_results: Optional["capo_dsql.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dsql.types.next_token.NextToken"] = None,
    ) -> "capo_dsql.types.list_clusters_output.ListClustersOutput":
        """<p>Retrieves information about a list of clusters.</p>

        Args:
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>
            next_token: <p>If your initial ListClusters operation returns a nextToken, you can include the returned nextToken in following ListClusters operations, which returns results in the next page.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List Clusters

            >>> client.list_clusters(max_results=20)
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.list_clusters_input.ListClustersInput]",
        ) -> OperationResponse[
            "capo_dsql.types.list_clusters_output.ListClustersOutput"
        ]:
            import capo_dsql._operations.dsql.list_clusters

            output, http_response = (
                capo_dsql._operations.dsql.list_clusters.list_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.list_clusters_input.ListClustersInput = {}
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

    def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        max_results: Optional["capo_dsql.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dsql.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_dsql.types.cluster_summary.ClusterSummary]":
        _token = next_token
        while True:
            _response = self.list_clusters(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def delete_cluster_policy(
        self,
        identifier: "capo_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        expected_policy_version: Optional[
            "capo_dsql.types.policy_version.PolicyVersion"
        ] = None,
        client_token: Optional["capo_dsql.types.client_token.ClientToken"] = None,
    ) -> "capo_dsql.types.delete_cluster_policy_output.DeleteClusterPolicyOutput":
        """<p>Deletes the resource-based policy attached to a cluster. This removes all access permissions defined by the policy, reverting to default access controls.</p>

        Args:
            expected_policy_version: <p>The expected version of the policy to delete. This parameter ensures that you're deleting the correct version of the policy and helps prevent accidental deletions.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.delete_cluster_policy_input.DeleteClusterPolicyInput]",
        ) -> OperationResponse[
            "capo_dsql.types.delete_cluster_policy_output.DeleteClusterPolicyOutput"
        ]:
            import capo_dsql._operations.dsql.delete_cluster_policy

            output, http_response = (
                capo_dsql._operations.dsql.delete_cluster_policy.delete_cluster_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.delete_cluster_policy_input.DeleteClusterPolicyInput = {
            "identifier": identifier
        }
        if expected_policy_version is not None:
            input_["expected_policy_version"] = expected_policy_version
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

    def get_cluster_policy(
        self,
        identifier: "capo_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> "capo_dsql.types.get_cluster_policy_output.GetClusterPolicyOutput":
        """<p>Retrieves the resource-based policy document attached to a cluster. This policy defines the access permissions and conditions for the cluster.</p>

        Args:
            identifier: <p>The ID of the cluster to retrieve the policy from.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.get_cluster_policy_input.GetClusterPolicyInput]",
        ) -> OperationResponse[
            "capo_dsql.types.get_cluster_policy_output.GetClusterPolicyOutput"
        ]:
            import capo_dsql._operations.dsql.get_cluster_policy

            output, http_response = (
                capo_dsql._operations.dsql.get_cluster_policy.get_cluster_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.get_cluster_policy_input.GetClusterPolicyInput = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_vpc_endpoint_service_name(
        self,
        identifier: "capo_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> "capo_dsql.types.get_vpc_endpoint_service_name_output.GetVpcEndpointServiceNameOutput":
        """<p>Retrieves the VPC endpoint service name.</p>

        Args:
            identifier: <p>The ID of the cluster to retrieve.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get VPC Endpoint Service Name

            >>> client.get_vpc_endpoint_service_name(identifier='kiqenqglxyl2snyvkvnj2c3s2e')
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.get_vpc_endpoint_service_name_input.GetVpcEndpointServiceNameInput]",
        ) -> OperationResponse[
            "capo_dsql.types.get_vpc_endpoint_service_name_output.GetVpcEndpointServiceNameOutput"
        ]:
            import capo_dsql._operations.dsql.get_vpc_endpoint_service_name

            output, http_response = (
                capo_dsql._operations.dsql.get_vpc_endpoint_service_name.get_vpc_endpoint_service_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.get_vpc_endpoint_service_name_input.GetVpcEndpointServiceNameInput = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_cluster_policy(
        self,
        identifier: "capo_dsql.types.cluster_id.ClusterId",
        policy: "capo_dsql.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        bypass_policy_lockout_safety_check: Optional[
            "capo_dsql.types.bypass_policy_lockout_safety_check.BypassPolicyLockoutSafetyCheck"
        ] = None,
        expected_policy_version: Optional[
            "capo_dsql.types.policy_version.PolicyVersion"
        ] = None,
        client_token: Optional["capo_dsql.types.client_token.ClientToken"] = None,
    ) -> "capo_dsql.types.put_cluster_policy_output.PutClusterPolicyOutput":
        """<p>Attaches a resource-based policy to a cluster. This policy defines access permissions and conditions for the cluster, allowing you to control which principals can perform actions on the cluster.</p>

        Args:
            policy: <p>The resource-based policy document to attach to the cluster. This should be a valid JSON policy document that defines permissions and conditions.</p>
            bypass_policy_lockout_safety_check: <p>A flag that allows you to bypass the policy lockout safety check. When set to true, this parameter allows you to apply a policy that might lock you out of the cluster. Use with caution.</p>
            expected_policy_version: <p>The expected version of the current policy. This parameter ensures that you're updating the correct version of the policy and helps prevent concurrent modification conflicts.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.put_cluster_policy_input.PutClusterPolicyInput]",
        ) -> OperationResponse[
            "capo_dsql.types.put_cluster_policy_output.PutClusterPolicyOutput"
        ]:
            import capo_dsql._operations.dsql.put_cluster_policy

            output, http_response = (
                capo_dsql._operations.dsql.put_cluster_policy.put_cluster_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.put_cluster_policy_input.PutClusterPolicyInput = {
            "identifier": identifier,
            "policy": policy,
        }
        if bypass_policy_lockout_safety_check is not None:
            input_["bypass_policy_lockout_safety_check"] = (
                bypass_policy_lockout_safety_check
            )
        if expected_policy_version is not None:
            input_["expected_policy_version"] = expected_policy_version
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

    def create_stream(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        target_definition: "capo_dsql.types.target_definition.TargetDefinition",
        ordering: "capo_dsql.types.stream_ordering.StreamOrdering",
        format: "capo_dsql.types.stream_format.StreamFormat",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        tags: Optional["capo_dsql.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_dsql.types.client_token.ClientToken"] = None,
    ) -> "capo_dsql.types.create_stream_output.CreateStreamOutput":
        """<p>Creates a new change data capture (CDC) stream for a cluster. The stream captures database changes and delivers them to the specified target destination.</p> <p> <b>Required permissions</b> </p> <dl> <dt>dsql:CreateStream</dt> <dd> <p>Permission to create a new stream.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/cluster-id</code> </p> </dd> <dt>iam:PassRole</dt> <dd> <p>Permission to pass the IAM role specified in the target definition to the service.</p> <p>Resources: ARN of the IAM role specified in <code>targetDefinition.kinesis.roleArn</code> </p> </dd> <dt>kms:Decrypt</dt> <dd> <p>Required when the cluster uses a customer managed KMS key (CMK). Permission to decrypt data using the cluster's CMK.</p> <p>Resources: ARN of the KMS key used by the cluster</p> </dd> </dl>

        Args:
            cluster_identifier: <p>The ID of the cluster for which to create the stream.</p>
            target_definition: <p>The target destination configuration for the stream. Contains Kinesis stream configuration including stream ARN and IAM role ARN.</p>
            ordering: <p>The ordering mode for the stream. Determines how change events are ordered when delivered to the target.</p>
            format: <p>The format of the stream records.</p>
            tags: <p>A map of key and value pairs to use to tag your stream.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.create_stream_input.CreateStreamInput]",
        ) -> OperationResponse[
            "capo_dsql.types.create_stream_output.CreateStreamOutput"
        ]:
            import capo_dsql._operations.dsql.create_stream

            output, http_response = (
                capo_dsql._operations.dsql.create_stream.create_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.create_stream_input.CreateStreamInput = {
            "cluster_identifier": cluster_identifier,
            "target_definition": target_definition,
            "ordering": ordering,
            "format": format,
        }
        if tags is not None:
            input_["tags"] = tags
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

    def get_stream(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        stream_identifier: "capo_dsql.types.stream_id.StreamId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> "capo_dsql.types.get_stream_output.GetStreamOutput":
        """<p>Retrieves information about a stream.</p>

        Args:
            cluster_identifier: <p>The ID of the cluster containing the stream to retrieve.</p>
            stream_identifier: <p>The ID of the stream to retrieve.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.get_stream_input.GetStreamInput]",
        ) -> OperationResponse["capo_dsql.types.get_stream_output.GetStreamOutput"]:
            import capo_dsql._operations.dsql.get_stream

            output, http_response = capo_dsql._operations.dsql.get_stream.get_stream(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.get_stream_input.GetStreamInput = {
            "cluster_identifier": cluster_identifier,
            "stream_identifier": stream_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def wait_until_stream_not_exists(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        stream_identifier: "capo_dsql.types.stream_id.StreamId",
        *,
        max_wait_time: float,
        min_delay: float = 2,
        max_delay: float = 120,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> ServiceError:
        """Wait until a Stream is gone

        Args:
            cluster_identifier: <p>The ID of the cluster containing the stream to retrieve.</p>
            stream_identifier: <p>The ID of the stream to retrieve.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_dsql.types.get_stream_output.GetStreamOutput | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = self.get_stream(  # noqa: F841
                    cluster_identifier,
                    stream_identifier,
                    config_overrides=config_overrides,
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("stream_not_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            time.sleep(delay)
            attempt += 1

    def delete_stream(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        stream_identifier: "capo_dsql.types.stream_id.StreamId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        client_token: Optional["capo_dsql.types.client_token.ClientToken"] = None,
    ) -> "capo_dsql.types.delete_stream_output.DeleteStreamOutput":
        """<p>Deletes a stream from a cluster.</p>

        Args:
            cluster_identifier: <p>The ID of the cluster containing the stream to delete.</p>
            stream_identifier: <p>The ID of the stream to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.delete_stream_input.DeleteStreamInput]",
        ) -> OperationResponse[
            "capo_dsql.types.delete_stream_output.DeleteStreamOutput"
        ]:
            import capo_dsql._operations.dsql.delete_stream

            output, http_response = (
                capo_dsql._operations.dsql.delete_stream.delete_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.delete_stream_input.DeleteStreamInput = {
            "cluster_identifier": cluster_identifier,
            "stream_identifier": stream_identifier,
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

    def list_streams(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        max_results: Optional["capo_dsql.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dsql.types.next_token.NextToken"] = None,
    ) -> "capo_dsql.types.list_streams_output.ListStreamsOutput":
        """<p>Retrieves information about a list of streams for a cluster.</p>

        Args:
            cluster_identifier: <p>The ID of the cluster for which to list streams.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results. Default: 10.</p>
            next_token: <p>If your initial ListStreams operation returns a nextToken, you can include the returned nextToken in following ListStreams operations, which returns results in the next page.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.list_streams_input.ListStreamsInput]",
        ) -> OperationResponse["capo_dsql.types.list_streams_output.ListStreamsOutput"]:
            import capo_dsql._operations.dsql.list_streams

            output, http_response = (
                capo_dsql._operations.dsql.list_streams.list_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dsql.types.list_streams_input.ListStreamsInput = {
            "cluster_identifier": cluster_identifier
        }
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

    def iter_list_streams(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        max_results: Optional["capo_dsql.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dsql.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_dsql.types.stream_summary.StreamSummary]":
        _token = next_token
        while True:
            _response = self.list_streams(
                cluster_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("streams",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
