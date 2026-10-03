"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ThinClient``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_workspaces_thin_client._auth._signers
import capo_workspaces_thin_client._auth._sigv4
from capo_workspaces_thin_client._auth._identity import Credentials
from capo_workspaces_thin_client._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_workspaces_thin_client._auth._zapros_handler import AuthMiddleware
from capo_workspaces_thin_client._pagination import resolve_path as _resolve_path
from capo_workspaces_thin_client._services._aws_config import aws_config
from capo_workspaces_thin_client._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.arn
    import capo_workspaces_thin_client.types.client_token
    import capo_workspaces_thin_client.types.create_environment_request
    import capo_workspaces_thin_client.types.create_environment_response
    import capo_workspaces_thin_client.types.delete_device_request
    import capo_workspaces_thin_client.types.delete_device_response
    import capo_workspaces_thin_client.types.delete_environment_request
    import capo_workspaces_thin_client.types.delete_environment_response
    import capo_workspaces_thin_client.types.deregister_device_request
    import capo_workspaces_thin_client.types.deregister_device_response
    import capo_workspaces_thin_client.types.desktop_endpoint
    import capo_workspaces_thin_client.types.device_creation_tags_map
    import capo_workspaces_thin_client.types.device_id
    import capo_workspaces_thin_client.types.device_name
    import capo_workspaces_thin_client.types.device_summary
    import capo_workspaces_thin_client.types.environment_id
    import capo_workspaces_thin_client.types.environment_name
    import capo_workspaces_thin_client.types.environment_summary
    import capo_workspaces_thin_client.types.get_device_request
    import capo_workspaces_thin_client.types.get_device_response
    import capo_workspaces_thin_client.types.get_environment_request
    import capo_workspaces_thin_client.types.get_environment_response
    import capo_workspaces_thin_client.types.get_software_set_request
    import capo_workspaces_thin_client.types.get_software_set_response
    import capo_workspaces_thin_client.types.kms_key_arn
    import capo_workspaces_thin_client.types.list_devices_request
    import capo_workspaces_thin_client.types.list_devices_response
    import capo_workspaces_thin_client.types.list_environments_request
    import capo_workspaces_thin_client.types.list_environments_response
    import capo_workspaces_thin_client.types.list_software_sets_request
    import capo_workspaces_thin_client.types.list_software_sets_response
    import capo_workspaces_thin_client.types.list_tags_for_resource_request
    import capo_workspaces_thin_client.types.list_tags_for_resource_response
    import capo_workspaces_thin_client.types.maintenance_window
    import capo_workspaces_thin_client.types.max_results
    import capo_workspaces_thin_client.types.pagination_token
    import capo_workspaces_thin_client.types.software_set_id
    import capo_workspaces_thin_client.types.software_set_id_or_empty_string
    import capo_workspaces_thin_client.types.software_set_summary
    import capo_workspaces_thin_client.types.software_set_update_mode
    import capo_workspaces_thin_client.types.software_set_update_schedule
    import capo_workspaces_thin_client.types.software_set_validation_status
    import capo_workspaces_thin_client.types.tag_keys
    import capo_workspaces_thin_client.types.tag_resource_request
    import capo_workspaces_thin_client.types.tag_resource_response
    import capo_workspaces_thin_client.types.tags_map
    import capo_workspaces_thin_client.types.target_device_status
    import capo_workspaces_thin_client.types.untag_resource_request
    import capo_workspaces_thin_client.types.untag_resource_response
    import capo_workspaces_thin_client.types.update_device_request
    import capo_workspaces_thin_client.types.update_device_response
    import capo_workspaces_thin_client.types.update_environment_request
    import capo_workspaces_thin_client.types.update_environment_response
    import capo_workspaces_thin_client.types.update_software_set_request
    import capo_workspaces_thin_client.types.update_software_set_response


class WorkSpacesThinClientClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class WorkSpacesThinClientClient:
    """A client for the ``WorkSpacesThinClient`` service.

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
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = WorkSpacesThinClientClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[WorkSpacesThinClientClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: WorkSpacesThinClientClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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
        )
        return interceptors_, options_

    def create_environment(
        self,
        desktop_arn: "capo_workspaces_thin_client.types.arn.Arn",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        name: Optional[
            "capo_workspaces_thin_client.types.environment_name.EnvironmentName"
        ] = None,
        desktop_endpoint: Optional[
            "capo_workspaces_thin_client.types.desktop_endpoint.DesktopEndpoint"
        ] = None,
        software_set_update_schedule: Optional[
            "capo_workspaces_thin_client.types.software_set_update_schedule.SoftwareSetUpdateSchedule"
        ] = None,
        maintenance_window: Optional[
            "capo_workspaces_thin_client.types.maintenance_window.MaintenanceWindow"
        ] = None,
        software_set_update_mode: Optional[
            "capo_workspaces_thin_client.types.software_set_update_mode.SoftwareSetUpdateMode"
        ] = None,
        desired_software_set_id: Optional[
            "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
        ] = None,
        kms_key_arn: Optional[
            "capo_workspaces_thin_client.types.kms_key_arn.KmsKeyArn"
        ] = None,
        client_token: Optional[
            "capo_workspaces_thin_client.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_workspaces_thin_client.types.tags_map.TagsMap"] = None,
        device_creation_tags: Optional[
            "capo_workspaces_thin_client.types.device_creation_tags_map.DeviceCreationTagsMap"
        ] = None,
    ) -> "capo_workspaces_thin_client.types.create_environment_response.CreateEnvironmentResponse":
        """<p>Creates an environment for your thin client devices.</p>

        Args:
            name: <p>The name for the environment.</p>
            desktop_arn: <p>The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Secure Browser, or AppStream 2.0.</p>
            desktop_endpoint: <p>The URL for the identity provider login (only for environments that use AppStream 2.0).</p>
            software_set_update_schedule: <p>An option to define if software updates should be applied within a maintenance window.</p>
            maintenance_window: <p>A specification for a time window to apply software updates.</p>
            software_set_update_mode: <p>An option to define which software updates to apply.</p>
            desired_software_set_id: <p>The ID of the software set to apply.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Key Management Service key to use to encrypt the environment.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
            device_creation_tags: <p>A map of the key-value pairs of the tag or tags to assign to the newly created devices for this environment.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.create_environment_request.CreateEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.create_environment_response.CreateEnvironmentResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.create_environment

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.create_environment.create_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.create_environment_request.CreateEnvironmentRequest = {
            "desktop_arn": desktop_arn
        }
        if name is not None:
            input_["name"] = name
        if desktop_endpoint is not None:
            input_["desktop_endpoint"] = desktop_endpoint
        if software_set_update_schedule is not None:
            input_["software_set_update_schedule"] = software_set_update_schedule
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window
        if software_set_update_mode is not None:
            input_["software_set_update_mode"] = software_set_update_mode
        if desired_software_set_id is not None:
            input_["desired_software_set_id"] = desired_software_set_id
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if device_creation_tags is not None:
            input_["device_creation_tags"] = device_creation_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_device(
        self,
        id: "capo_workspaces_thin_client.types.device_id.DeviceId",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        client_token: Optional[
            "capo_workspaces_thin_client.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_workspaces_thin_client.types.delete_device_response.DeleteDeviceResponse"
    ):
        """<p>Deletes a thin client device.</p>

        Args:
            id: <p>The ID of the device to delete.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.delete_device_request.DeleteDeviceRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.delete_device_response.DeleteDeviceResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.delete_device

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.delete_device.delete_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.delete_device_request.DeleteDeviceRequest = {
            "id": id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_environment(
        self,
        id: "capo_workspaces_thin_client.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        client_token: Optional[
            "capo_workspaces_thin_client.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_thin_client.types.delete_environment_response.DeleteEnvironmentResponse":
        """<p>Deletes an environment.</p>

        Args:
            id: <p>The ID of the environment to delete.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.delete_environment_response.DeleteEnvironmentResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.delete_environment

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.delete_environment_request.DeleteEnvironmentRequest = {
            "id": id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_device(
        self,
        id: "capo_workspaces_thin_client.types.device_id.DeviceId",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        target_device_status: Optional[
            "capo_workspaces_thin_client.types.target_device_status.TargetDeviceStatus"
        ] = None,
        client_token: Optional[
            "capo_workspaces_thin_client.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_thin_client.types.deregister_device_response.DeregisterDeviceResponse":
        """<p>Deregisters a thin client device.</p>

        Args:
            id: <p>The ID of the device to deregister.</p>
            target_device_status: <p>The desired new status for the device.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.deregister_device_request.DeregisterDeviceRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.deregister_device_response.DeregisterDeviceResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.deregister_device

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.deregister_device.deregister_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.deregister_device_request.DeregisterDeviceRequest = {
            "id": id
        }
        if target_device_status is not None:
            input_["target_device_status"] = target_device_status
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_device(
        self,
        id: "capo_workspaces_thin_client.types.device_id.DeviceId",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
    ) -> "capo_workspaces_thin_client.types.get_device_response.GetDeviceResponse":
        """<p>Returns information for a thin client device.</p>

        Args:
            id: <p>The ID of the device for which to return information.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.get_device_request.GetDeviceRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.get_device_response.GetDeviceResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.get_device

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.get_device.get_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.get_device_request.GetDeviceRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_environment(
        self,
        id: "capo_workspaces_thin_client.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
    ) -> "capo_workspaces_thin_client.types.get_environment_response.GetEnvironmentResponse":
        """<p>Returns information for an environment.</p>

        Args:
            id: <p>The ID of the environment for which to return information.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.get_environment_request.GetEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.get_environment

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.get_environment_request.GetEnvironmentRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_software_set(
        self,
        id: "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
    ) -> "capo_workspaces_thin_client.types.get_software_set_response.GetSoftwareSetResponse":
        """<p>Returns information for a software set.</p>

        Args:
            id: <p>The ID of the software set for which to return information.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.get_software_set_request.GetSoftwareSetRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.get_software_set_response.GetSoftwareSetResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.get_software_set

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.get_software_set.get_software_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.get_software_set_request.GetSoftwareSetRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_devices(
        self,
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_thin_client.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_thin_client.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_thin_client.types.list_devices_response.ListDevicesResponse":
        """<p>Returns a list of thin client devices.</p>

        Args:
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.list_devices_request.ListDevicesRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.list_devices_response.ListDevicesResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.list_devices

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.list_devices.list_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.list_devices_request.ListDevicesRequest = {}
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

    def iter_list_devices(
        self,
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_thin_client.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_thin_client.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_thin_client.types.device_summary.DeviceSummary]":
        _token = next_token
        while True:
            _response = self.list_devices(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("devices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_environments(
        self,
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_thin_client.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_thin_client.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_thin_client.types.list_environments_response.ListEnvironmentsResponse":
        """<p>Returns a list of environments.</p>

        Args:
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.list_environments

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.list_environments_request.ListEnvironmentsRequest = {}
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

    def iter_list_environments(
        self,
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_thin_client.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_thin_client.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_thin_client.types.environment_summary.EnvironmentSummary]":
        _token = next_token
        while True:
            _response = self.list_environments(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("environments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_software_sets(
        self,
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_thin_client.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_thin_client.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_thin_client.types.list_software_sets_response.ListSoftwareSetsResponse":
        """<p>Returns a list of software sets.</p>

        Args:
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.list_software_sets_request.ListSoftwareSetsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.list_software_sets_response.ListSoftwareSetsResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.list_software_sets

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.list_software_sets.list_software_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.list_software_sets_request.ListSoftwareSetsRequest = {}
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

    def iter_list_software_sets(
        self,
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_thin_client.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_thin_client.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_thin_client.types.software_set_summary.SoftwareSetSummary]":
        _token = next_token
        while True:
            _response = self.list_software_sets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("software_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
    ) -> "capo_workspaces_thin_client.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to retrieve tags.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.list_tags_for_resource

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: str,
        tags: "capo_workspaces_thin_client.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
    ) -> "capo_workspaces_thin_client.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.tag_resource

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: str,
        tag_keys: "capo_workspaces_thin_client.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
    ) -> "capo_workspaces_thin_client.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The keys of the key-value pairs for the tag or tags you want to remove from the specified resource.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.untag_resource

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_device(
        self,
        id: "capo_workspaces_thin_client.types.device_id.DeviceId",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        name: Optional[
            "capo_workspaces_thin_client.types.device_name.DeviceName"
        ] = None,
        desired_software_set_id: Optional[
            "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
        ] = None,
        software_set_update_schedule: Optional[
            "capo_workspaces_thin_client.types.software_set_update_schedule.SoftwareSetUpdateSchedule"
        ] = None,
    ) -> (
        "capo_workspaces_thin_client.types.update_device_response.UpdateDeviceResponse"
    ):
        """<p>Updates a thin client device.</p>

        Args:
            id: <p>The ID of the device to update.</p>
            name: <p>The name of the device to update.</p>
            desired_software_set_id: <p>The ID of the software set to apply.</p>
            software_set_update_schedule: <p>An option to define if software updates should be applied within a maintenance window.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.update_device_request.UpdateDeviceRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.update_device_response.UpdateDeviceResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.update_device

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.update_device.update_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.update_device_request.UpdateDeviceRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if desired_software_set_id is not None:
            input_["desired_software_set_id"] = desired_software_set_id
        if software_set_update_schedule is not None:
            input_["software_set_update_schedule"] = software_set_update_schedule

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_environment(
        self,
        id: "capo_workspaces_thin_client.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
        name: Optional[
            "capo_workspaces_thin_client.types.environment_name.EnvironmentName"
        ] = None,
        desktop_arn: Optional["capo_workspaces_thin_client.types.arn.Arn"] = None,
        desktop_endpoint: Optional[
            "capo_workspaces_thin_client.types.desktop_endpoint.DesktopEndpoint"
        ] = None,
        software_set_update_schedule: Optional[
            "capo_workspaces_thin_client.types.software_set_update_schedule.SoftwareSetUpdateSchedule"
        ] = None,
        maintenance_window: Optional[
            "capo_workspaces_thin_client.types.maintenance_window.MaintenanceWindow"
        ] = None,
        software_set_update_mode: Optional[
            "capo_workspaces_thin_client.types.software_set_update_mode.SoftwareSetUpdateMode"
        ] = None,
        desired_software_set_id: Optional[
            "capo_workspaces_thin_client.types.software_set_id_or_empty_string.SoftwareSetIdOrEmptyString"
        ] = None,
        device_creation_tags: Optional[
            "capo_workspaces_thin_client.types.device_creation_tags_map.DeviceCreationTagsMap"
        ] = None,
    ) -> "capo_workspaces_thin_client.types.update_environment_response.UpdateEnvironmentResponse":
        """<p>Updates an environment.</p>

        Args:
            id: <p>The ID of the environment to update.</p>
            name: <p>The name of the environment to update.</p>
            desktop_arn: <p>The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Secure Browser, or AppStream 2.0.</p>
            desktop_endpoint: <p>The URL for the identity provider login (only for environments that use AppStream 2.0).</p>
            software_set_update_schedule: <p>An option to define if software updates should be applied within a maintenance window.</p>
            maintenance_window: <p>A specification for a time window to apply software updates.</p>
            software_set_update_mode: <p>An option to define which software updates to apply.</p>
            desired_software_set_id: <p>The ID of the software set to apply.</p>
            device_creation_tags: <p>A map of the key-value pairs of the tag or tags to assign to the newly created devices for this environment.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.update_environment_request.UpdateEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.update_environment_response.UpdateEnvironmentResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.update_environment

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.update_environment.update_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.update_environment_request.UpdateEnvironmentRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if desktop_arn is not None:
            input_["desktop_arn"] = desktop_arn
        if desktop_endpoint is not None:
            input_["desktop_endpoint"] = desktop_endpoint
        if software_set_update_schedule is not None:
            input_["software_set_update_schedule"] = software_set_update_schedule
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window
        if software_set_update_mode is not None:
            input_["software_set_update_mode"] = software_set_update_mode
        if desired_software_set_id is not None:
            input_["desired_software_set_id"] = desired_software_set_id
        if device_creation_tags is not None:
            input_["device_creation_tags"] = device_creation_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_software_set(
        self,
        id: "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId",
        validation_status: "capo_workspaces_thin_client.types.software_set_validation_status.SoftwareSetValidationStatus",
        *,
        config_overrides: Optional[WorkSpacesThinClientClientConfig] = None,
    ) -> "capo_workspaces_thin_client.types.update_software_set_response.UpdateSoftwareSetResponse":
        """<p>Updates a software set.</p>

        Args:
            id: <p>The ID of the software set to update.</p>
            validation_status: <p>An option to define if the software set has been validated.</p>

        Raises:
            capo_workspaces_thin_client.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_workspaces_thin_client.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_workspaces_thin_client.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found.</p>
            capo_workspaces_thin_client.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_workspaces_thin_client.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            capo_workspaces_thin_client.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_thin_client.types.update_software_set_request.UpdateSoftwareSetRequest]",
        ) -> OperationResponse[
            "capo_workspaces_thin_client.types.update_software_set_response.UpdateSoftwareSetResponse"
        ]:
            import capo_workspaces_thin_client._operations.thin_client.update_software_set

            output, http_response = (
                capo_workspaces_thin_client._operations.thin_client.update_software_set.update_software_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_thin_client.types.update_software_set_request.UpdateSoftwareSetRequest = {
            "id": id,
            "validation_status": validation_status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
