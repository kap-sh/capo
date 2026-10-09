"""Generated from Smithy shape ``com.amazonaws.codeconnections#CodeConnections_20231201``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_codeconnections._auth._signers
import capo_codeconnections._auth._sigv4
from capo_codeconnections._auth._identity import Credentials
from capo_codeconnections._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_codeconnections._auth._zapros_handler import AuthMiddleware
from capo_codeconnections._pagination import resolve_path as _resolve_path
from capo_codeconnections._services._aws_config import aaws_config
from capo_codeconnections._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_codeconnections.types.amazon_resource_name
    import capo_codeconnections.types.branch_name
    import capo_codeconnections.types.connection_arn
    import capo_codeconnections.types.connection_name
    import capo_codeconnections.types.create_connection_input
    import capo_codeconnections.types.create_connection_output
    import capo_codeconnections.types.create_host_input
    import capo_codeconnections.types.create_host_output
    import capo_codeconnections.types.create_repository_link_input
    import capo_codeconnections.types.create_repository_link_output
    import capo_codeconnections.types.create_sync_configuration_input
    import capo_codeconnections.types.create_sync_configuration_output
    import capo_codeconnections.types.delete_connection_input
    import capo_codeconnections.types.delete_connection_output
    import capo_codeconnections.types.delete_host_input
    import capo_codeconnections.types.delete_host_output
    import capo_codeconnections.types.delete_repository_link_input
    import capo_codeconnections.types.delete_repository_link_output
    import capo_codeconnections.types.delete_sync_configuration_input
    import capo_codeconnections.types.delete_sync_configuration_output
    import capo_codeconnections.types.deployment_file_path
    import capo_codeconnections.types.get_connection_input
    import capo_codeconnections.types.get_connection_output
    import capo_codeconnections.types.get_host_input
    import capo_codeconnections.types.get_host_output
    import capo_codeconnections.types.get_repository_link_input
    import capo_codeconnections.types.get_repository_link_output
    import capo_codeconnections.types.get_repository_sync_status_input
    import capo_codeconnections.types.get_repository_sync_status_output
    import capo_codeconnections.types.get_resource_sync_status_input
    import capo_codeconnections.types.get_resource_sync_status_output
    import capo_codeconnections.types.get_sync_blocker_summary_input
    import capo_codeconnections.types.get_sync_blocker_summary_output
    import capo_codeconnections.types.get_sync_configuration_input
    import capo_codeconnections.types.get_sync_configuration_output
    import capo_codeconnections.types.host_arn
    import capo_codeconnections.types.host_name
    import capo_codeconnections.types.iam_role_arn
    import capo_codeconnections.types.id
    import capo_codeconnections.types.kms_key_arn
    import capo_codeconnections.types.list_connections_input
    import capo_codeconnections.types.list_connections_output
    import capo_codeconnections.types.list_hosts_input
    import capo_codeconnections.types.list_hosts_output
    import capo_codeconnections.types.list_repository_links_input
    import capo_codeconnections.types.list_repository_links_output
    import capo_codeconnections.types.list_repository_sync_definitions_input
    import capo_codeconnections.types.list_repository_sync_definitions_output
    import capo_codeconnections.types.list_sync_configurations_input
    import capo_codeconnections.types.list_sync_configurations_output
    import capo_codeconnections.types.list_tags_for_resource_input
    import capo_codeconnections.types.list_tags_for_resource_output
    import capo_codeconnections.types.max_results
    import capo_codeconnections.types.next_token
    import capo_codeconnections.types.owner_id
    import capo_codeconnections.types.provider_type
    import capo_codeconnections.types.publish_deployment_status
    import capo_codeconnections.types.pull_request_comment
    import capo_codeconnections.types.repository_link_id
    import capo_codeconnections.types.repository_name
    import capo_codeconnections.types.resolved_reason
    import capo_codeconnections.types.resource_name
    import capo_codeconnections.types.sharp_next_token
    import capo_codeconnections.types.sync_configuration_type
    import capo_codeconnections.types.tag_key_list
    import capo_codeconnections.types.tag_list
    import capo_codeconnections.types.tag_resource_input
    import capo_codeconnections.types.tag_resource_output
    import capo_codeconnections.types.trigger_resource_update_on
    import capo_codeconnections.types.untag_resource_input
    import capo_codeconnections.types.untag_resource_output
    import capo_codeconnections.types.update_host_input
    import capo_codeconnections.types.update_host_output
    import capo_codeconnections.types.update_repository_link_input
    import capo_codeconnections.types.update_repository_link_output
    import capo_codeconnections.types.update_sync_blocker_input
    import capo_codeconnections.types.update_sync_blocker_output
    import capo_codeconnections.types.update_sync_configuration_input
    import capo_codeconnections.types.update_sync_configuration_output
    import capo_codeconnections.types.url
    import capo_codeconnections.types.vpc_configuration


class AsyncCodeConnectionsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncCodeConnectionsClient:
    """A client for the ``CodeConnections`` service.

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
        self._config = AsyncCodeConnectionsClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCodeConnectionsClientConfig = config_overrides or {}
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

    async def create_connection(
        self,
        connection_name: "capo_codeconnections.types.connection_name.ConnectionName",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        provider_type: Optional[
            "capo_codeconnections.types.provider_type.ProviderType"
        ] = None,
        tags: Optional["capo_codeconnections.types.tag_list.TagList"] = None,
        host_arn: Optional["capo_codeconnections.types.host_arn.HostArn"] = None,
    ) -> "capo_codeconnections.types.create_connection_output.CreateConnectionOutput":
        """<p>Creates a connection that can then be given to other Amazon Web Services services like CodePipeline so that it can access third-party code repositories. The connection is in pending status until the third-party connection handshake is completed from the console.</p>

        Args:
            provider_type: <p>The name of the external provider where your third-party code repository is configured.</p>
            connection_name: <p>The name of the connection to be created.</p>
            tags: <p>The key-value pair to use when tagging the resource.</p>
            host_arn: <p>The Amazon Resource Name (ARN) of the host associated with the connection to be created.</p>

        Raises:
            capo_codeconnections.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded the maximum limit for connections.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.resource_unavailable_exception.ResourceUnavailableException: <p>Resource not found. Verify the ARN for the host resource and try again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.create_connection_input.CreateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.create_connection_output.CreateConnectionOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.create_connection

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.create_connection.async_create_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.create_connection_input.CreateConnectionInput = {
            "connection_name": connection_name
        }
        if provider_type is not None:
            input_["provider_type"] = provider_type
        if tags is not None:
            input_["tags"] = tags
        if host_arn is not None:
            input_["host_arn"] = host_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_host(
        self,
        name: "capo_codeconnections.types.host_name.HostName",
        provider_type: "capo_codeconnections.types.provider_type.ProviderType",
        provider_endpoint: "capo_codeconnections.types.url.Url",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        vpc_configuration: Optional[
            "capo_codeconnections.types.vpc_configuration.VpcConfiguration"
        ] = None,
        tags: Optional["capo_codeconnections.types.tag_list.TagList"] = None,
    ) -> "capo_codeconnections.types.create_host_output.CreateHostOutput":
        """<p>Creates a resource that represents the infrastructure where a third-party provider is installed. The host is used when you create connections to an installed third-party provider type, such as GitHub Enterprise Server. You create one host for all connections to that provider.</p> <note> <p>A host created through the CLI or the SDK is in `PENDING` status by default. You can make its status `AVAILABLE` by setting up the host in the console.</p> </note>

        Args:
            name: <p>The name of the host to be created.</p>
            provider_type: <p>The name of the installed provider to be associated with your connection. The host resource represents the infrastructure where your provider type is installed. The valid provider type is GitHub Enterprise Server.</p>
            provider_endpoint: <p>The endpoint of the infrastructure to be represented by the host after it is created.</p>
            vpc_configuration: <p>The VPC configuration to be provisioned for the host. A VPC must be configured and the infrastructure to be represented by the host must already be connected to the VPC.</p>
            tags: <p>Tags for the host to be created.</p>

        Raises:
            capo_codeconnections.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded the maximum limit for connections.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.create_host_input.CreateHostInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.create_host_output.CreateHostOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.create_host

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.create_host.async_create_host(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.create_host_input.CreateHostInput = {
            "name": name,
            "provider_type": provider_type,
            "provider_endpoint": provider_endpoint,
        }
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_repository_link(
        self,
        connection_arn: "capo_codeconnections.types.connection_arn.ConnectionArn",
        owner_id: "capo_codeconnections.types.owner_id.OwnerId",
        repository_name: "capo_codeconnections.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        encryption_key_arn: Optional[
            "capo_codeconnections.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_codeconnections.types.tag_list.TagList"] = None,
    ) -> "capo_codeconnections.types.create_repository_link_output.CreateRepositoryLinkOutput":
        """<p>Creates a link to a specified external Git repository. A repository link allows Git sync to monitor and sync changes to files in a specified Git repository.</p>

        Args:
            connection_arn: <p>The Amazon Resource Name (ARN) of the connection to be associated with the repository link.</p>
            owner_id: <p>The owner ID for the repository associated with a specific sync configuration, such as the owner ID in GitHub.</p>
            repository_name: <p>The name of the repository to be associated with the repository link.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) encryption key for the repository to be associated with the repository link.</p>
            tags: <p>The tags for the repository to be associated with the repository link.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time. </p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded the maximum limit for connections.</p>
            capo_codeconnections.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>Unable to create resource. Resource already exists.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.create_repository_link_input.CreateRepositoryLinkInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.create_repository_link_output.CreateRepositoryLinkOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.create_repository_link

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.create_repository_link.async_create_repository_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.create_repository_link_input.CreateRepositoryLinkInput = {
            "connection_arn": connection_arn,
            "owner_id": owner_id,
            "repository_name": repository_name,
        }
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_sync_configuration(
        self,
        branch: "capo_codeconnections.types.branch_name.BranchName",
        config_file: "capo_codeconnections.types.deployment_file_path.DeploymentFilePath",
        repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId",
        resource_name: "capo_codeconnections.types.resource_name.ResourceName",
        role_arn: "capo_codeconnections.types.iam_role_arn.IamRoleArn",
        sync_type: "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        publish_deployment_status: Optional[
            "capo_codeconnections.types.publish_deployment_status.PublishDeploymentStatus"
        ] = None,
        trigger_resource_update_on: Optional[
            "capo_codeconnections.types.trigger_resource_update_on.TriggerResourceUpdateOn"
        ] = None,
        pull_request_comment: Optional[
            "capo_codeconnections.types.pull_request_comment.PullRequestComment"
        ] = None,
    ) -> "capo_codeconnections.types.create_sync_configuration_output.CreateSyncConfigurationOutput":
        """<p>Creates a sync configuration which allows Amazon Web Services to sync content from a Git repository to update a specified Amazon Web Services resource. Parameters for the sync configuration are determined by the sync type.</p>

        Args:
            branch: <p>The branch in the repository from which changes will be synced.</p>
            config_file: <p>The file name of the configuration file that manages syncing between the connection and the repository. This configuration file is stored in the repository.</p>
            repository_link_id: <p>The ID of the repository link created for the connection. A repository link allows Git sync to monitor and sync changes to files in a specified Git repository.</p>
            resource_name: <p>The name of the Amazon Web Services resource (for example, a CloudFormation stack in the case of CFN_STACK_SYNC) that will be synchronized from the linked repository.</p>
            role_arn: <p>The ARN of the IAM role that grants permission for Amazon Web Services to use Git sync to update a given Amazon Web Services resource on your behalf.</p>
            sync_type: <p>The type of sync configuration.</p>
            publish_deployment_status: <p>Whether to enable or disable publishing of deployment status to source providers.</p>
            trigger_resource_update_on: <p>When to trigger Git sync to begin the stack update.</p>
            pull_request_comment: <p>A toggle that specifies whether to enable or disable pull request comments for the sync configuration to be created.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time. </p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded the maximum limit for connections.</p>
            capo_codeconnections.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>Unable to create resource. Resource already exists.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.create_sync_configuration_input.CreateSyncConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.create_sync_configuration_output.CreateSyncConfigurationOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.create_sync_configuration

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.create_sync_configuration.async_create_sync_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.create_sync_configuration_input.CreateSyncConfigurationInput = {
            "branch": branch,
            "config_file": config_file,
            "repository_link_id": repository_link_id,
            "resource_name": resource_name,
            "role_arn": role_arn,
            "sync_type": sync_type,
        }
        if publish_deployment_status is not None:
            input_["publish_deployment_status"] = publish_deployment_status
        if trigger_resource_update_on is not None:
            input_["trigger_resource_update_on"] = trigger_resource_update_on
        if pull_request_comment is not None:
            input_["pull_request_comment"] = pull_request_comment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connection(
        self,
        connection_arn: "capo_codeconnections.types.connection_arn.ConnectionArn",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.delete_connection_output.DeleteConnectionOutput":
        """<p>The connection to be deleted.</p>

        Args:
            connection_arn: <p>The Amazon Resource Name (ARN) of the connection to be deleted.</p> <note> <p>The ARN is never reused if the connection is deleted.</p> </note>

        Raises:
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.delete_connection_input.DeleteConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.delete_connection_output.DeleteConnectionOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.delete_connection

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.delete_connection.async_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.delete_connection_input.DeleteConnectionInput = {
            "connection_arn": connection_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_host(
        self,
        host_arn: "capo_codeconnections.types.host_arn.HostArn",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.delete_host_output.DeleteHostOutput":
        """<p>The host to be deleted. Before you delete a host, all connections associated to the host must be deleted.</p> <note> <p>A host cannot be deleted if it is in the VPC_CONFIG_INITIALIZING or VPC_CONFIG_DELETING state.</p> </note>

        Args:
            host_arn: <p>The Amazon Resource Name (ARN) of the host to be deleted.</p>

        Raises:
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.resource_unavailable_exception.ResourceUnavailableException: <p>Resource not found. Verify the ARN for the host resource and try again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.delete_host_input.DeleteHostInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.delete_host_output.DeleteHostOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.delete_host

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.delete_host.async_delete_host(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.delete_host_input.DeleteHostInput = {
            "host_arn": host_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_repository_link(
        self,
        repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.delete_repository_link_output.DeleteRepositoryLinkOutput":
        """<p>Deletes the association between your connection and a specified external Git repository.</p>

        Args:
            repository_link_id: <p>The ID of the repository link to be deleted.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time. </p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.sync_configuration_still_exists_exception.SyncConfigurationStillExistsException: <p>Unable to continue. The sync blocker still exists.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.unsupported_provider_type_exception.UnsupportedProviderTypeException: <p>The specified provider type is not supported for connections.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.delete_repository_link_input.DeleteRepositoryLinkInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.delete_repository_link_output.DeleteRepositoryLinkOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.delete_repository_link

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.delete_repository_link.async_delete_repository_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.delete_repository_link_input.DeleteRepositoryLinkInput = {
            "repository_link_id": repository_link_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_sync_configuration(
        self,
        sync_type: "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
        resource_name: "capo_codeconnections.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.delete_sync_configuration_output.DeleteSyncConfigurationOutput":
        """<p>Deletes the sync configuration for a specified repository and connection.</p>

        Args:
            sync_type: <p>The type of sync configuration to be deleted.</p>
            resource_name: <p>The name of the Amazon Web Services resource associated with the sync configuration to be deleted.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time. </p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded the maximum limit for connections.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.delete_sync_configuration_input.DeleteSyncConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.delete_sync_configuration_output.DeleteSyncConfigurationOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.delete_sync_configuration

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.delete_sync_configuration.async_delete_sync_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.delete_sync_configuration_input.DeleteSyncConfigurationInput = {
            "sync_type": sync_type,
            "resource_name": resource_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connection(
        self,
        connection_arn: "capo_codeconnections.types.connection_arn.ConnectionArn",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.get_connection_output.GetConnectionOutput":
        """<p>Returns the connection ARN and details such as status, owner, and provider type.</p>

        Args:
            connection_arn: <p>The Amazon Resource Name (ARN) of a connection.</p>

        Raises:
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.resource_unavailable_exception.ResourceUnavailableException: <p>Resource not found. Verify the ARN for the host resource and try again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.get_connection_input.GetConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.get_connection_output.GetConnectionOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.get_connection

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.get_connection.async_get_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.get_connection_input.GetConnectionInput = {
            "connection_arn": connection_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_host(
        self,
        host_arn: "capo_codeconnections.types.host_arn.HostArn",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.get_host_output.GetHostOutput":
        """<p>Returns the host ARN and details such as status, provider type, endpoint, and, if applicable, the VPC configuration.</p>

        Args:
            host_arn: <p>The Amazon Resource Name (ARN) of the requested host.</p>

        Raises:
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.resource_unavailable_exception.ResourceUnavailableException: <p>Resource not found. Verify the ARN for the host resource and try again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.get_host_input.GetHostInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.get_host_output.GetHostOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.get_host

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.get_host.async_get_host(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.get_host_input.GetHostInput = {
            "host_arn": host_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_repository_link(
        self,
        repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> (
        "capo_codeconnections.types.get_repository_link_output.GetRepositoryLinkOutput"
    ):
        """<p>Returns details about a repository link. A repository link allows Git sync to monitor and sync changes from files in a specified Git repository.</p>

        Args:
            repository_link_id: <p>The ID of the repository link to get.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time. </p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.get_repository_link_input.GetRepositoryLinkInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.get_repository_link_output.GetRepositoryLinkOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.get_repository_link

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.get_repository_link.async_get_repository_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.get_repository_link_input.GetRepositoryLinkInput = {
            "repository_link_id": repository_link_id
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
        branch: "capo_codeconnections.types.branch_name.BranchName",
        repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId",
        sync_type: "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.get_repository_sync_status_output.GetRepositorySyncStatusOutput":
        """<p>Returns details about the sync status for a repository. A repository sync uses Git sync to push and pull changes from your remote repository.</p>

        Args:
            branch: <p>The branch of the repository link for the requested repository sync status.</p>
            repository_link_id: <p>The repository link ID for the requested repository sync status.</p>
            sync_type: <p>The sync type of the requested sync status.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.get_repository_sync_status_input.GetRepositorySyncStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.get_repository_sync_status_output.GetRepositorySyncStatusOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.get_repository_sync_status

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.get_repository_sync_status.async_get_repository_sync_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.get_repository_sync_status_input.GetRepositorySyncStatusInput = {
            "branch": branch,
            "repository_link_id": repository_link_id,
            "sync_type": sync_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_sync_status(
        self,
        resource_name: "capo_codeconnections.types.resource_name.ResourceName",
        sync_type: "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.get_resource_sync_status_output.GetResourceSyncStatusOutput":
        """<p>Returns the status of the sync with the Git repository for a specific Amazon Web Services resource.</p>

        Args:
            resource_name: <p>The name of the Amazon Web Services resource for the sync status with the Git repository.</p>
            sync_type: <p>The sync type for the sync status with the Git repository.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.get_resource_sync_status_input.GetResourceSyncStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.get_resource_sync_status_output.GetResourceSyncStatusOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.get_resource_sync_status

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.get_resource_sync_status.async_get_resource_sync_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.get_resource_sync_status_input.GetResourceSyncStatusInput = {
            "resource_name": resource_name,
            "sync_type": sync_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_sync_blocker_summary(
        self,
        sync_type: "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
        resource_name: "capo_codeconnections.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.get_sync_blocker_summary_output.GetSyncBlockerSummaryOutput":
        """<p>Returns a list of the most recent sync blockers.</p>

        Args:
            sync_type: <p>The sync type for the sync blocker summary.</p>
            resource_name: <p>The name of the Amazon Web Services resource currently blocked from automatically being synced from a Git repository.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.get_sync_blocker_summary_input.GetSyncBlockerSummaryInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.get_sync_blocker_summary_output.GetSyncBlockerSummaryOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.get_sync_blocker_summary

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.get_sync_blocker_summary.async_get_sync_blocker_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.get_sync_blocker_summary_input.GetSyncBlockerSummaryInput = {
            "sync_type": sync_type,
            "resource_name": resource_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_sync_configuration(
        self,
        sync_type: "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
        resource_name: "capo_codeconnections.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.get_sync_configuration_output.GetSyncConfigurationOutput":
        """<p>Returns details about a sync configuration, including the sync type and resource name. A sync configuration allows the configuration to sync (push and pull) changes from the remote repository for a specified branch in a Git repository.</p>

        Args:
            sync_type: <p>The sync type for the sync configuration for which you want to retrieve information.</p>
            resource_name: <p>The name of the Amazon Web Services resource for the sync configuration for which you want to retrieve information.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.get_sync_configuration_input.GetSyncConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.get_sync_configuration_output.GetSyncConfigurationOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.get_sync_configuration

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.get_sync_configuration.async_get_sync_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.get_sync_configuration_input.GetSyncConfigurationInput = {
            "sync_type": sync_type,
            "resource_name": resource_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_connections(
        self,
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        provider_type_filter: Optional[
            "capo_codeconnections.types.provider_type.ProviderType"
        ] = None,
        host_arn_filter: Optional["capo_codeconnections.types.host_arn.HostArn"] = None,
        max_results: Optional[
            "capo_codeconnections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_codeconnections.types.next_token.NextToken"] = None,
    ) -> "capo_codeconnections.types.list_connections_output.ListConnectionsOutput":
        """<p>Lists the connections associated with your account.</p>

        Args:
            provider_type_filter: <p>Filters the list of connections to those associated with a specified provider, such as Bitbucket.</p>
            host_arn_filter: <p>Filters the list of connections to those associated with a specified host.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token that was returned from the previous <code>ListConnections</code> call, which can be used to return the next set of connections in the list.</p>

        Raises:
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.list_connections_input.ListConnectionsInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.list_connections_output.ListConnectionsOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.list_connections

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.list_connections.async_list_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.list_connections_input.ListConnectionsInput = {}
        if provider_type_filter is not None:
            input_["provider_type_filter"] = provider_type_filter
        if host_arn_filter is not None:
            input_["host_arn_filter"] = host_arn_filter
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

    async def iter_list_connections(
        self,
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        provider_type_filter: Optional[
            "capo_codeconnections.types.provider_type.ProviderType"
        ] = None,
        host_arn_filter: Optional["capo_codeconnections.types.host_arn.HostArn"] = None,
        max_results: Optional[
            "capo_codeconnections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_codeconnections.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_codeconnections.types.list_connections_output.ListConnectionsOutput]":
        _token = next_token
        while True:
            _response = await self.list_connections(
                config_overrides=config_overrides,
                provider_type_filter=provider_type_filter,
                host_arn_filter=host_arn_filter,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_hosts(
        self,
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        max_results: Optional[
            "capo_codeconnections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_codeconnections.types.next_token.NextToken"] = None,
    ) -> "capo_codeconnections.types.list_hosts_output.ListHostsOutput":
        """<p>Lists the hosts associated with your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token that was returned from the previous <code>ListHosts</code> call, which can be used to return the next set of hosts in the list.</p>

        Raises:
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.list_hosts_input.ListHostsInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.list_hosts_output.ListHostsOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.list_hosts

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.list_hosts.async_list_hosts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.list_hosts_input.ListHostsInput = {}
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

    async def iter_list_hosts(
        self,
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        max_results: Optional[
            "capo_codeconnections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_codeconnections.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_codeconnections.types.list_hosts_output.ListHostsOutput]":
        _token = next_token
        while True:
            _response = await self.list_hosts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_repository_links(
        self,
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        max_results: Optional[
            "capo_codeconnections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeconnections.types.sharp_next_token.SharpNextToken"
        ] = None,
    ) -> "capo_codeconnections.types.list_repository_links_output.ListRepositoryLinksOutput":
        """<p>Lists the repository links created for connections in your account.</p>

        Args:
            max_results: <p> A non-zero, non-negative integer used to limit the number of returned results.</p>
            next_token: <p> An enumeration token that, when provided in a request, returns the next batch of the results.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time. </p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.list_repository_links_input.ListRepositoryLinksInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.list_repository_links_output.ListRepositoryLinksOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.list_repository_links

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.list_repository_links.async_list_repository_links(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.list_repository_links_input.ListRepositoryLinksInput = {}
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

    async def iter_list_repository_links(
        self,
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        max_results: Optional[
            "capo_codeconnections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeconnections.types.sharp_next_token.SharpNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_codeconnections.types.list_repository_links_output.ListRepositoryLinksOutput]":
        _token = next_token
        while True:
            _response = await self.list_repository_links(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_repository_sync_definitions(
        self,
        repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId",
        sync_type: "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.list_repository_sync_definitions_output.ListRepositorySyncDefinitionsOutput":
        """<p>Lists the repository sync definitions for repository links in your account.</p>

        Args:
            repository_link_id: <p>The ID of the repository link for the sync definition for which you want to retrieve information.</p>
            sync_type: <p>The sync type of the repository link for the the sync definition for which you want to retrieve information.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.list_repository_sync_definitions_input.ListRepositorySyncDefinitionsInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.list_repository_sync_definitions_output.ListRepositorySyncDefinitionsOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.list_repository_sync_definitions

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.list_repository_sync_definitions.async_list_repository_sync_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.list_repository_sync_definitions_input.ListRepositorySyncDefinitionsInput = {
            "repository_link_id": repository_link_id,
            "sync_type": sync_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_sync_configurations(
        self,
        repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId",
        sync_type: "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        max_results: Optional[
            "capo_codeconnections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeconnections.types.sharp_next_token.SharpNextToken"
        ] = None,
    ) -> "capo_codeconnections.types.list_sync_configurations_output.ListSyncConfigurationsOutput":
        """<p>Returns a list of sync configurations for a specified repository.</p>

        Args:
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results.</p>
            next_token: <p>An enumeration token that allows the operation to batch the results of the operation.</p>
            repository_link_id: <p>The ID of the repository link for the requested list of sync configurations.</p>
            sync_type: <p>The sync type for the requested list of sync configurations.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.list_sync_configurations_input.ListSyncConfigurationsInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.list_sync_configurations_output.ListSyncConfigurationsOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.list_sync_configurations

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.list_sync_configurations.async_list_sync_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.list_sync_configurations_input.ListSyncConfigurationsInput = {
            "repository_link_id": repository_link_id,
            "sync_type": sync_type,
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

    async def iter_list_sync_configurations(
        self,
        repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId",
        sync_type: "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        max_results: Optional[
            "capo_codeconnections.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeconnections.types.sharp_next_token.SharpNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_codeconnections.types.list_sync_configurations_output.ListSyncConfigurationsOutput]":
        _token = next_token
        while True:
            _response = await self.list_sync_configurations(
                repository_link_id,
                sync_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_codeconnections.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Gets the set of key-value pairs (metadata) that are used to manage the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to get information about tags, if any.</p>

        Raises:
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.list_tags_for_resource_input.ListTagsForResourceInput = {
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
        resource_arn: "capo_codeconnections.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_codeconnections.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.tag_resource_output.TagResourceOutput":
        """<p>Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which you want to add or update tags.</p>
            tags: <p>The tags you want to modify or add to the resource.</p>

        Raises:
            capo_codeconnections.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded the maximum limit for connections.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.tag_resource

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_codeconnections.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_codeconnections.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> "capo_codeconnections.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from an Amazon Web Services resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The list of keys for the tags to be removed from the resource.</p>

        Raises:
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.untag_resource

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.untag_resource_input.UntagResourceInput = {
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

    async def update_host(
        self,
        host_arn: "capo_codeconnections.types.host_arn.HostArn",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        provider_endpoint: Optional["capo_codeconnections.types.url.Url"] = None,
        vpc_configuration: Optional[
            "capo_codeconnections.types.vpc_configuration.VpcConfiguration"
        ] = None,
    ) -> "capo_codeconnections.types.update_host_output.UpdateHostOutput":
        """<p>Updates a specified host with the provided configurations.</p>

        Args:
            host_arn: <p>The Amazon Resource Name (ARN) of the host to be updated.</p>
            provider_endpoint: <p>The URL or endpoint of the host to be updated.</p>
            vpc_configuration: <p>The VPC configuration of the host to be updated. A VPC must be configured and the infrastructure to be represented by the host must already be connected to the VPC.</p>

        Raises:
            capo_codeconnections.errors.conflict_exception.ConflictException: <p>Two conflicting operations have been made on the same resource.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.resource_unavailable_exception.ResourceUnavailableException: <p>Resource not found. Verify the ARN for the host resource and try again.</p>
            capo_codeconnections.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported. Check the connection status and try again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.update_host_input.UpdateHostInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.update_host_output.UpdateHostOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.update_host

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.update_host.async_update_host(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.update_host_input.UpdateHostInput = {
            "host_arn": host_arn
        }
        if provider_endpoint is not None:
            input_["provider_endpoint"] = provider_endpoint
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_repository_link(
        self,
        repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        connection_arn: Optional[
            "capo_codeconnections.types.connection_arn.ConnectionArn"
        ] = None,
        encryption_key_arn: Optional[
            "capo_codeconnections.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_codeconnections.types.update_repository_link_output.UpdateRepositoryLinkOutput":
        """<p>Updates the association between your connection and a specified external Git repository. A repository link allows Git sync to monitor and sync changes to files in a specified Git repository.</p>

        Args:
            connection_arn: <p>The Amazon Resource Name (ARN) of the connection for the repository link to be updated. The updated connection ARN must have the same providerType (such as GitHub) as the original connection ARN for the repo link.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the encryption key for the repository link to be updated.</p>
            repository_link_id: <p>The ID of the repository link to be updated.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.conditional_check_failed_exception.ConditionalCheckFailedException: <p>The conditional check failed. Try again later.</p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.update_out_of_sync_exception.UpdateOutOfSyncException: <p>The update is out of sync. Try syncing again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.update_repository_link_input.UpdateRepositoryLinkInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.update_repository_link_output.UpdateRepositoryLinkOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.update_repository_link

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.update_repository_link.async_update_repository_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.update_repository_link_input.UpdateRepositoryLinkInput = {
            "repository_link_id": repository_link_id
        }
        if connection_arn is not None:
            input_["connection_arn"] = connection_arn
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_sync_blocker(
        self,
        id: "capo_codeconnections.types.id.Id",
        sync_type: "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
        resource_name: "capo_codeconnections.types.resource_name.ResourceName",
        resolved_reason: "capo_codeconnections.types.resolved_reason.ResolvedReason",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
    ) -> (
        "capo_codeconnections.types.update_sync_blocker_output.UpdateSyncBlockerOutput"
    ):
        """<p>Allows you to update the status of a sync blocker, resolving the blocker and allowing syncing to continue.</p>

        Args:
            id: <p>The ID of the sync blocker to be updated.</p>
            sync_type: <p>The sync type of the sync blocker to be updated.</p>
            resource_name: <p>The name of the resource for the sync blocker to be updated.</p>
            resolved_reason: <p>The reason for resolving the sync blocker.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.retry_latest_commit_failed_exception.RetryLatestCommitFailedException: <p>Retrying the latest commit failed. Try again later.</p>
            capo_codeconnections.errors.sync_blocker_does_not_exist_exception.SyncBlockerDoesNotExistException: <p>Unable to continue. The sync blocker does not exist.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.update_sync_blocker_input.UpdateSyncBlockerInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.update_sync_blocker_output.UpdateSyncBlockerOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.update_sync_blocker

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.update_sync_blocker.async_update_sync_blocker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.update_sync_blocker_input.UpdateSyncBlockerInput = {
            "id": id,
            "sync_type": sync_type,
            "resource_name": resource_name,
            "resolved_reason": resolved_reason,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_sync_configuration(
        self,
        resource_name: "capo_codeconnections.types.resource_name.ResourceName",
        sync_type: "capo_codeconnections.types.sync_configuration_type.SyncConfigurationType",
        *,
        config_overrides: Optional[AsyncCodeConnectionsClientConfig] = None,
        branch: Optional["capo_codeconnections.types.branch_name.BranchName"] = None,
        config_file: Optional[
            "capo_codeconnections.types.deployment_file_path.DeploymentFilePath"
        ] = None,
        repository_link_id: Optional[
            "capo_codeconnections.types.repository_link_id.RepositoryLinkId"
        ] = None,
        role_arn: Optional["capo_codeconnections.types.iam_role_arn.IamRoleArn"] = None,
        publish_deployment_status: Optional[
            "capo_codeconnections.types.publish_deployment_status.PublishDeploymentStatus"
        ] = None,
        trigger_resource_update_on: Optional[
            "capo_codeconnections.types.trigger_resource_update_on.TriggerResourceUpdateOn"
        ] = None,
        pull_request_comment: Optional[
            "capo_codeconnections.types.pull_request_comment.PullRequestComment"
        ] = None,
    ) -> "capo_codeconnections.types.update_sync_configuration_output.UpdateSyncConfigurationOutput":
        """<p>Updates the sync configuration for your connection and a specified external Git repository.</p>

        Args:
            branch: <p>The branch for the sync configuration to be updated.</p>
            config_file: <p>The configuration file for the sync configuration to be updated.</p>
            repository_link_id: <p>The ID of the repository link for the sync configuration to be updated.</p>
            resource_name: <p>The name of the Amazon Web Services resource for the sync configuration to be updated.</p>
            role_arn: <p>The ARN of the IAM role for the sync configuration to be updated.</p>
            sync_type: <p>The sync type for the sync configuration to be updated.</p>
            publish_deployment_status: <p>Whether to enable or disable publishing of deployment status to source providers.</p>
            trigger_resource_update_on: <p>When to trigger Git sync to begin the stack update.</p>
            pull_request_comment: <p>TA toggle that specifies whether to enable or disable pull request comments for the sync configuration to be updated.</p>

        Raises:
            capo_codeconnections.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_codeconnections.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time. </p>
            capo_codeconnections.errors.internal_server_exception.InternalServerException: <p>Received an internal server exception. Try again later.</p>
            capo_codeconnections.errors.invalid_input_exception.InvalidInputException: <p>The input is not valid. Verify that the action is typed correctly.</p>
            capo_codeconnections.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found. Verify the connection resource ARN and try again.</p>
            capo_codeconnections.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeconnections.errors.update_out_of_sync_exception.UpdateOutOfSyncException: <p>The update is out of sync. Try syncing again.</p>
            capo_codeconnections.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeconnections.types.update_sync_configuration_input.UpdateSyncConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_codeconnections.types.update_sync_configuration_output.UpdateSyncConfigurationOutput"
        ]:
            import capo_codeconnections._operations.code_connections_20231201.update_sync_configuration

            (
                output,
                http_response,
            ) = await capo_codeconnections._operations.code_connections_20231201.update_sync_configuration.async_update_sync_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeconnections.types.update_sync_configuration_input.UpdateSyncConfigurationInput = {
            "resource_name": resource_name,
            "sync_type": sync_type,
        }
        if branch is not None:
            input_["branch"] = branch
        if config_file is not None:
            input_["config_file"] = config_file
        if repository_link_id is not None:
            input_["repository_link_id"] = repository_link_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if publish_deployment_status is not None:
            input_["publish_deployment_status"] = publish_deployment_status
        if trigger_resource_update_on is not None:
            input_["trigger_resource_update_on"] = trigger_resource_update_on
        if pull_request_comment is not None:
            input_["pull_request_comment"] = pull_request_comment

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
