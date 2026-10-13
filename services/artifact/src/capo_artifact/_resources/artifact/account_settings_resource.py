from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_artifact._auth._signers
import capo_artifact._auth._sigv4
from capo_artifact._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_artifact.types.get_account_settings_request
    import capo_artifact.types.get_account_settings_response
    import capo_artifact.types.notification_subscription_status
    import capo_artifact.types.put_account_settings_request
    import capo_artifact.types.put_account_settings_response
    from capo_artifact._services.artifact import ArtifactClient, ArtifactClientConfig
    from capo_artifact._services.async_artifact import (
        AsyncArtifactClient,
        AsyncArtifactClientConfig,
    )


class AccountSettingsResource:
    def __init__(self, service: ArtifactClient) -> None:
        self._service = service

    def get_account_settings(
        self, *, config_overrides: Optional[ArtifactClientConfig] = None
    ) -> "capo_artifact.types.get_account_settings_response.GetAccountSettingsResponse":
        """<p>Get the account settings for Artifact.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetAccountSettings operation
            Get the current account settings.

            >>> client.get_account_settings()
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.get_account_settings_request.GetAccountSettingsRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.get_account_settings_response.GetAccountSettingsResponse"
        ]:
            import capo_artifact._operations.artifact.get_account_settings

            output, http_response = (
                capo_artifact._operations.artifact.get_account_settings.get_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAccountSettings")
        )
        input_: capo_artifact.types.get_account_settings_request.GetAccountSettingsRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_account_settings(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        notification_subscription_status: Optional[
            "capo_artifact.types.notification_subscription_status.NotificationSubscriptionStatus"
        ] = None,
    ) -> "capo_artifact.types.put_account_settings_response.PutAccountSettingsResponse":
        """<p>Put the account settings for Artifact.</p>

        Args:
            notification_subscription_status: <p>Desired notification subscription status.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke PutAccountSettings operation
            Set the account settings.

            >>> client.put_account_settings(notification_subscription_status='SUBSCRIBED')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.put_account_settings_request.PutAccountSettingsRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.put_account_settings_response.PutAccountSettingsResponse"
        ]:
            import capo_artifact._operations.artifact.put_account_settings

            output, http_response = (
                capo_artifact._operations.artifact.put_account_settings.put_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutAccountSettings")
        )
        input_: capo_artifact.types.put_account_settings_request.PutAccountSettingsRequest = {}
        if notification_subscription_status is not None:
            input_["notification_subscription_status"] = (
                notification_subscription_status
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAccountSettingsResource:
    def __init__(self, service: AsyncArtifactClient) -> None:
        self._service = service

    async def get_account_settings(
        self, *, config_overrides: Optional[AsyncArtifactClientConfig] = None
    ) -> "capo_artifact.types.get_account_settings_response.GetAccountSettingsResponse":
        """<p>Get the account settings for Artifact.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetAccountSettings operation
            Get the current account settings.

            >>> await client.get_account_settings()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.get_account_settings_request.GetAccountSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.get_account_settings_response.GetAccountSettingsResponse"
        ]:
            import capo_artifact._operations.artifact.get_account_settings

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.get_account_settings.async_get_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAccountSettings")
        )
        input_: capo_artifact.types.get_account_settings_request.GetAccountSettingsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_settings(
        self,
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        notification_subscription_status: Optional[
            "capo_artifact.types.notification_subscription_status.NotificationSubscriptionStatus"
        ] = None,
    ) -> "capo_artifact.types.put_account_settings_response.PutAccountSettingsResponse":
        """<p>Put the account settings for Artifact.</p>

        Args:
            notification_subscription_status: <p>Desired notification subscription status.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke PutAccountSettings operation
            Set the account settings.

            >>> await client.put_account_settings(notification_subscription_status='SUBSCRIBED')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.put_account_settings_request.PutAccountSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.put_account_settings_response.PutAccountSettingsResponse"
        ]:
            import capo_artifact._operations.artifact.put_account_settings

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.put_account_settings.async_put_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutAccountSettings")
        )
        input_: capo_artifact.types.put_account_settings_request.PutAccountSettingsRequest = {}
        if notification_subscription_status is not None:
            input_["notification_subscription_status"] = (
                notification_subscription_status
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
