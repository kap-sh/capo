from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_notificationscontacts._auth._signers
import capo_notificationscontacts._auth._sigv4
from capo_notificationscontacts._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
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
    import capo_notificationscontacts.types.send_activation_code_request
    import capo_notificationscontacts.types.send_activation_code_response
    import capo_notificationscontacts.types.tag_map
    import capo_notificationscontacts.types.token
    from capo_notificationscontacts._services.async_notifications_contacts import (
        AsyncNotificationsContactsClient,
        AsyncNotificationsContactsClientConfig,
    )
    from capo_notificationscontacts._services.notifications_contacts import (
        NotificationsContactsClient,
        NotificationsContactsClientConfig,
    )


class EmailContactResource:
    def __init__(self, service: NotificationsContactsClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_notificationscontacts.types.email_contact_name.EmailContactName",
        email_address: "capo_notificationscontacts.types.email_contact_address.EmailContactAddress",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_notificationscontacts.types.create_email_contact_request.CreateEmailContactRequest]",
        ) -> OperationResponse[
            "capo_notificationscontacts.types.create_email_contact_response.CreateEmailContactResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.create_email_contact

            output, http_response = (
                capo_notificationscontacts._operations.notifications_contacts.create_email_contact.create_email_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.create_email_contact_request.CreateEmailContactRequest = {
            "name": name,
            "email_address": email_address,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_notificationscontacts.types.get_email_contact_request.GetEmailContactRequest]",
        ) -> OperationResponse[
            "capo_notificationscontacts.types.get_email_contact_response.GetEmailContactResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.get_email_contact

            output, http_response = (
                capo_notificationscontacts._operations.notifications_contacts.get_email_contact.get_email_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.get_email_contact_request.GetEmailContactRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_notificationscontacts.types.delete_email_contact_request.DeleteEmailContactRequest]",
        ) -> OperationResponse[
            "capo_notificationscontacts.types.delete_email_contact_response.DeleteEmailContactResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.delete_email_contact

            output, http_response = (
                capo_notificationscontacts._operations.notifications_contacts.delete_email_contact.delete_email_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.delete_email_contact_request.DeleteEmailContactRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_notificationscontacts.types.list_email_contacts_request.ListEmailContactsRequest]",
        ) -> OperationResponse[
            "capo_notificationscontacts.types.list_email_contacts_response.ListEmailContactsResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.list_email_contacts

            output, http_response = (
                capo_notificationscontacts._operations.notifications_contacts.list_email_contacts.list_email_contacts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.list_email_contacts_request.ListEmailContactsRequest = {}
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

    def activate_email_contact(
        self,
        arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn",
        code: "capo_notificationscontacts.types.token.Token",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_notificationscontacts.types.activate_email_contact_request.ActivateEmailContactRequest]",
        ) -> OperationResponse[
            "capo_notificationscontacts.types.activate_email_contact_response.ActivateEmailContactResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.activate_email_contact

            output, http_response = (
                capo_notificationscontacts._operations.notifications_contacts.activate_email_contact.activate_email_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.activate_email_contact_request.ActivateEmailContactRequest = {
            "arn": arn,
            "code": code,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_activation_code(
        self,
        arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_notificationscontacts.types.send_activation_code_request.SendActivationCodeRequest]",
        ) -> OperationResponse[
            "capo_notificationscontacts.types.send_activation_code_response.SendActivationCodeResponse"
        ]:
            import capo_notificationscontacts._operations.notifications_contacts.send_activation_code

            output, http_response = (
                capo_notificationscontacts._operations.notifications_contacts.send_activation_code.send_activation_code(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notificationscontacts.types.send_activation_code_request.SendActivationCodeRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEmailContactResource:
    def __init__(self, service: AsyncNotificationsContactsClient) -> None:
        self._service = service

    async def create(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def read(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def list(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
