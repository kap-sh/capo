"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#PartnerCentralChannel``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_partnercentral_channel._auth._signers
import capo_partnercentral_channel._auth._sigv4
from capo_partnercentral_channel._auth._identity import Credentials
from capo_partnercentral_channel._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_partnercentral_channel._auth._zapros_handler import AuthMiddleware
from capo_partnercentral_channel._pagination import resolve_path as _resolve_path
from capo_partnercentral_channel._resources.partner_central_channel.channel_handshake_resource import (
    ChannelHandshakeResource,
)
from capo_partnercentral_channel._resources.partner_central_channel.program_management_account_resource import (
    ProgramManagementAccountResource,
)
from capo_partnercentral_channel._resources.partner_central_channel.relationship_resource import (
    RelationshipResource,
)
from capo_partnercentral_channel._services._aws_config import aws_config
from capo_partnercentral_channel._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.accept_channel_handshake_request
    import capo_partnercentral_channel.types.accept_channel_handshake_response
    import capo_partnercentral_channel.types.account_id
    import capo_partnercentral_channel.types.account_id_list
    import capo_partnercentral_channel.types.associated_resource_identifier
    import capo_partnercentral_channel.types.associated_resource_identifier_list
    import capo_partnercentral_channel.types.association_type
    import capo_partnercentral_channel.types.association_type_list
    import capo_partnercentral_channel.types.cancel_channel_handshake_request
    import capo_partnercentral_channel.types.cancel_channel_handshake_response
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.channel_handshake_identifier
    import capo_partnercentral_channel.types.channel_handshake_payload
    import capo_partnercentral_channel.types.channel_handshake_summary
    import capo_partnercentral_channel.types.client_token
    import capo_partnercentral_channel.types.create_channel_handshake_request
    import capo_partnercentral_channel.types.create_channel_handshake_response
    import capo_partnercentral_channel.types.create_program_management_account_request
    import capo_partnercentral_channel.types.create_program_management_account_response
    import capo_partnercentral_channel.types.create_relationship_request
    import capo_partnercentral_channel.types.create_relationship_response
    import capo_partnercentral_channel.types.delete_program_management_account_request
    import capo_partnercentral_channel.types.delete_program_management_account_response
    import capo_partnercentral_channel.types.delete_relationship_request
    import capo_partnercentral_channel.types.delete_relationship_response
    import capo_partnercentral_channel.types.get_relationship_request
    import capo_partnercentral_channel.types.get_relationship_response
    import capo_partnercentral_channel.types.handshake_status_list
    import capo_partnercentral_channel.types.handshake_type
    import capo_partnercentral_channel.types.list_channel_handshakes_request
    import capo_partnercentral_channel.types.list_channel_handshakes_response
    import capo_partnercentral_channel.types.list_channel_handshakes_type_filters
    import capo_partnercentral_channel.types.list_channel_handshakes_type_sort
    import capo_partnercentral_channel.types.list_program_management_accounts_request
    import capo_partnercentral_channel.types.list_program_management_accounts_response
    import capo_partnercentral_channel.types.list_program_management_accounts_sort_base
    import capo_partnercentral_channel.types.list_relationships_request
    import capo_partnercentral_channel.types.list_relationships_response
    import capo_partnercentral_channel.types.list_relationships_sort_base
    import capo_partnercentral_channel.types.list_tags_for_resource_request
    import capo_partnercentral_channel.types.list_tags_for_resource_response
    import capo_partnercentral_channel.types.next_token
    import capo_partnercentral_channel.types.participant_type
    import capo_partnercentral_channel.types.program
    import capo_partnercentral_channel.types.program_list
    import capo_partnercentral_channel.types.program_management_account_display_name
    import capo_partnercentral_channel.types.program_management_account_display_name_list
    import capo_partnercentral_channel.types.program_management_account_identifier
    import capo_partnercentral_channel.types.program_management_account_identifier_list
    import capo_partnercentral_channel.types.program_management_account_status_list
    import capo_partnercentral_channel.types.program_management_account_summary
    import capo_partnercentral_channel.types.reject_channel_handshake_request
    import capo_partnercentral_channel.types.reject_channel_handshake_response
    import capo_partnercentral_channel.types.relationship_display_name
    import capo_partnercentral_channel.types.relationship_display_name_list
    import capo_partnercentral_channel.types.relationship_identifier
    import capo_partnercentral_channel.types.relationship_summary
    import capo_partnercentral_channel.types.resale_account_model
    import capo_partnercentral_channel.types.revision
    import capo_partnercentral_channel.types.sector
    import capo_partnercentral_channel.types.support_plan
    import capo_partnercentral_channel.types.tag_key_list
    import capo_partnercentral_channel.types.tag_list
    import capo_partnercentral_channel.types.tag_resource_request
    import capo_partnercentral_channel.types.tag_resource_response
    import capo_partnercentral_channel.types.taggable_arn
    import capo_partnercentral_channel.types.untag_resource_request
    import capo_partnercentral_channel.types.untag_resource_response
    import capo_partnercentral_channel.types.update_program_management_account_request
    import capo_partnercentral_channel.types.update_program_management_account_response
    import capo_partnercentral_channel.types.update_relationship_request
    import capo_partnercentral_channel.types.update_relationship_response


class PartnerCentralChannelClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class PartnerCentralChannelClient:
    """A client for the ``PartnerCentralChannel`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
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
        self._config = PartnerCentralChannelClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.channel_handshake_resource = ChannelHandshakeResource(self)
        self.program_management_account_resource = ProgramManagementAccountResource(
            self
        )
        self.relationship_resource = RelationshipResource(self)

    def operation_options(
        self, config_overrides: Optional[PartnerCentralChannelClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PartnerCentralChannelClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_partnercentral_channel.types.taggable_arn.TaggableArn",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "capo_partnercentral_channel.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags associated with a specific resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListTagsForResource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/program-management-account/pma-u8ic702rtzng8')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.list_tags_for_resource

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_partnercentral_channel.types.taggable_arn.TaggableArn",
        tags: "capo_partnercentral_channel.types.tag_list.TagList",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "capo_partnercentral_channel.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>Key-value pairs to associate with the resource.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for TagResource

            >>> client.tag_resource(resource_arn='arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/program-management-account/pma-u8ic702rtzng8/relationship/rs-l9o4fj3b5zb91', tags=[{'key': 'ExampleKey', 'value': 'ExampleValue'}])
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.tag_resource

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_partnercentral_channel.types.taggable_arn.TaggableArn",
        tag_keys: "capo_partnercentral_channel.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "capo_partnercentral_channel.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The keys of the tags to remove from the resource.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for UntagResource

            >>> client.untag_resource(resource_arn='arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/channel-handshake/ch-4fj3bd2o3vb91', tag_keys=['ExampleKey'])
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.untag_resource

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.untag_resource_request.UntagResourceRequest = {
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

    def create_channel_handshake(
        self,
        handshake_type: "capo_partnercentral_channel.types.handshake_type.HandshakeType",
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        associated_resource_identifier: "capo_partnercentral_channel.types.associated_resource_identifier.AssociatedResourceIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        payload: Optional[
            "capo_partnercentral_channel.types.channel_handshake_payload.ChannelHandshakePayload"
        ] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_channel.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_channel.types.create_channel_handshake_response.CreateChannelHandshakeResponse":
        """<p>Creates a new channel handshake request to establish a partnership with another AWS account.</p>

        Args:
            handshake_type: <p>The type of handshake to create (e.g., start service period, revoke service period).</p>
            catalog: <p>The catalog identifier for the handshake request.</p>
            associated_resource_identifier: <p>The identifier of the resource associated with this handshake.</p>
            payload: <p>The payload containing specific details for the handshake type.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Key-value pairs to associate with the channel handshake.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for CreateChannelHandshake - START_SERVICE_PERIOD with Minimum Notice Period

            >>> client.create_channel_handshake(handshake_type='START_SERVICE_PERIOD', catalog='AWS', associated_resource_identifier='rs-abc123def456g', payload={'startServicePeriodPayload': {'programManagementAccountIdentifier': 'pma-abcdef123456g', 'servicePeriodType': 'MINIMUM_NOTICE_PERIOD', 'minimumNoticeDays': '14', 'note': 'Optional Note'}}, client_token='clientToken')
            Example for CreateChannelHandshake - START_SERVICE_PERIOD with Fixed Commitment Period

            >>> client.create_channel_handshake(handshake_type='START_SERVICE_PERIOD', catalog='AWS', associated_resource_identifier='rs-abc123def456g', payload={'startServicePeriodPayload': {'programManagementAccountIdentifier': 'pma-abcdef123456g', 'servicePeriodType': 'FIXED_COMMITMENT_PERIOD', 'endDate': '2026-07-01T00:00:00Z', 'note': 'Optional Note'}}, client_token='clientToken')
            Example for CreateChannelHandshake - REVOKE_SERVICE_PERIOD

            >>> client.create_channel_handshake(handshake_type='REVOKE_SERVICE_PERIOD', catalog='AWS', associated_resource_identifier='rs-abc123def456g', payload={'revokeServicePeriodPayload': {'programManagementAccountIdentifier': 'pma-abcdef123456g', 'note': 'Optional Note'}}, client_token='clientToken')
            Example for CreateChannelHandshake - PROGRAM_MANAGEMENT_ACCOUNT

            >>> client.create_channel_handshake(handshake_type='PROGRAM_MANAGEMENT_ACCOUNT', catalog='AWS', associated_resource_identifier='pma-123abc456def7', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.create_channel_handshake_request.CreateChannelHandshakeRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.create_channel_handshake_response.CreateChannelHandshakeResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.create_channel_handshake

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.create_channel_handshake.create_channel_handshake(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.create_channel_handshake_request.CreateChannelHandshakeRequest = {
            "handshake_type": handshake_type,
            "catalog": catalog,
            "associated_resource_identifier": associated_resource_identifier,
        }
        if payload is not None:
            input_["payload"] = payload
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

    def list_channel_handshakes(
        self,
        handshake_type: "capo_partnercentral_channel.types.handshake_type.HandshakeType",
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        participant_type: "capo_partnercentral_channel.types.participant_type.ParticipantType",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        statuses: Optional[
            "capo_partnercentral_channel.types.handshake_status_list.HandshakeStatusList"
        ] = None,
        associated_resource_identifiers: Optional[
            "capo_partnercentral_channel.types.associated_resource_identifier_list.AssociatedResourceIdentifierList"
        ] = None,
        handshake_type_filters: Optional[
            "capo_partnercentral_channel.types.list_channel_handshakes_type_filters.ListChannelHandshakesTypeFilters"
        ] = None,
        handshake_type_sort: Optional[
            "capo_partnercentral_channel.types.list_channel_handshakes_type_sort.ListChannelHandshakesTypeSort"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.list_channel_handshakes_response.ListChannelHandshakesResponse":
        """<p>Lists channel handshakes based on specified criteria.</p>

        Args:
            handshake_type: <p>Filter results by handshake type.</p>
            catalog: <p>The catalog identifier to filter handshakes.</p>
            participant_type: <p>Filter by participant type (sender or receiver).</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            statuses: <p>Filter results by handshake status.</p>
            associated_resource_identifiers: <p>Filter by associated resource identifiers.</p>
            handshake_type_filters: <p>Type-specific filters for handshakes.</p>
            handshake_type_sort: <p>Type-specific sorting options for handshakes.</p>
            next_token: <p>Token for retrieving the next page of results.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListChannelHandshakes - START_SERVICE_PERIOD

            >>> client.list_channel_handshakes(handshake_type='START_SERVICE_PERIOD', catalog='AWS', participant_type='SENDER', statuses=['ACCEPTED'], associated_resource_identifiers=['rs-123abc456def7'], handshake_type_filters={'startServicePeriodTypeFilters': {'servicePeriodTypes': ['FIXED_COMMITMENT_PERIOD']}}, handshake_type_sort={'startServicePeriodTypeSort': {'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}})
            Example for ListChannelHandshakes - REVOKE_SERVICE_PERIOD

            >>> client.list_channel_handshakes(handshake_type='REVOKE_SERVICE_PERIOD', catalog='AWS', participant_type='SENDER', statuses=['ACCEPTED'], associated_resource_identifiers=['rs-123abc456def7'], handshake_type_filters={'revokeServicePeriodTypeFilters': {'servicePeriodTypes': ['MINIMUM_NOTICE_PERIOD']}}, handshake_type_sort={'revokeServicePeriodTypeSort': {'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}})
            Example for ListChannelHandshakes - PROGRAM_MANAGEMENT_ACCOUNT

            >>> client.list_channel_handshakes(handshake_type='PROGRAM_MANAGEMENT_ACCOUNT', catalog='AWS', participant_type='SENDER', statuses=['ACCEPTED'], associated_resource_identifiers=['pma-123abc456def7'], handshake_type_filters={'programManagementAccountTypeFilters': {'programs': ['SOLUTION_PROVIDER']}}, handshake_type_sort={'programManagementAccountTypeSort': {'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}}, max_results=20, next_token='nextToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.list_channel_handshakes_request.ListChannelHandshakesRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.list_channel_handshakes_response.ListChannelHandshakesResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.list_channel_handshakes

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.list_channel_handshakes.list_channel_handshakes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.list_channel_handshakes_request.ListChannelHandshakesRequest = {
            "handshake_type": handshake_type,
            "catalog": catalog,
            "participant_type": participant_type,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if statuses is not None:
            input_["statuses"] = statuses
        if associated_resource_identifiers is not None:
            input_["associated_resource_identifiers"] = associated_resource_identifiers
        if handshake_type_filters is not None:
            input_["handshake_type_filters"] = handshake_type_filters
        if handshake_type_sort is not None:
            input_["handshake_type_sort"] = handshake_type_sort
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_channel_handshakes(
        self,
        handshake_type: "capo_partnercentral_channel.types.handshake_type.HandshakeType",
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        participant_type: "capo_partnercentral_channel.types.participant_type.ParticipantType",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        statuses: Optional[
            "capo_partnercentral_channel.types.handshake_status_list.HandshakeStatusList"
        ] = None,
        associated_resource_identifiers: Optional[
            "capo_partnercentral_channel.types.associated_resource_identifier_list.AssociatedResourceIdentifierList"
        ] = None,
        handshake_type_filters: Optional[
            "capo_partnercentral_channel.types.list_channel_handshakes_type_filters.ListChannelHandshakesTypeFilters"
        ] = None,
        handshake_type_sort: Optional[
            "capo_partnercentral_channel.types.list_channel_handshakes_type_sort.ListChannelHandshakesTypeSort"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_partnercentral_channel.types.channel_handshake_summary.ChannelHandshakeSummary]":
        _token = next_token
        while True:
            _response = self.list_channel_handshakes(
                handshake_type,
                catalog,
                participant_type,
                config_overrides=config_overrides,
                max_results=max_results,
                statuses=statuses,
                associated_resource_identifiers=associated_resource_identifiers,
                handshake_type_filters=handshake_type_filters,
                handshake_type_sort=handshake_type_sort,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def accept_channel_handshake(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "capo_partnercentral_channel.types.accept_channel_handshake_response.AcceptChannelHandshakeResponse":
        """<p>Accepts a pending channel handshake request from another AWS account.</p>

        Args:
            catalog: <p>The catalog identifier for the handshake request.</p>
            identifier: <p>The unique identifier of the channel handshake to accept.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for AcceptChannelHandshake

            >>> client.accept_channel_handshake(catalog='AWS', identifier='ch-4fj3bd2o3vb91')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.accept_channel_handshake_request.AcceptChannelHandshakeRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.accept_channel_handshake_response.AcceptChannelHandshakeResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.accept_channel_handshake

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.accept_channel_handshake.accept_channel_handshake(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.accept_channel_handshake_request.AcceptChannelHandshakeRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_channel_handshake(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "capo_partnercentral_channel.types.cancel_channel_handshake_response.CancelChannelHandshakeResponse":
        """<p>Cancels a pending channel handshake request.</p>

        Args:
            catalog: <p>The catalog identifier for the handshake request.</p>
            identifier: <p>The unique identifier of the channel handshake to cancel.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for CancelChannelHandshake

            >>> client.cancel_channel_handshake(catalog='AWS', identifier='ch-4fj3bd2o3vb91')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.cancel_channel_handshake_request.CancelChannelHandshakeRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.cancel_channel_handshake_response.CancelChannelHandshakeResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.cancel_channel_handshake

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.cancel_channel_handshake.cancel_channel_handshake(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.cancel_channel_handshake_request.CancelChannelHandshakeRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_channel_handshake(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "capo_partnercentral_channel.types.reject_channel_handshake_response.RejectChannelHandshakeResponse":
        """<p>Rejects a pending channel handshake request.</p>

        Args:
            catalog: <p>The catalog identifier for the handshake request.</p>
            identifier: <p>The unique identifier of the channel handshake to reject.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for RejectChannelHandshake

            >>> client.reject_channel_handshake(catalog='AWS', identifier='ch-4fj3bd2o3vb91')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.reject_channel_handshake_request.RejectChannelHandshakeRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.reject_channel_handshake_response.RejectChannelHandshakeResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.reject_channel_handshake

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.reject_channel_handshake.reject_channel_handshake(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.reject_channel_handshake_request.RejectChannelHandshakeRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_program_management_account(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        program: "capo_partnercentral_channel.types.program.Program",
        display_name: "capo_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName",
        account_id: "capo_partnercentral_channel.types.account_id.AccountId",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_channel.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_channel.types.create_program_management_account_response.CreateProgramManagementAccountResponse":
        """<p>Creates a new program management account for managing partner relationships.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            program: <p>The program type for the management account.</p>
            display_name: <p>A human-readable name for the program management account.</p>
            account_id: <p>The AWS account ID to associate with the program management account.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Key-value pairs to associate with the program management account.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for CreateProgramManagementAccount

            >>> client.create_program_management_account(catalog='AWS', program='SOLUTION_PROVIDER', display_name='TestDisplayName', account_id='111122223333', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.create_program_management_account_request.CreateProgramManagementAccountRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.create_program_management_account_response.CreateProgramManagementAccountResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.create_program_management_account

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.create_program_management_account.create_program_management_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.create_program_management_account_request.CreateProgramManagementAccountRequest = {
            "catalog": catalog,
            "program": program,
            "display_name": display_name,
            "account_id": account_id,
        }
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

    def update_program_management_account(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        revision: Optional[
            "capo_partnercentral_channel.types.revision.Revision"
        ] = None,
        display_name: Optional[
            "capo_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
        ] = None,
    ) -> "capo_partnercentral_channel.types.update_program_management_account_response.UpdateProgramManagementAccountResponse":
        """<p>Updates the properties of a program management account.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            identifier: <p>The unique identifier of the program management account to update.</p>
            revision: <p>The current revision number of the program management account.</p>
            display_name: <p>The new display name for the program management account.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for UpdateProgramManagementAccount

            >>> client.update_program_management_account(catalog='AWS', identifier='pma-u8ic702rtzng8', revision='3', display_name='TestDisplayName')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.update_program_management_account_request.UpdateProgramManagementAccountRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.update_program_management_account_response.UpdateProgramManagementAccountResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.update_program_management_account

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.update_program_management_account.update_program_management_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.update_program_management_account_request.UpdateProgramManagementAccountRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision
        if display_name is not None:
            input_["display_name"] = display_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_program_management_account(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.delete_program_management_account_response.DeleteProgramManagementAccountResponse":
        """<p>Deletes a program management account.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            identifier: <p>The unique identifier of the program management account to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for DeleteProgramManagementAccount

            >>> client.delete_program_management_account(catalog='AWS', identifier='pma-u8ic702rtzng8', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.delete_program_management_account_request.DeleteProgramManagementAccountRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.delete_program_management_account_response.DeleteProgramManagementAccountResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.delete_program_management_account

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.delete_program_management_account.delete_program_management_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.delete_program_management_account_request.DeleteProgramManagementAccountRequest = {
            "catalog": catalog,
            "identifier": identifier,
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

    def list_program_management_accounts(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        display_names: Optional[
            "capo_partnercentral_channel.types.program_management_account_display_name_list.ProgramManagementAccountDisplayNameList"
        ] = None,
        programs: Optional[
            "capo_partnercentral_channel.types.program_list.ProgramList"
        ] = None,
        account_ids: Optional[
            "capo_partnercentral_channel.types.account_id_list.AccountIdList"
        ] = None,
        statuses: Optional[
            "capo_partnercentral_channel.types.program_management_account_status_list.ProgramManagementAccountStatusList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_channel.types.list_program_management_accounts_sort_base.ListProgramManagementAccountsSortBase"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.list_program_management_accounts_response.ListProgramManagementAccountsResponse":
        """<p>Lists program management accounts based on specified criteria.</p>

        Args:
            catalog: <p>The catalog identifier to filter accounts.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            display_names: <p>Filter by display names.</p>
            programs: <p>Filter by program types.</p>
            account_ids: <p>Filter by AWS account IDs.</p>
            statuses: <p>Filter by program management account statuses.</p>
            sort: <p>Sorting options for the results.</p>
            next_token: <p>Token for retrieving the next page of results.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListProgramManagementAccounts

            >>> client.list_program_management_accounts(catalog='AWS', max_results=20, programs=['SOLUTION_PROVIDER'], display_names=['TestDisplayName'], account_ids=['111122223333'], statuses=['PENDING'], sort={'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'})
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.list_program_management_accounts_request.ListProgramManagementAccountsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.list_program_management_accounts_response.ListProgramManagementAccountsResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.list_program_management_accounts

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.list_program_management_accounts.list_program_management_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.list_program_management_accounts_request.ListProgramManagementAccountsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if display_names is not None:
            input_["display_names"] = display_names
        if programs is not None:
            input_["programs"] = programs
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if statuses is not None:
            input_["statuses"] = statuses
        if sort is not None:
            input_["sort"] = sort
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_program_management_accounts(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        display_names: Optional[
            "capo_partnercentral_channel.types.program_management_account_display_name_list.ProgramManagementAccountDisplayNameList"
        ] = None,
        programs: Optional[
            "capo_partnercentral_channel.types.program_list.ProgramList"
        ] = None,
        account_ids: Optional[
            "capo_partnercentral_channel.types.account_id_list.AccountIdList"
        ] = None,
        statuses: Optional[
            "capo_partnercentral_channel.types.program_management_account_status_list.ProgramManagementAccountStatusList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_channel.types.list_program_management_accounts_sort_base.ListProgramManagementAccountsSortBase"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_partnercentral_channel.types.program_management_account_summary.ProgramManagementAccountSummary]":
        _token = next_token
        while True:
            _response = self.list_program_management_accounts(
                catalog,
                config_overrides=config_overrides,
                max_results=max_results,
                display_names=display_names,
                programs=programs,
                account_ids=account_ids,
                statuses=statuses,
                sort=sort,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_relationship(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        association_type: "capo_partnercentral_channel.types.association_type.AssociationType",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        associated_account_id: "capo_partnercentral_channel.types.account_id.AccountId",
        display_name: "capo_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName",
        sector: "capo_partnercentral_channel.types.sector.Sector",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        resale_account_model: Optional[
            "capo_partnercentral_channel.types.resale_account_model.ResaleAccountModel"
        ] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_channel.types.tag_list.TagList"] = None,
        requested_support_plan: Optional[
            "capo_partnercentral_channel.types.support_plan.SupportPlan"
        ] = None,
    ) -> "capo_partnercentral_channel.types.create_relationship_response.CreateRelationshipResponse":
        """<p>Creates a new partner relationship between accounts.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            association_type: <p>The type of association for the relationship (e.g., reseller, distributor).</p>
            program_management_account_identifier: <p>The identifier of the program management account for this relationship.</p>
            associated_account_id: <p>The AWS account ID to associate in this relationship.</p>
            display_name: <p>A human-readable name for the relationship.</p>
            resale_account_model: <p>The resale account model for the relationship.</p>
            sector: <p>The business sector for the relationship.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Key-value pairs to associate with the relationship.</p>
            requested_support_plan: <p>The support plan requested for this relationship.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for CreateRelationship

            >>> client.create_relationship(catalog='AWS', association_type='DOWNSTREAM_SELLER', program_management_account_identifier='pma-u8ic702rtzng8', associated_account_id='987654321012', display_name='TestDisplayName', resale_account_model='END_CUSTOMER', sector='COMMERCIAL', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.create_relationship_request.CreateRelationshipRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.create_relationship_response.CreateRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.create_relationship

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.create_relationship.create_relationship(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.create_relationship_request.CreateRelationshipRequest = {
            "catalog": catalog,
            "association_type": association_type,
            "program_management_account_identifier": program_management_account_identifier,
            "associated_account_id": associated_account_id,
            "display_name": display_name,
            "sector": sector,
        }
        if resale_account_model is not None:
            input_["resale_account_model"] = resale_account_model
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if requested_support_plan is not None:
            input_["requested_support_plan"] = requested_support_plan

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_relationship(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "capo_partnercentral_channel.types.get_relationship_response.GetRelationshipResponse":
        """<p>Retrieves details of a specific partner relationship.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            program_management_account_identifier: <p>The identifier of the program management account associated with the relationship.</p>
            identifier: <p>The unique identifier of the relationship to retrieve.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for GetRelationship

            >>> client.get_relationship(catalog='AWS', program_management_account_identifier='pma-u8ic702rtzng8', identifier='rs-l9o4fj3b5zb91')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.get_relationship_request.GetRelationshipRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.get_relationship_response.GetRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.get_relationship

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.get_relationship.get_relationship(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.get_relationship_request.GetRelationshipRequest = {
            "catalog": catalog,
            "program_management_account_identifier": program_management_account_identifier,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_relationship(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        revision: Optional[
            "capo_partnercentral_channel.types.revision.Revision"
        ] = None,
        display_name: Optional[
            "capo_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName"
        ] = None,
        requested_support_plan: Optional[
            "capo_partnercentral_channel.types.support_plan.SupportPlan"
        ] = None,
    ) -> "capo_partnercentral_channel.types.update_relationship_response.UpdateRelationshipResponse":
        """<p>Updates the properties of a partner relationship.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            identifier: <p>The unique identifier of the relationship to update.</p>
            program_management_account_identifier: <p>The identifier of the program management account associated with the relationship.</p>
            revision: <p>The current revision number of the relationship.</p>
            display_name: <p>The new display name for the relationship.</p>
            requested_support_plan: <p>The updated support plan for the relationship.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for UpdateRelationship

            >>> client.update_relationship(catalog='AWS', program_management_account_identifier='pma-u8ic702rtzng8', identifier='rs-l9o4fj3b5zb91', revision='3', display_name='TestDisplayName')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.update_relationship_request.UpdateRelationshipRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.update_relationship_response.UpdateRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.update_relationship

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.update_relationship.update_relationship(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.update_relationship_request.UpdateRelationshipRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "program_management_account_identifier": program_management_account_identifier,
        }
        if revision is not None:
            input_["revision"] = revision
        if display_name is not None:
            input_["display_name"] = display_name
        if requested_support_plan is not None:
            input_["requested_support_plan"] = requested_support_plan

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_relationship(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        identifier: "capo_partnercentral_channel.types.relationship_identifier.RelationshipIdentifier",
        program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.delete_relationship_response.DeleteRelationshipResponse":
        """<p>Deletes a partner relationship.</p>

        Args:
            catalog: <p>The catalog identifier for the relationship.</p>
            identifier: <p>The unique identifier of the relationship to delete.</p>
            program_management_account_identifier: <p>The identifier of the program management account associated with the relationship.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for DeleteRelationship

            >>> client.delete_relationship(catalog='AWS', program_management_account_identifier='pma-u8ic702rtzng8', identifier='rs-l9o4fj3b5zb91', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.delete_relationship_request.DeleteRelationshipRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.delete_relationship_response.DeleteRelationshipResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.delete_relationship

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.delete_relationship.delete_relationship(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.delete_relationship_request.DeleteRelationshipRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "program_management_account_identifier": program_management_account_identifier,
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

    def list_relationships(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        associated_account_ids: Optional[
            "capo_partnercentral_channel.types.account_id_list.AccountIdList"
        ] = None,
        association_types: Optional[
            "capo_partnercentral_channel.types.association_type_list.AssociationTypeList"
        ] = None,
        display_names: Optional[
            "capo_partnercentral_channel.types.relationship_display_name_list.RelationshipDisplayNameList"
        ] = None,
        program_management_account_identifiers: Optional[
            "capo_partnercentral_channel.types.program_management_account_identifier_list.ProgramManagementAccountIdentifierList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_channel.types.list_relationships_sort_base.ListRelationshipsSortBase"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_channel.types.list_relationships_response.ListRelationshipsResponse":
        """<p>Lists partner relationships based on specified criteria.</p>

        Args:
            catalog: <p>The catalog identifier to filter relationships.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            associated_account_ids: <p>Filter by associated AWS account IDs.</p>
            association_types: <p>Filter by association types.</p>
            display_names: <p>Filter by display names.</p>
            program_management_account_identifiers: <p>Filter by program management account identifiers.</p>
            sort: <p>Sorting options for the results.</p>
            next_token: <p>Token for retrieving the next page of results.</p>

        Raises:
            capo_partnercentral_channel.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions.</p>
            capo_partnercentral_channel.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request.</p>
            capo_partnercentral_channel.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_partnercentral_channel.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period.</p>
            capo_partnercentral_channel.errors.validation_exception.ValidationException: <p>The request failed validation due to invalid input parameters.</p>
            capo_partnercentral_channel.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example for ListRelationships

            >>> client.list_relationships(catalog='AWS', max_results=100, associated_account_ids=['123456789012'], association_types=['DOWNSTREAM_SELLER'], display_names=['TestDisplayName'], program_management_account_identifiers=['pma-u8ic702rtzng8'], sort={'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}, next_token='nextToken')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_channel.types.list_relationships_request.ListRelationshipsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_channel.types.list_relationships_response.ListRelationshipsResponse"
        ]:
            import capo_partnercentral_channel._operations.partner_central_channel.list_relationships

            output, http_response = (
                capo_partnercentral_channel._operations.partner_central_channel.list_relationships.list_relationships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_channel.types.list_relationships_request.ListRelationshipsRequest = {
            "catalog": catalog
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if associated_account_ids is not None:
            input_["associated_account_ids"] = associated_account_ids
        if association_types is not None:
            input_["association_types"] = association_types
        if display_names is not None:
            input_["display_names"] = display_names
        if program_management_account_identifiers is not None:
            input_["program_management_account_identifiers"] = (
                program_management_account_identifiers
            )
        if sort is not None:
            input_["sort"] = sort
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_relationships(
        self,
        catalog: "capo_partnercentral_channel.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        associated_account_ids: Optional[
            "capo_partnercentral_channel.types.account_id_list.AccountIdList"
        ] = None,
        association_types: Optional[
            "capo_partnercentral_channel.types.association_type_list.AssociationTypeList"
        ] = None,
        display_names: Optional[
            "capo_partnercentral_channel.types.relationship_display_name_list.RelationshipDisplayNameList"
        ] = None,
        program_management_account_identifiers: Optional[
            "capo_partnercentral_channel.types.program_management_account_identifier_list.ProgramManagementAccountIdentifierList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_channel.types.list_relationships_sort_base.ListRelationshipsSortBase"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_partnercentral_channel.types.relationship_summary.RelationshipSummary]":
        _token = next_token
        while True:
            _response = self.list_relationships(
                catalog,
                config_overrides=config_overrides,
                max_results=max_results,
                associated_account_ids=associated_account_ids,
                association_types=association_types,
                display_names=display_names,
                program_management_account_identifiers=program_management_account_identifiers,
                sort=sort,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
