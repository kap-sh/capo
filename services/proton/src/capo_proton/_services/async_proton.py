"""Generated from Smithy shape ``com.amazonaws.proton#AwsProton20200720``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_proton._auth._signers
import capo_proton._auth._sigv4
from capo_proton._auth._identity import Credentials
from capo_proton._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_proton._auth._zapros_handler import AuthMiddleware
from capo_proton._pagination import resolve_path as _resolve_path
from capo_proton._resources.aws_proton20200720.account_settings_resource import (
    AsyncAccountSettingsResource,
)
from capo_proton._resources.aws_proton20200720.component_output_resource import (
    AsyncComponentOutputResource,
)
from capo_proton._resources.aws_proton20200720.component_provisioned_resource_resource import (
    AsyncComponentProvisionedResourceResource,
)
from capo_proton._resources.aws_proton20200720.component_resource import (
    AsyncComponentResource,
)
from capo_proton._resources.aws_proton20200720.deployment_resource import (
    AsyncDeploymentResource,
)
from capo_proton._resources.aws_proton20200720.environment_account_connection_resource import (
    AsyncEnvironmentAccountConnectionResource,
)
from capo_proton._resources.aws_proton20200720.environment_output_resource import (
    AsyncEnvironmentOutputResource,
)
from capo_proton._resources.aws_proton20200720.environment_provisioned_resource_resource import (
    AsyncEnvironmentProvisionedResourceResource,
)
from capo_proton._resources.aws_proton20200720.environment_resource import (
    AsyncEnvironmentResource,
)
from capo_proton._resources.aws_proton20200720.environment_template_resource import (
    AsyncEnvironmentTemplateResource,
)
from capo_proton._resources.aws_proton20200720.environment_template_version_resource import (
    AsyncEnvironmentTemplateVersionResource,
)
from capo_proton._resources.aws_proton20200720.repository_resource import (
    AsyncRepositoryResource,
)
from capo_proton._resources.aws_proton20200720.service_instance_output_resource import (
    AsyncServiceInstanceOutputResource,
)
from capo_proton._resources.aws_proton20200720.service_instance_provisioned_resource_resource import (
    AsyncServiceInstanceProvisionedResourceResource,
)
from capo_proton._resources.aws_proton20200720.service_instance_resource import (
    AsyncServiceInstanceResource,
)
from capo_proton._resources.aws_proton20200720.service_pipeline_output_resource import (
    AsyncServicePipelineOutputResource,
)
from capo_proton._resources.aws_proton20200720.service_pipeline_provisioned_resource_resource import (
    AsyncServicePipelineProvisionedResourceResource,
)
from capo_proton._resources.aws_proton20200720.service_pipeline_resource import (
    AsyncServicePipelineResource,
)
from capo_proton._resources.aws_proton20200720.service_resource import (
    AsyncServiceResource,
)
from capo_proton._resources.aws_proton20200720.service_sync_blocker_resource import (
    AsyncServiceSyncBlockerResource,
)
from capo_proton._resources.aws_proton20200720.service_sync_config_resource import (
    AsyncServiceSyncConfigResource,
)
from capo_proton._resources.aws_proton20200720.service_template_resource import (
    AsyncServiceTemplateResource,
)
from capo_proton._resources.aws_proton20200720.service_template_version_resource import (
    AsyncServiceTemplateVersionResource,
)
from capo_proton._resources.aws_proton20200720.template_sync_config_resource import (
    AsyncTemplateSyncConfigResource,
)
from capo_proton._services._aws_config import aaws_config
from capo_proton._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_proton.types.accept_environment_account_connection_input
    import capo_proton.types.accept_environment_account_connection_output
    import capo_proton.types.arn
    import capo_proton.types.aws_account_id
    import capo_proton.types.cancel_component_deployment_input
    import capo_proton.types.cancel_component_deployment_output
    import capo_proton.types.cancel_environment_deployment_input
    import capo_proton.types.cancel_environment_deployment_output
    import capo_proton.types.cancel_service_instance_deployment_input
    import capo_proton.types.cancel_service_instance_deployment_output
    import capo_proton.types.cancel_service_pipeline_deployment_input
    import capo_proton.types.cancel_service_pipeline_deployment_output
    import capo_proton.types.client_token
    import capo_proton.types.compatible_environment_template_input_list
    import capo_proton.types.component_deployment_update_type
    import capo_proton.types.component_summary
    import capo_proton.types.create_component_input
    import capo_proton.types.create_component_output
    import capo_proton.types.create_environment_account_connection_input
    import capo_proton.types.create_environment_account_connection_output
    import capo_proton.types.create_environment_input
    import capo_proton.types.create_environment_output
    import capo_proton.types.create_environment_template_input
    import capo_proton.types.create_environment_template_output
    import capo_proton.types.create_environment_template_version_input
    import capo_proton.types.create_environment_template_version_output
    import capo_proton.types.create_repository_input
    import capo_proton.types.create_repository_output
    import capo_proton.types.create_service_input
    import capo_proton.types.create_service_instance_input
    import capo_proton.types.create_service_instance_output
    import capo_proton.types.create_service_output
    import capo_proton.types.create_service_sync_config_input
    import capo_proton.types.create_service_sync_config_output
    import capo_proton.types.create_service_template_input
    import capo_proton.types.create_service_template_output
    import capo_proton.types.create_service_template_version_input
    import capo_proton.types.create_service_template_version_output
    import capo_proton.types.create_template_sync_config_input
    import capo_proton.types.create_template_sync_config_output
    import capo_proton.types.delete_component_input
    import capo_proton.types.delete_component_output
    import capo_proton.types.delete_deployment_input
    import capo_proton.types.delete_deployment_output
    import capo_proton.types.delete_environment_account_connection_input
    import capo_proton.types.delete_environment_account_connection_output
    import capo_proton.types.delete_environment_input
    import capo_proton.types.delete_environment_output
    import capo_proton.types.delete_environment_template_input
    import capo_proton.types.delete_environment_template_output
    import capo_proton.types.delete_environment_template_version_input
    import capo_proton.types.delete_environment_template_version_output
    import capo_proton.types.delete_repository_input
    import capo_proton.types.delete_repository_output
    import capo_proton.types.delete_service_input
    import capo_proton.types.delete_service_output
    import capo_proton.types.delete_service_sync_config_input
    import capo_proton.types.delete_service_sync_config_output
    import capo_proton.types.delete_service_template_input
    import capo_proton.types.delete_service_template_output
    import capo_proton.types.delete_service_template_version_input
    import capo_proton.types.delete_service_template_version_output
    import capo_proton.types.delete_template_sync_config_input
    import capo_proton.types.delete_template_sync_config_output
    import capo_proton.types.deployment_id
    import capo_proton.types.deployment_summary
    import capo_proton.types.deployment_update_type
    import capo_proton.types.description
    import capo_proton.types.display_name
    import capo_proton.types.empty_next_token
    import capo_proton.types.environment_account_connection_id
    import capo_proton.types.environment_account_connection_requester_account_type
    import capo_proton.types.environment_account_connection_status_list
    import capo_proton.types.environment_account_connection_summary
    import capo_proton.types.environment_summary
    import capo_proton.types.environment_template_filter_list
    import capo_proton.types.environment_template_summary
    import capo_proton.types.environment_template_version_summary
    import capo_proton.types.get_account_settings_input
    import capo_proton.types.get_account_settings_output
    import capo_proton.types.get_component_input
    import capo_proton.types.get_component_output
    import capo_proton.types.get_deployment_input
    import capo_proton.types.get_deployment_output
    import capo_proton.types.get_environment_account_connection_input
    import capo_proton.types.get_environment_account_connection_output
    import capo_proton.types.get_environment_input
    import capo_proton.types.get_environment_output
    import capo_proton.types.get_environment_template_input
    import capo_proton.types.get_environment_template_output
    import capo_proton.types.get_environment_template_version_input
    import capo_proton.types.get_environment_template_version_output
    import capo_proton.types.get_repository_input
    import capo_proton.types.get_repository_output
    import capo_proton.types.get_repository_sync_status_input
    import capo_proton.types.get_repository_sync_status_output
    import capo_proton.types.get_resources_summary_input
    import capo_proton.types.get_resources_summary_output
    import capo_proton.types.get_service_input
    import capo_proton.types.get_service_instance_input
    import capo_proton.types.get_service_instance_output
    import capo_proton.types.get_service_instance_sync_status_input
    import capo_proton.types.get_service_instance_sync_status_output
    import capo_proton.types.get_service_output
    import capo_proton.types.get_service_sync_blocker_summary_input
    import capo_proton.types.get_service_sync_blocker_summary_output
    import capo_proton.types.get_service_sync_config_input
    import capo_proton.types.get_service_sync_config_output
    import capo_proton.types.get_service_template_input
    import capo_proton.types.get_service_template_output
    import capo_proton.types.get_service_template_version_input
    import capo_proton.types.get_service_template_version_output
    import capo_proton.types.get_template_sync_config_input
    import capo_proton.types.get_template_sync_config_output
    import capo_proton.types.get_template_sync_status_input
    import capo_proton.types.get_template_sync_status_output
    import capo_proton.types.git_branch_name
    import capo_proton.types.list_component_outputs_input
    import capo_proton.types.list_component_outputs_output
    import capo_proton.types.list_component_provisioned_resources_input
    import capo_proton.types.list_component_provisioned_resources_output
    import capo_proton.types.list_components_input
    import capo_proton.types.list_components_output
    import capo_proton.types.list_deployments_input
    import capo_proton.types.list_deployments_output
    import capo_proton.types.list_environment_account_connections_input
    import capo_proton.types.list_environment_account_connections_output
    import capo_proton.types.list_environment_outputs_input
    import capo_proton.types.list_environment_outputs_output
    import capo_proton.types.list_environment_provisioned_resources_input
    import capo_proton.types.list_environment_provisioned_resources_output
    import capo_proton.types.list_environment_template_versions_input
    import capo_proton.types.list_environment_template_versions_output
    import capo_proton.types.list_environment_templates_input
    import capo_proton.types.list_environment_templates_output
    import capo_proton.types.list_environments_input
    import capo_proton.types.list_environments_output
    import capo_proton.types.list_repositories_input
    import capo_proton.types.list_repositories_output
    import capo_proton.types.list_repository_sync_definitions_input
    import capo_proton.types.list_repository_sync_definitions_output
    import capo_proton.types.list_service_instance_outputs_input
    import capo_proton.types.list_service_instance_outputs_output
    import capo_proton.types.list_service_instance_provisioned_resources_input
    import capo_proton.types.list_service_instance_provisioned_resources_output
    import capo_proton.types.list_service_instances_filter_list
    import capo_proton.types.list_service_instances_input
    import capo_proton.types.list_service_instances_output
    import capo_proton.types.list_service_instances_sort_by
    import capo_proton.types.list_service_pipeline_outputs_input
    import capo_proton.types.list_service_pipeline_outputs_output
    import capo_proton.types.list_service_pipeline_provisioned_resources_input
    import capo_proton.types.list_service_pipeline_provisioned_resources_output
    import capo_proton.types.list_service_template_versions_input
    import capo_proton.types.list_service_template_versions_output
    import capo_proton.types.list_service_templates_input
    import capo_proton.types.list_service_templates_output
    import capo_proton.types.list_services_input
    import capo_proton.types.list_services_output
    import capo_proton.types.list_tags_for_resource_input
    import capo_proton.types.list_tags_for_resource_output
    import capo_proton.types.max_page_results
    import capo_proton.types.next_token
    import capo_proton.types.notify_resource_deployment_status_change_input
    import capo_proton.types.notify_resource_deployment_status_change_output
    import capo_proton.types.ops_file_path
    import capo_proton.types.output
    import capo_proton.types.outputs_list
    import capo_proton.types.provisioned_resource
    import capo_proton.types.provisioning
    import capo_proton.types.reject_environment_account_connection_input
    import capo_proton.types.reject_environment_account_connection_output
    import capo_proton.types.repository_branch_input
    import capo_proton.types.repository_id
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider
    import capo_proton.types.repository_summary
    import capo_proton.types.repository_sync_definition
    import capo_proton.types.resource_deployment_status
    import capo_proton.types.resource_name
    import capo_proton.types.resource_name_or_empty
    import capo_proton.types.role_arn
    import capo_proton.types.role_arn_or_empty_string
    import capo_proton.types.service_instance_summary
    import capo_proton.types.service_summary
    import capo_proton.types.service_template_summary
    import capo_proton.types.service_template_supported_component_source_input_list
    import capo_proton.types.service_template_version_summary
    import capo_proton.types.sort_order
    import capo_proton.types.spec_contents
    import capo_proton.types.status_message
    import capo_proton.types.subdirectory
    import capo_proton.types.sync_type
    import capo_proton.types.tag
    import capo_proton.types.tag_key_list
    import capo_proton.types.tag_list
    import capo_proton.types.tag_resource_input
    import capo_proton.types.tag_resource_output
    import capo_proton.types.template_file_contents
    import capo_proton.types.template_manifest_contents
    import capo_proton.types.template_type
    import capo_proton.types.template_version_part
    import capo_proton.types.template_version_source_input
    import capo_proton.types.template_version_status
    import capo_proton.types.untag_resource_input
    import capo_proton.types.untag_resource_output
    import capo_proton.types.update_account_settings_input
    import capo_proton.types.update_account_settings_output
    import capo_proton.types.update_component_input
    import capo_proton.types.update_component_output
    import capo_proton.types.update_environment_account_connection_input
    import capo_proton.types.update_environment_account_connection_output
    import capo_proton.types.update_environment_input
    import capo_proton.types.update_environment_output
    import capo_proton.types.update_environment_template_input
    import capo_proton.types.update_environment_template_output
    import capo_proton.types.update_environment_template_version_input
    import capo_proton.types.update_environment_template_version_output
    import capo_proton.types.update_service_input
    import capo_proton.types.update_service_instance_input
    import capo_proton.types.update_service_instance_output
    import capo_proton.types.update_service_output
    import capo_proton.types.update_service_pipeline_input
    import capo_proton.types.update_service_pipeline_output
    import capo_proton.types.update_service_sync_blocker_input
    import capo_proton.types.update_service_sync_blocker_output
    import capo_proton.types.update_service_sync_config_input
    import capo_proton.types.update_service_sync_config_output
    import capo_proton.types.update_service_template_input
    import capo_proton.types.update_service_template_output
    import capo_proton.types.update_service_template_version_input
    import capo_proton.types.update_service_template_version_output
    import capo_proton.types.update_template_sync_config_input
    import capo_proton.types.update_template_sync_config_output


class AsyncProtonClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncProtonClient:
    """A client for the ``Proton`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = AsyncProtonClientConfig(
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
        self.account_settings_resource = AsyncAccountSettingsResource(self)
        self.component_output_resource = AsyncComponentOutputResource(self)
        self.component_provisioned_resource_resource = (
            AsyncComponentProvisionedResourceResource(self)
        )
        self.component_resource = AsyncComponentResource(self)
        self.deployment_resource = AsyncDeploymentResource(self)
        self.environment_account_connection_resource = (
            AsyncEnvironmentAccountConnectionResource(self)
        )
        self.environment_output_resource = AsyncEnvironmentOutputResource(self)
        self.environment_provisioned_resource_resource = (
            AsyncEnvironmentProvisionedResourceResource(self)
        )
        self.environment_resource = AsyncEnvironmentResource(self)
        self.environment_template_resource = AsyncEnvironmentTemplateResource(self)
        self.environment_template_version_resource = (
            AsyncEnvironmentTemplateVersionResource(self)
        )
        self.repository_resource = AsyncRepositoryResource(self)
        self.service_instance_output_resource = AsyncServiceInstanceOutputResource(self)
        self.service_instance_provisioned_resource_resource = (
            AsyncServiceInstanceProvisionedResourceResource(self)
        )
        self.service_instance_resource = AsyncServiceInstanceResource(self)
        self.service_pipeline_output_resource = AsyncServicePipelineOutputResource(self)
        self.service_pipeline_provisioned_resource_resource = (
            AsyncServicePipelineProvisionedResourceResource(self)
        )
        self.service_pipeline_resource = AsyncServicePipelineResource(self)
        self.service_resource = AsyncServiceResource(self)
        self.service_sync_blocker_resource = AsyncServiceSyncBlockerResource(self)
        self.service_sync_config_resource = AsyncServiceSyncConfigResource(self)
        self.service_template_resource = AsyncServiceTemplateResource(self)
        self.service_template_version_resource = AsyncServiceTemplateVersionResource(
            self
        )
        self.template_sync_config_resource = AsyncTemplateSyncConfigResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncProtonClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncProtonClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def cancel_component_deployment(
        self,
        component_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.cancel_component_deployment_output.CancelComponentDeploymentOutput":
        """<p>Attempts to cancel a component deployment (for a component that is in the <code>IN_PROGRESS</code> deployment status).</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            component_name: <p>The name of the component with the deployment to cancel.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.cancel_component_deployment_input.CancelComponentDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.cancel_component_deployment_output.CancelComponentDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.cancel_component_deployment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.cancel_component_deployment.async_cancel_component_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.cancel_component_deployment_input.CancelComponentDeploymentInput = {
            "component_name": component_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_environment_deployment(
        self,
        environment_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.cancel_environment_deployment_output.CancelEnvironmentDeploymentOutput":
        """<p>Attempts to cancel an environment deployment on an <a>UpdateEnvironment</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-update.html">Update an environment</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateEnvironment</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>

        Args:
            environment_name: <p>The name of the environment with the deployment to cancel.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.cancel_environment_deployment_input.CancelEnvironmentDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.cancel_environment_deployment_output.CancelEnvironmentDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.cancel_environment_deployment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.cancel_environment_deployment.async_cancel_environment_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.cancel_environment_deployment_input.CancelEnvironmentDeploymentInput = {
            "environment_name": environment_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_service_instance_deployment(
        self,
        service_instance_name: "capo_proton.types.resource_name.ResourceName",
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.cancel_service_instance_deployment_output.CancelServiceInstanceDeploymentOutput":
        """<p>Attempts to cancel a service instance deployment on an <a>UpdateServiceInstance</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-update.html">Update a service instance</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateServiceInstance</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>

        Args:
            service_instance_name: <p>The name of the service instance with the deployment to cancel.</p>
            service_name: <p>The name of the service with the service instance deployment to cancel.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.cancel_service_instance_deployment_input.CancelServiceInstanceDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.cancel_service_instance_deployment_output.CancelServiceInstanceDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.cancel_service_instance_deployment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.cancel_service_instance_deployment.async_cancel_service_instance_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.cancel_service_instance_deployment_input.CancelServiceInstanceDeploymentInput = {
            "service_instance_name": service_instance_name,
            "service_name": service_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_service_pipeline_deployment(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.cancel_service_pipeline_deployment_output.CancelServicePipelineDeploymentOutput":
        """<p>Attempts to cancel a service pipeline deployment on an <a>UpdateServicePipeline</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-pipeline-update.html">Update a service pipeline</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateServicePipeline</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>

        Args:
            service_name: <p>The name of the service with the service pipeline deployment to cancel.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.cancel_service_pipeline_deployment_input.CancelServicePipelineDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.cancel_service_pipeline_deployment_output.CancelServicePipelineDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.cancel_service_pipeline_deployment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.cancel_service_pipeline_deployment.async_cancel_service_pipeline_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.cancel_service_pipeline_deployment_input.CancelServicePipelineDeploymentInput = {
            "service_name": service_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_repository_sync_status(
        self,
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        sync_type: "capo_proton.types.sync_type.SyncType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_repository_sync_status_output.GetRepositorySyncStatusOutput":
        """<p>Get the sync status of a repository used for Proton template sync. For more information about template sync, see .</p> <note> <p>A repository sync status isn't tied to the Proton Repository resource (or any other Proton resource). Therefore, tags on an Proton Repository resource have no effect on this action. Specifically, you can't use these tags to control access to this action using Attribute-based access control (ABAC).</p> <p>For more information about ABAC, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags">ABAC</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            repository_name: <p>The repository name.</p>
            repository_provider: <p>The repository provider.</p>
            branch: <p>The repository branch.</p>
            sync_type: <p>The repository sync type.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_repository_sync_status_input.GetRepositorySyncStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_repository_sync_status_output.GetRepositorySyncStatusOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_repository_sync_status

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_repository_sync_status.async_get_repository_sync_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_repository_sync_status_input.GetRepositorySyncStatusInput = {
            "repository_name": repository_name,
            "repository_provider": repository_provider,
            "branch": branch,
            "sync_type": sync_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resources_summary(
        self, *, config_overrides: Optional[AsyncProtonClientConfig] = None
    ) -> "capo_proton.types.get_resources_summary_output.GetResourcesSummaryOutput":
        """<p>Get counts of Proton resources.</p> <p>For infrastructure-provisioning resources (environments, services, service instances, pipelines), the action returns staleness counts. A resource is stale when it's behind the recommended version of the Proton template that it uses and it needs an update to become current.</p> <p>The action returns staleness counts (counts of resources that are up-to-date, behind a template major version, or behind a template minor version), the total number of resources, and the number of resources that are in a failed state, grouped by resource type. Components, environments, and service templates return less information - see the <code>components</code>, <code>environments</code>, and <code>serviceTemplates</code> field descriptions.</p> <p>For context, the action also returns the total number of each type of Proton template in the Amazon Web Services account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/monitoring-dashboard.html">Proton dashboard</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_resources_summary_input.GetResourcesSummaryInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_resources_summary_output.GetResourcesSummaryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_resources_summary

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_resources_summary.async_get_resources_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_resources_summary_input.GetResourcesSummaryInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_instance_sync_status(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        service_instance_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_instance_sync_status_output.GetServiceInstanceSyncStatusOutput":
        """<p>Get the status of the synced service instance.</p>

        Args:
            service_name: <p>The name of the service that the service instance belongs to.</p>
            service_instance_name: <p>The name of the service instance that you want the sync status input for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_service_instance_sync_status_input.GetServiceInstanceSyncStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_service_instance_sync_status_output.GetServiceInstanceSyncStatusOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_instance_sync_status

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_service_instance_sync_status.async_get_service_instance_sync_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_service_instance_sync_status_input.GetServiceInstanceSyncStatusInput = {
            "service_name": service_name,
            "service_instance_name": service_instance_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_template_sync_status(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_type: "capo_proton.types.template_type.TemplateType",
        template_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> (
        "capo_proton.types.get_template_sync_status_output.GetTemplateSyncStatusOutput"
    ):
        """<p>Get the status of a template sync.</p>

        Args:
            template_name: <p>The template name.</p>
            template_type: <p>The template type.</p>
            template_version: <p>The template major version.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_template_sync_status_input.GetTemplateSyncStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_template_sync_status_output.GetTemplateSyncStatusOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_template_sync_status

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_template_sync_status.async_get_template_sync_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_template_sync_status_input.GetTemplateSyncStatusInput = {
            "template_name": template_name,
            "template_type": template_type,
            "template_version": template_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_repository_sync_definitions(
        self,
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        sync_type: "capo_proton.types.sync_type.SyncType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "capo_proton.types.list_repository_sync_definitions_output.ListRepositorySyncDefinitionsOutput":
        """<p>List repository sync definitions with detail data.</p>

        Args:
            repository_name: <p>The repository name.</p>
            repository_provider: <p>The repository provider.</p>
            sync_type: <p>The sync type. The only supported value is <code>TEMPLATE_SYNC</code>.</p>
            next_token: <p>A token that indicates the location of the next repository sync definition in the array of repository sync definitions, after the list of repository sync definitions previously requested.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_repository_sync_definitions_input.ListRepositorySyncDefinitionsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_repository_sync_definitions_output.ListRepositorySyncDefinitionsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_repository_sync_definitions

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_repository_sync_definitions.async_list_repository_sync_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_repository_sync_definitions_input.ListRepositorySyncDefinitionsInput = {
            "repository_name": repository_name,
            "repository_provider": repository_provider,
            "sync_type": sync_type,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_repository_sync_definitions(
        self,
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        sync_type: "capo_proton.types.sync_type.SyncType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.repository_sync_definition.RepositorySyncDefinition]":
        _token = next_token
        while True:
            _response = await self.list_repository_sync_definitions(
                repository_name,
                repository_provider,
                sync_type,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sync_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_proton.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>List tags for a resource. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for the listed tags.</p>
            next_token: <p>A token that indicates the location of the next resource tag in the array of resource tags, after the list of resource tags that was previously requested.</p>
            max_results: <p>The maximum number of tags to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
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

    async def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_proton.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def notify_resource_deployment_status_change(
        self,
        resource_arn: "capo_proton.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        status: Optional[
            "capo_proton.types.resource_deployment_status.ResourceDeploymentStatus"
        ] = None,
        outputs: Optional["capo_proton.types.outputs_list.OutputsList"] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
        status_message: Optional[
            "capo_proton.types.status_message.StatusMessage"
        ] = None,
    ) -> "capo_proton.types.notify_resource_deployment_status_change_output.NotifyResourceDeploymentStatusChangeOutput":
        """<p>Notify Proton of status changes to a provisioned resource when you use self-managed provisioning.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self">Self-managed provisioning</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The provisioned resource Amazon Resource Name (ARN).</p>
            status: <p>The status of your provisioned resource.</p>
            outputs: <p>The provisioned resource state change detail data that's returned by Proton.</p>
            deployment_id: <p>The deployment ID for your provisioned resource.</p>
            status_message: <p>The deployment status message for your provisioned resource.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.notify_resource_deployment_status_change_input.NotifyResourceDeploymentStatusChangeInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.notify_resource_deployment_status_change_output.NotifyResourceDeploymentStatusChangeOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.notify_resource_deployment_status_change

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.notify_resource_deployment_status_change.async_notify_resource_deployment_status_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.notify_resource_deployment_status_change_input.NotifyResourceDeploymentStatusChangeInput = {
            "resource_arn": resource_arn
        }
        if status is not None:
            input_["status"] = status
        if outputs is not None:
            input_["outputs"] = outputs
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id
        if status_message is not None:
            input_["status_message"] = status_message

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_proton.types.arn.Arn",
        tags: "capo_proton.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.tag_resource_output.TagResourceOutput":
        """<p>Tag a resource. A tag is a key-value pair of metadata that you associate with an Proton resource.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Proton resource to apply customer tags to.</p>
            tags: <p>A list of customer tags to apply to the Proton resource.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.tag_resource

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_proton.types.arn.Arn",
        tag_keys: "capo_proton.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.untag_resource_output.UntagResourceOutput":
        """<p>Remove a customer tag from a resource. A tag is a key-value pair of metadata associated with an Proton resource.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove customer tags from.</p>
            tag_keys: <p>A list of customer tag keys that indicate the customer tags to be removed from the resource.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.untag_resource

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.untag_resource_input.UntagResourceInput = {
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

    async def get_account_settings(
        self, *, config_overrides: Optional[AsyncProtonClientConfig] = None
    ) -> "capo_proton.types.get_account_settings_output.GetAccountSettingsOutput":
        """<p>Get detail data for Proton account-wide settings.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_account_settings_input.GetAccountSettingsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_account_settings_output.GetAccountSettingsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_account_settings

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_account_settings.async_get_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_account_settings_input.GetAccountSettingsInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_account_settings(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        pipeline_service_role_arn: Optional[
            "capo_proton.types.role_arn_or_empty_string.RoleArnOrEmptyString"
        ] = None,
        pipeline_provisioning_repository: Optional[
            "capo_proton.types.repository_branch_input.RepositoryBranchInput"
        ] = None,
        delete_pipeline_provisioning_repository: Optional[bool] = None,
        pipeline_codebuild_role_arn: Optional[
            "capo_proton.types.role_arn_or_empty_string.RoleArnOrEmptyString"
        ] = None,
    ) -> "capo_proton.types.update_account_settings_output.UpdateAccountSettingsOutput":
        """<p>Update Proton settings that are used for multiple services in the Amazon Web Services account.</p>

        Args:
            pipeline_service_role_arn: <p>The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. Assumed by Proton for Amazon Web Services-managed provisioning, and by customer-owned automation for self-managed provisioning.</p> <p>To remove a previously configured ARN, specify an empty string.</p>
            pipeline_provisioning_repository: <p>A linked repository for pipeline provisioning. Specify it if you have environments configured for self-managed provisioning with services that include pipelines. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>To remove a previously configured repository, set <code>deletePipelineProvisioningRepository</code> to <code>true</code>, and don't set <code>pipelineProvisioningRepository</code>.</p>
            delete_pipeline_provisioning_repository: <p>Set to <code>true</code> to remove a configured pipeline repository from the account settings. Don't set this field if you are updating the configured pipeline repository.</p>
            pipeline_codebuild_role_arn: <p>The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. Proton assumes this role for CodeBuild-based provisioning.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_account_settings_input.UpdateAccountSettingsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_account_settings_output.UpdateAccountSettingsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_account_settings

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_account_settings.async_update_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_account_settings_input.UpdateAccountSettingsInput = {}
        if pipeline_service_role_arn is not None:
            input_["pipeline_service_role_arn"] = pipeline_service_role_arn
        if pipeline_provisioning_repository is not None:
            input_["pipeline_provisioning_repository"] = (
                pipeline_provisioning_repository
            )
        if delete_pipeline_provisioning_repository is not None:
            input_["delete_pipeline_provisioning_repository"] = (
                delete_pipeline_provisioning_repository
            )
        if pipeline_codebuild_role_arn is not None:
            input_["pipeline_codebuild_role_arn"] = pipeline_codebuild_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_component_outputs(
        self,
        component_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
    ) -> "capo_proton.types.list_component_outputs_output.ListComponentOutputsOutput":
        """<p>Get a list of component Infrastructure as Code (IaC) outputs.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            component_name: <p>The name of the component whose outputs you want.</p>
            next_token: <p>A token that indicates the location of the next output in the array of outputs, after the list of outputs that was previously requested.</p>
            deployment_id: <p>The ID of the deployment whose outputs you want.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_component_outputs_input.ListComponentOutputsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_component_outputs_output.ListComponentOutputsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_component_outputs

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_component_outputs.async_list_component_outputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_component_outputs_input.ListComponentOutputsInput = {
            "component_name": component_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_component_outputs(
        self,
        component_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
    ) -> "AsyncIterator[capo_proton.types.output.Output]":
        _token = next_token
        while True:
            _response = await self.list_component_outputs(
                component_name,
                config_overrides=config_overrides,
                next_token=_token,
                deployment_id=deployment_id,
            )
            _page = _resolve_path(_response, ("outputs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_component_provisioned_resources(
        self,
        component_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "capo_proton.types.list_component_provisioned_resources_output.ListComponentProvisionedResourcesOutput":
        """<p>List provisioned resources for a component with details.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            component_name: <p>The name of the component whose provisioned resources you want.</p>
            next_token: <p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_component_provisioned_resources_input.ListComponentProvisionedResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_component_provisioned_resources_output.ListComponentProvisionedResourcesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_component_provisioned_resources

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_component_provisioned_resources.async_list_component_provisioned_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_component_provisioned_resources_input.ListComponentProvisionedResourcesInput = {
            "component_name": component_name
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_component_provisioned_resources(
        self,
        component_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.provisioned_resource.ProvisionedResource]":
        _token = next_token
        while True:
            _response = await self.list_component_provisioned_resources(
                component_name,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("provisioned_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_component(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        template_file: "capo_proton.types.template_file_contents.TemplateFileContents",
        manifest: "capo_proton.types.template_manifest_contents.TemplateManifestContents",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        service_spec: Optional["capo_proton.types.spec_contents.SpecContents"] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
    ) -> "capo_proton.types.create_component_output.CreateComponentOutput":
        """<p>Create an Proton component. A component is an infrastructure extension for a service instance.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The customer-provided name of the component.</p>
            description: <p>An optional customer-provided description of the component.</p>
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated with. If you don't specify this, the component isn't attached to any service instance. Specify both <code>serviceInstanceName</code> and <code>serviceName</code> or neither of them.</p>
            service_instance_name: <p>The name of the service instance that you want to attach this component to. If you don't specify this, the component isn't attached to any service instance. Specify both <code>serviceInstanceName</code> and <code>serviceName</code> or neither of them.</p>
            environment_name: <p>The name of the Proton environment that you want to associate this component with. You must specify this when you don't specify <code>serviceInstanceName</code> and <code>serviceName</code>.</p>
            template_file: <p>A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.</p> <note> <p>Components support a single IaC file, even if you use Terraform as your template language.</p> </note>
            manifest: <p>A path to a manifest file that lists the Infrastructure as Code (IaC) file, template language, and rendering engine for infrastructure that a custom component provisions.</p>
            service_spec: <p>The service spec that you want the component to use to access service inputs. Set this only when you attach the component to a service instance.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton component. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            client_token: <p>The client token for the created component.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_component_input.CreateComponentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_component_output.CreateComponentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_component

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_component.async_create_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_component_input.CreateComponentInput = {
            "name": name,
            "template_file": template_file,
            "manifest": manifest,
        }
        if description is not None:
            input_["description"] = description
        if service_name is not None:
            input_["service_name"] = service_name
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if service_spec is not None:
            input_["service_spec"] = service_spec
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

    async def get_component(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_component_output.GetComponentOutput":
        """<p>Get detailed data for a component.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the component that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_component_input.GetComponentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_component_output.GetComponentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_component

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_component.async_get_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_component_input.GetComponentInput = {"name": name}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_component(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        deployment_type: "capo_proton.types.component_deployment_update_type.ComponentDeploymentUpdateType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        service_name: Optional[
            "capo_proton.types.resource_name_or_empty.ResourceNameOrEmpty"
        ] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name_or_empty.ResourceNameOrEmpty"
        ] = None,
        service_spec: Optional["capo_proton.types.spec_contents.SpecContents"] = None,
        template_file: Optional[
            "capo_proton.types.template_file_contents.TemplateFileContents"
        ] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
    ) -> "capo_proton.types.update_component_output.UpdateComponentOutput":
        """<p>Update a component.</p> <p>There are a few modes for updating a component. The <code>deploymentType</code> field defines the mode.</p> <note> <p>You can't update a component while its deployment status, or the deployment status of a service instance attached to it, is <code>IN_PROGRESS</code>.</p> </note> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the component to update.</p>
            deployment_type: <p>The deployment type. It defines the mode for updating a component, as follows:</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated. You can only specify <code>description</code> in this mode.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the component is deployed and updated with the new <code>serviceSpec</code>, <code>templateSource</code>, and/or <code>type</code> that you provide. Only requested parameters are updated.</p> </dd> </dl>
            description: <p>An optional customer-provided description of the component.</p>
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated with. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both <code>serviceInstanceName</code> and <code>serviceName</code> or for neither of them.</p>
            service_instance_name: <p>The name of the service instance that you want to attach this component to. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both <code>serviceInstanceName</code> and <code>serviceName</code> or for neither of them.</p>
            service_spec: <p>The service spec that you want the component to use to access service inputs. Set this only when the component is attached to a service instance.</p>
            template_file: <p>A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.</p> <note> <p>Components support a single IaC file, even if you use Terraform as your template language.</p> </note>
            client_token: <p>The client token for the updated component.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_component_input.UpdateComponentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_component_output.UpdateComponentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_component

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_component.async_update_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_component_input.UpdateComponentInput = {
            "name": name,
            "deployment_type": deployment_type,
        }
        if description is not None:
            input_["description"] = description
        if service_name is not None:
            input_["service_name"] = service_name
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name
        if service_spec is not None:
            input_["service_spec"] = service_spec
        if template_file is not None:
            input_["template_file"] = template_file
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
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_component_output.DeleteComponentOutput":
        """<p>Delete an Proton component resource.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the component to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_component_input.DeleteComponentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_component_output.DeleteComponentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_component

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_component.async_delete_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_component_input.DeleteComponentInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_components(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_components_output.ListComponentsOutput":
        """<p>List components with summary data. You can filter the result list by environment, service, or a single service instance.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            next_token: <p>A token that indicates the location of the next component in the array of components, after the list of components that was previously requested.</p>
            environment_name: <p>The name of an environment for result list filtering. Proton returns components associated with the environment or attached to service instances running in it.</p>
            service_name: <p>The name of a service for result list filtering. Proton returns components attached to service instances of the service.</p>
            service_instance_name: <p>The name of a service instance for result list filtering. Proton returns the component attached to the service instance, if any.</p>
            max_results: <p>The maximum number of components to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_components_input.ListComponentsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_components_output.ListComponentsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_components

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_components.async_list_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_components_input.ListComponentsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if service_name is not None:
            input_["service_name"] = service_name
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name
        if max_results is not None:
            input_["max_results"] = max_results

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
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.component_summary.ComponentSummary]":
        _token = next_token
        while True:
            _response = await self.list_components(
                config_overrides=config_overrides,
                next_token=_token,
                environment_name=environment_name,
                service_name=service_name,
                service_instance_name=service_instance_name,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("components",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_deployment(
        self,
        id: "capo_proton.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        component_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
    ) -> "capo_proton.types.get_deployment_output.GetDeploymentOutput":
        """<p>Get detailed data for a deployment.</p>

        Args:
            id: <p>The ID of the deployment that you want to get the detailed data for.</p>
            environment_name: <p>The name of a environment that you want to get the detailed data for.</p>
            service_name: <p>The name of the service associated with the given deployment ID.</p>
            service_instance_name: <p>The name of the service instance associated with the given deployment ID. <code>serviceName</code> must be specified to identify the service instance.</p>
            component_name: <p>The name of a component that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_deployment_input.GetDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_deployment_output.GetDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_deployment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_deployment.async_get_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_deployment_input.GetDeploymentInput = {"id": id}
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if service_name is not None:
            input_["service_name"] = service_name
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name
        if component_name is not None:
            input_["component_name"] = component_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_deployment(
        self,
        id: "capo_proton.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_deployment_output.DeleteDeploymentOutput":
        """<p>Delete the deployment.</p>

        Args:
            id: <p>The ID of the deployment to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_deployment_input.DeleteDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_deployment_output.DeleteDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_deployment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_deployment.async_delete_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_deployment_input.DeleteDeploymentInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_deployments(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        component_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_deployments_output.ListDeploymentsOutput":
        """<p>List deployments. You can filter the result list by environment, service, or a single service instance.</p>

        Args:
            next_token: <p>A token that indicates the location of the next deployment in the array of deployment, after the list of deployment that was previously requested.</p>
            environment_name: <p>The name of an environment for result list filtering. Proton returns deployments associated with the environment.</p>
            service_name: <p>The name of a service for result list filtering. Proton returns deployments associated with service instances of the service.</p>
            service_instance_name: <p>The name of a service instance for result list filtering. Proton returns the deployments associated with the service instance.</p>
            component_name: <p>The name of a component for result list filtering. Proton returns deployments associated with that component.</p>
            max_results: <p>The maximum number of deployments to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_deployments_input.ListDeploymentsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_deployments_output.ListDeploymentsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_deployments

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_deployments.async_list_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_deployments_input.ListDeploymentsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if service_name is not None:
            input_["service_name"] = service_name
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name
        if component_name is not None:
            input_["component_name"] = component_name
        if max_results is not None:
            input_["max_results"] = max_results

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
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        component_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.deployment_summary.DeploymentSummary]":
        _token = next_token
        while True:
            _response = await self.list_deployments(
                config_overrides=config_overrides,
                next_token=_token,
                environment_name=environment_name,
                service_name=service_name,
                service_instance_name=service_instance_name,
                component_name=component_name,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("deployments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_environment_account_connection(
        self,
        management_account_id: "capo_proton.types.aws_account_id.AwsAccountId",
        environment_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
        role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.create_environment_account_connection_output.CreateEnvironmentAccountConnectionOutput":
        """<p>Create an environment account connection in an environment account so that environment infrastructure resources can be provisioned in the environment account from a management account.</p> <p>An environment account connection is a secure bi-directional connection between a <i>management account</i> and an <i>environment account</i> that maintains authorization and permissions. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            client_token: <p>When included, if two identical requests are made with the same client token, Proton returns the environment account connection that the first request created.</p>
            management_account_id: <p>The ID of the management account that accepts or rejects the environment account connection. You create and manage the Proton environment in this account. If the management account accepts the environment account connection, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that's created in the environment account. Proton uses this role to provision infrastructure resources in the associated environment account.</p>
            environment_name: <p>The name of the Proton environment that's created in the associated management account.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment account connection. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>You must specify <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in this account.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_environment_account_connection_input.CreateEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_environment_account_connection_output.CreateEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_environment_account_connection.async_create_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_environment_account_connection_input.CreateEnvironmentAccountConnectionInput = {
            "management_account_id": management_account_id,
            "environment_name": environment_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
        if component_role_arn is not None:
            input_["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input_["codebuild_role_arn"] = codebuild_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment_account_connection(
        self,
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_environment_account_connection_output.GetEnvironmentAccountConnectionOutput":
        """<p>In an environment account, get the detailed data for an environment account connection.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_environment_account_connection_input.GetEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_environment_account_connection_output.GetEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_environment_account_connection.async_get_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_environment_account_connection_input.GetEnvironmentAccountConnectionInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_environment_account_connection(
        self,
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.update_environment_account_connection_output.UpdateEnvironmentAccountConnectionOutput":
        """<p>In an environment account, update an environment account connection to use a new IAM role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to update.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that's associated with the environment account connection to update.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>The environment account connection must have a <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in the account.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_environment_account_connection_input.UpdateEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_environment_account_connection_output.UpdateEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_environment_account_connection.async_update_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_environment_account_connection_input.UpdateEnvironmentAccountConnectionInput = {
            "id": id
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if component_role_arn is not None:
            input_["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input_["codebuild_role_arn"] = codebuild_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment_account_connection(
        self,
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_environment_account_connection_output.DeleteEnvironmentAccountConnectionOutput":
        """<p>In an environment account, delete an environment account connection.</p> <p>After you delete an environment account connection that’s in use by an Proton environment, Proton <i>can’t</i> manage the environment infrastructure resources until a new environment account connection is accepted for the environment account and associated environment. You're responsible for cleaning up provisioned resources that remain without an environment connection.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_environment_account_connection_input.DeleteEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_environment_account_connection_output.DeleteEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_environment_account_connection.async_delete_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_environment_account_connection_input.DeleteEnvironmentAccountConnectionInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_environment_account_connections(
        self,
        requested_by: "capo_proton.types.environment_account_connection_requester_account_type.EnvironmentAccountConnectionRequesterAccountType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        statuses: Optional[
            "capo_proton.types.environment_account_connection_status_list.EnvironmentAccountConnectionStatusList"
        ] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_environment_account_connections_output.ListEnvironmentAccountConnectionsOutput":
        """<p>View a list of environment account connections.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            requested_by: <p>The type of account making the <code>ListEnvironmentAccountConnections</code> request.</p>
            environment_name: <p>The environment name that's associated with each listed environment account connection.</p>
            statuses: <p>The status details for each listed environment account connection.</p>
            next_token: <p>A token that indicates the location of the next environment account connection in the array of environment account connections, after the list of environment account connections that was previously requested.</p>
            max_results: <p>The maximum number of environment account connections to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_environment_account_connections_input.ListEnvironmentAccountConnectionsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_environment_account_connections_output.ListEnvironmentAccountConnectionsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environment_account_connections

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_environment_account_connections.async_list_environment_account_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_environment_account_connections_input.ListEnvironmentAccountConnectionsInput = {
            "requested_by": requested_by
        }
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if statuses is not None:
            input_["statuses"] = statuses
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

    async def iter_list_environment_account_connections(
        self,
        requested_by: "capo_proton.types.environment_account_connection_requester_account_type.EnvironmentAccountConnectionRequesterAccountType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        statuses: Optional[
            "capo_proton.types.environment_account_connection_status_list.EnvironmentAccountConnectionStatusList"
        ] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.environment_account_connection_summary.EnvironmentAccountConnectionSummary]":
        _token = next_token
        while True:
            _response = await self.list_environment_account_connections(
                requested_by,
                config_overrides=config_overrides,
                environment_name=environment_name,
                statuses=statuses,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("environment_account_connections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def accept_environment_account_connection(
        self,
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.accept_environment_account_connection_output.AcceptEnvironmentAccountConnectionOutput":
        """<p>In a management account, an environment account connection request is accepted. When the environment account connection request is accepted, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.accept_environment_account_connection_input.AcceptEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.accept_environment_account_connection_output.AcceptEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.accept_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.accept_environment_account_connection.async_accept_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.accept_environment_account_connection_input.AcceptEnvironmentAccountConnectionInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_environment_account_connection(
        self,
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.reject_environment_account_connection_output.RejectEnvironmentAccountConnectionOutput":
        """<p>In a management account, reject an environment account connection from another environment account.</p> <p>After you reject an environment account connection request, you <i>can't</i> accept or use the rejected environment account connection.</p> <p>You <i>can’t</i> reject an environment account connection that's connected to an environment.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to reject.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.reject_environment_account_connection_input.RejectEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.reject_environment_account_connection_output.RejectEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.reject_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.reject_environment_account_connection.async_reject_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.reject_environment_account_connection_input.RejectEnvironmentAccountConnectionInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_environment_outputs(
        self,
        environment_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
    ) -> (
        "capo_proton.types.list_environment_outputs_output.ListEnvironmentOutputsOutput"
    ):
        """<p>List the infrastructure as code outputs for your environment.</p>

        Args:
            environment_name: <p>The environment name.</p>
            next_token: <p>A token that indicates the location of the next environment output in the array of environment outputs, after the list of environment outputs that was previously requested.</p>
            deployment_id: <p>The ID of the deployment whose outputs you want.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_environment_outputs_input.ListEnvironmentOutputsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_environment_outputs_output.ListEnvironmentOutputsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environment_outputs

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_environment_outputs.async_list_environment_outputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_environment_outputs_input.ListEnvironmentOutputsInput = {
            "environment_name": environment_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_environment_outputs(
        self,
        environment_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
    ) -> "AsyncIterator[capo_proton.types.output.Output]":
        _token = next_token
        while True:
            _response = await self.list_environment_outputs(
                environment_name,
                config_overrides=config_overrides,
                next_token=_token,
                deployment_id=deployment_id,
            )
            _page = _resolve_path(_response, ("outputs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_environment_provisioned_resources(
        self,
        environment_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "capo_proton.types.list_environment_provisioned_resources_output.ListEnvironmentProvisionedResourcesOutput":
        """<p>List the provisioned resources for your environment.</p>

        Args:
            environment_name: <p>The environment name.</p>
            next_token: <p>A token that indicates the location of the next environment provisioned resource in the array of environment provisioned resources, after the list of environment provisioned resources that was previously requested.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_environment_provisioned_resources_input.ListEnvironmentProvisionedResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_environment_provisioned_resources_output.ListEnvironmentProvisionedResourcesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environment_provisioned_resources

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_environment_provisioned_resources.async_list_environment_provisioned_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_environment_provisioned_resources_input.ListEnvironmentProvisionedResourcesInput = {
            "environment_name": environment_name
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_environment_provisioned_resources(
        self,
        environment_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.provisioned_resource.ProvisionedResource]":
        _token = next_token
        while True:
            _response = await self.list_environment_provisioned_resources(
                environment_name,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("provisioned_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_environment(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        spec: "capo_proton.types.spec_contents.SpecContents",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        proton_service_role_arn: Optional["capo_proton.types.arn.Arn"] = None,
        environment_account_connection_id: Optional[
            "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
        provisioning_repository: Optional[
            "capo_proton.types.repository_branch_input.RepositoryBranchInput"
        ] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.create_environment_output.CreateEnvironmentOutput":
        """<p>Deploy a new environment. An Proton environment is created from an environment template that defines infrastructure and resources that can be shared across services.</p> <p class="title"> <b>You can provision environments using the following methods:</b> </p> <ul> <li> <p>Amazon Web Services-managed provisioning: Proton makes direct calls to provision your resources.</p> </li> <li> <p>Self-managed provisioning: Proton makes pull requests on your repository to provide compiled infrastructure as code (IaC) files that your IaC engine uses to provision resources.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html">Environments</a> and <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html">Provisioning methods</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the environment.</p>
            template_name: <p>The name of the environment template. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html">Environment Templates</a> in the <i>Proton User Guide</i>.</p>
            template_major_version: <p>The major version of the environment template.</p>
            template_minor_version: <p>The minor version of the environment template.</p>
            description: <p>A description of the environment that's being created and deployed.</p>
            spec: <p>A YAML formatted string that provides inputs as defined in the environment template bundle schema file. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html">Environments</a> in the <i>Proton User Guide</i>.</p>
            proton_service_role_arn: <p>The Amazon Resource Name (ARN) of the Proton service role that allows Proton to make calls to other services on your behalf.</p> <p>To use Amazon Web Services-managed provisioning for the environment, specify either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and omit the <code>provisioningRepository</code> parameter.</p>
            environment_account_connection_id: <p>The ID of the environment account connection that you provide if you're provisioning your environment infrastructure resources to an environment account. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p> <p>To use Amazon Web Services-managed provisioning for the environment, specify either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and omit the <code>provisioningRepository</code> parameter.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            provisioning_repository: <p>The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>To use self-managed provisioning for the environment, specify this parameter and omit the <code>environmentAccountConnectionId</code> and <code>protonServiceRoleArn</code> parameters.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.</p> <p>You must specify <code>componentRoleArn</code> to allow directly defined components to be associated with this environment.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that allows Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.</p> <p>To use CodeBuild-based provisioning for the environment or for any service instance running in the environment, specify either the <code>environmentAccountConnectionId</code> or <code>codebuildRoleArn</code> parameter.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_environment_input.CreateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_environment_output.CreateEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_environment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_environment.async_create_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_environment_input.CreateEnvironmentInput = {
            "name": name,
            "template_name": template_name,
            "template_major_version": template_major_version,
            "spec": spec,
        }
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version
        if description is not None:
            input_["description"] = description
        if proton_service_role_arn is not None:
            input_["proton_service_role_arn"] = proton_service_role_arn
        if environment_account_connection_id is not None:
            input_["environment_account_connection_id"] = (
                environment_account_connection_id
            )
        if tags is not None:
            input_["tags"] = tags
        if provisioning_repository is not None:
            input_["provisioning_repository"] = provisioning_repository
        if component_role_arn is not None:
            input_["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input_["codebuild_role_arn"] = codebuild_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_environment_output.GetEnvironmentOutput":
        """<p>Get detailed data for an environment.</p>

        Args:
            name: <p>The name of the environment that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_environment_input.GetEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_environment_output.GetEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_environment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_environment.async_get_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_environment_input.GetEnvironmentInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_environment(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        deployment_type: "capo_proton.types.deployment_update_type.DeploymentUpdateType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        spec: Optional["capo_proton.types.spec_contents.SpecContents"] = None,
        template_major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        proton_service_role_arn: Optional["capo_proton.types.arn.Arn"] = None,
        environment_account_connection_id: Optional[
            "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
        ] = None,
        provisioning_repository: Optional[
            "capo_proton.types.repository_branch_input.RepositoryBranchInput"
        ] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.update_environment_output.UpdateEnvironmentOutput":
        """<p>Update an environment.</p> <p>If the environment is associated with an environment account connection, <i>don't</i> update or include the <code>protonServiceRoleArn</code> and <code>provisioningRepository</code> parameter to update or connect to an environment account connection.</p> <p>You can only update to a new environment account connection if that connection was created in the same environment account that the current environment account connection was created in. The account connection must also be associated with the current environment.</p> <p>If the environment <i>isn't</i> associated with an environment account connection, <i>don't</i> update or include the <code>environmentAccountConnectionId</code> parameter. You <i>can't</i> update or connect the environment to an environment account connection if it <i>isn't</i> already associated with an environment connection.</p> <p>You can update either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and value. You can’t update both.</p> <p>If the environment was configured for Amazon Web Services-managed provisioning, omit the <code>provisioningRepository</code> parameter.</p> <p>If the environment was configured for self-managed provisioning, specify the <code>provisioningRepository</code> parameter and omit the <code>protonServiceRoleArn</code> and <code>environmentAccountConnectionId</code> parameters.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html">Environments</a> and <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html">Provisioning methods</a> in the <i>Proton User Guide</i>.</p> <p>There are four modes for updating an environment. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include minor or major version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>

        Args:
            name: <p>The name of the environment to update.</p>
            description: <p>A description of the environment update.</p>
            spec: <p>The formatted specification that defines the update.</p>
            template_major_version: <p>The major version of the environment to update.</p>
            template_minor_version: <p>The minor version of the environment to update.</p>
            proton_service_role_arn: <p>The Amazon Resource Name (ARN) of the Proton service role that allows Proton to make API calls to other services your behalf.</p>
            deployment_type: <p>There are four modes for updating an environment. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that is higher than the major version in use and a minor version (optional).</p> </dd> </dl>
            environment_account_connection_id: <p>The ID of the environment account connection.</p> <p>You can only update to a new environment account connection if it was created in the same environment account that the current environment account connection was created in and is associated with the current environment.</p>
            provisioning_repository: <p>The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.</p> <p>The environment must have a <code>componentRoleArn</code> to allow directly defined components to be associated with the environment.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that allows Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_environment_input.UpdateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_environment_output.UpdateEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_environment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_environment.async_update_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_environment_input.UpdateEnvironmentInput = {
            "name": name,
            "deployment_type": deployment_type,
        }
        if description is not None:
            input_["description"] = description
        if spec is not None:
            input_["spec"] = spec
        if template_major_version is not None:
            input_["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version
        if proton_service_role_arn is not None:
            input_["proton_service_role_arn"] = proton_service_role_arn
        if environment_account_connection_id is not None:
            input_["environment_account_connection_id"] = (
                environment_account_connection_id
            )
        if provisioning_repository is not None:
            input_["provisioning_repository"] = provisioning_repository
        if component_role_arn is not None:
            input_["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input_["codebuild_role_arn"] = codebuild_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_environment_output.DeleteEnvironmentOutput":
        """<p>Delete an environment.</p>

        Args:
            name: <p>The name of the environment to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_environment_input.DeleteEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_environment_output.DeleteEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_environment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_environment.async_delete_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_environment_input.DeleteEnvironmentInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_environments(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        environment_templates: Optional[
            "capo_proton.types.environment_template_filter_list.EnvironmentTemplateFilterList"
        ] = None,
    ) -> "capo_proton.types.list_environments_output.ListEnvironmentsOutput":
        """<p>List environments with detail data summaries.</p>

        Args:
            next_token: <p>A token that indicates the location of the next environment in the array of environments, after the list of environments that was previously requested.</p>
            max_results: <p>The maximum number of environments to list.</p>
            environment_templates: <p>An array of the versions of the environment template.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_environments_input.ListEnvironmentsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_environments_output.ListEnvironmentsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environments

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_environments.async_list_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_environments_input.ListEnvironmentsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if environment_templates is not None:
            input_["environment_templates"] = environment_templates

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_environments(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        environment_templates: Optional[
            "capo_proton.types.environment_template_filter_list.EnvironmentTemplateFilterList"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.environment_summary.EnvironmentSummary]":
        _token = next_token
        while True:
            _response = await self.list_environments(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                environment_templates=environment_templates,
            )
            _page = _resolve_path(_response, ("environments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_environment_template(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        display_name: Optional["capo_proton.types.display_name.DisplayName"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        encryption_key: Optional["capo_proton.types.arn.Arn"] = None,
        provisioning: Optional["capo_proton.types.provisioning.Provisioning"] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
    ) -> "capo_proton.types.create_environment_template_output.CreateEnvironmentTemplateOutput":
        """<p>Create an environment template for Proton. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html">Environment Templates</a> in the <i>Proton User Guide</i>.</p> <p>You can create an environment template in one of the two following ways:</p> <ul> <li> <p>Register and publish a <i>standard</i> environment template that instructs Proton to deploy and manage environment infrastructure.</p> </li> <li> <p>Register and publish a <i>customer managed</i> environment template that connects Proton to your existing provisioned infrastructure that you manage. Proton <i>doesn't</i> manage your existing provisioned infrastructure. To create an environment template for customer provisioned and managed infrastructure, include the <code>provisioning</code> parameter and set the value to <code>CUSTOMER_MANAGED</code>. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/template-create.html">Register and publish an environment template</a> in the <i>Proton User Guide</i>.</p> </li> </ul>

        Args:
            name: <p>The name of the environment template.</p>
            display_name: <p>The environment template name as displayed in the developer interface.</p>
            description: <p>A description of the environment template.</p>
            encryption_key: <p>A customer provided encryption key that Proton uses to encrypt data.</p>
            provisioning: <p>When included, indicates that the environment template is for customer provisioned and managed infrastructure.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment template. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_environment_template_input.CreateEnvironmentTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_environment_template_output.CreateEnvironmentTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_environment_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_environment_template.async_create_environment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_environment_template_input.CreateEnvironmentTemplateInput = {
            "name": name
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if provisioning is not None:
            input_["provisioning"] = provisioning
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment_template(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> (
        "capo_proton.types.get_environment_template_output.GetEnvironmentTemplateOutput"
    ):
        """<p>Get detailed data for an environment template.</p>

        Args:
            name: <p>The name of the environment template that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_environment_template_input.GetEnvironmentTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_environment_template_output.GetEnvironmentTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_environment_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_environment_template.async_get_environment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_environment_template_input.GetEnvironmentTemplateInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_environment_template(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        display_name: Optional["capo_proton.types.display_name.DisplayName"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
    ) -> "capo_proton.types.update_environment_template_output.UpdateEnvironmentTemplateOutput":
        """<p>Update an environment template.</p>

        Args:
            name: <p>The name of the environment template to update.</p>
            display_name: <p>The name of the environment template to update as displayed in the developer interface.</p>
            description: <p>A description of the environment template update.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_environment_template_input.UpdateEnvironmentTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_environment_template_output.UpdateEnvironmentTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_environment_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_environment_template.async_update_environment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_environment_template_input.UpdateEnvironmentTemplateInput = {
            "name": name
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment_template(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_environment_template_output.DeleteEnvironmentTemplateOutput":
        """<p>If no other major or minor versions of an environment template exist, delete the environment template.</p>

        Args:
            name: <p>The name of the environment template to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_environment_template_input.DeleteEnvironmentTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_environment_template_output.DeleteEnvironmentTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_environment_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_environment_template.async_delete_environment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_environment_template_input.DeleteEnvironmentTemplateInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_environment_templates(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_environment_templates_output.ListEnvironmentTemplatesOutput":
        """<p>List environment templates.</p>

        Args:
            next_token: <p>A token that indicates the location of the next environment template in the array of environment templates, after the list of environment templates that was previously requested.</p>
            max_results: <p>The maximum number of environment templates to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_environment_templates_input.ListEnvironmentTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_environment_templates_output.ListEnvironmentTemplatesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environment_templates

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_environment_templates.async_list_environment_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_environment_templates_input.ListEnvironmentTemplatesInput = {}
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

    async def iter_list_environment_templates(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.environment_template_summary.EnvironmentTemplateSummary]":
        _token = next_token
        while True:
            _response = await self.list_environment_templates(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_environment_template_version(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        source: "capo_proton.types.template_version_source_input.TemplateVersionSourceInput",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
    ) -> "capo_proton.types.create_environment_template_version_output.CreateEnvironmentTemplateVersionOutput":
        """<p>Create a new major or minor version of an environment template. A major version of an environment template is a version that <i>isn't</i> backwards compatible. A minor version of an environment template is a version that's backwards compatible within its major version.</p>

        Args:
            client_token: <p>When included, if two identical requests are made with the same client token, Proton returns the environment template version that the first request created.</p>
            template_name: <p>The name of the environment template.</p>
            description: <p>A description of the new version of an environment template.</p>
            major_version: <p>To create a new minor version of the environment template, include <code>major Version</code>.</p> <p>To create a new major and minor version of the environment template, exclude <code>major Version</code>.</p>
            source: <p>An object that includes the template bundle S3 bucket path and name for the new version of an template.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment template version. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_environment_template_version_input.CreateEnvironmentTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_environment_template_version_output.CreateEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_environment_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_environment_template_version.async_create_environment_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_environment_template_version_input.CreateEnvironmentTemplateVersionInput = {
            "template_name": template_name,
            "source": source,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if major_version is not None:
            input_["major_version"] = major_version
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment_template_version(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_environment_template_version_output.GetEnvironmentTemplateVersionOutput":
        """<p>Get detailed data for a major or minor version of an environment template.</p>

        Args:
            template_name: <p>The name of the environment template a version of which you want to get detailed data for.</p>
            major_version: <p>To get environment template major version detail data, include <code>major Version</code>.</p>
            minor_version: <p>To get environment template minor version detail data, include <code>minorVersion</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_environment_template_version_input.GetEnvironmentTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_environment_template_version_output.GetEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_environment_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_environment_template_version.async_get_environment_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_environment_template_version_input.GetEnvironmentTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_environment_template_version(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        status: Optional[
            "capo_proton.types.template_version_status.TemplateVersionStatus"
        ] = None,
    ) -> "capo_proton.types.update_environment_template_version_output.UpdateEnvironmentTemplateVersionOutput":
        """<p>Update a major or minor version of an environment template.</p>

        Args:
            template_name: <p>The name of the environment template.</p>
            major_version: <p>To update a major version of an environment template, include <code>major Version</code>.</p>
            minor_version: <p>To update a minor version of an environment template, include <code>minorVersion</code>.</p>
            description: <p>A description of environment template version to update.</p>
            status: <p>The status of the environment template minor version to update.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_environment_template_version_input.UpdateEnvironmentTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_environment_template_version_output.UpdateEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_environment_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_environment_template_version.async_update_environment_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_environment_template_version_input.UpdateEnvironmentTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment_template_version(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_environment_template_version_output.DeleteEnvironmentTemplateVersionOutput":
        """<p>If no other minor versions of an environment template exist, delete a major version of the environment template if it's not the <code>Recommended</code> version. Delete the <code>Recommended</code> version of the environment template if no other major versions or minor versions of the environment template exist. A major version of an environment template is a version that's not backward compatible.</p> <p>Delete a minor version of an environment template if it <i>isn't</i> the <code>Recommended</code> version. Delete a <code>Recommended</code> minor version of the environment template if no other minor versions of the environment template exist. A minor version of an environment template is a version that's backward compatible.</p>

        Args:
            template_name: <p>The name of the environment template.</p>
            major_version: <p>The environment template major version to delete.</p>
            minor_version: <p>The environment template minor version to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_environment_template_version_input.DeleteEnvironmentTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_environment_template_version_output.DeleteEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_environment_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_environment_template_version.async_delete_environment_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_environment_template_version_input.DeleteEnvironmentTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_environment_template_versions(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
    ) -> "capo_proton.types.list_environment_template_versions_output.ListEnvironmentTemplateVersionsOutput":
        """<p>List major or minor versions of an environment template with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next major or minor version in the array of major or minor versions of an environment template, after the list of major or minor versions that was previously requested.</p>
            max_results: <p>The maximum number of major or minor versions of an environment template to list.</p>
            template_name: <p>The name of the environment template.</p>
            major_version: <p>To view a list of minor of versions under a major version of an environment template, include <code>major Version</code>.</p> <p>To view a list of major versions of an environment template, <i>exclude</i> <code>major Version</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_environment_template_versions_input.ListEnvironmentTemplateVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_environment_template_versions_output.ListEnvironmentTemplateVersionsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environment_template_versions

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_environment_template_versions.async_list_environment_template_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_environment_template_versions_input.ListEnvironmentTemplateVersionsInput = {
            "template_name": template_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if major_version is not None:
            input_["major_version"] = major_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_environment_template_versions(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.environment_template_version_summary.EnvironmentTemplateVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_environment_template_versions(
                template_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                major_version=major_version,
            )
            _page = _resolve_path(_response, ("template_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_repository(
        self,
        provider: "capo_proton.types.repository_provider.RepositoryProvider",
        name: "capo_proton.types.repository_name.RepositoryName",
        connection_arn: "capo_proton.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        encryption_key: Optional["capo_proton.types.arn.Arn"] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
    ) -> "capo_proton.types.create_repository_output.CreateRepositoryOutput":
        """<p>Create and register a link to a repository. Proton uses the link to repeatedly access the repository, to either push to it (self-managed provisioning) or pull from it (template sync). You can share a linked repository across multiple resources (like environments using self-managed provisioning, or synced templates). When you create a repository link, Proton creates a <a href="https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles.html">service-linked role</a> for you.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self">Self-managed provisioning</a>, <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles">Template bundles</a>, and <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html">Template sync configurations</a> in the <i>Proton User Guide</i>.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name (for example, <code>myrepos/myrepo</code>).</p>
            connection_arn: <p>The Amazon Resource Name (ARN) of your AWS CodeStar connection that connects Proton to your repository provider account. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html">Setting up for Proton</a> in the <i>Proton User Guide</i>.</p>
            encryption_key: <p>The ARN of your customer Amazon Web Services Key Management Service (Amazon Web Services KMS) key.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton repository. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_repository_input.CreateRepositoryInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_repository_output.CreateRepositoryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_repository

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_repository.async_create_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_repository_input.CreateRepositoryInput = {
            "provider": provider,
            "name": name,
            "connection_arn": connection_arn,
        }
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_repository(
        self,
        provider: "capo_proton.types.repository_provider.RepositoryProvider",
        name: "capo_proton.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_repository_output.GetRepositoryOutput":
        """<p>Get detail data for a linked repository.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name, for example <code>myrepos/myrepo</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_repository_input.GetRepositoryInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_repository_output.GetRepositoryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_repository

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_repository.async_get_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_repository_input.GetRepositoryInput = {
            "provider": provider,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_repository(
        self,
        provider: "capo_proton.types.repository_provider.RepositoryProvider",
        name: "capo_proton.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_repository_output.DeleteRepositoryOutput":
        """<p>De-register and unlink your repository.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_repository_input.DeleteRepositoryInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_repository_output.DeleteRepositoryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_repository

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_repository.async_delete_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_repository_input.DeleteRepositoryInput = {
            "provider": provider,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_repositories(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_repositories_output.ListRepositoriesOutput":
        """<p>List linked repositories with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next repository in the array of repositories, after the list of repositories previously requested.</p>
            max_results: <p>The maximum number of repositories to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_repositories_input.ListRepositoriesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_repositories_output.ListRepositoriesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_repositories

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_repositories.async_list_repositories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_repositories_input.ListRepositoriesInput = {}
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

    async def iter_list_repositories(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.repository_summary.RepositorySummary]":
        _token = next_token
        while True:
            _response = await self.list_repositories(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("repositories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_instance_outputs(
        self,
        service_instance_name: "capo_proton.types.resource_name.ResourceName",
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
    ) -> "capo_proton.types.list_service_instance_outputs_output.ListServiceInstanceOutputsOutput":
        """<p>Get a list service of instance Infrastructure as Code (IaC) outputs.</p>

        Args:
            service_instance_name: <p>The name of the service instance whose outputs you want.</p>
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated to.</p>
            next_token: <p>A token that indicates the location of the next output in the array of outputs, after the list of outputs that was previously requested.</p>
            deployment_id: <p>The ID of the deployment whose outputs you want.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_service_instance_outputs_input.ListServiceInstanceOutputsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_service_instance_outputs_output.ListServiceInstanceOutputsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_instance_outputs

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_service_instance_outputs.async_list_service_instance_outputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_service_instance_outputs_input.ListServiceInstanceOutputsInput = {
            "service_instance_name": service_instance_name,
            "service_name": service_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_service_instance_outputs(
        self,
        service_instance_name: "capo_proton.types.resource_name.ResourceName",
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
    ) -> "AsyncIterator[capo_proton.types.output.Output]":
        _token = next_token
        while True:
            _response = await self.list_service_instance_outputs(
                service_instance_name,
                service_name,
                config_overrides=config_overrides,
                next_token=_token,
                deployment_id=deployment_id,
            )
            _page = _resolve_path(_response, ("outputs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_instance_provisioned_resources(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        service_instance_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "capo_proton.types.list_service_instance_provisioned_resources_output.ListServiceInstanceProvisionedResourcesOutput":
        """<p>List provisioned resources for a service instance with details.</p>

        Args:
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated to.</p>
            service_instance_name: <p>The name of the service instance whose provisioned resources you want.</p>
            next_token: <p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_service_instance_provisioned_resources_input.ListServiceInstanceProvisionedResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_service_instance_provisioned_resources_output.ListServiceInstanceProvisionedResourcesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_instance_provisioned_resources

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_service_instance_provisioned_resources.async_list_service_instance_provisioned_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_service_instance_provisioned_resources_input.ListServiceInstanceProvisionedResourcesInput = {
            "service_name": service_name,
            "service_instance_name": service_instance_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_service_instance_provisioned_resources(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        service_instance_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.provisioned_resource.ProvisionedResource]":
        _token = next_token
        while True:
            _response = await self.list_service_instance_provisioned_resources(
                service_name,
                service_instance_name,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("provisioned_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_service_instance(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        service_name: "capo_proton.types.resource_name.ResourceName",
        spec: "capo_proton.types.spec_contents.SpecContents",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        template_major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
    ) -> "capo_proton.types.create_service_instance_output.CreateServiceInstanceOutput":
        """<p>Create a service instance.</p>

        Args:
            name: <p>The name of the service instance to create.</p>
            service_name: <p>The name of the service the service instance is added to.</p>
            spec: <p>The spec for the service instance you want to create.</p>
            template_major_version: <p>To create a new major and minor version of the service template, <i>exclude</i> <code>major Version</code>.</p>
            template_minor_version: <p>To create a new minor version of the service template, include a <code>major Version</code>.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service instance. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            client_token: <p>The client token of the service instance to create.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_service_instance_input.CreateServiceInstanceInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_service_instance_output.CreateServiceInstanceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_service_instance

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_service_instance.async_create_service_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_service_instance_input.CreateServiceInstanceInput = {
            "name": name,
            "service_name": service_name,
            "spec": spec,
        }
        if template_major_version is not None:
            input_["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version
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

    async def get_service_instance(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_instance_output.GetServiceInstanceOutput":
        """<p>Get detailed data for a service instance. A service instance is an instantiation of service template and it runs in a specific environment.</p>

        Args:
            name: <p>The name of a service instance that you want to get the detailed data for.</p>
            service_name: <p>The name of the service that you want the service instance input for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_service_instance_input.GetServiceInstanceInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_service_instance_output.GetServiceInstanceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_instance

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_service_instance.async_get_service_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_service_instance_input.GetServiceInstanceInput = {
            "name": name,
            "service_name": service_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service_instance(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        service_name: "capo_proton.types.resource_name.ResourceName",
        deployment_type: "capo_proton.types.deployment_update_type.DeploymentUpdateType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        spec: Optional["capo_proton.types.spec_contents.SpecContents"] = None,
        template_major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
    ) -> "capo_proton.types.update_service_instance_output.UpdateServiceInstanceOutput":
        """<p>Update a service instance.</p> <p>There are a few modes for updating a service instance. The <code>deploymentType</code> field defines the mode.</p> <note> <p>You can't update a service instance while its deployment status, or the deployment status of a component attached to it, is <code>IN_PROGRESS</code>.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service instance to update.</p>
            service_name: <p>The name of the service that the service instance belongs to.</p>
            deployment_type: <p>The deployment type. It defines the mode for updating a service instance, as follows:</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this deployment type.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>
            spec: <p>The formatted specification that defines the service instance update.</p>
            template_major_version: <p>The major version of the service template to update.</p>
            template_minor_version: <p>The minor version of the service template to update.</p>
            client_token: <p>The client token of the service instance to update.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_service_instance_input.UpdateServiceInstanceInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_instance_output.UpdateServiceInstanceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_instance

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service_instance.async_update_service_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_service_instance_input.UpdateServiceInstanceInput = {
            "name": name,
            "service_name": service_name,
            "deployment_type": deployment_type,
        }
        if spec is not None:
            input_["spec"] = spec
        if template_major_version is not None:
            input_["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version
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

    async def list_service_instances(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        filters: Optional[
            "capo_proton.types.list_service_instances_filter_list.ListServiceInstancesFilterList"
        ] = None,
        sort_by: Optional[
            "capo_proton.types.list_service_instances_sort_by.ListServiceInstancesSortBy"
        ] = None,
        sort_order: Optional["capo_proton.types.sort_order.SortOrder"] = None,
    ) -> "capo_proton.types.list_service_instances_output.ListServiceInstancesOutput":
        """<p>List service instances with summary data. This action lists service instances of all services in the Amazon Web Services account.</p>

        Args:
            service_name: <p>The name of the service that the service instance belongs to.</p>
            next_token: <p>A token that indicates the location of the next service in the array of service instances, after the list of service instances that was previously requested.</p>
            max_results: <p>The maximum number of service instances to list.</p>
            filters: <p>An array of filtering criteria that scope down the result list. By default, all service instances in the Amazon Web Services account are returned.</p>
            sort_by: <p>The field that the result list is sorted by.</p> <p>When you choose to sort by <code>serviceName</code>, service instances within each service are sorted by service instance name.</p> <p>Default: <code>serviceName</code> </p>
            sort_order: <p>Result list sort order.</p> <p>Default: <code>ASCENDING</code> </p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_service_instances_input.ListServiceInstancesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_service_instances_output.ListServiceInstancesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_instances

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_service_instances.async_list_service_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_service_instances_input.ListServiceInstancesInput = {}
        if service_name is not None:
            input_["service_name"] = service_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_service_instances(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        filters: Optional[
            "capo_proton.types.list_service_instances_filter_list.ListServiceInstancesFilterList"
        ] = None,
        sort_by: Optional[
            "capo_proton.types.list_service_instances_sort_by.ListServiceInstancesSortBy"
        ] = None,
        sort_order: Optional["capo_proton.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_proton.types.service_instance_summary.ServiceInstanceSummary]":
        _token = next_token
        while True:
            _response = await self.list_service_instances(
                config_overrides=config_overrides,
                service_name=service_name,
                next_token=_token,
                max_results=max_results,
                filters=filters,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("service_instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_pipeline_outputs(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
    ) -> "capo_proton.types.list_service_pipeline_outputs_output.ListServicePipelineOutputsOutput":
        """<p>Get a list of service pipeline Infrastructure as Code (IaC) outputs.</p>

        Args:
            service_name: <p>The name of the service whose pipeline's outputs you want.</p>
            next_token: <p>A token that indicates the location of the next output in the array of outputs, after the list of outputs that was previously requested.</p>
            deployment_id: <p>The ID of the deployment you want the outputs for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_service_pipeline_outputs_input.ListServicePipelineOutputsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_service_pipeline_outputs_output.ListServicePipelineOutputsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_pipeline_outputs

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_service_pipeline_outputs.async_list_service_pipeline_outputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_service_pipeline_outputs_input.ListServicePipelineOutputsInput = {
            "service_name": service_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_service_pipeline_outputs(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
    ) -> "AsyncIterator[capo_proton.types.output.Output]":
        _token = next_token
        while True:
            _response = await self.list_service_pipeline_outputs(
                service_name,
                config_overrides=config_overrides,
                next_token=_token,
                deployment_id=deployment_id,
            )
            _page = _resolve_path(_response, ("outputs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_pipeline_provisioned_resources(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "capo_proton.types.list_service_pipeline_provisioned_resources_output.ListServicePipelineProvisionedResourcesOutput":
        """<p>List provisioned resources for a service and pipeline with details.</p>

        Args:
            service_name: <p>The name of the service whose pipeline's provisioned resources you want.</p>
            next_token: <p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_service_pipeline_provisioned_resources_input.ListServicePipelineProvisionedResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_service_pipeline_provisioned_resources_output.ListServicePipelineProvisionedResourcesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_pipeline_provisioned_resources

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_service_pipeline_provisioned_resources.async_list_service_pipeline_provisioned_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_service_pipeline_provisioned_resources_input.ListServicePipelineProvisionedResourcesInput = {
            "service_name": service_name
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_service_pipeline_provisioned_resources(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.provisioned_resource.ProvisionedResource]":
        _token = next_token
        while True:
            _response = await self.list_service_pipeline_provisioned_resources(
                service_name,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("provisioned_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_service_pipeline(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        spec: "capo_proton.types.spec_contents.SpecContents",
        deployment_type: "capo_proton.types.deployment_update_type.DeploymentUpdateType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        template_major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
    ) -> "capo_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput":
        """<p>Update the service pipeline.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>

        Args:
            service_name: <p>The name of the service to that the pipeline is associated with.</p>
            spec: <p>The spec for the service pipeline to update.</p>
            deployment_type: <p>The deployment type.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>
            template_major_version: <p>The major version of the service template that was used to create the service that the pipeline is associated with.</p>
            template_minor_version: <p>The minor version of the service template that was used to create the service that the pipeline is associated with.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_service_pipeline_input.UpdateServicePipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_pipeline

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service_pipeline.async_update_service_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_service_pipeline_input.UpdateServicePipelineInput = {
            "service_name": service_name,
            "spec": spec,
            "deployment_type": deployment_type,
        }
        if template_major_version is not None:
            input_["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_service(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        spec: "capo_proton.types.spec_contents.SpecContents",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        repository_connection_arn: Optional["capo_proton.types.arn.Arn"] = None,
        repository_id: Optional["capo_proton.types.repository_id.RepositoryId"] = None,
        branch_name: Optional["capo_proton.types.git_branch_name.GitBranchName"] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
    ) -> "capo_proton.types.create_service_output.CreateServiceOutput":
        """<p>Create an Proton service. An Proton service is an instantiation of a service template and often includes several service instances and pipeline. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-services.html">Services</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The service name.</p>
            description: <p>A description of the Proton service.</p>
            template_name: <p>The name of the service template that's used to create the service.</p>
            template_major_version: <p>The major version of the service template that was used to create the service.</p>
            template_minor_version: <p>The minor version of the service template that was used to create the service.</p>
            spec: <p>A link to a spec file that provides inputs as defined in the service template bundle schema file. The spec file is in YAML format. <i>Don’t</i> include pipeline inputs in the spec if your service template <i>doesn’t</i> include a service pipeline. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-create-svc.html">Create a service</a> in the <i>Proton User Guide</i>.</p>
            repository_connection_arn: <p>The Amazon Resource Name (ARN) of the repository connection. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html#setting-up-vcontrol">Setting up an AWS CodeStar connection</a> in the <i>Proton User Guide</i>. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>
            repository_id: <p>The ID of the code repository. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>
            branch_name: <p>The name of the code repository branch that holds the code that's deployed in Proton. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_service_input.CreateServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_service_output.CreateServiceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_service

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_service.async_create_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_service_input.CreateServiceInput = {
            "name": name,
            "template_name": template_name,
            "template_major_version": template_major_version,
            "spec": spec,
        }
        if description is not None:
            input_["description"] = description
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version
        if repository_connection_arn is not None:
            input_["repository_connection_arn"] = repository_connection_arn
        if repository_id is not None:
            input_["repository_id"] = repository_id
        if branch_name is not None:
            input_["branch_name"] = branch_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_output.GetServiceOutput":
        """<p>Get detailed data for a service.</p>

        Args:
            name: <p>The name of the service that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_service_input.GetServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_service_output.GetServiceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_service.async_get_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_service_input.GetServiceInput = {"name": name}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        spec: Optional["capo_proton.types.spec_contents.SpecContents"] = None,
    ) -> "capo_proton.types.update_service_output.UpdateServiceOutput":
        """<p>Edit a service description or use a spec to add and delete service instances.</p> <note> <p>Existing service instances and the service pipeline <i>can't</i> be edited using this API. They can only be deleted.</p> </note> <p>Use the <code>description</code> parameter to modify the description.</p> <p>Edit the <code>spec</code> parameter to add or delete instances.</p> <note> <p>You can't delete a service instance (remove it from the spec) if it has an attached component.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service to edit.</p>
            description: <p>The edited service description.</p>
            spec: <p>Lists the service instances to add and the existing service instances to remain. Omit the existing service instances to delete from the list. <i>Don't</i> include edits to the existing service instances or pipeline. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-update.html">Edit a service</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_service_input.UpdateServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_output.UpdateServiceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service.async_update_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_service_input.UpdateServiceInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if spec is not None:
            input_["spec"] = spec

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_service(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_service_output.DeleteServiceOutput":
        """<p>Delete a service, with its instances and pipeline.</p> <note> <p>You can't delete a service if it has any service instances that have components attached to them.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_service_input.DeleteServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_service_output.DeleteServiceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_service

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_service.async_delete_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_service_input.DeleteServiceInput = {
            "name": name
        }

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
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_services_output.ListServicesOutput":
        """<p>List services with summaries of detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next service in the array of services, after the list of services that was previously requested.</p>
            max_results: <p>The maximum number of services to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_services_input.ListServicesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_services_output.ListServicesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_services

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_services.async_list_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_services_input.ListServicesInput = {}
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

    async def iter_list_services(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.service_summary.ServiceSummary]":
        _token = next_token
        while True:
            _response = await self.list_services(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("services",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_service_sync_blocker_summary(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_proton.types.get_service_sync_blocker_summary_output.GetServiceSyncBlockerSummaryOutput":
        """<p>Get detailed data for the service sync blocker summary.</p>

        Args:
            service_name: <p>The name of the service that you want to get the service sync blocker summary for. If given only the service name, all instances are blocked.</p>
            service_instance_name: <p>The name of the service instance that you want to get the service sync blocker summary for. If given bothe the instance name and the service name, only the instance is blocked.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_service_sync_blocker_summary_input.GetServiceSyncBlockerSummaryInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_service_sync_blocker_summary_output.GetServiceSyncBlockerSummaryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_sync_blocker_summary

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_service_sync_blocker_summary.async_get_service_sync_blocker_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_service_sync_blocker_summary_input.GetServiceSyncBlockerSummaryInput = {
            "service_name": service_name
        }
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service_sync_blocker(
        self,
        id: str,
        resolved_reason: str,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.update_service_sync_blocker_output.UpdateServiceSyncBlockerOutput":
        """<p>Update the service sync blocker by resolving it.</p>

        Args:
            id: <p>The ID of the service sync blocker.</p>
            resolved_reason: <p>The reason the service sync blocker was resolved.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_service_sync_blocker_input.UpdateServiceSyncBlockerInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_sync_blocker_output.UpdateServiceSyncBlockerOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_sync_blocker

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service_sync_blocker.async_update_service_sync_blocker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_service_sync_blocker_input.UpdateServiceSyncBlockerInput = {
            "id": id,
            "resolved_reason": resolved_reason,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_service_sync_config(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        file_path: "capo_proton.types.ops_file_path.OpsFilePath",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.create_service_sync_config_output.CreateServiceSyncConfigOutput":
        """<p>Create the Proton Ops configuration file.</p>

        Args:
            service_name: <p>The name of the service the Proton Ops file is for.</p>
            repository_provider: <p>The provider type for your repository.</p>
            repository_name: <p>The repository name.</p>
            branch: <p>The repository branch for your Proton Ops file.</p>
            file_path: <p>The path to the Proton Ops file.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_service_sync_config_input.CreateServiceSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_service_sync_config_output.CreateServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_service_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_service_sync_config.async_create_service_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_service_sync_config_input.CreateServiceSyncConfigInput = {
            "service_name": service_name,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
            "file_path": file_path,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_sync_config(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_sync_config_output.GetServiceSyncConfigOutput":
        """<p>Get detailed information for the service sync configuration.</p>

        Args:
            service_name: <p>The name of the service that you want to get the service sync configuration for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_service_sync_config_input.GetServiceSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_service_sync_config_output.GetServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_service_sync_config.async_get_service_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_service_sync_config_input.GetServiceSyncConfigInput = {
            "service_name": service_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service_sync_config(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        file_path: "capo_proton.types.ops_file_path.OpsFilePath",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.update_service_sync_config_output.UpdateServiceSyncConfigOutput":
        """<p>Update the Proton Ops config file.</p>

        Args:
            service_name: <p>The name of the service the Proton Ops file is for.</p>
            repository_provider: <p>The name of the repository provider where the Proton Ops file is found.</p>
            repository_name: <p>The name of the repository where the Proton Ops file is found.</p>
            branch: <p>The name of the code repository branch where the Proton Ops file is found.</p>
            file_path: <p>The path to the Proton Ops file.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_service_sync_config_input.UpdateServiceSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_sync_config_output.UpdateServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service_sync_config.async_update_service_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_service_sync_config_input.UpdateServiceSyncConfigInput = {
            "service_name": service_name,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
            "file_path": file_path,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_service_sync_config(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_service_sync_config_output.DeleteServiceSyncConfigOutput":
        """<p>Delete the Proton Ops file.</p>

        Args:
            service_name: <p>The name of the service that you want to delete the service sync configuration for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_service_sync_config_input.DeleteServiceSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_service_sync_config_output.DeleteServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_service_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_service_sync_config.async_delete_service_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_service_sync_config_input.DeleteServiceSyncConfigInput = {
            "service_name": service_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_service_template(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        display_name: Optional["capo_proton.types.display_name.DisplayName"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        encryption_key: Optional["capo_proton.types.arn.Arn"] = None,
        pipeline_provisioning: Optional[
            "capo_proton.types.provisioning.Provisioning"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
    ) -> "capo_proton.types.create_service_template_output.CreateServiceTemplateOutput":
        """<p>Create a service template. The administrator creates a service template to define standardized infrastructure and an optional CI/CD service pipeline. Developers, in turn, select the service template from Proton. If the selected service template includes a service pipeline definition, they provide a link to their source code repository. Proton then deploys and manages the infrastructure defined by the selected service template. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html">Proton templates</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the service template.</p>
            display_name: <p>The name of the service template as displayed in the developer interface.</p>
            description: <p>A description of the service template.</p>
            encryption_key: <p>A customer provided encryption key that's used to encrypt data.</p>
            pipeline_provisioning: <p>By default, Proton provides a service pipeline for your service. When this parameter is included, it indicates that an Proton service pipeline <i>isn't</i> provided for your service. After it's included, it <i>can't</i> be changed. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles">Template bundles</a> in the <i>Proton User Guide</i>.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service template. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_service_template_input.CreateServiceTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_service_template_output.CreateServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_service_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_service_template.async_create_service_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_service_template_input.CreateServiceTemplateInput = {
            "name": name
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if pipeline_provisioning is not None:
            input_["pipeline_provisioning"] = pipeline_provisioning
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_template(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_template_output.GetServiceTemplateOutput":
        """<p>Get detailed data for a service template.</p>

        Args:
            name: <p>The name of the service template that you want to get detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_service_template_input.GetServiceTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_service_template_output.GetServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_service_template.async_get_service_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_service_template_input.GetServiceTemplateInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service_template(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        display_name: Optional["capo_proton.types.display_name.DisplayName"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
    ) -> "capo_proton.types.update_service_template_output.UpdateServiceTemplateOutput":
        """<p>Update a service template.</p>

        Args:
            name: <p>The name of the service template to update.</p>
            display_name: <p>The name of the service template to update that's displayed in the developer interface.</p>
            description: <p>A description of the service template update.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_service_template_input.UpdateServiceTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_template_output.UpdateServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service_template.async_update_service_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_service_template_input.UpdateServiceTemplateInput = {
            "name": name
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_service_template(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_service_template_output.DeleteServiceTemplateOutput":
        """<p>If no other major or minor versions of the service template exist, delete the service template.</p>

        Args:
            name: <p>The name of the service template to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_service_template_input.DeleteServiceTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_service_template_output.DeleteServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_service_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_service_template.async_delete_service_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_service_template_input.DeleteServiceTemplateInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_service_templates(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_service_templates_output.ListServiceTemplatesOutput":
        """<p>List service templates with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next service template in the array of service templates, after the list of service templates previously requested.</p>
            max_results: <p>The maximum number of service templates to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_service_templates_input.ListServiceTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_service_templates_output.ListServiceTemplatesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_templates

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_service_templates.async_list_service_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_service_templates_input.ListServiceTemplatesInput = {}
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

    async def iter_list_service_templates(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.service_template_summary.ServiceTemplateSummary]":
        _token = next_token
        while True:
            _response = await self.list_service_templates(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_service_template_version(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        source: "capo_proton.types.template_version_source_input.TemplateVersionSourceInput",
        compatible_environment_templates: "capo_proton.types.compatible_environment_template_input_list.CompatibleEnvironmentTemplateInputList",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
        supported_component_sources: Optional[
            "capo_proton.types.service_template_supported_component_source_input_list.ServiceTemplateSupportedComponentSourceInputList"
        ] = None,
    ) -> "capo_proton.types.create_service_template_version_output.CreateServiceTemplateVersionOutput":
        """<p>Create a new major or minor version of a service template. A major version of a service template is a version that <i>isn't</i> backward compatible. A minor version of a service template is a version that's backward compatible within its major version.</p>

        Args:
            client_token: <p>When included, if two identical requests are made with the same client token, Proton returns the service template version that the first request created.</p>
            template_name: <p>The name of the service template.</p>
            description: <p>A description of the new version of a service template.</p>
            major_version: <p>To create a new minor version of the service template, include a <code>major Version</code>.</p> <p>To create a new major and minor version of the service template, <i>exclude</i> <code>major Version</code>.</p>
            source: <p>An object that includes the template bundle S3 bucket path and name for the new version of a service template.</p>
            compatible_environment_templates: <p>An array of environment template objects that are compatible with the new service template version. A service instance based on this service template version can run in environments based on compatible templates.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service template version. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            supported_component_sources: <p>An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_service_template_version_input.CreateServiceTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_service_template_version_output.CreateServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_service_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_service_template_version.async_create_service_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_service_template_version_input.CreateServiceTemplateVersionInput = {
            "template_name": template_name,
            "source": source,
            "compatible_environment_templates": compatible_environment_templates,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if major_version is not None:
            input_["major_version"] = major_version
        if tags is not None:
            input_["tags"] = tags
        if supported_component_sources is not None:
            input_["supported_component_sources"] = supported_component_sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_template_version(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_template_version_output.GetServiceTemplateVersionOutput":
        """<p>Get detailed data for a major or minor version of a service template.</p>

        Args:
            template_name: <p>The name of the service template a version of which you want to get detailed data for.</p>
            major_version: <p>To get service template major version detail data, include <code>major Version</code>.</p>
            minor_version: <p>To get service template minor version detail data, include <code>minorVersion</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_service_template_version_input.GetServiceTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_service_template_version_output.GetServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_service_template_version.async_get_service_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_service_template_version_input.GetServiceTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service_template_version(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        status: Optional[
            "capo_proton.types.template_version_status.TemplateVersionStatus"
        ] = None,
        compatible_environment_templates: Optional[
            "capo_proton.types.compatible_environment_template_input_list.CompatibleEnvironmentTemplateInputList"
        ] = None,
        supported_component_sources: Optional[
            "capo_proton.types.service_template_supported_component_source_input_list.ServiceTemplateSupportedComponentSourceInputList"
        ] = None,
    ) -> "capo_proton.types.update_service_template_version_output.UpdateServiceTemplateVersionOutput":
        """<p>Update a major or minor version of a service template.</p>

        Args:
            template_name: <p>The name of the service template.</p>
            major_version: <p>To update a major version of a service template, include <code>major Version</code>.</p>
            minor_version: <p>To update a minor version of a service template, include <code>minorVersion</code>.</p>
            description: <p>A description of a service template version to update.</p>
            status: <p>The status of the service template minor version to update.</p>
            compatible_environment_templates: <p>An array of environment template objects that are compatible with this service template version. A service instance based on this service template version can run in environments based on compatible templates.</p>
            supported_component_sources: <p>An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.</p> <note> <p>A change to <code>supportedComponentSources</code> doesn't impact existing component attachments to instances based on this template version. A change only affects later associations.</p> </note> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_service_template_version_input.UpdateServiceTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_template_version_output.UpdateServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service_template_version.async_update_service_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_service_template_version_input.UpdateServiceTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if compatible_environment_templates is not None:
            input_["compatible_environment_templates"] = (
                compatible_environment_templates
            )
        if supported_component_sources is not None:
            input_["supported_component_sources"] = supported_component_sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_service_template_version(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_service_template_version_output.DeleteServiceTemplateVersionOutput":
        """<p>If no other minor versions of a service template exist, delete a major version of the service template if it's not the <code>Recommended</code> version. Delete the <code>Recommended</code> version of the service template if no other major versions or minor versions of the service template exist. A major version of a service template is a version that <i>isn't</i> backwards compatible.</p> <p>Delete a minor version of a service template if it's not the <code>Recommended</code> version. Delete a <code>Recommended</code> minor version of the service template if no other minor versions of the service template exist. A minor version of a service template is a version that's backwards compatible.</p>

        Args:
            template_name: <p>The name of the service template.</p>
            major_version: <p>The service template major version to delete.</p>
            minor_version: <p>The service template minor version to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_service_template_version_input.DeleteServiceTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_service_template_version_output.DeleteServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_service_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_service_template_version.async_delete_service_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_service_template_version_input.DeleteServiceTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_service_template_versions(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
    ) -> "capo_proton.types.list_service_template_versions_output.ListServiceTemplateVersionsOutput":
        """<p>List major or minor versions of a service template with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next major or minor version in the array of major or minor versions of a service template, after the list of major or minor versions that was previously requested.</p>
            max_results: <p>The maximum number of major or minor versions of a service template to list.</p>
            template_name: <p>The name of the service template.</p>
            major_version: <p>To view a list of minor of versions under a major version of a service template, include <code>major Version</code>.</p> <p>To view a list of major versions of a service template, <i>exclude</i> <code>major Version</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_service_template_versions_input.ListServiceTemplateVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_service_template_versions_output.ListServiceTemplateVersionsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_template_versions

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_service_template_versions.async_list_service_template_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_service_template_versions_input.ListServiceTemplateVersionsInput = {
            "template_name": template_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if major_version is not None:
            input_["major_version"] = major_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_service_template_versions(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
    ) -> "AsyncIterator[capo_proton.types.service_template_version_summary.ServiceTemplateVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_service_template_versions(
                template_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                major_version=major_version,
            )
            _page = _resolve_path(_response, ("template_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_template_sync_config(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_type: "capo_proton.types.template_type.TemplateType",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        subdirectory: Optional["capo_proton.types.subdirectory.Subdirectory"] = None,
    ) -> "capo_proton.types.create_template_sync_config_output.CreateTemplateSyncConfigOutput":
        """<p>Set up a template to create new template versions automatically by tracking a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>When a commit is pushed to your linked repository, Proton checks for changes to your repository template bundles. If it detects a template bundle change, a new major or minor version of its template is created, if the version doesn’t already exist. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html">Template sync configurations</a> in the <i>Proton User Guide</i>.</p>

        Args:
            template_name: <p>The name of your registered template.</p>
            template_type: <p>The type of the registered template.</p>
            repository_provider: <p>The provider type for your repository.</p>
            repository_name: <p>The repository name (for example, <code>myrepos/myrepo</code>).</p>
            branch: <p>The repository branch for your template.</p>
            subdirectory: <p>A repository subdirectory path to your template bundle directory. When included, Proton limits the template bundle search to this repository directory.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_template_sync_config_input.CreateTemplateSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_template_sync_config_output.CreateTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_template_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_template_sync_config.async_create_template_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.create_template_sync_config_input.CreateTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_template_sync_config(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_type: "capo_proton.types.template_type.TemplateType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> (
        "capo_proton.types.get_template_sync_config_output.GetTemplateSyncConfigOutput"
    ):
        """<p>Get detail data for a template sync configuration.</p>

        Args:
            template_name: <p>The template name.</p>
            template_type: <p>The template type.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_template_sync_config_input.GetTemplateSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_template_sync_config_output.GetTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_template_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_template_sync_config.async_get_template_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_template_sync_config_input.GetTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_template_sync_config(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_type: "capo_proton.types.template_type.TemplateType",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        subdirectory: Optional["capo_proton.types.subdirectory.Subdirectory"] = None,
    ) -> "capo_proton.types.update_template_sync_config_output.UpdateTemplateSyncConfigOutput":
        """<p>Update template sync configuration parameters, except for the <code>templateName</code> and <code>templateType</code>. Repository details (branch, name, and provider) should be of a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p>

        Args:
            template_name: <p>The synced template name.</p>
            template_type: <p>The synced template type.</p>
            repository_provider: <p>The repository provider.</p>
            repository_name: <p>The repository name (for example, <code>myrepos/myrepo</code>).</p>
            branch: <p>The repository branch for your template.</p>
            subdirectory: <p>A subdirectory path to your template bundle version. When included, limits the template bundle search to this repository directory.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_template_sync_config_input.UpdateTemplateSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_template_sync_config_output.UpdateTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_template_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_template_sync_config.async_update_template_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.update_template_sync_config_input.UpdateTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_template_sync_config(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_type: "capo_proton.types.template_type.TemplateType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_template_sync_config_output.DeleteTemplateSyncConfigOutput":
        """<p>Delete a template sync configuration.</p>

        Args:
            template_name: <p>The template name.</p>
            template_type: <p>The template type.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_template_sync_config_input.DeleteTemplateSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_template_sync_config_output.DeleteTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_template_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_template_sync_config.async_delete_template_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.delete_template_sync_config_input.DeleteTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
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
