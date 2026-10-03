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
    import capo_mailmanager.types.address_list
    import capo_mailmanager.types.address_list_id
    import capo_mailmanager.types.address_list_name
    import capo_mailmanager.types.create_address_list_request
    import capo_mailmanager.types.create_address_list_response
    import capo_mailmanager.types.delete_address_list_request
    import capo_mailmanager.types.delete_address_list_response
    import capo_mailmanager.types.get_address_list_request
    import capo_mailmanager.types.get_address_list_response
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.list_address_lists_request
    import capo_mailmanager.types.list_address_lists_response
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


class AddressListResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        address_list_name: "capo_mailmanager.types.address_list_name.AddressListName",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> (
        "capo_mailmanager.types.create_address_list_response.CreateAddressListResponse"
    ):
        """<p>Creates a new address list.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            address_list_name: <p>A user-friendly name for the address list.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.create_address_list_request.CreateAddressListRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.create_address_list_response.CreateAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_address_list

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.create_address_list.create_address_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_address_list_request.CreateAddressListRequest = {
            "address_list_name": address_list_name
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
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_address_list_response.GetAddressListResponse":
        """<p>Fetch attributes of an address list.</p>

        Args:
            address_list_id: <p>The identifier of an existing address list resource to be retrieved.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.get_address_list_request.GetAddressListRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.get_address_list_response.GetAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_address_list

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.get_address_list.get_address_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_address_list_request.GetAddressListRequest = {
            "address_list_id": address_list_id
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
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> (
        "capo_mailmanager.types.delete_address_list_response.DeleteAddressListResponse"
    ):
        """<p>Deletes an address list.</p>

        Args:
            address_list_id: <p>The identifier of an existing address list resource to delete.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.delete_address_list_request.DeleteAddressListRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.delete_address_list_response.DeleteAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_address_list

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.delete_address_list.delete_address_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_address_list_request.DeleteAddressListRequest = {
            "address_list_id": address_list_id
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
    ) -> "capo_mailmanager.types.list_address_lists_response.ListAddressListsResponse":
        """<p>Lists address lists for this account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of address list resources that are returned per call. You can use NextToken to retrieve the next page of address lists.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.list_address_lists_request.ListAddressListsRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.list_address_lists_response.ListAddressListsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_address_lists

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.list_address_lists.list_address_lists(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_address_lists_request.ListAddressListsRequest = {}
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


class AsyncAddressListResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        address_list_name: "capo_mailmanager.types.address_list_name.AddressListName",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> (
        "capo_mailmanager.types.create_address_list_response.CreateAddressListResponse"
    ):
        """<p>Creates a new address list.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            address_list_name: <p>A user-friendly name for the address list.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_address_list_request.CreateAddressListRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_address_list_response.CreateAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_address_list

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_address_list.async_create_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_address_list_request.CreateAddressListRequest = {
            "address_list_name": address_list_name
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
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_address_list_response.GetAddressListResponse":
        """<p>Fetch attributes of an address list.</p>

        Args:
            address_list_id: <p>The identifier of an existing address list resource to be retrieved.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_address_list_request.GetAddressListRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_address_list_response.GetAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_address_list

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_address_list.async_get_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_address_list_request.GetAddressListRequest = {
            "address_list_id": address_list_id
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
        address_list_id: "capo_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> (
        "capo_mailmanager.types.delete_address_list_response.DeleteAddressListResponse"
    ):
        """<p>Deletes an address list.</p>

        Args:
            address_list_id: <p>The identifier of an existing address list resource to delete.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_address_list_request.DeleteAddressListRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_address_list_response.DeleteAddressListResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_address_list

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_address_list.async_delete_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_address_list_request.DeleteAddressListRequest = {
            "address_list_id": address_list_id
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
    ) -> "capo_mailmanager.types.list_address_lists_response.ListAddressListsResponse":
        """<p>Lists address lists for this account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of address list resources that are returned per call. You can use NextToken to retrieve the next page of address lists.</p>

        Raises:
            capo_mailmanager.errors.access_denied_exception.AccessDeniedException: <p>Occurs when a user is denied access to a specific resource or action.</p>
            capo_mailmanager.errors.throttling_exception.ThrottlingException: <p>Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_address_lists_request.ListAddressListsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_address_lists_response.ListAddressListsResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_address_lists

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_address_lists.async_list_address_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_address_lists_request.ListAddressListsRequest = {}
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
