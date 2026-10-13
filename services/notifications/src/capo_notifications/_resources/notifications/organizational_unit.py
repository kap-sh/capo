from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_notifications._auth._signers
import capo_notifications._auth._sigv4
from capo_notifications._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_notifications.types.associate_organizational_unit_request
    import capo_notifications.types.associate_organizational_unit_response
    import capo_notifications.types.disassociate_organizational_unit_request
    import capo_notifications.types.disassociate_organizational_unit_response
    import capo_notifications.types.list_organizational_units_request
    import capo_notifications.types.list_organizational_units_response
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.organizational_unit_id
    from capo_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from capo_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class OrganizationalUnit:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def put(
        self,
        organizational_unit_id: "capo_notifications.types.organizational_unit_id.OrganizationalUnitId",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.associate_organizational_unit_response.AssociateOrganizationalUnitResponse":
        """<p>Associates an organizational unit with a notification configuration.</p>

        Args:
            organizational_unit_id: <p>The unique identifier of the organizational unit to associate.</p>
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration to associate with the organizational unit.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.associate_organizational_unit_request.AssociateOrganizationalUnitRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.associate_organizational_unit_response.AssociateOrganizationalUnitResponse"
        ]:
            import capo_notifications._operations.notifications.associate_organizational_unit

            output, http_response = (
                capo_notifications._operations.notifications.associate_organizational_unit.associate_organizational_unit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateOrganizationalUnit")
        )
        input_: capo_notifications.types.associate_organizational_unit_request.AssociateOrganizationalUnitRequest = {
            "organizational_unit_id": organizational_unit_id,
            "notification_configuration_arn": notification_configuration_arn,
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
        organizational_unit_id: "capo_notifications.types.organizational_unit_id.OrganizationalUnitId",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.disassociate_organizational_unit_response.DisassociateOrganizationalUnitResponse":
        """<p>Removes the association between an organizational unit and a notification configuration.</p>

        Args:
            organizational_unit_id: <p>The unique identifier of the organizational unit to disassociate.</p>
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration to disassociate from the organizational unit.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.disassociate_organizational_unit_request.DisassociateOrganizationalUnitRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.disassociate_organizational_unit_response.DisassociateOrganizationalUnitResponse"
        ]:
            import capo_notifications._operations.notifications.disassociate_organizational_unit

            output, http_response = (
                capo_notifications._operations.notifications.disassociate_organizational_unit.disassociate_organizational_unit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateOrganizationalUnit")
        )
        input_: capo_notifications.types.disassociate_organizational_unit_request.DisassociateOrganizationalUnitRequest = {
            "organizational_unit_id": organizational_unit_id,
            "notification_configuration_arn": notification_configuration_arn,
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
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_organizational_units_response.ListOrganizationalUnitsResponse":
        """<p>Returns a list of organizational units associated with a notification configuration.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration used to filter the organizational units.</p>
            max_results: <p>The maximum number of organizational units to return in a single call. Valid values are 1-100.</p>
            next_token: <p>The token for the next page of results. Use the value returned in the previous response.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_organizational_units_request.ListOrganizationalUnitsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_organizational_units_response.ListOrganizationalUnitsResponse"
        ]:
            import capo_notifications._operations.notifications.list_organizational_units

            output, http_response = (
                capo_notifications._operations.notifications.list_organizational_units.list_organizational_units(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListOrganizationalUnits")
        )
        input_: capo_notifications.types.list_organizational_units_request.ListOrganizationalUnitsRequest = {
            "notification_configuration_arn": notification_configuration_arn
        }
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


class AsyncOrganizationalUnit:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def put(
        self,
        organizational_unit_id: "capo_notifications.types.organizational_unit_id.OrganizationalUnitId",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "capo_notifications.types.associate_organizational_unit_response.AssociateOrganizationalUnitResponse":
        """<p>Associates an organizational unit with a notification configuration.</p>

        Args:
            organizational_unit_id: <p>The unique identifier of the organizational unit to associate.</p>
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration to associate with the organizational unit.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.associate_organizational_unit_request.AssociateOrganizationalUnitRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.associate_organizational_unit_response.AssociateOrganizationalUnitResponse"
        ]:
            import capo_notifications._operations.notifications.associate_organizational_unit

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.associate_organizational_unit.async_associate_organizational_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateOrganizationalUnit")
        )
        input_: capo_notifications.types.associate_organizational_unit_request.AssociateOrganizationalUnitRequest = {
            "organizational_unit_id": organizational_unit_id,
            "notification_configuration_arn": notification_configuration_arn,
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
        organizational_unit_id: "capo_notifications.types.organizational_unit_id.OrganizationalUnitId",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "capo_notifications.types.disassociate_organizational_unit_response.DisassociateOrganizationalUnitResponse":
        """<p>Removes the association between an organizational unit and a notification configuration.</p>

        Args:
            organizational_unit_id: <p>The unique identifier of the organizational unit to disassociate.</p>
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration to disassociate from the organizational unit.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.disassociate_organizational_unit_request.DisassociateOrganizationalUnitRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.disassociate_organizational_unit_response.DisassociateOrganizationalUnitResponse"
        ]:
            import capo_notifications._operations.notifications.disassociate_organizational_unit

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.disassociate_organizational_unit.async_disassociate_organizational_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateOrganizationalUnit")
        )
        input_: capo_notifications.types.disassociate_organizational_unit_request.DisassociateOrganizationalUnitRequest = {
            "organizational_unit_id": organizational_unit_id,
            "notification_configuration_arn": notification_configuration_arn,
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
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_organizational_units_response.ListOrganizationalUnitsResponse":
        """<p>Returns a list of organizational units associated with a notification configuration.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration used to filter the organizational units.</p>
            max_results: <p>The maximum number of organizational units to return in a single call. Valid values are 1-100.</p>
            next_token: <p>The token for the next page of results. Use the value returned in the previous response.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.list_organizational_units_request.ListOrganizationalUnitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.list_organizational_units_response.ListOrganizationalUnitsResponse"
        ]:
            import capo_notifications._operations.notifications.list_organizational_units

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.list_organizational_units.async_list_organizational_units(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListOrganizationalUnits")
        )
        input_: capo_notifications.types.list_organizational_units_request.ListOrganizationalUnitsRequest = {
            "notification_configuration_arn": notification_configuration_arn
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
