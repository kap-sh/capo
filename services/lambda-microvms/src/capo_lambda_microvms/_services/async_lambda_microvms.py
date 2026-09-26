"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#LambdaMicrovms``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_lambda_microvms._auth._signers
import capo_lambda_microvms._auth._sigv4
from capo_lambda_microvms._auth._identity import Credentials
from capo_lambda_microvms._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lambda_microvms._auth._zapros_handler import AuthMiddleware
from capo_lambda_microvms._pagination import resolve_path as _resolve_path
from capo_lambda_microvms._resources.lambda_microvms.microvm import AsyncMicrovm
from capo_lambda_microvms._resources.lambda_microvms.microvm_image import (
    AsyncMicrovmImage,
)
from capo_lambda_microvms._services._aws_config import aaws_config
from capo_lambda_microvms._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_lambda_microvms.types.architecture
    import capo_lambda_microvms.types.capability_list
    import capo_lambda_microvms.types.chipset
    import capo_lambda_microvms.types.code_artifact
    import capo_lambda_microvms.types.cpu_configuration_list
    import capo_lambda_microvms.types.create_microvm_auth_token_request
    import capo_lambda_microvms.types.create_microvm_auth_token_response
    import capo_lambda_microvms.types.create_microvm_image_request
    import capo_lambda_microvms.types.create_microvm_image_response
    import capo_lambda_microvms.types.create_microvm_shell_auth_token_request
    import capo_lambda_microvms.types.create_microvm_shell_auth_token_response
    import capo_lambda_microvms.types.delete_microvm_image_input
    import capo_lambda_microvms.types.delete_microvm_image_output
    import capo_lambda_microvms.types.delete_microvm_image_version_input
    import capo_lambda_microvms.types.delete_microvm_image_version_output
    import capo_lambda_microvms.types.environment_variable_map
    import capo_lambda_microvms.types.get_microvm_image_build_input
    import capo_lambda_microvms.types.get_microvm_image_build_output
    import capo_lambda_microvms.types.get_microvm_image_input
    import capo_lambda_microvms.types.get_microvm_image_output
    import capo_lambda_microvms.types.get_microvm_image_version_input
    import capo_lambda_microvms.types.get_microvm_image_version_output
    import capo_lambda_microvms.types.get_microvm_request
    import capo_lambda_microvms.types.get_microvm_response
    import capo_lambda_microvms.types.hooks
    import capo_lambda_microvms.types.idle_policy
    import capo_lambda_microvms.types.image_name
    import capo_lambda_microvms.types.list_managed_microvm_image_versions_input
    import capo_lambda_microvms.types.list_managed_microvm_image_versions_output
    import capo_lambda_microvms.types.list_managed_microvm_images_input
    import capo_lambda_microvms.types.list_managed_microvm_images_output
    import capo_lambda_microvms.types.list_microvm_image_builds_input
    import capo_lambda_microvms.types.list_microvm_image_builds_output
    import capo_lambda_microvms.types.list_microvm_image_versions_input
    import capo_lambda_microvms.types.list_microvm_image_versions_output
    import capo_lambda_microvms.types.list_microvm_images_request
    import capo_lambda_microvms.types.list_microvm_images_response
    import capo_lambda_microvms.types.list_microvms_request
    import capo_lambda_microvms.types.list_microvms_response
    import capo_lambda_microvms.types.list_of_port_specification
    import capo_lambda_microvms.types.list_tags_request
    import capo_lambda_microvms.types.list_tags_response
    import capo_lambda_microvms.types.logging
    import capo_lambda_microvms.types.managed_microvm_image_summary
    import capo_lambda_microvms.types.managed_microvm_image_version
    import capo_lambda_microvms.types.microvm_identifier
    import capo_lambda_microvms.types.microvm_image_build_summary
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.microvm_image_summary
    import capo_lambda_microvms.types.microvm_image_version_status
    import capo_lambda_microvms.types.microvm_image_version_summary
    import capo_lambda_microvms.types.microvm_item
    import capo_lambda_microvms.types.network_connector_list
    import capo_lambda_microvms.types.non_blank_string
    import capo_lambda_microvms.types.positive_integer
    import capo_lambda_microvms.types.resources_list
    import capo_lambda_microvms.types.resume_microvm_request
    import capo_lambda_microvms.types.resume_microvm_response
    import capo_lambda_microvms.types.role_arn
    import capo_lambda_microvms.types.run_hook_payload
    import capo_lambda_microvms.types.run_microvm_request
    import capo_lambda_microvms.types.run_microvm_response
    import capo_lambda_microvms.types.string
    import capo_lambda_microvms.types.suspend_microvm_request
    import capo_lambda_microvms.types.suspend_microvm_response
    import capo_lambda_microvms.types.tag_key_list
    import capo_lambda_microvms.types.tag_resource_request
    import capo_lambda_microvms.types.taggable_resource
    import capo_lambda_microvms.types.tags
    import capo_lambda_microvms.types.terminate_microvm_request
    import capo_lambda_microvms.types.terminate_microvm_response
    import capo_lambda_microvms.types.untag_resource_request
    import capo_lambda_microvms.types.update_microvm_image_request
    import capo_lambda_microvms.types.update_microvm_image_response
    import capo_lambda_microvms.types.update_microvm_image_version_request
    import capo_lambda_microvms.types.update_microvm_image_version_response
    import capo_lambda_microvms.types.version


class AsyncLambdaMicrovmsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncLambdaMicrovmsClient:
    """A client for the ``LambdaMicrovms`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = AsyncLambdaMicrovmsClientConfig(
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

        # resources
        self.microvm = AsyncMicrovm(self)
        self.microvm_image = AsyncMicrovmImage(self)

    def operation_options(
        self, config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncLambdaMicrovmsClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def create_microvm_image(
        self,
        base_image_arn: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        build_role_arn: "capo_lambda_microvms.types.role_arn.RoleArn",
        code_artifact: "capo_lambda_microvms.types.code_artifact.CodeArtifact",
        name: "capo_lambda_microvms.types.image_name.ImageName",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        base_image_version: Optional[
            "capo_lambda_microvms.types.version.Version"
        ] = None,
        description: Optional[str] = None,
        logging: Optional["capo_lambda_microvms.types.logging.Logging"] = None,
        egress_network_connectors: Optional[
            "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
        ] = None,
        cpu_configurations: Optional[
            "capo_lambda_microvms.types.cpu_configuration_list.CpuConfigurationList"
        ] = None,
        resources: Optional[
            "capo_lambda_microvms.types.resources_list.ResourcesList"
        ] = None,
        additional_os_capabilities: Optional[
            "capo_lambda_microvms.types.capability_list.CapabilityList"
        ] = None,
        hooks: Optional["capo_lambda_microvms.types.hooks.Hooks"] = None,
        environment_variables: Optional[
            "capo_lambda_microvms.types.environment_variable_map.EnvironmentVariableMap"
        ] = None,
        tags: Optional["capo_lambda_microvms.types.tags.Tags"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_lambda_microvms.types.create_microvm_image_response.CreateMicrovmImageResponse":
        r"""<p>Creates a MicroVM image from the specified code artifact and base image. The build is asynchronous — the image transitions from CREATING to CREATED on success, or CREATE_FAILED on failure. Use GetMicrovmImage to poll for completion.</p>

        Args:
            base_image_arn: <p>The ARN of the Lambda-managed base MicroVM image to build upon. Use ListManagedMicrovmImages to discover available base images.</p>
            base_image_version: <p>The specific version of the base MicroVM image to use.</p>
            build_role_arn: <p>The ARN of the IAM role assumed during the image build process. This role must have permissions to access the code artifact and any required resources.</p>
            description: <p>A description of the MicroVM image.</p>
            code_artifact: <p>The code artifact containing the application code and metadata for the MicroVM image.</p>
            logging: <p>The logging configuration for build-time and runtime logs. Specify {\"cloudWatch\": {\"logGroup\": \"...\"}} to stream logs to a custom CloudWatch log group, or {\"disabled\": {}} to turn off logging.</p>
            egress_network_connectors: <p>The list of egress network connectors available to the MicroVM at runtime.</p>
            cpu_configurations: <p>The list of supported CPU configurations for the MicroVM.</p>
            resources: <p>The resource requirements for the MicroVM.</p>
            additional_os_capabilities: <p>Additional OS capabilities granted to the MicroVM runtime environment.</p>
            environment_variables: <p>Environment variables set in the MicroVM runtime environment.</p>
            name: <p>The name of the MicroVM image. Must be unique within the AWS account.</p>
            tags: <p>A set of key-value pairs that you can attach to the resource. Use tags to categorize resources for cost allocation, access control (ABAC), and organization.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the operation returns the successful response without performing any further actions.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded a service quota for Lambda MicroVMs.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.create_microvm_image_request.CreateMicrovmImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.create_microvm_image_response.CreateMicrovmImageResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.create_microvm_image

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.create_microvm_image.async_create_microvm_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.create_microvm_image_request.CreateMicrovmImageRequest = {
            "base_image_arn": base_image_arn,
            "build_role_arn": build_role_arn,
            "code_artifact": code_artifact,
            "name": name,
        }
        if base_image_version is not None:
            input_["base_image_version"] = base_image_version
        if description is not None:
            input_["description"] = description
        if logging is not None:
            input_["logging"] = logging
        if egress_network_connectors is not None:
            input_["egress_network_connectors"] = egress_network_connectors
        if cpu_configurations is not None:
            input_["cpu_configurations"] = cpu_configurations
        if resources is not None:
            input_["resources"] = resources
        if additional_os_capabilities is not None:
            input_["additional_os_capabilities"] = additional_os_capabilities
        if hooks is not None:
            input_["hooks"] = hooks
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_managed_microvm_images(
        self,
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
    ) -> "capo_lambda_microvms.types.list_managed_microvm_images_output.ListManagedMicrovmImagesOutput":
        """<p>Lists AWS managed MicroVM images available for use as base images. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_managed_microvm_images_input.ListManagedMicrovmImagesInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_managed_microvm_images_output.ListManagedMicrovmImagesOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_managed_microvm_images

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_managed_microvm_images.async_list_managed_microvm_images(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_managed_microvm_images_input.ListManagedMicrovmImagesInput = {}
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

    async def iter_list_managed_microvm_images(
        self,
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
    ) -> "AsyncIterator[capo_lambda_microvms.types.managed_microvm_image_summary.ManagedMicrovmImageSummary]":
        _token = next_token
        while True:
            _response = await self.list_managed_microvm_images(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags(
        self,
        resource: "capo_lambda_microvms.types.taggable_resource.TaggableResource",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.list_tags_response.ListTagsResponse":
        """<p>Lists the tags associated with a Lambda MicroVM resource.</p>

        Args:
            resource: <p>The ARN of the resource to list tags for.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.service_exception.ServiceException: <p>The AWS Lambda MicroVMs service encountered an internal error.</p>
            capo_lambda_microvms.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. Retry the request later.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_tags_request.ListTagsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_tags_response.ListTagsResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_tags

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_tags.async_list_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_tags_request.ListTagsRequest = {
            "resource": resource
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
        resource: "capo_lambda_microvms.types.taggable_resource.TaggableResource",
        tags: "capo_lambda_microvms.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> None:
        """<p>Adds tags to a Lambda MicroVM resource.</p>

        Args:
            resource: <p>The ARN of the resource to tag.</p>
            tags: <p>The key-value pairs of tags to add to the resource.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda_microvms.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.service_exception.ServiceException: <p>The AWS Lambda MicroVMs service encountered an internal error.</p>
            capo_lambda_microvms.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. Retry the request later.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda_microvms._operations.lambda_microvms.tag_resource

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.tag_resource_request.TagResourceRequest = {
            "resource": resource,
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
        resource: "capo_lambda_microvms.types.taggable_resource.TaggableResource",
        tag_keys: "capo_lambda_microvms.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> None:
        """<p>Removes tags from a Lambda MicroVM resource.</p>

        Args:
            resource: <p>The ARN of the resource to remove tags from.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda_microvms.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.service_exception.ServiceException: <p>The AWS Lambda MicroVMs service encountered an internal error.</p>
            capo_lambda_microvms.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. Retry the request later.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda_microvms._operations.lambda_microvms.untag_resource

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.untag_resource_request.UntagResourceRequest = {
            "resource": resource,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def run_microvm(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        ingress_network_connectors: Optional[
            "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
        ] = None,
        egress_network_connectors: Optional[
            "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
        ] = None,
        image_version: Optional["capo_lambda_microvms.types.version.Version"] = None,
        execution_role_arn: Optional[
            "capo_lambda_microvms.types.role_arn.RoleArn"
        ] = None,
        idle_policy: Optional[
            "capo_lambda_microvms.types.idle_policy.IdlePolicy"
        ] = None,
        logging: Optional["capo_lambda_microvms.types.logging.Logging"] = None,
        run_hook_payload: Optional[
            "capo_lambda_microvms.types.run_hook_payload.RunHookPayload"
        ] = None,
        maximum_duration_in_seconds: Optional[int] = None,
        client_token: Optional[str] = None,
    ) -> "capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse":
        r"""<p>Runs a new MicroVM from the specified image. The MicroVM starts in PENDING state and transitions to RUNNING once provisioning completes. To connect, generate an authentication token using CreateMicrovmAuthToken.</p>

        Args:
            ingress_network_connectors: <p>The list of ingress network connectors to configure for the MicroVM.</p>
            egress_network_connectors: <p>The list of egress network connectors to configure for the MicroVM.</p>
            image_identifier: <p>The identifier (ARN or ID) of the MicroVM image to run.</p>
            image_version: <p>The version of the MicroVM image to run.</p>
            execution_role_arn: <p>The ARN of the IAM role to be assumed by the MicroVM during execution.</p>
            idle_policy: <p>Configuration to control auto-suspend and auto-resume behavior.</p>
            logging: <p>The logging configuration for this MicroVM instance. Specify {\"cloudWatch\": {\"logGroup\": \"...\"}} to stream application logs to a custom CloudWatch log group, or {\"disabled\": {}} to turn off logging.</p>
            run_hook_payload: <p>Per-MicroVM initialization data delivered as the request body of the /run lifecycle hook. Use to pass tenant-specific configuration such as session IDs or secret references. Maximum: 16,384 bytes.</p>
            maximum_duration_in_seconds: <p>The maximum duration in seconds that the MicroVM can exist before being terminated by the platform. Valid range: 1–28,800 (8 hours).</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>There is insufficient capacity to fulfill the request. Retry the request later.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded a service quota for Lambda MicroVMs.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.run_microvm_request.RunMicrovmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.run_microvm_response.RunMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.run_microvm

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.run_microvm.async_run_microvm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.run_microvm_request.RunMicrovmRequest = {
            "image_identifier": image_identifier
        }
        if ingress_network_connectors is not None:
            input_["ingress_network_connectors"] = ingress_network_connectors
        if egress_network_connectors is not None:
            input_["egress_network_connectors"] = egress_network_connectors
        if image_version is not None:
            input_["image_version"] = image_version
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if idle_policy is not None:
            input_["idle_policy"] = idle_policy
        if logging is not None:
            input_["logging"] = logging
        if run_hook_payload is not None:
            input_["run_hook_payload"] = run_hook_payload
        if maximum_duration_in_seconds is not None:
            input_["maximum_duration_in_seconds"] = maximum_duration_in_seconds
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_microvm(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_response.GetMicrovmResponse":
        """<p>Retrieves the details of a specific MicroVM, including its state, endpoint, image information, and configuration. The state field is eventually consistent — determine readiness by connecting to the endpoint.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.get_microvm_request.GetMicrovmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.get_microvm_response.GetMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.get_microvm.async_get_microvm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_request.GetMicrovmRequest = {
            "microvm_identifier": microvm_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def terminate_microvm(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> (
        "capo_lambda_microvms.types.terminate_microvm_response.TerminateMicrovmResponse"
    ):
        """<p>Terminates a MicroVM. This operation is idempotent; terminating a MicroVM that has already been terminated succeeds without error.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to terminate.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.terminate_microvm_request.TerminateMicrovmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.terminate_microvm_response.TerminateMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.terminate_microvm

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.terminate_microvm.async_terminate_microvm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.terminate_microvm_request.TerminateMicrovmRequest = {
            "microvm_identifier": microvm_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_microvms(
        self,
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        image_identifier: Optional[
            "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
        ] = None,
        image_version: Optional[str] = None,
    ) -> "capo_lambda_microvms.types.list_microvms_response.ListMicrovmsResponse":
        """<p>Lists MicroVMs in the account with optional filtering by image and version. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>Optional filter to list only MicroVMs running the specified image.</p>
            image_version: <p>Optional filter to list only MicroVMs running the specified image version.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_microvms_request.ListMicrovmsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_microvms_response.ListMicrovmsResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvms

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_microvms.async_list_microvms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvms_request.ListMicrovmsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if image_identifier is not None:
            input_["image_identifier"] = image_identifier
        if image_version is not None:
            input_["image_version"] = image_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_microvms(
        self,
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        image_identifier: Optional[
            "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
        ] = None,
        image_version: Optional[str] = None,
    ) -> "AsyncIterator[capo_lambda_microvms.types.microvm_item.MicrovmItem]":
        _token = next_token
        while True:
            _response = await self.list_microvms(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                image_identifier=image_identifier,
                image_version=image_version,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_microvm_auth_token(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        expiration_in_minutes: "capo_lambda_microvms.types.positive_integer.PositiveInteger",
        allowed_ports: "capo_lambda_microvms.types.list_of_port_specification.ListOfPortSpecification",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.create_microvm_auth_token_response.CreateMicrovmAuthTokenResponse":
        """<p>Creates an authentication token for accessing a running MicroVM. The token grants access to the specified ports on the MicroVM endpoint.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to create an authentication token for.</p>
            expiration_in_minutes: <p>The duration in minutes before the authentication token expires. Maximum: 60 minutes.</p>
            allowed_ports: <p>The list of port specifications that the authentication token grants access to on the MicroVM.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.create_microvm_auth_token_request.CreateMicrovmAuthTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.create_microvm_auth_token_response.CreateMicrovmAuthTokenResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.create_microvm_auth_token

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.create_microvm_auth_token.async_create_microvm_auth_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.create_microvm_auth_token_request.CreateMicrovmAuthTokenRequest = {
            "microvm_identifier": microvm_identifier,
            "expiration_in_minutes": expiration_in_minutes,
            "allowed_ports": allowed_ports,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_microvm_shell_auth_token(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        expiration_in_minutes: "capo_lambda_microvms.types.positive_integer.PositiveInteger",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.create_microvm_shell_auth_token_response.CreateMicrovmShellAuthTokenResponse":
        """<p>Creates a shell authentication token for interactive shell access to a running MicroVM. The MicroVM must have been run with the SHELL_INGRESS network connector attached.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to create a shell authentication token for.</p>
            expiration_in_minutes: <p>The duration in minutes before the shell authentication token expires.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.create_microvm_shell_auth_token_request.CreateMicrovmShellAuthTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.create_microvm_shell_auth_token_response.CreateMicrovmShellAuthTokenResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.create_microvm_shell_auth_token

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.create_microvm_shell_auth_token.async_create_microvm_shell_auth_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.create_microvm_shell_auth_token_request.CreateMicrovmShellAuthTokenRequest = {
            "microvm_identifier": microvm_identifier,
            "expiration_in_minutes": expiration_in_minutes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resume_microvm(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse":
        """<p>Resumes a suspended MicroVM, restoring it to RUNNING state with all state intact. The MicroVM must be in SUSPENDED state.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to resume.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.resume_microvm_request.ResumeMicrovmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.resume_microvm_response.ResumeMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.resume_microvm

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.resume_microvm.async_resume_microvm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.resume_microvm_request.ResumeMicrovmRequest = {
            "microvm_identifier": microvm_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def suspend_microvm(
        self,
        microvm_identifier: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.suspend_microvm_response.SuspendMicrovmResponse":
        """<p>Suspends a running MicroVM, preserving its full memory and disk state. The MicroVM transitions through SUSPENDING to SUSPENDED. To restore, call ResumeMicrovm or send traffic to the endpoint if autoResumeEnabled is true.</p>

        Args:
            microvm_identifier: <p>The ID of the MicroVM to suspend.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.suspend_microvm_request.SuspendMicrovmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.suspend_microvm_response.SuspendMicrovmResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.suspend_microvm

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.suspend_microvm.async_suspend_microvm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.suspend_microvm_request.SuspendMicrovmRequest = {
            "microvm_identifier": microvm_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_microvm_image(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_image_output.GetMicrovmImageOutput":
        """<p>Retrieves the details of a MicroVM image, including its state, versions, and configuration.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.get_microvm_image_input.GetMicrovmImageInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.get_microvm_image_output.GetMicrovmImageOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm_image

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.get_microvm_image.async_get_microvm_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_image_input.GetMicrovmImageInput = {
            "image_identifier": image_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_microvm_image(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.delete_microvm_image_output.DeleteMicrovmImageOutput":
        """<p>Deletes a MicroVM image. This operation is idempotent; deleting an image that has already been deleted succeeds without error.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to delete.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.delete_microvm_image_input.DeleteMicrovmImageInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.delete_microvm_image_output.DeleteMicrovmImageOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image.async_delete_microvm_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.delete_microvm_image_input.DeleteMicrovmImageInput = {
            "image_identifier": image_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_microvm_images(
        self,
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        name_filter: Optional[
            "capo_lambda_microvms.types.non_blank_string.NonBlankString"
        ] = None,
    ) -> "capo_lambda_microvms.types.list_microvm_images_response.ListMicrovmImagesResponse":
        """<p>Lists MicroVM images in the account with optional name filtering. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            name_filter: <p>Filters images whose name contains the specified string.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_microvm_images_request.ListMicrovmImagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_microvm_images_response.ListMicrovmImagesResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvm_images

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_microvm_images.async_list_microvm_images(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvm_images_request.ListMicrovmImagesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name_filter is not None:
            input_["name_filter"] = name_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_microvm_images(
        self,
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        name_filter: Optional[
            "capo_lambda_microvms.types.non_blank_string.NonBlankString"
        ] = None,
    ) -> "AsyncIterator[capo_lambda_microvms.types.microvm_image_summary.MicrovmImageSummary]":
        _token = next_token
        while True:
            _response = await self.list_microvm_images(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                name_filter=name_filter,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def delete_microvm_image_version(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.delete_microvm_image_version_output.DeleteMicrovmImageVersionOutput":
        """<p>Deletes a specific version of a MicroVM image. This operation is idempotent; deleting a version that has already been deleted succeeds without error.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to delete.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.delete_microvm_image_version_input.DeleteMicrovmImageVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.delete_microvm_image_version_output.DeleteMicrovmImageVersionOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image_version

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.delete_microvm_image_version.async_delete_microvm_image_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.delete_microvm_image_version_input.DeleteMicrovmImageVersionInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_microvm_image_build(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        build_id: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_image_build_output.GetMicrovmImageBuildOutput":
        """<p>Retrieves the details of a specific MicroVM image build, including its state, target architecture, and snapshot information.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image.</p>
            build_id: <p>The unique identifier of the build to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.get_microvm_image_build_input.GetMicrovmImageBuildInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.get_microvm_image_build_output.GetMicrovmImageBuildOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_build

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_build.async_get_microvm_image_build(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_image_build_input.GetMicrovmImageBuildInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
            "build_id": build_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_microvm_image_version(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.get_microvm_image_version_output.GetMicrovmImageVersionOutput":
        """<p>Retrieves the details of a specific version of a MicroVM image, including its configuration, state, and build information.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to retrieve.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.get_microvm_image_version_input.GetMicrovmImageVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.get_microvm_image_version_output.GetMicrovmImageVersionOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_version

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.get_microvm_image_version.async_get_microvm_image_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.get_microvm_image_version_input.GetMicrovmImageVersionInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_managed_microvm_image_versions(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
    ) -> "capo_lambda_microvms.types.list_managed_microvm_image_versions_output.ListManagedMicrovmImageVersionsOutput":
        """<p>Lists versions of a managed MicroVM image. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the managed MicroVM image to list versions for.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_managed_microvm_image_versions_input.ListManagedMicrovmImageVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_managed_microvm_image_versions_output.ListManagedMicrovmImageVersionsOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_managed_microvm_image_versions

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_managed_microvm_image_versions.async_list_managed_microvm_image_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_managed_microvm_image_versions_input.ListManagedMicrovmImageVersionsInput = {
            "image_identifier": image_identifier
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

    async def iter_list_managed_microvm_image_versions(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
    ) -> "AsyncIterator[capo_lambda_microvms.types.managed_microvm_image_version.ManagedMicrovmImageVersion]":
        _token = next_token
        while True:
            _response = await self.list_managed_microvm_image_versions(
                image_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_microvm_image_builds(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        architecture: Optional[
            "capo_lambda_microvms.types.architecture.Architecture"
        ] = None,
        chipset: Optional["capo_lambda_microvms.types.chipset.Chipset"] = None,
        chipset_generation: Optional[
            "capo_lambda_microvms.types.non_blank_string.NonBlankString"
        ] = None,
    ) -> "capo_lambda_microvms.types.list_microvm_image_builds_output.ListMicrovmImageBuildsOutput":
        """<p>Lists builds for a MicroVM image version with optional filtering by architecture and chipset. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to list builds for.</p>
            architecture: <p>Filters builds by target CPU architecture.</p>
            chipset: <p>Filters builds by target chipset.</p>
            chipset_generation: <p>Filters builds by target chipset generation.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_microvm_image_builds_input.ListMicrovmImageBuildsInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_microvm_image_builds_output.ListMicrovmImageBuildsOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_builds

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_builds.async_list_microvm_image_builds(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvm_image_builds_input.ListMicrovmImageBuildsInput = {
            "image_identifier": image_identifier,
            "image_version": image_version,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if architecture is not None:
            input_["architecture"] = architecture
        if chipset is not None:
            input_["chipset"] = chipset
        if chipset_generation is not None:
            input_["chipset_generation"] = chipset_generation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_microvm_image_builds(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
        architecture: Optional[
            "capo_lambda_microvms.types.architecture.Architecture"
        ] = None,
        chipset: Optional["capo_lambda_microvms.types.chipset.Chipset"] = None,
        chipset_generation: Optional[
            "capo_lambda_microvms.types.non_blank_string.NonBlankString"
        ] = None,
    ) -> "AsyncIterator[capo_lambda_microvms.types.microvm_image_build_summary.MicrovmImageBuildSummary]":
        _token = next_token
        while True:
            _response = await self.list_microvm_image_builds(
                image_identifier,
                image_version,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                architecture=architecture,
                chipset=chipset,
                chipset_generation=chipset_generation,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_microvm_image_versions(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
    ) -> "capo_lambda_microvms.types.list_microvm_image_versions_output.ListMicrovmImageVersionsOutput":
        """<p>Lists versions of a MicroVM image. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to list versions for.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.list_microvm_image_versions_input.ListMicrovmImageVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.list_microvm_image_versions_output.ListMicrovmImageVersionsOutput"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_versions

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.list_microvm_image_versions.async_list_microvm_image_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.list_microvm_image_versions_input.ListMicrovmImageVersionsInput = {
            "image_identifier": image_identifier
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

    async def iter_list_microvm_image_versions(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_lambda_microvms.types.string.String"] = None,
    ) -> "AsyncIterator[capo_lambda_microvms.types.microvm_image_version_summary.MicrovmImageVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_microvm_image_versions(
                image_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_microvm_image(
        self,
        base_image_arn: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        build_role_arn: "capo_lambda_microvms.types.role_arn.RoleArn",
        code_artifact: "capo_lambda_microvms.types.code_artifact.CodeArtifact",
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
        base_image_version: Optional[
            "capo_lambda_microvms.types.version.Version"
        ] = None,
        description: Optional[str] = None,
        logging: Optional["capo_lambda_microvms.types.logging.Logging"] = None,
        egress_network_connectors: Optional[
            "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
        ] = None,
        cpu_configurations: Optional[
            "capo_lambda_microvms.types.cpu_configuration_list.CpuConfigurationList"
        ] = None,
        resources: Optional[
            "capo_lambda_microvms.types.resources_list.ResourcesList"
        ] = None,
        additional_os_capabilities: Optional[
            "capo_lambda_microvms.types.capability_list.CapabilityList"
        ] = None,
        hooks: Optional["capo_lambda_microvms.types.hooks.Hooks"] = None,
        environment_variables: Optional[
            "capo_lambda_microvms.types.environment_variable_map.EnvironmentVariableMap"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_lambda_microvms.types.update_microvm_image_response.UpdateMicrovmImageResponse":
        r"""<p>Updates the configuration of a MicroVM image and triggers a new version build. This operation uses PUT semantics — all required fields (codeArtifact, baseImageArn, buildRoleArn) must be provided with every request.</p>

        Args:
            base_image_arn: <p>The ARN of the base MicroVM image.</p>
            base_image_version: <p>The specific version of the base MicroVM image to use.</p>
            build_role_arn: <p>The ARN of the IAM build role.</p>
            description: <p>The description of the MicroVM image.</p>
            code_artifact: <p>The code artifact containing the application code and metadata for the MicroVM image.</p>
            logging: <p>The logging configuration for build-time and runtime logs. Specify {\"cloudWatch\": {\"logGroup\": \"...\"}} to stream logs to a custom CloudWatch log group, or {\"disabled\": {}} to turn off logging.</p>
            egress_network_connectors: <p>The list of egress network connectors available to the MicroVM at runtime.</p>
            cpu_configurations: <p>The list of supported CPU configurations for the MicroVM.</p>
            resources: <p>The resource requirements for the MicroVM.</p>
            additional_os_capabilities: <p>Additional OS capabilities granted to the MicroVM runtime environment.</p>
            environment_variables: <p>Environment variables set in the MicroVM runtime environment.</p>
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image to update.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded a service quota for Lambda MicroVMs.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.update_microvm_image_request.UpdateMicrovmImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.update_microvm_image_response.UpdateMicrovmImageResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.update_microvm_image

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.update_microvm_image.async_update_microvm_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.update_microvm_image_request.UpdateMicrovmImageRequest = {
            "base_image_arn": base_image_arn,
            "build_role_arn": build_role_arn,
            "code_artifact": code_artifact,
            "image_identifier": image_identifier,
        }
        if base_image_version is not None:
            input_["base_image_version"] = base_image_version
        if description is not None:
            input_["description"] = description
        if logging is not None:
            input_["logging"] = logging
        if egress_network_connectors is not None:
            input_["egress_network_connectors"] = egress_network_connectors
        if cpu_configurations is not None:
            input_["cpu_configurations"] = cpu_configurations
        if resources is not None:
            input_["resources"] = resources
        if additional_os_capabilities is not None:
            input_["additional_os_capabilities"] = additional_os_capabilities
        if hooks is not None:
            input_["hooks"] = hooks
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_microvm_image_version(
        self,
        image_identifier: "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier",
        image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString",
        status: "capo_lambda_microvms.types.microvm_image_version_status.MicrovmImageVersionStatus",
        *,
        config_overrides: Optional[AsyncLambdaMicrovmsClientConfig] = None,
    ) -> "capo_lambda_microvms.types.update_microvm_image_version_response.UpdateMicrovmImageVersionResponse":
        """<p>Updates the status of a specific MicroVM image version.</p>

        Args:
            image_identifier: <p>The unique identifier (ARN or ID) of the MicroVM image.</p>
            image_version: <p>The version of the MicroVM image to update.</p>
            status: <p>The new status to set for the MicroVM image version.</p>

        Raises:
            capo_lambda_microvms.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_lambda_microvms.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry the request later.</p>
            capo_lambda_microvms.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request later.</p>
            capo_lambda_microvms.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by the service.</p>
            capo_lambda_microvms.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_lambda_microvms.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_lambda_microvms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_microvms.types.update_microvm_image_version_request.UpdateMicrovmImageVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_microvms.types.update_microvm_image_version_response.UpdateMicrovmImageVersionResponse"
        ]:
            import capo_lambda_microvms._operations.lambda_microvms.update_microvm_image_version

            (
                output,
                http_response,
            ) = await capo_lambda_microvms._operations.lambda_microvms.update_microvm_image_version.async_update_microvm_image_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lambda_microvms.types.update_microvm_image_version_request.UpdateMicrovmImageVersionRequest = {
            "image_identifier": image_identifier,
            "image_version": image_version,
            "status": status,
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
