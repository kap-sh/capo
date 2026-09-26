"""Generated from Smithy shape ``com.amazonaws.interconnect#Interconnect``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_interconnect._auth._signers
import capo_interconnect._auth._sigv4
from capo_interconnect._auth._identity import Credentials
from capo_interconnect._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_interconnect._auth._zapros_handler import AuthMiddleware
from capo_interconnect._pagination import resolve_path as _resolve_path
from capo_interconnect._resources.interconnect.connection_resource import (
    AsyncConnectionResource,
)
from capo_interconnect._resources.interconnect.environment_resource import (
    AsyncEnvironmentResource,
)
from capo_interconnect._services._aws_config import aaws_config
from capo_interconnect._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_interconnect.types.accept_connection_proposal_request
    import capo_interconnect.types.accept_connection_proposal_response
    import capo_interconnect.types.activation_key
    import capo_interconnect.types.amazon_resource_name
    import capo_interconnect.types.attach_point
    import capo_interconnect.types.attach_point_descriptor
    import capo_interconnect.types.connection_bandwidth
    import capo_interconnect.types.connection_description
    import capo_interconnect.types.connection_id
    import capo_interconnect.types.connection_state
    import capo_interconnect.types.connection_summary
    import capo_interconnect.types.create_connection_request
    import capo_interconnect.types.create_connection_response
    import capo_interconnect.types.delete_connection_request
    import capo_interconnect.types.delete_connection_response
    import capo_interconnect.types.describe_connection_proposal_request
    import capo_interconnect.types.describe_connection_proposal_response
    import capo_interconnect.types.environment
    import capo_interconnect.types.environment_id
    import capo_interconnect.types.get_connection_request
    import capo_interconnect.types.get_connection_response
    import capo_interconnect.types.get_environment_request
    import capo_interconnect.types.get_environment_response
    import capo_interconnect.types.list_attach_points_request
    import capo_interconnect.types.list_attach_points_response
    import capo_interconnect.types.list_connections_request
    import capo_interconnect.types.list_connections_response
    import capo_interconnect.types.list_environments_request
    import capo_interconnect.types.list_environments_response
    import capo_interconnect.types.list_tags_for_resource_request
    import capo_interconnect.types.list_tags_for_resource_response
    import capo_interconnect.types.location
    import capo_interconnect.types.max_results
    import capo_interconnect.types.next_token
    import capo_interconnect.types.provider
    import capo_interconnect.types.remote_account_identifier
    import capo_interconnect.types.tag_key_list
    import capo_interconnect.types.tag_map
    import capo_interconnect.types.tag_resource_request
    import capo_interconnect.types.tag_resource_response
    import capo_interconnect.types.untag_resource_request
    import capo_interconnect.types.untag_resource_response
    import capo_interconnect.types.update_connection_request
    import capo_interconnect.types.update_connection_response


class AsyncInterconnectClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncInterconnectClient:
    """A client for the ``Interconnect`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncInterconnectClientConfig(
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
        self.connection_resource = AsyncConnectionResource(self)
        self.environment_resource = AsyncEnvironmentResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncInterconnectClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncInterconnectClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def accept_connection_proposal(
        self,
        attach_point: "capo_interconnect.types.attach_point.AttachPoint",
        activation_key: "capo_interconnect.types.activation_key.ActivationKey",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        description: Optional[
            "capo_interconnect.types.connection_description.ConnectionDescription"
        ] = None,
        tags: Optional["capo_interconnect.types.tag_map.TagMap"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_interconnect.types.accept_connection_proposal_response.AcceptConnectionProposalResponse":
        """<p>Accepts a connection proposal which was generated at a supported partner's portal.</p> <p>The proposal contains the Environment and bandwidth that were chosen on the partner's portal and cannot be modified.</p> <p>Upon accepting the proposal a connection will be made between the AWS network as accessed via the selected Attach Point and the network previously selected network on the partner's portal.</p>

        Args:
            attach_point: <p>The Attach Point to which the connection should be associated.</p>
            activation_key: <p>An Activation Key that was generated on a supported partner's portal. This key captures the desired parameters from the initial creation request.</p> <p>The details of this request can be described using with <a>DescribeConnectionProposal</a>. </p>
            description: <p>A description to distinguish this <a>Connection</a>.</p>
            tags: <p>The tags to associate with the resulting <a>Connection</a>.</p>
            client_token: <p>Idempotency token used for the request.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Accept Connection Proposal

            >>> await client.accept_connection_proposal(activation_key='<Activation Key Data>', attach_point={'directConnectGateway': '90392BE3-219C-47FD-BBA5-03DF76D2542A'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.accept_connection_proposal_request.AcceptConnectionProposalRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.accept_connection_proposal_response.AcceptConnectionProposalResponse"
        ]:
            import capo_interconnect._operations.interconnect.accept_connection_proposal

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.accept_connection_proposal.async_accept_connection_proposal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.accept_connection_proposal_request.AcceptConnectionProposalRequest = {
            "attach_point": attach_point,
            "activation_key": activation_key,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_connection_proposal(
        self,
        activation_key: "capo_interconnect.types.activation_key.ActivationKey",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
    ) -> "capo_interconnect.types.describe_connection_proposal_response.DescribeConnectionProposalResponse":
        """<p>Describes the details of a connection proposal generated at a partner's portal.</p>

        Args:
            activation_key: <p>An Activation Key that was generated on a supported partner's portal. This key captures the desired parameters from the initial creation request.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe Connection Proposal

            >>> await client.describe_connection_proposal(activation_key='<Activation Key Data>')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.describe_connection_proposal_request.DescribeConnectionProposalRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.describe_connection_proposal_response.DescribeConnectionProposalResponse"
        ]:
            import capo_interconnect._operations.interconnect.describe_connection_proposal

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.describe_connection_proposal.async_describe_connection_proposal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.describe_connection_proposal_request.DescribeConnectionProposalRequest = {
            "activation_key": activation_key
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_attach_points(
        self,
        environment_id: "capo_interconnect.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        max_results: Optional["capo_interconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_interconnect.types.next_token.NextToken"] = None,
    ) -> "capo_interconnect.types.list_attach_points_response.ListAttachPointsResponse":
        """<p>Lists all Attach Points the caller has access to that are valid for the specified <a>Environment</a>.</p>

        Args:
            environment_id: <p>The identifier of the <a>Environment</a> for which to list valid Attach Points.</p>
            max_results: <p>The max number of list results in a single paginated response.</p>
            next_token: <p>A pagination token from a previous paginated response indicating you wish to get the next page.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List Attach Points

            >>> await client.list_attach_points(environment_id='mce-aws-acme-1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.list_attach_points_request.ListAttachPointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.list_attach_points_response.ListAttachPointsResponse"
        ]:
            import capo_interconnect._operations.interconnect.list_attach_points

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.list_attach_points.async_list_attach_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.list_attach_points_request.ListAttachPointsRequest = {
            "environment_id": environment_id
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

    async def iter_list_attach_points(
        self,
        environment_id: "capo_interconnect.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        max_results: Optional["capo_interconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_interconnect.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_interconnect.types.attach_point_descriptor.AttachPointDescriptor]":
        _token = next_token
        while True:
            _response = await self.list_attach_points(
                environment_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("attach_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        arn: "capo_interconnect.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
    ) -> "capo_interconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all current tags on the specified resource. Currently this supports <a>Connection</a> resources. </p>

        Args:
            arn: <p>The resource ARN for which to list tags. </p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List Tags

            >>> await client.list_tags_for_resource(arn='arn:aws:interconnect:us-east-1:000000000000:connection/mcc-abc12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_interconnect._operations.interconnect.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
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
        arn: "capo_interconnect.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_interconnect.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
    ) -> "capo_interconnect.types.tag_resource_response.TagResourceResponse":
        """<p>Add new tags to the specified resource.</p>

        Args:
            arn: <p>The ARN of the resource that should receive the new tags.</p>
            tags: <p>A map of tags to apply to the specified resource.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Apply Tags

            >>> await client.tag_resource(arn='arn:aws:interconnect:us-east-1:000000000000:connection/mcc-abc12345', tags={'TagKey1': 'TagValue1', 'TagKey2': 'TagValue2'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_interconnect._operations.interconnect.tag_resource

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.tag_resource_request.TagResourceRequest = {
            "arn": arn,
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
        arn: "capo_interconnect.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_interconnect.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
    ) -> "capo_interconnect.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the specified resource.</p>

        Args:
            arn: <p>The ARN of the resource from which the specified tags should be removed.</p>
            tag_keys: <p>The list of tag keys that should be removed from the resource.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Remove Tags

            >>> await client.untag_resource(arn='arn:aws:interconnect:us-east-1:000000000000:connection/mcc-abc12345', tag_keys=['TagKey1', 'TagKey2'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_interconnect._operations.interconnect.untag_resource

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.untag_resource_request.UntagResourceRequest = {
            "arn": arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_connection(
        self,
        bandwidth: "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth",
        attach_point: "capo_interconnect.types.attach_point.AttachPoint",
        environment_id: "capo_interconnect.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        description: Optional[
            "capo_interconnect.types.connection_description.ConnectionDescription"
        ] = None,
        remote_account: Optional[
            "capo_interconnect.types.remote_account_identifier.RemoteAccountIdentifier"
        ] = None,
        tags: Optional["capo_interconnect.types.tag_map.TagMap"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_interconnect.types.create_connection_response.CreateConnectionResponse":
        r"""<p>Initiates the process to create a Connection across the specified Environment. </p> <p>The Environment dictates the specified partner and location to which the other end of the connection should attach. You can see a list of the available Environments by calling <a>ListEnvironments</a> </p> <p>The Attach Point specifies where within the AWS Network your connection will logically connect.</p> <p>After a successful call to this method, the resulting <a>Connection</a> will return an Activation Key which will need to be brought to the specific partner's portal to confirm the <a>Connection</a> on both sides. (See <a>Environment$activationPageUrl</a> for a direct link to the partner portal). </p>

        Args:
            description: <p>A description to distinguish this <a>Connection</a>.</p>
            bandwidth: <p>The desired bandwidth of the requested <a>Connection</a> </p>
            attach_point: <p>The Attach Point to which the connection should be associated.\"</p>
            environment_id: <p>The identifier of the <a>Environment</a> across which this <a>Connection</a> should be created.</p> <p>The available <a>Environment</a> objects can be determined using <a>ListEnvironments</a>.</p>
            remote_account: <p>Account and/or principal identifying information that can be verified by the partner of this specific Environment.</p>
            tags: <p>The tag to associate with the resulting <a>Connection</a>.</p>
            client_token: <p>Idempotency token used for the request.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create Connection on specific environment

            >>> await client.create_connection(bandwidth='1Gbps', environment_id='mce-aws-acme-1', remote_account={'identifier': 'PartnerAccountDetails'}, attach_point={'directConnectGateway': '90392BE3-219C-47FD-BBA5-03DF76D2542A'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.create_connection_request.CreateConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.create_connection_response.CreateConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.create_connection

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.create_connection.async_create_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.create_connection_request.CreateConnectionRequest = {
            "bandwidth": bandwidth,
            "attach_point": attach_point,
            "environment_id": environment_id,
        }
        if description is not None:
            input_["description"] = description
        if remote_account is not None:
            input_["remote_account"] = remote_account
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connection(
        self,
        identifier: "capo_interconnect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
    ) -> "capo_interconnect.types.get_connection_response.GetConnectionResponse":
        """<p>Describes the current state of a Connection resource as specified by the identifier. </p>

        Args:
            identifier: <p>The identifier of the requested <a>Connection</a> </p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get connection

            >>> await client.get_connection(identifier='mcc-abc12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.get_connection_request.GetConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.get_connection_response.GetConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.get_connection

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.get_connection.async_get_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.get_connection_request.GetConnectionRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connection(
        self,
        identifier: "capo_interconnect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        description: Optional[
            "capo_interconnect.types.connection_description.ConnectionDescription"
        ] = None,
        bandwidth: Optional[
            "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_interconnect.types.update_connection_response.UpdateConnectionResponse":
        """<p>Modifies an existing connection. Currently we support modifications to the connection's description and/or bandwidth.</p>

        Args:
            identifier: <p>The identifier of the <a>Connection</a> that should be updated.</p>
            description: <p>An updated description to apply to the <a>Connection</a> </p>
            bandwidth: <p>Request a new bandwidth size on the given <a>Connection</a>.</p> <p>Note that changes to the size may be subject to additional policy, and does require the remote partner provider to acknowledge and permit this new bandwidth size.</p>
            client_token: <p>Idempotency token used for the request.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update Connection Description

            >>> await client.update_connection(identifier='mcc-abc12345', description='Changed Description')
            Update Connection Bandwidth

            >>> await client.update_connection(identifier='mcc-abc12345', bandwidth='2Gbps')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.update_connection_request.UpdateConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.update_connection_response.UpdateConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.update_connection

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.update_connection.async_update_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.update_connection_request.UpdateConnectionRequest = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if bandwidth is not None:
            input_["bandwidth"] = bandwidth
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connection(
        self,
        identifier: "capo_interconnect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_interconnect.types.delete_connection_response.DeleteConnectionResponse":
        """<p>Deletes an existing Connection with the supplied identifier.</p> <p>This operation will also inform the remote partner of your intention to delete your connection. Note, the partner may still require you to delete to fully clean up resources, but the network connectivity provided by the <a>Connection</a> will cease to exist.</p>

        Args:
            identifier: <p>The identifier of the <a>Connection</a> to be deleted. </p>
            client_token: <p>Idempotency token used for the request.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete Connection

            >>> await client.delete_connection(identifier='mcc-abc12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.delete_connection_response.DeleteConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.delete_connection

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.delete_connection.async_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.delete_connection_request.DeleteConnectionRequest = {
            "identifier": identifier
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_connections(
        self,
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        max_results: Optional["capo_interconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_interconnect.types.next_token.NextToken"] = None,
        state: Optional[
            "capo_interconnect.types.connection_state.ConnectionState"
        ] = None,
        environment_id: Optional[
            "capo_interconnect.types.environment_id.EnvironmentId"
        ] = None,
        provider: Optional["capo_interconnect.types.provider.Provider"] = None,
        attach_point: Optional[
            "capo_interconnect.types.attach_point.AttachPoint"
        ] = None,
    ) -> "capo_interconnect.types.list_connections_response.ListConnectionsResponse":
        """<p>Lists all connection objects to which the caller has access.</p> <p>Allows for optional filtering by the following properties:</p> <ul> <li> <p> <code>state</code> </p> </li> <li> <p> <code>environmentId</code> </p> </li> <li> <p> <code>provider</code> </p> </li> <li> <p> <code>attach point</code> </p> </li> </ul> <p>Only <a>Connection</a> objects matching all filters will be returned.</p>

        Args:
            max_results: <p>The max number of list results in a single paginated response.</p>
            next_token: <p>A pagination token from a previous paginated response indicating you wish to get the next page of results.</p>
            state: <p>Filter the results to only include <a>Connection</a> objects in the given <a>Connection$state</a>.</p>
            environment_id: <p>Filter the results to only include <a>Connection</a> objects on the given <a>Environment</a>.</p>
            provider: <p>Filter the results to only include <a>Connection</a> objects to the given <a>Provider</a>.</p>
            attach_point: <p>Filter results to only include <a>Connection</a> objects attached to the given <a>AttachPoint</a>.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List All Connections

            >>> await client.list_connections()
            List Connections in available state

            >>> await client.list_connections(state='available')
            List Connections on specific Environment

            >>> await client.list_connections(environment_id='mce-aws-acme-1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.list_connections_request.ListConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.list_connections_response.ListConnectionsResponse"
        ]:
            import capo_interconnect._operations.interconnect.list_connections

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.list_connections.async_list_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.list_connections_request.ListConnectionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state is not None:
            input_["state"] = state
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if provider is not None:
            input_["provider"] = provider
        if attach_point is not None:
            input_["attach_point"] = attach_point

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_connections(
        self,
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        max_results: Optional["capo_interconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_interconnect.types.next_token.NextToken"] = None,
        state: Optional[
            "capo_interconnect.types.connection_state.ConnectionState"
        ] = None,
        environment_id: Optional[
            "capo_interconnect.types.environment_id.EnvironmentId"
        ] = None,
        provider: Optional["capo_interconnect.types.provider.Provider"] = None,
        attach_point: Optional[
            "capo_interconnect.types.attach_point.AttachPoint"
        ] = None,
    ) -> "AsyncIterator[capo_interconnect.types.connection_summary.ConnectionSummary]":
        _token = next_token
        while True:
            _response = await self.list_connections(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                state=state,
                environment_id=environment_id,
                provider=provider,
                attach_point=attach_point,
            )
            _page = _resolve_path(_response, ("connections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_environment(
        self,
        id: "capo_interconnect.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
    ) -> "capo_interconnect.types.get_environment_response.GetEnvironmentResponse":
        """<p>Describes a specific <a>Environment</a> </p>

        Args:
            id: <p>The identifier of the specific <a>Environment</a> to describe.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a specific environment

            >>> await client.get_environment(id='mce-aws-acme-1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.get_environment_request.GetEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import capo_interconnect._operations.interconnect.get_environment

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.get_environment.async_get_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.get_environment_request.GetEnvironmentRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_environments(
        self,
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        max_results: Optional["capo_interconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_interconnect.types.next_token.NextToken"] = None,
        provider: Optional["capo_interconnect.types.provider.Provider"] = None,
        location: Optional["capo_interconnect.types.location.Location"] = None,
    ) -> "capo_interconnect.types.list_environments_response.ListEnvironmentsResponse":
        """<p>Lists all of the environments that can produce connections that will land in the called AWS region.</p>

        Args:
            max_results: <p>The max number of list results in a single paginated response.</p>
            next_token: <p>A pagination token from a previous paginated response indicating you wish to get the next page of results.</p>
            provider: <p>Filter results to only include <a>Environment</a> objects that connect to the <a>Provider</a>.</p>
            location: <p>Filter results to only include <a>Environment</a> objects that connect to a given location distiguisher.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List All Environments

            >>> await client.list_environments()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import capo_interconnect._operations.interconnect.list_environments

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.list_environments.async_list_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_interconnect.types.list_environments_request.ListEnvironmentsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if provider is not None:
            input_["provider"] = provider
        if location is not None:
            input_["location"] = location

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_environments(
        self,
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        max_results: Optional["capo_interconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_interconnect.types.next_token.NextToken"] = None,
        provider: Optional["capo_interconnect.types.provider.Provider"] = None,
        location: Optional["capo_interconnect.types.location.Location"] = None,
    ) -> "AsyncIterator[capo_interconnect.types.environment.Environment]":
        _token = next_token
        while True:
            _response = await self.list_environments(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                provider=provider,
                location=location,
            )
            _page = _resolve_path(_response, ("environments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
