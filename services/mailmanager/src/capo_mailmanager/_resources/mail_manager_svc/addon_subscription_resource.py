from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_mailmanager._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mailmanager.types.addon_name
    import capo_mailmanager.types.addon_subscription
    import capo_mailmanager.types.addon_subscription_id
    import capo_mailmanager.types.create_addon_subscription_request
    import capo_mailmanager.types.create_addon_subscription_response
    import capo_mailmanager.types.delete_addon_subscription_request
    import capo_mailmanager.types.delete_addon_subscription_response
    import capo_mailmanager.types.get_addon_subscription_request
    import capo_mailmanager.types.get_addon_subscription_response
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.list_addon_subscriptions_request
    import capo_mailmanager.types.list_addon_subscriptions_response
    import capo_mailmanager.types.page_size
    import capo_mailmanager.types.pagination_token
    import capo_mailmanager.types.tag_list
    from capo_mailmanager._services.async_mail_manager import (
        AsyncMailManagerClient,
        AsyncMailManagerClientConfig,
    )
    from capo_mailmanager._services.mail_manager import (
        MailManagerClient,
        MailManagerClientConfig,
    )


class AddonSubscriptionResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        addon_name: "capo_mailmanager.types.addon_name.AddonName",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_addon_subscription_response.CreateAddonSubscriptionResponse":
        """<p>Creates a subscription for an Add On representing the acceptance of its terms of use and additional pricing. The subscription can then be used to create an instance for use in rule sets or traffic policies.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            addon_name: <p>The name of the Add On to subscribe to. You can only have one subscription for each Add On name.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.create_addon_subscription_request.CreateAddonSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.create_addon_subscription_response.CreateAddonSubscriptionResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_addon_subscription

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.create_addon_subscription.create_addon_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_addon_subscription_request.CreateAddonSubscriptionRequest = {
            "addon_name": addon_name
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

    def read(
        self,
        addon_subscription_id: "capo_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_addon_subscription_response.GetAddonSubscriptionResponse":
        """<p>Gets detailed information about an Add On subscription.</p>

        Args:
            addon_subscription_id: <p>The Add On subscription ID to retrieve information for.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.get_addon_subscription_request.GetAddonSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.get_addon_subscription_response.GetAddonSubscriptionResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_addon_subscription

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.get_addon_subscription.get_addon_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_addon_subscription_request.GetAddonSubscriptionRequest = {
            "addon_subscription_id": addon_subscription_id
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
        addon_subscription_id: "capo_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_addon_subscription_response.DeleteAddonSubscriptionResponse":
        """<p>Deletes an Add On subscription.</p>

        Args:
            addon_subscription_id: <p>The Add On subscription ID to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.delete_addon_subscription_request.DeleteAddonSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.delete_addon_subscription_response.DeleteAddonSubscriptionResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_addon_subscription

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.delete_addon_subscription.delete_addon_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_addon_subscription_request.DeleteAddonSubscriptionRequest = {
            "addon_subscription_id": addon_subscription_id
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
        config_overrides: Optional[MailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_addon_subscriptions_response.ListAddonSubscriptionsResponse":
        """<p>Lists all Add On subscriptions in your account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints. </p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.list_addon_subscriptions_request.ListAddonSubscriptionsRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.list_addon_subscriptions_response.ListAddonSubscriptionsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_addon_subscriptions

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.list_addon_subscriptions.list_addon_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_addon_subscriptions_request.ListAddonSubscriptionsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAddonSubscriptionResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        addon_name: "capo_mailmanager.types.addon_name.AddonName",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_addon_subscription_response.CreateAddonSubscriptionResponse":
        """<p>Creates a subscription for an Add On representing the acceptance of its terms of use and additional pricing. The subscription can then be used to create an instance for use in rule sets or traffic policies.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            addon_name: <p>The name of the Add On to subscribe to. You can only have one subscription for each Add On name.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_addon_subscription_request.CreateAddonSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_addon_subscription_response.CreateAddonSubscriptionResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_addon_subscription

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_addon_subscription.async_create_addon_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_addon_subscription_request.CreateAddonSubscriptionRequest = {
            "addon_name": addon_name
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

    async def read(
        self,
        addon_subscription_id: "capo_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_addon_subscription_response.GetAddonSubscriptionResponse":
        """<p>Gets detailed information about an Add On subscription.</p>

        Args:
            addon_subscription_id: <p>The Add On subscription ID to retrieve information for.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_addon_subscription_request.GetAddonSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_addon_subscription_response.GetAddonSubscriptionResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_addon_subscription

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_addon_subscription.async_get_addon_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_addon_subscription_request.GetAddonSubscriptionRequest = {
            "addon_subscription_id": addon_subscription_id
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
        addon_subscription_id: "capo_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_addon_subscription_response.DeleteAddonSubscriptionResponse":
        """<p>Deletes an Add On subscription.</p>

        Args:
            addon_subscription_id: <p>The Add On subscription ID to delete.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_addon_subscription_request.DeleteAddonSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_addon_subscription_response.DeleteAddonSubscriptionResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_addon_subscription

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_addon_subscription.async_delete_addon_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_addon_subscription_request.DeleteAddonSubscriptionRequest = {
            "addon_subscription_id": addon_subscription_id
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
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["capo_mailmanager.types.page_size.PageSize"] = None,
    ) -> "capo_mailmanager.types.list_addon_subscriptions_response.ListAddonSubscriptionsResponse":
        """<p>Lists all Add On subscriptions in your account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints. </p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_addon_subscriptions_request.ListAddonSubscriptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_addon_subscriptions_response.ListAddonSubscriptionsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_addon_subscriptions

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_addon_subscriptions.async_list_addon_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_addon_subscriptions_request.ListAddonSubscriptionsRequest = {}
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
