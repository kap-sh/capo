"""Generated from Smithy shape ``com.amazonaws.ecs#AmazonEC2ContainerServiceV20141113``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_ecs._auth._signers
import capo_ecs._auth._sigv4
from capo_ecs._auth._identity import Credentials
from capo_ecs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ecs._auth._zapros_handler import AuthMiddleware
from capo_ecs._pagination import resolve_path as _resolve_path
from capo_ecs._resources.amazon_ec2_container_service_v20141113.capacity_provider_resource import (
    AsyncCapacityProviderResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.cluster_resource import (
    AsyncClusterResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.container_instance_resource import (
    AsyncContainerInstanceResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.daemon_deployment_resource import (
    AsyncDaemonDeploymentResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.daemon_resource import (
    AsyncDaemonResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.daemon_revision_resource import (
    AsyncDaemonRevisionResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.daemon_task_definition_resource import (
    AsyncDaemonTaskDefinitionResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.service_deployment_resource import (
    AsyncServiceDeploymentResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.service_resource import (
    AsyncServiceResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.service_revision_resource import (
    AsyncServiceRevisionResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.task_definition_resource import (
    AsyncTaskDefinitionResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.task_resource import (
    AsyncTaskResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.task_set_resource import (
    AsyncTaskSetResource,
)
from capo_ecs._services._aws_config import aaws_config
from capo_ecs._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_ecs.types.attachment_state_changes
    import capo_ecs.types.attribute
    import capo_ecs.types.attributes
    import capo_ecs.types.auto_scaling_group_provider
    import capo_ecs.types.auto_scaling_group_provider_update
    import capo_ecs.types.availability_zone_rebalancing
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.capacity_provider_field_list
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.cluster_configuration
    import capo_ecs.types.cluster_field_list
    import capo_ecs.types.cluster_service_connect_defaults_request
    import capo_ecs.types.cluster_settings
    import capo_ecs.types.compatibility_list
    import capo_ecs.types.container_definitions
    import capo_ecs.types.container_instance_field_list
    import capo_ecs.types.container_instance_status
    import capo_ecs.types.container_state_changes
    import capo_ecs.types.continue_service_deployment_request
    import capo_ecs.types.continue_service_deployment_response
    import capo_ecs.types.create_capacity_provider_request
    import capo_ecs.types.create_capacity_provider_response
    import capo_ecs.types.create_cluster_request
    import capo_ecs.types.create_cluster_response
    import capo_ecs.types.create_daemon_request
    import capo_ecs.types.create_daemon_response
    import capo_ecs.types.create_express_gateway_service_request
    import capo_ecs.types.create_express_gateway_service_response
    import capo_ecs.types.create_managed_instances_provider_configuration
    import capo_ecs.types.create_service_request
    import capo_ecs.types.create_service_response
    import capo_ecs.types.create_task_set_request
    import capo_ecs.types.create_task_set_response
    import capo_ecs.types.created_at
    import capo_ecs.types.daemon_container_definition_list
    import capo_ecs.types.daemon_deployment_configuration
    import capo_ecs.types.daemon_deployment_status_list
    import capo_ecs.types.daemon_ipc_mode
    import capo_ecs.types.daemon_pid_mode
    import capo_ecs.types.daemon_propagate_tags
    import capo_ecs.types.daemon_task_definition_revision_filter
    import capo_ecs.types.daemon_task_definition_status_filter
    import capo_ecs.types.daemon_volume_list
    import capo_ecs.types.delete_account_setting_request
    import capo_ecs.types.delete_account_setting_response
    import capo_ecs.types.delete_attributes_request
    import capo_ecs.types.delete_attributes_response
    import capo_ecs.types.delete_capacity_provider_request
    import capo_ecs.types.delete_capacity_provider_response
    import capo_ecs.types.delete_cluster_request
    import capo_ecs.types.delete_cluster_response
    import capo_ecs.types.delete_daemon_request
    import capo_ecs.types.delete_daemon_response
    import capo_ecs.types.delete_daemon_task_definition_request
    import capo_ecs.types.delete_daemon_task_definition_response
    import capo_ecs.types.delete_express_gateway_service_request
    import capo_ecs.types.delete_express_gateway_service_response
    import capo_ecs.types.delete_service_request
    import capo_ecs.types.delete_service_response
    import capo_ecs.types.delete_task_definitions_request
    import capo_ecs.types.delete_task_definitions_response
    import capo_ecs.types.delete_task_set_request
    import capo_ecs.types.delete_task_set_response
    import capo_ecs.types.deployment_configuration
    import capo_ecs.types.deployment_controller
    import capo_ecs.types.deployment_lifecycle_hook_action
    import capo_ecs.types.deregister_container_instance_request
    import capo_ecs.types.deregister_container_instance_response
    import capo_ecs.types.deregister_task_definition_request
    import capo_ecs.types.deregister_task_definition_response
    import capo_ecs.types.describe_capacity_providers_request
    import capo_ecs.types.describe_capacity_providers_response
    import capo_ecs.types.describe_clusters_request
    import capo_ecs.types.describe_clusters_response
    import capo_ecs.types.describe_container_instances_request
    import capo_ecs.types.describe_container_instances_response
    import capo_ecs.types.describe_daemon_deployments_request
    import capo_ecs.types.describe_daemon_deployments_response
    import capo_ecs.types.describe_daemon_request
    import capo_ecs.types.describe_daemon_response
    import capo_ecs.types.describe_daemon_revisions_request
    import capo_ecs.types.describe_daemon_revisions_response
    import capo_ecs.types.describe_daemon_task_definition_request
    import capo_ecs.types.describe_daemon_task_definition_response
    import capo_ecs.types.describe_express_gateway_service_request
    import capo_ecs.types.describe_express_gateway_service_response
    import capo_ecs.types.describe_service_deployments_request
    import capo_ecs.types.describe_service_deployments_response
    import capo_ecs.types.describe_service_revisions_request
    import capo_ecs.types.describe_service_revisions_response
    import capo_ecs.types.describe_services_request
    import capo_ecs.types.describe_services_response
    import capo_ecs.types.describe_task_definition_request
    import capo_ecs.types.describe_task_definition_response
    import capo_ecs.types.describe_task_sets_request
    import capo_ecs.types.describe_task_sets_response
    import capo_ecs.types.describe_tasks_request
    import capo_ecs.types.describe_tasks_response
    import capo_ecs.types.desired_status
    import capo_ecs.types.discover_poll_endpoint_request
    import capo_ecs.types.discover_poll_endpoint_response
    import capo_ecs.types.ephemeral_storage
    import capo_ecs.types.execute_command_request
    import capo_ecs.types.execute_command_response
    import capo_ecs.types.express_cpu_architecture
    import capo_ecs.types.express_gateway_container
    import capo_ecs.types.express_gateway_scaling_target
    import capo_ecs.types.express_gateway_service_include_list
    import capo_ecs.types.express_gateway_service_network_configuration
    import capo_ecs.types.get_task_protection_request
    import capo_ecs.types.get_task_protection_response
    import capo_ecs.types.inference_accelerators
    import capo_ecs.types.integer
    import capo_ecs.types.ipc_mode
    import capo_ecs.types.launch_type
    import capo_ecs.types.list_account_settings_request
    import capo_ecs.types.list_account_settings_response
    import capo_ecs.types.list_attributes_request
    import capo_ecs.types.list_attributes_response
    import capo_ecs.types.list_clusters_request
    import capo_ecs.types.list_clusters_response
    import capo_ecs.types.list_container_instances_request
    import capo_ecs.types.list_container_instances_response
    import capo_ecs.types.list_daemon_deployments_request
    import capo_ecs.types.list_daemon_deployments_response
    import capo_ecs.types.list_daemon_task_definitions_request
    import capo_ecs.types.list_daemon_task_definitions_response
    import capo_ecs.types.list_daemons_request
    import capo_ecs.types.list_daemons_response
    import capo_ecs.types.list_service_deployments_request
    import capo_ecs.types.list_service_deployments_response
    import capo_ecs.types.list_services_by_namespace_request
    import capo_ecs.types.list_services_by_namespace_response
    import capo_ecs.types.list_services_request
    import capo_ecs.types.list_services_response
    import capo_ecs.types.list_tags_for_resource_request
    import capo_ecs.types.list_tags_for_resource_response
    import capo_ecs.types.list_task_definition_families_request
    import capo_ecs.types.list_task_definition_families_response
    import capo_ecs.types.list_task_definitions_request
    import capo_ecs.types.list_task_definitions_response
    import capo_ecs.types.list_tasks_request
    import capo_ecs.types.list_tasks_response
    import capo_ecs.types.load_balancers
    import capo_ecs.types.managed_agent_state_changes
    import capo_ecs.types.monitoring_configuration
    import capo_ecs.types.network_bindings
    import capo_ecs.types.network_configuration
    import capo_ecs.types.network_mode
    import capo_ecs.types.pid_mode
    import capo_ecs.types.placement_constraints
    import capo_ecs.types.placement_strategies
    import capo_ecs.types.platform_devices
    import capo_ecs.types.propagate_tags
    import capo_ecs.types.proxy_configuration
    import capo_ecs.types.put_account_setting_default_request
    import capo_ecs.types.put_account_setting_default_response
    import capo_ecs.types.put_account_setting_request
    import capo_ecs.types.put_account_setting_response
    import capo_ecs.types.put_attributes_request
    import capo_ecs.types.put_attributes_response
    import capo_ecs.types.put_cluster_capacity_providers_request
    import capo_ecs.types.put_cluster_capacity_providers_response
    import capo_ecs.types.register_container_instance_request
    import capo_ecs.types.register_container_instance_response
    import capo_ecs.types.register_daemon_task_definition_request
    import capo_ecs.types.register_daemon_task_definition_response
    import capo_ecs.types.register_task_definition_request
    import capo_ecs.types.register_task_definition_response
    import capo_ecs.types.resource_management_type
    import capo_ecs.types.resources
    import capo_ecs.types.run_task_request
    import capo_ecs.types.run_task_response
    import capo_ecs.types.runtime_platform
    import capo_ecs.types.scale
    import capo_ecs.types.scheduling_strategy
    import capo_ecs.types.service_connect_configuration
    import capo_ecs.types.service_deployment_status_list
    import capo_ecs.types.service_field_list
    import capo_ecs.types.service_registries
    import capo_ecs.types.service_volume_configurations
    import capo_ecs.types.setting
    import capo_ecs.types.setting_name
    import capo_ecs.types.sort_order
    import capo_ecs.types.start_task_request
    import capo_ecs.types.start_task_response
    import capo_ecs.types.stop_service_deployment_request
    import capo_ecs.types.stop_service_deployment_response
    import capo_ecs.types.stop_service_deployment_stop_type
    import capo_ecs.types.stop_task_request
    import capo_ecs.types.stop_task_response
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.submit_attachment_state_changes_request
    import capo_ecs.types.submit_attachment_state_changes_response
    import capo_ecs.types.submit_container_state_change_request
    import capo_ecs.types.submit_container_state_change_response
    import capo_ecs.types.submit_task_state_change_request
    import capo_ecs.types.submit_task_state_change_response
    import capo_ecs.types.tag_keys
    import capo_ecs.types.tag_resource_request
    import capo_ecs.types.tag_resource_response
    import capo_ecs.types.tags
    import capo_ecs.types.target_type
    import capo_ecs.types.task_definition_family_status
    import capo_ecs.types.task_definition_field_list
    import capo_ecs.types.task_definition_placement_constraints
    import capo_ecs.types.task_definition_status
    import capo_ecs.types.task_field_list
    import capo_ecs.types.task_override
    import capo_ecs.types.task_set_field_list
    import capo_ecs.types.task_volume_configurations
    import capo_ecs.types.timestamp
    import capo_ecs.types.untag_resource_request
    import capo_ecs.types.untag_resource_response
    import capo_ecs.types.update_capacity_provider_request
    import capo_ecs.types.update_capacity_provider_response
    import capo_ecs.types.update_cluster_request
    import capo_ecs.types.update_cluster_response
    import capo_ecs.types.update_cluster_settings_request
    import capo_ecs.types.update_cluster_settings_response
    import capo_ecs.types.update_container_agent_request
    import capo_ecs.types.update_container_agent_response
    import capo_ecs.types.update_container_instances_state_request
    import capo_ecs.types.update_container_instances_state_response
    import capo_ecs.types.update_daemon_request
    import capo_ecs.types.update_daemon_response
    import capo_ecs.types.update_express_gateway_service_request
    import capo_ecs.types.update_express_gateway_service_response
    import capo_ecs.types.update_managed_instances_provider_configuration
    import capo_ecs.types.update_service_primary_task_set_request
    import capo_ecs.types.update_service_primary_task_set_response
    import capo_ecs.types.update_service_request
    import capo_ecs.types.update_service_response
    import capo_ecs.types.update_task_protection_request
    import capo_ecs.types.update_task_protection_response
    import capo_ecs.types.update_task_set_request
    import capo_ecs.types.update_task_set_response
    import capo_ecs.types.version_info
    import capo_ecs.types.volume_list
    import capo_ecs.types.vpc_lattice_configurations


class AsyncECSClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncECSClient:
    """A client for the ``ECS`` service.

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
        self._config = AsyncECSClientConfig(
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
        self.capacity_provider_resource = AsyncCapacityProviderResource(self)
        self.cluster_resource = AsyncClusterResource(self)
        self.container_instance_resource = AsyncContainerInstanceResource(self)
        self.daemon_deployment_resource = AsyncDaemonDeploymentResource(self)
        self.daemon_resource = AsyncDaemonResource(self)
        self.daemon_revision_resource = AsyncDaemonRevisionResource(self)
        self.daemon_task_definition_resource = AsyncDaemonTaskDefinitionResource(self)
        self.service_deployment_resource = AsyncServiceDeploymentResource(self)
        self.service_resource = AsyncServiceResource(self)
        self.service_revision_resource = AsyncServiceRevisionResource(self)
        self.task_definition_resource = AsyncTaskDefinitionResource(self)
        self.task_resource = AsyncTaskResource(self)
        self.task_set_resource = AsyncTaskSetResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncECSClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncECSClientConfig = config_overrides or {}
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

    async def continue_service_deployment(
        self,
        service_deployment_arn: "capo_ecs.types.string.String",
        hook_id: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        action: Optional[
            "capo_ecs.types.deployment_lifecycle_hook_action.DeploymentLifecycleHookAction"
        ] = None,
    ) -> "capo_ecs.types.continue_service_deployment_response.ContinueServiceDeploymentResponse":
        """<p>Continues or rolls back an Amazon ECS service deployment that is paused at a lifecycle hook.</p> <p>When a service deployment reaches a lifecycle stage that has a <code>PAUSE</code> hook configured, the deployment pauses and waits for an explicit action. Use this API to either continue the deployment to the next stage or roll back to the previous service revision.</p> <p>To find the <code>hookId</code> of the paused hook, call <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html">DescribeServiceDeployments</a> and inspect the <code>lifecycleHookDetails</code> field.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/continue-service-deployment.html">Continuing Amazon ECS service deployments</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            service_deployment_arn: <p>The ARN of the service deployment to continue or roll back.</p>
            hook_id: <p>The ID of the paused lifecycle hook to act on. You can find the <code>hookId</code> by calling <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html">DescribeServiceDeployments</a> and inspecting the <code>lifecycleHookDetails</code> field of the service deployment.</p>
            action: <p>The action to take on the paused lifecycle hook. Valid values are:</p> <ul> <li> <p> <code>CONTINUE</code> - Proceeds the deployment to the next lifecycle stage.</p> </li> <li> <p> <code>ROLLBACK</code> - Rolls back the deployment to the previous service revision.</p> </li> </ul> <p>If no value is specified, the default action is <code>CONTINUE</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_deployment_not_found_exception.ServiceDeploymentNotFoundException: <p>The service deploy ARN that you specified in the <code>ContinueServiceDeployment</code> doesn't exist. You can use <code>ListServiceDeployments</code> to retrieve the service deployment ARNs.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To continue a paused service deployment
            This example continues a service deployment that is paused at a lifecycle hook, using the CONTINUE action to proceed to the next deployment stage.

            >>> await client.continue_service_deployment(service_deployment_arn='arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r', hook_id='ecs-pause-Xk7rT2mP9sLwQn4vB8fYd3hJ6gA1cE5iO0uR_ZpWq', action='CONTINUE')
            To roll back a paused service deployment
            This example rolls back a service deployment that is paused at a lifecycle hook, using the ROLLBACK action to revert to the previous service revision.

            >>> await client.continue_service_deployment(service_deployment_arn='arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r', hook_id='ecs-pause-Xk7rT2mP9sLwQn4vB8fYd3hJ6gA1cE5iO0uR_ZpWq', action='ROLLBACK')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.continue_service_deployment_request.ContinueServiceDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.continue_service_deployment_response.ContinueServiceDeploymentResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.continue_service_deployment

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.continue_service_deployment.async_continue_service_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.continue_service_deployment_request.ContinueServiceDeploymentRequest = {
            "service_deployment_arn": service_deployment_arn,
            "hook_id": hook_id,
        }
        if action is not None:
            input_["action"] = action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_account_setting(
        self,
        name: "capo_ecs.types.setting_name.SettingName",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        principal_arn: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.delete_account_setting_response.DeleteAccountSettingResponse":
        """<p>Disables an account setting for a specified user, role, or the root user for an account.</p>

        Args:
            name: <p>The resource name to disable the account setting for. If <code>serviceLongArnFormat</code> is specified, the ARN for your Amazon ECS services is affected. If <code>taskLongArnFormat</code> is specified, the ARN and resource ID for your Amazon ECS tasks is affected. If <code>containerInstanceLongArnFormat</code> is specified, the ARN and resource ID for your Amazon ECS container instances is affected. If <code>awsvpcTrunking</code> is specified, the ENI limit for your Amazon ECS container instances is affected.</p>
            principal_arn: <p>The Amazon Resource Name (ARN) of the principal. It can be a user, role, or the root user. If you specify the root user, it disables the account setting for all users, roles, and the root user of the account unless a user or role explicitly overrides these settings. If this field is omitted, the setting is changed only for the authenticated user.</p> <p>In order to use this parameter, you must be the root user, or the principal.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete your account setting
            This example deletes the account setting for your user for the specified resource type.

            >>> await client.delete_account_setting(name='serviceLongArnFormat')
            To delete the account settings for a specific IAM user or IAM role
            This example deletes the account setting for a specific IAM user or IAM role for the specified resource type. Only the root user can view or modify the account settings for another user.

            >>> await client.delete_account_setting(name='containerInstanceLongArnFormat', principal_arn='arn:aws:iam::<aws_account_id>:user/principalName')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_account_setting_request.DeleteAccountSettingRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_account_setting_response.DeleteAccountSettingResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_account_setting

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_account_setting.async_delete_account_setting(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.delete_account_setting_request.DeleteAccountSettingRequest = {
            "name": name
        }
        if principal_arn is not None:
            input_["principal_arn"] = principal_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_task_definition(
        self,
        task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.deregister_task_definition_response.DeregisterTaskDefinitionResponse":
        """<p>Deregisters the specified task definition by family and revision. Upon deregistration, the task definition is marked as <code>INACTIVE</code>. Existing tasks and services that reference an <code>INACTIVE</code> task definition continue to run without disruption. Existing services that reference an <code>INACTIVE</code> task definition can still scale up or down by modifying the service's desired count. If you want to delete a task definition revision, you must first deregister the task definition revision.</p> <p>You can't use an <code>INACTIVE</code> task definition to run new tasks or create new services, and you can't update an existing service to reference an <code>INACTIVE</code> task definition. However, there may be up to a 10-minute window following deregistration where these restrictions have not yet taken effect.</p> <note> <p>At this time, <code>INACTIVE</code> task definitions remain discoverable in your account indefinitely. However, this behavior is subject to change in the future. We don't recommend that you rely on <code>INACTIVE</code> task definitions persisting beyond the lifecycle of any associated tasks and services.</p> </note> <p>You must deregister a task definition revision before you delete it. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteTaskDefinitions.html">DeleteTaskDefinitions</a>.</p>

        Args:
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a <code>revision</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To deregister a revision of a task definition
            This example deregisters the first revision of the fargate-task task definition

            >>> await client.deregister_task_definition(task_definition='fargate-task:1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.deregister_task_definition_request.DeregisterTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.deregister_task_definition_response.DeregisterTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.deregister_task_definition

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.deregister_task_definition.async_deregister_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.deregister_task_definition_request.DeregisterTaskDefinitionRequest = {
            "task_definition": task_definition
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_task_definition(
        self,
        task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        include: Optional[
            "capo_ecs.types.task_definition_field_list.TaskDefinitionFieldList"
        ] = None,
    ) -> "capo_ecs.types.describe_task_definition_response.DescribeTaskDefinitionResponse":
        """<p>Describes a task definition. You can specify a <code>family</code> and <code>revision</code> to find information about a specific task definition, or you can simply specify the family to find the latest <code>ACTIVE</code> revision in that family.</p> <note> <p>You can only describe <code>INACTIVE</code> task definitions while an active task or service references them.</p> </note>

        Args:
            task_definition: <p>The <code>family</code> for the latest <code>ACTIVE</code> revision, <code>family</code> and <code>revision</code> (<code>family:revision</code>) for a specific revision in the family, or full Amazon Resource Name (ARN) of the task definition to describe.</p>
            include: <p>Determines whether to see the resource tags for the task definition. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a task definition
            This example provides a description of the specified task definition.

            >>> await client.describe_task_definition(task_definition='hello_world:8')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_task_definition_request.DescribeTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_task_definition_response.DescribeTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_task_definition

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_task_definition.async_describe_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_task_definition_request.DescribeTaskDefinitionRequest = {
            "task_definition": task_definition
        }
        if include is not None:
            input_["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def discover_poll_endpoint(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        container_instance: Optional["capo_ecs.types.string.String"] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.discover_poll_endpoint_response.DiscoverPollEndpointResponse":
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Returns an endpoint for the Amazon ECS agent to poll for updates.</p>

        Args:
            container_instance: <p>The container instance ID or full ARN of the container instance. For more information about the ARN format, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that the container instance belongs to.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.discover_poll_endpoint_request.DiscoverPollEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.discover_poll_endpoint_response.DiscoverPollEndpointResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.discover_poll_endpoint

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.discover_poll_endpoint.async_discover_poll_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.discover_poll_endpoint_request.DiscoverPollEndpointRequest = {}
        if container_instance is not None:
            input_["container_instance"] = container_instance
        if cluster is not None:
            input_["cluster"] = cluster

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_account_settings(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        name: Optional["capo_ecs.types.setting_name.SettingName"] = None,
        value: Optional["capo_ecs.types.string.String"] = None,
        principal_arn: Optional["capo_ecs.types.string.String"] = None,
        effective_settings: Optional["capo_ecs.types.boolean.Boolean"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.integer.Integer"] = None,
    ) -> "capo_ecs.types.list_account_settings_response.ListAccountSettingsResponse":
        """<p>Lists the account settings for a specified principal.</p>

        Args:
            name: <p>The name of the account setting you want to list the settings for.</p>
            value: <p>The value of the account settings to filter results with. You must also specify an account setting name to use this parameter.</p>
            principal_arn: <p>The ARN of the principal, which can be a user, role, or the root user. If this field is omitted, the account settings are listed only for the authenticated user.</p> <p>In order to use this parameter, you must be the root user, or the principal.</p> <note> <p>Federated users assume the account setting of the root user and can't have explicit account settings set for them.</p> </note>
            effective_settings: <p>Determines whether to return the effective settings. If <code>true</code>, the account settings for the root user or the default setting for the <code>principalArn</code> are returned. If <code>false</code>, the account settings for the <code>principalArn</code> are returned if they're set. Otherwise, no account settings are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListAccountSettings</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of account setting results returned by <code>ListAccountSettings</code> in paginated output. When this parameter is used, <code>ListAccountSettings</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListAccountSettings</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 10. If this parameter isn't used, then <code>ListAccountSettings</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view your effective account settings
            This example displays the effective account settings for your account.

            >>> await client.list_account_settings(effective_settings=True)
            To view the effective account settings for a specific IAM user or IAM role
            This example displays the effective account settings for the specified user or role.

            >>> await client.list_account_settings(effective_settings=True, principal_arn='arn:aws:iam::<aws_account_id>:user/principalName')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_account_settings_request.ListAccountSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_account_settings_response.ListAccountSettingsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_account_settings

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_account_settings.async_list_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_account_settings_request.ListAccountSettingsRequest = {}
        if name is not None:
            input_["name"] = name
        if value is not None:
            input_["value"] = value
        if principal_arn is not None:
            input_["principal_arn"] = principal_arn
        if effective_settings is not None:
            input_["effective_settings"] = effective_settings
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

    async def iter_list_account_settings(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        name: Optional["capo_ecs.types.setting_name.SettingName"] = None,
        value: Optional["capo_ecs.types.string.String"] = None,
        principal_arn: Optional["capo_ecs.types.string.String"] = None,
        effective_settings: Optional["capo_ecs.types.boolean.Boolean"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.integer.Integer"] = None,
    ) -> "AsyncIterator[capo_ecs.types.setting.Setting]":
        _token = next_token
        while True:
            _response = await self.list_account_settings(
                config_overrides=config_overrides,
                name=name,
                value=value,
                principal_arn=principal_arn,
                effective_settings=effective_settings,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("settings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_services_by_namespace(
        self,
        namespace: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_services_by_namespace_response.ListServicesByNamespaceResponse":
        """<p>This operation lists all of the services that are associated with a Cloud Map namespace. This list might include services in different clusters. In contrast, <code>ListServices</code> can only list services in one cluster at a time. If you need to filter the list of services in a single cluster by various parameters, use <code>ListServices</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            namespace: <p>The namespace name or full Amazon Resource Name (ARN) of the Cloud Map namespace to list the services in.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            next_token: <p>The <code>nextToken</code> value that's returned from a <code>ListServicesByNamespace</code> request. It indicates that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> is returned, it is possible the number of results is less than <code>maxResults</code>.</p>
            max_results: <p>The maximum number of service results that <code>ListServicesByNamespace</code> returns in paginated output. When this parameter is used, <code>ListServicesByNamespace</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServicesByNamespace</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServicesByNamespace</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_services_by_namespace_request.ListServicesByNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_services_by_namespace_response.ListServicesByNamespaceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_services_by_namespace

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_services_by_namespace.async_list_services_by_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_services_by_namespace_request.ListServicesByNamespaceRequest = {
            "namespace": namespace
        }
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

    async def iter_list_services_by_namespace(
        self,
        namespace: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "AsyncIterator[capo_ecs.types.string.String]":
        _token = next_token
        while True:
            _response = await self.list_services_by_namespace(
                namespace,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("service_arns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List the tags for an Amazon ECS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon ECS tasks, services, task definitions, clusters, and container instances.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the tags for a cluster.
            This example lists the tags for the 'dev' cluster.

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:ecs:region:aws_account_id:cluster/dev')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_task_definition_families(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        family_prefix: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.task_definition_family_status.TaskDefinitionFamilyStatus"
        ] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_task_definition_families_response.ListTaskDefinitionFamiliesResponse":
        """<p>Returns a list of task definition families that are registered to your account. This list includes task definition families that no longer have any <code>ACTIVE</code> task definition revisions.</p> <p>You can filter out task definition families that don't contain any <code>ACTIVE</code> task definition revisions by setting the <code>status</code> parameter to <code>ACTIVE</code>. You can also filter the results with the <code>familyPrefix</code> parameter.</p>

        Args:
            family_prefix: <p>The <code>familyPrefix</code> is a string that's used to filter the results of <code>ListTaskDefinitionFamilies</code>. If you specify a <code>familyPrefix</code>, only task definition family names that begin with the <code>familyPrefix</code> string are returned.</p>
            status: <p>The task definition family status to filter the <code>ListTaskDefinitionFamilies</code> results with. By default, both <code>ACTIVE</code> and <code>INACTIVE</code> task definition families are listed. If this parameter is set to <code>ACTIVE</code>, only task definition families that have an <code>ACTIVE</code> task definition revision are returned. If this parameter is set to <code>INACTIVE</code>, only task definition families that do not have any <code>ACTIVE</code> task definition revisions are returned. If you paginate the resulting output, be sure to keep the <code>status</code> value constant in each subsequent request.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListTaskDefinitionFamilies</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it is possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of task definition family results that <code>ListTaskDefinitionFamilies</code> returned in paginated output. When this parameter is used, <code>ListTaskDefinitions</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListTaskDefinitionFamilies</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListTaskDefinitionFamilies</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your registered task definition families
            This example lists all of your registered task definition families.

            >>> await client.list_task_definition_families()
            To filter your registered task definition families
            This example lists the task definition revisions that start with "hpcc".

            >>> await client.list_task_definition_families(family_prefix='hpcc')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_task_definition_families_request.ListTaskDefinitionFamiliesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_task_definition_families_response.ListTaskDefinitionFamiliesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_task_definition_families

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_task_definition_families.async_list_task_definition_families(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_task_definition_families_request.ListTaskDefinitionFamiliesRequest = {}
        if family_prefix is not None:
            input_["family_prefix"] = family_prefix
        if status is not None:
            input_["status"] = status
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

    async def iter_list_task_definition_families(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        family_prefix: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.task_definition_family_status.TaskDefinitionFamilyStatus"
        ] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "AsyncIterator[capo_ecs.types.string.String]":
        _token = next_token
        while True:
            _response = await self.list_task_definition_families(
                config_overrides=config_overrides,
                family_prefix=family_prefix,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("families",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_account_setting(
        self,
        name: "capo_ecs.types.setting_name.SettingName",
        value: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        principal_arn: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.put_account_setting_response.PutAccountSettingResponse":
        """<p>Modifies an account setting. Account settings are set on a per-Region basis.</p> <p>If you change the root user account setting, the default settings are reset for users and roles that do not have specified individual account settings. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html">Account Settings</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            name: <p>The Amazon ECS account setting name to modify.</p> <p>The following are the valid values for the account setting name.</p> <ul> <li> <p> <code>serviceLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>taskLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>containerInstanceLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>awsvpcTrunking</code> - When modified, the elastic network interface (ENI) limit for any new container instances that support the feature is changed. If <code>awsvpcTrunking</code> is turned on, any new container instances that support the feature are launched have the increased ENI limits available to them. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-eni.html">Elastic Network Interface Trunking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>containerInsights</code> - Container Insights with enhanced observability provides all the Container Insights metrics, plus additional task and container metrics. This version supports enhanced observability for Amazon ECS clusters using the Amazon EC2 and Fargate launch types. After you configure Container Insights with enhanced observability on Amazon ECS, Container Insights auto-collects detailed infrastructure telemetry from the cluster level down to the container level in your environment and displays these critical performance data in curated dashboards removing the heavy lifting in observability set-up. </p> <p>To use Container Insights with enhanced observability, set the <code>containerInsights</code> account setting to <code>enhanced</code>.</p> <p>To use Container Insights, set the <code>containerInsights</code> account setting to <code>enabled</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html">Monitor Amazon ECS containers using Container Insights with enhanced observability</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>dualStackIPv6</code> - When turned on, when using a VPC in dual stack mode, your tasks using the <code>awsvpc</code> network mode can have an IPv6 address assigned. For more information on using IPv6 with tasks launched on Amazon EC2 instances, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html#task-networking-vpc-dual-stack">Using a VPC in dual-stack mode</a>. For more information on using IPv6 with tasks launched on Fargate, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html#fargate-task-networking-vpc-dual-stack">Using a VPC in dual-stack mode</a>.</p> </li> <li> <p> <code>fargateTaskRetirementWaitPeriod</code> - When Amazon Web Services determines that a security or infrastructure update is needed for an Amazon ECS task hosted on Fargate, the tasks need to be stopped and new tasks launched to replace them. Use <code>fargateTaskRetirementWaitPeriod</code> to configure the wait time to retire a Fargate task. For information about the Fargate tasks maintenance, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-maintenance.html">Amazon Web Services Fargate task maintenance</a> in the <i>Amazon ECS Developer Guide</i>.</p> </li> <li> <p> <code>fargateEventWindows</code> - When Amazon Web Services determines that a security or infrastructure update is needed for an Amazon ECS task hosted on Fargate, the tasks need to be stopped and new tasks launched to replace them. Use <code>fargateEventWindows</code> to use EC2 Event Windows associated with Fargate tasks to configure time windows for task retirement.</p> </li> <li> <p> <code>tagResourceAuthorization</code> - Amazon ECS is introducing tagging authorization for resource creation. Users must have permissions for actions that create the resource, such as <code>ecsCreateCluster</code>. If tags are specified when you create a resource, Amazon Web Services performs additional authorization to verify if users or roles have permissions to create tags. Therefore, you must grant explicit permissions to use the <code>ecs:TagResource</code> action. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/supported-iam-actions-tagging.html">Grant permission to tag resources on creation</a> in the <i>Amazon ECS Developer Guide</i>.</p> </li> <li> <p> <code>defaultLogDriverMode</code> - Amazon ECS supports setting a default delivery mode of log messages from a container to the <code>logDriver</code> that you specify in the container's <code>logConfiguration</code>. The delivery mode affects application stability when the flow of logs from the container to the log driver is interrupted. The <code>defaultLogDriverMode</code> setting supports two values: <code>blocking</code> and <code>non-blocking</code>. If you don't specify a delivery mode in your container definition's <code>logConfiguration</code>, the mode you specify using this account setting will be used as the default. For more information about log delivery modes, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_LogConfiguration.html">LogConfiguration</a>. </p> <note> <p>On June 25, 2025, Amazon ECS changed the default log driver mode from <code>blocking</code> to <code>non-blocking</code> to prioritize task availability over logging. To continue using the <code>blocking</code> mode after this change, do one of the following:</p> <ul> <li> <p>Set the <code>mode</code> option in your container definition's <code>logConfiguration</code> as <code>blocking</code>.</p> </li> <li> <p>Set the <code>defaultLogDriverMode</code> account setting to <code>blocking</code>.</p> </li> </ul> </note> </li> <li> <p> <code>guardDutyActivate</code> - The <code>guardDutyActivate</code> parameter is read-only in Amazon ECS and indicates whether Amazon ECS Runtime Monitoring is enabled or disabled by your security administrator in your Amazon ECS account. Amazon GuardDuty controls this account setting on your behalf. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-integration.html">Protecting Amazon ECS workloads with Amazon ECS Runtime Monitoring</a>.</p> </li> </ul>
            value: <p>The account setting value for the specified principal ARN. Accepted values are <code>enabled</code>, <code>disabled</code>, <code>enhanced</code>, <code>on</code>, and <code>off</code>.</p> <p>When you specify <code>fargateTaskRetirementWaitPeriod</code> for the <code>name</code>, the following are the valid values:</p> <ul> <li> <p> <code>0</code> - Amazon Web Services sends the notification, and immediately retires the affected tasks.</p> </li> <li> <p> <code>7</code> - Amazon Web Services sends the notification, and waits 7 calendar days to retire the tasks.</p> </li> <li> <p> <code>14</code> - Amazon Web Services sends the notification, and waits 14 calendar days to retire the tasks.</p> </li> </ul>
            principal_arn: <p>The ARN of the principal, which can be a user, role, or the root user. If you specify the root user, it modifies the account setting for all users, roles, and the root user of the account unless a user or role explicitly overrides these settings. If this field is omitted, the setting is changed only for the authenticated user.</p> <p>In order to use this parameter, you must be the root user, or the principal.</p> <note> <p>You must use the root user when you set the Fargate wait time (<code>fargateTaskRetirementWaitPeriod</code>). </p> <p>Federated users assume the account setting of the root user and can't have explicit account settings set for them.</p> </note>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To modify your account settings
            This example modifies your account settings to opt in to the new ARN and resource ID format for Amazon ECS services. If you’re using this command as the root user, then changes apply to the entire AWS account, unless an IAM user or role explicitly overrides these settings for themselves.

            >>> await client.put_account_setting(name='serviceLongArnFormat', value='enabled')
            To modify the account settings for a specific IAM user or IAM role
            This example modifies the account setting for a specific IAM user or IAM role to opt in to the new ARN and resource ID format for Amazon ECS container instances. If you’re using this command as the root user, then changes apply to the entire AWS account, unless an IAM user or role explicitly overrides these settings for themselves.

            >>> await client.put_account_setting(name='containerInstanceLongArnFormat', value='enabled', principal_arn='arn:aws:iam::<aws_account_id>:user/principalName')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.put_account_setting_request.PutAccountSettingRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.put_account_setting_response.PutAccountSettingResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.put_account_setting

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.put_account_setting.async_put_account_setting(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.put_account_setting_request.PutAccountSettingRequest = {
            "name": name,
            "value": value,
        }
        if principal_arn is not None:
            input_["principal_arn"] = principal_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_setting_default(
        self,
        name: "capo_ecs.types.setting_name.SettingName",
        value: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.put_account_setting_default_response.PutAccountSettingDefaultResponse":
        """<p>Modifies an account setting for all users on an account for whom no individual account setting has been specified. Account settings are set on a per-Region basis.</p>

        Args:
            name: <p>The resource name for which to modify the account setting.</p> <p>The following are the valid values for the account setting name.</p> <ul> <li> <p> <code>serviceLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>taskLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>containerInstanceLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>awsvpcTrunking</code> - When modified, the elastic network interface (ENI) limit for any new container instances that support the feature is changed. If <code>awsvpcTrunking</code> is turned on, any new container instances that support the feature are launched have the increased ENI limits available to them. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-eni.html">Elastic Network Interface Trunking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>containerInsights</code> - Container Insights with enhanced observability provides all the Container Insights metrics, plus additional task and container metrics. This version supports enhanced observability for Amazon ECS clusters using the Amazon EC2 and Fargate launch types. After you configure Container Insights with enhanced observability on Amazon ECS, Container Insights auto-collects detailed infrastructure telemetry from the cluster level down to the container level in your environment and displays these critical performance data in curated dashboards removing the heavy lifting in observability set-up. </p> <p>To use Container Insights with enhanced observability, set the <code>containerInsights</code> account setting to <code>enhanced</code>.</p> <p>To use Container Insights, set the <code>containerInsights</code> account setting to <code>enabled</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html">Monitor Amazon ECS containers using Container Insights with enhanced observability</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>dualStackIPv6</code> - When turned on, when using a VPC in dual stack mode, your tasks using the <code>awsvpc</code> network mode can have an IPv6 address assigned. For more information on using IPv6 with tasks launched on Amazon EC2 instances, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html#task-networking-vpc-dual-stack">Using a VPC in dual-stack mode</a>. For more information on using IPv6 with tasks launched on Fargate, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html#fargate-task-networking-vpc-dual-stack">Using a VPC in dual-stack mode</a>.</p> </li> <li> <p> <code>fargateFIPSMode</code> - If you specify <code>fargateFIPSMode</code>, Fargate FIPS 140 compliance is affected.</p> </li> <li> <p> <code>fargateTaskRetirementWaitPeriod</code> - When Amazon Web Services determines that a security or infrastructure update is needed for an Amazon ECS task hosted on Fargate, the tasks need to be stopped and new tasks launched to replace them. Use <code>fargateTaskRetirementWaitPeriod</code> to configure the wait time to retire a Fargate task. For information about the Fargate tasks maintenance, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-maintenance.html">Amazon Web Services Fargate task maintenance</a> in the <i>Amazon ECS Developer Guide</i>.</p> </li> <li> <p> <code>fargateEventWindows</code> - When Amazon Web Services determines that a security or infrastructure update is needed for an Amazon ECS task hosted on Fargate, the tasks need to be stopped and new tasks launched to replace them. Use <code>fargateEventWindows</code> to use EC2 Event Windows associated with Fargate tasks to configure time windows for task retirement.</p> </li> <li> <p> <code>tagResourceAuthorization</code> - Amazon ECS is introducing tagging authorization for resource creation. Users must have permissions for actions that create the resource, such as <code>ecsCreateCluster</code>. If tags are specified when you create a resource, Amazon Web Services performs additional authorization to verify if users or roles have permissions to create tags. Therefore, you must grant explicit permissions to use the <code>ecs:TagResource</code> action. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/supported-iam-actions-tagging.html">Grant permission to tag resources on creation</a> in the <i>Amazon ECS Developer Guide</i>.</p> </li> <li> <p> <code>defaultLogDriverMode</code> -Amazon ECS supports setting a default delivery mode of log messages from a container to the <code>logDriver</code> that you specify in the container's <code>logConfiguration</code>. The delivery mode affects application stability when the flow of logs from the container to the log driver is interrupted. The <code>defaultLogDriverMode</code> setting supports two values: <code>blocking</code> and <code>non-blocking</code>. If you don't specify a delivery mode in your container definition's <code>logConfiguration</code>, the mode you specify using this account setting will be used as the default. For more information about log delivery modes, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_LogConfiguration.html">LogConfiguration</a>.</p> <note> <p>On June 25, 2025, Amazon ECS changed the default log driver mode from <code>blocking</code> to <code>non-blocking</code> to prioritize task availability over logging. To continue using the <code>blocking</code> mode after this change, do one of the following:</p> <ul> <li> <p>Set the <code>mode</code> option in your container definition's <code>logConfiguration</code> as <code>blocking</code>.</p> </li> <li> <p>Set the <code>defaultLogDriverMode</code> account setting to <code>blocking</code>.</p> </li> </ul> </note> </li> <li> <p> <code>guardDutyActivate</code> - The <code>guardDutyActivate</code> parameter is read-only in Amazon ECS and indicates whether Amazon ECS Runtime Monitoring is enabled or disabled by your security administrator in your Amazon ECS account. Amazon GuardDuty controls this account setting on your behalf. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-integration.html">Protecting Amazon ECS workloads with Amazon ECS Runtime Monitoring</a>.</p> </li> </ul>
            value: <p>The account setting value for the specified principal ARN. Accepted values are <code>enabled</code>, <code>disabled</code>, <code>on</code>, <code>enhanced</code>, and <code>off</code>.</p> <p>When you specify <code>fargateTaskRetirementWaitPeriod</code> for the <code>name</code>, the following are the valid values:</p> <ul> <li> <p> <code>0</code> - Amazon Web Services sends the notification, and immediately retires the affected tasks.</p> </li> <li> <p> <code>7</code> - Amazon Web Services sends the notification, and waits 7 calendar days to retire the tasks.</p> </li> <li> <p> <code>14</code> - Amazon Web Services sends the notification, and waits 14 calendar days to retire the tasks.</p> </li> </ul>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To modify the default account settings for all IAM users or roles on an account
            This example modifies the default account setting for the specified resource for all IAM users or roles on an account. These changes apply to the entire AWS account, unless an IAM user or role explicitly overrides these settings for themselves.

            >>> await client.put_account_setting_default(name='serviceLongArnFormat', value='enabled')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.put_account_setting_default_request.PutAccountSettingDefaultRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.put_account_setting_default_response.PutAccountSettingDefaultResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.put_account_setting_default

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.put_account_setting_default.async_put_account_setting_default(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.put_account_setting_default_request.PutAccountSettingDefaultRequest = {
            "name": name,
            "value": value,
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
        resource_arn: "capo_ecs.types.string.String",
        tags: "capo_ecs.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.tag_resource_response.TagResourceResponse":
        """<p>Associates the specified tags to a resource with the specified <code>resourceArn</code>. If existing tags on a resource aren't specified in the request parameters, they aren't changed. When a resource is deleted, the tags that are associated with that resource are deleted as well.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to add tags to. Currently, the supported resources are Amazon ECS capacity providers, tasks, services, task definitions, clusters, and container instances.</p> <p>In order to tag a service that has the following ARN format, you need to migrate the service to the long ARN. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-arn-migration.html">Migrate an Amazon ECS short service ARN to a long ARN</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p> <code>arn:aws:ecs:region:aws_account_id:service/service-name</code> </p> <p>After the migration is complete, the service has the long ARN format, as shown below. Use this ARN to tag the service.</p> <p> <code>arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name</code> </p> <p>If you try to tag a service with a short ARN, you receive an <code>InvalidParameterException</code> error.</p>
            tags: <p>The tags to add to the resource. A tag is an array of key-value pairs.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To tag a cluster.
            This example tags the 'dev' cluster with key 'team' and value 'dev'.

            >>> await client.tag_resource(resource_arn='arn:aws:ecs:region:aws_account_id:cluster/dev', tags=[{'key': 'team', 'value': 'dev'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.tag_resource

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_ecs.types.string.String",
        tag_keys: "capo_ecs.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to delete tags from. Currently, the supported resources are Amazon ECS capacity providers, tasks, services, task definitions, clusters, and container instances.</p>
            tag_keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To untag a cluster.
            This example deletes the 'team' tag from the 'dev' cluster.

            >>> await client.untag_resource(resource_arn='arn:aws:ecs:region:aws_account_id:cluster/dev', tag_keys=['team'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.untag_resource

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_capacity_provider(
        self,
        name: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        auto_scaling_group_provider: Optional[
            "capo_ecs.types.auto_scaling_group_provider.AutoScalingGroupProvider"
        ] = None,
        managed_instances_provider: Optional[
            "capo_ecs.types.create_managed_instances_provider_configuration.CreateManagedInstancesProviderConfiguration"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
    ) -> "capo_ecs.types.create_capacity_provider_response.CreateCapacityProviderResponse":
        """<p>Creates a capacity provider. Capacity providers are associated with a cluster and are used in capacity provider strategies to facilitate cluster auto scaling. You can create capacity providers for Amazon ECS Managed Instances and EC2 instances. Fargate has the predefined <code>FARGATE</code> and <code>FARGATE_SPOT</code> capacity providers.</p>

        Args:
            name: <p>The name of the capacity provider. Up to 255 characters are allowed. They include letters (both upper and lowercase letters), numbers, underscores (_), and hyphens (-). The name can't be prefixed with "<code>aws</code>", "<code>ecs</code>", or "<code>fargate</code>".</p>
            cluster: <p>The name of the cluster to associate with the capacity provider. When you create a capacity provider with Amazon ECS Managed Instances, it becomes available only within the specified cluster.</p>
            auto_scaling_group_provider: <p>The details of the Auto Scaling group for the capacity provider.</p>
            managed_instances_provider: <p>The configuration for the Amazon ECS Managed Instances provider. This configuration specifies how Amazon ECS manages Amazon EC2 instances on your behalf, including the infrastructure role, instance launch template, and tag propagation settings.</p>
            tags: <p>The metadata that you apply to the capacity provider to categorize and organize them more conveniently. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a capacity provider
            This example creates a capacity provider that uses the specified Auto Scaling group MyASG and has managed scaling and manager termination protection enabled.

            >>> await client.create_capacity_provider(name='MyCapacityProvider', auto_scaling_group_provider={'autoScalingGroupArn': 'arn:aws:autoscaling:us-east-1:123456789012:autoScalingGroup:57ffcb94-11f0-4d6d-bf60-3bac5EXAMPLE:autoScalingGroupName/MyASG', 'managedScaling': {'status': 'ENABLED', 'targetCapacity': 100}, 'managedTerminationProtection': 'ENABLED'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.create_capacity_provider_request.CreateCapacityProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.create_capacity_provider_response.CreateCapacityProviderResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_capacity_provider

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.create_capacity_provider.async_create_capacity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.create_capacity_provider_request.CreateCapacityProviderRequest = {
            "name": name
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if auto_scaling_group_provider is not None:
            input_["auto_scaling_group_provider"] = auto_scaling_group_provider
        if managed_instances_provider is not None:
            input_["managed_instances_provider"] = managed_instances_provider
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_capacity_provider(
        self,
        name: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        auto_scaling_group_provider: Optional[
            "capo_ecs.types.auto_scaling_group_provider_update.AutoScalingGroupProviderUpdate"
        ] = None,
        managed_instances_provider: Optional[
            "capo_ecs.types.update_managed_instances_provider_configuration.UpdateManagedInstancesProviderConfiguration"
        ] = None,
    ) -> "capo_ecs.types.update_capacity_provider_response.UpdateCapacityProviderResponse":
        """<p>Modifies the parameters for a capacity provider.</p> <p>These changes only apply to new Amazon ECS Managed Instances, or EC2 instances, not existing ones.</p>

        Args:
            name: <p>The name of the capacity provider to update.</p>
            cluster: <p>The name of the cluster that contains the capacity provider to update. Managed instances capacity providers are cluster-scoped and can only be updated within their associated cluster.</p>
            auto_scaling_group_provider: <p>An object that represent the parameters to update for the Auto Scaling group capacity provider.</p>
            managed_instances_provider: <p>The updated configuration for the Amazon ECS Managed Instances provider. You can modify the infrastructure role, instance launch template, and tag propagation settings. Changes take effect for new instances launched after the update.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a capacity provider's parameters
            This example updates the targetCapacity and instanceWarmupPeriod parameters for the capacity provider MyCapacityProvider to 90 and 150 respectively.

            >>> await client.update_capacity_provider(name='MyCapacityProvider', auto_scaling_group_provider={'managedScaling': {'status': 'ENABLED', 'targetCapacity': 90, 'instanceWarmupPeriod': 150}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_capacity_provider_request.UpdateCapacityProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_capacity_provider_response.UpdateCapacityProviderResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_capacity_provider

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_capacity_provider.async_update_capacity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.update_capacity_provider_request.UpdateCapacityProviderRequest = {
            "name": name
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if auto_scaling_group_provider is not None:
            input_["auto_scaling_group_provider"] = auto_scaling_group_provider
        if managed_instances_provider is not None:
            input_["managed_instances_provider"] = managed_instances_provider

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_capacity_provider(
        self,
        capacity_provider: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.delete_capacity_provider_response.DeleteCapacityProviderResponse":
        """<p>Deletes the specified capacity provider.</p> <note> <p>The <code>FARGATE</code> and <code>FARGATE_SPOT</code> capacity providers are reserved and can't be deleted. You can disassociate them from a cluster using either <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> or by deleting the cluster.</p> </note> <p>Prior to a capacity provider being deleted, the capacity provider must be removed from the capacity provider strategy from all services. The <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a> API can be used to remove a capacity provider from a service's capacity provider strategy. When updating a service, the <code>forceNewDeployment</code> option can be used to ensure that any tasks using the Amazon EC2 instance capacity provided by the capacity provider are transitioned to use the capacity from the remaining capacity providers. Only capacity providers that aren't associated with a cluster can be deleted. To remove a capacity provider from a cluster, you can either use <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> or delete the cluster.</p>

        Args:
            capacity_provider: <p>The short name or full Amazon Resource Name (ARN) of the capacity provider to delete.</p>
            cluster: <p>The name of the cluster that contains the capacity provider to delete. Managed instances capacity providers are cluster-scoped and can only be deleted from their associated cluster.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a specified capacity provider
            This example deletes a specified capacity provider.

            >>> await client.delete_capacity_provider(capacity_provider='arn:aws:ecs:us-west-2:123456789012:capacity-provider/ExampleCapacityProvider')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_capacity_provider_request.DeleteCapacityProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_capacity_provider_response.DeleteCapacityProviderResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_capacity_provider

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_capacity_provider.async_delete_capacity_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.delete_capacity_provider_request.DeleteCapacityProviderRequest = {
            "capacity_provider": capacity_provider
        }
        if cluster is not None:
            input_["cluster"] = cluster

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_capacity_providers(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        capacity_providers: Optional["capo_ecs.types.string_list.StringList"] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        include: Optional[
            "capo_ecs.types.capacity_provider_field_list.CapacityProviderFieldList"
        ] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.describe_capacity_providers_response.DescribeCapacityProvidersResponse":
        """<p>Describes one or more of your capacity providers.</p>

        Args:
            capacity_providers: <p>The short name or full Amazon Resource Name (ARN) of one or more capacity providers. Up to <code>100</code> capacity providers can be described in an action.</p>
            cluster: <p>The name of the cluster to describe capacity providers for. When specified, only capacity providers associated with this cluster are returned, including Amazon ECS Managed Instances capacity providers.</p>
            include: <p>Specifies whether or not you want to see the resource tags for the capacity provider. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>
            max_results: <p>The maximum number of account setting results returned by <code>DescribeCapacityProviders</code> in paginated output. When this parameter is used, <code>DescribeCapacityProviders</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeCapacityProviders</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 10. If this parameter is not used, then <code>DescribeCapacityProviders</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeCapacityProviders</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe all capacity providers
            This example retrieves details about all capacity providers.

            >>> await client.describe_capacity_providers()
            To describe a specific capacity provider
            This example retrieves details about the capacity provider MyCapacityProvider

            >>> await client.describe_capacity_providers(capacity_providers=['MyCapacityProvider'], include=['TAGS'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_capacity_providers_request.DescribeCapacityProvidersRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_capacity_providers_response.DescribeCapacityProvidersResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_capacity_providers

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_capacity_providers.async_describe_capacity_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_capacity_providers_request.DescribeCapacityProvidersRequest = {}
        if capacity_providers is not None:
            input_["capacity_providers"] = capacity_providers
        if cluster is not None:
            input_["cluster"] = cluster
        if include is not None:
            input_["include"] = include
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

    async def update_cluster(
        self,
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        settings: Optional["capo_ecs.types.cluster_settings.ClusterSettings"] = None,
        configuration: Optional[
            "capo_ecs.types.cluster_configuration.ClusterConfiguration"
        ] = None,
        service_connect_defaults: Optional[
            "capo_ecs.types.cluster_service_connect_defaults_request.ClusterServiceConnectDefaultsRequest"
        ] = None,
    ) -> "capo_ecs.types.update_cluster_response.UpdateClusterResponse":
        """<p>Updates the cluster.</p>

        Args:
            cluster: <p>The name of the cluster to modify the settings for.</p>
            settings: <p>The cluster settings for your cluster.</p>
            configuration: <p>The execute command configuration for the cluster.</p>
            service_connect_defaults: <p>Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the <code>enabled</code> parameter to <code>true</code> in the <code>ServiceConnectConfiguration</code>. You can set the namespace of each service individually in the <code>ServiceConnectConfiguration</code> to override this default parameter.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a cluster's observability settings.
            This example turns on enhanced containerInsights in an existing cluster.

            >>> await client.update_cluster(cluster='ECS-project-update-cluster', settings=[{'name': 'containerInsights', 'value': 'enhanced'}])
            To update a cluster's Service Connect defaults.
            This example sets a default Service Connect namespace.

            >>> await client.update_cluster(cluster='ECS-project-update-cluster', service_connect_defaults={'namespace': 'test'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_cluster_request.UpdateClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster.async_update_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.update_cluster_request.UpdateClusterRequest = {
            "cluster": cluster
        }
        if settings is not None:
            input_["settings"] = settings
        if configuration is not None:
            input_["configuration"] = configuration
        if service_connect_defaults is not None:
            input_["service_connect_defaults"] = service_connect_defaults

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cluster(
        self,
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes the specified cluster. The cluster transitions to the <code>INACTIVE</code> state. Clusters with an <code>INACTIVE</code> status might remain discoverable in your account for a period of time. However, this behavior is subject to change in the future. We don't recommend that you rely on <code>INACTIVE</code> clusters persisting.</p> <p>You must deregister all container instances from this cluster before you may delete it. You can list the container instances in a cluster with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListContainerInstances.html">ListContainerInstances</a> and deregister them with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterContainerInstance.html">DeregisterContainerInstance</a>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to delete.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_contains_capacity_provider_exception.ClusterContainsCapacityProviderException: <p>The cluster contains one or more capacity providers that prevent the requested operation. This exception occurs when you try to delete a cluster that still has active capacity providers, including Amazon ECS Managed Instances capacity providers. You must first delete all capacity providers from the cluster before you can delete the cluster itself.</p>
            capo_ecs.errors.cluster_contains_container_instances_exception.ClusterContainsContainerInstancesException: <p>You can't delete a cluster that has registered container instances. First, deregister the container instances before you can delete the cluster. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterContainerInstance.html">DeregisterContainerInstance</a>.</p>
            capo_ecs.errors.cluster_contains_services_exception.ClusterContainsServicesException: <p>You can't delete a cluster that contains services. First, update the service to reduce its desired task count to 0, and then delete the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a> and <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteService.html">DeleteService</a>.</p>
            capo_ecs.errors.cluster_contains_tasks_exception.ClusterContainsTasksException: <p>You can't delete a cluster that has active tasks.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an empty cluster
            This example deletes an empty cluster in your default region.

            >>> await client.delete_cluster(cluster='my_cluster')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_cluster

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.delete_cluster_request.DeleteClusterRequest = {
            "cluster": cluster
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_cluster_capacity_providers(
        self,
        cluster: "capo_ecs.types.string.String",
        capacity_providers: "capo_ecs.types.string_list.StringList",
        default_capacity_provider_strategy: "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.put_cluster_capacity_providers_response.PutClusterCapacityProvidersResponse":
        """<p>Modifies the available capacity providers and the default capacity provider strategy for a cluster.</p> <p>You must specify both the available capacity providers and a default capacity provider strategy for the cluster. If the specified cluster has existing capacity providers associated with it, you must specify all existing capacity providers in addition to any new ones you want to add. Any existing capacity providers that are associated with a cluster that are omitted from a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API call will be disassociated with the cluster. You can only disassociate an existing capacity provider from a cluster if it's not being used by any existing tasks.</p> <p>When creating a service or running a task on a cluster, if no capacity provider or launch type is specified, then the cluster's default capacity provider strategy is used. We recommend that you define a default capacity provider strategy for your cluster. However, you must specify an empty array (<code>[]</code>) to bypass defining a default strategy.</p> <p>Amazon ECS Managed Instances doesn't support this, because when you create a capacity provider with Amazon ECS Managed Instances, it becomes available only within the specified cluster.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to modify the capacity provider settings for. If you don't specify a cluster, the default cluster is assumed.</p>
            capacity_providers: <p>The name of one or more capacity providers to associate with the cluster.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p>
            default_capacity_provider_strategy: <p>The capacity provider strategy to use by default for the cluster.</p> <p>When creating a service or running a task on a cluster, if no capacity provider or launch type is specified then the default capacity provider strategy for the cluster is used.</p> <p>A capacity provider strategy consists of one or more capacity providers along with the <code>base</code> and <code>weight</code> to assign to them. A capacity provider must be associated with the cluster to be used in a capacity provider strategy. The <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API is used to associate a capacity provider with a cluster. Only capacity providers with an <code>ACTIVE</code> or <code>UPDATING</code> status can be used.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in-use and can't be removed.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add an existing capacity provider to a cluuster
            This example adds an existing capacity provider "MyCapacityProvider2" to a cluster that already has the capacity provider "MyCapacityProvider1" associated with it. Both "MyCapacityProvider2" and "MyCapacityProvider1" need to be specified.

            >>> await client.put_cluster_capacity_providers(cluster='MyCluster', capacity_providers=['MyCapacityProvider1', 'MyCapacityProvider2'], default_capacity_provider_strategy=[{'capacityProvider': 'MyCapacityProvider1', 'weight': 1}, {'capacityProvider': 'MyCapacityProvider2', 'weight': 1}])
            To remove a capacity provider from a cluster
            This example removes a capacity provider "MyCapacityProvider2" from a cluster that has both "MyCapacityProvider2" and "MyCapacityProvider1" associated with it. Only "MyCapacityProvider1" needs to be specified in this scenario.

            >>> await client.put_cluster_capacity_providers(cluster='MyCluster', capacity_providers=['MyCapacityProvider1'], default_capacity_provider_strategy=[{'capacityProvider': 'MyCapacityProvider1', 'weight': 1, 'base': 0}])
            To remove all capacity providers from a cluster
            This example removes all capacity providers associated with a cluster.

            >>> await client.put_cluster_capacity_providers(cluster='MyCluster', capacity_providers=[], default_capacity_provider_strategy=[])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.put_cluster_capacity_providers_request.PutClusterCapacityProvidersRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.put_cluster_capacity_providers_response.PutClusterCapacityProvidersResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.put_cluster_capacity_providers

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.put_cluster_capacity_providers.async_put_cluster_capacity_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.put_cluster_capacity_providers_request.PutClusterCapacityProvidersRequest = {
            "cluster": cluster,
            "capacity_providers": capacity_providers,
            "default_capacity_provider_strategy": default_capacity_provider_strategy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_cluster_settings(
        self,
        cluster: "capo_ecs.types.string.String",
        settings: "capo_ecs.types.cluster_settings.ClusterSettings",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> (
        "capo_ecs.types.update_cluster_settings_response.UpdateClusterSettingsResponse"
    ):
        """<p>Modifies the settings to use for a cluster.</p>

        Args:
            cluster: <p>The name of the cluster to modify the settings for.</p>
            settings: <p>The setting to use by default for a cluster. This parameter is used to turn on CloudWatch Container Insights for a cluster. If this value is specified, it overrides the <code>containerInsights</code> value set with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html">PutAccountSetting</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html">PutAccountSettingDefault</a>.</p> <important> <p>Currently, if you delete an existing cluster that does not have Container Insights turned on, and then create a new cluster with the same name with Container Insights tuned on, Container Insights will not actually be turned on. If you want to preserve the same name for your existing cluster and turn on Container Insights, you must wait 7 days before you can re-create it.</p> </important>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a cluster's settings
            This example enables CloudWatch Container Insights for the default cluster.

            >>> await client.update_cluster_settings(cluster='default', settings=[{'name': 'containerInsights', 'value': 'enabled'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_cluster_settings_request.UpdateClusterSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_cluster_settings_response.UpdateClusterSettingsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster_settings

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster_settings.async_update_cluster_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.update_cluster_settings_request.UpdateClusterSettingsRequest = {
            "cluster": cluster,
            "settings": settings,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cluster(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster_name: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        settings: Optional["capo_ecs.types.cluster_settings.ClusterSettings"] = None,
        configuration: Optional[
            "capo_ecs.types.cluster_configuration.ClusterConfiguration"
        ] = None,
        capacity_providers: Optional["capo_ecs.types.string_list.StringList"] = None,
        default_capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        service_connect_defaults: Optional[
            "capo_ecs.types.cluster_service_connect_defaults_request.ClusterServiceConnectDefaultsRequest"
        ] = None,
    ) -> "capo_ecs.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates a new Amazon ECS cluster. By default, your account receives a <code>default</code> cluster when you launch your first container instance. However, you can create your own cluster with a unique name.</p> <note> <p>When you call the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCluster.html">CreateCluster</a> API operation, Amazon ECS attempts to create the Amazon ECS service-linked role for your account. This is so that it can manage required resources in other Amazon Web Services services on your behalf. However, if the user that makes the call doesn't have permissions to create the service-linked role, it isn't created. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>

        Args:
            cluster_name: <p>The name of your cluster. If you don't specify a name for your cluster, you create a cluster that's named <code>default</code>. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. </p>
            tags: <p>The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            settings: <p>The setting to use when creating a cluster. This parameter is used to turn on CloudWatch Container Insights for a cluster. If this value is specified, it overrides the <code>containerInsights</code> value set with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html">PutAccountSetting</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html">PutAccountSettingDefault</a>.</p>
            configuration: <p>The <code>execute</code> command configuration for the cluster.</p>
            capacity_providers: <p>The short name of one or more capacity providers to associate with the cluster. A capacity provider must be associated with a cluster before it can be included as part of the default capacity provider strategy of the cluster or used in a capacity provider strategy when calling the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html">RunTask</a> actions.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must be created but not associated with another cluster. New Auto Scaling group capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p> <p>The <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutCapacityProvider.html">PutCapacityProvider</a> API operation is used to update the list of available capacity providers for a cluster after the cluster is created.</p>
            default_capacity_provider_strategy: <p>The capacity provider strategy to set as the default for the cluster. After a default capacity provider strategy is set for a cluster, when you call the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html">RunTask</a> APIs with no capacity provider strategy or launch type specified, the default capacity provider strategy for the cluster is used.</p> <p>If a default capacity provider strategy isn't defined for a cluster when it was created, it can be defined later with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API operation.</p>
            service_connect_defaults: <p>Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the <code>enabled</code> parameter to <code>true</code> in the <code>ServiceConnectConfiguration</code>. You can set the namespace of each service individually in the <code>ServiceConnectConfiguration</code> to override this default parameter.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new cluster
            This example creates a cluster in your default region.

            >>> await client.create_cluster(cluster_name='my_cluster')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.create_cluster_request.CreateClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.create_cluster_response.CreateClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_cluster

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.create_cluster_request.CreateClusterRequest = {}
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if tags is not None:
            input_["tags"] = tags
        if settings is not None:
            input_["settings"] = settings
        if configuration is not None:
            input_["configuration"] = configuration
        if capacity_providers is not None:
            input_["capacity_providers"] = capacity_providers
        if default_capacity_provider_strategy is not None:
            input_["default_capacity_provider_strategy"] = (
                default_capacity_provider_strategy
            )
        if service_connect_defaults is not None:
            input_["service_connect_defaults"] = service_connect_defaults

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_container_instance(
        self,
        container_instance: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        force: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.deregister_container_instance_response.DeregisterContainerInstanceResponse":
        """<p>Deregisters an Amazon ECS container instance from the specified cluster. This instance is no longer available to run tasks.</p> <p>If you intend to use the container instance for some other purpose after deregistration, we recommend that you stop all of the tasks running on the container instance before deregistration. That prevents any orphaned tasks from consuming resources.</p> <p>Deregistering a container instance removes the instance from a cluster, but it doesn't terminate the EC2 instance. If you are finished using the instance, be sure to terminate it in the Amazon EC2 console to stop billing.</p> <note> <p>If you terminate a running container instance, Amazon ECS automatically deregisters the instance from your cluster (stopped container instances or instances with disconnected agents aren't automatically deregistered when terminated).</p> </note>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to deregister. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instance: <p>The container instance ID or full ARN of the container instance to deregister. For more information about the ARN format, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>
            force: <p>Forces the container instance to be deregistered. If you have tasks running on the container instance when you deregister it with the <code>force</code> option, these tasks remain running until you terminate the instance or the tasks stop through some other means, but they're orphaned (no longer monitored or accounted for by Amazon ECS). If an orphaned task on your container instance is part of an Amazon ECS service, then the service scheduler starts another copy of that task, on a different container instance if possible. </p> <p>Any containers in orphaned service tasks that are registered with a Classic Load Balancer or an Application Load Balancer target group are deregistered. They begin connection draining according to the settings on the load balancer or target group.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To deregister a container instance from a cluster
            This example deregisters a container instance from the specified cluster in your default region. If there are still tasks running on the container instance, you must either stop those tasks before deregistering, or use the force option.

            >>> await client.deregister_container_instance(cluster='default', force=True, container_instance='container_instance_UUID')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.deregister_container_instance_request.DeregisterContainerInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.deregister_container_instance_response.DeregisterContainerInstanceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.deregister_container_instance

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.deregister_container_instance.async_deregister_container_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.deregister_container_instance_request.DeregisterContainerInstanceRequest = {
            "container_instance": container_instance
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_clusters(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        clusters: Optional["capo_ecs.types.string_list.StringList"] = None,
        include: Optional["capo_ecs.types.cluster_field_list.ClusterFieldList"] = None,
    ) -> "capo_ecs.types.describe_clusters_response.DescribeClustersResponse":
        """<p>Describes one or more of your clusters.</p> <p> For CLI examples, see <a href="https://github.com/aws/aws-cli/blob/develop/awscli/examples/ecs/describe-clusters.rst">describe-clusters.rst</a> on GitHub.</p>

        Args:
            clusters: <p>A list of up to 100 cluster names or full cluster Amazon Resource Name (ARN) entries. If you do not specify a cluster, the default cluster is assumed.</p>
            include: <p>Determines whether to include additional information about the clusters in the response. If this field is omitted, this information isn't included.</p> <p>If <code>ATTACHMENTS</code> is specified, the attachments for the container instances or tasks within the cluster are included, for example the capacity providers.</p> <p>If <code>SETTINGS</code> is specified, the settings for the cluster are included.</p> <p>If <code>CONFIGURATIONS</code> is specified, the configuration for the cluster is included.</p> <p>If <code>STATISTICS</code> is specified, the task and service count is included, separated by launch type.</p> <p>If <code>TAGS</code> is specified, the metadata tags associated with the cluster are included.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a cluster
            This example provides a description of the specified cluster in your default region.

            >>> await client.describe_clusters(clusters=['default'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_clusters_request.DescribeClustersRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_clusters_response.DescribeClustersResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_clusters

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_clusters.async_describe_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_clusters_request.DescribeClustersRequest = {}
        if clusters is not None:
            input_["clusters"] = clusters
        if include is not None:
            input_["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_command(
        self,
        command: "capo_ecs.types.string.String",
        interactive: "capo_ecs.types.boolean.Boolean",
        task: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        container: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.execute_command_response.ExecuteCommandResponse":
        """<p>Runs a command remotely on a container within a task.</p> <p>If you use a condition key in your IAM policy to refine the conditions for the policy statement, for example limit the actions to a specific cluster, you receive an <code>AccessDeniedException</code> when there is a mismatch between the condition key value and the corresponding parameter value.</p> <p>For information about required permissions and considerations, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html">Using Amazon ECS Exec for debugging</a> in the <i>Amazon ECS Developer Guide</i>. </p>

        Args:
            cluster: <p>The Amazon Resource Name (ARN) or short name of the cluster the task is running in. If you do not specify a cluster, the default cluster is assumed.</p>
            container: <p>The name of the container to execute the command on. A container name only needs to be specified for tasks containing multiple containers.</p>
            command: <p>The command to run on the container.</p>
            interactive: <p>Use this flag to run your command in interactive mode.</p>
            task: <p>The Amazon Resource Name (ARN) or ID of the task the container is part of.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.target_not_connected_exception.TargetNotConnectedException: <p>The execute command cannot run. This error can be caused by any of the following configuration issues:</p> <ul> <li> <p>Incorrect IAM permissions</p> </li> <li> <p>The SSM agent is not installed or is not running</p> </li> <li> <p> There is an interface Amazon VPC endpoint for Amazon ECS, but there is not one for Systems Manager Session Manager</p> </li> </ul> <p>For information about how to troubleshoot the issues, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html">Troubleshooting issues with ECS Exec</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To run a command remotely on a container in a task
            This example runs an interactive /bin/sh command on a container MyContainer.

            >>> await client.execute_command(cluster='MyCluster', container='MyContainer', command='/bin/sh', interactive=True, task='arn:aws:ecs:us-east-1:123456789012:task/MyCluster/d789e94343414c25b9f6bd59eEXAMPLE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.execute_command_request.ExecuteCommandRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.execute_command_response.ExecuteCommandResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.execute_command

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.execute_command.async_execute_command(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.execute_command_request.ExecuteCommandRequest = {
            "command": command,
            "interactive": interactive,
            "task": task,
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if container is not None:
            input_["container"] = container

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_attributes(
        self,
        target_type: "capo_ecs.types.target_type.TargetType",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        attribute_name: Optional["capo_ecs.types.string.String"] = None,
        attribute_value: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_attributes_response.ListAttributesResponse":
        """<p>Lists the attributes for Amazon ECS resources within a specified target type and cluster. When you specify a target type and cluster, <code>ListAttributes</code> returns a list of attribute objects, one for each attribute on each resource. You can filter the list of results to a single attribute name to only return results that have that name. You can also filter the results by attribute name and value. You can do this, for example, to see which container instances in a cluster are running a Linux AMI (<code>ecs.os-type=linux</code>). </p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to list attributes. If you do not specify a cluster, the default cluster is assumed.</p>
            target_type: <p>The type of the target to list attributes with.</p>
            attribute_name: <p>The name of the attribute to filter the results with. </p>
            attribute_value: <p>The value of the attribute to filter results with. You must also specify an attribute name to use this parameter.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListAttributes</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of cluster results that <code>ListAttributes</code> returned in paginated output. When this parameter is used, <code>ListAttributes</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListAttributes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListAttributes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list container instances that have a specific attribute
            This example lists attributes for a container instance with the attribute "stack" equal to the value "production".

            >>> await client.list_attributes(cluster='MyCluster', target_type='container-instance', attribute_name='stack', attribute_value='production')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_attributes_request.ListAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_attributes_response.ListAttributesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_attributes

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_attributes.async_list_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_attributes_request.ListAttributesRequest = {
            "target_type": target_type
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if attribute_name is not None:
            input_["attribute_name"] = attribute_name
        if attribute_value is not None:
            input_["attribute_value"] = attribute_value
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

    async def iter_list_attributes(
        self,
        target_type: "capo_ecs.types.target_type.TargetType",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        attribute_name: Optional["capo_ecs.types.string.String"] = None,
        attribute_value: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "AsyncIterator[capo_ecs.types.attribute.Attribute]":
        _token = next_token
        while True:
            _response = await self.list_attributes(
                target_type,
                config_overrides=config_overrides,
                cluster=cluster,
                attribute_name=attribute_name,
                attribute_value=attribute_value,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("attributes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_clusters(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_clusters_response.ListClustersResponse":
        """<p>Returns a list of existing clusters.</p>

        Args:
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListClusters</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of cluster results that <code>ListClusters</code> returned in paginated output. When this parameter is used, <code>ListClusters</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListClusters</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListClusters</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your available clusters
            This example lists all of your available clusters in your default region.

            >>> await client.list_clusters()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_clusters_request.ListClustersRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_clusters_response.ListClustersResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_clusters

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_clusters.async_list_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_clusters_request.ListClustersRequest = {}
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

    async def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "AsyncIterator[capo_ecs.types.string.String]":
        _token = next_token
        while True:
            _response = await self.list_clusters(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("cluster_arns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_container_instances(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        filter: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        status: Optional[
            "capo_ecs.types.container_instance_status.ContainerInstanceStatus"
        ] = None,
    ) -> "capo_ecs.types.list_container_instances_response.ListContainerInstancesResponse":
        """<p>Returns a list of container instances in a specified cluster. You can filter the results of a <code>ListContainerInstances</code> operation with cluster query language statements inside the <code>filter</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html">Cluster Query Language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.</p>
            filter: <p>You can filter the results of a <code>ListContainerInstances</code> operation with cluster query language statements. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html">Cluster Query Language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListContainerInstances</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of container instance results that <code>ListContainerInstances</code> returned in paginated output. When this parameter is used, <code>ListContainerInstances</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListContainerInstances</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListContainerInstances</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            status: <p>Filters the container instances by status. For example, if you specify the <code>DRAINING</code> status, the results include only container instances that have been set to <code>DRAINING</code> using <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateContainerInstancesState.html">UpdateContainerInstancesState</a>. If you don't specify this parameter, the The default is to include container instances set to all states other than <code>INACTIVE</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your available container instances in a cluster
            This example lists all of your available container instances in the specified cluster in your default region.

            >>> await client.list_container_instances(cluster='default')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_container_instances_request.ListContainerInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_container_instances_response.ListContainerInstancesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_container_instances

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_container_instances.async_list_container_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_container_instances_request.ListContainerInstancesRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_container_instances(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        filter: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        status: Optional[
            "capo_ecs.types.container_instance_status.ContainerInstanceStatus"
        ] = None,
    ) -> "AsyncIterator[capo_ecs.types.string.String]":
        _token = next_token
        while True:
            _response = await self.list_container_instances(
                config_overrides=config_overrides,
                cluster=cluster,
                filter=filter,
                next_token=_token,
                max_results=max_results,
                status=status,
            )
            _page = _resolve_path(_response, ("container_instance_arns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def submit_attachment_state_changes(
        self,
        attachments: "capo_ecs.types.attachment_state_changes.AttachmentStateChanges",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.submit_attachment_state_changes_response.SubmitAttachmentStateChangesResponse":
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Sent to acknowledge that an attachment changed states.</p>

        Args:
            cluster: <p>The short name or full ARN of the cluster that hosts the container instance the attachment belongs to.</p>
            attachments: <p>Any attachments associated with the state change request.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.submit_attachment_state_changes_request.SubmitAttachmentStateChangesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.submit_attachment_state_changes_response.SubmitAttachmentStateChangesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_attachment_state_changes

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_attachment_state_changes.async_submit_attachment_state_changes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.submit_attachment_state_changes_request.SubmitAttachmentStateChangesRequest = {
            "attachments": attachments
        }
        if cluster is not None:
            input_["cluster"] = cluster

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_container_state_change(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        task: Optional["capo_ecs.types.string.String"] = None,
        container_name: Optional["capo_ecs.types.string.String"] = None,
        runtime_id: Optional["capo_ecs.types.string.String"] = None,
        status: Optional["capo_ecs.types.string.String"] = None,
        exit_code: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        reason: Optional["capo_ecs.types.string.String"] = None,
        network_bindings: Optional[
            "capo_ecs.types.network_bindings.NetworkBindings"
        ] = None,
    ) -> "capo_ecs.types.submit_container_state_change_response.SubmitContainerStateChangeResponse":
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Sent to acknowledge that a container changed states.</p>

        Args:
            cluster: <p>The short name or full ARN of the cluster that hosts the container.</p>
            task: <p>The task ID or full Amazon Resource Name (ARN) of the task that hosts the container.</p>
            container_name: <p>The name of the container.</p>
            runtime_id: <p>The ID of the Docker container.</p>
            status: <p>The status of the state change request.</p>
            exit_code: <p>The exit code that's returned for the state change request.</p>
            reason: <p>The reason for the state change request.</p>
            network_bindings: <p>The network bindings of the container.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.submit_container_state_change_request.SubmitContainerStateChangeRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.submit_container_state_change_response.SubmitContainerStateChangeResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_container_state_change

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_container_state_change.async_submit_container_state_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.submit_container_state_change_request.SubmitContainerStateChangeRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if task is not None:
            input_["task"] = task
        if container_name is not None:
            input_["container_name"] = container_name
        if runtime_id is not None:
            input_["runtime_id"] = runtime_id
        if status is not None:
            input_["status"] = status
        if exit_code is not None:
            input_["exit_code"] = exit_code
        if reason is not None:
            input_["reason"] = reason
        if network_bindings is not None:
            input_["network_bindings"] = network_bindings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_task_state_change(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        task: Optional["capo_ecs.types.string.String"] = None,
        status: Optional["capo_ecs.types.string.String"] = None,
        reason: Optional["capo_ecs.types.string.String"] = None,
        containers: Optional[
            "capo_ecs.types.container_state_changes.ContainerStateChanges"
        ] = None,
        attachments: Optional[
            "capo_ecs.types.attachment_state_changes.AttachmentStateChanges"
        ] = None,
        managed_agents: Optional[
            "capo_ecs.types.managed_agent_state_changes.ManagedAgentStateChanges"
        ] = None,
        pull_started_at: Optional["capo_ecs.types.timestamp.Timestamp"] = None,
        pull_stopped_at: Optional["capo_ecs.types.timestamp.Timestamp"] = None,
        execution_stopped_at: Optional["capo_ecs.types.timestamp.Timestamp"] = None,
    ) -> (
        "capo_ecs.types.submit_task_state_change_response.SubmitTaskStateChangeResponse"
    ):
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Sent to acknowledge that a task changed states.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task.</p>
            task: <p>The task ID or full ARN of the task in the state change request.</p>
            status: <p>The status of the state change request.</p>
            reason: <p>The reason for the state change request.</p>
            containers: <p>Any containers that's associated with the state change request.</p>
            attachments: <p>Any attachments associated with the state change request.</p>
            managed_agents: <p>The details for the managed agent that's associated with the task.</p>
            pull_started_at: <p>The Unix timestamp for the time when the container image pull started.</p>
            pull_stopped_at: <p>The Unix timestamp for the time when the container image pull completed.</p>
            execution_stopped_at: <p>The Unix timestamp for the time when the task execution stopped.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.submit_task_state_change_request.SubmitTaskStateChangeRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.submit_task_state_change_response.SubmitTaskStateChangeResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_task_state_change

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_task_state_change.async_submit_task_state_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.submit_task_state_change_request.SubmitTaskStateChangeRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if task is not None:
            input_["task"] = task
        if status is not None:
            input_["status"] = status
        if reason is not None:
            input_["reason"] = reason
        if containers is not None:
            input_["containers"] = containers
        if attachments is not None:
            input_["attachments"] = attachments
        if managed_agents is not None:
            input_["managed_agents"] = managed_agents
        if pull_started_at is not None:
            input_["pull_started_at"] = pull_started_at
        if pull_stopped_at is not None:
            input_["pull_stopped_at"] = pull_stopped_at
        if execution_stopped_at is not None:
            input_["execution_stopped_at"] = execution_stopped_at

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_attributes(
        self,
        attributes: "capo_ecs.types.attributes.Attributes",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.delete_attributes_response.DeleteAttributesResponse":
        """<p>Deletes one or more custom attributes from an Amazon ECS resource.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to delete attributes. If you do not specify a cluster, the default cluster is assumed.</p>
            attributes: <p>The attributes to delete from your resource. You can specify up to 10 attributes for each request. For custom attributes, specify the attribute name and target ID, but don't specify the value. If you specify the target ID using the short form, you must also specify the target type.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.target_not_found_exception.TargetNotFoundException: <p>The specified target wasn't found. You can view your available container instances with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListContainerInstances.html">ListContainerInstances</a>. Amazon ECS container instances are cluster-specific and Region-specific.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a custom attribute from an Amazon ECS instance
            This example deletes an attribute named stack from a container instance.

            >>> await client.delete_attributes(attributes=[{'name': 'stack', 'targetId': 'aws:ecs:us-west-2:130757420319:container-instance/1c3be8ed-df30-47b4-8f1e-6e68ebd01f34'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_attributes_request.DeleteAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_attributes_response.DeleteAttributesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_attributes

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_attributes.async_delete_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.delete_attributes_request.DeleteAttributesRequest = {
            "attributes": attributes
        }
        if cluster is not None:
            input_["cluster"] = cluster

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_container_instances(
        self,
        container_instances: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        include: Optional[
            "capo_ecs.types.container_instance_field_list.ContainerInstanceFieldList"
        ] = None,
    ) -> "capo_ecs.types.describe_container_instances_response.DescribeContainerInstancesResponse":
        """<p>Describes one or more container instances. Returns metadata about each container instance requested.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the container instance or container instances you are describing were launched in any cluster other than the default cluster.</p>
            container_instances: <p>A list of up to 100 container instance IDs or full Amazon Resource Name (ARN) entries.</p>
            include: <p>Specifies whether you want to see the resource tags for the container instance. If <code>TAGS</code> is specified, the tags are included in the response. If <code>CONTAINER_INSTANCE_HEALTH</code> is specified, the container instance health is included in the response. If this field is omitted, tags and container instance health status aren't included in the response.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe container instance
            This example provides a description of the specified container instance in your default region, using the container instance UUID as an identifier.

            >>> await client.describe_container_instances(cluster='default', container_instances=['f2756532-8f13-4d53-87c9-aed50dc94cd7'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_container_instances_request.DescribeContainerInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_container_instances_response.DescribeContainerInstancesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_container_instances

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_container_instances.async_describe_container_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_container_instances_request.DescribeContainerInstancesRequest = {
            "container_instances": container_instances
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if include is not None:
            input_["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tasks(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        container_instance: Optional["capo_ecs.types.string.String"] = None,
        family: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        started_by: Optional["capo_ecs.types.string.String"] = None,
        service_name: Optional["capo_ecs.types.string.String"] = None,
        desired_status: Optional["capo_ecs.types.desired_status.DesiredStatus"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        daemon_name: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.list_tasks_response.ListTasksResponse":
        """<p>Returns a list of tasks. You can filter the results by cluster, task definition family, container instance, launch type, what IAM principal started the task, or by the desired status of the task.</p> <p>Recently stopped tasks might appear in the returned results. </p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the <code>ListTasks</code> results. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instance: <p>The container instance ID or full ARN of the container instance to use when filtering the <code>ListTasks</code> results. Specifying a <code>containerInstance</code> limits the results to tasks that belong to that container instance.</p>
            family: <p>The name of the task definition family to use when filtering the <code>ListTasks</code> results. Specifying a <code>family</code> limits the results to tasks that belong to that family.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListTasks</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of task results that <code>ListTasks</code> returned in paginated output. When this parameter is used, <code>ListTasks</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListTasks</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListTasks</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            started_by: <p>The <code>startedBy</code> value to filter the task results with. Specifying a <code>startedBy</code> value limits the results to tasks that were started with that value.</p> <p>When you specify <code>startedBy</code> as the filter, it must be the only filter that you use.</p>
            service_name: <p>The name of the service to use when filtering the <code>ListTasks</code> results. Specifying a <code>serviceName</code> limits the results to tasks that belong to that service.</p>
            desired_status: <p>The task desired status to use when filtering the <code>ListTasks</code> results. Specifying a <code>desiredStatus</code> of <code>STOPPED</code> limits the results to tasks that Amazon ECS has set the desired status to <code>STOPPED</code>. This can be useful for debugging tasks that aren't starting properly or have died or finished. The default status filter is <code>RUNNING</code>, which shows tasks that Amazon ECS has set the desired status to <code>RUNNING</code>.</p> <note> <p>Although you can filter results based on a desired status of <code>PENDING</code>, this doesn't return any results. Amazon ECS never sets the desired status of a task to that value (only a task's <code>lastStatus</code> may have a value of <code>PENDING</code>).</p> </note>
            launch_type: <p>The launch type to use when filtering the <code>ListTasks</code> results.</p>
            daemon_name: <p>The name of the daemon to use when filtering the <code>ListTasks</code> results. Specifying a <code>daemonName</code> limits the results to tasks that belong to that daemon.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the tasks in a cluster
            This example lists all of the tasks in a cluster.

            >>> await client.list_tasks(cluster='default')
            To list the tasks on a particular container instance
            This example lists the tasks of a specified container instance. Specifying a ``containerInstance`` value limits  the  results  to  tasks  that belong to that container instance.

            >>> await client.list_tasks(cluster='default', container_instance='f6bbb147-5370-4ace-8c73-c7181ded911f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_tasks_request.ListTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_tasks_response.ListTasksResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_tasks

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_tasks.async_list_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_tasks_request.ListTasksRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if container_instance is not None:
            input_["container_instance"] = container_instance
        if family is not None:
            input_["family"] = family
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if started_by is not None:
            input_["started_by"] = started_by
        if service_name is not None:
            input_["service_name"] = service_name
        if desired_status is not None:
            input_["desired_status"] = desired_status
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if daemon_name is not None:
            input_["daemon_name"] = daemon_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_tasks(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        container_instance: Optional["capo_ecs.types.string.String"] = None,
        family: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        started_by: Optional["capo_ecs.types.string.String"] = None,
        service_name: Optional["capo_ecs.types.string.String"] = None,
        desired_status: Optional["capo_ecs.types.desired_status.DesiredStatus"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        daemon_name: Optional["capo_ecs.types.string.String"] = None,
    ) -> "AsyncIterator[capo_ecs.types.string.String]":
        _token = next_token
        while True:
            _response = await self.list_tasks(
                config_overrides=config_overrides,
                cluster=cluster,
                container_instance=container_instance,
                family=family,
                next_token=_token,
                max_results=max_results,
                started_by=started_by,
                service_name=service_name,
                desired_status=desired_status,
                launch_type=launch_type,
                daemon_name=daemon_name,
            )
            _page = _resolve_path(_response, ("task_arns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_attributes(
        self,
        attributes: "capo_ecs.types.attributes.Attributes",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.put_attributes_response.PutAttributesResponse":
        """<p>Create or update an attribute on an Amazon ECS resource. If the attribute doesn't exist, it's created. If the attribute exists, its value is replaced with the specified value. To delete an attribute, use <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteAttributes.html">DeleteAttributes</a>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes">Attributes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to apply attributes. If you do not specify a cluster, the default cluster is assumed.</p>
            attributes: <p>The attributes to apply to your resource. You can specify up to 10 custom attributes for each resource. You can specify up to 10 attributes in a single call.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.attribute_limit_exceeded_exception.AttributeLimitExceededException: <p>You can apply up to 10 custom attributes for each resource. You can view the attributes of a resource with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListAttributes.html">ListAttributes</a>. You can remove existing attributes on a resource with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteAttributes.html">DeleteAttributes</a>.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.target_not_found_exception.TargetNotFoundException: <p>The specified target wasn't found. You can view your available container instances with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListContainerInstances.html">ListContainerInstances</a>. Amazon ECS container instances are cluster-specific and Region-specific.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create or update an attribute on a resource
            This example adds an attribute "stack" with the value "production" to a container instance.

            >>> await client.put_attributes(cluster='MyCluster', attributes=[{'targetId': 'arn:aws:ecs:us-west-2:123456789012:container-instance/1c3be8ed-df30-47b4-8f1e-6e68ebd01f34', 'name': 'stack', 'value': 'production'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.put_attributes_request.PutAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.put_attributes_response.PutAttributesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.put_attributes

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.put_attributes.async_put_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.put_attributes_request.PutAttributesRequest = {
            "attributes": attributes
        }
        if cluster is not None:
            input_["cluster"] = cluster

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_container_instance(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        instance_identity_document: Optional["capo_ecs.types.string.String"] = None,
        instance_identity_document_signature: Optional[
            "capo_ecs.types.string.String"
        ] = None,
        total_resources: Optional["capo_ecs.types.resources.Resources"] = None,
        version_info: Optional["capo_ecs.types.version_info.VersionInfo"] = None,
        container_instance_arn: Optional["capo_ecs.types.string.String"] = None,
        attributes: Optional["capo_ecs.types.attributes.Attributes"] = None,
        platform_devices: Optional[
            "capo_ecs.types.platform_devices.PlatformDevices"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
    ) -> "capo_ecs.types.register_container_instance_response.RegisterContainerInstanceResponse":
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to register your container instance with. If you do not specify a cluster, the default cluster is assumed.</p>
            instance_identity_document: <p>The instance identity document for the EC2 instance to register. This document can be found by running the following command from the instance: <code>curl http://169.254.169.254/latest/dynamic/instance-identity/document/</code> </p>
            instance_identity_document_signature: <p>The instance identity document signature for the EC2 instance to register. This signature can be found by running the following command from the instance: <code>curl http://169.254.169.254/latest/dynamic/instance-identity/signature/</code> </p>
            total_resources: <p>The resources available on the instance.</p>
            version_info: <p>The version information for the Amazon ECS container agent and Docker daemon that runs on the container instance.</p>
            container_instance_arn: <p>The ARN of the container instance (if it was previously registered).</p>
            attributes: <p>The container instance attributes that this container instance supports.</p>
            platform_devices: <p>The devices that are available on the container instance. The supported device types are GPUs and Neuron devices.</p>
            tags: <p>The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.register_container_instance_request.RegisterContainerInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.register_container_instance_response.RegisterContainerInstanceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.register_container_instance

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.register_container_instance.async_register_container_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.register_container_instance_request.RegisterContainerInstanceRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if instance_identity_document is not None:
            input_["instance_identity_document"] = instance_identity_document
        if instance_identity_document_signature is not None:
            input_["instance_identity_document_signature"] = (
                instance_identity_document_signature
            )
        if total_resources is not None:
            input_["total_resources"] = total_resources
        if version_info is not None:
            input_["version_info"] = version_info
        if container_instance_arn is not None:
            input_["container_instance_arn"] = container_instance_arn
        if attributes is not None:
            input_["attributes"] = attributes
        if platform_devices is not None:
            input_["platform_devices"] = platform_devices
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_container_agent(
        self,
        container_instance: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.update_container_agent_response.UpdateContainerAgentResponse":
        """<p>Updates the Amazon ECS container agent on a specified container instance. Updating the Amazon ECS container agent doesn't interrupt running tasks or services on the container instance. The process for updating the agent differs depending on whether your container instance was launched with the Amazon ECS-optimized AMI or another operating system.</p> <note> <p>The <code>UpdateContainerAgent</code> API isn't supported for container instances using the Amazon ECS-optimized Amazon Linux 2 (arm64) AMI. To update the container agent, you can update the <code>ecs-init</code> package. This updates the agent. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/agent-update-ecs-ami.html">Updating the Amazon ECS container agent</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note> <note> <p>Agent updates with the <code>UpdateContainerAgent</code> API operation do not apply to Windows container instances. We recommend that you launch new container instances to update the agent version in your Windows clusters.</p> </note> <p>The <code>UpdateContainerAgent</code> API requires an Amazon ECS-optimized AMI or Amazon Linux AMI with the <code>ecs-init</code> service installed and running. For help updating the Amazon ECS container agent on other operating systems, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html#manually_update_agent">Manually updating the Amazon ECS container agent</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that your container instance is running on. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instance: <p>The container instance ID or full ARN entries for the container instance where you would like to update the Amazon ECS container agent.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.missing_version_exception.MissingVersionException: <p>Amazon ECS can't determine the current version of the Amazon ECS container agent on the container instance and doesn't have enough information to proceed with an update. This could be because the agent running on the container instance is a previous or custom version that doesn't use our version information.</p>
            capo_ecs.errors.no_update_available_exception.NoUpdateAvailableException: <p>There's no update available for this Amazon ECS container agent. This might be because the agent is already running the latest version or because it's so old that there's no update path to the current version.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update the container agent version on a container instance
            This example updates the container agent version on the specified container instance in cluster MyCluster.

            >>> await client.update_container_agent(cluster='MyCluster', container_instance='53ac7152-dcd1-4102-81f5-208962864132')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_container_agent_request.UpdateContainerAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_container_agent_response.UpdateContainerAgentResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_container_agent

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_container_agent.async_update_container_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.update_container_agent_request.UpdateContainerAgentRequest = {
            "container_instance": container_instance
        }
        if cluster is not None:
            input_["cluster"] = cluster

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_container_instances_state(
        self,
        container_instances: "capo_ecs.types.string_list.StringList",
        status: "capo_ecs.types.container_instance_status.ContainerInstanceStatus",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.update_container_instances_state_response.UpdateContainerInstancesStateResponse":
        """<p>Modifies the status of an Amazon ECS container instance.</p> <p>Once a container instance has reached an <code>ACTIVE</code> state, you can change the status of a container instance to <code>DRAINING</code> to manually remove an instance from a cluster, for example to perform system updates, update the Docker daemon, or scale down the cluster size.</p> <important> <p>A container instance can't be changed to <code>DRAINING</code> until it has reached an <code>ACTIVE</code> status. If the instance is in any other status, an error will be received.</p> </important> <p>When you set a container instance to <code>DRAINING</code>, Amazon ECS prevents new tasks from being scheduled for placement on the container instance and replacement service tasks are started on other container instances in the cluster if the resources are available. Service tasks on the container instance that are in the <code>PENDING</code> state are stopped immediately.</p> <p>Service tasks on the container instance that are in the <code>RUNNING</code> state are stopped and replaced according to the service's deployment configuration parameters, <code>minimumHealthyPercent</code> and <code>maximumPercent</code>. You can change the deployment configuration of your service using <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a>.</p> <ul> <li> <p>If <code>minimumHealthyPercent</code> is below 100%, the scheduler can ignore <code>desiredCount</code> temporarily during task replacement. For example, <code>desiredCount</code> is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. If the minimum is 100%, the service scheduler can't remove existing tasks until the replacement tasks are considered healthy. Tasks for services that do not use a load balancer are considered healthy if they're in the <code>RUNNING</code> state. Tasks for services that use a load balancer are considered healthy if they're in the <code>RUNNING</code> state and are reported as healthy by the load balancer.</p> </li> <li> <p>The <code>maximumPercent</code> parameter represents an upper limit on the number of running tasks during task replacement. You can use this to define the replacement batch size. For example, if <code>desiredCount</code> is four tasks, a maximum of 200% starts four new tasks before stopping the four tasks to be drained, provided that the cluster resources required to do this are available. If the maximum is 100%, then replacement tasks can't start until the draining tasks have stopped.</p> </li> </ul> <p>Any <code>PENDING</code> or <code>RUNNING</code> tasks that do not belong to a service aren't affected. You must wait for them to finish or stop them manually.</p> <p>A container instance has completed draining when it has no more <code>RUNNING</code> tasks. You can verify this using <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html">ListTasks</a>.</p> <p>When a container instance has been drained, you can set a container instance to <code>ACTIVE</code> status and once it has reached that status the Amazon ECS scheduler can begin scheduling tasks on the instance again.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to update. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instances: <p>A list of up to 10 container instance IDs or full ARN entries.</p>
            status: <p>The container instance state to update the container instance with. The only valid values for this action are <code>ACTIVE</code> and <code>DRAINING</code>. A container instance can only be updated to <code>DRAINING</code> status once it has reached an <code>ACTIVE</code> state. If a container instance is in <code>REGISTERING</code>, <code>DEREGISTERING</code>, or <code>REGISTRATION_FAILED</code> state you can describe the container instance but can't update the container instance state.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update the state of a container instance
            This example updates the state of the specified container instance in the default cluster to DRAINING.

            >>> await client.update_container_instances_state(cluster='default', container_instances=['1c3be8ed-df30-47b4-8f1e-6e68ebd01f34'], status='DRAINING')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_container_instances_state_request.UpdateContainerInstancesStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_container_instances_state_response.UpdateContainerInstancesStateResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_container_instances_state

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_container_instances_state.async_update_container_instances_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.update_container_instances_state_request.UpdateContainerInstancesStateRequest = {
            "container_instances": container_instances,
            "status": status,
        }
        if cluster is not None:
            input_["cluster"] = cluster

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_daemon_deployments(
        self,
        daemon_deployment_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_daemon_deployments_response.DescribeDaemonDeploymentsResponse":
        """<p>Describes one or more of your daemon deployments.</p> <p>A daemon deployment orchestrates the progressive rollout of daemon task updates across container instances managed by the daemon's capacity providers. Each deployment includes circuit breaker and alarm-based rollback capabilities.</p>

        Args:
            daemon_deployment_arns: <p>The ARN of the daemon deployments to describe. You can specify up to 20 ARNs.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe daemon deployments
            This example describes a daemon deployment for the my-monitoring-daemon daemon.

            >>> await client.describe_daemon_deployments(daemon_deployment_arns=['arn:aws:ecs:us-east-1:123456789012:daemon-deployment/my-cluster/my-monitoring-daemon/aB1cD2eF3gH4iJ5k'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_daemon_deployments_request.DescribeDaemonDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_daemon_deployments_response.DescribeDaemonDeploymentsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_deployments

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_deployments.async_describe_daemon_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_daemon_deployments_request.DescribeDaemonDeploymentsRequest = {
            "daemon_deployment_arns": daemon_deployment_arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_daemon(
        self,
        daemon_name: "capo_ecs.types.string.String",
        daemon_task_definition_arn: "capo_ecs.types.string.String",
        capacity_provider_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster_arn: Optional["capo_ecs.types.string.String"] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.daemon_deployment_configuration.DaemonDeploymentConfiguration"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        propagate_tags: Optional[
            "capo_ecs.types.daemon_propagate_tags.DaemonPropagateTags"
        ] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        critical: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.create_daemon_response.CreateDaemonResponse":
        """<p>Creates a new daemon in the specified cluster and capacity providers. A daemon deploys cross-cutting software agents such as security monitoring, telemetry, and logging independently across your Amazon ECS infrastructure.</p> <p>Amazon ECS deploys exactly one daemon task on each container instance of the specified capacity providers. When a container instance registers with the cluster, Amazon ECS automatically starts daemon tasks. Amazon ECS starts a daemon task before scheduling other tasks.</p> <p>Daemons are essential for instance health - if a daemon task stops, Amazon ECS automatically drains and replaces that container instance.</p> <note> <p>ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.</p> </note>

        Args:
            daemon_name: <p>The name of the daemon. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster to create the daemon in.</p>
            daemon_task_definition_arn: <p>The Amazon Resource Name (ARN) of the daemon task definition to use for the daemon.</p>
            capacity_provider_arns: <p>The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon. The daemon deploys tasks on container instances managed by these capacity providers.</p>
            deployment_configuration: <p>Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.</p>
            tags: <p>The metadata that you apply to the daemon to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            propagate_tags: <p>Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation. To add tags to a task after task creation, use the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html">TagResource</a> API action.</p>
            enable_ecs_managed_tags: <p>Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>Determines whether the execute command functionality is turned on for the daemon. If <code>true</code>, the execute command functionality is turned on for all tasks in the daemon.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>
            critical: <p>If the <code>critical</code> parameter of a daemon is <code>true</code>, and the daemon task fails, stops, or becomes unhealthy, Amazon ECS drains the container instance and stops the other tasks running on it. If the <code>critical</code> parameter is <code>false</code>, the daemon task failure doesn't affect the other tasks on the instance. The default value is <code>true</code>.</p> <p>A non-critical daemon doesn't block instance registration. The container instance becomes active and continues to run your other tasks, whether the daemon task fails during scale-out or during a deployment.</p> <p>Amazon ECS emits an EventBridge event when a daemon task fails to start, for both critical and non-critical daemons.</p> <p>Daemon task launch failures during a deployment are still counted by the deployment circuit breaker. The circuit breaker can roll back an unstable target revision.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a daemon
            This example creates a daemon named my-monitoring-daemon in the specified cluster that uses the monitoring-agent daemon task definition and deploys to the specified capacity provider.

            >>> await client.create_daemon(daemon_name='my-monitoring-daemon', cluster_arn='arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster', daemon_task_definition_arn='arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:1', capacity_provider_arns=['arn:aws:ecs:us-east-1:123456789012:capacity-provider/my-capacity-provider'], deployment_configuration={'drainPercent': 10.0, 'bakeTimeInMinutes': 5})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.create_daemon_request.CreateDaemonRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.create_daemon_response.CreateDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_daemon

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.create_daemon.async_create_daemon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.create_daemon_request.CreateDaemonRequest = {
            "daemon_name": daemon_name,
            "daemon_task_definition_arn": daemon_task_definition_arn,
            "capacity_provider_arns": capacity_provider_arns,
        }
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if tags is not None:
            input_["tags"] = tags
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if client_token is not None:
            input_["client_token"] = client_token
        if critical is not None:
            input_["critical"] = critical

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_daemon(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_daemon_response.DeleteDaemonResponse":
        """<p>Deletes the specified daemon. The daemon must be in an <code>ACTIVE</code> state to be deleted. Deleting a daemon stops all running daemon tasks on the associated container instances. Amazon ECS drains existing container instances and provisions new instances without the deleted daemon. Amazon ECS automatically launches replacement tasks for your Amazon ECS services.</p> <note> <p>ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.</p> </note>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to delete.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.daemon_not_active_exception.DaemonNotActiveException: <p>The specified daemon isn't active. You can't update a daemon that's inactive. If you have previously deleted a daemon, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateDaemon.html">CreateDaemon</a>.</p>
            capo_ecs.errors.daemon_not_found_exception.DaemonNotFoundException: <p>The specified daemon wasn't found. You can view your available daemons with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html">ListDaemons</a>. Amazon ECS daemons are cluster specific and Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a daemon
            This example deletes the my-monitoring-daemon daemon.

            >>> await client.delete_daemon(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_daemon_request.DeleteDaemonRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_daemon_response.DeleteDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon.async_delete_daemon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.delete_daemon_request.DeleteDaemonRequest = {
            "daemon_arn": daemon_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_daemon(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_daemon_response.DescribeDaemonResponse":
        """<p>Describes the specified daemon.</p>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to describe.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.daemon_not_found_exception.DaemonNotFoundException: <p>The specified daemon wasn't found. You can view your available daemons with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html">ListDaemons</a>. Amazon ECS daemons are cluster specific and Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a daemon
            This example describes the my-monitoring-daemon daemon.

            >>> await client.describe_daemon(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_daemon_request.DescribeDaemonRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_daemon_response.DescribeDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon.async_describe_daemon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_daemon_request.DescribeDaemonRequest = {
            "daemon_arn": daemon_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_daemon_deployments(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        status: Optional[
            "capo_ecs.types.daemon_deployment_status_list.DaemonDeploymentStatusList"
        ] = None,
        created_at: Optional["capo_ecs.types.created_at.CreatedAt"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> (
        "capo_ecs.types.list_daemon_deployments_response.ListDaemonDeploymentsResponse"
    ):
        """<p>Returns a list of daemon deployments for a specified daemon. You can filter the results by status or creation time.</p>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to list deployments for.</p>
            status: <p>An optional filter to narrow the <code>ListDaemonDeployments</code> results by deployment status. If you don't specify a status, all deployments are returned.</p>
            created_at: <p>An optional filter to narrow the <code>ListDaemonDeployments</code> results by creation time. If you don't specify a time range, all deployments are returned.</p>
            max_results: <p>The maximum number of daemon deployment results that <code>ListDaemonDeployments</code> returned in paginated output. When this parameter is used, <code>ListDaemonDeployments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemonDeployments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemonDeployments</code> returns up to 20 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListDaemonDeployments</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list daemon deployments
            This example lists all successful daemon deployments for the my-monitoring-daemon daemon.

            >>> await client.list_daemon_deployments(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon', status=['SUCCESSFUL'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_daemon_deployments_request.ListDaemonDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_daemon_deployments_response.ListDaemonDeploymentsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_deployments

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_deployments.async_list_daemon_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_daemon_deployments_request.ListDaemonDeploymentsRequest = {
            "daemon_arn": daemon_arn
        }
        if status is not None:
            input_["status"] = status
        if created_at is not None:
            input_["created_at"] = created_at
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

    async def list_daemons(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster_arn: Optional["capo_ecs.types.string.String"] = None,
        capacity_provider_arns: Optional[
            "capo_ecs.types.string_list.StringList"
        ] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.list_daemons_response.ListDaemonsResponse":
        """<p>Returns a list of daemons. You can filter the results by cluster or capacity provider.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster to filter daemons by. If you do not specify a cluster, the default cluster is assumed.</p>
            capacity_provider_arns: <p>The Amazon Resource Names (ARNs) of the capacity providers to filter daemons by. Only daemons associated with the specified capacity providers are returned.</p>
            max_results: <p>The maximum number of daemon results that <code>ListDaemons</code> returned in paginated output. When this parameter is used, <code>ListDaemons</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemons</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemons</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListDaemons</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list daemons in a cluster
            This example lists all daemons in the specified cluster.

            >>> await client.list_daemons(cluster_arn='arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_daemons_request.ListDaemonsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_daemons_response.ListDaemonsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemons

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemons.async_list_daemons(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_daemons_request.ListDaemonsRequest = {}
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
        if capacity_provider_arns is not None:
            input_["capacity_provider_arns"] = capacity_provider_arns
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

    async def update_daemon(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        daemon_task_definition_arn: "capo_ecs.types.string.String",
        capacity_provider_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.daemon_deployment_configuration.DaemonDeploymentConfiguration"
        ] = None,
        propagate_tags: Optional[
            "capo_ecs.types.daemon_propagate_tags.DaemonPropagateTags"
        ] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        critical: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.update_daemon_response.UpdateDaemonResponse":
        """<p>Updates the specified daemon. When you update a daemon, a new deployment is triggered that progressively rolls out the changes to the container instances associated with the daemon's capacity providers. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/daemon-deployments.html">Daemon deployments</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Amazon ECS drains existing container instances and provisions new instances with the updated daemon. Amazon ECS automatically launches replacement tasks for your services.</p> <important> <p>Updating a daemon triggers a rolling deployment that drains and replaces container instances. Plan updates during maintenance windows to minimize impact on running services.</p> </important> <note> <p>ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.</p> </note>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to update.</p>
            daemon_task_definition_arn: <p>The Amazon Resource Name (ARN) of the daemon task definition to use for the updated daemon.</p>
            capacity_provider_arns: <p>The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon.</p>
            deployment_configuration: <p>Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation.</p>
            enable_ecs_managed_tags: <p>Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>If <code>true</code>, the execute command functionality is turned on for all tasks in the daemon. If <code>false</code>, the execute command functionality is turned off.</p>
            critical: <p>If the <code>critical</code> parameter of a daemon is <code>true</code>, and the daemon task fails, stops, or becomes unhealthy, Amazon ECS drains the container instance and stops the other tasks running on it. If the <code>critical</code> parameter is <code>false</code>, the daemon task failure doesn't affect the other tasks on the instance. The default value is <code>true</code>.</p> <p>A non-critical daemon doesn't block instance registration. The container instance becomes active and continues to run your other tasks, whether the daemon task fails during scale-out or during a deployment.</p> <p>Amazon ECS emits an EventBridge event when a daemon task fails to start, for both critical and non-critical daemons.</p> <p>Daemon task launch failures during a deployment are still counted by the deployment circuit breaker. The circuit breaker can roll back an unstable target revision.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.daemon_not_active_exception.DaemonNotActiveException: <p>The specified daemon isn't active. You can't update a daemon that's inactive. If you have previously deleted a daemon, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateDaemon.html">CreateDaemon</a>.</p>
            capo_ecs.errors.daemon_not_found_exception.DaemonNotFoundException: <p>The specified daemon wasn't found. You can view your available daemons with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html">ListDaemons</a>. Amazon ECS daemons are cluster specific and Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a daemon
            This example updates the my-monitoring-daemon daemon to use a new daemon task definition revision.

            >>> await client.update_daemon(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon', daemon_task_definition_arn='arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:2', capacity_provider_arns=['arn:aws:ecs:us-east-1:123456789012:capacity-provider/my-capacity-provider'], deployment_configuration={'drainPercent': 10.0, 'bakeTimeInMinutes': 5})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_daemon_request.UpdateDaemonRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_daemon_response.UpdateDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_daemon

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_daemon.async_update_daemon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.update_daemon_request.UpdateDaemonRequest = {
            "daemon_arn": daemon_arn,
            "daemon_task_definition_arn": daemon_task_definition_arn,
            "capacity_provider_arns": capacity_provider_arns,
        }
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if critical is not None:
            input_["critical"] = critical

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_daemon_revisions(
        self,
        daemon_revision_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_daemon_revisions_response.DescribeDaemonRevisionsResponse":
        """<p>Describes one or more of your daemon revisions.</p> <p>A daemon revision is a snapshot of a daemon's configuration at the time a deployment was initiated. It captures the daemon task definition, container images, tag propagation, and execute command settings. Daemon revisions are immutable.</p>

        Args:
            daemon_revision_arns: <p>The ARN of the daemon revisions to describe. You can specify up to 20 ARNs.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe daemon revisions
            This example describes a daemon revision for the my-monitoring-daemon daemon.

            >>> await client.describe_daemon_revisions(daemon_revision_arns=['arn:aws:ecs:us-east-1:123456789012:daemon-revision/my-cluster/my-monitoring-daemon/4980306466373577095'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_daemon_revisions_request.DescribeDaemonRevisionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_daemon_revisions_response.DescribeDaemonRevisionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_revisions

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_revisions.async_describe_daemon_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_daemon_revisions_request.DescribeDaemonRevisionsRequest = {
            "daemon_revision_arns": daemon_revision_arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_daemon_task_definition(
        self,
        daemon_task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_daemon_task_definition_response.DeleteDaemonTaskDefinitionResponse":
        """<p>Deletes the specified daemon task definition. After a daemon task definition is deleted, no new daemons can be created using this definition. Existing daemons that reference the deleted daemon task definition continue to run.</p> <p>A daemon task definition must be in an <code>ACTIVE</code> state to be deleted.</p>

        Args:
            daemon_task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the daemon task definition to delete.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a daemon task definition
            This example deletes the first revision of the monitoring-agent daemon task definition.

            >>> await client.delete_daemon_task_definition(daemon_task_definition='monitoring-agent:1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_daemon_task_definition_request.DeleteDaemonTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_daemon_task_definition_response.DeleteDaemonTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon_task_definition

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon_task_definition.async_delete_daemon_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.delete_daemon_task_definition_request.DeleteDaemonTaskDefinitionRequest = {
            "daemon_task_definition": daemon_task_definition
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_daemon_task_definition(
        self,
        daemon_task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_daemon_task_definition_response.DescribeDaemonTaskDefinitionResponse":
        """<p>Describes a daemon task definition. You can specify a <code>family</code> and <code>revision</code> to find information about a specific daemon task definition, or you can simply specify the family to find the latest <code>ACTIVE</code> revision in that family.</p>

        Args:
            daemon_task_definition: <p>The <code>family</code> for the latest <code>ACTIVE</code> revision, <code>family</code> and <code>revision</code> (<code>family:revision</code>) for a specific revision in the family, or full Amazon Resource Name (ARN) of the daemon task definition to describe.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a daemon task definition
            This example describes the first revision of the monitoring-agent daemon task definition.

            >>> await client.describe_daemon_task_definition(daemon_task_definition='monitoring-agent:1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_daemon_task_definition_request.DescribeDaemonTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_daemon_task_definition_response.DescribeDaemonTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_task_definition

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_task_definition.async_describe_daemon_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_daemon_task_definition_request.DescribeDaemonTaskDefinitionRequest = {
            "daemon_task_definition": daemon_task_definition
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_daemon_task_definitions(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        family_prefix: Optional["capo_ecs.types.string.String"] = None,
        family: Optional["capo_ecs.types.string.String"] = None,
        revision: Optional[
            "capo_ecs.types.daemon_task_definition_revision_filter.DaemonTaskDefinitionRevisionFilter"
        ] = None,
        status: Optional[
            "capo_ecs.types.daemon_task_definition_status_filter.DaemonTaskDefinitionStatusFilter"
        ] = None,
        sort: Optional["capo_ecs.types.sort_order.SortOrder"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_daemon_task_definitions_response.ListDaemonTaskDefinitionsResponse":
        """<p>Returns a list of daemon task definitions that are registered to your account. You can filter the results by family name, status, or both to find daemon task definitions that match your criteria.</p>

        Args:
            family_prefix: <p>The full family name to filter the <code>ListDaemonTaskDefinitions</code> results with. Specifying a <code>familyPrefix</code> limits the listed daemon task definitions to daemon task definition families that start with the <code>familyPrefix</code> string.</p>
            family: <p>The exact name of the daemon task definition family to filter results with.</p>
            revision: <p>The revision filter to apply. Specify <code>LAST_REGISTERED</code> to return only the last registered revision for each daemon task definition family.</p>
            status: <p>The daemon task definition status to filter the <code>ListDaemonTaskDefinitions</code> results with. By default, only <code>ACTIVE</code> daemon task definitions are listed. If you set this parameter to <code>DELETE_IN_PROGRESS</code>, only daemon task definitions that are in the process of being deleted are listed. If you set this parameter to <code>ALL</code>, all daemon task definitions are listed regardless of status.</p>
            sort: <p>The order to sort the results. Valid values are <code>ASC</code> and <code>DESC</code>. By default (<code>ASC</code>), daemon task definitions are listed in ascending order by family name and revision number.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListDaemonTaskDefinitions</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of daemon task definition results that <code>ListDaemonTaskDefinitions</code> returned in paginated output. When this parameter is used, <code>ListDaemonTaskDefinitions</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemonTaskDefinitions</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemonTaskDefinitions</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list daemon task definitions
            This example lists all daemon task definitions in your account that start with the monitoring prefix.

            >>> await client.list_daemon_task_definitions(family_prefix='monitoring')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_daemon_task_definitions_request.ListDaemonTaskDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_daemon_task_definitions_response.ListDaemonTaskDefinitionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_task_definitions

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_task_definitions.async_list_daemon_task_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_daemon_task_definitions_request.ListDaemonTaskDefinitionsRequest = {}
        if family_prefix is not None:
            input_["family_prefix"] = family_prefix
        if family is not None:
            input_["family"] = family
        if revision is not None:
            input_["revision"] = revision
        if status is not None:
            input_["status"] = status
        if sort is not None:
            input_["sort"] = sort
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

    async def register_daemon_task_definition(
        self,
        family: "capo_ecs.types.string.String",
        container_definitions: "capo_ecs.types.daemon_container_definition_list.DaemonContainerDefinitionList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        volumes: Optional["capo_ecs.types.daemon_volume_list.DaemonVolumeList"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        pid_mode: Optional["capo_ecs.types.daemon_pid_mode.DaemonPidMode"] = None,
        ipc_mode: Optional["capo_ecs.types.daemon_ipc_mode.DaemonIpcMode"] = None,
    ) -> "capo_ecs.types.register_daemon_task_definition_response.RegisterDaemonTaskDefinitionResponse":
        """<p>Registers a new daemon task definition from the supplied <code>family</code> and <code>containerDefinitions</code>. Optionally, you can add data volumes to your containers with the <code>volumes</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/daemon-task-definitions.html">Daemon task definitions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>A daemon task definition is a template that describes the containers that form a daemon. Daemons deploy cross-cutting software agents such as security monitoring, telemetry, and logging across your Amazon ECS infrastructure.</p> <p>Each time you call <code>RegisterDaemonTaskDefinition</code>, a new revision of the daemon task definition is created. You can't modify a revision after you register it.</p>

        Args:
            family: <p>You must specify a <code>family</code> for a daemon task definition. This family is used as a name for your daemon task definition. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>
            task_role_arn: <p>The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this daemon task can assume. All containers in this daemon task are granted the permissions that are specified in this role.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. The task execution role is required for daemon tasks that pull container images from Amazon ECR or send container logs to CloudWatch.</p>
            container_definitions: <p>A list of container definitions in JSON format that describe the containers that make up your daemon task.</p>
            cpu: <p>The number of CPU units used by the daemon task. It can be expressed as an integer using CPU units (for example, <code>1024</code>).</p>
            memory: <p>The amount of memory (in MiB) used by the daemon task. It can be expressed as an integer using MiB (for example, <code>1024</code>).</p>
            volumes: <p>A list of volume definitions in JSON format that containers in your daemon task can use.</p>
            tags: <p>The metadata that you apply to the daemon task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            pid_mode: <p>The PID namespace mode for the daemon. The valid values are <code>none</code> and <code>shared</code>. The default is <code>none</code>.</p> <p>If <code>none</code> is specified or no value is provided, the daemon runs with its own PID namespace, isolated from other tasks. If <code>shared</code> is specified, the daemon joins the host PID namespace, making it accessible to non-daemon tasks that use <code>pidMode: "host"</code> or other daemons that use <code>pidMode: "shared"</code>.</p>
            ipc_mode: <p>The IPC namespace mode for the daemon. The valid values are <code>none</code> and <code>shared</code>. The default is <code>none</code>.</p> <p>If <code>none</code> is specified or no value is provided, the daemon runs with its own IPC namespace, isolated from other tasks. If <code>shared</code> is specified, the daemon joins the host IPC namespace, making it accessible to non-daemon tasks that use <code>ipcMode: "host"</code> or other daemons that use <code>ipcMode: "shared"</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To register a daemon task definition
            This example registers a daemon task definition in the monitoring-agent family with a single container that runs a CloudWatch agent.

            >>> await client.register_daemon_task_definition(family='monitoring-agent', container_definitions=[{'name': 'cloudwatch-agent', 'image': 'public.ecr.aws/cloudwatch-agent/cloudwatch-agent:latest', 'memory': 256, 'cpu': 128, 'essential': True, 'logConfiguration': {'logDriver': 'awslogs', 'options': {'awslogs-group': '/ecs/daemon/monitoring-agent', 'awslogs-region': 'us-east-1', 'awslogs-stream-prefix': 'ecs'}}, 'environment': [{'name': 'USE_DEFAULT_CONFIG', 'value': 'true'}]}], cpu='128', memory='256', execution_role_arn='arn:aws:iam::123456789012:role/ecsTaskExecutionRole', task_role_arn='arn:aws:iam::123456789012:role/ecsDaemonTaskRole')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.register_daemon_task_definition_request.RegisterDaemonTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.register_daemon_task_definition_response.RegisterDaemonTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.register_daemon_task_definition

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.register_daemon_task_definition.async_register_daemon_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.register_daemon_task_definition_request.RegisterDaemonTaskDefinitionRequest = {
            "family": family,
            "container_definitions": container_definitions,
        }
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if volumes is not None:
            input_["volumes"] = volumes
        if tags is not None:
            input_["tags"] = tags
        if pid_mode is not None:
            input_["pid_mode"] = pid_mode
        if ipc_mode is not None:
            input_["ipc_mode"] = ipc_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_service_deployments(
        self,
        service_deployment_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse":
        """<p>Describes one or more of your service deployments.</p> <p>A service deployment happens when you release a software update for the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html">View service history using Amazon ECS service deployments</a>.</p>

        Args:
            service_deployment_arns: <p>The ARN of the service deployment.</p> <p>You can specify a maximum of 20 ARNs.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a service deployment
            This example describes a service deployment for the service sd-example in the example cluster.

            >>> await client.describe_service_deployments(service_deployment_arns=['arn:aws:ecs:us-west-2:123456789012:service-deployment/example/sd-example/NCWGC2ZR-taawPAYrIaU5'])
            To describe a service deployment with a paused lifecycle hook
            This example describes a service deployment that is currently paused at a lifecycle hook. The lifecycleHookDetails field shows the status of the pause hook, including when it will expire and what action will be taken if the timeout is reached.

            >>> await client.describe_service_deployments(service_deployment_arns=['arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_deployments

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_deployments.async_describe_service_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest = {
            "service_deployment_arns": service_deployment_arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service_primary_task_set(
        self,
        cluster: "capo_ecs.types.string.String",
        service: "capo_ecs.types.string.String",
        primary_task_set: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.update_service_primary_task_set_response.UpdateServicePrimaryTaskSetResponse":
        """<p>Modifies which task set in a service is the primary task set. Any parameters that are updated on the primary task set in a service will transition to the service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS Deployment Types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that the task set exists in.</p>
            primary_task_set: <p>The short name or full Amazon Resource Name (ARN) of the task set to set as the primary task set in the deployment.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.task_set_not_found_exception.TaskSetNotFoundException: <p>The specified task set wasn't found. You can view your available task sets with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskSets.html">DescribeTaskSets</a>. Task sets are specific to each cluster, service and Region.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update the primary task set for a service
            This example updates the primary task set for a service MyService that uses the EXTERNAL deployment controller type.

            >>> await client.update_service_primary_task_set(cluster='MyCluster', service='MyService', primary_task_set='arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_service_primary_task_set_request.UpdateServicePrimaryTaskSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_service_primary_task_set_response.UpdateServicePrimaryTaskSetResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service_primary_task_set

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service_primary_task_set.async_update_service_primary_task_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.update_service_primary_task_set_request.UpdateServicePrimaryTaskSetRequest = {
            "cluster": cluster,
            "service": service,
            "primary_task_set": primary_task_set,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_express_gateway_service(
        self,
        infrastructure_role_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        service_name: Optional["capo_ecs.types.string.String"] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        health_check_path: Optional["capo_ecs.types.string.String"] = None,
        primary_container: Optional[
            "capo_ecs.types.express_gateway_container.ExpressGatewayContainer"
        ] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "capo_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
        ] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        cpu_architecture: Optional[
            "capo_ecs.types.express_cpu_architecture.ExpressCpuArchitecture"
        ] = None,
        scaling_target: Optional[
            "capo_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        task_definition_arn: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.create_express_gateway_service_response.CreateExpressGatewayServiceResponse":
        """<p>Creates an Express service that simplifies deploying containerized web applications on Amazon ECS with managed Amazon Web Services infrastructure. This operation provisions and configures Application Load Balancers, target groups, security groups, and auto-scaling policies automatically.</p> <p>Specify a primary container configuration with your application image and basic settings. Amazon ECS creates the necessary Amazon Web Services resources for traffic distribution, health monitoring, network access control, and capacity management.</p> <p>Provide an execution role for task operations and an infrastructure role for managing Amazon Web Services resources on your behalf.</p>

        Args:
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. This role is required for Amazon ECS to pull container images from Amazon ECR, send container logs to Amazon CloudWatch Logs, and retrieve sensitive data from Amazon Web Services Systems Manager Parameter Store or Amazon Web Services Secrets Manager.</p> <p>The execution role must include the <code>AmazonECSTaskExecutionRolePolicy</code> managed policy or equivalent permissions. For Express services, this role is used during task startup and runtime for container management operations.</p>
            infrastructure_role_arn: <p>The Amazon Resource Name (ARN) of the infrastructure role that grants Amazon ECS permission to create and manage Amazon Web Services resources on your behalf for the Express service. This role is used to provision and manage Application Load Balancers, target groups, security groups, auto-scaling policies, and other Amazon Web Services infrastructure components.</p> <p>The infrastructure role must include permissions for Elastic Load Balancing, Application Auto Scaling, Amazon EC2 (for security groups), and other services required for managed infrastructure. This role is only used during Express service creation, updates, and deletion operations.</p>
            service_name: <p>The name of the Express service. This name must be unique within the specified cluster and can contain up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens. The name is used to identify the service in the Amazon ECS console and API operations.</p> <p>If you don't specify a service name, Amazon ECS generates a unique name for the service. The service name becomes part of the service ARN and cannot be changed after the service is created.</p>
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster on which to create the Express service. If you do not specify a cluster, the <code>default</code> cluster is assumed.</p>
            health_check_path: <p>The path on the container that the Application Load Balancer uses for health checks. This should be a valid HTTP endpoint that returns a successful response (HTTP 200) when the application is healthy.</p> <p>If not specified, the default health check path is <code>/ping</code>. The health check path must start with a forward slash and can include query parameters. Examples: <code>/health</code>, <code>/api/status</code>, <code>/ping?format=json</code>.</p>
            primary_container: <p>The primary container configuration for the Express service. This defines the main application container that will receive traffic from the Application Load Balancer.</p> <p>The primary container must specify at minimum a container image. You can also configure the container port (defaults to 80), logging configuration, environment variables, secrets, and startup commands. The container image can be from Amazon ECR, Docker Hub, or any other container registry accessible to your execution role.</p>
            task_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. This role allows your application code to access other Amazon Web Services services securely.</p> <p>The task role is different from the execution role. While the execution role is used by the Amazon ECS agent to set up the task, the task role is used by your application code running inside the container to make Amazon Web Services API calls. If your application doesn't need to access Amazon Web Services services, you can omit this parameter.</p>
            network_configuration: <p>The network configuration for the Express service tasks. This specifies the VPC subnets and security groups for the tasks.</p> <p>For Express services, you can specify custom security groups and subnets. If not provided, Amazon ECS will use the default VPC configuration and create appropriate security groups automatically. The network configuration determines how your service integrates with your VPC and what network access it has.</p>
            cpu: <p>The number of CPU units used by the task. This parameter determines the CPU allocation for each task in the Express service. The default value for an Express service is 256 (.25 vCPU).</p>
            memory: <p>The amount of memory (in MiB) used by the task. This parameter determines the memory allocation for each task in the Express service. The default value for an express service is 512 MiB.</p>
            cpu_architecture: <p>The CPU architecture that the tasks in the Express service run on. Amazon ECS applies this value to the task definition revision that it registers for the service. If you don't specify a value, the default is <code>X86_64</code>.</p> <p>Valid values:</p> <ul> <li> <p> <code>X86_64</code> - The x86 64-bit architecture.</p> </li> <li> <p> <code>ARM64</code> - The 64-bit ARM architecture.</p> </li> </ul> <p>Make sure that the container image that you specify supports the architecture that you choose. The operating system family for an Express service is always <code>LINUX</code>.</p> <p>You can't specify <code>cpuArchitecture</code> when you also specify <code>taskDefinitionArn</code>, because this value applies only to a task definition that Amazon ECS registers on your behalf.</p>
            scaling_target: <p>The auto-scaling configuration for the Express service. This defines how the service automatically adjusts the number of running tasks based on demand.</p> <p>You can specify the minimum and maximum number of tasks, the scaling metric (CPU utilization, memory utilization, or request count per target), and the target value for the metric. If not specified, the default target value for an Express service is 60.</p>
            tags: <p>The metadata that you apply to the Express service to help categorize and organize it. Each tag consists of a key and an optional value. You can apply up to 50 tags to a service.</p>
            task_definition_arn: <p>The Amazon Resource Name (ARN) of a task definition to use to create the Express Gateway service. This allows you to manage your own task definition, giving you more control over the service configuration such as adding sidecar containers.</p> <p>The task definition must have a container named <code>Main</code> with a single TCP port mapping that includes a container port and port name. The task definition must also have <code>FARGATE</code> compatibility.</p> <p>If you provide a task definition ARN, you cannot also specify <code>primaryContainer</code>, <code>executionRoleArn</code>, <code>taskRoleArn</code>, <code>cpu</code>, <code>memory</code>, or <code>cpuArchitecture</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.create_express_gateway_service_request.CreateExpressGatewayServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.create_express_gateway_service_response.CreateExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_express_gateway_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.create_express_gateway_service.async_create_express_gateway_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.create_express_gateway_service_request.CreateExpressGatewayServiceRequest = {
            "infrastructure_role_arn": infrastructure_role_arn
        }
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if service_name is not None:
            input_["service_name"] = service_name
        if cluster is not None:
            input_["cluster"] = cluster
        if health_check_path is not None:
            input_["health_check_path"] = health_check_path
        if primary_container is not None:
            input_["primary_container"] = primary_container
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if cpu_architecture is not None:
            input_["cpu_architecture"] = cpu_architecture
        if scaling_target is not None:
            input_["scaling_target"] = scaling_target
        if tags is not None:
            input_["tags"] = tags
        if task_definition_arn is not None:
            input_["task_definition_arn"] = task_definition_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_service(
        self,
        service_name: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        task_definition: Optional["capo_ecs.types.string.String"] = None,
        availability_zone_rebalancing: Optional[
            "capo_ecs.types.availability_zone_rebalancing.AvailabilityZoneRebalancing"
        ] = None,
        load_balancers: Optional["capo_ecs.types.load_balancers.LoadBalancers"] = None,
        service_registries: Optional[
            "capo_ecs.types.service_registries.ServiceRegistries"
        ] = None,
        desired_count: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        platform_version: Optional["capo_ecs.types.string.String"] = None,
        role: Optional["capo_ecs.types.string.String"] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.deployment_configuration.DeploymentConfiguration"
        ] = None,
        placement_constraints: Optional[
            "capo_ecs.types.placement_constraints.PlacementConstraints"
        ] = None,
        placement_strategy: Optional[
            "capo_ecs.types.placement_strategies.PlacementStrategies"
        ] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        health_check_grace_period_seconds: Optional[
            "capo_ecs.types.boxed_integer.BoxedInteger"
        ] = None,
        scheduling_strategy: Optional[
            "capo_ecs.types.scheduling_strategy.SchedulingStrategy"
        ] = None,
        deployment_controller: Optional[
            "capo_ecs.types.deployment_controller.DeploymentController"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        service_connect_configuration: Optional[
            "capo_ecs.types.service_connect_configuration.ServiceConnectConfiguration"
        ] = None,
        volume_configurations: Optional[
            "capo_ecs.types.service_volume_configurations.ServiceVolumeConfigurations"
        ] = None,
        vpc_lattice_configurations: Optional[
            "capo_ecs.types.vpc_lattice_configurations.VpcLatticeConfigurations"
        ] = None,
        monitoring: Optional[
            "capo_ecs.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
    ) -> "capo_ecs.types.create_service_response.CreateServiceResponse":
        """<p>Runs and maintains your desired number of tasks from a specified task definition. If the number of tasks running in a service drops below the <code>desiredCount</code>, Amazon ECS runs another copy of the task in the specified cluster. To update an existing service, use <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a>.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <note> <p>Amazon Elastic Inference (EI) is no longer available to customers.</p> </note> <p>In addition to maintaining the desired count of tasks in your service, you can optionally run your service behind one or more load balancers. The load balancers distribute traffic across the tasks that are associated with the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html">Service load balancing</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. <code>volumeConfigurations</code> is only supported for REPLICA service and not DAEMON service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Tasks for services that don't use a load balancer are considered healthy if they're in the <code>RUNNING</code> state. Tasks for services that use a load balancer are considered healthy if they're in the <code>RUNNING</code> state and are reported as healthy by the load balancer.</p> <p>There are two service scheduler strategies available:</p> <ul> <li> <p> <code>REPLICA</code> - The replica scheduling strategy places and maintains your desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Service scheduler concepts</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>DAEMON</code> - The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks. It also stops tasks that don't meet the placement constraints. When using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Amazon ECS services</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> </ul> <p>The deployment controller is the mechanism that determines how tasks are deployed for your service. The valid options are:</p> <ul> <li> <p>ECS</p> <p> When you create a service which uses the <code>ECS</code> deployment controller, you can choose between the following deployment strategies (which you can set in the “<code>strategy</code>” field in “<code>deploymentConfiguration</code>”): :</p> <ul> <li> <p> <code>ROLLING</code>: When you create a service which uses the <i>rolling update</i> (<code>ROLLING</code>) deployment strategy, the Amazon ECS service scheduler replaces the currently running tasks with new tasks. The number of tasks that Amazon ECS adds or removes from the service during a rolling update is controlled by the service deployment configuration. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html">Deploy Amazon ECS services by replacing tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Rolling update deployments are best suited for the following scenarios:</p> <ul> <li> <p>Gradual service updates: You need to update your service incrementally without taking the entire service offline at once.</p> </li> <li> <p>Limited resource requirements: You want to avoid the additional resource costs of running two complete environments simultaneously (as required by blue/green deployments).</p> </li> <li> <p>Acceptable deployment time: Your application can tolerate a longer deployment process, as rolling updates replace tasks one by one.</p> </li> <li> <p>No need for instant roll back: Your service can tolerate a rollback process that takes minutes rather than seconds.</p> </li> <li> <p>Simple deployment process: You prefer a straightforward deployment approach without the complexity of managing multiple environments, target groups, and listeners.</p> </li> <li> <p>No load balancer requirement: Your service doesn't use or require a load balancer, Application Load Balancer, Network Load Balancer, or Service Connect (which are required for blue/green deployments).</p> </li> <li> <p>Stateful applications: Your application maintains state that makes it difficult to run two parallel environments.</p> </li> <li> <p>Cost sensitivity: You want to minimize deployment costs by not running duplicate environments during deployment.</p> </li> </ul> <p>Rolling updates are the default deployment strategy for services and provide a balance between deployment safety and resource efficiency for many common application scenarios.</p> </li> <li> <p> <code>BLUE_GREEN</code>: A <i>blue/green</i> deployment strategy (<code>BLUE_GREEN</code>) is a release methodology that reduces downtime and risk by running two identical production environments called blue and green. With Amazon ECS blue/green deployments, you can validate new service revisions before directing production traffic to them. This approach provides a safer way to deploy changes with the ability to quickly roll back if needed. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html">Amazon ECS blue/green deployments</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Amazon ECS blue/green deployments are best suited for the following scenarios:</p> <ul> <li> <p>Service validation: When you need to validate new service revisions before directing production traffic to them</p> </li> <li> <p>Zero downtime: When your service requires zero-downtime deployments</p> </li> <li> <p>Instant roll back: When you need the ability to quickly roll back if issues are detected</p> </li> <li> <p>Load balancer requirement: When your service uses Application Load Balancer, Network Load Balancer, or Service Connect</p> </li> </ul> </li> <li> <p> <code>LINEAR</code>: A <i>linear</i> deployment strategy (<code>LINEAR</code>) gradually shifts traffic from the current production environment to a new environment in equal percentage increments. With Amazon ECS linear deployments, you can control the pace of traffic shifting and validate new service revisions with increasing amounts of production traffic.</p> <p>Linear deployments are best suited for the following scenarios:</p> <ul> <li> <p>Gradual validation: When you want to gradually validate your new service version with increasing traffic</p> </li> <li> <p>Performance monitoring: When you need time to monitor metrics and performance during the deployment</p> </li> <li> <p>Risk minimization: When you want to minimize risk by exposing the new version to production traffic incrementally</p> </li> <li> <p>Load balancer requirement: When your service uses Application Load Balancer or Service Connect</p> </li> </ul> </li> <li> <p> <code>CANARY</code>: A <i>canary</i> deployment strategy (<code>CANARY</code>) shifts a small percentage of traffic to the new service revision first, then shifts the remaining traffic all at once after a specified time period. This allows you to test the new version with a subset of users before full deployment.</p> <p>Canary deployments are best suited for the following scenarios:</p> <ul> <li> <p>Feature testing: When you want to test new features with a small subset of users before full rollout</p> </li> <li> <p>Production validation: When you need to validate performance and functionality with real production traffic</p> </li> <li> <p>Blast radius control: When you want to minimize blast radius if issues are discovered in the new version</p> </li> <li> <p>Load balancer requirement: When your service uses Application Load Balancer or Service Connect</p> </li> </ul> </li> </ul> </li> <li> <p>External</p> <p>Use a third-party deployment controller.</p> </li> <li> <p>Blue/green deployment (powered by CodeDeploy)</p> <p>CodeDeploy installs an updated version of the application as a new replacement task set and reroutes production traffic from the original application task set to the replacement task set. The original task set is terminated after a successful deployment. Use this deployment controller to verify a new deployment of a service before sending production traffic to it.</p> </li> </ul> <p>When creating a service that uses the <code>EXTERNAL</code> deployment controller, you can specify only parameters that aren't controlled at the task set level. The only required parameter is the service name. You control your services using the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html">CreateTaskSet</a>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS deployment types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>When the service scheduler launches new tasks, it determines task placement. For information about task placement and task placement strategies, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement.html">Amazon ECS task placement</a> in the <i>Amazon Elastic Container Service Developer Guide</i> </p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed.</p>
            service_name: <p>The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.</p>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run in your service. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p> <p>A task definition must be specified if the service uses either the <code>ECS</code> or <code>CODE_DEPLOY</code> deployment controllers.</p> <p>For more information about deployment types, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS deployment types</a>.</p>
            availability_zone_rebalancing: <p>Indicates whether to use Availability Zone rebalancing for the service.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html">Balancing an Amazon ECS service across Availability Zones</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <p>The default behavior of <code>AvailabilityZoneRebalancing</code> differs between create and update requests:</p> <ul> <li> <p>For create service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults the value to <code>ENABLED</code>.</p> </li> <li> <p>For update service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults to the existing service’s <code>AvailabilityZoneRebalancing</code> value. If the service never had an <code>AvailabilityZoneRebalancing</code> value set, Amazon ECS treats this as <code>DISABLED</code>.</p> </li> </ul>
            load_balancers: <p>A load balancer object representing the load balancers to use with your service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html">Service load balancing</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the service uses the <code>ECS</code> deployment controller and using either an Application Load Balancer or Network Load Balancer, you must specify one or more target group ARNs to attach to the service. The service-linked role is required for services that use multiple target groups. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the service uses the <code>CODE_DEPLOY</code> deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When creating an CodeDeploy deployment group, you specify two target groups (referred to as a <code>targetGroupPair</code>). During a deployment, CodeDeploy determines which task set in your service has the status <code>PRIMARY</code>, and it associates one target group with it. Then, it also associates the other target group with the replacement task set. The load balancer can also have up to two listeners: a required listener for production traffic and an optional listener that you can use to perform validation tests with Lambda functions before routing production traffic to it.</p> <p>If you use the <code>CODE_DEPLOY</code> deployment controller, these values can be changed when updating the service.</p> <p>For Application Load Balancers and Network Load Balancers, this object must contain the load balancer target group ARN, the container name, and the container port to access from the load balancer. The container name must be as it appears in a container definition. The load balancer name parameter must be omitted. When a task from this service is placed on a container instance, the container instance and port combination is registered as a target in the target group that's specified here.</p> <p>For Classic Load Balancers, this object must contain the load balancer name, the container name , and the container port to access from the load balancer. The container name must be as it appears in a container definition. The target group ARN parameter must be omitted. When a task from this service is placed on a container instance, the container instance is registered with the load balancer that's specified here.</p> <p>Services with tasks that use the <code>awsvpc</code> network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers aren't supported. Also, when you create any target groups for these services, you must choose <code>ip</code> as the target type, not <code>instance</code>. This is because tasks that use the <code>awsvpc</code> network mode are associated with an elastic network interface, not an Amazon EC2 instance.</p>
            service_registries: <p>The details of the service discovery registry to associate with this service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html">Service discovery</a>.</p> <note> <p>Each service may be associated with one service registry. Multiple service registries for each service isn't supported.</p> </note>
            desired_count: <p>The number of instantiations of the specified task definition to place and keep running in your service.</p> <p>This is required if <code>schedulingStrategy</code> is <code>REPLICA</code> or isn't specified. If <code>schedulingStrategy</code> is <code>DAEMON</code> then this isn't required.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>
            launch_type: <p>The infrastructure that you run your service on. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>The <code>FARGATE</code> launch type runs your tasks on Fargate On-Demand infrastructure.</p> <note> <p>Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html">Fargate capacity providers</a> in the <i>Amazon ECS Developer Guide</i>.</p> </note> <p>The <code>EC2</code> launch type runs your tasks on Amazon EC2 instances registered to your cluster.</p> <p>The <code>EXTERNAL</code> launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.</p> <p>A service can use either a launch type or a capacity provider strategy. If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p>
            capacity_provider_strategy: <p>The capacity provider strategy to use for the service.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>A capacity provider strategy can contain a maximum of 20 capacity providers.</p>
            platform_version: <p>The platform version that your tasks in the service are running on. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            role: <p>The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition doesn't use the <code>awsvpc</code> network mode. If you specify the <code>role</code> parameter, you must also specify a load balancer object with the <code>loadBalancers</code> parameter.</p> <important> <p>If your account has already created the Amazon ECS service-linked role, that role is used for your service unless you specify a role here. The service-linked role is required if your task definition uses the <code>awsvpc</code> network mode or if the service is configured to use service discovery, an external deployment controller, multiple target groups, or Elastic Inference accelerators in which case you don't specify a role here. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </important> <p>If your specified role has a path other than <code>/</code>, then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name <code>bar</code> has a path of <code>/foo/</code> then you would specify <code>/foo/bar</code> as the role name. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names">Friendly names and paths</a> in the <i>IAM User Guide</i>.</p>
            deployment_configuration: <p>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</p>
            placement_constraints: <p>An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p>
            placement_strategy: <p>The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules for each service.</p>
            network_configuration: <p>The network configuration for the service. This parameter is required for task definitions that use the <code>awsvpc</code> network mode to receive their own elastic network interface, and it isn't supported for other network modes. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            health_check_grace_period_seconds: <p>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you do not specify a health check grace period value, the default value of 0 is used. If you do not use any of the health checks, then <code>healthCheckGracePeriodSeconds</code> is unused.</p> <p>If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.</p>
            scheduling_strategy: <p>The scheduling strategy to use for the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Services</a>.</p> <p>There are two service scheduler strategies available:</p> <ul> <li> <p> <code>REPLICA</code>-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if the service uses the <code>CODE_DEPLOY</code> or <code>EXTERNAL</code> deployment controller types.</p> </li> <li> <p> <code>DAEMON</code>-The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks and will stop tasks that don't meet the placement constraints. When you're using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.</p> <note> <p>Tasks using the Fargate launch type or the <code>CODE_DEPLOY</code> or <code>EXTERNAL</code> deployment controller types don't support the <code>DAEMON</code> scheduling strategy.</p> </note> </li> </ul>
            deployment_controller: <p>The deployment controller to use for the service. If no deployment controller is specified, the default value of <code>ECS</code> is used.</p>
            tags: <p>The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            enable_ecs_managed_tags: <p>Specifies whether to turn on Amazon ECS managed tags for the tasks within the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>When you use Amazon ECS managed tags, you must set the <code>propagateTags</code> request parameter.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html">TagResource</a> API action.</p> <p>You must set this to a value other than <code>NONE</code> when you use Cost Explorer. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/usage-reports.html">Amazon ECS usage reports</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>The default is <code>NONE</code>.</p>
            enable_execute_command: <p>Determines whether the execute command functionality is turned on for the service. If <code>true</code>, this enables execute command functionality on all containers in the service tasks.</p>
            service_connect_configuration: <p>The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            volume_configurations: <p>The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.</p>
            vpc_lattice_configurations: <p>The VPC Lattice configuration for the service being created.</p>
            monitoring: <p>The optional monitoring configuration for the service, which defines the resolution for the service-level <code>CPUUtilization</code> and <code>MemoryUtilization</code> Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of <code>60</code> seconds.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new service
            This example creates a service in your default region called ``ecs-simple-service``. The service uses the ``hello_world`` task definition and it maintains 10 copies of that task.

            >>> await client.create_service(service_name='ecs-simple-service', task_definition='hello_world', desired_count=10)
            To create a new service behind a load balancer
            This example creates a service in your default region called ``ecs-simple-service-elb``. The service uses the ``ecs-demo`` task definition and it maintains 10 copies of that task. You must reference an existing load balancer in the same region by its name.

            >>> await client.create_service(load_balancers=[{'containerName': 'simple-app', 'containerPort': 80, 'loadBalancerName': 'EC2Contai-EcsElast-15DCDAURT3ZO2'}], service_name='ecs-simple-service-elb', role='ecsServiceRole', task_definition='console-sample-app-static', desired_count=10)
            To create a service with a pause lifecycle hook
            This example creates a service with a blue/green deployment strategy that includes a pause lifecycle hook at the POST_PRODUCTION_TRAFFIC_SHIFT stage. The deployment will pause at that stage until you explicitly continue or roll back using the ContinueServiceDeployment API, or until the 60-minute timeout expires and triggers a rollback.

            >>> await client.create_service(service_name='ecs-service-with-pause-hook', task_definition='ecs-demo', desired_count=2, deployment_configuration={'strategy': 'BLUE_GREEN', 'lifecycleHooks': [{'targetType': 'PAUSE', 'lifecycleStages': ['POST_PRODUCTION_TRAFFIC_SHIFT'], 'timeoutConfiguration': {'timeoutInMinutes': 60, 'action': 'ROLLBACK'}}]})
            To create a service with a monitoring configuration
            This example creates a service with a monitoring configuration that sets 20-second resolution for CPUUtilization and MemoryUtilization CloudWatch metrics. The monitoring configuration is not returned in the CreateService response. Use DescribeServiceRevisions to view the monitoring configuration.

            >>> await client.create_service(service_name='ecs-monitored-service', task_definition='my-app:1', desired_count=2, monitoring={'metricConfigurations': [{'metricNames': ['CPUUtilization', 'MemoryUtilization'], 'resolutionSeconds': 20}]})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.create_service_request.CreateServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.create_service_response.CreateServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.create_service.async_create_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.create_service_request.CreateServiceRequest = {
            "service_name": service_name
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if task_definition is not None:
            input_["task_definition"] = task_definition
        if availability_zone_rebalancing is not None:
            input_["availability_zone_rebalancing"] = availability_zone_rebalancing
        if load_balancers is not None:
            input_["load_balancers"] = load_balancers
        if service_registries is not None:
            input_["service_registries"] = service_registries
        if desired_count is not None:
            input_["desired_count"] = desired_count
        if client_token is not None:
            input_["client_token"] = client_token
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if capacity_provider_strategy is not None:
            input_["capacity_provider_strategy"] = capacity_provider_strategy
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if role is not None:
            input_["role"] = role
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if placement_strategy is not None:
            input_["placement_strategy"] = placement_strategy
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if health_check_grace_period_seconds is not None:
            input_["health_check_grace_period_seconds"] = (
                health_check_grace_period_seconds
            )
        if scheduling_strategy is not None:
            input_["scheduling_strategy"] = scheduling_strategy
        if deployment_controller is not None:
            input_["deployment_controller"] = deployment_controller
        if tags is not None:
            input_["tags"] = tags
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if service_connect_configuration is not None:
            input_["service_connect_configuration"] = service_connect_configuration
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations
        if vpc_lattice_configurations is not None:
            input_["vpc_lattice_configurations"] = vpc_lattice_configurations
        if monitoring is not None:
            input_["monitoring"] = monitoring

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_express_gateway_service(
        self,
        service_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_express_gateway_service_response.DeleteExpressGatewayServiceResponse":
        """<p>Deletes an Express service and removes all associated Amazon Web Services resources. This operation stops service tasks, removes the Application Load Balancer, target groups, security groups, auto-scaling policies, and other managed infrastructure components.</p> <p>The service enters a <code>DRAINING</code> state where existing tasks complete current requests without starting new tasks. After all tasks stop, the service and infrastructure are permanently removed.</p> <p>This operation cannot be reversed. Back up important data and verify the service is no longer needed before deletion.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the Express service to delete. The ARN uniquely identifies the service within your Amazon Web Services account and region.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_express_gateway_service_request.DeleteExpressGatewayServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_express_gateway_service_response.DeleteExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_express_gateway_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_express_gateway_service.async_delete_express_gateway_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.delete_express_gateway_service_request.DeleteExpressGatewayServiceRequest = {
            "service_arn": service_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_service(
        self,
        service: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        force: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.delete_service_response.DeleteServiceResponse":
        """<p>Deletes a specified service within a cluster. You can delete a service if you have no running tasks in it and the desired task count is zero. If the service is actively maintaining tasks, you can't delete it, and you must update the service to a desired task count of zero. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a>.</p> <note> <p>When you delete a service, if there are still running tasks that require cleanup, the service status moves from <code>ACTIVE</code> to <code>DRAINING</code>, and the service is no longer visible in the console or in the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a> API operation. After all tasks have transitioned to either <code>STOPPING</code> or <code>STOPPED</code> status, the service status moves from <code>DRAINING</code> to <code>INACTIVE</code>. Services in the <code>DRAINING</code> or <code>INACTIVE</code> status can still be viewed with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html">DescribeServices</a> API operation. However, in the future, <code>INACTIVE</code> services may be cleaned up and purged from Amazon ECS record keeping, and <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html">DescribeServices</a> calls on those services return a <code>ServiceNotFoundException</code> error.</p> </note> <important> <p>If you attempt to create a new service with the same name as an existing service in either <code>ACTIVE</code> or <code>DRAINING</code> status, you receive an error.</p> </important>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to delete. If you do not specify a cluster, the default cluster is assumed.</p>
            service: <p>The name of the service to delete.</p>
            force: <p>If <code>true</code>, allows you to delete a service even if it wasn't scaled down to zero tasks. It's only necessary to use this if the service uses the <code>REPLICA</code> scheduling strategy.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a service
            This example deletes the my-http-service service. The service must have a desired count and running count of 0 before you can delete it.

            >>> await client.delete_service(service='my-http-service')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_service_request.DeleteServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_service_response.DeleteServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_service.async_delete_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.delete_service_request.DeleteServiceRequest = {
            "service": service
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_express_gateway_service(
        self,
        service_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        include: Optional[
            "capo_ecs.types.express_gateway_service_include_list.ExpressGatewayServiceIncludeList"
        ] = None,
    ) -> "capo_ecs.types.describe_express_gateway_service_response.DescribeExpressGatewayServiceResponse":
        """<p>Retrieves detailed information about an Express service, including current status, configuration, managed infrastructure, and service revisions.</p> <p>Returns comprehensive service details, active service revisions, ingress paths with endpoints, and managed Amazon Web Services resource status including load balancers and auto-scaling policies.</p> <p>Use the <code>include</code> parameter to retrieve additional information such as resource tags.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the Express service to describe. The ARN uniquely identifies the service within your Amazon Web Services account and region.</p>
            include: <p>Specifies additional information to include in the response. Valid values are <code>TAGS</code> to include resource tags associated with the Express service.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_express_gateway_service_request.DescribeExpressGatewayServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_express_gateway_service_response.DescribeExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_express_gateway_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_express_gateway_service.async_describe_express_gateway_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_express_gateway_service_request.DescribeExpressGatewayServiceRequest = {
            "service_arn": service_arn
        }
        if include is not None:
            input_["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_services(
        self,
        services: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        include: Optional["capo_ecs.types.service_field_list.ServiceFieldList"] = None,
    ) -> "capo_ecs.types.describe_services_response.DescribeServicesResponse":
        """<p>Describes the specified services running in your cluster.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the service or services you are describing were launched in any cluster other than the default cluster.</p>
            services: <p>A list of services to describe. You may specify up to 10 services to describe in a single operation.</p>
            include: <p>Determines whether you want to see the resource tags for the service. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a service
            This example provides descriptive information about the service named ``ecs-simple-service``.

            >>> await client.describe_services(services=['ecs-simple-service'])
            To describe a service with a pause lifecycle hook
            This example provides descriptive information about the service ``ecs-service-with-pause-hook``, which is configured with a pause lifecycle hook in its deployment configuration.

            >>> await client.describe_services(services=['ecs-service-with-pause-hook'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_services_request.DescribeServicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_services_response.DescribeServicesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_services

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_services.async_describe_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_services_request.DescribeServicesRequest = {
            "services": services
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if include is not None:
            input_["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_service_deployments(
        self,
        service: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.service_deployment_status_list.ServiceDeploymentStatusList"
        ] = None,
        created_at: Optional["capo_ecs.types.created_at.CreatedAt"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_service_deployments_response.ListServiceDeploymentsResponse":
        """<p>This operation lists all the service deployments that meet the specified filter criteria.</p> <p>A service deployment happens when you release a software update for the service. You route traffic from the running service revisions to the new service revison and control the number of running tasks. </p> <p>This API returns the values that you use for the request parameters in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceRevisions.html">DescribeServiceRevisions</a>.</p>

        Args:
            service: <p>The ARN or name of the service</p>
            cluster: <p>The cluster that hosts the service. This can either be the cluster name or ARN. Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. If you don't specify a cluster, <code>default</code> is used.</p>
            status: <p>An optional filter you can use to narrow the results. If you do not specify a status, then all status values are included in the result.</p>
            created_at: <p>An optional filter you can use to narrow the results by the service creation date. If you do not specify a value, the result includes all services created before the current time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListServiceDeployments</code> request indicating that more results are available to fulfill the request and further calls are needed. If you provided <code>maxResults</code>, it's possible the number of results is fewer than <code>maxResults</code>.</p>
            max_results: <p>The maximum number of service deployment results that <code>ListServiceDeployments</code> returned in paginated output. When this parameter is used, <code>ListServiceDeployments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServiceDeployments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServiceDeployments</code> returns up to 20 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list service deployments that meet the specified criteria
            This example lists all successful service deployments for the service "sd-example" in the cluster "example".

            >>> await client.list_service_deployments(service='sd-example', cluster='example', status=['SUCCESSFUL'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_service_deployments_request.ListServiceDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_service_deployments_response.ListServiceDeploymentsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_service_deployments

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_service_deployments.async_list_service_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_service_deployments_request.ListServiceDeploymentsRequest = {
            "service": service
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if status is not None:
            input_["status"] = status
        if created_at is not None:
            input_["created_at"] = created_at
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

    async def list_services(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        scheduling_strategy: Optional[
            "capo_ecs.types.scheduling_strategy.SchedulingStrategy"
        ] = None,
        resource_management_type: Optional[
            "capo_ecs.types.resource_management_type.ResourceManagementType"
        ] = None,
    ) -> "capo_ecs.types.list_services_response.ListServicesResponse":
        """<p>Returns a list of services. You can filter the results by cluster, launch type, and scheduling strategy.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the <code>ListServices</code> results. If you do not specify a cluster, the default cluster is assumed.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListServices</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it is possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of service results that <code>ListServices</code> returned in paginated output. When this parameter is used, <code>ListServices</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServices</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServices</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>
            launch_type: <p>The launch type to use when filtering the <code>ListServices</code> results.</p>
            scheduling_strategy: <p>The scheduling strategy to use when filtering the <code>ListServices</code> results.</p>
            resource_management_type: <p>The resourceManagementType type to use when filtering the <code>ListServices</code> results.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the services in a cluster
            This example lists the services running in the default cluster for an account.

            >>> await client.list_services()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_services_request.ListServicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_services_response.ListServicesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_services

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_services.async_list_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_services_request.ListServicesRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if scheduling_strategy is not None:
            input_["scheduling_strategy"] = scheduling_strategy
        if resource_management_type is not None:
            input_["resource_management_type"] = resource_management_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_services(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        scheduling_strategy: Optional[
            "capo_ecs.types.scheduling_strategy.SchedulingStrategy"
        ] = None,
        resource_management_type: Optional[
            "capo_ecs.types.resource_management_type.ResourceManagementType"
        ] = None,
    ) -> "AsyncIterator[capo_ecs.types.string.String]":
        _token = next_token
        while True:
            _response = await self.list_services(
                config_overrides=config_overrides,
                cluster=cluster,
                next_token=_token,
                max_results=max_results,
                launch_type=launch_type,
                scheduling_strategy=scheduling_strategy,
                resource_management_type=resource_management_type,
            )
            _page = _resolve_path(_response, ("service_arns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def stop_service_deployment(
        self,
        service_deployment_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        stop_type: Optional[
            "capo_ecs.types.stop_service_deployment_stop_type.StopServiceDeploymentStopType"
        ] = None,
    ) -> (
        "capo_ecs.types.stop_service_deployment_response.StopServiceDeploymentResponse"
    ):
        """<p>Stops an ongoing service deployment.</p> <p>The following stop types are avaiable:</p> <ul> <li> <p>ROLLBACK - This option rolls back the service deployment to the previous service revision. </p> <p>You can use this option even if you didn't configure the service deployment for the rollback option. </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stop-service-deployment.html">Stopping Amazon ECS service deployments</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            service_deployment_arn: <p>The ARN of the service deployment that you want to stop.</p>
            stop_type: <p>How you want Amazon ECS to stop the service. </p> <p>The valid values are <code>ROLLBACK</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. </p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_deployment_not_found_exception.ServiceDeploymentNotFoundException: <p>The service deploy ARN that you specified in the <code>ContinueServiceDeployment</code> doesn't exist. You can use <code>ListServiceDeployments</code> to retrieve the service deployment ARNs.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To stop a service deployment
            This example stops the service deployment using the ROLLBACK option.

            >>> await client.stop_service_deployment(service_deployment_arn='arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r', stop_type='ROLLBACK')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.stop_service_deployment_request.StopServiceDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.stop_service_deployment_response.StopServiceDeploymentResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_service_deployment

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_service_deployment.async_stop_service_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.stop_service_deployment_request.StopServiceDeploymentRequest = {
            "service_deployment_arn": service_deployment_arn
        }
        if stop_type is not None:
            input_["stop_type"] = stop_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_express_gateway_service(
        self,
        service_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        health_check_path: Optional["capo_ecs.types.string.String"] = None,
        primary_container: Optional[
            "capo_ecs.types.express_gateway_container.ExpressGatewayContainer"
        ] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "capo_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
        ] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        cpu_architecture: Optional[
            "capo_ecs.types.express_cpu_architecture.ExpressCpuArchitecture"
        ] = None,
        scaling_target: Optional[
            "capo_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
        ] = None,
        task_definition_arn: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.update_express_gateway_service_response.UpdateExpressGatewayServiceResponse":
        """<p>Updates an existing Express service configuration. Modifies container settings, resource allocation, auto-scaling configuration, and other service parameters without recreating the service.</p> <p>Amazon ECS creates a new service revision with updated configuration and performs a rolling deployment to replace existing tasks. The service remains available during updates, ensuring zero-downtime deployments.</p> <p>Some parameters like the infrastructure role cannot be modified after service creation and require creating a new service.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the Express service to update.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role for the Express service.</p>
            health_check_path: <p>The path on the container for Application Load Balancer health checks.</p>
            primary_container: <p>The primary container configuration for the Express service.</p>
            task_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role for containers in this task.</p>
            network_configuration: <p>The network configuration for the Express service tasks. By default, the network configuration for an Express service uses the default VPC.</p>
            cpu: <p>The number of CPU units used by the task.</p>
            memory: <p>The amount of memory (in MiB) used by the task.</p>
            cpu_architecture: <p>The CPU architecture that the tasks in the Express service run on. Amazon ECS applies this value to the task definition revision that it registers for the service. If you don't specify a value, the service keeps the architecture that it currently runs on.</p> <p>Valid values:</p> <ul> <li> <p> <code>X86_64</code> - The x86 64-bit architecture.</p> </li> <li> <p> <code>ARM64</code> - The 64-bit ARM architecture.</p> </li> </ul> <p>Changing the architecture starts a new deployment that replaces the running tasks. Make sure that the container image that the service uses supports the architecture that you choose. The operating system family for an Express service is always <code>LINUX</code>.</p> <p>You can't specify <code>cpuArchitecture</code> when you also specify <code>taskDefinitionArn</code>, because this value applies only to a task definition that Amazon ECS registers on your behalf.</p>
            scaling_target: <p>The auto-scaling configuration for the Express service.</p>
            task_definition_arn: <p>The Amazon Resource Name (ARN) of a task definition to use to update the Express Gateway service. This allows you to manage your own task definition, giving you more control over the service configuration such as adding sidecar containers.</p> <p>The task definition must have a container named <code>Main</code> with a single TCP port mapping that includes a container port and port name. The task definition must also have <code>FARGATE</code> compatibility.</p> <p>If you provide a task definition ARN, you cannot also specify <code>primaryContainer</code>, <code>executionRoleArn</code>, <code>taskRoleArn</code>, <code>cpu</code>, <code>memory</code>, or <code>cpuArchitecture</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_express_gateway_service_request.UpdateExpressGatewayServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_express_gateway_service_response.UpdateExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_express_gateway_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_express_gateway_service.async_update_express_gateway_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.update_express_gateway_service_request.UpdateExpressGatewayServiceRequest = {
            "service_arn": service_arn
        }
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if health_check_path is not None:
            input_["health_check_path"] = health_check_path
        if primary_container is not None:
            input_["primary_container"] = primary_container
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if cpu_architecture is not None:
            input_["cpu_architecture"] = cpu_architecture
        if scaling_target is not None:
            input_["scaling_target"] = scaling_target
        if task_definition_arn is not None:
            input_["task_definition_arn"] = task_definition_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service(
        self,
        service: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        desired_count: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        task_definition: Optional["capo_ecs.types.string.String"] = None,
        capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.deployment_configuration.DeploymentConfiguration"
        ] = None,
        availability_zone_rebalancing: Optional[
            "capo_ecs.types.availability_zone_rebalancing.AvailabilityZoneRebalancing"
        ] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        placement_constraints: Optional[
            "capo_ecs.types.placement_constraints.PlacementConstraints"
        ] = None,
        placement_strategy: Optional[
            "capo_ecs.types.placement_strategies.PlacementStrategies"
        ] = None,
        platform_version: Optional["capo_ecs.types.string.String"] = None,
        force_new_deployment: Optional["capo_ecs.types.boolean.Boolean"] = None,
        health_check_grace_period_seconds: Optional[
            "capo_ecs.types.boxed_integer.BoxedInteger"
        ] = None,
        deployment_controller: Optional[
            "capo_ecs.types.deployment_controller.DeploymentController"
        ] = None,
        enable_execute_command: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
        enable_ecs_managed_tags: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
        load_balancers: Optional["capo_ecs.types.load_balancers.LoadBalancers"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        service_registries: Optional[
            "capo_ecs.types.service_registries.ServiceRegistries"
        ] = None,
        service_connect_configuration: Optional[
            "capo_ecs.types.service_connect_configuration.ServiceConnectConfiguration"
        ] = None,
        volume_configurations: Optional[
            "capo_ecs.types.service_volume_configurations.ServiceVolumeConfigurations"
        ] = None,
        vpc_lattice_configurations: Optional[
            "capo_ecs.types.vpc_lattice_configurations.VpcLatticeConfigurations"
        ] = None,
        monitoring: Optional[
            "capo_ecs.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
    ) -> "capo_ecs.types.update_service_response.UpdateServiceResponse":
        """<p>Modifies the parameters of a service.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <p>For services using the rolling update (<code>ECS</code>) you can update the desired count, deployment configuration, network configuration, load balancers, service registries, enable ECS managed tags option, propagate tags option, task placement constraints and strategies, and task definition. When you update any of these parameters, Amazon ECS starts new tasks with the new configuration. </p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when starting or running a task, or when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. You can update your volume configurations and trigger a new deployment. <code>volumeConfigurations</code> is only supported for REPLICA service and not DAEMON service. If you leave <code>volumeConfigurations</code> <code>null</code>, it doesn't trigger a new deployment. For more information on volumes, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>For services using the blue/green (<code>CODE_DEPLOY</code>) deployment controller, only the desired count, deployment configuration, health check grace period, task placement constraints and strategies, enable ECS managed tags option, and propagate tags can be updated using this API. If the network configuration, platform version, task definition, or load balancer need to be updated, create a new CodeDeploy deployment. For more information, see <a href="https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html">CreateDeployment</a> in the <i>CodeDeploy API Reference</i>.</p> <p>For services using an external deployment controller, you can update only the desired count, task placement constraints and strategies, health check grace period, enable ECS managed tags option, and propagate tags option, using this API. If the launch type, load balancer, network configuration, platform version, or task definition need to be updated, create a new task set For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html">CreateTaskSet</a>.</p> <p>You can add to or subtract from the number of instantiations of a task definition in a service by specifying the cluster that the service is running in and a new <code>desiredCount</code> parameter.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when starting or running a task, or when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If you have updated the container image of your application, you can create a new task definition with that image and deploy it to your service. The service scheduler uses the minimum healthy percent and maximum percent parameters (in the service's deployment configuration) to determine the deployment strategy.</p> <note> <p>If your updated Docker image uses the same tag as what is in the existing task definition for your service (for example, <code>my_image:latest</code>), you don't need to create a new revision of your task definition. You can update the service using the <code>forceNewDeployment</code> option. The new tasks launched by the deployment pull the current image/tag combination from your repository when they start.</p> </note> <p>You can also update the deployment configuration of a service. When a deployment is triggered by updating the task definition of a service, the service scheduler uses the deployment configuration parameters, <code>minimumHealthyPercent</code> and <code>maximumPercent</code>, to determine the deployment strategy.</p> <ul> <li> <p>If <code>minimumHealthyPercent</code> is below 100%, the scheduler can ignore <code>desiredCount</code> temporarily during a deployment. For example, if <code>desiredCount</code> is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. Tasks for services that don't use a load balancer are considered healthy if they're in the <code>RUNNING</code> state. Tasks for services that use a load balancer are considered healthy if they're in the <code>RUNNING</code> state and are reported as healthy by the load balancer.</p> </li> <li> <p>The <code>maximumPercent</code> parameter represents an upper limit on the number of running tasks during a deployment. You can use it to define the deployment batch size. For example, if <code>desiredCount</code> is four tasks, a maximum of 200% starts four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available).</p> </li> </ul> <p>When <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a> stops a task during a deployment, the equivalent of <code>docker stop</code> is issued to the containers running in the task. This results in a <code>SIGTERM</code> and a 30-second timeout. After this, <code>SIGKILL</code> is sent and the containers are forcibly stopped. If the container handles the <code>SIGTERM</code> gracefully and exits within 30 seconds from receiving it, no <code>SIGKILL</code> is sent.</p> <p>When the service scheduler launches new tasks, it determines task placement in your cluster with the following logic.</p> <ul> <li> <p>Determine which of the container instances in your cluster can support your service's task definition. For example, they have the required CPU, memory, ports, and container instance attributes.</p> </li> <li> <p>By default, the service scheduler attempts to balance tasks across Availability Zones in this manner even though you can choose a different placement strategy.</p> <ul> <li> <p>Sort the valid container instances by the fewest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement.</p> </li> <li> <p>Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service.</p> </li> </ul> </li> </ul> <p>When the service scheduler stops running tasks, it attempts to maintain balance across the Availability Zones in your cluster using the following logic: </p> <ul> <li> <p>Sort the container instances by the largest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have two, container instances in either zone B or C are considered optimal for termination.</p> </li> <li> <p>Stop the task on a container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the largest number of running tasks for this service.</p> </li> </ul>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that your service runs on. If you do not specify a cluster, the default cluster is assumed.</p> <p>You can't change the cluster name.</p>
            service: <p>The name of the service to update.</p>
            desired_count: <p>The number of instantiations of the task to place and keep running in your service.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run in your service. If a <code>revision</code> is not specified, the latest <code>ACTIVE</code> revision is used. If you modify the task definition with <code>UpdateService</code>, Amazon ECS spawns a task with the new version of the task definition and then stops an old task after the new version is running.</p> <p>This parameter triggers a new service deployment.</p>
            capacity_provider_strategy: <p>The details of a capacity provider strategy. You can set a capacity provider when you create a cluster, run a task, or update a service.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter.</p> </note> <p>When you use Fargate, the capacity providers are <code>FARGATE</code> or <code>FARGATE_SPOT</code>.</p> <p>When you use Amazon EC2, the capacity providers are Auto Scaling groups.</p> <p>You can change capacity providers for rolling deployments and blue/green deployments.</p> <p>The following list provides the valid transitions:</p> <ul> <li> <p>Update the Fargate launch type to an Auto Scaling group capacity provider.</p> </li> <li> <p>Update the Amazon EC2 launch type to a Fargate capacity provider.</p> </li> <li> <p>Update the Fargate capacity provider to an Auto Scaling group capacity provider.</p> </li> <li> <p>Update the Amazon EC2 capacity provider to a Fargate capacity provider. </p> </li> <li> <p>Update the Auto Scaling group or Fargate capacity provider back to the launch type.</p> <p>Pass an empty list in the <code>capacityProviderStrategy</code> parameter.</p> </li> </ul> <p>For information about Amazon Web Services CDK considerations, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-parameters.html">Amazon Web Services CDK considerations</a>.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            deployment_configuration: <p>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            availability_zone_rebalancing: <p>Indicates whether to use Availability Zone rebalancing for the service.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html">Balancing an Amazon ECS service across Availability Zones</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <p>The default behavior of <code>AvailabilityZoneRebalancing</code> differs between create and update requests:</p> <ul> <li> <p>For create service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults the value to <code>ENABLED</code>.</p> </li> <li> <p>For update service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults to the existing service’s <code>AvailabilityZoneRebalancing</code> value. If the service never had an <code>AvailabilityZoneRebalancing</code> value set, Amazon ECS treats this as <code>DISABLED</code>.</p> </li> </ul> <p>This parameter doesn't trigger a new service deployment.</p>
            network_configuration: <p>An object representing the network configuration for the service.</p> <p>This parameter triggers a new service deployment.</p>
            placement_constraints: <p>An array of task placement constraint objects to update the service to use. If no value is specified, the existing placement constraints for the service will remain unchanged. If this value is specified, it will override any existing placement constraints defined for the service. To remove all existing placement constraints, specify an empty array.</p> <p>You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            placement_strategy: <p>The task placement strategy objects to update the service to use. If no value is specified, the existing placement strategy for the service will remain unchanged. If this value is specified, it will override the existing placement strategy defined for the service. To remove an existing placement strategy, specify an empty object.</p> <p>You can specify a maximum of five strategy rules for each service.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            platform_version: <p>The platform version that your tasks in the service run on. A platform version is only specified for tasks using the Fargate launch type. If a platform version is not specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate Platform Versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>This parameter triggers a new service deployment.</p>
            force_new_deployment: <p>Determines whether to force a new deployment of the service. By default, deployments aren't forced. You can use this option to start a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (<code>my_image:latest</code>) or to roll Fargate tasks onto a newer platform version.</p>
            health_check_grace_period_seconds: <p>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you don't specify a health check grace period value, the default value of <code>0</code> is used. If you don't use any of the health checks, then <code>healthCheckGracePeriodSeconds</code> is unused.</p> <p>If your service's tasks take a while to start and respond to health checks, you can specify a health check grace period of up to 2,147,483,647 seconds (about 69 years). During that time, the Amazon ECS service scheduler ignores health check status. This grace period can prevent the service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.</p> <p>If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            enable_execute_command: <p>If <code>true</code>, this enables execute command functionality on all task containers.</p> <p>If you do not want to override the value that was set when the service was created, you can set this to <code>null</code> when performing this action.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            enable_ecs_managed_tags: <p>Determines whether to turn on Amazon ECS managed tags for the tasks in the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Only tasks launched after the update will reflect the update. To update the tags on all tasks, set <code>forceNewDeployment</code> to <code>true</code>, so that Amazon ECS starts new tasks with the updated tags.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            load_balancers: <note> <p>You must have a service-linked role when you update this property</p> </note> <p>A list of Elastic Load Balancing load balancer objects. It contains the load balancer name, the container name, and the container port to access from the load balancer. The container name is as it appears in a container definition.</p> <p>When you add, update, or remove a load balancer configuration, Amazon ECS starts new tasks with the updated Elastic Load Balancing configuration, and then stops the old tasks when the new tasks are running.</p> <p>For services that use rolling updates, you can add, update, or remove Elastic Load Balancing target groups. You can update from a single target group to multiple target groups and from multiple target groups to a single target group.</p> <p>For services that use blue/green deployments, you can update Elastic Load Balancing target groups by using <code> <a href="https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html">CreateDeployment</a> </code> through CodeDeploy. Note that multiple target groups are not supported for blue/green deployments. For more information see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html">Register multiple target groups with a service</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. </p> <p>For services that use the external deployment controller, you can add, update, or remove load balancers by using <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html">CreateTaskSet</a>. Note that multiple target groups are not supported for external deployments. For more information see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html">Register multiple target groups with a service</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. </p> <p>You can remove existing <code>loadBalancers</code> by passing an empty list.</p> <p>This parameter triggers a new service deployment.</p>
            propagate_tags: <p>Determines whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.</p> <p>Only tasks launched after the update will reflect the update. To update the tags on all tasks, set <code>forceNewDeployment</code> to <code>true</code>, so that Amazon ECS starts new tasks with the updated tags.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            service_registries: <note> <p>You must have a service-linked role when you update this property.</p> <p>For more information about the role see the <code>CreateService</code> request parameter <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html#ECS-CreateService-request-role"> <code>role</code> </a>. </p> </note> <p>The details for the service discovery registries to assign to this service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html">Service Discovery</a>.</p> <p>When you add, update, or remove the service registries configuration, Amazon ECS starts new tasks with the updated service registries configuration, and then stops the old tasks when the new tasks are running.</p> <p>You can remove existing <code>serviceRegistries</code> by passing an empty list.</p> <p>This parameter triggers a new service deployment.</p>
            service_connect_configuration: <p>The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>This parameter triggers a new service deployment.</p>
            volume_configurations: <p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceManagedEBSVolumeConfiguration.html">ServiceManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition. If set to null, no new deployment is triggered. Otherwise, if this configuration differs from the existing one, it triggers a new deployment.</p> <p>This parameter triggers a new service deployment.</p>
            vpc_lattice_configurations: <p>An object representing the VPC Lattice configuration for the service being updated.</p> <p>This parameter triggers a new service deployment.</p>
            monitoring: <p>The optional monitoring configuration for the service, which defines the resolution for the service-level <code>CPUUtilization</code> and <code>MemoryUtilization</code> Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of <code>60</code> seconds.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To change the task definition used in a service
            This example updates the my-http-service service to use the amazon-ecs-sample task definition.

            >>> await client.update_service(service='my-http-service', task_definition='amazon-ecs-sample')
            To change the number of tasks in a service
            This example updates the desired count of the my-http-service service to 10.

            >>> await client.update_service(service='my-http-service', desired_count=10)
            To update a service to add a pause lifecycle hook
            This example updates the my-blue-green-service service to add a pause lifecycle hook at the POST_PRODUCTION_TRAFFIC_SHIFT stage. The deployment will pause at that stage until you explicitly continue or roll back using the ContinueServiceDeployment API, or until the 30-minute timeout expires and triggers a continue.

            >>> await client.update_service(service='my-blue-green-service', deployment_configuration={'strategy': 'BLUE_GREEN', 'lifecycleHooks': [{'targetType': 'PAUSE', 'lifecycleStages': ['POST_PRODUCTION_TRAFFIC_SHIFT'], 'timeoutConfiguration': {'timeoutInMinutes': 30, 'action': 'CONTINUE'}}]})
            To update a service with a monitoring configuration
            This example updates a service to add a monitoring configuration that sets 20-second resolution for CPUUtilization and MemoryUtilization CloudWatch metrics. The monitoring configuration is not returned in the UpdateService response. Use DescribeServiceRevisions to view the monitoring configuration.

            >>> await client.update_service(service='ecs-monitored-service', monitoring={'metricConfigurations': [{'metricNames': ['CPUUtilization', 'MemoryUtilization'], 'resolutionSeconds': 20}]})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_service_request.UpdateServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_service_response.UpdateServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service.async_update_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.update_service_request.UpdateServiceRequest = {
            "service": service
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if desired_count is not None:
            input_["desired_count"] = desired_count
        if task_definition is not None:
            input_["task_definition"] = task_definition
        if capacity_provider_strategy is not None:
            input_["capacity_provider_strategy"] = capacity_provider_strategy
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if availability_zone_rebalancing is not None:
            input_["availability_zone_rebalancing"] = availability_zone_rebalancing
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if placement_strategy is not None:
            input_["placement_strategy"] = placement_strategy
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if force_new_deployment is not None:
            input_["force_new_deployment"] = force_new_deployment
        if health_check_grace_period_seconds is not None:
            input_["health_check_grace_period_seconds"] = (
                health_check_grace_period_seconds
            )
        if deployment_controller is not None:
            input_["deployment_controller"] = deployment_controller
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if load_balancers is not None:
            input_["load_balancers"] = load_balancers
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if service_registries is not None:
            input_["service_registries"] = service_registries
        if service_connect_configuration is not None:
            input_["service_connect_configuration"] = service_connect_configuration
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations
        if vpc_lattice_configurations is not None:
            input_["vpc_lattice_configurations"] = vpc_lattice_configurations
        if monitoring is not None:
            input_["monitoring"] = monitoring

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_service_revisions(
        self,
        service_revision_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse":
        """<p>Describes one or more service revisions.</p> <p>A service revision is a version of the service that includes the values for the Amazon ECS resources (for example, task definition) and the environment resources (for example, load balancers, subnets, and security groups). For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html">Amazon ECS service revisions</a>.</p> <p>You can't describe a service revision that was created before October 25, 2024.</p>

        Args:
            service_revision_arns: <p>The ARN of the service revision. </p> <p>You can specify a maximum of 20 ARNs.</p> <p>You can call <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html">ListServiceDeployments</a> to get the ARNs.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a service revision
            This example describes a service revision with the specified ARN

            >>> await client.describe_service_revisions(service_revision_arns=['arn:aws:ecs:us-west-2:123456789012:service-revision/testc/sd1/4980306466373577095'])
            To describe a service revision with a monitoring configuration
            This example describes a service revision that has a monitoring configuration with 20-second resolution for CPUUtilization and MemoryUtilization CloudWatch metrics.

            >>> await client.describe_service_revisions(service_revision_arns=['arn:aws:ecs:us-east-1:012345678910:service-revision/default/ecs-monitored-service/8675309012345678901'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_revisions

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_revisions.async_describe_service_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest = {
            "service_revision_arns": service_revision_arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_task_definitions(
        self,
        task_definitions: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> (
        "capo_ecs.types.delete_task_definitions_response.DeleteTaskDefinitionsResponse"
    ):
        """<p>Deletes one or more task definitions.</p> <p>You must deregister a task definition revision before you delete it. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterTaskDefinition.html">DeregisterTaskDefinition</a>.</p> <p>When you delete a task definition revision, it is immediately transitions from the <code>INACTIVE</code> to <code>DELETE_IN_PROGRESS</code>. Existing tasks and services that reference a <code>DELETE_IN_PROGRESS</code> task definition revision continue to run without disruption. Existing services that reference a <code>DELETE_IN_PROGRESS</code> task definition revision can still scale up or down by modifying the service's desired count.</p> <p>You can't use a <code>DELETE_IN_PROGRESS</code> task definition revision to run new tasks or create new services. You also can't update an existing service to reference a <code>DELETE_IN_PROGRESS</code> task definition revision.</p> <p> A task definition revision will stay in <code>DELETE_IN_PROGRESS</code> status until all the associated tasks and services have been terminated.</p> <p>When you delete all <code>INACTIVE</code> task definition revisions, the task definition name is not displayed in the console and not returned in the API. If a task definition revisions are in the <code>DELETE_IN_PROGRESS</code> state, the task definition name is displayed in the console and returned in the API. The task definition name is retained by Amazon ECS and the revision is incremented the next time you create a task definition with that name.</p>

        Args:
            task_definitions: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the task definition to delete. You must specify a <code>revision</code>.</p> <p>You can specify up to 10 task definitions as a comma separated list.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a task definition that has been deregistered
            This example deletes a specified deregistered task definition.

            >>> await client.delete_task_definitions(task_definitions=['Example-task-definition:1'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_task_definitions_request.DeleteTaskDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_task_definitions_response.DeleteTaskDefinitionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_definitions

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_definitions.async_delete_task_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.delete_task_definitions_request.DeleteTaskDefinitionsRequest = {
            "task_definitions": task_definitions
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_task_definitions(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        family_prefix: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.task_definition_status.TaskDefinitionStatus"
        ] = None,
        sort: Optional["capo_ecs.types.sort_order.SortOrder"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_task_definitions_response.ListTaskDefinitionsResponse":
        """<p>Returns a list of task definitions that are registered to your account. You can filter the results by family name with the <code>familyPrefix</code> parameter or by status with the <code>status</code> parameter.</p>

        Args:
            family_prefix: <p>The full family name to filter the <code>ListTaskDefinitions</code> results with. Specifying a <code>familyPrefix</code> limits the listed task definitions to task definition revisions that belong to that family.</p>
            status: <p>The task definition status to filter the <code>ListTaskDefinitions</code> results with. By default, only <code>ACTIVE</code> task definitions are listed. By setting this parameter to <code>INACTIVE</code>, you can view task definitions that are <code>INACTIVE</code> as long as an active task or service still references them. If you paginate the resulting output, be sure to keep the <code>status</code> value constant in each subsequent request.</p>
            sort: <p>The order to sort the results in. Valid values are <code>ASC</code> and <code>DESC</code>. By default, (<code>ASC</code>) task definitions are listed lexicographically by family name and in ascending numerical order by revision so that the newest task definitions in a family are listed last. Setting this parameter to <code>DESC</code> reverses the sort order on family name and revision. This is so that the newest task definitions in a family are listed first.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListTaskDefinitions</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it is possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of task definition results that <code>ListTaskDefinitions</code> returned in paginated output. When this parameter is used, <code>ListTaskDefinitions</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListTaskDefinitions</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListTaskDefinitions</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your registered task definitions
            This example lists all of your registered task definitions.

            >>> await client.list_task_definitions()
            To list the registered task definitions in a family
            This example lists the task definition revisions of a specified family.

            >>> await client.list_task_definitions(family_prefix='wordpress')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_task_definitions_request.ListTaskDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_task_definitions_response.ListTaskDefinitionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_task_definitions

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_task_definitions.async_list_task_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_task_definitions_request.ListTaskDefinitionsRequest = {}
        if family_prefix is not None:
            input_["family_prefix"] = family_prefix
        if status is not None:
            input_["status"] = status
        if sort is not None:
            input_["sort"] = sort
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

    async def iter_list_task_definitions(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        family_prefix: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.task_definition_status.TaskDefinitionStatus"
        ] = None,
        sort: Optional["capo_ecs.types.sort_order.SortOrder"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "AsyncIterator[capo_ecs.types.string.String]":
        _token = next_token
        while True:
            _response = await self.list_task_definitions(
                config_overrides=config_overrides,
                family_prefix=family_prefix,
                status=status,
                sort=sort,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("task_definition_arns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def register_task_definition(
        self,
        family: "capo_ecs.types.string.String",
        container_definitions: "capo_ecs.types.container_definitions.ContainerDefinitions",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        network_mode: Optional["capo_ecs.types.network_mode.NetworkMode"] = None,
        volumes: Optional["capo_ecs.types.volume_list.VolumeList"] = None,
        placement_constraints: Optional[
            "capo_ecs.types.task_definition_placement_constraints.TaskDefinitionPlacementConstraints"
        ] = None,
        requires_compatibilities: Optional[
            "capo_ecs.types.compatibility_list.CompatibilityList"
        ] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        pid_mode: Optional["capo_ecs.types.pid_mode.PidMode"] = None,
        ipc_mode: Optional["capo_ecs.types.ipc_mode.IpcMode"] = None,
        proxy_configuration: Optional[
            "capo_ecs.types.proxy_configuration.ProxyConfiguration"
        ] = None,
        inference_accelerators: Optional[
            "capo_ecs.types.inference_accelerators.InferenceAccelerators"
        ] = None,
        ephemeral_storage: Optional[
            "capo_ecs.types.ephemeral_storage.EphemeralStorage"
        ] = None,
        runtime_platform: Optional[
            "capo_ecs.types.runtime_platform.RuntimePlatform"
        ] = None,
        enable_fault_injection: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
    ) -> "capo_ecs.types.register_task_definition_response.RegisterTaskDefinitionResponse":
        """<p>Registers a new task definition from the supplied <code>family</code> and <code>containerDefinitions</code>. Optionally, you can add data volumes to your containers with the <code>volumes</code> parameter. For more information about task definition parameters and defaults, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html">Amazon ECS Task Definitions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can specify a role for your task with the <code>taskRoleArn</code> parameter. When you specify a role for a task, its containers can then use the latest versions of the CLI or SDKs to make API requests to the Amazon Web Services services that are specified in the policy that's associated with the role. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html">IAM Roles for Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can specify a Docker networking mode for the containers in your task definition with the <code>networkMode</code> parameter. If you specify the <code>awsvpc</code> network mode, the task is allocated an elastic network interface, and you must specify a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html">NetworkConfiguration</a> when you create a service or run a task with the task definition. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task Networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            family: <p>You must specify a <code>family</code> for a task definition. You can use it track multiple versions of the same task definition. The <code>family</code> is used as a name for your task definition. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>
            task_role_arn: <p>The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html">IAM Roles for Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. For informationabout the required IAM roles for Amazon ECS, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-ecs-iam-role-overview.html">IAM roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            network_mode: <p>The Docker networking mode to use for the containers in the task. The valid values are <code>none</code>, <code>bridge</code>, <code>awsvpc</code>, and <code>host</code>. If no network mode is specified, the default is <code>bridge</code>.</p> <p>For Amazon ECS tasks on Fargate, the <code>awsvpc</code> network mode is required. For Amazon ECS tasks on Amazon EC2 Linux instances, any network mode can be used. For Amazon ECS tasks on Amazon EC2 Windows instances, <code>&lt;default&gt;</code> or <code>awsvpc</code> can be used. If the network mode is set to <code>none</code>, you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The <code>host</code> and <code>awsvpc</code> network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the <code>bridge</code> mode.</p> <p>With the <code>host</code> and <code>awsvpc</code> network modes, exposed container ports are mapped directly to the corresponding host port (for the <code>host</code> network mode) or the attached elastic network interface port (for the <code>awsvpc</code> network mode), so you cannot take advantage of dynamic host port mappings. </p> <important> <p>When using the <code>host</code> network mode, you should not run containers using the root user (UID 0). It is considered best practice to use a non-root user.</p> </important> <p>If the network mode is <code>awsvpc</code>, the task is allocated an elastic network interface, and you must specify a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html">NetworkConfiguration</a> value when you create a service or run a task with the task definition. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task Networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the network mode is <code>host</code>, you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.</p>
            container_definitions: <p>A list of container definitions in JSON format that describe the different containers that make up your task.</p>
            volumes: <p>A list of volume definitions in JSON format that containers in your task might use.</p>
            placement_constraints: <p>An array of placement constraint objects to use for the task. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p>
            requires_compatibilities: <p>The task launch type that Amazon ECS validates the task definition against. A client exception is returned if the task definition doesn't validate against the compatibilities specified. If no value is specified, the parameter is omitted from the response.</p>
            cpu: <p>The number of CPU units used by the task. It can be expressed as an integer using CPU units (for example, <code>1024</code>) or as a string using vCPUs (for example, <code>1 vCPU</code> or <code>1 vcpu</code>) in a task definition. String values are converted to an integer indicating the CPU units when the task definition is registered.</p> <note> <p>Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.</p> </note> <p>If you're using the EC2 launch type or external launch type, this field is optional. Supported values are between <code>128</code> CPU units (<code>0.125</code> vCPUs) and <code>196608</code> CPU units (<code>192</code> vCPUs). If you do not specify a value, the parameter is ignored.</p> <p>This field is required for Fargate. For information about the valid values, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size">Task size</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            memory: <p>The amount of memory (in MiB) used by the task. It can be expressed as an integer using MiB (for example ,<code>1024</code>) or as a string using GB (for example, <code>1GB</code> or <code>1 GB</code>) in a task definition. String values are converted to an integer indicating the MiB when the task definition is registered.</p> <note> <p>Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.</p> </note> <p>If using the EC2 launch type, this field is optional.</p> <p>If using the Fargate launch type, this field is required and you must use one of the following values. This determines your range of supported values for the <code>cpu</code> parameter.</p> <p>The CPU units cannot be less than 1 vCPU when you use Windows containers on Fargate.</p> <ul> <li> <p>512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available <code>cpu</code> values: 256 (.25 vCPU)</p> </li> <li> <p>1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available <code>cpu</code> values: 512 (.5 vCPU)</p> </li> <li> <p>2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available <code>cpu</code> values: 1024 (1 vCPU)</p> </li> <li> <p>Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 2048 (2 vCPU)</p> </li> <li> <p>Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 4096 (4 vCPU)</p> </li> <li> <p>Between 16 GB and 60 GB in 4 GB increments - Available <code>cpu</code> values: 8192 (8 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> <li> <p>Between 32GB and 120 GB in 8 GB increments - Available <code>cpu</code> values: 16384 (16 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> </ul>
            tags: <p>The metadata that you apply to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            pid_mode: <p>The process namespace to use for the containers in the task. The valid values are <code>host</code> or <code>task</code>. On Fargate for Linux containers, the only valid value is <code>task</code>. For example, monitoring sidecars might need <code>pidMode</code> to access information about other containers running in the same task.</p> <p>If <code>host</code> is specified, all containers within the tasks that specified the <code>host</code> PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance.</p> <p>If <code>task</code> is specified, all containers within the specified task share the same process namespace.</p> <p>If no value is specified, the The default is a private namespace for each container.</p> <p>If the <code>host</code> PID mode is used, there's a heightened risk of undesired process namespace exposure.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note> <note> <p>This parameter is only supported for tasks that are hosted on Fargate if the tasks are using platform version <code>1.4.0</code> or later (Linux). This isn't supported for Windows containers on Fargate.</p> </note>
            ipc_mode: <p>The IPC resource namespace to use for the containers in the task. The valid values are <code>host</code>, <code>task</code>, or <code>none</code>. If <code>host</code> is specified, then all containers within the tasks that specified the <code>host</code> IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If <code>task</code> is specified, all containers within the specified task share the same IPC resources. If <code>none</code> is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance.</p> <p>If the <code>host</code> IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose.</p> <p>If you are setting namespaced kernel parameters using <code>systemControls</code> for the containers in the task, the following will apply to your IPC resource namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html">System Controls</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <ul> <li> <p>For tasks that use the <code>host</code> IPC mode, IPC namespace related <code>systemControls</code> are not supported.</p> </li> <li> <p>For tasks that use the <code>task</code> IPC mode, IPC namespace related <code>systemControls</code> will apply to all containers within a task.</p> </li> </ul> <note> <p>This parameter is not supported for Windows containers or tasks run on Fargate.</p> </note>
            proxy_configuration: <p>The configuration details for the App Mesh proxy.</p> <p>For tasks hosted on Amazon EC2 instances, the container instances require at least version <code>1.26.0</code> of the container agent and at least version <code>1.26.0-1</code> of the <code>ecs-init</code> package to use a proxy configuration. If your container instances are launched from the Amazon ECS-optimized AMI version <code>20190301</code> or later, then they contain the required versions of the container agent and <code>ecs-init</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-ami-versions.html">Amazon ECS-optimized AMI versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            inference_accelerators: <p>The Elastic Inference accelerators to use for the containers in the task.</p>
            ephemeral_storage: <p>The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html">Using data volumes in tasks</a> in the <i>Amazon ECS Developer Guide</i>.</p> <note> <p>For tasks using the Fargate launch type, the task requires the following platforms:</p> <ul> <li> <p>Linux platform version <code>1.4.0</code> or later.</p> </li> <li> <p>Windows platform version <code>1.0.0</code> or later.</p> </li> </ul> </note>
            runtime_platform: <p>The operating system that your tasks definitions run on.</p>
            enable_fault_injection: <p>Enables fault injection when you register your task definition and allows for fault injection requests to be accepted from the task's containers. The default value is <code>false</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To register a task definition
            This example registers a task definition to the specified family.

            >>> await client.register_task_definition(family='sleep360', task_role_arn='', container_definitions=[{'name': 'sleep', 'image': 'public.ecr.aws/docker/library/busybox:latest', 'cpu': 10, 'command': ['sleep', '360'], 'memory': 10, 'essential': True}], volumes=[])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.register_task_definition_request.RegisterTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.register_task_definition_response.RegisterTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.register_task_definition

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.register_task_definition.async_register_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.register_task_definition_request.RegisterTaskDefinitionRequest = {
            "family": family,
            "container_definitions": container_definitions,
        }
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if network_mode is not None:
            input_["network_mode"] = network_mode
        if volumes is not None:
            input_["volumes"] = volumes
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if requires_compatibilities is not None:
            input_["requires_compatibilities"] = requires_compatibilities
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if tags is not None:
            input_["tags"] = tags
        if pid_mode is not None:
            input_["pid_mode"] = pid_mode
        if ipc_mode is not None:
            input_["ipc_mode"] = ipc_mode
        if proxy_configuration is not None:
            input_["proxy_configuration"] = proxy_configuration
        if inference_accelerators is not None:
            input_["inference_accelerators"] = inference_accelerators
        if ephemeral_storage is not None:
            input_["ephemeral_storage"] = ephemeral_storage
        if runtime_platform is not None:
            input_["runtime_platform"] = runtime_platform
        if enable_fault_injection is not None:
            input_["enable_fault_injection"] = enable_fault_injection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_tasks(
        self,
        tasks: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        include: Optional["capo_ecs.types.task_field_list.TaskFieldList"] = None,
    ) -> "capo_ecs.types.describe_tasks_response.DescribeTasksResponse":
        """<p>Describes a specified task or tasks.</p> <p>Currently, stopped tasks appear in the returned results for at least one hour.</p> <p>If you have tasks with tags, and then delete the cluster, the tagged tasks are returned in the response. If you create a new cluster with the same name as the deleted cluster, the tagged tasks are not included in the response.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task or tasks to describe. If you do not specify a cluster, the default cluster is assumed.</p>
            tasks: <p>A list of up to 100 task IDs or full ARN entries.</p>
            include: <p>Specifies whether you want to see the resource tags for the task. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a task
            This example provides a description of the specified task, using the task UUID as an identifier.

            >>> await client.describe_tasks(tasks=['c5cba4eb-5dad-405e-96db-71ef8eefe6a8'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_tasks_request.DescribeTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_tasks_response.DescribeTasksResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_tasks

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_tasks.async_describe_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_tasks_request.DescribeTasksRequest = {
            "tasks": tasks
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if include is not None:
            input_["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_task_protection(
        self,
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        tasks: Optional["capo_ecs.types.string_list.StringList"] = None,
    ) -> "capo_ecs.types.get_task_protection_response.GetTaskProtectionResponse":
        """<p>Retrieves the protection status of tasks in an Amazon ECS service.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>
            tasks: <p>A list of up to 100 task IDs or full ARN entries.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the protection status of a task
            In this example, we get the protection status for a single task.

            >>> await client.get_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.get_task_protection_request.GetTaskProtectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.get_task_protection_response.GetTaskProtectionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.get_task_protection

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.get_task_protection.async_get_task_protection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.get_task_protection_request.GetTaskProtectionRequest = {
            "cluster": cluster
        }
        if tasks is not None:
            input_["tasks"] = tasks

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def run_task(
        self,
        task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        count: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        group: Optional["capo_ecs.types.string.String"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        overrides: Optional["capo_ecs.types.task_override.TaskOverride"] = None,
        placement_constraints: Optional[
            "capo_ecs.types.placement_constraints.PlacementConstraints"
        ] = None,
        placement_strategy: Optional[
            "capo_ecs.types.placement_strategies.PlacementStrategies"
        ] = None,
        platform_version: Optional["capo_ecs.types.string.String"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        reference_id: Optional["capo_ecs.types.string.String"] = None,
        started_by: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        volume_configurations: Optional[
            "capo_ecs.types.task_volume_configurations.TaskVolumeConfigurations"
        ] = None,
    ) -> "capo_ecs.types.run_task_response.RunTaskResponse":
        """<p>Starts a new task using the specified task definition.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <note> <p>Amazon Elastic Inference (EI) is no longer available to customers.</p> </note> <p>You can allow Amazon ECS to place tasks for you, or you can customize how Amazon ECS places tasks using placement constraints and placement strategies. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html">Scheduling Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Alternatively, you can use <code>StartTask</code> to use your own scheduler or place tasks manually on specific container instances.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>The Amazon ECS API follows an eventual consistency model. This is because of the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your Amazon ECS resources might not be immediately visible to all subsequent commands you run. Keep this in mind when you carry out an API command that immediately follows a previous API command.</p> <p>To manage eventual consistency, you can do the following:</p> <ul> <li> <p>Confirm the state of the resource before you run a command to modify it. Run the DescribeTasks command using an exponential backoff algorithm to ensure that you allow enough time for the previous command to propagate through the system. To do this, run the DescribeTasks command repeatedly, starting with a couple of seconds of wait time and increasing gradually up to five minutes of wait time.</p> </li> <li> <p>Add wait time between subsequent commands, even if the DescribeTasks command returns an accurate response. Apply an exponential backoff algorithm starting with a couple of seconds of wait time, and increase gradually up to about five minutes of wait time.</p> </li> </ul> <p>If you get a <code>ConflictException</code> error, the <code>RunTask</code> request could not be processed due to conflicts. The provided <code>clientToken</code> is already in use with a different <code>RunTask</code> request. The <code>resourceIds</code> are the existing task ARNs which are already associated with the <code>clientToken</code>. </p> <p>To fix this issue:</p> <ul> <li> <p>Run <code>RunTask</code> with a unique <code>clientToken</code>.</p> </li> <li> <p>Run <code>RunTask</code> with the <code>clientToken</code> and the original set of parameters</p> </li> </ul> <p>If you get a <code>ClientException</code>error, the <code>RunTask</code> could not be processed because you use managed scaling and there is a capacity error because the quota of tasks in the <code>PROVISIONING</code> per cluster has been reached. For information about the service quotas, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html">Amazon ECS service quotas</a>.</p>

        Args:
            capacity_provider_strategy: <p>The capacity provider strategy to use for the task.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>When you use cluster auto scaling, you must specify <code>capacityProviderStrategy</code> and not <code>launchType</code>. </p> <p>A capacity provider strategy can contain a maximum of 20 capacity providers.</p>
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to run your task on. If you do not specify a cluster, the default cluster is assumed.</p> <p>Each account receives a default cluster the first time you use the service, but you may also create other clusters.</p>
            count: <p>The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks for each call.</p>
            enable_ecs_managed_tags: <p>Specifies whether to use Amazon ECS managed tags for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>Determines whether to use the execute command functionality for the containers in this task. If <code>true</code>, this enables execute command functionality on all containers in the task.</p> <p>If <code>true</code>, then the task definition must have a task role, or you must provide one as an override.</p>
            group: <p>The name of the task group to associate with the task. The default value is the family name of the task definition (for example, <code>family:my-family-name</code>).</p>
            launch_type: <p>The infrastructure to run your standalone task on. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>The <code>FARGATE</code> launch type runs your tasks on Fargate On-Demand infrastructure.</p> <note> <p>Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html">Fargate capacity providers</a> in the <i>Amazon ECS Developer Guide</i>.</p> </note> <p>The <code>EC2</code> launch type runs your tasks on Amazon EC2 instances registered to your cluster.</p> <p>The <code>EXTERNAL</code> launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.</p> <p>A task can use either a launch type or a capacity provider strategy. If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p> <p>When you use cluster auto scaling, you must specify <code>capacityProviderStrategy</code> and not <code>launchType</code>. </p>
            network_configuration: <p>The network configuration for the task. This parameter is required for task definitions that use the <code>awsvpc</code> network mode to receive their own elastic network interface, and it isn't supported for other network modes. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            overrides: <p>A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that's specified in the task definition or Docker image) with a <code>command</code> override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an <code>environment</code> override.</p> <p>A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.</p>
            placement_constraints: <p>An array of placement constraint objects to use for the task. You can specify up to 10 constraints for each task (including constraints in the task definition and those specified at runtime).</p>
            placement_strategy: <p>The placement strategy objects to use for the task. You can specify a maximum of 5 strategy rules for each task.</p>
            platform_version: <p>The platform version the task uses. A platform version is only specified for tasks hosted on Fargate. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the<a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html">TagResource</a> API action.</p> <note> <p>An error will be received if you specify the <code>SERVICE</code> option when running a task.</p> </note>
            reference_id: <p>This parameter is only used by Amazon ECS. It is not intended for use by customers.</p>
            started_by: <p>An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the <code>startedBy</code> parameter. You can then identify which tasks belong to that job by filtering the results of a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html">ListTasks</a> call with the <code>startedBy</code> value. Up to 128 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (_) are allowed.</p> <p>If a task is started by an Amazon ECS service, then the <code>startedBy</code> parameter contains the deployment ID of the service that starts it.</p>
            tags: <p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p> <p>The full ARN value must match the value that you specified as the <code>Resource</code> of the principal's permissions policy.</p> <p>When you specify a task definition, you must either specify a specific revision, or all revisions in the ARN.</p> <p>To specify a specific revision, include the revision number in the ARN. For example, to specify revision 2, use <code>arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:2</code>.</p> <p>To specify all revisions, use the wildcard (*) in the ARN. For example, to specify all revisions, use <code>arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:*</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">Policy Resources for Amazon ECS</a> in the Amazon Elastic Container Service Developer Guide.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 64 characters are allowed. The valid characters are characters in the range of 33-126, inclusive. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/ECS_Idempotency.html">Ensuring idempotency</a>.</p>
            volume_configurations: <p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html">TaskManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.blocked_exception.BlockedException: <p>Your Amazon Web Services account was blocked. For more information, contact <a href="http://aws.amazon.com/contact-us/"> Amazon Web Services Support</a>.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. </p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To run a task on your default cluster
            This example runs the specified task definition on your default cluster.

            >>> await client.run_task(cluster='default', task_definition='sleep360:1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.run_task_request.RunTaskRequest]",
        ) -> AsyncOperationResponse["capo_ecs.types.run_task_response.RunTaskResponse"]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.run_task

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.run_task.async_run_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.run_task_request.RunTaskRequest = {
            "task_definition": task_definition
        }
        if capacity_provider_strategy is not None:
            input_["capacity_provider_strategy"] = capacity_provider_strategy
        if cluster is not None:
            input_["cluster"] = cluster
        if count is not None:
            input_["count"] = count
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if group is not None:
            input_["group"] = group
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if overrides is not None:
            input_["overrides"] = overrides
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if placement_strategy is not None:
            input_["placement_strategy"] = placement_strategy
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if reference_id is not None:
            input_["reference_id"] = reference_id
        if started_by is not None:
            input_["started_by"] = started_by
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_task(
        self,
        container_instances: "capo_ecs.types.string_list.StringList",
        task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        group: Optional["capo_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        overrides: Optional["capo_ecs.types.task_override.TaskOverride"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        reference_id: Optional["capo_ecs.types.string.String"] = None,
        started_by: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        volume_configurations: Optional[
            "capo_ecs.types.task_volume_configurations.TaskVolumeConfigurations"
        ] = None,
    ) -> "capo_ecs.types.start_task_response.StartTaskResponse":
        """<p>Starts a new task from the specified task definition on the specified container instance or instances.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <note> <p>Amazon Elastic Inference (EI) is no longer available to customers.</p> </note> <p>Alternatively, you can use<code>RunTask</code> to place tasks for you. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html">Scheduling Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster where to start your task. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instances: <p>The container instance IDs or full ARN entries for the container instances where you would like to place your task. You can specify up to 10 container instances.</p>
            enable_ecs_managed_tags: <p>Specifies whether to use Amazon ECS managed tags for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>Whether or not the execute command functionality is turned on for the task. If <code>true</code>, this turns on the execute command functionality on all containers in the task.</p>
            group: <p>The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).</p>
            network_configuration: <p>The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the <code>awsvpc</code> networking mode.</p>
            overrides: <p>A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it receives. You can override the default command for a container (that's specified in the task definition or Docker image) with a <code>command</code> override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an <code>environment</code> override.</p> <note> <p>A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.</p> </note>
            propagate_tags: <p>Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.</p>
            reference_id: <p>This parameter is only used by Amazon ECS. It is not intended for use by customers.</p>
            started_by: <p>An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the <code>startedBy</code> parameter. You can then identify which tasks belong to that job by filtering the results of a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html">ListTasks</a> call with the <code>startedBy</code> value. Up to 36 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (_) are allowed.</p> <p>If a task is started by an Amazon ECS service, the <code>startedBy</code> parameter contains the deployment ID of the service that starts it.</p>
            tags: <p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to start. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p>
            volume_configurations: <p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html">TaskManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To start a new task
            This example starts a new task in the cluster "MyCluster" on the specified container instance using the latest revision of the "hello-world" task definition.

            >>> await client.start_task(cluster='MyCluster', container_instances=['4c543eed-f83f-47da-b1d8-3d23f1da4c64'], task_definition='hello-world')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.start_task_request.StartTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.start_task_response.StartTaskResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.start_task

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.start_task.async_start_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.start_task_request.StartTaskRequest = {
            "container_instances": container_instances,
            "task_definition": task_definition,
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if group is not None:
            input_["group"] = group
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if overrides is not None:
            input_["overrides"] = overrides
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if reference_id is not None:
            input_["reference_id"] = reference_id
        if started_by is not None:
            input_["started_by"] = started_by
        if tags is not None:
            input_["tags"] = tags
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_task(
        self,
        task: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        reason: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.stop_task_response.StopTaskResponse":
        """<p>Stops a running task. Any tags associated with the task will be deleted.</p> <p>When you call <code>StopTask</code> on a task, the equivalent of <code>docker stop</code> is issued to the containers running in the task. This results in a stop signal value and a default 30-second timeout, after which the <code>SIGKILL</code> value is sent and the containers are forcibly stopped. This signal can be defined in your container image with the <code>STOPSIGNAL</code> instruction and will default to <code>SIGTERM</code>. If the container handles the <code>SIGTERM</code> value gracefully and exits within 30 seconds from receiving it, no <code>SIGKILL</code> value is sent.</p> <p>For Windows containers, POSIX signals do not work and runtime stops the container by sending a <code>CTRL_SHUTDOWN_EVENT</code>. For more information, see <a href="https://github.com/moby/moby/issues/25982">Unable to react to graceful shutdown of (Windows) container #25982</a> on GitHub.</p> <note> <p>The default 30-second timeout can be configured on the Amazon ECS container agent with the <code>ECS_CONTAINER_STOP_TIMEOUT</code> variable. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html">Amazon ECS Container Agent Configuration</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed.</p>
            task: <p>Thefull Amazon Resource Name (ARN) of the task.</p>
            reason: <p>An optional message specified when a task is stopped. For example, if you're using a custom scheduler, you can use this parameter to specify the reason for stopping the task here, and the message appears in subsequent <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html">DescribeTasks</a>&gt; API operations on this task.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To stop a task
            This example stops a task with ID "1dc5c17a-422b-4dc4-b493-371970c6c4d6" in cluster "MyCluster".

            >>> await client.stop_task(cluster='MyCluster', task='1dc5c17a-422b-4dc4-b493-371970c6c4d6', reason='testing stop task.')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.stop_task_request.StopTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.stop_task_response.StopTaskResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_task

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_task.async_stop_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.stop_task_request.StopTaskRequest = {"task": task}
        if cluster is not None:
            input_["cluster"] = cluster
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_task_protection(
        self,
        cluster: "capo_ecs.types.string.String",
        tasks: "capo_ecs.types.string_list.StringList",
        protection_enabled: "capo_ecs.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        expires_in_minutes: Optional[
            "capo_ecs.types.boxed_integer.BoxedInteger"
        ] = None,
    ) -> "capo_ecs.types.update_task_protection_response.UpdateTaskProtectionResponse":
        """<p>Updates the protection status of a task. You can set <code>protectionEnabled</code> to <code>true</code> to protect your task from termination during scale-in events from <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html">Service Autoscaling</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">deployments</a>.</p> <p>Task-protection, by default, expires after 2 hours at which point Amazon ECS clears the <code>protectionEnabled</code> property making the task eligible for termination by a subsequent scale-in event.</p> <p>You can specify a custom expiration period for task protection from 1 minute to up to 2,880 minutes (48 hours). To specify the custom expiration period, set the <code>expiresInMinutes</code> property. The <code>expiresInMinutes</code> property is always reset when you invoke this operation for a task that already has <code>protectionEnabled</code> set to <code>true</code>. You can keep extending the protection expiration period of a task by invoking this operation repeatedly.</p> <p>To learn more about Amazon ECS task protection, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection.html">Task scale-in protection</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <note> <p>This operation is only supported for tasks belonging to an Amazon ECS service. Invoking this operation for a standalone task will result in an <code>TASK_NOT_VALID</code> failure. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html">API failure reasons</a>.</p> </note> <important> <p>If you prefer to set task protection from within the container, we recommend using the <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection-endpoint.html">Task scale-in protection endpoint</a>.</p> </important>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>
            tasks: <p>A list of up to 10 task IDs or full ARN entries.</p>
            protection_enabled: <p>Specify <code>true</code> to mark a task for protection and <code>false</code> to unset protection, making it eligible for termination.</p>
            expires_in_minutes: <p>If you set <code>protectionEnabled</code> to <code>true</code>, you can specify the duration for task protection in minutes. You can specify a value from 1 minute to up to 2,880 minutes (48 hours). During this time, your task will not be terminated by scale-in events from Service Auto Scaling or deployments. After this time period lapses, <code>protectionEnabled</code> will be reset to <code>false</code>.</p> <p>If you don’t specify the time, then the task is automatically protected for 120 minutes (2 hours).</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To set task scale-in protection for a task for 60 minutes
            This example enables scale-in protection for a task for 60 minutes.

            >>> await client.update_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'], protection_enabled=True, expires_in_minutes=60)
            To set task scale-in protection for the default time period in minutes
            This example enables task scale-in protection for a task, without specifying the expiresInMinutes parameter, for the default protection period of 120 minutes.

            >>> await client.update_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'], protection_enabled=True)
            To remove task scale-in protection
            This example removes scale-in protection for a task.

            >>> await client.update_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'], protection_enabled=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_task_protection_request.UpdateTaskProtectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_task_protection_response.UpdateTaskProtectionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_task_protection

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_task_protection.async_update_task_protection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.update_task_protection_request.UpdateTaskProtectionRequest = {
            "cluster": cluster,
            "tasks": tasks,
            "protection_enabled": protection_enabled,
        }
        if expires_in_minutes is not None:
            input_["expires_in_minutes"] = expires_in_minutes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_task_set(
        self,
        cluster: "capo_ecs.types.string.String",
        service: "capo_ecs.types.string.String",
        task_set: "capo_ecs.types.string.String",
        scale: "capo_ecs.types.scale.Scale",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.update_task_set_response.UpdateTaskSetResponse":
        """<p>Modifies a task set. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS Deployment Types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set is found in.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that the task set is found in.</p>
            task_set: <p>The short name or full Amazon Resource Name (ARN) of the task set to update.</p>
            scale: <p>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.task_set_not_found_exception.TaskSetNotFoundException: <p>The specified task set wasn't found. You can view your available task sets with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskSets.html">DescribeTaskSets</a>. Task sets are specific to each cluster, service and Region.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a task set
            This example updates the task set to adjust the scale.

            >>> await client.update_task_set(cluster='MyCluster', service='MyService', task_set='arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789', scale={'value': 50, 'unit': 'PERCENT'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_task_set_request.UpdateTaskSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_task_set_response.UpdateTaskSetResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_task_set

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_task_set.async_update_task_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.update_task_set_request.UpdateTaskSetRequest = {
            "cluster": cluster,
            "service": service,
            "task_set": task_set,
            "scale": scale,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_task_set(
        self,
        cluster: "capo_ecs.types.string.String",
        service: "capo_ecs.types.string.String",
        task_set: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        force: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.delete_task_set_response.DeleteTaskSetResponse":
        """<p>Deletes a specified task set within a service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS deployment types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set found in to delete.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that hosts the task set to delete.</p>
            task_set: <p>The task set ID or full Amazon Resource Name (ARN) of the task set to delete.</p>
            force: <p>If <code>true</code>, you can delete a task set even if it hasn't been scaled down to zero.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.task_set_not_found_exception.TaskSetNotFoundException: <p>The specified task set wasn't found. You can view your available task sets with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskSets.html">DescribeTaskSets</a>. Task sets are specific to each cluster, service and Region.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a task set within a service that uses the EXTERNAL deployment controller type
            This example deletes a task set and uses the force flag to force deletion if it hasn't scaled to zero.

            >>> await client.delete_task_set(cluster='MyCluster', service='MyService', task_set='arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789', force=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_task_set_request.DeleteTaskSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_task_set_response.DeleteTaskSetResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_set

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_set.async_delete_task_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.delete_task_set_request.DeleteTaskSetRequest = {
            "cluster": cluster,
            "service": service,
            "task_set": task_set,
        }
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_task_set(
        self,
        service: "capo_ecs.types.string.String",
        cluster: "capo_ecs.types.string.String",
        task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        external_id: Optional["capo_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        load_balancers: Optional["capo_ecs.types.load_balancers.LoadBalancers"] = None,
        service_registries: Optional[
            "capo_ecs.types.service_registries.ServiceRegistries"
        ] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        platform_version: Optional["capo_ecs.types.string.String"] = None,
        scale: Optional["capo_ecs.types.scale.Scale"] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
    ) -> "capo_ecs.types.create_task_set_response.CreateTaskSetResponse":
        """<p>Create a task set in the specified cluster and service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS deployment types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <p>For information about the maximum number of task sets and other quotas, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html">Amazon ECS service quotas</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            service: <p>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</p>
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</p>
            external_id: <p>An optional non-unique tag that identifies this task set in external systems. If the task set is associated with a service discovery registry, the tasks in this task set will have the <code>ECS_TASK_SET_EXTERNAL_ID</code> Cloud Map attribute set to the provided value.</p>
            task_definition: <p>The task definition for the tasks in the task set to use. If a revision isn't specified, the latest <code>ACTIVE</code> revision is used.</p>
            network_configuration: <p>An object representing the network configuration for a task set.</p>
            load_balancers: <p>A load balancer object representing the load balancer to use with the task set. The supported load balancer types are either an Application Load Balancer or a Network Load Balancer.</p>
            service_registries: <p>The details of the service discovery registries to assign to this task set. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html">Service discovery</a>.</p>
            launch_type: <p>The launch type that new tasks in the task set uses. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p>
            capacity_provider_strategy: <p>The capacity provider strategy to use for the task set.</p> <p>A capacity provider strategy consists of one or more capacity providers along with the <code>base</code> and <code>weight</code> to assign to them. A capacity provider must be associated with the cluster to be used in a capacity provider strategy. The <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API is used to associate a capacity provider with a cluster. Only capacity providers with an <code>ACTIVE</code> or <code>UPDATING</code> status can be used.</p> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProviderProvider.html">CreateCapacityProviderProvider</a>API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p> <p>The <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API operation is used to update the list of available capacity providers for a cluster after the cluster is created.</p>
            platform_version: <p>The platform version that the tasks in the task set uses. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the <code>LATEST</code> platform version is used.</p>
            scale: <p>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>
            tags: <p>The metadata that you apply to the task set to help you categorize and organize them. Each tag consists of a key and an optional value. You define both. When a service is deleted, the tags are deleted.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a task set
            This example creates a task set in a service that uses the EXTERNAL deployment controller.

            >>> await client.create_task_set(service='MyService', cluster='MyCluster', task_definition='MyTaskDefinition:2', network_configuration={'awsvpcConfiguration': {'subnets': ['subnet-12344321'], 'securityGroups': ['sg-12344321']}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.create_task_set_request.CreateTaskSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.create_task_set_response.CreateTaskSetResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_task_set

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.create_task_set.async_create_task_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.create_task_set_request.CreateTaskSetRequest = {
            "service": service,
            "cluster": cluster,
            "task_definition": task_definition,
        }
        if external_id is not None:
            input_["external_id"] = external_id
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if load_balancers is not None:
            input_["load_balancers"] = load_balancers
        if service_registries is not None:
            input_["service_registries"] = service_registries
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if capacity_provider_strategy is not None:
            input_["capacity_provider_strategy"] = capacity_provider_strategy
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if scale is not None:
            input_["scale"] = scale
        if client_token is not None:
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

    async def describe_task_sets(
        self,
        cluster: "capo_ecs.types.string.String",
        service: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        task_sets: Optional["capo_ecs.types.string_list.StringList"] = None,
        include: Optional["capo_ecs.types.task_set_field_list.TaskSetFieldList"] = None,
    ) -> "capo_ecs.types.describe_task_sets_response.DescribeTaskSetsResponse":
        """<p>Describes the task sets in the specified cluster and service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS Deployment Types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that the task sets exist in.</p>
            task_sets: <p>The ID or full Amazon Resource Name (ARN) of task sets to describe.</p>
            include: <p>Specifies whether to see the resource tags for the task set. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a task set
            This example describes a task set in service MyService that uses an EXTERNAL deployment controller.

            >>> await client.describe_task_sets(cluster='MyCluster', service='MyService', task_sets=['arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_task_sets_request.DescribeTaskSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_task_sets_response.DescribeTaskSetsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_task_sets

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_task_sets.async_describe_task_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_task_sets_request.DescribeTaskSetsRequest = {
            "cluster": cluster,
            "service": service,
        }
        if task_sets is not None:
            input_["task_sets"] = task_sets
        if include is not None:
            input_["include"] = include

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
