"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#LicenseManagerUserSubscriptions``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_license_manager_user_subscriptions._auth._signers
import capo_license_manager_user_subscriptions._auth._sigv4
from capo_license_manager_user_subscriptions._auth._identity import Credentials
from capo_license_manager_user_subscriptions._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_license_manager_user_subscriptions._auth._zapros_handler import AuthMiddleware
from capo_license_manager_user_subscriptions._pagination import (
    resolve_path as _resolve_path,
)
from capo_license_manager_user_subscriptions._services._aws_config import aaws_config
from capo_license_manager_user_subscriptions._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.arn
    import capo_license_manager_user_subscriptions.types.associate_user_request
    import capo_license_manager_user_subscriptions.types.associate_user_response
    import capo_license_manager_user_subscriptions.types.box_integer
    import capo_license_manager_user_subscriptions.types.create_license_server_endpoint_request
    import capo_license_manager_user_subscriptions.types.create_license_server_endpoint_response
    import capo_license_manager_user_subscriptions.types.delete_license_server_endpoint_request
    import capo_license_manager_user_subscriptions.types.delete_license_server_endpoint_response
    import capo_license_manager_user_subscriptions.types.deregister_identity_provider_request
    import capo_license_manager_user_subscriptions.types.deregister_identity_provider_response
    import capo_license_manager_user_subscriptions.types.disassociate_user_request
    import capo_license_manager_user_subscriptions.types.disassociate_user_response
    import capo_license_manager_user_subscriptions.types.filter_list
    import capo_license_manager_user_subscriptions.types.identity_provider
    import capo_license_manager_user_subscriptions.types.identity_provider_summary
    import capo_license_manager_user_subscriptions.types.instance_summary
    import capo_license_manager_user_subscriptions.types.instance_user_summary
    import capo_license_manager_user_subscriptions.types.license_server_endpoint
    import capo_license_manager_user_subscriptions.types.license_server_settings
    import capo_license_manager_user_subscriptions.types.list_identity_providers_request
    import capo_license_manager_user_subscriptions.types.list_identity_providers_response
    import capo_license_manager_user_subscriptions.types.list_instances_request
    import capo_license_manager_user_subscriptions.types.list_instances_response
    import capo_license_manager_user_subscriptions.types.list_license_server_endpoints_request
    import capo_license_manager_user_subscriptions.types.list_license_server_endpoints_response
    import capo_license_manager_user_subscriptions.types.list_product_subscriptions_request
    import capo_license_manager_user_subscriptions.types.list_product_subscriptions_response
    import capo_license_manager_user_subscriptions.types.list_tags_for_resource_request
    import capo_license_manager_user_subscriptions.types.list_tags_for_resource_response
    import capo_license_manager_user_subscriptions.types.list_user_associations_request
    import capo_license_manager_user_subscriptions.types.list_user_associations_response
    import capo_license_manager_user_subscriptions.types.product_user_summary
    import capo_license_manager_user_subscriptions.types.register_identity_provider_request
    import capo_license_manager_user_subscriptions.types.register_identity_provider_response
    import capo_license_manager_user_subscriptions.types.resource_arn
    import capo_license_manager_user_subscriptions.types.server_type
    import capo_license_manager_user_subscriptions.types.settings
    import capo_license_manager_user_subscriptions.types.start_product_subscription_request
    import capo_license_manager_user_subscriptions.types.start_product_subscription_response
    import capo_license_manager_user_subscriptions.types.stop_product_subscription_request
    import capo_license_manager_user_subscriptions.types.stop_product_subscription_response
    import capo_license_manager_user_subscriptions.types.tag_key_list
    import capo_license_manager_user_subscriptions.types.tag_resource_request
    import capo_license_manager_user_subscriptions.types.tag_resource_response
    import capo_license_manager_user_subscriptions.types.tags
    import capo_license_manager_user_subscriptions.types.untag_resource_request
    import capo_license_manager_user_subscriptions.types.untag_resource_response
    import capo_license_manager_user_subscriptions.types.update_identity_provider_settings_request
    import capo_license_manager_user_subscriptions.types.update_identity_provider_settings_response
    import capo_license_manager_user_subscriptions.types.update_settings


class AsyncLicenseManagerUserSubscriptionsClientConfig(
    TypedDict, total=False, closed=True
):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncLicenseManagerUserSubscriptionsClient:
    """A client for the ``LicenseManagerUserSubscriptions`` service.

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
        self._config = AsyncLicenseManagerUserSubscriptionsClientConfig(
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
        self,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncLicenseManagerUserSubscriptionsClientConfig = (
            config_overrides or {}
        )
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

    async def associate_user(
        self,
        username: str,
        instance_id: str,
        identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider",
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        domain: Optional[str] = None,
        tags: Optional[
            "capo_license_manager_user_subscriptions.types.tags.Tags"
        ] = None,
    ) -> "capo_license_manager_user_subscriptions.types.associate_user_response.AssociateUserResponse":
        """<p>Associates the user to an EC2 instance to utilize user-based subscriptions.</p> <note> <p>Your estimated bill for charges on the number of users and related costs will take 48 hours to appear for billing periods that haven't closed (marked as <b>Pending</b> billing status) in Amazon Web Services Billing. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/invoice.html">Viewing your monthly charges</a> in the <i>Amazon Web Services Billing User Guide</i>.</p> </note>

        Args:
            username: <p>The user name from the identity provider.</p>
            instance_id: <p>The ID of the EC2 instance that provides the user-based subscription.</p>
            identity_provider: <p>The identity provider for the user.</p>
            domain: <p>The domain name of the Active Directory that contains information for the user to associate.</p>
            tags: <p>The tags that apply for the user association.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.associate_user_request.AssociateUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.associate_user_response.AssociateUserResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.associate_user

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.associate_user.async_associate_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.associate_user_request.AssociateUserRequest = {
            "username": username,
            "instance_id": instance_id,
            "identity_provider": identity_provider,
        }
        if domain is not None:
            input_["domain"] = domain
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_license_server_endpoint(
        self,
        identity_provider_arn: "capo_license_manager_user_subscriptions.types.arn.Arn",
        license_server_settings: "capo_license_manager_user_subscriptions.types.license_server_settings.LicenseServerSettings",
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        tags: Optional[
            "capo_license_manager_user_subscriptions.types.tags.Tags"
        ] = None,
    ) -> "capo_license_manager_user_subscriptions.types.create_license_server_endpoint_response.CreateLicenseServerEndpointResponse":
        """<p>Creates a network endpoint for the Remote Desktop Services (RDS) license server.</p>

        Args:
            identity_provider_arn: <p>The Amazon Resource Name (ARN) that identifies the <code>IdentityProvider</code> resource that contains details about a registered identity provider. In the case of Active Directory, that can be a self-managed Active Directory or an Amazon Web Services Managed Active Directory that contains user identity details.</p>
            license_server_settings: <p>The <code>LicenseServerSettings</code> resource to create for the endpoint. The settings include the type of license server and the Secrets Manager secret that enables administrators to add or remove users associated with the license server.</p>
            tags: <p>The tags that apply for the license server endpoint.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.create_license_server_endpoint_request.CreateLicenseServerEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.create_license_server_endpoint_response.CreateLicenseServerEndpointResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.create_license_server_endpoint

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.create_license_server_endpoint.async_create_license_server_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.create_license_server_endpoint_request.CreateLicenseServerEndpointRequest = {
            "identity_provider_arn": identity_provider_arn,
            "license_server_settings": license_server_settings,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_license_server_endpoint(
        self,
        license_server_endpoint_arn: "capo_license_manager_user_subscriptions.types.arn.Arn",
        server_type: "capo_license_manager_user_subscriptions.types.server_type.ServerType",
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
    ) -> "capo_license_manager_user_subscriptions.types.delete_license_server_endpoint_response.DeleteLicenseServerEndpointResponse":
        """<p>Deletes a <code>LicenseServerEndpoint</code> resource.</p>

        Args:
            license_server_endpoint_arn: <p>The Amazon Resource Name (ARN) that identifies the <code>LicenseServerEndpoint</code> resource to delete.</p>
            server_type: <p>The type of License Server that the delete request refers to.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.delete_license_server_endpoint_request.DeleteLicenseServerEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.delete_license_server_endpoint_response.DeleteLicenseServerEndpointResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.delete_license_server_endpoint

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.delete_license_server_endpoint.async_delete_license_server_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.delete_license_server_endpoint_request.DeleteLicenseServerEndpointRequest = {
            "license_server_endpoint_arn": license_server_endpoint_arn,
            "server_type": server_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_identity_provider(
        self,
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        identity_provider: Optional[
            "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
        ] = None,
        product: Optional[str] = None,
        identity_provider_arn: Optional[
            "capo_license_manager_user_subscriptions.types.arn.Arn"
        ] = None,
    ) -> "capo_license_manager_user_subscriptions.types.deregister_identity_provider_response.DeregisterIdentityProviderResponse":
        """<p>Deregisters the Active Directory identity provider from License Manager user-based subscriptions.</p>

        Args:
            identity_provider: <p>An object that specifies details for the Active Directory identity provider.</p>
            product: <p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>OFFICE_STANDARD</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>
            identity_provider_arn: <p>The Amazon Resource Name (ARN) that identifies the identity provider to deregister.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.deregister_identity_provider_request.DeregisterIdentityProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.deregister_identity_provider_response.DeregisterIdentityProviderResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.deregister_identity_provider

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.deregister_identity_provider.async_deregister_identity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.deregister_identity_provider_request.DeregisterIdentityProviderRequest = {}
        if identity_provider is not None:
            input_["identity_provider"] = identity_provider
        if product is not None:
            input_["product"] = product
        if identity_provider_arn is not None:
            input_["identity_provider_arn"] = identity_provider_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_user(
        self,
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        username: Optional[str] = None,
        instance_id: Optional[str] = None,
        identity_provider: Optional[
            "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
        ] = None,
        instance_user_arn: Optional[
            "capo_license_manager_user_subscriptions.types.arn.Arn"
        ] = None,
        domain: Optional[str] = None,
    ) -> "capo_license_manager_user_subscriptions.types.disassociate_user_response.DisassociateUserResponse":
        """<p>Disassociates the user from an EC2 instance providing user-based subscriptions.</p>

        Args:
            username: <p>The user name from the Active Directory identity provider for the user.</p>
            instance_id: <p>The ID of the EC2 instance which provides user-based subscriptions.</p>
            identity_provider: <p>An object that specifies details for the Active Directory identity provider.</p>
            instance_user_arn: <p>The Amazon Resource Name (ARN) of the user to disassociate from the EC2 instance.</p>
            domain: <p>The domain name of the Active Directory that contains information for the user to disassociate.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.disassociate_user_request.DisassociateUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.disassociate_user_response.DisassociateUserResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.disassociate_user

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.disassociate_user.async_disassociate_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.disassociate_user_request.DisassociateUserRequest = {}
        if username is not None:
            input_["username"] = username
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if identity_provider is not None:
            input_["identity_provider"] = identity_provider
        if instance_user_arn is not None:
            input_["instance_user_arn"] = instance_user_arn
        if domain is not None:
            input_["domain"] = domain

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_identity_providers(
        self,
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        max_results: Optional[
            "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        filters: Optional[
            "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_license_manager_user_subscriptions.types.list_identity_providers_response.ListIdentityProvidersResponse":
        """<p>Lists the Active Directory identity providers for user-based subscriptions.</p>

        Args:
            max_results: <p>The maximum number of results to return from a single request.</p>
            filters: <p>You can use the following filters to streamline results:</p> <ul> <li> <p>Product</p> </li> <li> <p>DirectoryId</p> </li> </ul>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.list_identity_providers_request.ListIdentityProvidersRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.list_identity_providers_response.ListIdentityProvidersResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_identity_providers

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_identity_providers.async_list_identity_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.list_identity_providers_request.ListIdentityProvidersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_identity_providers(
        self,
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        max_results: Optional[
            "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        filters: Optional[
            "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_license_manager_user_subscriptions.types.identity_provider_summary.IdentityProviderSummary]":
        _token = next_token
        while True:
            _response = await self.list_identity_providers(
                config_overrides=config_overrides,
                max_results=max_results,
                filters=filters,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("identity_provider_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_instances(
        self,
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        max_results: Optional[
            "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
        ] = None,
    ) -> "capo_license_manager_user_subscriptions.types.list_instances_response.ListInstancesResponse":
        """<p>Lists the EC2 instances providing user-based subscriptions.</p>

        Args:
            max_results: <p>The maximum number of results to return from a single request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>
            filters: <p>You can use the following filters to streamline results:</p> <ul> <li> <p>Status</p> </li> <li> <p>InstanceId</p> </li> </ul>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.list_instances_request.ListInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.list_instances_response.ListInstancesResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_instances

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_instances.async_list_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.list_instances_request.ListInstancesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_instances(
        self,
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        max_results: Optional[
            "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
        ] = None,
    ) -> "AsyncIterator[capo_license_manager_user_subscriptions.types.instance_summary.InstanceSummary]":
        _token = next_token
        while True:
            _response = await self.list_instances(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("instance_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_license_server_endpoints(
        self,
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        max_results: Optional[
            "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        filters: Optional[
            "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_license_manager_user_subscriptions.types.list_license_server_endpoints_response.ListLicenseServerEndpointsResponse":
        """<p>List the Remote Desktop Services (RDS) License Server endpoints </p>

        Args:
            max_results: <p>The maximum number of results to return from a single request.</p>
            filters: <p>You can use the following filters to streamline results:</p> <ul> <li> <p>IdentityProviderArn</p> </li> </ul>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.list_license_server_endpoints_request.ListLicenseServerEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.list_license_server_endpoints_response.ListLicenseServerEndpointsResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_license_server_endpoints

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_license_server_endpoints.async_list_license_server_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.list_license_server_endpoints_request.ListLicenseServerEndpointsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_license_server_endpoints(
        self,
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        max_results: Optional[
            "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        filters: Optional[
            "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_license_manager_user_subscriptions.types.license_server_endpoint.LicenseServerEndpoint]":
        _token = next_token
        while True:
            _response = await self.list_license_server_endpoints(
                config_overrides=config_overrides,
                max_results=max_results,
                filters=filters,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("license_server_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_product_subscriptions(
        self,
        identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider",
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        product: Optional[str] = None,
        max_results: Optional[
            "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        filters: Optional[
            "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_license_manager_user_subscriptions.types.list_product_subscriptions_response.ListProductSubscriptionsResponse":
        """<p>Lists the user-based subscription products available from an identity provider.</p>

        Args:
            product: <p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>OFFICE_STANDARD</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>
            identity_provider: <p>An object that specifies details for the identity provider.</p>
            max_results: <p>The maximum number of results to return from a single request.</p>
            filters: <p>You can use the following filters to streamline results:</p> <ul> <li> <p>Status</p> </li> <li> <p>Username</p> </li> <li> <p>Domain</p> </li> </ul>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.list_product_subscriptions_request.ListProductSubscriptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.list_product_subscriptions_response.ListProductSubscriptionsResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_product_subscriptions

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_product_subscriptions.async_list_product_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.list_product_subscriptions_request.ListProductSubscriptionsRequest = {
            "identity_provider": identity_provider
        }
        if product is not None:
            input_["product"] = product
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_product_subscriptions(
        self,
        identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider",
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        product: Optional[str] = None,
        max_results: Optional[
            "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        filters: Optional[
            "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_license_manager_user_subscriptions.types.product_user_summary.ProductUserSummary]":
        _token = next_token
        while True:
            _response = await self.list_product_subscriptions(
                identity_provider,
                config_overrides=config_overrides,
                product=product,
                max_results=max_results,
                filters=filters,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("product_user_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_license_manager_user_subscriptions.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
    ) -> "capo_license_manager_user_subscriptions.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns the list of tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_user_associations(
        self,
        instance_id: str,
        identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider",
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        max_results: Optional[
            "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        filters: Optional[
            "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_license_manager_user_subscriptions.types.list_user_associations_response.ListUserAssociationsResponse":
        """<p>Lists user associations for an identity provider.</p>

        Args:
            instance_id: <p>The ID of the EC2 instance, which provides user-based subscriptions.</p>
            identity_provider: <p>An object that specifies details for the identity provider.</p>
            max_results: <p>The maximum number of results to return from a single request.</p>
            filters: <p>You can use the following filters to streamline results:</p> <ul> <li> <p>Status</p> </li> <li> <p>Username</p> </li> <li> <p>Domain</p> </li> </ul>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.list_user_associations_request.ListUserAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.list_user_associations_response.ListUserAssociationsResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_user_associations

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.list_user_associations.async_list_user_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.list_user_associations_request.ListUserAssociationsRequest = {
            "instance_id": instance_id,
            "identity_provider": identity_provider,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_user_associations(
        self,
        instance_id: str,
        identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider",
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        max_results: Optional[
            "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        filters: Optional[
            "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_license_manager_user_subscriptions.types.instance_user_summary.InstanceUserSummary]":
        _token = next_token
        while True:
            _response = await self.list_user_associations(
                instance_id,
                identity_provider,
                config_overrides=config_overrides,
                max_results=max_results,
                filters=filters,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("instance_user_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def register_identity_provider(
        self,
        identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider",
        product: str,
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        settings: Optional[
            "capo_license_manager_user_subscriptions.types.settings.Settings"
        ] = None,
        tags: Optional[
            "capo_license_manager_user_subscriptions.types.tags.Tags"
        ] = None,
    ) -> "capo_license_manager_user_subscriptions.types.register_identity_provider_response.RegisterIdentityProviderResponse":
        """<p>Registers an identity provider for user-based subscriptions.</p>

        Args:
            identity_provider: <p>An object that specifies details for the identity provider to register.</p>
            product: <p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>OFFICE_STANDARD</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>
            settings: <p>The registered identity provider’s product related configuration settings such as the subnets to provision VPC endpoints.</p>
            tags: <p>The tags that apply to the identity provider's registration.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.register_identity_provider_request.RegisterIdentityProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.register_identity_provider_response.RegisterIdentityProviderResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.register_identity_provider

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.register_identity_provider.async_register_identity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.register_identity_provider_request.RegisterIdentityProviderRequest = {
            "identity_provider": identity_provider,
            "product": product,
        }
        if settings is not None:
            input_["settings"] = settings
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_product_subscription(
        self,
        username: str,
        identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider",
        product: str,
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        domain: Optional[str] = None,
        tags: Optional[
            "capo_license_manager_user_subscriptions.types.tags.Tags"
        ] = None,
    ) -> "capo_license_manager_user_subscriptions.types.start_product_subscription_response.StartProductSubscriptionResponse":
        """<p>Starts a product subscription for a user with the specified identity provider.</p> <note> <p>Your estimated bill for charges on the number of users and related costs will take 48 hours to appear for billing periods that haven't closed (marked as <b>Pending</b> billing status) in Amazon Web Services Billing. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/invoice.html">Viewing your monthly charges</a> in the <i>Amazon Web Services Billing User Guide</i>.</p> </note>

        Args:
            username: <p>The user name from the identity provider of the user.</p>
            identity_provider: <p>An object that specifies details for the identity provider.</p>
            product: <p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>OFFICE_STANDARD</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>
            domain: <p>The domain name of the Active Directory that contains the user for whom to start the product subscription.</p>
            tags: <p>The tags that apply to the product subscription.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.start_product_subscription_request.StartProductSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.start_product_subscription_response.StartProductSubscriptionResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.start_product_subscription

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.start_product_subscription.async_start_product_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.start_product_subscription_request.StartProductSubscriptionRequest = {
            "username": username,
            "identity_provider": identity_provider,
            "product": product,
        }
        if domain is not None:
            input_["domain"] = domain
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_product_subscription(
        self,
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        username: Optional[str] = None,
        identity_provider: Optional[
            "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
        ] = None,
        product: Optional[str] = None,
        product_user_arn: Optional[
            "capo_license_manager_user_subscriptions.types.arn.Arn"
        ] = None,
        domain: Optional[str] = None,
    ) -> "capo_license_manager_user_subscriptions.types.stop_product_subscription_response.StopProductSubscriptionResponse":
        """<p>Stops a product subscription for a user with the specified identity provider.</p>

        Args:
            username: <p>The user name from the identity provider for the user.</p>
            identity_provider: <p>An object that specifies details for the identity provider.</p>
            product: <p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>OFFICE_STANDARD</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>
            product_user_arn: <p>The Amazon Resource Name (ARN) of the product user.</p>
            domain: <p>The domain name of the Active Directory that contains the user for whom to stop the product subscription.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.conflict_exception.ConflictException: <p>The request couldn't be completed because it conflicted with the current state of the resource.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.stop_product_subscription_request.StopProductSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.stop_product_subscription_response.StopProductSubscriptionResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.stop_product_subscription

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.stop_product_subscription.async_stop_product_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.stop_product_subscription_request.StopProductSubscriptionRequest = {}
        if username is not None:
            input_["username"] = username
        if identity_provider is not None:
            input_["identity_provider"] = identity_provider
        if product is not None:
            input_["product"] = product
        if product_user_arn is not None:
            input_["product_user_arn"] = product_user_arn
        if domain is not None:
            input_["domain"] = domain

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_license_manager_user_subscriptions.types.resource_arn.ResourceArn",
        tags: "capo_license_manager_user_subscriptions.types.tags.Tags",
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
    ) -> "capo_license_manager_user_subscriptions.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>The tags to apply to the specified resource.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.tag_resource

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_license_manager_user_subscriptions.types.resource_arn.ResourceArn",
        tag_keys: "capo_license_manager_user_subscriptions.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
    ) -> "capo_license_manager_user_subscriptions.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from.</p>
            tag_keys: <p>The tag keys to remove from the resource.</p>

        Raises:
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.untag_resource

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_identity_provider_settings(
        self,
        update_settings: "capo_license_manager_user_subscriptions.types.update_settings.UpdateSettings",
        *,
        config_overrides: Optional[
            AsyncLicenseManagerUserSubscriptionsClientConfig
        ] = None,
        identity_provider: Optional[
            "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
        ] = None,
        product: Optional[str] = None,
        identity_provider_arn: Optional[
            "capo_license_manager_user_subscriptions.types.arn.Arn"
        ] = None,
    ) -> "capo_license_manager_user_subscriptions.types.update_identity_provider_settings_response.UpdateIdentityProviderSettingsResponse":
        """<p>Updates additional product configuration settings for the registered identity provider.</p>

        Args:
            product: <p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>OFFICE_STANDARD</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>
            identity_provider_arn: <p>The Amazon Resource Name (ARN) of the identity provider to update.</p>
            update_settings: <p>Updates the registered identity provider’s product related configuration settings. You can update any combination of settings in a single operation such as the:</p> <ul> <li> <p>Subnets which you want to add to provision VPC endpoints.</p> </li> <li> <p>Subnets which you want to remove the VPC endpoints from.</p> </li> <li> <p>Security group ID which permits traffic to the VPC endpoints.</p> </li> </ul>

        Raises:
            capo_license_manager_user_subscriptions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_license_manager_user_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_user_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_license_manager_user_subscriptions.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_license_manager_user_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_license_manager_user_subscriptions.types.update_identity_provider_settings_request.UpdateIdentityProviderSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_license_manager_user_subscriptions.types.update_identity_provider_settings_response.UpdateIdentityProviderSettingsResponse"
        ]:
            import capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.update_identity_provider_settings

            (
                output,
                http_response,
            ) = await capo_license_manager_user_subscriptions._operations.license_manager_user_subscriptions.update_identity_provider_settings.async_update_identity_provider_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_user_subscriptions.types.update_identity_provider_settings_request.UpdateIdentityProviderSettingsRequest = {
            "update_settings": update_settings
        }
        if identity_provider is not None:
            input_["identity_provider"] = identity_provider
        if product is not None:
            input_["product"] = product
        if identity_provider_arn is not None:
            input_["identity_provider_arn"] = identity_provider_arn

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
