"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GreengrassV2``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_greengrassv2._auth._signers
import capo_greengrassv2._auth._sigv4
from capo_greengrassv2._auth._identity import Credentials
from capo_greengrassv2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_greengrassv2._auth._zapros_handler import AuthMiddleware
from capo_greengrassv2._pagination import resolve_path as _resolve_path
from capo_greengrassv2._services._aws_config import aaws_config
from capo_greengrassv2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_greengrassv2.types.associate_client_device_with_core_device_entry_list
    import capo_greengrassv2.types.associate_service_role_to_account_request
    import capo_greengrassv2.types.associate_service_role_to_account_response
    import capo_greengrassv2.types.associated_client_device
    import capo_greengrassv2.types.batch_associate_client_device_with_core_device_request
    import capo_greengrassv2.types.batch_associate_client_device_with_core_device_response
    import capo_greengrassv2.types.batch_disassociate_client_device_from_core_device_request
    import capo_greengrassv2.types.batch_disassociate_client_device_from_core_device_response
    import capo_greengrassv2.types.cancel_deployment_request
    import capo_greengrassv2.types.cancel_deployment_response
    import capo_greengrassv2.types.client_token_string
    import capo_greengrassv2.types.component
    import capo_greengrassv2.types.component_arn
    import capo_greengrassv2.types.component_candidate_list
    import capo_greengrassv2.types.component_deployment_specifications
    import capo_greengrassv2.types.component_platform
    import capo_greengrassv2.types.component_version_arn
    import capo_greengrassv2.types.component_version_list_item
    import capo_greengrassv2.types.component_visibility_scope
    import capo_greengrassv2.types.connectivity_info_list
    import capo_greengrassv2.types.core_device
    import capo_greengrassv2.types.core_device_runtime_string
    import capo_greengrassv2.types.core_device_status
    import capo_greengrassv2.types.core_device_thing_name
    import capo_greengrassv2.types.create_component_version_request
    import capo_greengrassv2.types.create_component_version_response
    import capo_greengrassv2.types.create_deployment_request
    import capo_greengrassv2.types.create_deployment_response
    import capo_greengrassv2.types.default_max_results
    import capo_greengrassv2.types.delete_component_request
    import capo_greengrassv2.types.delete_core_device_request
    import capo_greengrassv2.types.delete_deployment_request
    import capo_greengrassv2.types.deployment
    import capo_greengrassv2.types.deployment_history_filter
    import capo_greengrassv2.types.deployment_io_t_job_configuration
    import capo_greengrassv2.types.deployment_name_string
    import capo_greengrassv2.types.deployment_policies
    import capo_greengrassv2.types.describe_component_request
    import capo_greengrassv2.types.describe_component_response
    import capo_greengrassv2.types.disassociate_client_device_from_core_device_entry_list
    import capo_greengrassv2.types.disassociate_service_role_from_account_request
    import capo_greengrassv2.types.disassociate_service_role_from_account_response
    import capo_greengrassv2.types.effective_deployment
    import capo_greengrassv2.types.generic_v2_arn
    import capo_greengrassv2.types.get_component_request
    import capo_greengrassv2.types.get_component_response
    import capo_greengrassv2.types.get_component_version_artifact_request
    import capo_greengrassv2.types.get_component_version_artifact_response
    import capo_greengrassv2.types.get_connectivity_info_request
    import capo_greengrassv2.types.get_connectivity_info_response
    import capo_greengrassv2.types.get_core_device_request
    import capo_greengrassv2.types.get_core_device_response
    import capo_greengrassv2.types.get_deployment_request
    import capo_greengrassv2.types.get_deployment_response
    import capo_greengrassv2.types.get_service_role_for_account_request
    import capo_greengrassv2.types.get_service_role_for_account_response
    import capo_greengrassv2.types.installed_component
    import capo_greengrassv2.types.installed_component_topology_filter
    import capo_greengrassv2.types.io_t_thing_name
    import capo_greengrassv2.types.iot_endpoint_type
    import capo_greengrassv2.types.lambda_function_recipe_source
    import capo_greengrassv2.types.list_client_devices_associated_with_core_device_request
    import capo_greengrassv2.types.list_client_devices_associated_with_core_device_response
    import capo_greengrassv2.types.list_component_versions_request
    import capo_greengrassv2.types.list_component_versions_response
    import capo_greengrassv2.types.list_components_request
    import capo_greengrassv2.types.list_components_response
    import capo_greengrassv2.types.list_core_devices_request
    import capo_greengrassv2.types.list_core_devices_response
    import capo_greengrassv2.types.list_deployments_request
    import capo_greengrassv2.types.list_deployments_response
    import capo_greengrassv2.types.list_effective_deployments_request
    import capo_greengrassv2.types.list_effective_deployments_response
    import capo_greengrassv2.types.list_installed_components_request
    import capo_greengrassv2.types.list_installed_components_response
    import capo_greengrassv2.types.list_tags_for_resource_request
    import capo_greengrassv2.types.list_tags_for_resource_response
    import capo_greengrassv2.types.next_token_string
    import capo_greengrassv2.types.non_empty_string
    import capo_greengrassv2.types.recipe_blob
    import capo_greengrassv2.types.recipe_output_format
    import capo_greengrassv2.types.resolve_component_candidates_request
    import capo_greengrassv2.types.resolve_component_candidates_response
    import capo_greengrassv2.types.s3_endpoint_type
    import capo_greengrassv2.types.string
    import capo_greengrassv2.types.tag_key_list
    import capo_greengrassv2.types.tag_map
    import capo_greengrassv2.types.tag_resource_request
    import capo_greengrassv2.types.tag_resource_response
    import capo_greengrassv2.types.target_arn
    import capo_greengrassv2.types.thing_group_arn
    import capo_greengrassv2.types.untag_resource_request
    import capo_greengrassv2.types.untag_resource_response
    import capo_greengrassv2.types.update_connectivity_info_request
    import capo_greengrassv2.types.update_connectivity_info_response


class AsyncGreengrassV2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncGreengrassV2Client:
    """A client for the ``GreengrassV2`` service.

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
        self._config = AsyncGreengrassV2ClientConfig(
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
        self, config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncGreengrassV2ClientConfig = config_overrides or {}
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

    async def associate_service_role_to_account(
        self,
        role_arn: "capo_greengrassv2.types.string.String",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> "capo_greengrassv2.types.associate_service_role_to_account_response.AssociateServiceRoleToAccountResponse":
        """<p>Associates a Greengrass service role with IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region. IoT Greengrass uses this role to verify the identity of client devices and manage core device connectivity information. The role must include the <a href="https://console.aws.amazon.com/iam/home#/policies/arn:awsiam::aws:policy/service-role/AWSGreengrassResourceAccessRolePolicy">AWSGreengrassResourceAccessRolePolicy</a> managed policy or a custom policy that defines equivalent permissions for the IoT Greengrass features that you use. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html">Greengrass service role</a> in the <i>IoT Greengrass Version 2 Developer Guide</i>.</p>

        Args:
            role_arn: <p>The Amazon Resource Name (ARN) of the service role to associate with IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region.</p>

        Raises:
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.associate_service_role_to_account_request.AssociateServiceRoleToAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.associate_service_role_to_account_response.AssociateServiceRoleToAccountResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.associate_service_role_to_account

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.associate_service_role_to_account.async_associate_service_role_to_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.associate_service_role_to_account_request.AssociateServiceRoleToAccountRequest = {
            "role_arn": role_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_associate_client_device_with_core_device(
        self,
        core_device_thing_name: "capo_greengrassv2.types.io_t_thing_name.IoTThingName",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        entries: Optional[
            "capo_greengrassv2.types.associate_client_device_with_core_device_entry_list.AssociateClientDeviceWithCoreDeviceEntryList"
        ] = None,
    ) -> "capo_greengrassv2.types.batch_associate_client_device_with_core_device_response.BatchAssociateClientDeviceWithCoreDeviceResponse":
        """<p>Associates a list of client devices with a core device. Use this API operation to specify which client devices can discover a core device through cloud discovery. With cloud discovery, client devices connect to IoT Greengrass to retrieve associated core devices' connectivity information and certificates. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-cloud-discovery.html">Configure cloud discovery</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p> <note> <p>Client devices are local IoT devices that connect to and communicate with an IoT Greengrass core device over MQTT. You can connect client devices to a core device to sync MQTT messages and data to Amazon Web Services IoT Core and interact with client devices in Greengrass components. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/interact-with-local-iot-devices.html">Interact with local IoT devices</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p> </note>

        Args:
            entries: <p>The list of client devices to associate.</p>
            core_device_thing_name: <p>The name of the core device. This is also the name of the IoT thing.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.batch_associate_client_device_with_core_device_request.BatchAssociateClientDeviceWithCoreDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.batch_associate_client_device_with_core_device_response.BatchAssociateClientDeviceWithCoreDeviceResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.batch_associate_client_device_with_core_device

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.batch_associate_client_device_with_core_device.async_batch_associate_client_device_with_core_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.batch_associate_client_device_with_core_device_request.BatchAssociateClientDeviceWithCoreDeviceRequest = {
            "core_device_thing_name": core_device_thing_name
        }
        if entries is not None:
            input_["entries"] = entries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_disassociate_client_device_from_core_device(
        self,
        core_device_thing_name: "capo_greengrassv2.types.io_t_thing_name.IoTThingName",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        entries: Optional[
            "capo_greengrassv2.types.disassociate_client_device_from_core_device_entry_list.DisassociateClientDeviceFromCoreDeviceEntryList"
        ] = None,
    ) -> "capo_greengrassv2.types.batch_disassociate_client_device_from_core_device_response.BatchDisassociateClientDeviceFromCoreDeviceResponse":
        """<p>Disassociates a list of client devices from a core device. After you disassociate a client device from a core device, the client device won't be able to use cloud discovery to retrieve the core device's connectivity information and certificates.</p>

        Args:
            entries: <p>The list of client devices to disassociate.</p>
            core_device_thing_name: <p>The name of the core device. This is also the name of the IoT thing.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.batch_disassociate_client_device_from_core_device_request.BatchDisassociateClientDeviceFromCoreDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.batch_disassociate_client_device_from_core_device_response.BatchDisassociateClientDeviceFromCoreDeviceResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.batch_disassociate_client_device_from_core_device

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.batch_disassociate_client_device_from_core_device.async_batch_disassociate_client_device_from_core_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.batch_disassociate_client_device_from_core_device_request.BatchDisassociateClientDeviceFromCoreDeviceRequest = {
            "core_device_thing_name": core_device_thing_name
        }
        if entries is not None:
            input_["entries"] = entries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_deployment(
        self,
        deployment_id: "capo_greengrassv2.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> "capo_greengrassv2.types.cancel_deployment_response.CancelDeploymentResponse":
        """<p>Cancels a deployment. This operation cancels the deployment for devices that haven't yet received it. If a device already received the deployment, this operation doesn't change anything for that device.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.cancel_deployment_request.CancelDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.cancel_deployment_response.CancelDeploymentResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.cancel_deployment

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.cancel_deployment.async_cancel_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.cancel_deployment_request.CancelDeploymentRequest = {
            "deployment_id": deployment_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_component_version(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        inline_recipe: Optional[
            "capo_greengrassv2.types.recipe_blob.RecipeBlob"
        ] = None,
        lambda_function: Optional[
            "capo_greengrassv2.types.lambda_function_recipe_source.LambdaFunctionRecipeSource"
        ] = None,
        tags: Optional["capo_greengrassv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_greengrassv2.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "capo_greengrassv2.types.create_component_version_response.CreateComponentVersionResponse":
        """<p>Creates a component. Components are software that run on Greengrass core devices. After you develop and test a component on your core device, you can use this operation to upload your component to IoT Greengrass. Then, you can deploy the component to other core devices.</p> <p>You can use this operation to do the following:</p> <ul> <li> <p> <b>Create components from recipes</b> </p> <p>Create a component from a recipe, which is a file that defines the component's metadata, parameters, dependencies, lifecycle, artifacts, and platform capability. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html">IoT Greengrass component recipe reference</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p> <p>To create a component from a recipe, specify <code>inlineRecipe</code> when you call this operation.</p> </li> <li> <p> <b>Create components from Lambda functions</b> </p> <p>Create a component from an Lambda function that runs on IoT Greengrass. This creates a recipe and artifacts from the Lambda function's deployment package. You can use this operation to migrate Lambda functions from IoT Greengrass V1 to IoT Greengrass V2.</p> <p>This function accepts Lambda functions in all supported versions of Python, Node.js, and Java runtimes. IoT Greengrass doesn't apply any additional restrictions on deprecated Lambda runtime versions.</p> <p>To create a component from a Lambda function, specify <code>lambdaFunction</code> when you call this operation.</p> <note> <p>IoT Greengrass currently supports Lambda functions on only Linux core devices.</p> </note> </li> </ul>

        Args:
            inline_recipe: <p>The recipe to use to create the component. The recipe defines the component's metadata, parameters, dependencies, lifecycle, artifacts, and platform compatibility.</p> <p>You must specify either <code>inlineRecipe</code> or <code>lambdaFunction</code>.</p>
            lambda_function: <p>The parameters to create a component from a Lambda function.</p> <p>You must specify either <code>inlineRecipe</code> or <code>lambdaFunction</code>.</p>
            tags: <p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>
            client_token: <p>A unique, case-sensitive identifier that you can provide to ensure that the request is idempotent. Idempotency means that the request is successfully processed only once, even if you send the request multiple times. When a request succeeds, and you specify the same client token for subsequent successful requests, the IoT Greengrass V2 service returns the successful response that it caches from the previous request. IoT Greengrass V2 caches successful responses for idempotent requests for up to 8 hours.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.request_already_in_progress_exception.RequestAlreadyInProgressException: <p>The request is already in progress. This exception occurs when you use a client token for multiple requests while IoT Greengrass is still processing an earlier request that uses the same client token.</p>
            capo_greengrassv2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota. For example, you might have the maximum number of components that you can create.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.create_component_version_request.CreateComponentVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.create_component_version_response.CreateComponentVersionResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.create_component_version

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.create_component_version.async_create_component_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.create_component_version_request.CreateComponentVersionRequest = {}
        if inline_recipe is not None:
            input_["inline_recipe"] = inline_recipe
        if lambda_function is not None:
            input_["lambda_function"] = lambda_function
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

    async def create_deployment(
        self,
        target_arn: "capo_greengrassv2.types.target_arn.TargetARN",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        deployment_name: Optional[
            "capo_greengrassv2.types.deployment_name_string.DeploymentNameString"
        ] = None,
        components: Optional[
            "capo_greengrassv2.types.component_deployment_specifications.ComponentDeploymentSpecifications"
        ] = None,
        iot_job_configuration: Optional[
            "capo_greengrassv2.types.deployment_io_t_job_configuration.DeploymentIoTJobConfiguration"
        ] = None,
        deployment_policies: Optional[
            "capo_greengrassv2.types.deployment_policies.DeploymentPolicies"
        ] = None,
        parent_target_arn: Optional[
            "capo_greengrassv2.types.thing_group_arn.ThingGroupARN"
        ] = None,
        tags: Optional["capo_greengrassv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_greengrassv2.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "capo_greengrassv2.types.create_deployment_response.CreateDeploymentResponse":
        """<p>Creates a continuous deployment for a target, which is a Greengrass core device or group of core devices. When you add a new core device to a group of core devices that has a deployment, IoT Greengrass deploys that group's deployment to the new device.</p> <p>You can define one deployment for each target. When you create a new deployment for a target that has an existing deployment, you replace the previous deployment. IoT Greengrass applies the new deployment to the target devices.</p> <p>Every deployment has a revision number that indicates how many deployment revisions you define for a target. Use this operation to create a new revision of an existing deployment.</p> <p>For more information, see the <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html">Create deployments</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>

        Args:
            target_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the target IoT thing or thing group. When creating a subdeployment, the targetARN can only be a thing group.</p>
            deployment_name: <p>The name of the deployment.</p>
            components: <p>The components to deploy. This is a dictionary, where each key is the name of a component, and each key's value is the version and configuration to deploy for that component.</p>
            iot_job_configuration: <p>The job configuration for the deployment configuration. The job configuration specifies the rollout, timeout, and stop configurations for the deployment configuration.</p>
            deployment_policies: <p>The deployment policies for the deployment. These policies define how the deployment updates components and handles failure.</p>
            parent_target_arn: <p>The parent deployment's target <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> within a subdeployment.</p>
            tags: <p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>
            client_token: <p>A unique, case-sensitive identifier that you can provide to ensure that the request is idempotent. Idempotency means that the request is successfully processed only once, even if you send the request multiple times. When a request succeeds, and you specify the same client token for subsequent successful requests, the IoT Greengrass V2 service returns the successful response that it caches from the previous request. IoT Greengrass V2 caches successful responses for idempotent requests for up to 8 hours.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.request_already_in_progress_exception.RequestAlreadyInProgressException: <p>The request is already in progress. This exception occurs when you use a client token for multiple requests while IoT Greengrass is still processing an earlier request that uses the same client token.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.create_deployment_request.CreateDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.create_deployment_response.CreateDeploymentResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.create_deployment

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.create_deployment.async_create_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.create_deployment_request.CreateDeploymentRequest = {
            "target_arn": target_arn
        }
        if deployment_name is not None:
            input_["deployment_name"] = deployment_name
        if components is not None:
            input_["components"] = components
        if iot_job_configuration is not None:
            input_["iot_job_configuration"] = iot_job_configuration
        if deployment_policies is not None:
            input_["deployment_policies"] = deployment_policies
        if parent_target_arn is not None:
            input_["parent_target_arn"] = parent_target_arn
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

    async def delete_component(
        self,
        arn: "capo_greengrassv2.types.component_version_arn.ComponentVersionARN",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a version of a component from IoT Greengrass.</p> <note> <p>This operation deletes the component's recipe and artifacts. As a result, deployments that refer to this component version will fail. If you have deployments that use this component version, you can remove the component from the deployment or update the deployment to use a valid version.</p> </note>

        Args:
            arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component version.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.delete_component_request.DeleteComponentRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_greengrassv2._operations.greengrass_v2.delete_component

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.delete_component.async_delete_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.delete_component_request.DeleteComponentRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_core_device(
        self,
        core_device_thing_name: "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a Greengrass core device, which is an IoT thing. This operation removes the core device from the list of core devices. This operation doesn't delete the IoT thing. For more information about how to delete the IoT thing, see <a href="https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThing.html">DeleteThing</a> in the <i>IoT API Reference</i>.</p>

        Args:
            core_device_thing_name: <p>The name of the core device. This is also the name of the IoT thing.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.delete_core_device_request.DeleteCoreDeviceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_greengrassv2._operations.greengrass_v2.delete_core_device

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.delete_core_device.async_delete_core_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.delete_core_device_request.DeleteCoreDeviceRequest = {
            "core_device_thing_name": core_device_thing_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_deployment(
        self,
        deployment_id: "capo_greengrassv2.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a deployment. To delete an active deployment, you must first cancel it. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/apireference/API_CancelDeployment.html">CancelDeployment</a>.</p> <p>Deleting a deployment doesn't affect core devices that run that deployment, because core devices store the deployment's configuration on the device. Additionally, core devices can roll back to a previous deployment that has been deleted.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.delete_deployment_request.DeleteDeploymentRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_greengrassv2._operations.greengrass_v2.delete_deployment

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.delete_deployment.async_delete_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.delete_deployment_request.DeleteDeploymentRequest = {
            "deployment_id": deployment_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_component(
        self,
        arn: "capo_greengrassv2.types.component_version_arn.ComponentVersionARN",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> (
        "capo_greengrassv2.types.describe_component_response.DescribeComponentResponse"
    ):
        """<p>Retrieves metadata for a version of a component.</p>

        Args:
            arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component version.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.describe_component_request.DescribeComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.describe_component_response.DescribeComponentResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.describe_component

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.describe_component.async_describe_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.describe_component_request.DescribeComponentRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_service_role_from_account(
        self, *, config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None
    ) -> "capo_greengrassv2.types.disassociate_service_role_from_account_response.DisassociateServiceRoleFromAccountResponse":
        """<p>Disassociates the Greengrass service role from IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region. Without a service role, IoT Greengrass can't verify the identity of client devices or manage core device connectivity information. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html">Greengrass service role</a> in the <i>IoT Greengrass Version 2 Developer Guide</i>.</p>

        Raises:
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.disassociate_service_role_from_account_request.DisassociateServiceRoleFromAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.disassociate_service_role_from_account_response.DisassociateServiceRoleFromAccountResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.disassociate_service_role_from_account

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.disassociate_service_role_from_account.async_disassociate_service_role_from_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.disassociate_service_role_from_account_request.DisassociateServiceRoleFromAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_component(
        self,
        arn: "capo_greengrassv2.types.component_version_arn.ComponentVersionARN",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        recipe_output_format: Optional[
            "capo_greengrassv2.types.recipe_output_format.RecipeOutputFormat"
        ] = None,
    ) -> "capo_greengrassv2.types.get_component_response.GetComponentResponse":
        """<p>Gets the recipe for a version of a component.</p>

        Args:
            recipe_output_format: <p>The format of the recipe.</p>
            arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component version.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.get_component_request.GetComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.get_component_response.GetComponentResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.get_component

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.get_component.async_get_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.get_component_request.GetComponentRequest = {
            "arn": arn
        }
        if recipe_output_format is not None:
            input_["recipe_output_format"] = recipe_output_format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_component_version_artifact(
        self,
        arn: "capo_greengrassv2.types.component_version_arn.ComponentVersionARN",
        artifact_name: "capo_greengrassv2.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        s3_endpoint_type: Optional[
            "capo_greengrassv2.types.s3_endpoint_type.S3EndpointType"
        ] = None,
        iot_endpoint_type: Optional[
            "capo_greengrassv2.types.iot_endpoint_type.IotEndpointType"
        ] = None,
    ) -> "capo_greengrassv2.types.get_component_version_artifact_response.GetComponentVersionArtifactResponse":
        """<p>Gets the pre-signed URL to download a public or a Lambda component artifact. Core devices call this operation to identify the URL that they can use to download an artifact to install.</p>

        Args:
            arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component version. Specify the ARN of a public or a Lambda component version.</p>
            artifact_name: <p>The name of the artifact.</p> <p>You can use the <a href="https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponent.html">GetComponent</a> operation to download the component recipe, which includes the URI of the artifact. The artifact name is the section of the URI after the scheme. For example, in the artifact URI <code>greengrass:SomeArtifact.zip</code>, the artifact name is <code>SomeArtifact.zip</code>.</p>
            s3_endpoint_type: <p>Specifies the endpoint to use when getting Amazon S3 pre-signed URLs.</p> <p>All Amazon Web Services Regions except US East (N. Virginia) use <code>REGIONAL</code> in all cases. In the US East (N. Virginia) Region the default is <code>GLOBAL</code>, but you can change it to <code>REGIONAL</code> with this parameter.</p>
            iot_endpoint_type: <p>Determines if the Amazon S3 URL returned is a FIPS pre-signed URL endpoint. Specify <code>fips</code> if you want the returned Amazon S3 pre-signed URL to point to an Amazon S3 FIPS endpoint. If you don't specify a value, the default is <code>standard</code>.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.get_component_version_artifact_request.GetComponentVersionArtifactRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.get_component_version_artifact_response.GetComponentVersionArtifactResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.get_component_version_artifact

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.get_component_version_artifact.async_get_component_version_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.get_component_version_artifact_request.GetComponentVersionArtifactRequest = {
            "arn": arn,
            "artifact_name": artifact_name,
        }
        if s3_endpoint_type is not None:
            input_["s3_endpoint_type"] = s3_endpoint_type
        if iot_endpoint_type is not None:
            input_["iot_endpoint_type"] = iot_endpoint_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connectivity_info(
        self,
        thing_name: "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> "capo_greengrassv2.types.get_connectivity_info_response.GetConnectivityInfoResponse":
        """<p>Retrieves connectivity information for a Greengrass core device.</p> <p>Connectivity information includes endpoints and ports where client devices can connect to an MQTT broker on the core device. When a client device calls the <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-discover-api.html">IoT Greengrass discovery API</a>, IoT Greengrass returns connectivity information for all of the core devices where the client device can connect. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/connect-client-devices.html">Connect client devices to core devices</a> in the <i>IoT Greengrass Version 2 Developer Guide</i>.</p>

        Args:
            thing_name: <p>The name of the core device. This is also the name of the IoT thing.</p>

        Raises:
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.get_connectivity_info_request.GetConnectivityInfoRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.get_connectivity_info_response.GetConnectivityInfoResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.get_connectivity_info

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.get_connectivity_info.async_get_connectivity_info(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.get_connectivity_info_request.GetConnectivityInfoRequest = {
            "thing_name": thing_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_core_device(
        self,
        core_device_thing_name: "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> "capo_greengrassv2.types.get_core_device_response.GetCoreDeviceResponse":
        """<p>Retrieves metadata for a Greengrass core device.</p> <note> <p>IoT Greengrass relies on individual devices to send status updates to the Amazon Web Services Cloud. If the IoT Greengrass Core software isn't running on the device, or if device isn't connected to the Amazon Web Services Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.</p> <p>Core devices send status updates at the following times:</p> <ul> <li> <p>When the IoT Greengrass Core software starts</p> </li> <li> <p>When the core device receives a deployment from the Amazon Web Services Cloud</p> </li> <li> <p>When the status of any component on the core device becomes <code>BROKEN</code> </p> </li> <li> <p>At a <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss">regular interval that you can configure</a>, which defaults to 24 hours</p> </li> <li> <p>For IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment</p> </li> </ul> </note>

        Args:
            core_device_thing_name: <p>The name of the core device. This is also the name of the IoT thing.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.get_core_device_request.GetCoreDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.get_core_device_response.GetCoreDeviceResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.get_core_device

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.get_core_device.async_get_core_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.get_core_device_request.GetCoreDeviceRequest = {
            "core_device_thing_name": core_device_thing_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_deployment(
        self,
        deployment_id: "capo_greengrassv2.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> "capo_greengrassv2.types.get_deployment_response.GetDeploymentResponse":
        """<p>Gets a deployment. Deployments define the components that run on Greengrass core devices.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.get_deployment_request.GetDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.get_deployment_response.GetDeploymentResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.get_deployment

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.get_deployment.async_get_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.get_deployment_request.GetDeploymentRequest = {
            "deployment_id": deployment_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_role_for_account(
        self, *, config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None
    ) -> "capo_greengrassv2.types.get_service_role_for_account_response.GetServiceRoleForAccountResponse":
        """<p>Gets the service role associated with IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region. IoT Greengrass uses this role to verify the identity of client devices and manage core device connectivity information. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html">Greengrass service role</a> in the <i>IoT Greengrass Version 2 Developer Guide</i>.</p>

        Raises:
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.get_service_role_for_account_request.GetServiceRoleForAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.get_service_role_for_account_response.GetServiceRoleForAccountResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.get_service_role_for_account

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.get_service_role_for_account.async_get_service_role_for_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.get_service_role_for_account_request.GetServiceRoleForAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_client_devices_associated_with_core_device(
        self,
        core_device_thing_name: "capo_greengrassv2.types.io_t_thing_name.IoTThingName",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "capo_greengrassv2.types.list_client_devices_associated_with_core_device_response.ListClientDevicesAssociatedWithCoreDeviceResponse":
        """<p>Retrieves a paginated list of client devices that are associated with a core device.</p>

        Args:
            core_device_thing_name: <p>The name of the core device. This is also the name of the IoT thing.</p>
            max_results: <p>The maximum number of results to be returned per paginated request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.list_client_devices_associated_with_core_device_request.ListClientDevicesAssociatedWithCoreDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.list_client_devices_associated_with_core_device_response.ListClientDevicesAssociatedWithCoreDeviceResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.list_client_devices_associated_with_core_device

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.list_client_devices_associated_with_core_device.async_list_client_devices_associated_with_core_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.list_client_devices_associated_with_core_device_request.ListClientDevicesAssociatedWithCoreDeviceRequest = {
            "core_device_thing_name": core_device_thing_name
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

    async def iter_list_client_devices_associated_with_core_device(
        self,
        core_device_thing_name: "capo_greengrassv2.types.io_t_thing_name.IoTThingName",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "AsyncIterator[capo_greengrassv2.types.associated_client_device.AssociatedClientDevice]":
        _token = next_token
        while True:
            _response = await self.list_client_devices_associated_with_core_device(
                core_device_thing_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("associated_client_devices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_components(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        scope: Optional[
            "capo_greengrassv2.types.component_visibility_scope.ComponentVisibilityScope"
        ] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "capo_greengrassv2.types.list_components_response.ListComponentsResponse":
        """<p>Retrieves a paginated list of component summaries. This list includes components that you have permission to view.</p>

        Args:
            scope: <p>The scope of the components to list.</p> <p>Default: <code>PRIVATE</code> </p>
            max_results: <p>The maximum number of results to be returned per paginated request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.list_components_request.ListComponentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.list_components_response.ListComponentsResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.list_components

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.list_components.async_list_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.list_components_request.ListComponentsRequest = {}
        if scope is not None:
            input_["scope"] = scope
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

    async def iter_list_components(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        scope: Optional[
            "capo_greengrassv2.types.component_visibility_scope.ComponentVisibilityScope"
        ] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "AsyncIterator[capo_greengrassv2.types.component.Component]":
        _token = next_token
        while True:
            _response = await self.list_components(
                config_overrides=config_overrides,
                scope=scope,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("components",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_component_versions(
        self,
        arn: "capo_greengrassv2.types.component_arn.ComponentARN",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "capo_greengrassv2.types.list_component_versions_response.ListComponentVersionsResponse":
        """<p>Retrieves a paginated list of all versions for a component. Greater versions are listed first.</p>

        Args:
            arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component.</p>
            max_results: <p>The maximum number of results to be returned per paginated request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.list_component_versions_request.ListComponentVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.list_component_versions_response.ListComponentVersionsResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.list_component_versions

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.list_component_versions.async_list_component_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.list_component_versions_request.ListComponentVersionsRequest = {
            "arn": arn
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

    async def iter_list_component_versions(
        self,
        arn: "capo_greengrassv2.types.component_arn.ComponentARN",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "AsyncIterator[capo_greengrassv2.types.component_version_list_item.ComponentVersionListItem]":
        _token = next_token
        while True:
            _response = await self.list_component_versions(
                arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("component_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_core_devices(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        thing_group_arn: Optional[
            "capo_greengrassv2.types.thing_group_arn.ThingGroupARN"
        ] = None,
        status: Optional[
            "capo_greengrassv2.types.core_device_status.CoreDeviceStatus"
        ] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
        runtime: Optional[
            "capo_greengrassv2.types.core_device_runtime_string.CoreDeviceRuntimeString"
        ] = None,
    ) -> "capo_greengrassv2.types.list_core_devices_response.ListCoreDevicesResponse":
        """<p>Retrieves a paginated list of Greengrass core devices.</p> <note> <p>IoT Greengrass relies on individual devices to send status updates to the Amazon Web Services Cloud. If the IoT Greengrass Core software isn't running on the device, or if device isn't connected to the Amazon Web Services Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.</p> <p>Core devices send status updates at the following times:</p> <ul> <li> <p>When the IoT Greengrass Core software starts</p> </li> <li> <p>When the core device receives a deployment from the Amazon Web Services Cloud</p> </li> <li> <p>For Greengrass nucleus 2.12.2 and earlier, the core device sends status updates when the status of any component on the core device becomes <code>ERRORED</code> or <code>BROKEN</code>.</p> </li> <li> <p>For Greengrass nucleus 2.12.3 and later, the core device sends status updates when the status of any component on the core device becomes <code>ERRORED</code>, <code>BROKEN</code>, <code>RUNNING</code>, or <code>FINISHED</code>.</p> </li> <li> <p>At a <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss">regular interval that you can configure</a>, which defaults to 24 hours</p> </li> <li> <p>For IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment</p> </li> </ul> </note>

        Args:
            thing_group_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the IoT thing group by which to filter. If you specify this parameter, the list includes only core devices that have successfully deployed a deployment that targets the thing group. When you remove a core device from a thing group, the list continues to include that core device.</p>
            status: <p>The core device status by which to filter. If you specify this parameter, the list includes only core devices that have this status. Choose one of the following options:</p> <ul> <li> <p> <code>HEALTHY</code> – The IoT Greengrass Core software and all components run on the core device without issue.</p> </li> <li> <p> <code>UNHEALTHY</code> – The IoT Greengrass Core software or a component is in a failed state on the core device.</p> </li> </ul>
            max_results: <p>The maximum number of results to be returned per paginated request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            runtime: <p>The runtime to be used by the core device. The runtime can be:</p> <ul> <li> <p> <code>aws_nucleus_classic</code> </p> </li> <li> <p> <code>aws_nucleus_lite</code> </p> </li> </ul>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.list_core_devices_request.ListCoreDevicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.list_core_devices_response.ListCoreDevicesResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.list_core_devices

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.list_core_devices.async_list_core_devices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.list_core_devices_request.ListCoreDevicesRequest = {}
        if thing_group_arn is not None:
            input_["thing_group_arn"] = thing_group_arn
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if runtime is not None:
            input_["runtime"] = runtime

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_core_devices(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        thing_group_arn: Optional[
            "capo_greengrassv2.types.thing_group_arn.ThingGroupARN"
        ] = None,
        status: Optional[
            "capo_greengrassv2.types.core_device_status.CoreDeviceStatus"
        ] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
        runtime: Optional[
            "capo_greengrassv2.types.core_device_runtime_string.CoreDeviceRuntimeString"
        ] = None,
    ) -> "AsyncIterator[capo_greengrassv2.types.core_device.CoreDevice]":
        _token = next_token
        while True:
            _response = await self.list_core_devices(
                config_overrides=config_overrides,
                thing_group_arn=thing_group_arn,
                status=status,
                max_results=max_results,
                next_token=_token,
                runtime=runtime,
            )
            _page = _resolve_path(_response, ("core_devices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_deployments(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        target_arn: Optional["capo_greengrassv2.types.target_arn.TargetARN"] = None,
        history_filter: Optional[
            "capo_greengrassv2.types.deployment_history_filter.DeploymentHistoryFilter"
        ] = None,
        parent_target_arn: Optional[
            "capo_greengrassv2.types.thing_group_arn.ThingGroupARN"
        ] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "capo_greengrassv2.types.list_deployments_response.ListDeploymentsResponse":
        """<p>Retrieves a paginated list of deployments.</p>

        Args:
            target_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the target IoT thing or thing group.</p>
            history_filter: <p>The filter for the list of deployments. Choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all deployments.</p> </li> <li> <p> <code>LATEST_ONLY</code> – The list includes only the latest revision of each deployment.</p> </li> </ul> <p>Default: <code>LATEST_ONLY</code> </p>
            parent_target_arn: <p>The parent deployment's target <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> within a subdeployment.</p>
            max_results: <p>The maximum number of results to be returned per paginated request.</p> <p>Default: <code>50</code> </p>
            next_token: <p>The token to be used for the next set of paginated results.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.list_deployments_request.ListDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.list_deployments_response.ListDeploymentsResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.list_deployments

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.list_deployments.async_list_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.list_deployments_request.ListDeploymentsRequest = {}
        if target_arn is not None:
            input_["target_arn"] = target_arn
        if history_filter is not None:
            input_["history_filter"] = history_filter
        if parent_target_arn is not None:
            input_["parent_target_arn"] = parent_target_arn
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

    async def iter_list_deployments(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        target_arn: Optional["capo_greengrassv2.types.target_arn.TargetARN"] = None,
        history_filter: Optional[
            "capo_greengrassv2.types.deployment_history_filter.DeploymentHistoryFilter"
        ] = None,
        parent_target_arn: Optional[
            "capo_greengrassv2.types.thing_group_arn.ThingGroupARN"
        ] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "AsyncIterator[capo_greengrassv2.types.deployment.Deployment]":
        _token = next_token
        while True:
            _response = await self.list_deployments(
                config_overrides=config_overrides,
                target_arn=target_arn,
                history_filter=history_filter,
                parent_target_arn=parent_target_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("deployments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_effective_deployments(
        self,
        core_device_thing_name: "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "capo_greengrassv2.types.list_effective_deployments_response.ListEffectiveDeploymentsResponse":
        """<p>Retrieves a paginated list of deployment jobs that IoT Greengrass sends to Greengrass core devices.</p>

        Args:
            core_device_thing_name: <p>The name of the core device. This is also the name of the IoT thing.</p>
            max_results: <p>The maximum number of results to be returned per paginated request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.list_effective_deployments_request.ListEffectiveDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.list_effective_deployments_response.ListEffectiveDeploymentsResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.list_effective_deployments

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.list_effective_deployments.async_list_effective_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.list_effective_deployments_request.ListEffectiveDeploymentsRequest = {
            "core_device_thing_name": core_device_thing_name
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

    async def iter_list_effective_deployments(
        self,
        core_device_thing_name: "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "AsyncIterator[capo_greengrassv2.types.effective_deployment.EffectiveDeployment]":
        _token = next_token
        while True:
            _response = await self.list_effective_deployments(
                core_device_thing_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("effective_deployments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_installed_components(
        self,
        core_device_thing_name: "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
        topology_filter: Optional[
            "capo_greengrassv2.types.installed_component_topology_filter.InstalledComponentTopologyFilter"
        ] = None,
    ) -> "capo_greengrassv2.types.list_installed_components_response.ListInstalledComponentsResponse":
        """<p>Retrieves a paginated list of the components that a Greengrass core device runs. By default, this list doesn't include components that are deployed as dependencies of other components. To include dependencies in the response, set the <code>topologyFilter</code> parameter to <code>ALL</code>.</p> <note> <p>IoT Greengrass relies on individual devices to send status updates to the Amazon Web Services Cloud. If the IoT Greengrass Core software isn't running on the device, or if device isn't connected to the Amazon Web Services Cloud, then the reported status of that device might not reflect its current status. The status timestamp indicates when the device status was last updated.</p> <p>Core devices send status updates at the following times:</p> <ul> <li> <p>When the IoT Greengrass Core software starts</p> </li> <li> <p>When the core device receives a deployment from the Amazon Web Services Cloud</p> </li> <li> <p>When the status of any component on the core device becomes <code>BROKEN</code> </p> </li> <li> <p>At a <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html#greengrass-nucleus-component-configuration-fss">regular interval that you can configure</a>, which defaults to 24 hours</p> </li> <li> <p>For IoT Greengrass Core v2.7.0, the core device sends status updates upon local deployment and cloud deployment</p> </li> </ul> </note>

        Args:
            core_device_thing_name: <p>The name of the core device. This is also the name of the IoT thing.</p>
            max_results: <p>The maximum number of results to be returned per paginated request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            topology_filter: <p>The filter for the list of components. Choose from the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all components installed on the core device.</p> </li> <li> <p> <code>ROOT</code> – The list includes only <i>root</i> components, which are components that you specify in a deployment. When you choose this option, the list doesn't include components that the core device installs as dependencies of other components.</p> </li> </ul> <p>Default: <code>ROOT</code> </p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.list_installed_components_request.ListInstalledComponentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.list_installed_components_response.ListInstalledComponentsResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.list_installed_components

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.list_installed_components.async_list_installed_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.list_installed_components_request.ListInstalledComponentsRequest = {
            "core_device_thing_name": core_device_thing_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if topology_filter is not None:
            input_["topology_filter"] = topology_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_installed_components(
        self,
        core_device_thing_name: "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        max_results: Optional[
            "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
        ] = None,
        next_token: Optional[
            "capo_greengrassv2.types.next_token_string.NextTokenString"
        ] = None,
        topology_filter: Optional[
            "capo_greengrassv2.types.installed_component_topology_filter.InstalledComponentTopologyFilter"
        ] = None,
    ) -> (
        "AsyncIterator[capo_greengrassv2.types.installed_component.InstalledComponent]"
    ):
        _token = next_token
        while True:
            _response = await self.list_installed_components(
                core_device_thing_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                topology_filter=topology_filter,
            )
            _page = _resolve_path(_response, ("installed_components",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_greengrassv2.types.generic_v2_arn.GenericV2ARN",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> "capo_greengrassv2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the list of tags for an IoT Greengrass resource.</p>

        Args:
            resource_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the resource.</p>

        Raises:
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resolve_component_candidates(
        self,
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
        platform: Optional[
            "capo_greengrassv2.types.component_platform.ComponentPlatform"
        ] = None,
        component_candidates: Optional[
            "capo_greengrassv2.types.component_candidate_list.ComponentCandidateList"
        ] = None,
    ) -> "capo_greengrassv2.types.resolve_component_candidates_response.ResolveComponentCandidatesResponse":
        """<p>Retrieves a list of components that meet the component, version, and platform requirements of a deployment. Greengrass core devices call this operation when they receive a deployment to identify the components to install.</p> <p>This operation identifies components that meet all dependency requirements for a deployment. If the requirements conflict, then this operation returns an error and the deployment fails. For example, this occurs if component <code>A</code> requires version <code>>2.0.0</code> and component <code>B</code> requires version <code><2.0.0</code> of a component dependency.</p> <p>When you specify the component candidates to resolve, IoT Greengrass compares each component's digest from the core device with the component's digest in the Amazon Web Services Cloud. If the digests don't match, then IoT Greengrass specifies to use the version from the Amazon Web Services Cloud.</p> <important> <p>To use this operation, you must use the data plane API endpoint and authenticate with an IoT device certificate. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/greengrass.html">IoT Greengrass endpoints and quotas</a>.</p> </important>

        Args:
            platform: <p>The platform to use to resolve compatible components.</p>
            component_candidates: <p>The list of components to resolve.</p>

        Raises:
            capo_greengrassv2.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_greengrassv2.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.resolve_component_candidates_request.ResolveComponentCandidatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.resolve_component_candidates_response.ResolveComponentCandidatesResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.resolve_component_candidates

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.resolve_component_candidates.async_resolve_component_candidates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.resolve_component_candidates_request.ResolveComponentCandidatesRequest = {}
        if platform is not None:
            input_["platform"] = platform
        if component_candidates is not None:
            input_["component_candidates"] = component_candidates

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_greengrassv2.types.generic_v2_arn.GenericV2ARN",
        tags: "capo_greengrassv2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> "capo_greengrassv2.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to an IoT Greengrass resource. If a tag already exists for the resource, this operation updates the tag's value.</p>

        Args:
            resource_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the resource to tag.</p>
            tags: <p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>

        Raises:
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.tag_resource

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
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
        resource_arn: "capo_greengrassv2.types.generic_v2_arn.GenericV2ARN",
        tag_keys: "capo_greengrassv2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> "capo_greengrassv2.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from an IoT Greengrass resource.</p>

        Args:
            resource_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the resource to untag.</p>
            tag_keys: <p>A list of keys for tags to remove from the resource.</p>

        Raises:
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.untag_resource

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connectivity_info(
        self,
        thing_name: "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName",
        connectivity_info: "capo_greengrassv2.types.connectivity_info_list.connectivityInfoList",
        *,
        config_overrides: Optional[AsyncGreengrassV2ClientConfig] = None,
    ) -> "capo_greengrassv2.types.update_connectivity_info_response.UpdateConnectivityInfoResponse":
        """<p>Updates connectivity information for a Greengrass core device.</p> <p>Connectivity information includes endpoints and ports where client devices can connect to an MQTT broker on the core device. When a client device calls the <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-discover-api.html">IoT Greengrass discovery API</a>, IoT Greengrass returns connectivity information for all of the core devices where the client device can connect. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/connect-client-devices.html">Connect client devices to core devices</a> in the <i>IoT Greengrass Version 2 Developer Guide</i>.</p>

        Args:
            thing_name: <p>The name of the core device. This is also the name of the IoT thing.</p>
            connectivity_info: <p>The connectivity information for the core device.</p>

        Raises:
            capo_greengrassv2.errors.internal_server_exception.InternalServerException: <p>IoT Greengrass can't process your request right now. Try again later.</p>
            capo_greengrassv2.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_greengrassv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_greengrassv2.types.update_connectivity_info_request.UpdateConnectivityInfoRequest]",
        ) -> AsyncOperationResponse[
            "capo_greengrassv2.types.update_connectivity_info_response.UpdateConnectivityInfoResponse"
        ]:
            import capo_greengrassv2._operations.greengrass_v2.update_connectivity_info

            (
                output,
                http_response,
            ) = await capo_greengrassv2._operations.greengrass_v2.update_connectivity_info.async_update_connectivity_info(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_greengrassv2.types.update_connectivity_info_request.UpdateConnectivityInfoRequest = {
            "thing_name": thing_name,
            "connectivity_info": connectivity_info,
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
