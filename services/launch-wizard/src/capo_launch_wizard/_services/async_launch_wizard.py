"""Generated from Smithy shape ``com.amazonaws.launchwizard#LaunchWizard``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_launch_wizard._auth._signers
import capo_launch_wizard._auth._sigv4
from capo_launch_wizard._auth._identity import Credentials
from capo_launch_wizard._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_launch_wizard._auth._zapros_handler import AuthMiddleware
from capo_launch_wizard._pagination import resolve_path as _resolve_path
from capo_launch_wizard._resources.launch_wizard.deployment import AsyncDeployment
from capo_launch_wizard._resources.launch_wizard.settings_set import AsyncSettingsSet
from capo_launch_wizard._resources.launch_wizard.workload import AsyncWorkload
from capo_launch_wizard._services._aws_config import aaws_config
from capo_launch_wizard._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_launch_wizard.types.create_deployment_input
    import capo_launch_wizard.types.create_deployment_output
    import capo_launch_wizard.types.delete_deployment_input
    import capo_launch_wizard.types.delete_deployment_output
    import capo_launch_wizard.types.deployment_data_summary
    import capo_launch_wizard.types.deployment_event_data_summary
    import capo_launch_wizard.types.deployment_filter_list
    import capo_launch_wizard.types.deployment_id
    import capo_launch_wizard.types.deployment_name
    import capo_launch_wizard.types.deployment_pattern_name
    import capo_launch_wizard.types.deployment_pattern_version_data_summary
    import capo_launch_wizard.types.deployment_pattern_version_name
    import capo_launch_wizard.types.deployment_specifications
    import capo_launch_wizard.types.filter_list
    import capo_launch_wizard.types.get_deployment_input
    import capo_launch_wizard.types.get_deployment_output
    import capo_launch_wizard.types.get_deployment_pattern_version_input
    import capo_launch_wizard.types.get_deployment_pattern_version_output
    import capo_launch_wizard.types.get_workload_deployment_pattern_input
    import capo_launch_wizard.types.get_workload_deployment_pattern_output
    import capo_launch_wizard.types.get_workload_input
    import capo_launch_wizard.types.get_workload_output
    import capo_launch_wizard.types.list_deployment_events_input
    import capo_launch_wizard.types.list_deployment_events_output
    import capo_launch_wizard.types.list_deployment_pattern_versions_input
    import capo_launch_wizard.types.list_deployment_pattern_versions_output
    import capo_launch_wizard.types.list_deployments_input
    import capo_launch_wizard.types.list_deployments_output
    import capo_launch_wizard.types.list_tags_for_resource_input
    import capo_launch_wizard.types.list_tags_for_resource_output
    import capo_launch_wizard.types.list_workload_deployment_patterns_input
    import capo_launch_wizard.types.list_workload_deployment_patterns_output
    import capo_launch_wizard.types.list_workloads_input
    import capo_launch_wizard.types.list_workloads_output
    import capo_launch_wizard.types.max_deployment_event_results
    import capo_launch_wizard.types.max_deployment_results
    import capo_launch_wizard.types.max_workload_deployment_pattern_results
    import capo_launch_wizard.types.max_workload_results
    import capo_launch_wizard.types.next_token
    import capo_launch_wizard.types.tag_key_list
    import capo_launch_wizard.types.tag_resource_input
    import capo_launch_wizard.types.tag_resource_output
    import capo_launch_wizard.types.tags
    import capo_launch_wizard.types.untag_resource_input
    import capo_launch_wizard.types.untag_resource_output
    import capo_launch_wizard.types.update_deployment_input
    import capo_launch_wizard.types.update_deployment_output
    import capo_launch_wizard.types.workload_data_summary
    import capo_launch_wizard.types.workload_deployment_pattern_data_summary
    import capo_launch_wizard.types.workload_name
    import capo_launch_wizard.types.workload_version_name


class AsyncLaunchWizardClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncLaunchWizardClient:
    """A client for the ``LaunchWizard`` service.

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
        self._config = AsyncLaunchWizardClientConfig(
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
        self.deployment = AsyncDeployment(self)
        self.settings_set = AsyncSettingsSet(self)
        self.workload = AsyncWorkload(self)

    def operation_options(
        self, config_overrides: Optional[AsyncLaunchWizardClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncLaunchWizardClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags associated with a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Listing tags on a Launch Wizard deployment resource.

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:launchwizard:us-east-1:123456789012:deployment/11111111-1111-1111-1111-111111111111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
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
        resource_arn: str,
        tags: "capo_launch_wizard.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.tag_resource_output.TagResourceOutput":
        """<p>Adds the specified tags to the given resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>One or more tags to attach to the resource.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Adding tags to a Launch Wizard deployment resource.

            >>> await client.tag_resource(resource_arn='arn:aws:launchwizard:us-east-1:123456789012:deployment/11111111-1111-1111-1111-111111111111', tags={'key1': 'value1', 'key2': 'value2'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.tag_resource

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: str,
        tag_keys: "capo_launch_wizard.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes the specified tags from the given resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>Keys identifying the tags to remove.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Removing tags on a Launch Wizard deployment resource.

            >>> await client.untag_resource(resource_arn='arn:aws:launchwizard:us-east-1:123456789012:deployment/11111111-1111-1111-1111-111111111111', tag_keys=['key1', 'key2'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.untag_resource

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.untag_resource_input.UntagResourceInput = {
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

    async def create_deployment(
        self,
        workload_name: "capo_launch_wizard.types.workload_name.WorkloadName",
        deployment_pattern_name: "capo_launch_wizard.types.deployment_pattern_name.DeploymentPatternName",
        name: "capo_launch_wizard.types.deployment_name.DeploymentName",
        specifications: "capo_launch_wizard.types.deployment_specifications.DeploymentSpecifications",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        dry_run: Optional[bool] = None,
        tags: Optional["capo_launch_wizard.types.tags.Tags"] = None,
    ) -> "capo_launch_wizard.types.create_deployment_output.CreateDeploymentOutput":
        """<p>Creates a deployment for the given workload. Deployments created by this operation are not available in the Launch Wizard console to use the <code>Clone deployment</code> action on.</p>

        Args:
            workload_name: <p>The name of the workload. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html"> <code>ListWorkloads</code> </a> operation to discover supported values for this parameter.</p>
            deployment_pattern_name: <p>The name of the deployment pattern supported by a given workload. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html"> <code>ListWorkloadDeploymentPatterns</code> </a> operation to discover supported values for this parameter. </p>
            name: <p>The name of the deployment.</p>
            specifications: <p>The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html">SAP deployment specifications</a>. To retrieve the specifications required to create a deployment for other workloads, use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html"> <code>GetWorkloadDeploymentPattern</code> </a> operation.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            tags: <p>The tags to add to the deployment.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_limit_exception.ResourceLimitException: <p>You have exceeded an Launch Wizard resource limit. For example, you might have too many deployments in progress.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Deploy a given workload with given settings.

            >>> await client.create_deployment(workload_name='SAP', deployment_pattern_name='SapHanaSingle', name='TestDeployment1', dry_run=False, specifications={'DisableDeploymentRollback': 'Yes', 'SaveDeploymentArtifacts': 'No', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234566', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://xyz.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'Yes', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo'})
            Deploy a given workload with given settings and passing tags for Launch Wizard deployment resource.

            >>> await client.create_deployment(workload_name='SAP', deployment_pattern_name='SapHanaSingle', name='TestDeployment2', dry_run=False, specifications={'DisableDeploymentRollback': 'Yes', 'SaveDeploymentArtifacts': 'No', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234566', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://xyz.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'Yes', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo'}, tags={'key1': 'val1', 'key2': 'val2'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.create_deployment_input.CreateDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.create_deployment_output.CreateDeploymentOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.create_deployment

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.create_deployment.async_create_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.create_deployment_input.CreateDeploymentInput = {
            "workload_name": workload_name,
            "deployment_pattern_name": deployment_pattern_name,
            "name": name,
            "specifications": specifications,
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_deployment(
        self,
        deployment_id: "capo_launch_wizard.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.get_deployment_output.GetDeploymentOutput":
        """<p>Returns information about the deployment.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get details about a given deployment.

            >>> await client.get_deployment(deployment_id='1111111-1111-1111-1111-111111111111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.get_deployment_input.GetDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.get_deployment_output.GetDeploymentOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.get_deployment

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.get_deployment.async_get_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.get_deployment_input.GetDeploymentInput = {
            "deployment_id": deployment_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_deployment(
        self,
        deployment_id: "capo_launch_wizard.types.deployment_id.DeploymentId",
        specifications: "capo_launch_wizard.types.deployment_specifications.DeploymentSpecifications",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        workload_version_name: Optional[
            "capo_launch_wizard.types.workload_version_name.WorkloadVersionName"
        ] = None,
        deployment_pattern_version_name: Optional[
            "capo_launch_wizard.types.deployment_pattern_version_name.DeploymentPatternVersionName"
        ] = None,
        dry_run: Optional[bool] = None,
        force: Optional[bool] = None,
    ) -> "capo_launch_wizard.types.update_deployment_output.UpdateDeploymentOutput":
        """<p>Updates a deployment.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>
            specifications: <p>The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html">SAP deployment specifications</a>. To retrieve the specifications required to create a deployment for other workloads, use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html"> <code>GetWorkloadDeploymentPattern</code> </a> operation.</p>
            workload_version_name: <p>The name of the workload version.</p>
            deployment_pattern_version_name: <p>The name of the deployment pattern version.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            force: <p>Forces the update even if validation warnings are present.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_limit_exception.ResourceLimitException: <p>You have exceeded an Launch Wizard resource limit. For example, you might have too many deployments in progress.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Edit deployment specifications.

            >>> await client.update_deployment(deployment_id='4c1b59c1-659c-467f-b6e9-6ef6f9d28e1d', specifications={'DisableDeploymentRollback': 'No', 'SaveDeploymentArtifacts': 'Yes', 'DeploymentArtifactsS3Uri': 'aws-bucket-name', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234567', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://mno.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'No', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo'}, dry_run=False)
            Update deployment version.

            >>> await client.update_deployment(deployment_id='4c1b59c1-659c-467f-b6e9-6ef6f9d28e1d', deployment_pattern_version_name='2.0.0', specifications={'DisableDeploymentRollback': 'No', 'SaveDeploymentArtifacts': 'Yes', 'DeploymentArtifactsS3Uri': 'aws-bucket-name', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234567', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://mno.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'No', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo', 'NewParameter': 'Allow'}, dry_run=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.update_deployment_input.UpdateDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.update_deployment_output.UpdateDeploymentOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.update_deployment

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.update_deployment.async_update_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.update_deployment_input.UpdateDeploymentInput = {
            "deployment_id": deployment_id,
            "specifications": specifications,
        }
        if workload_version_name is not None:
            input_["workload_version_name"] = workload_version_name
        if deployment_pattern_version_name is not None:
            input_["deployment_pattern_version_name"] = deployment_pattern_version_name
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_deployment(
        self,
        deployment_id: "capo_launch_wizard.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.delete_deployment_output.DeleteDeploymentOutput":
        """<p>Deletes a deployment.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_limit_exception.ResourceLimitException: <p>You have exceeded an Launch Wizard resource limit. For example, you might have too many deployments in progress.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a deployment.

            >>> await client.delete_deployment(deployment_id='4c1b59c1-659c-467f-b6e9-6ef6f9d28e1d')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.delete_deployment_input.DeleteDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.delete_deployment_output.DeleteDeploymentOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.delete_deployment

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.delete_deployment.async_delete_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.delete_deployment_input.DeleteDeploymentInput = {
            "deployment_id": deployment_id
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
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        filters: Optional[
            "capo_launch_wizard.types.deployment_filter_list.DeploymentFilterList"
        ] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_deployment_results.MaxDeploymentResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "capo_launch_wizard.types.list_deployments_output.ListDeploymentsOutput":
        """<p>Lists the deployments that have been created.</p>

        Args:
            filters: <p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>WORKLOAD_NAME</code> - The name used in deployments.</p> </li> <li> <p> <code>DEPLOYMENT_STATUS</code> - <code>COMPLETED</code> | <code>CREATING</code> | <code>DELETE_IN_PROGRESS</code> | <code>DELETE_INITIATING</code> | <code>DELETE_FAILED</code> | <code>DELETED</code> | <code>FAILED</code> | <code>IN_PROGRESS</code> | <code>VALIDATING</code> </p> </li> </ul>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List deployments in the account with filters.

            >>> await client.list_deployments(filters=[{'name': 'DEPLOYMENT_STATUS', 'values': ['IN_PROGRESS']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.list_deployments_input.ListDeploymentsInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.list_deployments_output.ListDeploymentsOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.list_deployments

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.list_deployments.async_list_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.list_deployments_input.ListDeploymentsInput = {}
        if filters is not None:
            input_["filters"] = filters
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
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        filters: Optional[
            "capo_launch_wizard.types.deployment_filter_list.DeploymentFilterList"
        ] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_deployment_results.MaxDeploymentResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_launch_wizard.types.deployment_data_summary.DeploymentDataSummary]":
        _token = next_token
        while True:
            _response = await self.list_deployments(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("deployments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_deployment_events(
        self,
        deployment_id: "capo_launch_wizard.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_deployment_event_results.MaxDeploymentEventResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "capo_launch_wizard.types.list_deployment_events_output.ListDeploymentEventsOutput":
        """<p>Lists the events of a deployment.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all actions taken during a deployment.

            >>> await client.list_deployment_events(deployment_id='4c1b59c1-659c-467f-b6e9-6ef6f9d28e1d')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.list_deployment_events_input.ListDeploymentEventsInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.list_deployment_events_output.ListDeploymentEventsOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.list_deployment_events

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.list_deployment_events.async_list_deployment_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.list_deployment_events_input.ListDeploymentEventsInput = {
            "deployment_id": deployment_id
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

    async def iter_list_deployment_events(
        self,
        deployment_id: "capo_launch_wizard.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_deployment_event_results.MaxDeploymentEventResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_launch_wizard.types.deployment_event_data_summary.DeploymentEventDataSummary]":
        _token = next_token
        while True:
            _response = await self.list_deployment_events(
                deployment_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("deployment_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_workload(
        self,
        workload_name: "capo_launch_wizard.types.workload_name.WorkloadName",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.get_workload_output.GetWorkloadOutput":
        """<p>Returns information about a workload.</p>

        Args:
            workload_name: <p>The name of the workload.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get details about a specific workload.

            >>> await client.get_workload(workload_name='SAP')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.get_workload_input.GetWorkloadInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.get_workload_output.GetWorkloadOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.get_workload

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.get_workload.async_get_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.get_workload_input.GetWorkloadInput = {
            "workload_name": workload_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workloads(
        self,
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_workload_results.MaxWorkloadResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "capo_launch_wizard.types.list_workloads_output.ListWorkloadsOutput":
        """<p>Lists the available workload names. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html">ListWorkloadDeploymentPatterns</a> operation to discover the available deployment patterns for a given workload.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all available workloads supported by AWS Launch Wizard.

            >>> await client.list_workloads()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.list_workloads_input.ListWorkloadsInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.list_workloads_output.ListWorkloadsOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.list_workloads

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.list_workloads.async_list_workloads(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.list_workloads_input.ListWorkloadsInput = {}
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

    async def iter_list_workloads(
        self,
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_workload_results.MaxWorkloadResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_launch_wizard.types.workload_data_summary.WorkloadDataSummary]":
        _token = next_token
        while True:
            _response = await self.list_workloads(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workloads",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_workload_deployment_pattern(
        self,
        workload_name: "capo_launch_wizard.types.workload_name.WorkloadName",
        deployment_pattern_name: "capo_launch_wizard.types.deployment_pattern_name.DeploymentPatternName",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.get_workload_deployment_pattern_output.GetWorkloadDeploymentPatternOutput":
        """<p>Returns details for a given workload and deployment pattern, including the available specifications. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html">ListWorkloads</a> operation to discover the available workload names and the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html">ListWorkloadDeploymentPatterns</a> operation to discover the available deployment pattern names of a given workload.</p>

        Args:
            workload_name: <p>The name of the workload.</p>
            deployment_pattern_name: <p>The name of the deployment pattern.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get details about a specific Workload deployment pattern

            >>> await client.get_workload_deployment_pattern(workload_name='MicrosoftActiveDirectory', deployment_pattern_name='adSelfManagedNewVpc')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.get_workload_deployment_pattern_input.GetWorkloadDeploymentPatternInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.get_workload_deployment_pattern_output.GetWorkloadDeploymentPatternOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.get_workload_deployment_pattern

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.get_workload_deployment_pattern.async_get_workload_deployment_pattern(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.get_workload_deployment_pattern_input.GetWorkloadDeploymentPatternInput = {
            "workload_name": workload_name,
            "deployment_pattern_name": deployment_pattern_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workload_deployment_patterns(
        self,
        workload_name: "capo_launch_wizard.types.workload_name.WorkloadName",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_workload_deployment_pattern_results.MaxWorkloadDeploymentPatternResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "capo_launch_wizard.types.list_workload_deployment_patterns_output.ListWorkloadDeploymentPatternsOutput":
        """<p>Lists the workload deployment patterns for a given workload name. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html">ListWorkloads</a> operation to discover the available workload names.</p>

        Args:
            workload_name: <p>The name of the workload.</p>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all available workloads supported by AWS Launch Wizard.

            >>> await client.list_workload_deployment_patterns(workload_name='SAP')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.list_workload_deployment_patterns_input.ListWorkloadDeploymentPatternsInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.list_workload_deployment_patterns_output.ListWorkloadDeploymentPatternsOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.list_workload_deployment_patterns

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.list_workload_deployment_patterns.async_list_workload_deployment_patterns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.list_workload_deployment_patterns_input.ListWorkloadDeploymentPatternsInput = {
            "workload_name": workload_name
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

    async def iter_list_workload_deployment_patterns(
        self,
        workload_name: "capo_launch_wizard.types.workload_name.WorkloadName",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_workload_deployment_pattern_results.MaxWorkloadDeploymentPatternResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_launch_wizard.types.workload_deployment_pattern_data_summary.WorkloadDeploymentPatternDataSummary]":
        _token = next_token
        while True:
            _response = await self.list_workload_deployment_patterns(
                workload_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workload_deployment_patterns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_deployment_pattern_version(
        self,
        workload_name: "capo_launch_wizard.types.workload_name.WorkloadName",
        deployment_pattern_name: "capo_launch_wizard.types.deployment_pattern_name.DeploymentPatternName",
        deployment_pattern_version_name: "capo_launch_wizard.types.deployment_pattern_version_name.DeploymentPatternVersionName",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.get_deployment_pattern_version_output.GetDeploymentPatternVersionOutput":
        """<p>Returns information about a deployment pattern version.</p>

        Args:
            workload_name: <p>The name of the workload. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html"> <code>ListWorkloads</code> </a> operation to discover supported values for this parameter.</p>
            deployment_pattern_name: <p>The name of the deployment pattern. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html"> <code>ListWorkloadDeploymentPatterns</code> </a> operation to discover supported values for this parameter.</p>
            deployment_pattern_version_name: <p>The name of the deployment pattern version.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.get_deployment_pattern_version_input.GetDeploymentPatternVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.get_deployment_pattern_version_output.GetDeploymentPatternVersionOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.get_deployment_pattern_version

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.get_deployment_pattern_version.async_get_deployment_pattern_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.get_deployment_pattern_version_input.GetDeploymentPatternVersionInput = {
            "workload_name": workload_name,
            "deployment_pattern_name": deployment_pattern_name,
            "deployment_pattern_version_name": deployment_pattern_version_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_deployment_pattern_versions(
        self,
        workload_name: "capo_launch_wizard.types.workload_name.WorkloadName",
        deployment_pattern_name: "capo_launch_wizard.types.deployment_pattern_name.DeploymentPatternName",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_workload_results.MaxWorkloadResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
        filters: Optional["capo_launch_wizard.types.filter_list.FilterList"] = None,
    ) -> "capo_launch_wizard.types.list_deployment_pattern_versions_output.ListDeploymentPatternVersionsOutput":
        """<p>Lists the deployment pattern versions.</p>

        Args:
            workload_name: <p>The name of the workload. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html"> <code>ListWorkloads</code> </a> operation to discover supported values for this parameter.</p>
            deployment_pattern_name: <p>The name of the deployment pattern. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html"> <code>ListWorkloadDeploymentPatterns</code> </a> operation to discover supported values for this parameter.</p>
            max_results: <p>The maximum number of deployment pattern versions to list.</p>
            next_token: <p>The token for the next set of results.</p>
            filters: <p>Filters to apply when listing deployment pattern versions.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all visible versions for the given workload and deployment pattern.

            >>> await client.list_deployment_pattern_versions(workload_name='security-automations-for-aws-waf', deployment_pattern_name='default')
            List filtered versions for the given workload and deployment pattern.

            >>> await client.list_deployment_pattern_versions(workload_name='security-automations-for-aws-waf', deployment_pattern_name='default', filters=[{'name': 'updateFromVersion', 'values': ['4.0.2']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.list_deployment_pattern_versions_input.ListDeploymentPatternVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.list_deployment_pattern_versions_output.ListDeploymentPatternVersionsOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.list_deployment_pattern_versions

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.list_deployment_pattern_versions.async_list_deployment_pattern_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.list_deployment_pattern_versions_input.ListDeploymentPatternVersionsInput = {
            "workload_name": workload_name,
            "deployment_pattern_name": deployment_pattern_name,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_deployment_pattern_versions(
        self,
        workload_name: "capo_launch_wizard.types.workload_name.WorkloadName",
        deployment_pattern_name: "capo_launch_wizard.types.deployment_pattern_name.DeploymentPatternName",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_workload_results.MaxWorkloadResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
        filters: Optional["capo_launch_wizard.types.filter_list.FilterList"] = None,
    ) -> "AsyncIterator[capo_launch_wizard.types.deployment_pattern_version_data_summary.DeploymentPatternVersionDataSummary]":
        _token = next_token
        while True:
            _response = await self.list_deployment_pattern_versions(
                workload_name,
                deployment_pattern_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("deployment_pattern_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
