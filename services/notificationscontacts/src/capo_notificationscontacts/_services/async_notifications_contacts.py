"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#NotificationsContacts``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_notificationscontacts._auth._signers
import capo_notificationscontacts._auth._sigv4
from capo_notificationscontacts._auth._identity import Credentials
from capo_notificationscontacts._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_notificationscontacts._auth._zapros_handler import AuthMiddleware
from capo_notificationscontacts._pagination import resolve_path as _resolve_path
from capo_notificationscontacts._resources.notifications_contacts.email_contact_resource import (
    AsyncEmailContactResource,
)
from capo_notificationscontacts._services._aws_config import aaws_config
from capo_notificationscontacts._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_notificationscontacts.types.activate_email_contact_request
    import capo_notificationscontacts.types.activate_email_contact_response
    import capo_notificationscontacts.types.create_email_contact_request
    import capo_notificationscontacts.types.create_email_contact_response
    import capo_notificationscontacts.types.delete_email_contact_request
    import capo_notificationscontacts.types.delete_email_contact_response
    import capo_notificationscontacts.types.email_contact
    import capo_notificationscontacts.types.email_contact_address
    import capo_notificationscontacts.types.email_contact_arn
    import capo_notificationscontacts.types.email_contact_name
    import capo_notificationscontacts.types.get_email_contact_request
    import capo_notificationscontacts.types.get_email_contact_response
    import capo_notificationscontacts.types.list_email_contacts_request
    import capo_notificationscontacts.types.list_email_contacts_response
    import capo_notificationscontacts.types.list_tags_for_resource_request
    import capo_notificationscontacts.types.list_tags_for_resource_response
    import capo_notificationscontacts.types.send_activation_code_request
    import capo_notificationscontacts.types.send_activation_code_response
    import capo_notificationscontacts.types.tag_keys
    import capo_notificationscontacts.types.tag_map
    import capo_notificationscontacts.types.tag_resource_request
    import capo_notificationscontacts.types.tag_resource_response
    import capo_notificationscontacts.types.token
    import capo_notificationscontacts.types.untag_resource_request
    import capo_notificationscontacts.types.untag_resource_response


class AsyncNotificationsContactsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncNotificationsContactsClient:
    """A client for the ``NotificationsContacts`` service.

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
        self._config = AsyncNotificationsContactsClientConfig(
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
        self.email_contact_resource = AsyncEmailContactResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncNotificationsContactsClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
    ) -> "capo_notificationscontacts.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify. The resource can be a user, server, or role.</p>

        Args:
            arn: <p>The ARN you specified to list the tags of.</p>

        Raises:
            capo_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notificationscontacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Your request references a resource which does not exist. </p>
            capo_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notificationscontacts.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_notificationscontacts.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_notificationscontacts._operations.notifications_contacts.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn",
        tags: "capo_notificationscontacts.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
    ) -> "capo_notificationscontacts.types.tag_resource_response.TagResourceResponse":
        """<p>Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN). Taggable resources in AWS User Notifications Contacts include email contacts.</p>

        Args:
            arn: <p>The ARN of the configuration.</p>
            tags: <p>A list of tags to apply to the configuration.</p>

        Raises:
            capo_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notificationscontacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Your request references a resource which does not exist. </p>
            capo_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notificationscontacts.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_notificationscontacts.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.tag_resource

            (
                output,
                http_response,
            ) = await capo_notificationscontacts._operations.notifications_contacts.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.tag_resource_request.TagResourceRequest = {
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
        arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn",
        tag_keys: "capo_notificationscontacts.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
    ) -> (
        "capo_notificationscontacts.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>Detaches a key-value pair from a resource, as identified by its Amazon Resource Name (ARN). Taggable resources in AWS User Notifications Contacts include email contacts..</p>

        Args:
            arn: <p>The value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific AWS resource, such as a server, user, or role.</p>
            tag_keys: <p>Specifies a list of tag keys that you want to remove from the specified resources.</p>

        Raises:
            capo_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notificationscontacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Your request references a resource which does not exist. </p>
            capo_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notificationscontacts.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_notificationscontacts.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.untag_resource

            (
                output,
                http_response,
            ) = await capo_notificationscontacts._operations.notifications_contacts.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_email_contact(
        self,
        name: "capo_notificationscontacts.types.email_contact_name.EmailContactName",
        email_address: "capo_notificationscontacts.types.email_contact_address.EmailContactAddress",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
        tags: Optional["capo_notificationscontacts.types.tag_map.TagMap"] = None,
    ) -> "capo_notificationscontacts.types.create_email_contact_response.CreateEmailContactResponse":
        """<p>Creates an email contact for the provided email address.</p>

        Args:
            name: <p>The name of the email contact.</p>
            email_address: <p>The email address this email contact points to. The activation email and any subscribed emails are sent here.</p> <note> <p>This email address can't receive emails until it's activated.</p> </note>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>

        Raises:
            capo_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_notificationscontacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notificationscontacts.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> Request would cause a service quota to be exceeded.</p>
            capo_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notificationscontacts.types.create_email_contact_request.CreateEmailContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_notificationscontacts.types.create_email_contact_response.CreateEmailContactResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.create_email_contact

            (
                output,
                http_response,
            ) = await capo_notificationscontacts._operations.notifications_contacts.create_email_contact.async_create_email_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.create_email_contact_request.CreateEmailContactRequest = {
            "name": name,
            "email_address": email_address,
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

    async def get_email_contact(
        self,
        arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
    ) -> "capo_notificationscontacts.types.get_email_contact_response.GetEmailContactResponse":
        """<p>Returns an email contact.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the email contact to get.</p>

        Raises:
            capo_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notificationscontacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Your request references a resource which does not exist. </p>
            capo_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notificationscontacts.types.get_email_contact_request.GetEmailContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_notificationscontacts.types.get_email_contact_response.GetEmailContactResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.get_email_contact

            (
                output,
                http_response,
            ) = await capo_notificationscontacts._operations.notifications_contacts.get_email_contact.async_get_email_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.get_email_contact_request.GetEmailContactRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_email_contact(
        self,
        arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
    ) -> "capo_notificationscontacts.types.delete_email_contact_response.DeleteEmailContactResponse":
        """<p>Deletes an email contact.</p> <note> <p>Deleting an email contact removes it from all associated notification configurations.</p> </note>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_notificationscontacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notificationscontacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Your request references a resource which does not exist. </p>
            capo_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notificationscontacts.types.delete_email_contact_request.DeleteEmailContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_notificationscontacts.types.delete_email_contact_response.DeleteEmailContactResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.delete_email_contact

            (
                output,
                http_response,
            ) = await capo_notificationscontacts._operations.notifications_contacts.delete_email_contact.async_delete_email_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.delete_email_contact_request.DeleteEmailContactRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_email_contacts(
        self,
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_notificationscontacts.types.list_email_contacts_response.ListEmailContactsResponse":
        """<p>Lists all email contacts created under the Account.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>

        Raises:
            capo_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notificationscontacts.types.list_email_contacts_request.ListEmailContactsRequest]",
        ) -> AsyncOperationResponse[
            "capo_notificationscontacts.types.list_email_contacts_response.ListEmailContactsResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.list_email_contacts

            (
                output,
                http_response,
            ) = await capo_notificationscontacts._operations.notifications_contacts.list_email_contacts.async_list_email_contacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.list_email_contacts_request.ListEmailContactsRequest = {}
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

    async def iter_list_email_contacts(
        self,
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_notificationscontacts.types.email_contact.EmailContact]":
        _token = next_token
        while True:
            _response = await self.list_email_contacts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("email_contacts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def activate_email_contact(
        self,
        arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn",
        code: "capo_notificationscontacts.types.token.Token",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
    ) -> "capo_notificationscontacts.types.activate_email_contact_response.ActivateEmailContactResponse":
        """<p>Activates an email contact using an activation code. This code is in the activation email sent to the email address associated with this email contact.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            code: <p>The activation code for this email contact.</p> <p>An email contact has a maximum of five activation attempts. Activation codes expire after 12 hours and are generated by the <a href="https://docs.aws.amazon.com/notificationscontacts/latest/APIReference/API_SendActivationCode.html">SendActivationCode</a> API action.</p>

        Raises:
            capo_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_notificationscontacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notificationscontacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Your request references a resource which does not exist. </p>
            capo_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notificationscontacts.types.activate_email_contact_request.ActivateEmailContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_notificationscontacts.types.activate_email_contact_response.ActivateEmailContactResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.activate_email_contact

            (
                output,
                http_response,
            ) = await capo_notificationscontacts._operations.notifications_contacts.activate_email_contact.async_activate_email_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.activate_email_contact_request.ActivateEmailContactRequest = {
            "arn": arn,
            "code": code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_activation_code(
        self,
        arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
    ) -> "capo_notificationscontacts.types.send_activation_code_response.SendActivationCodeResponse":
        """<p>Sends an activation email to the email address associated with the specified email contact.</p> <note> <p>It might take a few minutes for the activation email to arrive. If it doesn't arrive, check in your spam folder or try sending another activation email.</p> </note>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_notificationscontacts.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notificationscontacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Your request references a resource which does not exist. </p>
            capo_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notificationscontacts.types.send_activation_code_request.SendActivationCodeRequest]",
        ) -> AsyncOperationResponse[
            "capo_notificationscontacts.types.send_activation_code_response.SendActivationCodeResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.send_activation_code

            (
                output,
                http_response,
            ) = await capo_notificationscontacts._operations.notifications_contacts.send_activation_code.async_send_activation_code(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.send_activation_code_request.SendActivationCodeRequest = {
            "arn": arn
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
