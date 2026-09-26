"""Generated from Smithy shape ``com.amazonaws.drs#ElasticDisasterRecoveryService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_drs._auth._signers
import capo_drs._auth._sigv4
from capo_drs._auth._identity import Credentials
from capo_drs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_drs._auth._zapros_handler import AuthMiddleware
from capo_drs._pagination import resolve_path as _resolve_path
from capo_drs._resources.elastic_disaster_recovery_service.account_resource import (
    AsyncAccountResource,
)
from capo_drs._resources.elastic_disaster_recovery_service.job_resource import (
    AsyncJobResource,
)
from capo_drs._resources.elastic_disaster_recovery_service.launch_configuration_template_resource import (
    AsyncLaunchConfigurationTemplateResource,
)
from capo_drs._resources.elastic_disaster_recovery_service.recovery_instance_resource import (
    AsyncRecoveryInstanceResource,
)
from capo_drs._resources.elastic_disaster_recovery_service.replication_configuration_template_resource import (
    AsyncReplicationConfigurationTemplateResource,
)
from capo_drs._resources.elastic_disaster_recovery_service.source_network_resource import (
    AsyncSourceNetworkResource,
)
from capo_drs._resources.elastic_disaster_recovery_service.source_server_resource import (
    AsyncSourceServerResource,
)
from capo_drs._services._aws_config import aaws_config
from capo_drs._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_drs.types.account
    import capo_drs.types.account_id
    import capo_drs.types.arn
    import capo_drs.types.associate_source_network_stack_request
    import capo_drs.types.associate_source_network_stack_response
    import capo_drs.types.aws_region
    import capo_drs.types.bounded_string
    import capo_drs.types.cfn_stack_name
    import capo_drs.types.create_extended_source_server_request
    import capo_drs.types.create_extended_source_server_response
    import capo_drs.types.create_launch_configuration_template_request
    import capo_drs.types.create_launch_configuration_template_response
    import capo_drs.types.create_replication_configuration_template_request
    import capo_drs.types.create_source_network_request
    import capo_drs.types.create_source_network_response
    import capo_drs.types.delete_job_request
    import capo_drs.types.delete_job_response
    import capo_drs.types.delete_launch_action_request
    import capo_drs.types.delete_launch_action_response
    import capo_drs.types.delete_launch_configuration_template_request
    import capo_drs.types.delete_launch_configuration_template_response
    import capo_drs.types.delete_recovery_instance_request
    import capo_drs.types.delete_replication_configuration_template_request
    import capo_drs.types.delete_replication_configuration_template_response
    import capo_drs.types.delete_source_network_request
    import capo_drs.types.delete_source_network_response
    import capo_drs.types.delete_source_server_request
    import capo_drs.types.delete_source_server_response
    import capo_drs.types.describe_job_log_items_request
    import capo_drs.types.describe_job_log_items_response
    import capo_drs.types.describe_jobs_request
    import capo_drs.types.describe_jobs_request_filters
    import capo_drs.types.describe_jobs_response
    import capo_drs.types.describe_launch_configuration_templates_request
    import capo_drs.types.describe_launch_configuration_templates_response
    import capo_drs.types.describe_recovery_instances_request
    import capo_drs.types.describe_recovery_instances_request_filters
    import capo_drs.types.describe_recovery_instances_response
    import capo_drs.types.describe_recovery_snapshots_request
    import capo_drs.types.describe_recovery_snapshots_request_filters
    import capo_drs.types.describe_recovery_snapshots_response
    import capo_drs.types.describe_replication_configuration_templates_request
    import capo_drs.types.describe_replication_configuration_templates_response
    import capo_drs.types.describe_source_networks_request
    import capo_drs.types.describe_source_networks_request_filters
    import capo_drs.types.describe_source_networks_response
    import capo_drs.types.describe_source_servers_request
    import capo_drs.types.describe_source_servers_request_filters
    import capo_drs.types.describe_source_servers_response
    import capo_drs.types.disconnect_recovery_instance_request
    import capo_drs.types.disconnect_source_server_request
    import capo_drs.types.ec2_instance_type
    import capo_drs.types.export_source_network_cfn_template_request
    import capo_drs.types.export_source_network_cfn_template_response
    import capo_drs.types.get_failback_replication_configuration_request
    import capo_drs.types.get_failback_replication_configuration_response
    import capo_drs.types.get_launch_configuration_request
    import capo_drs.types.get_replication_configuration_request
    import capo_drs.types.initialize_service_request
    import capo_drs.types.initialize_service_response
    import capo_drs.types.internet_protocol
    import capo_drs.types.job
    import capo_drs.types.job_id
    import capo_drs.types.job_log
    import capo_drs.types.launch_action
    import capo_drs.types.launch_action_category
    import capo_drs.types.launch_action_description
    import capo_drs.types.launch_action_id
    import capo_drs.types.launch_action_name
    import capo_drs.types.launch_action_order
    import capo_drs.types.launch_action_parameters
    import capo_drs.types.launch_action_resource_id
    import capo_drs.types.launch_action_version
    import capo_drs.types.launch_actions_request_filters
    import capo_drs.types.launch_configuration
    import capo_drs.types.launch_configuration_template
    import capo_drs.types.launch_configuration_template_i_ds
    import capo_drs.types.launch_configuration_template_id
    import capo_drs.types.launch_disposition
    import capo_drs.types.launch_into_instance_properties
    import capo_drs.types.licensing
    import capo_drs.types.list_extensible_source_servers_request
    import capo_drs.types.list_extensible_source_servers_response
    import capo_drs.types.list_launch_actions_request
    import capo_drs.types.list_launch_actions_response
    import capo_drs.types.list_staging_accounts_request
    import capo_drs.types.list_staging_accounts_response
    import capo_drs.types.list_tags_for_resource_request
    import capo_drs.types.list_tags_for_resource_response
    import capo_drs.types.max_results_replicating_source_servers
    import capo_drs.types.max_results_type
    import capo_drs.types.pagination_token
    import capo_drs.types.pit_policy
    import capo_drs.types.positive_integer
    import capo_drs.types.put_launch_action_request
    import capo_drs.types.put_launch_action_response
    import capo_drs.types.recovery_instance
    import capo_drs.types.recovery_instance_id
    import capo_drs.types.recovery_instances_for_termination_request
    import capo_drs.types.recovery_snapshot
    import capo_drs.types.recovery_snapshots_order
    import capo_drs.types.replication_configuration
    import capo_drs.types.replication_configuration_data_plane_routing
    import capo_drs.types.replication_configuration_default_large_staging_disk_type
    import capo_drs.types.replication_configuration_ebs_encryption
    import capo_drs.types.replication_configuration_replicated_disks
    import capo_drs.types.replication_configuration_template
    import capo_drs.types.replication_configuration_template_i_ds
    import capo_drs.types.replication_configuration_template_id
    import capo_drs.types.replication_servers_security_groups_i_ds
    import capo_drs.types.retry_data_replication_request
    import capo_drs.types.reverse_replication_request
    import capo_drs.types.reverse_replication_response
    import capo_drs.types.small_bounded_string
    import capo_drs.types.source_network
    import capo_drs.types.source_network_id
    import capo_drs.types.source_server
    import capo_drs.types.source_server_arn
    import capo_drs.types.source_server_id
    import capo_drs.types.ssm_document_name
    import capo_drs.types.staging_source_server
    import capo_drs.types.start_failback_launch_request
    import capo_drs.types.start_failback_launch_response
    import capo_drs.types.start_failback_request_recovery_instance_i_ds
    import capo_drs.types.start_recovery_request
    import capo_drs.types.start_recovery_request_source_servers
    import capo_drs.types.start_recovery_response
    import capo_drs.types.start_replication_request
    import capo_drs.types.start_replication_response
    import capo_drs.types.start_source_network_recovery_request
    import capo_drs.types.start_source_network_recovery_request_network_entries
    import capo_drs.types.start_source_network_recovery_response
    import capo_drs.types.start_source_network_replication_request
    import capo_drs.types.start_source_network_replication_response
    import capo_drs.types.stop_failback_request
    import capo_drs.types.stop_replication_request
    import capo_drs.types.stop_replication_response
    import capo_drs.types.stop_source_network_replication_request
    import capo_drs.types.stop_source_network_replication_response
    import capo_drs.types.strictly_positive_integer
    import capo_drs.types.subnet_id
    import capo_drs.types.tag_keys
    import capo_drs.types.tag_resource_request
    import capo_drs.types.tags_map
    import capo_drs.types.target_instance_type_right_sizing_method
    import capo_drs.types.terminate_recovery_instances_request
    import capo_drs.types.terminate_recovery_instances_response
    import capo_drs.types.untag_resource_request
    import capo_drs.types.update_failback_replication_configuration_request
    import capo_drs.types.update_launch_configuration_request
    import capo_drs.types.update_launch_configuration_template_request
    import capo_drs.types.update_launch_configuration_template_response
    import capo_drs.types.update_replication_configuration_request
    import capo_drs.types.update_replication_configuration_template_request
    import capo_drs.types.vpc_id


class AsyncdrsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncdrsClient:
    """A client for the ``drs`` service.

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
        self._config = AsyncdrsClientConfig(
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
        self.account_resource = AsyncAccountResource(self)
        self.job_resource = AsyncJobResource(self)
        self.launch_configuration_template_resource = (
            AsyncLaunchConfigurationTemplateResource(self)
        )
        self.recovery_instance_resource = AsyncRecoveryInstanceResource(self)
        self.replication_configuration_template_resource = (
            AsyncReplicationConfigurationTemplateResource(self)
        )
        self.source_network_resource = AsyncSourceNetworkResource(self)
        self.source_server_resource = AsyncSourceServerResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncdrsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncdrsClientConfig = config_overrides or {}
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

    async def create_extended_source_server(
        self,
        source_server_arn: "capo_drs.types.source_server_arn.SourceServerARN",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.create_extended_source_server_response.CreateExtendedSourceServerResponse":
        """<p>Create an extended source server in the target Account based on the source server in staging account.</p>

        Args:
            source_server_arn: <p>This defines the ARN of the source server in staging Account based on which you want to create an extended source server.</p>
            tags: <p>A list of tags associated with the extended source server.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.create_extended_source_server_request.CreateExtendedSourceServerRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.create_extended_source_server_response.CreateExtendedSourceServerResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_extended_source_server

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.create_extended_source_server.async_create_extended_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.create_extended_source_server_request.CreateExtendedSourceServerRequest = {
            "source_server_arn": source_server_arn
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_launch_action(
        self,
        resource_id: "capo_drs.types.launch_action_resource_id.LaunchActionResourceId",
        action_id: "capo_drs.types.launch_action_id.LaunchActionId",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.delete_launch_action_response.DeleteLaunchActionResponse":
        """<p>Deletes a resource launch action.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_launch_action_request.DeleteLaunchActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.delete_launch_action_response.DeleteLaunchActionResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_launch_action

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_launch_action.async_delete_launch_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.delete_launch_action_request.DeleteLaunchActionRequest = {
            "resource_id": resource_id,
            "action_id": action_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def initialize_service(
        self, *, config_overrides: Optional[AsyncdrsClientConfig] = None
    ) -> "capo_drs.types.initialize_service_response.InitializeServiceResponse":
        """<p>Initialize Elastic Disaster Recovery.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.initialize_service_request.InitializeServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.initialize_service_response.InitializeServiceResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.initialize_service

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.initialize_service.async_initialize_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.initialize_service_request.InitializeServiceRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_extensible_source_servers(
        self,
        staging_account_id: "capo_drs.types.account_id.AccountID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[
            "capo_drs.types.max_results_replicating_source_servers.MaxResultsReplicatingSourceServers"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.list_extensible_source_servers_response.ListExtensibleSourceServersResponse":
        """<p>Returns a list of source servers on a staging account that are extensible, which means that: a. The source server is not already extended into this Account. b. The source server on the Account we’re reading from is not an extension of another source server. </p>

        Args:
            staging_account_id: <p>The Id of the staging Account to retrieve extensible source servers from.</p>
            max_results: <p>The maximum number of extensible source servers to retrieve.</p>
            next_token: <p>The token of the next extensible source server to retrieve.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.list_extensible_source_servers_request.ListExtensibleSourceServersRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.list_extensible_source_servers_response.ListExtensibleSourceServersResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.list_extensible_source_servers

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.list_extensible_source_servers.async_list_extensible_source_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.list_extensible_source_servers_request.ListExtensibleSourceServersRequest = {
            "staging_account_id": staging_account_id
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

    async def iter_list_extensible_source_servers(
        self,
        staging_account_id: "capo_drs.types.account_id.AccountID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[
            "capo_drs.types.max_results_replicating_source_servers.MaxResultsReplicatingSourceServers"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_drs.types.staging_source_server.StagingSourceServer]":
        _token = next_token
        while True:
            _response = await self.list_extensible_source_servers(
                staging_account_id,
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

    async def list_launch_actions(
        self,
        resource_id: "capo_drs.types.launch_action_resource_id.LaunchActionResourceId",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.launch_actions_request_filters.LaunchActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_drs.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.list_launch_actions_response.ListLaunchActionsResponse":
        """<p>Lists resource launch actions.</p>

        Args:
            filters: <p>Filters to apply when listing resource launch actions.</p>
            max_results: <p>Maximum amount of items to return when listing resource launch actions.</p>
            next_token: <p>Next token to use when listing resource launch actions.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.list_launch_actions_request.ListLaunchActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.list_launch_actions_response.ListLaunchActionsResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.list_launch_actions

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.list_launch_actions.async_list_launch_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.list_launch_actions_request.ListLaunchActionsRequest = {
            "resource_id": resource_id
        }
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

    async def iter_list_launch_actions(
        self,
        resource_id: "capo_drs.types.launch_action_resource_id.LaunchActionResourceId",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.launch_actions_request_filters.LaunchActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_drs.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_drs.types.launch_action.LaunchAction]":
        _token = next_token
        while True:
            _response = await self.list_launch_actions(
                resource_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_staging_accounts(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.list_staging_accounts_response.ListStagingAccountsResponse":
        """<p>Returns an array of staging accounts for existing extended source servers.</p>

        Args:
            max_results: <p>The maximum number of staging Accounts to retrieve.</p>
            next_token: <p>The token of the next staging Account to retrieve.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.list_staging_accounts_request.ListStagingAccountsRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.list_staging_accounts_response.ListStagingAccountsResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.list_staging_accounts

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.list_staging_accounts.async_list_staging_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.list_staging_accounts_request.ListStagingAccountsRequest = {}
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

    async def iter_list_staging_accounts(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_drs.types.account.Account]":
        _token = next_token
        while True:
            _response = await self.list_staging_accounts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_drs.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all tags for your Elastic Disaster Recovery resources.</p>

        Args:
            resource_arn: <p>The ARN of the resource whose tags should be returned.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_launch_action(
        self,
        resource_id: "capo_drs.types.launch_action_resource_id.LaunchActionResourceId",
        action_code: "capo_drs.types.ssm_document_name.SsmDocumentName",
        order: "capo_drs.types.launch_action_order.LaunchActionOrder",
        action_id: "capo_drs.types.launch_action_id.LaunchActionId",
        optional: bool,
        active: bool,
        name: "capo_drs.types.launch_action_name.LaunchActionName",
        action_version: "capo_drs.types.launch_action_version.LaunchActionVersion",
        category: "capo_drs.types.launch_action_category.LaunchActionCategory",
        description: "capo_drs.types.launch_action_description.LaunchActionDescription",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        parameters: Optional[
            "capo_drs.types.launch_action_parameters.LaunchActionParameters"
        ] = None,
    ) -> "capo_drs.types.put_launch_action_response.PutLaunchActionResponse":
        """<p>Puts a resource launch action.</p>

        Args:
            action_code: <p>Launch action code.</p>
            optional: <p>Whether the launch will not be marked as failed if this action fails.</p>
            active: <p>Whether the launch action is active.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.put_launch_action_request.PutLaunchActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.put_launch_action_response.PutLaunchActionResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.put_launch_action

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.put_launch_action.async_put_launch_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.put_launch_action_request.PutLaunchActionRequest = {
            "resource_id": resource_id,
            "action_code": action_code,
            "order": order,
            "action_id": action_id,
            "optional": optional,
            "active": active,
            "name": name,
            "action_version": action_version,
            "category": category,
            "description": description,
        }
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_drs.types.arn.ARN",
        tags: "capo_drs.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> None:
        """<p>Adds or overwrites only the specified tags for the specified Elastic Disaster Recovery resource or resources. When you specify an existing tag key, the value is overwritten with the new value. Each resource can have a maximum of 50 tags. Each tag consists of a key and optional value.</p>

        Args:
            resource_arn: <p>ARN of the resource for which tags are to be added or updated.</p>
            tags: <p>Array of tags to be added or updated.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_drs.types.arn.ARN",
        tag_keys: "capo_drs.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified set of tags from the specified set of Elastic Disaster Recovery resources.</p>

        Args:
            resource_arn: <p>ARN of the resource for which tags are to be removed.</p>
            tag_keys: <p>Array of tags to be removed.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.untag_resource_request.UntagResourceRequest = {
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

    async def delete_job(
        self,
        job_id: "capo_drs.types.job_id.JobID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes a single Job by ID.</p>

        Args:
            job_id: <p>The ID of the Job to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_job_request.DeleteJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.delete_job_response.DeleteJobResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_job

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_job.async_delete_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.delete_job_request.DeleteJobRequest = {"job_id": job_id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_jobs(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_jobs_response.DescribeJobsResponse":
        """<p>Returns a list of Jobs. Use the JobsID and fromDate and toDate filters to limit which jobs are returned. The response is sorted by creationDataTime - latest date first. Jobs are created by the StartRecovery, TerminateRecoveryInstances and StartFailbackLaunch APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to *Support* and only used in response to relevant support tickets.</p>

        Args:
            filters: <p>A set of filters by which to return Jobs.</p>
            max_results: <p>Maximum number of Jobs to retrieve.</p>
            next_token: <p>The token of the next Job to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_jobs_request.DescribeJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_jobs_response.DescribeJobsResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_jobs

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_jobs.async_describe_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.describe_jobs_request.DescribeJobsRequest = {}
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

    async def iter_describe_jobs(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_drs.types.job.Job]":
        _token = next_token
        while True:
            _response = await self.describe_jobs(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_job_log_items(
        self,
        job_id: "capo_drs.types.job_id.JobID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_job_log_items_response.DescribeJobLogItemsResponse":
        """<p>Retrieves a detailed Job log with pagination.</p>

        Args:
            job_id: <p>The ID of the Job for which Job log items will be retrieved.</p>
            max_results: <p>Maximum number of Job log items to retrieve.</p>
            next_token: <p>The token of the next Job log items to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_job_log_items_request.DescribeJobLogItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_job_log_items

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_job_log_items.async_describe_job_log_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.describe_job_log_items_request.DescribeJobLogItemsRequest = {
            "job_id": job_id
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

    async def iter_describe_job_log_items(
        self,
        job_id: "capo_drs.types.job_id.JobID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_drs.types.job_log.JobLog]":
        _token = next_token
        while True:
            _response = await self.describe_job_log_items(
                job_id,
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

    async def create_launch_configuration_template(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        launch_disposition: Optional[
            "capo_drs.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_drs.types.licensing.Licensing"] = None,
        export_bucket_arn: Optional["capo_drs.types.arn.ARN"] = None,
        post_launch_enabled: Optional[bool] = None,
        launch_into_source_instance: Optional[bool] = None,
    ) -> "capo_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse":
        """<p>Creates a new Launch Configuration Template.</p>

        Args:
            tags: <p>Request to associate tags during creation of a Launch Configuration Template.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private IP.</p>
            copy_tags: <p>Copy tags.</p>
            licensing: <p>Licensing.</p>
            export_bucket_arn: <p>S3 bucket ARN to export Source Network templates.</p>
            post_launch_enabled: <p>Whether we want to activate post-launch actions.</p>
            launch_into_source_instance: <p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_launch_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.create_launch_configuration_template.async_create_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest = {}
        if tags is not None:
            input_["tags"] = tags
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if export_bucket_arn is not None:
            input_["export_bucket_arn"] = export_bucket_arn
        if post_launch_enabled is not None:
            input_["post_launch_enabled"] = post_launch_enabled
        if launch_into_source_instance is not None:
            input_["launch_into_source_instance"] = launch_into_source_instance

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_launch_configuration_template(
        self,
        launch_configuration_template_id: "capo_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        launch_disposition: Optional[
            "capo_drs.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_drs.types.licensing.Licensing"] = None,
        export_bucket_arn: Optional["capo_drs.types.arn.ARN"] = None,
        post_launch_enabled: Optional[bool] = None,
        launch_into_source_instance: Optional[bool] = None,
    ) -> "capo_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse":
        """<p>Updates an existing Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>Launch Configuration Template ID.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private IP.</p>
            copy_tags: <p>Copy tags.</p>
            licensing: <p>Licensing.</p>
            export_bucket_arn: <p>S3 bucket ARN to export Source Network templates.</p>
            post_launch_enabled: <p>Whether we want to activate post-launch actions.</p>
            launch_into_source_instance: <p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration_template.async_update_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
        }
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if export_bucket_arn is not None:
            input_["export_bucket_arn"] = export_bucket_arn
        if post_launch_enabled is not None:
            input_["post_launch_enabled"] = post_launch_enabled
        if launch_into_source_instance is not None:
            input_["launch_into_source_instance"] = launch_into_source_instance

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_launch_configuration_template(
        self,
        launch_configuration_template_id: "capo_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse":
        """<p>Deletes a single Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>The ID of the Launch Configuration Template to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_launch_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_launch_configuration_template.async_delete_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_launch_configuration_templates(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        launch_configuration_template_i_ds: Optional[
            "capo_drs.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_drs.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse":
        """<p>Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs</p>

        Args:
            launch_configuration_template_i_ds: <p>Request to filter Launch Configuration Templates list by Launch Configuration Template ID.</p>
            max_results: <p>Maximum results to be returned in DescribeLaunchConfigurationTemplates.</p>
            next_token: <p>The token of the next Launch Configuration Template to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_launch_configuration_templates

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_launch_configuration_templates.async_describe_launch_configuration_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest = {}
        if launch_configuration_template_i_ds is not None:
            input_["launch_configuration_template_i_ds"] = (
                launch_configuration_template_i_ds
            )
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

    async def iter_describe_launch_configuration_templates(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        launch_configuration_template_i_ds: Optional[
            "capo_drs.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_drs.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_drs.types.launch_configuration_template.LaunchConfigurationTemplate]":
        _token = next_token
        while True:
            _response = await self.describe_launch_configuration_templates(
                config_overrides=config_overrides,
                launch_configuration_template_i_ds=launch_configuration_template_i_ds,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_recovery_instances(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_recovery_instances_request_filters.DescribeRecoveryInstancesRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_recovery_instances_response.DescribeRecoveryInstancesResponse":
        """<p>Lists all Recovery Instances or multiple Recovery Instances by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Recovery Instances.</p>
            max_results: <p>Maximum number of Recovery Instances to retrieve.</p>
            next_token: <p>The token of the next Recovery Instance to retrieve.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_recovery_instances_request.DescribeRecoveryInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_recovery_instances_response.DescribeRecoveryInstancesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_instances

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_instances.async_describe_recovery_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.describe_recovery_instances_request.DescribeRecoveryInstancesRequest = {}
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

    async def iter_describe_recovery_instances(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_recovery_instances_request_filters.DescribeRecoveryInstancesRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_drs.types.recovery_instance.RecoveryInstance]":
        _token = next_token
        while True:
            _response = await self.describe_recovery_instances(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def delete_recovery_instance(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> None:
        """<p>Deletes a single Recovery Instance by ID. This deletes the Recovery Instance resource from Elastic Disaster Recovery. The Recovery Instance must be disconnected first in order to delete it.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance to be deleted.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_recovery_instance_request.DeleteRecoveryInstanceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_recovery_instance

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_recovery_instance.async_delete_recovery_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.delete_recovery_instance_request.DeleteRecoveryInstanceRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disconnect_recovery_instance(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> None:
        """<p>Disconnect a Recovery Instance from Elastic Disaster Recovery. Data replication is stopped immediately. All AWS resources created by Elastic Disaster Recovery for enabling the replication of the Recovery Instance will be terminated / deleted within 90 minutes. If the agent on the Recovery Instance has not been prevented from communicating with the Elastic Disaster Recovery service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the Recovery Instance will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance to disconnect.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.disconnect_recovery_instance_request.DisconnectRecoveryInstanceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.disconnect_recovery_instance

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.disconnect_recovery_instance.async_disconnect_recovery_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.disconnect_recovery_instance_request.DisconnectRecoveryInstanceRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_failback_replication_configuration(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.get_failback_replication_configuration_response.GetFailbackReplicationConfigurationResponse":
        """<p>Lists all Failback ReplicationConfigurations, filtered by Recovery Instance ID.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance whose failback replication configuration should be returned.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.get_failback_replication_configuration_request.GetFailbackReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.get_failback_replication_configuration_response.GetFailbackReplicationConfigurationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.get_failback_replication_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.get_failback_replication_configuration.async_get_failback_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.get_failback_replication_configuration_request.GetFailbackReplicationConfigurationRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reverse_replication(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.reverse_replication_response.ReverseReplicationResponse":
        """<p>Start replication to origin / target region - applies only to protected instances that originated in EC2. For recovery instances on target region - starts replication back to origin region. For failback instances on origin region - starts replication to target region to re-protect them. </p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance that we want to reverse the replication for.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.reverse_replication_request.ReverseReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.reverse_replication_response.ReverseReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.reverse_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.reverse_replication.async_reverse_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.reverse_replication_request.ReverseReplicationRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_failback(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> None:
        """<p>Stops the failback process for a specified Recovery Instance. This changes the Failback State of the Recovery Instance back to FAILBACK_NOT_STARTED.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance we want to stop failback for.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.stop_failback_request.StopFailbackRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.stop_failback

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.stop_failback.async_stop_failback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.stop_failback_request.StopFailbackRequest = {
            "recovery_instance_id": recovery_instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_failback_replication_configuration(
        self,
        recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        name: Optional["capo_drs.types.bounded_string.BoundedString"] = None,
        bandwidth_throttling: Optional[
            "capo_drs.types.positive_integer.PositiveInteger"
        ] = None,
        use_private_ip: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> None:
        """<p>Allows you to update the failback replication configuration of a Recovery Instance by ID.</p>

        Args:
            recovery_instance_id: <p>The ID of the Recovery Instance.</p>
            name: <p>The name of the Failback Replication Configuration.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Recovery Instance in Mbps.</p>
            use_private_ip: <p>Whether to use Private IP for the failback replication of the Recovery Instance.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.update_failback_replication_configuration_request.UpdateFailbackReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_failback_replication_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.update_failback_replication_configuration.async_update_failback_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.update_failback_replication_configuration_request.UpdateFailbackReplicationConfigurationRequest = {
            "recovery_instance_id": recovery_instance_id
        }
        if name is not None:
            input_["name"] = name
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if use_private_ip is not None:
            input_["use_private_ip"] = use_private_ip
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_failback_launch(
        self,
        recovery_instance_i_ds: "capo_drs.types.start_failback_request_recovery_instance_i_ds.StartFailbackRequestRecoveryInstanceIDs",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.start_failback_launch_response.StartFailbackLaunchResponse":
        """<p>Initiates a Job for launching the machine that is being failed back to from the specified Recovery Instance. This will run conversion on the failback client and will reboot your machine, thus completing the failback process.</p>

        Args:
            recovery_instance_i_ds: <p>The IDs of the Recovery Instance whose failback launch we want to request.</p>
            tags: <p>The tags to be associated with the failback launch Job.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.start_failback_launch_request.StartFailbackLaunchRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.start_failback_launch_response.StartFailbackLaunchResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_failback_launch

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.start_failback_launch.async_start_failback_launch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.start_failback_launch_request.StartFailbackLaunchRequest = {
            "recovery_instance_i_ds": recovery_instance_i_ds
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def terminate_recovery_instances(
        self,
        recovery_instance_i_ds: "capo_drs.types.recovery_instances_for_termination_request.RecoveryInstancesForTerminationRequest",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.terminate_recovery_instances_response.TerminateRecoveryInstancesResponse":
        """<p>Initiates a Job for terminating the EC2 resources associated with the specified Recovery Instances, and then will delete the Recovery Instances from the Elastic Disaster Recovery service.</p>

        Args:
            recovery_instance_i_ds: <p>The IDs of the Recovery Instances that should be terminated.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.terminate_recovery_instances_request.TerminateRecoveryInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.terminate_recovery_instances_response.TerminateRecoveryInstancesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.terminate_recovery_instances

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.terminate_recovery_instances.async_terminate_recovery_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.terminate_recovery_instances_request.TerminateRecoveryInstancesRequest = {
            "recovery_instance_i_ds": recovery_instance_i_ds
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_replication_configuration_template(
        self,
        staging_area_subnet_id: "capo_drs.types.subnet_id.SubnetID",
        replication_servers_security_groups_i_ds: "capo_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs",
        ebs_encryption: "capo_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption",
        bandwidth_throttling: "capo_drs.types.positive_integer.PositiveInteger",
        staging_area_tags: "capo_drs.types.tags_map.TagsMap",
        pit_policy: "capo_drs.types.pit_policy.PITPolicy",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_server_instance_type: Optional[
            "capo_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_drs.types.arn.ARN"] = None,
        data_plane_routing: Optional[
            "capo_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Creates a new ReplicationConfigurationTemplate.</p>

        Args:
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            tags: <p>A set of tags to be associated with the Replication Configuration Template resource.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_replication_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.create_replication_configuration_template.async_create_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest = {
            "staging_area_subnet_id": staging_area_subnet_id,
            "replication_servers_security_groups_i_ds": replication_servers_security_groups_i_ds,
            "ebs_encryption": ebs_encryption,
            "bandwidth_throttling": bandwidth_throttling,
            "staging_area_tags": staging_area_tags,
            "pit_policy": pit_policy,
        }
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
        if replication_server_instance_type is not None:
            input_["replication_server_instance_type"] = (
                replication_server_instance_type
            )
        if use_dedicated_replication_server is not None:
            input_["use_dedicated_replication_server"] = (
                use_dedicated_replication_server
            )
        if default_large_staging_disk_type is not None:
            input_["default_large_staging_disk_type"] = default_large_staging_disk_type
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if tags is not None:
            input_["tags"] = tags
        if auto_replicate_new_disks is not None:
            input_["auto_replicate_new_disks"] = auto_replicate_new_disks
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_replication_configuration_template(
        self,
        replication_configuration_template_id: "capo_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        arn: Optional["capo_drs.types.arn.ARN"] = None,
        staging_area_subnet_id: Optional["capo_drs.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        ebs_encryption: Optional[
            "capo_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_drs.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_drs.types.positive_integer.PositiveInteger"
        ] = None,
        data_plane_routing: Optional[
            "capo_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        pit_policy: Optional["capo_drs.types.pit_policy.PITPolicy"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Updates a ReplicationConfigurationTemplate by ID.</p>

        Args:
            replication_configuration_template_id: <p>The Replication Configuration Template ID.</p>
            arn: <p>The Replication Configuration Template ARN.</p>
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration_template.async_update_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest = {
            "replication_configuration_template_id": replication_configuration_template_id
        }
        if arn is not None:
            input_["arn"] = arn
        if staging_area_subnet_id is not None:
            input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
        if replication_servers_security_groups_i_ds is not None:
            input_["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input_["replication_server_instance_type"] = (
                replication_server_instance_type
            )
        if use_dedicated_replication_server is not None:
            input_["use_dedicated_replication_server"] = (
                use_dedicated_replication_server
            )
        if default_large_staging_disk_type is not None:
            input_["default_large_staging_disk_type"] = default_large_staging_disk_type
        if ebs_encryption is not None:
            input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input_["staging_area_tags"] = staging_area_tags
        if pit_policy is not None:
            input_["pit_policy"] = pit_policy
        if auto_replicate_new_disks is not None:
            input_["auto_replicate_new_disks"] = auto_replicate_new_disks
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_replication_configuration_template(
        self,
        replication_configuration_template_id: "capo_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse":
        """<p>Deletes a single Replication Configuration Template by ID</p>

        Args:
            replication_configuration_template_id: <p>The ID of the Replication Configuration Template to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_replication_configuration_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_replication_configuration_template.async_delete_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest = {
            "replication_configuration_template_id": replication_configuration_template_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_replication_configuration_templates(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        replication_configuration_template_i_ds: Optional[
            "capo_drs.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse":
        """<p>Lists all ReplicationConfigurationTemplates, filtered by Source Server IDs.</p>

        Args:
            replication_configuration_template_i_ds: <p>The IDs of the Replication Configuration Templates to retrieve. An empty list means all Replication Configuration Templates.</p>
            max_results: <p>Maximum number of Replication Configuration Templates to retrieve.</p>
            next_token: <p>The token of the next Replication Configuration Template to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_replication_configuration_templates

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_replication_configuration_templates.async_describe_replication_configuration_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest = {}
        if replication_configuration_template_i_ds is not None:
            input_["replication_configuration_template_i_ds"] = (
                replication_configuration_template_i_ds
            )
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

    async def iter_describe_replication_configuration_templates(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        replication_configuration_template_i_ds: Optional[
            "capo_drs.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_drs.types.replication_configuration_template.ReplicationConfigurationTemplate]":
        _token = next_token
        while True:
            _response = await self.describe_replication_configuration_templates(
                config_overrides=config_overrides,
                replication_configuration_template_i_ds=replication_configuration_template_i_ds,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_source_network(
        self,
        vpc_id: "capo_drs.types.vpc_id.VpcID",
        origin_account_id: "capo_drs.types.account_id.AccountID",
        origin_region: "capo_drs.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.create_source_network_response.CreateSourceNetworkResponse":
        """<p>Create a new Source Network resource for a provided VPC ID.</p>

        Args:
            vpc_id: <p>Which VPC ID to protect.</p>
            origin_account_id: <p>Account containing the VPC to protect.</p>
            origin_region: <p>Region containing the VPC to protect.</p>
            tags: <p>A set of tags to be associated with the Source Network resource.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.create_source_network_request.CreateSourceNetworkRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.create_source_network_response.CreateSourceNetworkResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.create_source_network

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.create_source_network.async_create_source_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.create_source_network_request.CreateSourceNetworkRequest = {
            "vpc_id": vpc_id,
            "origin_account_id": origin_account_id,
            "origin_region": origin_region,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_source_network(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.delete_source_network_response.DeleteSourceNetworkResponse":
        """<p>Delete Source Network resource.</p>

        Args:
            source_network_id: <p>ID of the Source Network to delete.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_source_network_request.DeleteSourceNetworkRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.delete_source_network_response.DeleteSourceNetworkResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_source_network

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_source_network.async_delete_source_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.delete_source_network_request.DeleteSourceNetworkRequest = {
            "source_network_id": source_network_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_source_networks(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_source_networks_request_filters.DescribeSourceNetworksRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse":
        """<p>Lists all Source Networks or multiple Source Networks filtered by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Source Networks.</p>
            max_results: <p>Maximum number of Source Networks to retrieve.</p>
            next_token: <p>The token of the next Source Networks to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_source_networks_request.DescribeSourceNetworksRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_source_networks

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_source_networks.async_describe_source_networks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.describe_source_networks_request.DescribeSourceNetworksRequest = {}
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

    async def iter_describe_source_networks(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_source_networks_request_filters.DescribeSourceNetworksRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_drs.types.source_network.SourceNetwork]":
        _token = next_token
        while True:
            _response = await self.describe_source_networks(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def associate_source_network_stack(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        cfn_stack_name: "capo_drs.types.cfn_stack_name.CfnStackName",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse":
        """<p>Associate a Source Network to an existing CloudFormation Stack and modify launch templates to use this network. Can be used for reverting to previously deployed CloudFormation stacks.</p>

        Args:
            source_network_id: <p>The Source Network ID to associate with CloudFormation template.</p>
            cfn_stack_name: <p>CloudFormation template to associate with a Source Network.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.associate_source_network_stack

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.associate_source_network_stack.async_associate_source_network_stack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest = {
            "source_network_id": source_network_id,
            "cfn_stack_name": cfn_stack_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_source_network_cfn_template(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.export_source_network_cfn_template_response.ExportSourceNetworkCfnTemplateResponse":
        """<p>Export the Source Network CloudFormation template to an S3 bucket.</p>

        Args:
            source_network_id: <p>The Source Network ID to export its CloudFormation template to an S3 bucket.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.export_source_network_cfn_template_request.ExportSourceNetworkCfnTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.export_source_network_cfn_template_response.ExportSourceNetworkCfnTemplateResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.export_source_network_cfn_template

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.export_source_network_cfn_template.async_export_source_network_cfn_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.export_source_network_cfn_template_request.ExportSourceNetworkCfnTemplateRequest = {
            "source_network_id": source_network_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_source_network_replication(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse":
        """<p>Starts replication for a Source Network. This action would make the Source Network protected.</p>

        Args:
            source_network_id: <p>ID of the Source Network to replicate.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.start_source_network_replication_request.StartSourceNetworkReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_source_network_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.start_source_network_replication.async_start_source_network_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.start_source_network_replication_request.StartSourceNetworkReplicationRequest = {
            "source_network_id": source_network_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_source_network_replication(
        self,
        source_network_id: "capo_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse":
        """<p>Stops replication for a Source Network. This action would make the Source Network unprotected.</p>

        Args:
            source_network_id: <p>ID of the Source Network to stop replication.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.stop_source_network_replication_request.StopSourceNetworkReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.stop_source_network_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.stop_source_network_replication.async_stop_source_network_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.stop_source_network_replication_request.StopSourceNetworkReplicationRequest = {
            "source_network_id": source_network_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_source_network_recovery(
        self,
        source_networks: "capo_drs.types.start_source_network_recovery_request_network_entries.StartSourceNetworkRecoveryRequestNetworkEntries",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        deploy_as_new: Optional[bool] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse":
        """<p>Deploy VPC for the specified Source Network and modify launch templates to use this network. The VPC will be deployed using a dedicated CloudFormation stack.</p>

        Args:
            source_networks: <p>The Source Networks that we want to start a Recovery Job for.</p>
            deploy_as_new: <p>Don't update existing CloudFormation Stack, recover the network using a new stack.</p>
            tags: <p>The tags to be associated with the Source Network recovery Job.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_source_network_recovery

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.start_source_network_recovery.async_start_source_network_recovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest = {
            "source_networks": source_networks
        }
        if deploy_as_new is not None:
            input_["deploy_as_new"] = deploy_as_new
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_source_server(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.delete_source_server_response.DeleteSourceServerResponse":
        """<p>Deletes a single Source Server by ID. The Source Server must be disconnected first.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_source_server_request.DeleteSourceServerRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.delete_source_server_response.DeleteSourceServerResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_source_server

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_source_server.async_delete_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.delete_source_server_request.DeleteSourceServerRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_source_servers(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> (
        "capo_drs.types.describe_source_servers_response.DescribeSourceServersResponse"
    ):
        """<p>Lists all Source Servers or multiple Source Servers filtered by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Source Servers.</p>
            max_results: <p>Maximum number of Source Servers to retrieve.</p>
            next_token: <p>The token of the next Source Server to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_source_servers_request.DescribeSourceServersRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_source_servers_response.DescribeSourceServersResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_source_servers

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_source_servers.async_describe_source_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.describe_source_servers_request.DescribeSourceServersRequest = {}
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

    async def iter_describe_source_servers(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_drs.types.source_server.SourceServer]":
        _token = next_token
        while True:
            _response = await self.describe_source_servers(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_recovery_snapshots(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_recovery_snapshots_request_filters.DescribeRecoverySnapshotsRequestFilters"
        ] = None,
        order: Optional[
            "capo_drs.types.recovery_snapshots_order.RecoverySnapshotsOrder"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_recovery_snapshots_response.DescribeRecoverySnapshotsResponse":
        """<p>Lists all Recovery Snapshots for a single Source Server.</p>

        Args:
            source_server_id: <p>Filter Recovery Snapshots by Source Server ID.</p>
            filters: <p>A set of filters by which to return Recovery Snapshots.</p>
            order: <p>The sorted ordering by which to return Recovery Snapshots.</p>
            max_results: <p>Maximum number of Recovery Snapshots to retrieve.</p>
            next_token: <p>The token of the next Recovery Snapshot to retrieve.</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_recovery_snapshots_request.DescribeRecoverySnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_recovery_snapshots_response.DescribeRecoverySnapshotsResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_snapshots

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_recovery_snapshots.async_describe_recovery_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.describe_recovery_snapshots_request.DescribeRecoverySnapshotsRequest = {
            "source_server_id": source_server_id
        }
        if filters is not None:
            input_["filters"] = filters
        if order is not None:
            input_["order"] = order
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

    async def iter_describe_recovery_snapshots(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_recovery_snapshots_request_filters.DescribeRecoverySnapshotsRequestFilters"
        ] = None,
        order: Optional[
            "capo_drs.types.recovery_snapshots_order.RecoverySnapshotsOrder"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "AsyncIterator[capo_drs.types.recovery_snapshot.RecoverySnapshot]":
        _token = next_token
        while True:
            _response = await self.describe_recovery_snapshots(
                source_server_id,
                config_overrides=config_overrides,
                filters=filters,
                order=order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disconnect_source_server(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.source_server.SourceServer":
        """<p>Disconnects a specific Source Server from Elastic Disaster Recovery. Data replication is stopped immediately. All AWS resources created by Elastic Disaster Recovery for enabling the replication of the Source Server will be terminated / deleted within 90 minutes. You cannot disconnect a Source Server if it has a Recovery Instance. If the agent on the Source Server has not been prevented from communicating with the Elastic Disaster Recovery service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to disconnect.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.disconnect_source_server_request.DisconnectSourceServerRequest]",
        ) -> AsyncOperationResponse["capo_drs.types.source_server.SourceServer"]:
            import capo_drs._operations.elastic_disaster_recovery_service.disconnect_source_server

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.disconnect_source_server.async_disconnect_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.disconnect_source_server_request.DisconnectSourceServerRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_launch_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.launch_configuration.LaunchConfiguration":
        """<p>Gets a LaunchConfiguration, filtered by Source Server IDs.</p>

        Args:
            source_server_id: <p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.get_launch_configuration_request.GetLaunchConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.get_launch_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.get_launch_configuration.async_get_launch_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.get_launch_configuration_request.GetLaunchConfigurationRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_replication_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.replication_configuration.ReplicationConfiguration":
        """<p>Gets a ReplicationConfiguration, filtered by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Serve for this Replication Configuration.r</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.get_replication_configuration_request.GetReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.get_replication_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.get_replication_configuration.async_get_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.get_replication_configuration_request.GetReplicationConfigurationRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retry_data_replication(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.source_server.SourceServer":
        """<p>WARNING: RetryDataReplication is deprecated. Causes the data replication initiation sequence to begin immediately upon next Handshake for the specified Source Server ID, regardless of when the previous initiation started. This command will work only if the Source Server is stalled or is in a DISCONNECTED or STOPPED state. </p>

        Args:
            source_server_id: <p>The ID of the Source Server whose data replication should be retried.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.retry_data_replication_request.RetryDataReplicationRequest]",
        ) -> AsyncOperationResponse["capo_drs.types.source_server.SourceServer"]:
            import capo_drs._operations.elastic_disaster_recovery_service.retry_data_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.retry_data_replication.async_retry_data_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.retry_data_replication_request.RetryDataReplicationRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_replication(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.start_replication_response.StartReplicationResponse":
        """<p>Starts replication for a stopped Source Server. This action would make the Source Server protected again and restart billing for it.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to start replication for.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.start_replication_request.StartReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.start_replication_response.StartReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.start_replication.async_start_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.start_replication_request.StartReplicationRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_replication(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.stop_replication_response.StopReplicationResponse":
        """<p>Stops replication for a Source Server. This action would make the Source Server unprotected, delete its existing snapshots and stop billing for it.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to stop replication for.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.stop_replication_request.StopReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.stop_replication_response.StopReplicationResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.stop_replication

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.stop_replication.async_stop_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.stop_replication_request.StopReplicationRequest = {
            "source_server_id": source_server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_launch_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        name: Optional["capo_drs.types.small_bounded_string.SmallBoundedString"] = None,
        launch_disposition: Optional[
            "capo_drs.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_drs.types.licensing.Licensing"] = None,
        post_launch_enabled: Optional[bool] = None,
        launch_into_instance_properties: Optional[
            "capo_drs.types.launch_into_instance_properties.LaunchIntoInstanceProperties"
        ] = None,
    ) -> "capo_drs.types.launch_configuration.LaunchConfiguration":
        """<p>Updates a LaunchConfiguration by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>
            name: <p>The name of the launch configuration.</p>
            launch_disposition: <p>The state of the Recovery Instance in EC2 after the recovery operation.</p>
            target_instance_type_right_sizing_method: <p>Whether Elastic Disaster Recovery should try to automatically choose the instance type that best matches the OS, CPU, and RAM of your Source Server.</p>
            copy_private_ip: <p>Whether we should copy the Private IP of the Source Server to the Recovery Instance.</p>
            copy_tags: <p>Whether we want to copy the tags of the Source Server to the EC2 machine of the Recovery Instance.</p>
            licensing: <p>The licensing configuration to be used for this launch configuration.</p>
            post_launch_enabled: <p>Whether we want to enable post-launch actions for the Source Server.</p>
            launch_into_instance_properties: <p>Launch into existing instance properties.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.update_launch_configuration.async_update_launch_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if name is not None:
            input_["name"] = name
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if post_launch_enabled is not None:
            input_["post_launch_enabled"] = post_launch_enabled
        if launch_into_instance_properties is not None:
            input_["launch_into_instance_properties"] = launch_into_instance_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_replication_configuration(
        self,
        source_server_id: "capo_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        name: Optional["capo_drs.types.small_bounded_string.SmallBoundedString"] = None,
        staging_area_subnet_id: Optional["capo_drs.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        replicated_disks: Optional[
            "capo_drs.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
        ] = None,
        ebs_encryption: Optional[
            "capo_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_drs.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_drs.types.positive_integer.PositiveInteger"
        ] = None,
        data_plane_routing: Optional[
            "capo_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
        pit_policy: Optional["capo_drs.types.pit_policy.PITPolicy"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "capo_drs.types.replication_configuration.ReplicationConfiguration":
        """<p>Allows you to update a ReplicationConfiguration by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Server for this Replication Configuration.</p>
            name: <p>The name of the Replication Configuration.</p>
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            replicated_disks: <p>The configuration of the disks of the Source Server to be replicated.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>

        Raises:
            capo_drs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.update_replication_configuration.async_update_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if name is not None:
            input_["name"] = name
        if staging_area_subnet_id is not None:
            input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
        if replication_servers_security_groups_i_ds is not None:
            input_["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input_["replication_server_instance_type"] = (
                replication_server_instance_type
            )
        if use_dedicated_replication_server is not None:
            input_["use_dedicated_replication_server"] = (
                use_dedicated_replication_server
            )
        if default_large_staging_disk_type is not None:
            input_["default_large_staging_disk_type"] = default_large_staging_disk_type
        if replicated_disks is not None:
            input_["replicated_disks"] = replicated_disks
        if ebs_encryption is not None:
            input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input_["staging_area_tags"] = staging_area_tags
        if pit_policy is not None:
            input_["pit_policy"] = pit_policy
        if auto_replicate_new_disks is not None:
            input_["auto_replicate_new_disks"] = auto_replicate_new_disks
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_recovery(
        self,
        source_servers: "capo_drs.types.start_recovery_request_source_servers.StartRecoveryRequestSourceServers",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        is_drill: Optional[bool] = None,
        tags: Optional["capo_drs.types.tags_map.TagsMap"] = None,
    ) -> "capo_drs.types.start_recovery_response.StartRecoveryResponse":
        """<p>Launches Recovery Instances for the specified Source Servers. For each Source Server you may choose a point in time snapshot to launch from, or use an on demand snapshot.</p>

        Args:
            source_servers: <p>The Source Servers that we want to start a Recovery Job for.</p>
            is_drill: <p>Whether this Source Server Recovery operation is a drill or not.</p>
            tags: <p>The tags to be associated with the Recovery Job.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.start_recovery_request.StartRecoveryRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.start_recovery_response.StartRecoveryResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.start_recovery

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.start_recovery.async_start_recovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_drs.types.start_recovery_request.StartRecoveryRequest = {
            "source_servers": source_servers
        }
        if is_drill is not None:
            input_["is_drill"] = is_drill
        if tags is not None:
            input_["tags"] = tags

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
