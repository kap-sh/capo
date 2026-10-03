"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#PcaConnectorScep``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_pca_connector_scep._auth._signers
import capo_pca_connector_scep._auth._sigv4
from capo_pca_connector_scep._auth._identity import Credentials
from capo_pca_connector_scep._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_pca_connector_scep._auth._zapros_handler import AuthMiddleware
from capo_pca_connector_scep._pagination import resolve_path as _resolve_path
from capo_pca_connector_scep._resources.pca_connector_scep.challenge_resource import (
    AsyncChallengeResource,
)
from capo_pca_connector_scep._resources.pca_connector_scep.connector_resource import (
    AsyncConnectorResource,
)
from capo_pca_connector_scep._services._aws_config import aaws_config
from capo_pca_connector_scep._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.certificate_authority_arn
    import capo_pca_connector_scep.types.challenge_arn
    import capo_pca_connector_scep.types.challenge_metadata_summary
    import capo_pca_connector_scep.types.client_token
    import capo_pca_connector_scep.types.connector_arn
    import capo_pca_connector_scep.types.connector_summary
    import capo_pca_connector_scep.types.create_challenge_request
    import capo_pca_connector_scep.types.create_challenge_response
    import capo_pca_connector_scep.types.create_connector_request
    import capo_pca_connector_scep.types.create_connector_response
    import capo_pca_connector_scep.types.delete_challenge_request
    import capo_pca_connector_scep.types.delete_connector_request
    import capo_pca_connector_scep.types.get_challenge_metadata_request
    import capo_pca_connector_scep.types.get_challenge_metadata_response
    import capo_pca_connector_scep.types.get_challenge_password_request
    import capo_pca_connector_scep.types.get_challenge_password_response
    import capo_pca_connector_scep.types.get_connector_request
    import capo_pca_connector_scep.types.get_connector_response
    import capo_pca_connector_scep.types.list_challenge_metadata_request
    import capo_pca_connector_scep.types.list_challenge_metadata_response
    import capo_pca_connector_scep.types.list_connectors_request
    import capo_pca_connector_scep.types.list_connectors_response
    import capo_pca_connector_scep.types.list_tags_for_resource_request
    import capo_pca_connector_scep.types.list_tags_for_resource_response
    import capo_pca_connector_scep.types.max_results
    import capo_pca_connector_scep.types.mobile_device_management
    import capo_pca_connector_scep.types.next_token
    import capo_pca_connector_scep.types.tag_key_list
    import capo_pca_connector_scep.types.tag_resource_request
    import capo_pca_connector_scep.types.tags
    import capo_pca_connector_scep.types.untag_resource_request
    import capo_pca_connector_scep.types.vpc_endpoint_id


class AsyncPcaConnectorScepClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncPcaConnectorScepClient:
    """A client for the ``PcaConnectorScep`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = AsyncPcaConnectorScepClientConfig(
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

        # resources
        self.challenge_resource = AsyncChallengeResource(self)
        self.connector_resource = AsyncConnectorResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPcaConnectorScepClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> "capo_pca_connector_scep.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the tags associated with the specified resource. Tags are key-value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to "customer" and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: str,
        tags: "capo_pca_connector_scep.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> None:
        """<p>Adds one or more tags to your resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The key-value pairs to associate with the resource.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_scep._operations.pca_connector_scep.tag_resource

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: str,
        tag_keys: "capo_pca_connector_scep.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> None:
        """<p>Removes one or more tags from your resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>Specifies a list of tag keys that you want to remove from the specified resources.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_scep._operations.pca_connector_scep.untag_resource

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_challenge(
        self,
        connector_arn: "capo_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_scep.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pca_connector_scep.types.tags.Tags"] = None,
    ) -> "capo_pca_connector_scep.types.create_challenge_response.CreateChallengeResponse":
        """<p>For general-purpose connectors. Creates a <i>challenge password</i> for the specified connector. The SCEP protocol uses a challenge password to authenticate a request before issuing a certificate from a certificate authority (CA). Your SCEP clients include the challenge password as part of their certificate request to Connector for SCEP. To retrieve the connector Amazon Resource Names (ARNs) for the connectors in your account, call <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListConnectors.html">ListConnectors</a>.</p> <p>To create additional challenge passwords for the connector, call <code>CreateChallenge</code> again. We recommend frequently rotating your challenge passwords.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector that you want to create a challenge for.</p>
            client_token: <p>Custom string that can be used to distinguish between calls to the <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html">CreateChallenge</a> action. Client tokens for <code>CreateChallenge</code> time out after five minutes. Therefore, if you call <code>CreateChallenge</code> multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.</p>
            tags: <p>The key-value pairs to associate with the resource.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_pca_connector_scep.errors.conflict_exception.ConflictException: <p>This request can't be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.create_challenge_request.CreateChallengeRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.create_challenge_response.CreateChallengeResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.create_challenge

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.create_challenge.async_create_challenge(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.create_challenge_request.CreateChallengeRequest = {
            "connector_arn": connector_arn
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_challenge_metadata(
        self,
        challenge_arn: "capo_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> "capo_pca_connector_scep.types.get_challenge_metadata_response.GetChallengeMetadataResponse":
        """<p>Retrieves the metadata for the specified <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.get_challenge_metadata_request.GetChallengeMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.get_challenge_metadata_response.GetChallengeMetadataResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_metadata

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_metadata.async_get_challenge_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.get_challenge_metadata_request.GetChallengeMetadataRequest = {
            "challenge_arn": challenge_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_challenge(
        self,
        challenge_arn: "capo_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge password to delete.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.conflict_exception.ConflictException: <p>This request can't be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.delete_challenge_request.DeleteChallengeRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_scep._operations.pca_connector_scep.delete_challenge

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.delete_challenge.async_delete_challenge(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.delete_challenge_request.DeleteChallengeRequest = {
            "challenge_arn": challenge_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_challenge_metadata(
        self,
        connector_arn: "capo_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_scep.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_pca_connector_scep.types.next_token.NextToken"
        ] = None,
    ) -> "capo_pca_connector_scep.types.list_challenge_metadata_response.ListChallengeMetadataResponse":
        """<p>Retrieves the challenge metadata for the specified ARN.</p>

        Args:
            max_results: <p>The maximum number of objects that you want Connector for SCEP to return for this request. If more objects are available, in the response, Connector for SCEP provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.list_challenge_metadata_request.ListChallengeMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.list_challenge_metadata_response.ListChallengeMetadataResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.list_challenge_metadata

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.list_challenge_metadata.async_list_challenge_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.list_challenge_metadata_request.ListChallengeMetadataRequest = {
            "connector_arn": connector_arn
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

    async def iter_list_challenge_metadata(
        self,
        connector_arn: "capo_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_scep.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_pca_connector_scep.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_pca_connector_scep.types.challenge_metadata_summary.ChallengeMetadataSummary]":
        _token = next_token
        while True:
            _response = await self.list_challenge_metadata(
                connector_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("challenges",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_challenge_password(
        self,
        challenge_arn: "capo_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> "capo_pca_connector_scep.types.get_challenge_password_response.GetChallengePasswordResponse":
        """<p>Retrieves the challenge password for the specified <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.get_challenge_password_request.GetChallengePasswordRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.get_challenge_password_response.GetChallengePasswordResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_password

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.get_challenge_password.async_get_challenge_password(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.get_challenge_password_request.GetChallengePasswordRequest = {
            "challenge_arn": challenge_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_connector(
        self,
        certificate_authority_arn: "capo_pca_connector_scep.types.certificate_authority_arn.CertificateAuthorityArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        mobile_device_management: Optional[
            "capo_pca_connector_scep.types.mobile_device_management.MobileDeviceManagement"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_pca_connector_scep.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        client_token: Optional[
            "capo_pca_connector_scep.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pca_connector_scep.types.tags.Tags"] = None,
    ) -> "capo_pca_connector_scep.types.create_connector_response.CreateConnectorResponse":
        """<p>Creates a SCEP connector. A SCEP connector links Amazon Web Services Private Certificate Authority to your SCEP-compatible devices and mobile device management (MDM) systems. Before you create a connector, you must complete a set of prerequisites, including creation of a private certificate authority (CA) to use with this connector. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-prerequisites.html">Connector for SCEP prerequisites</a>.</p>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Private Certificate Authority certificate authority to use with this connector. Due to security vulnerabilities present in the SCEP protocol, we recommend using a private CA that's dedicated for use with the connector.</p> <p>To retrieve the private CAs associated with your account, you can call <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> using the Amazon Web Services Private CA API.</p>
            mobile_device_management: <p>If you don't supply a value, by default Connector for SCEP creates a connector for general-purpose use. A general-purpose connector is designed to work with clients or endpoints that support the SCEP protocol, except Connector for SCEP for Microsoft Intune. With connectors for general-purpose use, you manage SCEP challenge passwords using Connector for SCEP. For information about considerations and limitations with using Connector for SCEP, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlc4scep-considerations-limitations.html">Considerations and Limitations</a>.</p> <p>If you provide an <code>IntuneConfiguration</code>, Connector for SCEP creates a connector for use with Microsoft Intune, and you manage the challenge passwords using Microsoft Intune. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html">Using Connector for SCEP for Microsoft Intune</a>.</p>
            vpc_endpoint_id: <p>If you don't supply a value, by default Connector for SCEP creates a connector accessible over the public internet. If you provide a VPC endpoint ID, creates a connector accessible only through that specific VPC endpoint.</p>
            client_token: <p>Custom string that can be used to distinguish between calls to the <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html">CreateChallenge</a> action. Client tokens for <code>CreateChallenge</code> time out after five minutes. Therefore, if you call <code>CreateChallenge</code> multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.</p>
            tags: <p>The key-value pairs to associate with the resource.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.conflict_exception.ConflictException: <p>This request can't be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.create_connector_request.CreateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.create_connector_response.CreateConnectorResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.create_connector

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.create_connector.async_create_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.create_connector_request.CreateConnectorRequest = {
            "certificate_authority_arn": certificate_authority_arn
        }
        if mobile_device_management is not None:
            input_["mobile_device_management"] = mobile_device_management
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connector(
        self,
        connector_arn: "capo_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> "capo_pca_connector_scep.types.get_connector_response.GetConnectorResponse":
        """<p>Retrieves details about the specified <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Connector.html">Connector</a>. Calling this action returns important details about the connector, such as the public SCEP URL where your clients can request certificates.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.get_connector_request.GetConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.get_connector_response.GetConnectorResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.get_connector

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.get_connector.async_get_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.get_connector_request.GetConnectorRequest = {
            "connector_arn": connector_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connector(
        self,
        connector_arn: "capo_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Connector.html">Connector</a>. This operation also deletes any challenges associated with the connector.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector to delete.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.conflict_exception.ConflictException: <p>This request can't be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might be incorrectly specified, or it might have a status other than <code>ACTIVE</code>.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_scep._operations.pca_connector_scep.delete_connector

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.delete_connector.async_delete_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.delete_connector_request.DeleteConnectorRequest = {
            "connector_arn": connector_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_connectors(
        self,
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_scep.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_pca_connector_scep.types.next_token.NextToken"
        ] = None,
    ) -> (
        "capo_pca_connector_scep.types.list_connectors_response.ListConnectorsResponse"
    ):
        """<p>Lists the connectors belonging to your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of objects that you want Connector for SCEP to return for this request. If more objects are available, in the response, Connector for SCEP provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>

        Raises:
            capo_pca_connector_scep.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account.</p>
            capo_pca_connector_scep.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_pca_connector_scep.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_pca_connector_scep.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.</p>
            capo_pca_connector_scep.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_scep.types.list_connectors_request.ListConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_scep.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_pca_connector_scep._operations.pca_connector_scep.list_connectors

            (
                output,
                http_response,
            ) = await capo_pca_connector_scep._operations.pca_connector_scep.list_connectors.async_list_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_scep.types.list_connectors_request.ListConnectorsRequest = {}
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

    async def iter_list_connectors(
        self,
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_scep.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_pca_connector_scep.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_pca_connector_scep.types.connector_summary.ConnectorSummary]":
        _token = next_token
        while True:
            _response = await self.list_connectors(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("connectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
