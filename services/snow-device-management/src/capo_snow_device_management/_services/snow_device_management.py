"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#SnowDeviceManagement``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_snow_device_management._auth._signers
import capo_snow_device_management._auth._sigv4
from capo_snow_device_management._auth._identity import Credentials
from capo_snow_device_management._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_snow_device_management._auth._zapros_handler import AuthMiddleware
from capo_snow_device_management._pagination import resolve_path as _resolve_path
from capo_snow_device_management._resources.snow_device_management.managed_device import (
    ManagedDevice,
)
from capo_snow_device_management._resources.snow_device_management.task import Task
from capo_snow_device_management._services._aws_config import aws_config
from capo_snow_device_management._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_snow_device_management.types.cancel_task_input
    import capo_snow_device_management.types.cancel_task_output
    import capo_snow_device_management.types.command
    import capo_snow_device_management.types.create_task_input
    import capo_snow_device_management.types.create_task_output
    import capo_snow_device_management.types.describe_device_ec2_input
    import capo_snow_device_management.types.describe_device_ec2_output
    import capo_snow_device_management.types.describe_device_input
    import capo_snow_device_management.types.describe_device_output
    import capo_snow_device_management.types.describe_execution_input
    import capo_snow_device_management.types.describe_execution_output
    import capo_snow_device_management.types.describe_task_input
    import capo_snow_device_management.types.describe_task_output
    import capo_snow_device_management.types.device_summary
    import capo_snow_device_management.types.execution_state
    import capo_snow_device_management.types.execution_summary
    import capo_snow_device_management.types.idempotency_token
    import capo_snow_device_management.types.instance_ids_list
    import capo_snow_device_management.types.job_id
    import capo_snow_device_management.types.list_device_resources_input
    import capo_snow_device_management.types.list_device_resources_output
    import capo_snow_device_management.types.list_devices_input
    import capo_snow_device_management.types.list_devices_output
    import capo_snow_device_management.types.list_executions_input
    import capo_snow_device_management.types.list_executions_output
    import capo_snow_device_management.types.list_tags_for_resource_input
    import capo_snow_device_management.types.list_tags_for_resource_output
    import capo_snow_device_management.types.list_tasks_input
    import capo_snow_device_management.types.list_tasks_output
    import capo_snow_device_management.types.managed_device_id
    import capo_snow_device_management.types.max_results
    import capo_snow_device_management.types.next_token
    import capo_snow_device_management.types.resource_summary
    import capo_snow_device_management.types.tag_keys
    import capo_snow_device_management.types.tag_map
    import capo_snow_device_management.types.tag_resource_input
    import capo_snow_device_management.types.target_list
    import capo_snow_device_management.types.task_description_string
    import capo_snow_device_management.types.task_id
    import capo_snow_device_management.types.task_state
    import capo_snow_device_management.types.task_summary
    import capo_snow_device_management.types.untag_resource_input


class SnowDeviceManagementClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class SnowDeviceManagementClient:
    """A client for the ``SnowDeviceManagement`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = SnowDeviceManagementClientConfig(
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
        self.managed_device = ManagedDevice(self)
        self.task = Task(self)

    def operation_options(
        self, config_overrides: Optional[SnowDeviceManagementClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SnowDeviceManagementClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "capo_snow_device_management.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns a list of tags for a managed device or task.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the device or task.</p>

        Raises:
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.list_tags_for_resource

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.list_tags_for_resource_input.ListTagsForResourceInput = {
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
        tags: "capo_snow_device_management.types.tag_map.TagMap",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> None:
        """<p>Adds or replaces tags on a device or task.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the device or task.</p>
            tags: <p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.</p>

        Raises:
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[None]:
            import capo_snow_device_management._operations.snow_device_management.tag_resource

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.tag_resource_input.TagResourceInput = {
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
        tag_keys: "capo_snow_device_management.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> None:
        """<p>Removes a tag from a device or task.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the device or task.</p>
            tag_keys: <p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.</p>

        Raises:
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[None]:
            import capo_snow_device_management._operations.snow_device_management.untag_resource

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.untag_resource_input.UntagResourceInput = {
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

    def describe_device(
        self,
        managed_device_id: "capo_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> (
        "capo_snow_device_management.types.describe_device_output.DescribeDeviceOutput"
    ):
        """<p>Checks device-specific information, such as the device type, software version, IP addresses, and lock status.</p>

        Args:
            managed_device_id: <p>The ID of the device that you are checking the information of.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.describe_device_input.DescribeDeviceInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.describe_device_output.DescribeDeviceOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.describe_device

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.describe_device.describe_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.describe_device_input.DescribeDeviceInput = {
            "managed_device_id": managed_device_id
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
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        job_id: Optional["capo_snow_device_management.types.job_id.JobId"] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "capo_snow_device_management.types.list_devices_output.ListDevicesOutput":
        """<p>Returns a list of all devices on your Amazon Web Services account that have Amazon Web Services Snow Device Management enabled in the Amazon Web Services Region where the command is run.</p>

        Args:
            job_id: <p>The ID of the job used to order the device.</p>
            max_results: <p>The maximum number of devices to list per page.</p>
            next_token: <p>A pagination token to continue to the next page of results.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.list_devices_input.ListDevicesInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.list_devices_output.ListDevicesOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.list_devices

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.list_devices.list_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.list_devices_input.ListDevicesInput = {}
        if job_id is not None:
            input_["job_id"] = job_id
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

    def iter_list_devices(
        self,
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        job_id: Optional["capo_snow_device_management.types.job_id.JobId"] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_snow_device_management.types.device_summary.DeviceSummary]":
        _token = next_token
        while True:
            _response = self.list_devices(
                config_overrides=config_overrides,
                job_id=job_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("devices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_device_ec2_instances(
        self,
        managed_device_id: "capo_snow_device_management.types.managed_device_id.ManagedDeviceId",
        instance_ids: "capo_snow_device_management.types.instance_ids_list.InstanceIdsList",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "capo_snow_device_management.types.describe_device_ec2_output.DescribeDeviceEc2Output":
        """<p>Checks the current state of the Amazon EC2 instances. The output is similar to <code>describeDevice</code>, but the results are sourced from the device cache in the Amazon Web Services Cloud and include a subset of the available fields. </p>

        Args:
            managed_device_id: <p>The ID of the managed device.</p>
            instance_ids: <p>A list of instance IDs associated with the managed device.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.describe_device_ec2_input.DescribeDeviceEc2Input]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.describe_device_ec2_output.DescribeDeviceEc2Output"
        ]:
            import capo_snow_device_management._operations.snow_device_management.describe_device_ec2_instances

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.describe_device_ec2_instances.describe_device_ec2_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.describe_device_ec2_input.DescribeDeviceEc2Input = {
            "managed_device_id": managed_device_id,
            "instance_ids": instance_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_device_resources(
        self,
        managed_device_id: "capo_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        type: Optional[str] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "capo_snow_device_management.types.list_device_resources_output.ListDeviceResourcesOutput":
        """<p>Returns a list of the Amazon Web Services resources available for a device. Currently, Amazon EC2 instances are the only supported resource type.</p>

        Args:
            managed_device_id: <p>The ID of the managed device that you are listing the resources of.</p>
            type: <p>A structure used to filter the results by type of resource.</p>
            max_results: <p>The maximum number of resources per page.</p>
            next_token: <p>A pagination token to continue to the next page of results.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.list_device_resources_input.ListDeviceResourcesInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.list_device_resources_output.ListDeviceResourcesOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.list_device_resources

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.list_device_resources.list_device_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.list_device_resources_input.ListDeviceResourcesInput = {
            "managed_device_id": managed_device_id
        }
        if type is not None:
            input_["type"] = type
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

    def iter_list_device_resources(
        self,
        managed_device_id: "capo_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        type: Optional[str] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_snow_device_management.types.resource_summary.ResourceSummary]":
        _token = next_token
        while True:
            _response = self.list_device_resources(
                managed_device_id,
                config_overrides=config_overrides,
                type=type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_task(
        self,
        targets: "capo_snow_device_management.types.target_list.TargetList",
        command: "capo_snow_device_management.types.command.Command",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        description: Optional[
            "capo_snow_device_management.types.task_description_string.TaskDescriptionString"
        ] = None,
        tags: Optional["capo_snow_device_management.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_snow_device_management.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_snow_device_management.types.create_task_output.CreateTaskOutput":
        """<p>Instructs one or more devices to start a task, such as unlocking or rebooting.</p>

        Args:
            targets: <p>A list of managed device IDs.</p>
            command: <p>The task to be performed. Only one task is executed on a device at a time.</p>
            description: <p>A description of the task and its targets.</p>
            tags: <p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment. </p>
            client_token: <p>A token ensuring that the action is called only once with the specified details.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.create_task_input.CreateTaskInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.create_task_output.CreateTaskOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.create_task

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.create_task.create_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.create_task_input.CreateTaskInput = {
            "targets": targets,
            "command": command,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
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

    def describe_task(
        self,
        task_id: "capo_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "capo_snow_device_management.types.describe_task_output.DescribeTaskOutput":
        """<p>Checks the metadata for a given task on a device. </p>

        Args:
            task_id: <p>The ID of the task to be described.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.describe_task_input.DescribeTaskInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.describe_task_output.DescribeTaskOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.describe_task

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.describe_task.describe_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.describe_task_input.DescribeTaskInput = {
            "task_id": task_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tasks(
        self,
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        state: Optional[
            "capo_snow_device_management.types.task_state.TaskState"
        ] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "capo_snow_device_management.types.list_tasks_output.ListTasksOutput":
        """<p>Returns a list of tasks that can be filtered by state.</p>

        Args:
            state: <p>A structure used to filter the list of tasks.</p>
            max_results: <p>The maximum number of tasks per page.</p>
            next_token: <p>A pagination token to continue to the next page of tasks.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.list_tasks_input.ListTasksInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.list_tasks_output.ListTasksOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.list_tasks

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.list_tasks.list_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.list_tasks_input.ListTasksInput = {}
        if state is not None:
            input_["state"] = state
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

    def iter_list_tasks(
        self,
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        state: Optional[
            "capo_snow_device_management.types.task_state.TaskState"
        ] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_snow_device_management.types.task_summary.TaskSummary]":
        _token = next_token
        while True:
            _response = self.list_tasks(
                config_overrides=config_overrides,
                state=state,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def cancel_task(
        self,
        task_id: "capo_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "capo_snow_device_management.types.cancel_task_output.CancelTaskOutput":
        """<p>Sends a cancel request for a specified task. You can cancel a task only if it's still in a <code>QUEUED</code> state. Tasks that are already running can't be cancelled.</p> <note> <p>A task might still run if it's processed from the queue before the <code>CancelTask</code> operation changes the task's state.</p> </note>

        Args:
            task_id: <p>The ID of the task that you are attempting to cancel. You can retrieve a task ID by using the <code>ListTasks</code> operation.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.cancel_task_input.CancelTaskInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.cancel_task_output.CancelTaskOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.cancel_task

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.cancel_task.cancel_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.cancel_task_input.CancelTaskInput = {
            "task_id": task_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_execution(
        self,
        task_id: "capo_snow_device_management.types.task_id.TaskId",
        managed_device_id: "capo_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "capo_snow_device_management.types.describe_execution_output.DescribeExecutionOutput":
        """<p>Checks the status of a remote task running on one or more target devices.</p>

        Args:
            task_id: <p>The ID of the task that the action is describing.</p>
            managed_device_id: <p>The ID of the managed device.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.describe_execution_input.DescribeExecutionInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.describe_execution_output.DescribeExecutionOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.describe_execution

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.describe_execution.describe_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.describe_execution_input.DescribeExecutionInput = {
            "task_id": task_id,
            "managed_device_id": managed_device_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_executions(
        self,
        task_id: "capo_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        state: Optional[
            "capo_snow_device_management.types.execution_state.ExecutionState"
        ] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> (
        "capo_snow_device_management.types.list_executions_output.ListExecutionsOutput"
    ):
        """<p>Returns the status of tasks for one or more target devices.</p>

        Args:
            task_id: <p>The ID of the task.</p>
            state: <p>A structure used to filter the tasks by their current state.</p>
            max_results: <p>The maximum number of tasks to list per page.</p>
            next_token: <p>A pagination token to continue to the next page of tasks.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.list_executions_input.ListExecutionsInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.list_executions_output.ListExecutionsOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.list_executions

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.list_executions.list_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snow_device_management.types.list_executions_input.ListExecutionsInput = {
            "task_id": task_id
        }
        if state is not None:
            input_["state"] = state
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

    def iter_list_executions(
        self,
        task_id: "capo_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        state: Optional[
            "capo_snow_device_management.types.execution_state.ExecutionState"
        ] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> (
        "Iterator[capo_snow_device_management.types.execution_summary.ExecutionSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_executions(
                task_id,
                config_overrides=config_overrides,
                state=state,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
