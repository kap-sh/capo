"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PartnerCentralAccount``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_partnercentral_account._auth._signers
import capo_partnercentral_account._auth._sigv4
from capo_partnercentral_account._auth._identity import Credentials
from capo_partnercentral_account._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_partnercentral_account._auth._zapros_handler import AuthMiddleware
from capo_partnercentral_account._pagination import resolve_path as _resolve_path
from capo_partnercentral_account._resources.partner_central_account.connection_invitation import (
    AsyncConnectionInvitation,
)
from capo_partnercentral_account._resources.partner_central_account.connection_preferences import (
    AsyncConnectionPreferences,
)
from capo_partnercentral_account._resources.partner_central_account.connection_resource import (
    AsyncConnectionResource,
)
from capo_partnercentral_account._resources.partner_central_account.partner import (
    AsyncPartner,
)
from capo_partnercentral_account._services._aws_config import aaws_config
from capo_partnercentral_account._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_partnercentral_account.types.accept_connection_invitation_request
    import capo_partnercentral_account.types.accept_connection_invitation_response
    import capo_partnercentral_account.types.access_type
    import capo_partnercentral_account.types.alliance_lead_contact
    import capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request
    import capo_partnercentral_account.types.associate_aws_training_certification_email_domain_response
    import capo_partnercentral_account.types.cancel_connection_invitation_request
    import capo_partnercentral_account.types.cancel_connection_invitation_response
    import capo_partnercentral_account.types.cancel_connection_request
    import capo_partnercentral_account.types.cancel_connection_response
    import capo_partnercentral_account.types.cancel_profile_update_task_request
    import capo_partnercentral_account.types.cancel_profile_update_task_response
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.connection_id
    import capo_partnercentral_account.types.connection_invitation_id
    import capo_partnercentral_account.types.connection_invitation_summary
    import capo_partnercentral_account.types.connection_summary
    import capo_partnercentral_account.types.connection_type
    import capo_partnercentral_account.types.connection_type_filter
    import capo_partnercentral_account.types.create_connection_invitation_request
    import capo_partnercentral_account.types.create_connection_invitation_response
    import capo_partnercentral_account.types.create_partner_request
    import capo_partnercentral_account.types.create_partner_response
    import capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request
    import capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response
    import capo_partnercentral_account.types.domain_name
    import capo_partnercentral_account.types.email
    import capo_partnercentral_account.types.email_verification_code
    import capo_partnercentral_account.types.get_alliance_lead_contact_request
    import capo_partnercentral_account.types.get_alliance_lead_contact_response
    import capo_partnercentral_account.types.get_connection_invitation_request
    import capo_partnercentral_account.types.get_connection_invitation_response
    import capo_partnercentral_account.types.get_connection_preferences_request
    import capo_partnercentral_account.types.get_connection_preferences_response
    import capo_partnercentral_account.types.get_connection_request
    import capo_partnercentral_account.types.get_connection_response
    import capo_partnercentral_account.types.get_partner_request
    import capo_partnercentral_account.types.get_partner_response
    import capo_partnercentral_account.types.get_profile_update_task_request
    import capo_partnercentral_account.types.get_profile_update_task_response
    import capo_partnercentral_account.types.get_profile_visibility_request
    import capo_partnercentral_account.types.get_profile_visibility_response
    import capo_partnercentral_account.types.get_qualifications_association_details_request
    import capo_partnercentral_account.types.get_qualifications_association_details_response
    import capo_partnercentral_account.types.get_qualifications_association_task_request
    import capo_partnercentral_account.types.get_qualifications_association_task_response
    import capo_partnercentral_account.types.get_qualifications_disassociation_task_request
    import capo_partnercentral_account.types.get_qualifications_disassociation_task_response
    import capo_partnercentral_account.types.get_verification_request
    import capo_partnercentral_account.types.get_verification_response
    import capo_partnercentral_account.types.invitation_status
    import capo_partnercentral_account.types.list_connection_invitations_request
    import capo_partnercentral_account.types.list_connection_invitations_response
    import capo_partnercentral_account.types.list_connections_request
    import capo_partnercentral_account.types.list_connections_response
    import capo_partnercentral_account.types.list_partners_request
    import capo_partnercentral_account.types.list_partners_response
    import capo_partnercentral_account.types.list_tags_for_resource_request
    import capo_partnercentral_account.types.list_tags_for_resource_response
    import capo_partnercentral_account.types.max_results
    import capo_partnercentral_account.types.next_token
    import capo_partnercentral_account.types.participant_identifier
    import capo_partnercentral_account.types.participant_identifier_list
    import capo_partnercentral_account.types.participant_type
    import capo_partnercentral_account.types.partner_identifier
    import capo_partnercentral_account.types.partner_summary
    import capo_partnercentral_account.types.primary_solution_type
    import capo_partnercentral_account.types.profile_task_id
    import capo_partnercentral_account.types.profile_visibility
    import capo_partnercentral_account.types.put_alliance_lead_contact_request
    import capo_partnercentral_account.types.put_alliance_lead_contact_response
    import capo_partnercentral_account.types.put_profile_visibility_request
    import capo_partnercentral_account.types.put_profile_visibility_response
    import capo_partnercentral_account.types.qualifications_association_partner
    import capo_partnercentral_account.types.reject_connection_invitation_request
    import capo_partnercentral_account.types.reject_connection_invitation_response
    import capo_partnercentral_account.types.revision
    import capo_partnercentral_account.types.send_email_verification_code_request
    import capo_partnercentral_account.types.send_email_verification_code_response
    import capo_partnercentral_account.types.sensitive_unicode_string
    import capo_partnercentral_account.types.start_profile_update_task_request
    import capo_partnercentral_account.types.start_profile_update_task_response
    import capo_partnercentral_account.types.start_qualifications_association_task_request
    import capo_partnercentral_account.types.start_qualifications_association_task_response
    import capo_partnercentral_account.types.start_qualifications_disassociation_task_request
    import capo_partnercentral_account.types.start_qualifications_disassociation_task_response
    import capo_partnercentral_account.types.start_verification_request
    import capo_partnercentral_account.types.start_verification_response
    import capo_partnercentral_account.types.tag_key_list
    import capo_partnercentral_account.types.tag_list
    import capo_partnercentral_account.types.tag_resource_request
    import capo_partnercentral_account.types.tag_resource_response
    import capo_partnercentral_account.types.taggable_resource_arn
    import capo_partnercentral_account.types.task_details
    import capo_partnercentral_account.types.unicode_string_including_new_line
    import capo_partnercentral_account.types.untag_resource_request
    import capo_partnercentral_account.types.untag_resource_response
    import capo_partnercentral_account.types.update_connection_preferences_request
    import capo_partnercentral_account.types.update_connection_preferences_response
    import capo_partnercentral_account.types.verification_details
    import capo_partnercentral_account.types.verification_type


class AsyncPartnerCentralAccountClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncPartnerCentralAccountClient:
    """A client for the ``PartnerCentralAccount`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncPartnerCentralAccountClientConfig(
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
        self.connection_invitation = AsyncConnectionInvitation(self)
        self.connection_preferences = AsyncConnectionPreferences(self)
        self.connection_resource = AsyncConnectionResource(self)
        self.partner = AsyncPartner(self)

    def operation_options(
        self, config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPartnerCentralAccountClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def get_verification(
        self,
        verification_type: "capo_partnercentral_account.types.verification_type.VerificationType",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_verification_response.GetVerificationResponse":
        """<p>Retrieves the current status and details of a verification process for a partner account. This operation allows partners to check the progress and results of business or registrant verification processes.</p>

        Args:
            verification_type: <p>The type of verification to retrieve information for. Valid values include business verification for company registration details and registrant verification for individual identity confirmation.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_verification_request.GetVerificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_verification_response.GetVerificationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_verification

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_verification.async_get_verification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_verification_request.GetVerificationRequest = {
            "verification_type": verification_type
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_partnercentral_account.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with a specific AWS Partner Central Account resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_email_verification_code(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        email: "capo_partnercentral_account.types.email.Email",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.send_email_verification_code_response.SendEmailVerificationCodeResponse":
        """<p>Sends an email verification code to the specified email address for account verification purposes.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            email: <p>The email address to send the verification code to.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.send_email_verification_code_request.SendEmailVerificationCodeRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.send_email_verification_code_response.SendEmailVerificationCodeResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.send_email_verification_code

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.send_email_verification_code.async_send_email_verification_code(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.send_email_verification_code_request.SendEmailVerificationCodeRequest = {
            "catalog": catalog,
            "email": email,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_verification(
        self,
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
        verification_details: Optional[
            "capo_partnercentral_account.types.verification_details.VerificationDetails"
        ] = None,
    ) -> "capo_partnercentral_account.types.start_verification_response.StartVerificationResponse":
        """<p>Initiates a new verification process for a partner account. This operation begins the verification workflow for either business registration or individual registrant identity verification as required by AWS Partner Central.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This prevents duplicate verification processes from being started accidentally.</p>
            verification_details: <p>The specific details required for the verification process, including business information for business verification or personal information for registrant verification.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.start_verification_request.StartVerificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.start_verification_response.StartVerificationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.start_verification

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.start_verification.async_start_verification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.start_verification_request.StartVerificationRequest = {}
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if verification_details is not None:
            input_["verification_details"] = verification_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_partnercentral_account.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_partnercentral_account.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for a specified AWS Partner Central Account resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>A list of tags to add or update for the specified resource.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.tag_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_partnercentral_account.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_partnercentral_account.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes specified tags from an AWS Partner Central Account resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>A list of tag keys to remove from the specified resource.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.untag_resource

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_connection_invitation(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        connection_type: "capo_partnercentral_account.types.connection_type.ConnectionType",
        email: "capo_partnercentral_account.types.email.Email",
        message: "capo_partnercentral_account.types.unicode_string_including_new_line.UnicodeStringIncludingNewLine",
        name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString",
        receiver_identifier: "capo_partnercentral_account.types.participant_identifier.ParticipantIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse":
        """<p>Creates a new connection invitation to establish a partnership with another organization.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation will be created.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            connection_type: <p>The type of connection being requested (e.g., reseller, distributor, technology partner).</p>
            email: <p>The email address of the person to send the connection invitation to.</p>
            message: <p>A custom message to include with the connection invitation.</p>
            name: <p>The name of the person sending the connection invitation.</p>
            receiver_identifier: <p>The identifier of the organization or partner to invite for connection.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.create_connection_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.create_connection_invitation.async_create_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "connection_type": connection_type,
            "email": email,
            "message": message,
            "name": name,
            "receiver_identifier": receiver_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connection_invitation(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse":
        """<p>Retrieves detailed information about a specific connection invitation.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to retrieve.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_connection_invitation_request.GetConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_connection_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_connection_invitation.async_get_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_connection_invitation_request.GetConnectionInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_connection_invitations(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "capo_partnercentral_account.types.next_token.NextToken"
        ] = None,
        connection_type: Optional[
            "capo_partnercentral_account.types.connection_type.ConnectionType"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_account.types.max_results.MaxResults"
        ] = None,
        other_participant_identifiers: Optional[
            "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
        participant_type: Optional[
            "capo_partnercentral_account.types.participant_type.ParticipantType"
        ] = None,
        status: Optional[
            "capo_partnercentral_account.types.invitation_status.InvitationStatus"
        ] = None,
    ) -> "capo_partnercentral_account.types.list_connection_invitations_response.ListConnectionInvitationsResponse":
        """<p>Lists connection invitations for the partner account, with optional filtering by status, type, and other criteria.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>
            connection_type: <p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>
            max_results: <p>The maximum number of connection invitations to return in a single response.</p>
            other_participant_identifiers: <p>Filter results by specific participant identifiers.</p>
            participant_type: <p>Filter results by participant type (inviter or invitee).</p>
            status: <p>Filter results by invitation status (pending, accepted, rejected, canceled, expired).</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.list_connection_invitations_request.ListConnectionInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.list_connection_invitations_response.ListConnectionInvitationsResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.list_connection_invitations

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.list_connection_invitations.async_list_connection_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.list_connection_invitations_request.ListConnectionInvitationsRequest = {
            "catalog": catalog
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if connection_type is not None:
            input_["connection_type"] = connection_type
        if max_results is not None:
            input_["max_results"] = max_results
        if other_participant_identifiers is not None:
            input_["other_participant_identifiers"] = other_participant_identifiers
        if participant_type is not None:
            input_["participant_type"] = participant_type
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_connection_invitations(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "capo_partnercentral_account.types.next_token.NextToken"
        ] = None,
        connection_type: Optional[
            "capo_partnercentral_account.types.connection_type.ConnectionType"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_account.types.max_results.MaxResults"
        ] = None,
        other_participant_identifiers: Optional[
            "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
        participant_type: Optional[
            "capo_partnercentral_account.types.participant_type.ParticipantType"
        ] = None,
        status: Optional[
            "capo_partnercentral_account.types.invitation_status.InvitationStatus"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_account.types.connection_invitation_summary.ConnectionInvitationSummary]":
        _token = next_token
        while True:
            _response = await self.list_connection_invitations(
                catalog,
                config_overrides=config_overrides,
                next_token=_token,
                connection_type=connection_type,
                max_results=max_results,
                other_participant_identifiers=other_participant_identifiers,
                participant_type=participant_type,
                status=status,
            )
            _page = _resolve_path(_response, ("connection_invitation_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def accept_connection_invitation(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse":
        """<p>Accepts a connection invitation from another partner, establishing a formal partnership connection between the two parties.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to accept.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.accept_connection_invitation_request.AcceptConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.accept_connection_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.accept_connection_invitation.async_accept_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.accept_connection_invitation_request.AcceptConnectionInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_connection_invitation(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse":
        """<p>Cancels a pending connection invitation before it has been accepted or rejected.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to cancel.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.cancel_connection_invitation_request.CancelConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.cancel_connection_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.cancel_connection_invitation.async_cancel_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.cancel_connection_invitation_request.CancelConnectionInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_connection_invitation(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        reason: Optional[str] = None,
    ) -> "capo_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse":
        """<p>Rejects a connection invitation from another partner, declining the partnership request.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to reject.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            reason: <p>The reason for rejecting the connection invitation.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.reject_connection_invitation_request.RejectConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.reject_connection_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.reject_connection_invitation.async_reject_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.reject_connection_invitation_request.RejectConnectionInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "client_token": client_token,
        }
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connection_preferences(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_connection_preferences_response.GetConnectionPreferencesResponse":
        """<p>Retrieves the connection preferences for a partner account, including access settings and exclusions.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_connection_preferences_request.GetConnectionPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_connection_preferences_response.GetConnectionPreferencesResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_connection_preferences

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_connection_preferences.async_get_connection_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_connection_preferences_request.GetConnectionPreferencesRequest = {
            "catalog": catalog
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connection_preferences(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        revision: "capo_partnercentral_account.types.revision.Revision",
        access_type: "capo_partnercentral_account.types.access_type.AccessType",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        excluded_participant_identifiers: Optional[
            "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
    ) -> "capo_partnercentral_account.types.update_connection_preferences_response.UpdateConnectionPreferencesResponse":
        """<p>Updates the connection preferences for a partner account, modifying access settings and exclusions.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            revision: <p>The revision number of the connection preferences for optimistic locking.</p>
            access_type: <p>The access type setting for connections (e.g., open, restricted, invitation-only).</p>
            excluded_participant_identifiers: <p>The updated list of participant identifiers to exclude from connections.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.update_connection_preferences_request.UpdateConnectionPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.update_connection_preferences_response.UpdateConnectionPreferencesResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.update_connection_preferences

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.update_connection_preferences.async_update_connection_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.update_connection_preferences_request.UpdateConnectionPreferencesRequest = {
            "catalog": catalog,
            "revision": revision,
            "access_type": access_type,
        }
        if excluded_participant_identifiers is not None:
            input_["excluded_participant_identifiers"] = (
                excluded_participant_identifiers
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connection(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_connection_response.GetConnectionResponse":
        """<p>Retrieves detailed information about a specific connection between partners.</p>

        Args:
            catalog: <p>The catalog identifier where the connection exists.</p>
            identifier: <p>The unique identifier of the connection to retrieve.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_connection_request.GetConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_connection_response.GetConnectionResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_connection

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_connection.async_get_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_connection_request.GetConnectionRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_connections(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "capo_partnercentral_account.types.next_token.NextToken"
        ] = None,
        connection_type: Optional[
            "capo_partnercentral_account.types.connection_type_filter.ConnectionTypeFilter"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_account.types.max_results.MaxResults"
        ] = None,
        other_participant_identifiers: Optional[
            "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
    ) -> "capo_partnercentral_account.types.list_connections_response.ListConnectionsResponse":
        """<p>Lists active connections for the partner account, with optional filtering by connection type and participant.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>
            connection_type: <p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>
            max_results: <p>The maximum number of connections to return in a single response.</p>
            other_participant_identifiers: <p>Filter results by specific participant identifiers.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.list_connections_request.ListConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.list_connections_response.ListConnectionsResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.list_connections

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.list_connections.async_list_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.list_connections_request.ListConnectionsRequest = {
            "catalog": catalog
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if connection_type is not None:
            input_["connection_type"] = connection_type
        if max_results is not None:
            input_["max_results"] = max_results
        if other_participant_identifiers is not None:
            input_["other_participant_identifiers"] = other_participant_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_connections(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "capo_partnercentral_account.types.next_token.NextToken"
        ] = None,
        connection_type: Optional[
            "capo_partnercentral_account.types.connection_type_filter.ConnectionTypeFilter"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_account.types.max_results.MaxResults"
        ] = None,
        other_participant_identifiers: Optional[
            "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_account.types.connection_summary.ConnectionSummary]":
        _token = next_token
        while True:
            _response = await self.list_connections(
                catalog,
                config_overrides=config_overrides,
                next_token=_token,
                connection_type=connection_type,
                max_results=max_results,
                other_participant_identifiers=other_participant_identifiers,
            )
            _page = _resolve_path(_response, ("connection_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def cancel_connection(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_id.ConnectionId",
        connection_type: "capo_partnercentral_account.types.connection_type.ConnectionType",
        reason: str,
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.cancel_connection_response.CancelConnectionResponse":
        """<p>Cancels an existing connection between partners, terminating the partnership relationship.</p>

        Args:
            catalog: <p>The catalog identifier where the connection exists.</p>
            identifier: <p>The unique identifier of the connection to cancel.</p>
            connection_type: <p>The type of connection to cancel (e.g., reseller, distributor, technology partner).</p>
            reason: <p>The reason for canceling the connection, providing context for the termination.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.cancel_connection_request.CancelConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.cancel_connection_response.CancelConnectionResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.cancel_connection

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.cancel_connection.async_cancel_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.cancel_connection_request.CancelConnectionRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "connection_type": connection_type,
            "reason": reason,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_partner(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        legal_name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString",
        primary_solution_type: "capo_partnercentral_account.types.primary_solution_type.PrimarySolutionType",
        alliance_lead_contact: "capo_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact",
        email_verification_code: "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_account.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_account.types.create_partner_response.CreatePartnerResponse":
        """<p>Creates a new partner account in the AWS Partner Network with the specified details and configuration.</p>

        Args:
            catalog: <p>The catalog identifier where the partner account will be created.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            legal_name: <p>The legal name of the organization becoming a partner.</p>
            primary_solution_type: <p>The primary type of solution or service the partner provides (e.g., consulting, software, managed services).</p>
            alliance_lead_contact: <p>The primary contact person for alliance and partnership matters.</p>
            email_verification_code: <p>The verification code sent to the alliance lead contact's email to confirm account creation.</p>
            tags: <p>A list of tags to associate with the partner account for organization and billing purposes.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.create_partner_request.CreatePartnerRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.create_partner_response.CreatePartnerResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.create_partner

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.create_partner.async_create_partner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.create_partner_request.CreatePartnerRequest = {
            "catalog": catalog,
            "legal_name": legal_name,
            "primary_solution_type": primary_solution_type,
            "alliance_lead_contact": alliance_lead_contact,
            "email_verification_code": email_verification_code,
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

    async def get_partner(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_partner_response.GetPartnerResponse":
        """<p>Retrieves detailed information about a specific partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account to retrieve.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_partner_request.GetPartnerRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_partner_response.GetPartnerResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_partner

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_partner.async_get_partner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_partner_request.GetPartnerRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_partners(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "capo_partnercentral_account.types.next_token.NextToken"
        ] = None,
    ) -> (
        "capo_partnercentral_account.types.list_partners_response.ListPartnersResponse"
    ):
        """<p>Lists partner accounts in the catalog, providing a summary view of all partners.</p>

        Args:
            catalog: <p>The catalog identifier to list partners from.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.list_partners_request.ListPartnersRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.list_partners_response.ListPartnersResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.list_partners

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.list_partners.async_list_partners(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.list_partners_request.ListPartnersRequest = {
            "catalog": catalog
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_partners(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "capo_partnercentral_account.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_partnercentral_account.types.partner_summary.PartnerSummary]":
        _token = next_token
        while True:
            _response = await self.list_partners(
                catalog,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("partner_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def associate_aws_training_certification_email_domain(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        email: "capo_partnercentral_account.types.email.Email",
        email_verification_code: "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.associate_aws_training_certification_email_domain_response.AssociateAwsTrainingCertificationEmailDomainResponse":
        """<p>Associates an email domain with AWS training and certification for the partner account, enabling automatic verification of employee certifications.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            email: <p>The email address used to verify domain ownership for AWS training and certification association.</p>
            email_verification_code: <p>The verification code sent to the email address to confirm domain ownership.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.associate_aws_training_certification_email_domain_response.AssociateAwsTrainingCertificationEmailDomainResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.associate_aws_training_certification_email_domain

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.associate_aws_training_certification_email_domain.async_associate_aws_training_certification_email_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "email": email,
            "email_verification_code": email_verification_code,
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

    async def cancel_profile_update_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        task_id: "capo_partnercentral_account.types.profile_task_id.ProfileTaskId",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.cancel_profile_update_task_response.CancelProfileUpdateTaskResponse":
        """<p>Cancels an in-progress profile update task, stopping any pending changes to the partner profile.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            task_id: <p>The unique identifier of the profile update task to cancel.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.cancel_profile_update_task_request.CancelProfileUpdateTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.cancel_profile_update_task_response.CancelProfileUpdateTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.cancel_profile_update_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.cancel_profile_update_task.async_cancel_profile_update_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.cancel_profile_update_task_request.CancelProfileUpdateTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "task_id": task_id,
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

    async def disassociate_aws_training_certification_email_domain(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        domain_name: "capo_partnercentral_account.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response.DisassociateAwsTrainingCertificationEmailDomainResponse":
        """<p>Removes the association between an email domain and AWS training and certification for the partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            domain_name: <p>The domain name to disassociate from AWS training and certification.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request.DisassociateAwsTrainingCertificationEmailDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response.DisassociateAwsTrainingCertificationEmailDomainResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.disassociate_aws_training_certification_email_domain

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.disassociate_aws_training_certification_email_domain.async_disassociate_aws_training_certification_email_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request.DisassociateAwsTrainingCertificationEmailDomainRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "domain_name": domain_name,
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

    async def get_alliance_lead_contact(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse":
        """<p>Retrieves the alliance lead contact information for a partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_alliance_lead_contact_request.GetAllianceLeadContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_alliance_lead_contact

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_alliance_lead_contact.async_get_alliance_lead_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_alliance_lead_contact_request.GetAllianceLeadContactRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_profile_update_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_profile_update_task_response.GetProfileUpdateTaskResponse":
        """<p>Retrieves information about a specific profile update task.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_profile_update_task_request.GetProfileUpdateTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_profile_update_task_response.GetProfileUpdateTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_profile_update_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_profile_update_task.async_get_profile_update_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_profile_update_task_request.GetProfileUpdateTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_profile_visibility(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_profile_visibility_response.GetProfileVisibilityResponse":
        """<p>Retrieves the visibility settings for a partner profile, determining who can see the profile information.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_profile_visibility_request.GetProfileVisibilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_profile_visibility_response.GetProfileVisibilityResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_profile_visibility

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_profile_visibility.async_get_profile_visibility(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_profile_visibility_request.GetProfileVisibilityRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_qualifications_association_details(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_qualifications_association_details_response.GetQualificationsAssociationDetailsResponse":
        """<p>Returns your current qualifications association status, the primary partner, and the full list of partners associated under the primary partner.</p>

        Args:
            catalog: <p>The catalog in which to look up the qualifications association. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_qualifications_association_details_request.GetQualificationsAssociationDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_qualifications_association_details_response.GetQualificationsAssociationDetailsResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_details

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_details.async_get_qualifications_association_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_qualifications_association_details_request.GetQualificationsAssociationDetailsRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_qualifications_association_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_qualifications_association_task_response.GetQualificationsAssociationTaskResponse":
        """<p>Retrieves the status and details of the most recent qualifications association task for your partner account. Use this operation to poll the progress of an association task initiated by <code>StartQualificationsAssociationTask</code>.</p>

        Args:
            catalog: <p>The catalog in which to look up the qualifications association task. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_qualifications_association_task_request.GetQualificationsAssociationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_qualifications_association_task_response.GetQualificationsAssociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_task.async_get_qualifications_association_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_qualifications_association_task_request.GetQualificationsAssociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_qualifications_disassociation_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_qualifications_disassociation_task_response.GetQualificationsDisassociationTaskResponse":
        """<p>Retrieves the status and details of the most recent qualifications disassociation task for your partner account. Use this operation to poll the progress of a disassociation task initiated by <code>StartQualificationsDisassociationTask</code>.</p>

        Args:
            catalog: <p>The catalog in which to look up the qualifications disassociation task. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_qualifications_disassociation_task_request.GetQualificationsDisassociationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_qualifications_disassociation_task_response.GetQualificationsDisassociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_qualifications_disassociation_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_qualifications_disassociation_task.async_get_qualifications_disassociation_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_qualifications_disassociation_task_request.GetQualificationsDisassociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_alliance_lead_contact(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        alliance_lead_contact: "capo_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        email_verification_code: Optional[
            "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode"
        ] = None,
    ) -> "capo_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse":
        """<p>Creates or updates the alliance lead contact information for a partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            alliance_lead_contact: <p>The alliance lead contact information to set for the partner account.</p>
            email_verification_code: <p>The verification code sent to the alliance lead contact's email to confirm the update.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.put_alliance_lead_contact

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.put_alliance_lead_contact.async_put_alliance_lead_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "alliance_lead_contact": alliance_lead_contact,
        }
        if email_verification_code is not None:
            input_["email_verification_code"] = email_verification_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_profile_visibility(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        visibility: "capo_partnercentral_account.types.profile_visibility.ProfileVisibility",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.put_profile_visibility_response.PutProfileVisibilityResponse":
        """<p>Sets the visibility level for a partner profile, controlling who can view the profile information.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            visibility: <p>The visibility setting to apply to the partner profile.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.put_profile_visibility_request.PutProfileVisibilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.put_profile_visibility_response.PutProfileVisibilityResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.put_profile_visibility

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.put_profile_visibility.async_put_profile_visibility(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.put_profile_visibility_request.PutProfileVisibilityRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "visibility": visibility,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_profile_update_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        task_details: "capo_partnercentral_account.types.task_details.TaskDetails",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.start_profile_update_task_response.StartProfileUpdateTaskResponse":
        """<p>Initiates a profile update task to modify partner profile information asynchronously.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            task_details: <p>The details of the profile updates to be performed.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.start_profile_update_task_request.StartProfileUpdateTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.start_profile_update_task_response.StartProfileUpdateTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.start_profile_update_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.start_profile_update_task.async_start_profile_update_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.start_profile_update_task_request.StartProfileUpdateTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "task_details": task_details,
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

    async def start_qualifications_association_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        primary_partner: "capo_partnercentral_account.types.qualifications_association_partner.QualificationsAssociationPartner",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.start_qualifications_association_task_response.StartQualificationsAssociationTaskResponse":
        """<p>Initiates an asynchronous task to associate your partner qualifications with a primary account. You must be a subsidiary of the primary account with an active subsidiary connection. Use <code>GetQualificationsAssociationTask</code> to monitor task progress.</p>

        Args:
            catalog: <p>The catalog in which to perform the qualifications association. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            primary_partner: <p>The primary (acquiring) partner's profile and account identifier to associate qualifications with. You must provide at least one of <code>ProfileId</code> or <code>AccountId</code>. You cannot specify yourself as the primary partner.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.start_qualifications_association_task_request.StartQualificationsAssociationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.start_qualifications_association_task_response.StartQualificationsAssociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.start_qualifications_association_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.start_qualifications_association_task.async_start_qualifications_association_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.start_qualifications_association_task_request.StartQualificationsAssociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "primary_partner": primary_partner,
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

    async def start_qualifications_disassociation_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        associated_partner: "capo_partnercentral_account.types.qualifications_association_partner.QualificationsAssociationPartner",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.start_qualifications_disassociation_task_response.StartQualificationsDisassociationTaskResponse":
        """<p>Initiates an asynchronous task to disassociate your partner qualifications from a primary account. You must currently be associated and cannot disassociate if you are the primary partner. Use <code>GetQualificationsDisassociationTask</code> to monitor task progress.</p>

        Args:
            catalog: <p>The catalog in which to perform the qualifications disassociation. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            associated_partner: <p>The primary partner's profile and account identifier that you are currently associated with and will disassociate from. You must provide at least one of <code>ProfileId</code> or <code>AccountId</code>. The specified partner must match your current primary association.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.start_qualifications_disassociation_task_request.StartQualificationsDisassociationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.start_qualifications_disassociation_task_response.StartQualificationsDisassociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.start_qualifications_disassociation_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.start_qualifications_disassociation_task.async_start_qualifications_disassociation_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.start_qualifications_disassociation_task_request.StartQualificationsDisassociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "associated_partner": associated_partner,
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
