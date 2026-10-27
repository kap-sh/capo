from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_deadline._auth._signers
import capo_deadline._auth._sigv4
from capo_deadline._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.create_monitor_request
    import capo_deadline.types.create_monitor_response
    import capo_deadline.types.delete_monitor_request
    import capo_deadline.types.delete_monitor_response
    import capo_deadline.types.get_monitor_request
    import capo_deadline.types.get_monitor_response
    import capo_deadline.types.get_monitor_settings_request
    import capo_deadline.types.get_monitor_settings_response
    import capo_deadline.types.iam_role_arn
    import capo_deadline.types.identity_center_instance_arn
    import capo_deadline.types.list_monitors_request
    import capo_deadline.types.list_monitors_response
    import capo_deadline.types.max_results
    import capo_deadline.types.monitor_id
    import capo_deadline.types.monitor_summary
    import capo_deadline.types.next_token
    import capo_deadline.types.region
    import capo_deadline.types.resource_name
    import capo_deadline.types.settings_map
    import capo_deadline.types.subdomain
    import capo_deadline.types.tags
    import capo_deadline.types.update_monitor_request
    import capo_deadline.types.update_monitor_response
    import capo_deadline.types.update_monitor_settings_request
    import capo_deadline.types.update_monitor_settings_response
    from capo_deadline._services.async_deadline import (
        AsyncdeadlineClient,
        AsyncdeadlineClientConfig,
    )
    from capo_deadline._services.deadline import deadlineClient, deadlineClientConfig


class MonitorResource:
    def __init__(self, service: deadlineClient) -> None:
        self._service = service

    def create(
        self,
        display_name: "capo_deadline.types.resource_name.ResourceName",
        identity_center_instance_arn: "capo_deadline.types.identity_center_instance_arn.IdentityCenterInstanceArn",
        subdomain: "capo_deadline.types.subdomain.Subdomain",
        role_arn: "capo_deadline.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        identity_center_region: Optional["capo_deadline.types.region.Region"] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_monitor_response.CreateMonitorResponse":
        """<p>Creates an Amazon Web Services Deadline Cloud monitor that you can use to view your farms, queues, and fleets. After you submit a job, you can track the progress of the tasks and steps that make up the job, and then download the job's results. </p>

        Args:
            client_token: The unique token which the server uses to recognize retries of the same request.
            display_name: <p>The name that you give the monitor that is displayed in the Deadline Cloud console.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            identity_center_instance_arn: The Amazon Resource Name of the IAM Identity Center instance that authenticates monitor users.
            identity_center_region: The Region where IAM Identity Center is enabled. Required when IAM Identity Center is in a different Region than the monitor.
            subdomain: The subdomain to use when creating the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.
            role_arn: The Amazon Resource Name of the IAM role that the monitor uses to connect to Deadline Cloud. Every user that signs in to the monitor using IAM Identity Center uses this role to access Deadline Cloud resources.
            tags: The tags to add to your monitor. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_monitor_request.CreateMonitorRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_monitor_response.CreateMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.create_monitor

            output, http_response = (
                capo_deadline._operations.deadline.create_monitor.create_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateMonitor")
        )
        input_: capo_deadline.types.create_monitor_request.CreateMonitorRequest = {
            "display_name": display_name,
            "identity_center_instance_arn": identity_center_instance_arn,
            "subdomain": subdomain,
            "role_arn": role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region
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
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_monitor_response.GetMonitorResponse":
        """Gets information about the specified monitor.

        Args:
            monitor_id: The unique identifier for the monitor. This ID is returned by the <code>CreateMonitor</code> operation.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_monitor_request.GetMonitorRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_monitor_response.GetMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.get_monitor

            output, http_response = (
                capo_deadline._operations.deadline.get_monitor.get_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMonitor")
        )
        input_: capo_deadline.types.get_monitor_request.GetMonitorRequest = {
            "monitor_id": monitor_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        subdomain: Optional["capo_deadline.types.subdomain.Subdomain"] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        role_arn: Optional["capo_deadline.types.iam_role_arn.IamRoleArn"] = None,
    ) -> "capo_deadline.types.update_monitor_response.UpdateMonitorResponse":
        """Modifies the settings for a Deadline Cloud monitor. You can modify one or all of the settings when you call <code>UpdateMonitor</code>.

        Args:
            monitor_id: The unique identifier of the monitor to update.
            subdomain: The new value of the subdomain to use when forming the monitor URL.
            display_name: <p>The new value to use for the monitor's display name.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            role_arn: The Amazon Resource Name of the new IAM role to use with the monitor.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_monitor_request.UpdateMonitorRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_monitor_response.UpdateMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.update_monitor

            output, http_response = (
                capo_deadline._operations.deadline.update_monitor.update_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateMonitor")
        )
        input_: capo_deadline.types.update_monitor_request.UpdateMonitorRequest = {
            "monitor_id": monitor_id
        }
        if subdomain is not None:
            input_["subdomain"] = subdomain
        if display_name is not None:
            input_["display_name"] = display_name
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_monitor_response.DeleteMonitorResponse":
        """Removes a Deadline Cloud monitor. After you delete a monitor, you can create a new one and attach farms to the monitor.

        Args:
            monitor_id: The unique identifier of the monitor to delete. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>GetMonitor</code> operation.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_monitor_request.DeleteMonitorRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_monitor_response.DeleteMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.delete_monitor

            output, http_response = (
                capo_deadline._operations.deadline.delete_monitor.delete_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMonitor")
        )
        input_: capo_deadline.types.delete_monitor_request.DeleteMonitorRequest = {
            "monitor_id": monitor_id
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
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_monitors_response.ListMonitorsResponse":
        """Gets a list of your monitors in Deadline Cloud.

        Args:
            next_token: The token for the next set of results, or <code>null</code> to start from the beginning.
            max_results: The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_monitors_request.ListMonitorsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_monitors_response.ListMonitorsResponse"
        ]:
            import capo_deadline._operations.deadline.list_monitors

            output, http_response = (
                capo_deadline._operations.deadline.list_monitors.list_monitors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMonitors")
        )
        input_: capo_deadline.types.list_monitors_request.ListMonitorsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_monitor_settings(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_monitor_settings_response.GetMonitorSettingsResponse":
        """Gets the settings for a Deadline Cloud monitor.

        Args:
            monitor_id: The unique identifier of the monitor. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>ListMonitors</code> operation.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get monitor settings

            >>> client.get_monitor_settings(monitor_id='monitor-1234567890abcdef1234567890abcdef')
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_monitor_settings_request.GetMonitorSettingsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_monitor_settings_response.GetMonitorSettingsResponse"
        ]:
            import capo_deadline._operations.deadline.get_monitor_settings

            output, http_response = (
                capo_deadline._operations.deadline.get_monitor_settings.get_monitor_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMonitorSettings")
        )
        input_: capo_deadline.types.get_monitor_settings_request.GetMonitorSettingsRequest = {
            "monitor_id": monitor_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_monitor_settings(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        settings: "capo_deadline.types.settings_map.SettingsMap",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.update_monitor_settings_response.UpdateMonitorSettingsResponse":
        """Updates the settings for a Deadline Cloud monitor. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key.

        Args:
            monitor_id: The unique identifier of the monitor to update settings for.
            settings: The monitor settings to update as key-value pairs. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update monitor settings

            >>> client.update_monitor_settings(monitor_id='monitor-1234567890abcdef1234567890abcdef', settings={'idcApplicationArn': 'arn:aws:sso::123456789012:application/ins-1234567890abcdef/apl-1234567890abcdef'})
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_monitor_settings_request.UpdateMonitorSettingsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_monitor_settings_response.UpdateMonitorSettingsResponse"
        ]:
            import capo_deadline._operations.deadline.update_monitor_settings

            output, http_response = (
                capo_deadline._operations.deadline.update_monitor_settings.update_monitor_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateMonitorSettings")
        )
        input_: capo_deadline.types.update_monitor_settings_request.UpdateMonitorSettingsRequest = {
            "monitor_id": monitor_id,
            "settings": settings,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMonitorResource:
    def __init__(self, service: AsyncdeadlineClient) -> None:
        self._service = service

    async def create(
        self,
        display_name: "capo_deadline.types.resource_name.ResourceName",
        identity_center_instance_arn: "capo_deadline.types.identity_center_instance_arn.IdentityCenterInstanceArn",
        subdomain: "capo_deadline.types.subdomain.Subdomain",
        role_arn: "capo_deadline.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        identity_center_region: Optional["capo_deadline.types.region.Region"] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_monitor_response.CreateMonitorResponse":
        """<p>Creates an Amazon Web Services Deadline Cloud monitor that you can use to view your farms, queues, and fleets. After you submit a job, you can track the progress of the tasks and steps that make up the job, and then download the job's results. </p>

        Args:
            client_token: The unique token which the server uses to recognize retries of the same request.
            display_name: <p>The name that you give the monitor that is displayed in the Deadline Cloud console.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            identity_center_instance_arn: The Amazon Resource Name of the IAM Identity Center instance that authenticates monitor users.
            identity_center_region: The Region where IAM Identity Center is enabled. Required when IAM Identity Center is in a different Region than the monitor.
            subdomain: The subdomain to use when creating the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.
            role_arn: The Amazon Resource Name of the IAM role that the monitor uses to connect to Deadline Cloud. Every user that signs in to the monitor using IAM Identity Center uses this role to access Deadline Cloud resources.
            tags: The tags to add to your monitor. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.create_monitor_request.CreateMonitorRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.create_monitor_response.CreateMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.create_monitor

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.create_monitor.async_create_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateMonitor")
        )
        input_: capo_deadline.types.create_monitor_request.CreateMonitorRequest = {
            "display_name": display_name,
            "identity_center_instance_arn": identity_center_instance_arn,
            "subdomain": subdomain,
            "role_arn": role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region
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
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_monitor_response.GetMonitorResponse":
        """Gets information about the specified monitor.

        Args:
            monitor_id: The unique identifier for the monitor. This ID is returned by the <code>CreateMonitor</code> operation.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.get_monitor_request.GetMonitorRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.get_monitor_response.GetMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.get_monitor

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.get_monitor.async_get_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMonitor")
        )
        input_: capo_deadline.types.get_monitor_request.GetMonitorRequest = {
            "monitor_id": monitor_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        subdomain: Optional["capo_deadline.types.subdomain.Subdomain"] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        role_arn: Optional["capo_deadline.types.iam_role_arn.IamRoleArn"] = None,
    ) -> "capo_deadline.types.update_monitor_response.UpdateMonitorResponse":
        """Modifies the settings for a Deadline Cloud monitor. You can modify one or all of the settings when you call <code>UpdateMonitor</code>.

        Args:
            monitor_id: The unique identifier of the monitor to update.
            subdomain: The new value of the subdomain to use when forming the monitor URL.
            display_name: <p>The new value to use for the monitor's display name.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            role_arn: The Amazon Resource Name of the new IAM role to use with the monitor.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.update_monitor_request.UpdateMonitorRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.update_monitor_response.UpdateMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.update_monitor

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.update_monitor.async_update_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateMonitor")
        )
        input_: capo_deadline.types.update_monitor_request.UpdateMonitorRequest = {
            "monitor_id": monitor_id
        }
        if subdomain is not None:
            input_["subdomain"] = subdomain
        if display_name is not None:
            input_["display_name"] = display_name
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_monitor_response.DeleteMonitorResponse":
        """Removes a Deadline Cloud monitor. After you delete a monitor, you can create a new one and attach farms to the monitor.

        Args:
            monitor_id: The unique identifier of the monitor to delete. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>GetMonitor</code> operation.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.delete_monitor_request.DeleteMonitorRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.delete_monitor_response.DeleteMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.delete_monitor

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.delete_monitor.async_delete_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMonitor")
        )
        input_: capo_deadline.types.delete_monitor_request.DeleteMonitorRequest = {
            "monitor_id": monitor_id
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
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_monitors_response.ListMonitorsResponse":
        """Gets a list of your monitors in Deadline Cloud.

        Args:
            next_token: The token for the next set of results, or <code>null</code> to start from the beginning.
            max_results: The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.list_monitors_request.ListMonitorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.list_monitors_response.ListMonitorsResponse"
        ]:
            import capo_deadline._operations.deadline.list_monitors

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.list_monitors.async_list_monitors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMonitors")
        )
        input_: capo_deadline.types.list_monitors_request.ListMonitorsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_monitor_settings(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_monitor_settings_response.GetMonitorSettingsResponse":
        """Gets the settings for a Deadline Cloud monitor.

        Args:
            monitor_id: The unique identifier of the monitor. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>ListMonitors</code> operation.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get monitor settings

            >>> await client.get_monitor_settings(monitor_id='monitor-1234567890abcdef1234567890abcdef')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.get_monitor_settings_request.GetMonitorSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.get_monitor_settings_response.GetMonitorSettingsResponse"
        ]:
            import capo_deadline._operations.deadline.get_monitor_settings

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.get_monitor_settings.async_get_monitor_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMonitorSettings")
        )
        input_: capo_deadline.types.get_monitor_settings_request.GetMonitorSettingsRequest = {
            "monitor_id": monitor_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_monitor_settings(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        settings: "capo_deadline.types.settings_map.SettingsMap",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "capo_deadline.types.update_monitor_settings_response.UpdateMonitorSettingsResponse":
        """Updates the settings for a Deadline Cloud monitor. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key.

        Args:
            monitor_id: The unique identifier of the monitor to update settings for.
            settings: The monitor settings to update as key-value pairs. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key.

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: You don't have permission to perform the action.
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: Deadline Cloud can't process your request right now. Try again later.
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource can't be found.
            capo_deadline.errors.throttling_exception.ThrottlingException: Your request exceeded a request rate quota.
            capo_deadline.errors.validation_exception.ValidationException: The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update monitor settings

            >>> await client.update_monitor_settings(monitor_id='monitor-1234567890abcdef1234567890abcdef', settings={'idcApplicationArn': 'arn:aws:sso::123456789012:application/ins-1234567890abcdef/apl-1234567890abcdef'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_deadline.types.update_monitor_settings_request.UpdateMonitorSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_deadline.types.update_monitor_settings_response.UpdateMonitorSettingsResponse"
        ]:
            import capo_deadline._operations.deadline.update_monitor_settings

            (
                output,
                http_response,
            ) = await capo_deadline._operations.deadline.update_monitor_settings.async_update_monitor_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateMonitorSettings")
        )
        input_: capo_deadline.types.update_monitor_settings_request.UpdateMonitorSettingsRequest = {
            "monitor_id": monitor_id,
            "settings": settings,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
