"""Generated from Smithy shape ``com.amazonaws.s3outposts#S3Outposts``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_s3outposts._auth._signers
import capo_s3outposts._auth._sigv4
from capo_s3outposts._auth._identity import Credentials
from capo_s3outposts._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_s3outposts._auth._zapros_handler import AuthMiddleware
from capo_s3outposts._pagination import resolve_path as _resolve_path
from capo_s3outposts._services._aws_config import aws_config
from capo_s3outposts._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_s3outposts.types.create_endpoint_request
    import capo_s3outposts.types.create_endpoint_result
    import capo_s3outposts.types.customer_owned_ipv4_pool
    import capo_s3outposts.types.delete_endpoint_request
    import capo_s3outposts.types.endpoint
    import capo_s3outposts.types.endpoint_access_type
    import capo_s3outposts.types.endpoint_id
    import capo_s3outposts.types.list_endpoints_request
    import capo_s3outposts.types.list_endpoints_result
    import capo_s3outposts.types.list_outposts_with_s3_request
    import capo_s3outposts.types.list_outposts_with_s3_result
    import capo_s3outposts.types.list_shared_endpoints_request
    import capo_s3outposts.types.list_shared_endpoints_result
    import capo_s3outposts.types.max_results
    import capo_s3outposts.types.next_token
    import capo_s3outposts.types.outpost
    import capo_s3outposts.types.outpost_id
    import capo_s3outposts.types.security_group_id
    import capo_s3outposts.types.subnet_id


class S3OutpostsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class S3OutpostsClient:
    """A client for the ``S3Outposts`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = S3OutpostsClientConfig(
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
        self, config_overrides: Optional[S3OutpostsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: S3OutpostsClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def create_endpoint(
        self,
        outpost_id: "capo_s3outposts.types.outpost_id.OutpostId",
        subnet_id: "capo_s3outposts.types.subnet_id.SubnetId",
        security_group_id: "capo_s3outposts.types.security_group_id.SecurityGroupId",
        *,
        config_overrides: Optional[S3OutpostsClientConfig] = None,
        access_type: Optional[
            "capo_s3outposts.types.endpoint_access_type.EndpointAccessType"
        ] = None,
        customer_owned_ipv4_pool: Optional[
            "capo_s3outposts.types.customer_owned_ipv4_pool.CustomerOwnedIpv4Pool"
        ] = None,
    ) -> "capo_s3outposts.types.create_endpoint_result.CreateEndpointResult":
        """<p>Creates an endpoint and associates it with the specified Outpost.</p> <note> <p>It can take up to 5 minutes for this action to finish.</p> </note> <p></p> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html">DeleteEndpoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListEndpoints.html">ListEndpoints</a> </p> </li> </ul>

        Args:
            outpost_id: <p>The ID of the Outposts. </p>
            subnet_id: <p>The ID of the subnet in the selected VPC. The endpoint subnet must belong to the Outpost that has Amazon S3 on Outposts provisioned.</p>
            security_group_id: <p>The ID of the security group to use with the endpoint.</p>
            access_type: <p>The type of access for the network connectivity for the Amazon S3 on Outposts endpoint. To use the Amazon Web Services VPC, choose <code>Private</code>. To use the endpoint with an on-premises network, choose <code>CustomerOwnedIp</code>. If you choose <code>CustomerOwnedIp</code>, you must also provide the customer-owned IP address pool (CoIP pool).</p> <note> <p> <code>Private</code> is the default access type value.</p> </note>
            customer_owned_ipv4_pool: <p>The ID of the customer-owned IPv4 address pool (CoIP pool) for the endpoint. IP addresses are allocated from this pool for the endpoint.</p>

        Raises:
            capo_s3outposts.errors.access_denied_exception.AccessDeniedException: <p>Access was denied for this action.</p>
            capo_s3outposts.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_s3outposts.errors.internal_server_exception.InternalServerException: <p>There was an exception with the internal server.</p>
            capo_s3outposts.errors.outpost_offline_exception.OutpostOfflineException: <p>The service link connection to your Outposts home Region is down. Check your connection and try again.</p>
            capo_s3outposts.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_s3outposts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_s3outposts.errors.validation_exception.ValidationException: <p>There was an exception validating this data.</p>
            capo_s3outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3outposts.types.create_endpoint_request.CreateEndpointRequest]",
        ) -> OperationResponse[
            "capo_s3outposts.types.create_endpoint_result.CreateEndpointResult"
        ]:
            import capo_s3outposts._operations.s3_outposts.create_endpoint

            output, http_response = (
                capo_s3outposts._operations.s3_outposts.create_endpoint.create_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3outposts.types.create_endpoint_request.CreateEndpointRequest = {
            "outpost_id": outpost_id,
            "subnet_id": subnet_id,
            "security_group_id": security_group_id,
        }
        if access_type is not None:
            input_["access_type"] = access_type
        if customer_owned_ipv4_pool is not None:
            input_["customer_owned_ipv4_pool"] = customer_owned_ipv4_pool

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_endpoint(
        self,
        endpoint_id: "capo_s3outposts.types.endpoint_id.EndpointId",
        outpost_id: "capo_s3outposts.types.outpost_id.OutpostId",
        *,
        config_overrides: Optional[S3OutpostsClientConfig] = None,
    ) -> None:
        """<p>Deletes an endpoint.</p> <note> <p>It can take up to 5 minutes for this action to finish.</p> </note> <p></p> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html">CreateEndpoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListEndpoints.html">ListEndpoints</a> </p> </li> </ul>

        Args:
            endpoint_id: <p>The ID of the endpoint.</p>
            outpost_id: <p>The ID of the Outposts. </p>

        Raises:
            capo_s3outposts.errors.access_denied_exception.AccessDeniedException: <p>Access was denied for this action.</p>
            capo_s3outposts.errors.internal_server_exception.InternalServerException: <p>There was an exception with the internal server.</p>
            capo_s3outposts.errors.outpost_offline_exception.OutpostOfflineException: <p>The service link connection to your Outposts home Region is down. Check your connection and try again.</p>
            capo_s3outposts.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_s3outposts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_s3outposts.errors.validation_exception.ValidationException: <p>There was an exception validating this data.</p>
            capo_s3outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3outposts.types.delete_endpoint_request.DeleteEndpointRequest]",
        ) -> OperationResponse[None]:
            import capo_s3outposts._operations.s3_outposts.delete_endpoint

            output, http_response = (
                capo_s3outposts._operations.s3_outposts.delete_endpoint.delete_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3outposts.types.delete_endpoint_request.DeleteEndpointRequest = {
            "endpoint_id": endpoint_id,
            "outpost_id": outpost_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_endpoints(
        self,
        *,
        config_overrides: Optional[S3OutpostsClientConfig] = None,
        next_token: Optional["capo_s3outposts.types.next_token.NextToken"] = None,
        max_results: Optional["capo_s3outposts.types.max_results.MaxResults"] = None,
    ) -> "capo_s3outposts.types.list_endpoints_result.ListEndpointsResult":
        """<p>Lists endpoints associated with the specified Outpost. </p> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html">CreateEndpoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html">DeleteEndpoint</a> </p> </li> </ul>

        Args:
            next_token: <p>If a previous response from this operation included a <code>NextToken</code> value, provide that value here to retrieve the next page of results.</p>
            max_results: <p>The maximum number of endpoints that will be returned in the response.</p>

        Raises:
            capo_s3outposts.errors.access_denied_exception.AccessDeniedException: <p>Access was denied for this action.</p>
            capo_s3outposts.errors.internal_server_exception.InternalServerException: <p>There was an exception with the internal server.</p>
            capo_s3outposts.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_s3outposts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_s3outposts.errors.validation_exception.ValidationException: <p>There was an exception validating this data.</p>
            capo_s3outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3outposts.types.list_endpoints_request.ListEndpointsRequest]",
        ) -> OperationResponse[
            "capo_s3outposts.types.list_endpoints_result.ListEndpointsResult"
        ]:
            import capo_s3outposts._operations.s3_outposts.list_endpoints

            output, http_response = (
                capo_s3outposts._operations.s3_outposts.list_endpoints.list_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3outposts.types.list_endpoints_request.ListEndpointsRequest = {}
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

    def iter_list_endpoints(
        self,
        *,
        config_overrides: Optional[S3OutpostsClientConfig] = None,
        next_token: Optional["capo_s3outposts.types.next_token.NextToken"] = None,
        max_results: Optional["capo_s3outposts.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_s3outposts.types.endpoint.Endpoint]":
        _token = next_token
        while True:
            _response = self.list_endpoints(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_outposts_with_s3(
        self,
        *,
        config_overrides: Optional[S3OutpostsClientConfig] = None,
        next_token: Optional["capo_s3outposts.types.next_token.NextToken"] = None,
        max_results: Optional["capo_s3outposts.types.max_results.MaxResults"] = None,
    ) -> "capo_s3outposts.types.list_outposts_with_s3_result.ListOutpostsWithS3Result":
        """<p>Lists the Outposts with S3 on Outposts capacity for your Amazon Web Services account. Includes S3 on Outposts that you have access to as the Outposts owner, or as a shared user from Resource Access Manager (RAM). </p>

        Args:
            next_token: <p>When you can get additional results from the <code>ListOutpostsWithS3</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional Outposts.</p>
            max_results: <p>The maximum number of Outposts to return. The limit is 100.</p>

        Raises:
            capo_s3outposts.errors.access_denied_exception.AccessDeniedException: <p>Access was denied for this action.</p>
            capo_s3outposts.errors.internal_server_exception.InternalServerException: <p>There was an exception with the internal server.</p>
            capo_s3outposts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_s3outposts.errors.validation_exception.ValidationException: <p>There was an exception validating this data.</p>
            capo_s3outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3outposts.types.list_outposts_with_s3_request.ListOutpostsWithS3Request]",
        ) -> OperationResponse[
            "capo_s3outposts.types.list_outposts_with_s3_result.ListOutpostsWithS3Result"
        ]:
            import capo_s3outposts._operations.s3_outposts.list_outposts_with_s3

            output, http_response = (
                capo_s3outposts._operations.s3_outposts.list_outposts_with_s3.list_outposts_with_s3(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3outposts.types.list_outposts_with_s3_request.ListOutpostsWithS3Request = {}
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

    def iter_list_outposts_with_s3(
        self,
        *,
        config_overrides: Optional[S3OutpostsClientConfig] = None,
        next_token: Optional["capo_s3outposts.types.next_token.NextToken"] = None,
        max_results: Optional["capo_s3outposts.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_s3outposts.types.outpost.Outpost]":
        _token = next_token
        while True:
            _response = self.list_outposts_with_s3(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("outposts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_shared_endpoints(
        self,
        outpost_id: "capo_s3outposts.types.outpost_id.OutpostId",
        *,
        config_overrides: Optional[S3OutpostsClientConfig] = None,
        next_token: Optional["capo_s3outposts.types.next_token.NextToken"] = None,
        max_results: Optional["capo_s3outposts.types.max_results.MaxResults"] = None,
    ) -> "capo_s3outposts.types.list_shared_endpoints_result.ListSharedEndpointsResult":
        """<p>Lists all endpoints associated with an Outpost that has been shared by Amazon Web Services Resource Access Manager (RAM).</p> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html">CreateEndpoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html">DeleteEndpoint</a> </p> </li> </ul>

        Args:
            next_token: <p>If a previous response from this operation included a <code>NextToken</code> value, you can provide that value here to retrieve the next page of results.</p>
            max_results: <p>The maximum number of endpoints that will be returned in the response.</p>
            outpost_id: <p>The ID of the Amazon Web Services Outpost.</p>

        Raises:
            capo_s3outposts.errors.access_denied_exception.AccessDeniedException: <p>Access was denied for this action.</p>
            capo_s3outposts.errors.internal_server_exception.InternalServerException: <p>There was an exception with the internal server.</p>
            capo_s3outposts.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_s3outposts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_s3outposts.errors.validation_exception.ValidationException: <p>There was an exception validating this data.</p>
            capo_s3outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3outposts.types.list_shared_endpoints_request.ListSharedEndpointsRequest]",
        ) -> OperationResponse[
            "capo_s3outposts.types.list_shared_endpoints_result.ListSharedEndpointsResult"
        ]:
            import capo_s3outposts._operations.s3_outposts.list_shared_endpoints

            output, http_response = (
                capo_s3outposts._operations.s3_outposts.list_shared_endpoints.list_shared_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3outposts.types.list_shared_endpoints_request.ListSharedEndpointsRequest = {
            "outpost_id": outpost_id
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

    def iter_list_shared_endpoints(
        self,
        outpost_id: "capo_s3outposts.types.outpost_id.OutpostId",
        *,
        config_overrides: Optional[S3OutpostsClientConfig] = None,
        next_token: Optional["capo_s3outposts.types.next_token.NextToken"] = None,
        max_results: Optional["capo_s3outposts.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_s3outposts.types.endpoint.Endpoint]":
        _token = next_token
        while True:
            _response = self.list_shared_endpoints(
                outpost_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
