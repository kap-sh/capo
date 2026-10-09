"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#RolesAnywhere``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_rolesanywhere._auth._signers
import capo_rolesanywhere._auth._sigv4
from capo_rolesanywhere._auth._identity import Credentials
from capo_rolesanywhere._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_rolesanywhere._auth._zapros_handler import AuthMiddleware
from capo_rolesanywhere._pagination import resolve_path as _resolve_path
from capo_rolesanywhere._resources.roles_anywhere.crl import AsyncCrl
from capo_rolesanywhere._resources.roles_anywhere.profile import AsyncProfile
from capo_rolesanywhere._resources.roles_anywhere.subject import AsyncSubject
from capo_rolesanywhere._resources.roles_anywhere.trust_anchor import AsyncTrustAnchor
from capo_rolesanywhere._services._aws_config import aaws_config
from capo_rolesanywhere._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_rolesanywhere.types.amazon_resource_name
    import capo_rolesanywhere.types.certificate_field
    import capo_rolesanywhere.types.create_profile_request
    import capo_rolesanywhere.types.create_trust_anchor_request
    import capo_rolesanywhere.types.crl_detail
    import capo_rolesanywhere.types.crl_detail_response
    import capo_rolesanywhere.types.delete_attribute_mapping_request
    import capo_rolesanywhere.types.delete_attribute_mapping_response
    import capo_rolesanywhere.types.import_crl_request
    import capo_rolesanywhere.types.list_crls_response
    import capo_rolesanywhere.types.list_profiles_response
    import capo_rolesanywhere.types.list_request
    import capo_rolesanywhere.types.list_subjects_response
    import capo_rolesanywhere.types.list_tags_for_resource_request
    import capo_rolesanywhere.types.list_tags_for_resource_response
    import capo_rolesanywhere.types.list_trust_anchors_response
    import capo_rolesanywhere.types.managed_policy_list
    import capo_rolesanywhere.types.mapping_rules
    import capo_rolesanywhere.types.notification_setting_keys
    import capo_rolesanywhere.types.notification_settings
    import capo_rolesanywhere.types.profile_detail
    import capo_rolesanywhere.types.profile_detail_response
    import capo_rolesanywhere.types.put_attribute_mapping_request
    import capo_rolesanywhere.types.put_attribute_mapping_response
    import capo_rolesanywhere.types.put_notification_settings_request
    import capo_rolesanywhere.types.put_notification_settings_response
    import capo_rolesanywhere.types.reset_notification_settings_request
    import capo_rolesanywhere.types.reset_notification_settings_response
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.role_arn_list
    import capo_rolesanywhere.types.scalar_crl_request
    import capo_rolesanywhere.types.scalar_profile_request
    import capo_rolesanywhere.types.scalar_subject_request
    import capo_rolesanywhere.types.scalar_trust_anchor_request
    import capo_rolesanywhere.types.source
    import capo_rolesanywhere.types.specifier_list
    import capo_rolesanywhere.types.subject_detail_response
    import capo_rolesanywhere.types.subject_summary
    import capo_rolesanywhere.types.tag_key_list
    import capo_rolesanywhere.types.tag_list
    import capo_rolesanywhere.types.tag_resource_request
    import capo_rolesanywhere.types.tag_resource_response
    import capo_rolesanywhere.types.trust_anchor_arn
    import capo_rolesanywhere.types.trust_anchor_detail
    import capo_rolesanywhere.types.trust_anchor_detail_response
    import capo_rolesanywhere.types.untag_resource_request
    import capo_rolesanywhere.types.untag_resource_response
    import capo_rolesanywhere.types.update_crl_request
    import capo_rolesanywhere.types.update_profile_request
    import capo_rolesanywhere.types.update_trust_anchor_request
    import capo_rolesanywhere.types.uuid


class AsyncRolesAnywhereClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncRolesAnywhereClient:
    """A client for the ``RolesAnywhere`` service.

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
        self._config = AsyncRolesAnywhereClientConfig(
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
        self.crl = AsyncCrl(self)
        self.profile = AsyncProfile(self)
        self.subject = AsyncSubject(self)
        self.trust_anchor = AsyncTrustAnchor(self)

    def operation_options(
        self, config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRolesAnywhereClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_rolesanywhere.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags attached to the resource.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListTagsForResource</code>. </p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_notification_settings(
        self,
        trust_anchor_id: "capo_rolesanywhere.types.uuid.Uuid",
        notification_settings: "capo_rolesanywhere.types.notification_settings.NotificationSettings",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.put_notification_settings_response.PutNotificationSettingsResponse":
        """<p>Attaches a list of <i>notification settings</i> to a trust anchor.</p> <p>A notification setting includes information such as event name, threshold, status of the notification setting, and the channel to notify.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:PutNotificationSettings</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
            notification_settings: <p>A list of notification settings to be associated to the trust anchor.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            PutNotificationSettings - Adds custom notification settings

            >>> await client.put_notification_settings(trust_anchor_id='c2505e61-2fc1-4a18-9fcf-94e18a22928b', notification_settings=[{'event': 'END_ENTITY_CERTIFICATE_EXPIRY', 'enabled': True, 'threshold': 10}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.put_notification_settings_request.PutNotificationSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.put_notification_settings_response.PutNotificationSettingsResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.put_notification_settings

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.put_notification_settings.async_put_notification_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.put_notification_settings_request.PutNotificationSettingsRequest = {
            "trust_anchor_id": trust_anchor_id,
            "notification_settings": notification_settings,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_notification_settings(
        self,
        trust_anchor_id: "capo_rolesanywhere.types.uuid.Uuid",
        notification_setting_keys: "capo_rolesanywhere.types.notification_setting_keys.NotificationSettingKeys",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.reset_notification_settings_response.ResetNotificationSettingsResponse":
        """<p>Resets the <i>custom notification setting</i> to IAM Roles Anywhere default setting. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:ResetNotificationSettings</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
            notification_setting_keys: <p>A list of notification setting keys to reset. A notification setting key includes the event and the channel. </p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ResetNotificationSettings - Resets to IAM Roles Anywhere defined default notification settings

            >>> await client.reset_notification_settings(trust_anchor_id='c2505e61-2fc1-4a18-9fcf-94e18a22928b', notification_setting_keys=[{'event': 'END_ENTITY_CERTIFICATE_EXPIRY'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.reset_notification_settings_request.ResetNotificationSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.reset_notification_settings_response.ResetNotificationSettingsResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.reset_notification_settings

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.reset_notification_settings.async_reset_notification_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.reset_notification_settings_request.ResetNotificationSettingsRequest = {
            "trust_anchor_id": trust_anchor_id,
            "notification_setting_keys": notification_setting_keys,
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
        resource_arn: "capo_rolesanywhere.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_rolesanywhere.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.tag_resource_response.TagResourceResponse":
        """<p>Attaches tags to a resource.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:TagResource</code>. </p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>The tags to attach to the resource.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.too_many_tags_exception.TooManyTagsException: <p>Too many tags.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.tag_resource

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_rolesanywhere.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_rolesanywhere.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the resource.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UntagResource</code>. </p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>A list of keys. Tag keys are the unique identifiers of tags. </p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.untag_resource

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.untag_resource_request.UntagResourceRequest = {
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

    async def import_crl(
        self,
        name: "capo_rolesanywhere.types.resource_name.ResourceName",
        crl_data: bytes,
        trust_anchor_arn: "capo_rolesanywhere.types.trust_anchor_arn.TrustAnchorArn",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        enabled: Optional[bool] = None,
        tags: Optional["capo_rolesanywhere.types.tag_list.TagList"] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Imports the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate Authority (CA).In order to be properly imported, a CRL must be in PEM format. IAM Roles Anywhere validates against the CRL before issuing credentials. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:ImportCrl</code>. </p>

        Args:
            name: <p>The name of the certificate revocation list (CRL).</p>
            crl_data: <p>The x509 v3 specified certificate revocation list (CRL).</p>
            enabled: <p>Specifies whether the certificate revocation list (CRL) is enabled.</p>
            tags: <p>A list of tags to attach to the certificate revocation list (CRL).</p>
            trust_anchor_arn: <p>The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.import_crl_request.ImportCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.import_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.import_crl.async_import_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.import_crl_request.ImportCrlRequest = {
            "name": name,
            "crl_data": crl_data,
            "trust_anchor_arn": trust_anchor_arn,
        }
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

    async def get_crl(
        self,
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Gets a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.get_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.get_crl.async_get_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_crl(
        self,
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        name: Optional["capo_rolesanywhere.types.resource_name.ResourceName"] = None,
        crl_data: Optional[bytes] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Updates the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate authority (CA). IAM Roles Anywhere validates against the CRL before issuing credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UpdateCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
            name: <p>The name of the Crl.</p>
            crl_data: <p>The x509 v3 specified certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.update_crl_request.UpdateCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.update_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.update_crl.async_update_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.update_crl_request.UpdateCrlRequest = {
            "crl_id": crl_id
        }
        if name is not None:
            input_["name"] = name
        if crl_data is not None:
            input_["crl_data"] = crl_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_crl(
        self,
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Deletes a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DeleteCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.delete_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.delete_crl.async_delete_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_crls(
        self,
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "capo_rolesanywhere.types.list_crls_response.ListCrlsResponse":
        """<p>Lists all certificate revocation lists (CRL) in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListCrls</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.list_request.ListRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.list_crls_response.ListCrlsResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.list_crls

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.list_crls.async_list_crls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.list_request.ListRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_crls(
        self,
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "AsyncIterator[capo_rolesanywhere.types.crl_detail.CrlDetail]":
        _token = next_token
        while True:
            _response = await self.list_crls(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("crls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disable_crl(
        self,
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Disables a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DisableCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.disable_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.disable_crl.async_disable_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_crl(
        self,
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Enables a certificate revocation list (CRL). When enabled, certificates stored in the CRL are unauthorized to receive session credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:EnableCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.enable_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.enable_crl.async_enable_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_profile(
        self,
        name: "capo_rolesanywhere.types.resource_name.ResourceName",
        role_arns: "capo_rolesanywhere.types.role_arn_list.RoleArnList",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        require_instance_properties: Optional[bool] = None,
        session_policy: Optional[str] = None,
        managed_policy_arns: Optional[
            "capo_rolesanywhere.types.managed_policy_list.ManagedPolicyList"
        ] = None,
        duration_seconds: Optional[int] = None,
        enabled: Optional[bool] = None,
        tags: Optional["capo_rolesanywhere.types.tag_list.TagList"] = None,
        accept_role_session_name: Optional[bool] = None,
    ) -> "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Creates a <i>profile</i>, a list of the roles that Roles Anywhere service is trusted to assume. You use profiles to intersect permissions with IAM managed policies.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:CreateProfile</code>. </p>

        Args:
            name: <p>The name of the profile.</p>
            require_instance_properties: <p>Unused, saved for future use. Will likely specify whether instance properties are required in temporary credential requests with this profile. </p>
            session_policy: <p>A session policy that applies to the trust boundary of the vended session credentials. </p>
            role_arns: <p>A list of IAM roles that this profile can assume in a temporary credential request.</p>
            managed_policy_arns: <p>A list of managed policy ARNs that apply to the vended session credentials. </p>
            duration_seconds: <p> Used to determine how long sessions vended using this profile are valid for. See the <code>Expiration</code> section of the <a href="https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object">CreateSession API documentation</a> page for more details. In requests, if this value is not provided, the default value will be 3600. </p>
            enabled: <p>Specifies whether the profile is enabled.</p>
            tags: <p>The tags to attach to the profile.</p>
            accept_role_session_name: <p>Used to determine if a custom role session name will be accepted in a temporary credential request.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.create_profile_request.CreateProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.create_profile

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.create_profile.async_create_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.create_profile_request.CreateProfileRequest = {
            "name": name,
            "role_arns": role_arns,
        }
        if require_instance_properties is not None:
            input_["require_instance_properties"] = require_instance_properties
        if session_policy is not None:
            input_["session_policy"] = session_policy
        if managed_policy_arns is not None:
            input_["managed_policy_arns"] = managed_policy_arns
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if enabled is not None:
            input_["enabled"] = enabled
        if tags is not None:
            input_["tags"] = tags
        if accept_role_session_name is not None:
            input_["accept_role_session_name"] = accept_role_session_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_profile(
        self,
        profile_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Gets a profile.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.get_profile

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.get_profile.async_get_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {
            "profile_id": profile_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_profile(
        self,
        profile_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        name: Optional["capo_rolesanywhere.types.resource_name.ResourceName"] = None,
        session_policy: Optional[str] = None,
        role_arns: Optional[
            "capo_rolesanywhere.types.role_arn_list.RoleArnList"
        ] = None,
        managed_policy_arns: Optional[
            "capo_rolesanywhere.types.managed_policy_list.ManagedPolicyList"
        ] = None,
        duration_seconds: Optional[int] = None,
        accept_role_session_name: Optional[bool] = None,
    ) -> "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Updates a <i>profile</i>, a list of the roles that IAM Roles Anywhere service is trusted to assume. You use profiles to intersect permissions with IAM managed policies.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UpdateProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
            name: <p>The name of the profile.</p>
            session_policy: <p>A session policy that applies to the trust boundary of the vended session credentials. </p>
            role_arns: <p>A list of IAM roles that this profile can assume in a temporary credential request.</p>
            managed_policy_arns: <p>A list of managed policy ARNs that apply to the vended session credentials. </p>
            duration_seconds: <p> Used to determine how long sessions vended using this profile are valid for. See the <code>Expiration</code> section of the <a href="https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object">CreateSession API documentation</a> page for more details. In requests, if this value is not provided, the default value will be 3600. </p>
            accept_role_session_name: <p>Used to determine if a custom role session name will be accepted in a temporary credential request.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.update_profile_request.UpdateProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.update_profile

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.update_profile.async_update_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.update_profile_request.UpdateProfileRequest = {
            "profile_id": profile_id
        }
        if name is not None:
            input_["name"] = name
        if session_policy is not None:
            input_["session_policy"] = session_policy
        if role_arns is not None:
            input_["role_arns"] = role_arns
        if managed_policy_arns is not None:
            input_["managed_policy_arns"] = managed_policy_arns
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if accept_role_session_name is not None:
            input_["accept_role_session_name"] = accept_role_session_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_profile(
        self,
        profile_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Deletes a profile.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DeleteProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.delete_profile

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.delete_profile.async_delete_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {
            "profile_id": profile_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_profiles(
        self,
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "capo_rolesanywhere.types.list_profiles_response.ListProfilesResponse":
        """<p>Lists all profiles in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListProfiles</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.list_request.ListRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.list_profiles_response.ListProfilesResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.list_profiles

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.list_profiles.async_list_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.list_request.ListRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_profiles(
        self,
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "AsyncIterator[capo_rolesanywhere.types.profile_detail.ProfileDetail]":
        _token = next_token
        while True:
            _response = await self.list_profiles(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("profiles",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def delete_attribute_mapping(
        self,
        profile_id: "capo_rolesanywhere.types.uuid.Uuid",
        certificate_field: "capo_rolesanywhere.types.certificate_field.CertificateField",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        specifiers: Optional[
            "capo_rolesanywhere.types.specifier_list.SpecifierList"
        ] = None,
    ) -> "capo_rolesanywhere.types.delete_attribute_mapping_response.DeleteAttributeMappingResponse":
        """<p>Delete an entry from the attribute mapping rules enforced by a given profile.</p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
            certificate_field: <p>Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.</p>
            specifiers: <p>A list of specifiers of a certificate field; for example, CN, OU, UID from a Subject.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteAttributeMapping - Deletes a custom attribute mapping rule

            >>> await client.delete_attribute_mapping(profile_id='00000000-0000-0000-0000-000000000000', specifiers=['OU'], certificate_field='x509Subject')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.delete_attribute_mapping_request.DeleteAttributeMappingRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.delete_attribute_mapping_response.DeleteAttributeMappingResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.delete_attribute_mapping

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.delete_attribute_mapping.async_delete_attribute_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.delete_attribute_mapping_request.DeleteAttributeMappingRequest = {
            "profile_id": profile_id,
            "certificate_field": certificate_field,
        }
        if specifiers is not None:
            input_["specifiers"] = specifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_profile(
        self,
        profile_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Disables a profile. When disabled, temporary credential requests with this profile fail.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DisableProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.disable_profile

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.disable_profile.async_disable_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {
            "profile_id": profile_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_profile(
        self,
        profile_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Enables temporary credential requests for a profile. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:EnableProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.enable_profile

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.enable_profile.async_enable_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {
            "profile_id": profile_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_attribute_mapping(
        self,
        profile_id: "capo_rolesanywhere.types.uuid.Uuid",
        certificate_field: "capo_rolesanywhere.types.certificate_field.CertificateField",
        mapping_rules: "capo_rolesanywhere.types.mapping_rules.MappingRules",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.put_attribute_mapping_response.PutAttributeMappingResponse":
        """<p>Put an entry in the attribute mapping rules that will be enforced by a given profile. A mapping specifies a certificate field and one or more specifiers that have contextual meanings.</p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
            certificate_field: <p>Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.</p>
            mapping_rules: <p>A list of mapping entries for every supported specifier or sub-field.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            PutAttributeMapping - Adds a custom attribute mapping rule

            >>> await client.put_attribute_mapping(profile_id='00000000-0000-0000-0000-000000000000', mapping_rules=[{'specifier': 'CN'}], certificate_field='x509Subject')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.put_attribute_mapping_request.PutAttributeMappingRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.put_attribute_mapping_response.PutAttributeMappingResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.put_attribute_mapping

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.put_attribute_mapping.async_put_attribute_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.put_attribute_mapping_request.PutAttributeMappingRequest = {
            "profile_id": profile_id,
            "certificate_field": certificate_field,
            "mapping_rules": mapping_rules,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_subject(
        self,
        subject_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.subject_detail_response.SubjectDetailResponse":
        """<p>Gets a <i>subject</i>, which associates a certificate identity with authentication attempts. The subject stores auditing information such as the status of the last authentication attempt, the certificate data used in the attempt, and the last time the associated identity attempted authentication. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetSubject</code>. </p>

        Args:
            subject_id: <p>The unique identifier of the subject. </p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_subject_request.ScalarSubjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.subject_detail_response.SubjectDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.get_subject

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.get_subject.async_get_subject(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_subject_request.ScalarSubjectRequest = {
            "subject_id": subject_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_subjects(
        self,
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "capo_rolesanywhere.types.list_subjects_response.ListSubjectsResponse":
        """<p>Lists the subjects in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListSubjects</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.list_request.ListRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.list_subjects_response.ListSubjectsResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.list_subjects

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.list_subjects.async_list_subjects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.list_request.ListRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_subjects(
        self,
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "AsyncIterator[capo_rolesanywhere.types.subject_summary.SubjectSummary]":
        _token = next_token
        while True:
            _response = await self.list_subjects(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("subjects",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_trust_anchor(
        self,
        name: "capo_rolesanywhere.types.resource_name.ResourceName",
        source: "capo_rolesanywhere.types.source.Source",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        enabled: Optional[bool] = None,
        tags: Optional["capo_rolesanywhere.types.tag_list.TagList"] = None,
        notification_settings: Optional[
            "capo_rolesanywhere.types.notification_settings.NotificationSettings"
        ] = None,
    ) -> "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Creates a trust anchor to establish trust between IAM Roles Anywhere and your certificate authority (CA). You can define a trust anchor as a reference to an Private Certificate Authority (Private CA) or by uploading a CA certificate. Your Amazon Web Services workloads can authenticate with the trust anchor using certificates issued by the CA in exchange for temporary Amazon Web Services credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:CreateTrustAnchor</code>. </p>

        Args:
            name: <p>The name of the trust anchor.</p>
            source: <p>The trust anchor type and its related certificate data.</p>
            enabled: <p>Specifies whether the trust anchor is enabled.</p>
            tags: <p>The tags to attach to the trust anchor.</p>
            notification_settings: <p>A list of notification settings to be associated to the trust anchor.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.create_trust_anchor_request.CreateTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.create_trust_anchor

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.create_trust_anchor.async_create_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.create_trust_anchor_request.CreateTrustAnchorRequest = {
            "name": name,
            "source": source,
        }
        if enabled is not None:
            input_["enabled"] = enabled
        if tags is not None:
            input_["tags"] = tags
        if notification_settings is not None:
            input_["notification_settings"] = notification_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_trust_anchor(
        self,
        trust_anchor_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Gets a trust anchor.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.get_trust_anchor

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.get_trust_anchor.async_get_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {
            "trust_anchor_id": trust_anchor_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_trust_anchor(
        self,
        trust_anchor_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        name: Optional["capo_rolesanywhere.types.resource_name.ResourceName"] = None,
        source: Optional["capo_rolesanywhere.types.source.Source"] = None,
    ) -> "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Updates a trust anchor. You establish trust between IAM Roles Anywhere and your certificate authority (CA) by configuring a trust anchor. You can define a trust anchor as a reference to an Private Certificate Authority (Private CA) or by uploading a CA certificate. Your Amazon Web Services workloads can authenticate with the trust anchor using certificates issued by the CA in exchange for temporary Amazon Web Services credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UpdateTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
            name: <p>The name of the trust anchor.</p>
            source: <p>The trust anchor type and its related certificate data.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.update_trust_anchor_request.UpdateTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.update_trust_anchor

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.update_trust_anchor.async_update_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.update_trust_anchor_request.UpdateTrustAnchorRequest = {
            "trust_anchor_id": trust_anchor_id
        }
        if name is not None:
            input_["name"] = name
        if source is not None:
            input_["source"] = source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_trust_anchor(
        self,
        trust_anchor_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Deletes a trust anchor.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DeleteTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.delete_trust_anchor

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.delete_trust_anchor.async_delete_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {
            "trust_anchor_id": trust_anchor_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_trust_anchors(
        self,
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> (
        "capo_rolesanywhere.types.list_trust_anchors_response.ListTrustAnchorsResponse"
    ):
        """<p>Lists the trust anchors in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListTrustAnchors</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.list_request.ListRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.list_trust_anchors_response.ListTrustAnchorsResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.list_trust_anchors

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.list_trust_anchors.async_list_trust_anchors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.list_request.ListRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_trust_anchors(
        self,
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> (
        "AsyncIterator[capo_rolesanywhere.types.trust_anchor_detail.TrustAnchorDetail]"
    ):
        _token = next_token
        while True:
            _response = await self.list_trust_anchors(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("trust_anchors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disable_trust_anchor(
        self,
        trust_anchor_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Disables a trust anchor. When disabled, temporary credential requests specifying this trust anchor are unauthorized.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DisableTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.disable_trust_anchor

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.disable_trust_anchor.async_disable_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {
            "trust_anchor_id": trust_anchor_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_trust_anchor(
        self,
        trust_anchor_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse":
        """<p>Enables a trust anchor. When enabled, certificates in the trust anchor chain are authorized for trust validation. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:EnableTrustAnchor</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.trust_anchor_detail_response.TrustAnchorDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.enable_trust_anchor

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.enable_trust_anchor.async_enable_trust_anchor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rolesanywhere.types.scalar_trust_anchor_request.ScalarTrustAnchorRequest = {
            "trust_anchor_id": trust_anchor_id
        }

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
