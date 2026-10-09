"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#AWSElasticBeanstalkService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_elastic_beanstalk._auth._signers
import capo_elastic_beanstalk._auth._sigv4
from capo_elastic_beanstalk._auth._identity import Credentials
from capo_elastic_beanstalk._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_elastic_beanstalk._auth._zapros_handler import AuthMiddleware
from capo_elastic_beanstalk._pagination import resolve_path as _resolve_path
from capo_elastic_beanstalk._services._aws_config import aaws_config
from capo_elastic_beanstalk._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.abort_environment_update_message
    import capo_elastic_beanstalk.types.action_status
    import capo_elastic_beanstalk.types.application_description_message
    import capo_elastic_beanstalk.types.application_descriptions_message
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.application_names_list
    import capo_elastic_beanstalk.types.application_resource_lifecycle_config
    import capo_elastic_beanstalk.types.application_resource_lifecycle_description_message
    import capo_elastic_beanstalk.types.application_version_description_message
    import capo_elastic_beanstalk.types.application_version_descriptions_message
    import capo_elastic_beanstalk.types.application_version_proccess
    import capo_elastic_beanstalk.types.apply_environment_managed_action_request
    import capo_elastic_beanstalk.types.apply_environment_managed_action_result
    import capo_elastic_beanstalk.types.associate_environment_operations_role_message
    import capo_elastic_beanstalk.types.auto_create_application
    import capo_elastic_beanstalk.types.build_configuration
    import capo_elastic_beanstalk.types.check_dns_availability_message
    import capo_elastic_beanstalk.types.check_dns_availability_result_message
    import capo_elastic_beanstalk.types.compose_environments_message
    import capo_elastic_beanstalk.types.configuration_option_settings_list
    import capo_elastic_beanstalk.types.configuration_options_description
    import capo_elastic_beanstalk.types.configuration_settings_description
    import capo_elastic_beanstalk.types.configuration_settings_descriptions
    import capo_elastic_beanstalk.types.configuration_settings_validation_messages
    import capo_elastic_beanstalk.types.configuration_template_name
    import capo_elastic_beanstalk.types.create_application_message
    import capo_elastic_beanstalk.types.create_application_version_message
    import capo_elastic_beanstalk.types.create_configuration_template_message
    import capo_elastic_beanstalk.types.create_environment_message
    import capo_elastic_beanstalk.types.create_platform_version_request
    import capo_elastic_beanstalk.types.create_platform_version_result
    import capo_elastic_beanstalk.types.create_storage_location_result_message
    import capo_elastic_beanstalk.types.delete_application_message
    import capo_elastic_beanstalk.types.delete_application_version_message
    import capo_elastic_beanstalk.types.delete_configuration_template_message
    import capo_elastic_beanstalk.types.delete_environment_configuration_message
    import capo_elastic_beanstalk.types.delete_platform_version_request
    import capo_elastic_beanstalk.types.delete_platform_version_result
    import capo_elastic_beanstalk.types.delete_source_bundle
    import capo_elastic_beanstalk.types.describe_account_attributes_result
    import capo_elastic_beanstalk.types.describe_application_versions_message
    import capo_elastic_beanstalk.types.describe_applications_message
    import capo_elastic_beanstalk.types.describe_configuration_options_message
    import capo_elastic_beanstalk.types.describe_configuration_settings_message
    import capo_elastic_beanstalk.types.describe_environment_health_request
    import capo_elastic_beanstalk.types.describe_environment_health_result
    import capo_elastic_beanstalk.types.describe_environment_managed_action_history_request
    import capo_elastic_beanstalk.types.describe_environment_managed_action_history_result
    import capo_elastic_beanstalk.types.describe_environment_managed_actions_request
    import capo_elastic_beanstalk.types.describe_environment_managed_actions_result
    import capo_elastic_beanstalk.types.describe_environment_resources_message
    import capo_elastic_beanstalk.types.describe_environments_message
    import capo_elastic_beanstalk.types.describe_events_message
    import capo_elastic_beanstalk.types.describe_instances_health_request
    import capo_elastic_beanstalk.types.describe_instances_health_result
    import capo_elastic_beanstalk.types.describe_platform_version_request
    import capo_elastic_beanstalk.types.describe_platform_version_result
    import capo_elastic_beanstalk.types.description
    import capo_elastic_beanstalk.types.disassociate_environment_operations_role_message
    import capo_elastic_beanstalk.types.dns_cname_prefix
    import capo_elastic_beanstalk.types.environment_description
    import capo_elastic_beanstalk.types.environment_descriptions_message
    import capo_elastic_beanstalk.types.environment_health_attributes
    import capo_elastic_beanstalk.types.environment_id
    import capo_elastic_beanstalk.types.environment_id_list
    import capo_elastic_beanstalk.types.environment_info_type
    import capo_elastic_beanstalk.types.environment_name
    import capo_elastic_beanstalk.types.environment_names_list
    import capo_elastic_beanstalk.types.environment_resource_descriptions_message
    import capo_elastic_beanstalk.types.environment_tier
    import capo_elastic_beanstalk.types.event_description
    import capo_elastic_beanstalk.types.event_descriptions_message
    import capo_elastic_beanstalk.types.event_severity
    import capo_elastic_beanstalk.types.force_terminate
    import capo_elastic_beanstalk.types.group_name
    import capo_elastic_beanstalk.types.image_configuration
    import capo_elastic_beanstalk.types.include_deleted
    import capo_elastic_beanstalk.types.include_deleted_back_to
    import capo_elastic_beanstalk.types.instances_health_attributes
    import capo_elastic_beanstalk.types.list_available_solution_stacks_result_message
    import capo_elastic_beanstalk.types.list_platform_branches_request
    import capo_elastic_beanstalk.types.list_platform_branches_result
    import capo_elastic_beanstalk.types.list_platform_versions_request
    import capo_elastic_beanstalk.types.list_platform_versions_result
    import capo_elastic_beanstalk.types.list_tags_for_resource_message
    import capo_elastic_beanstalk.types.managed_action_history_item
    import capo_elastic_beanstalk.types.managed_action_history_max_items
    import capo_elastic_beanstalk.types.max_records
    import capo_elastic_beanstalk.types.next_token
    import capo_elastic_beanstalk.types.operations_role
    import capo_elastic_beanstalk.types.options_specifier_list
    import capo_elastic_beanstalk.types.platform_arn
    import capo_elastic_beanstalk.types.platform_branch_max_records
    import capo_elastic_beanstalk.types.platform_filters
    import capo_elastic_beanstalk.types.platform_max_records
    import capo_elastic_beanstalk.types.platform_name
    import capo_elastic_beanstalk.types.platform_summary
    import capo_elastic_beanstalk.types.platform_version
    import capo_elastic_beanstalk.types.rebuild_environment_message
    import capo_elastic_beanstalk.types.request_environment_info_message
    import capo_elastic_beanstalk.types.request_id
    import capo_elastic_beanstalk.types.resource_arn
    import capo_elastic_beanstalk.types.resource_tags_description_message
    import capo_elastic_beanstalk.types.restart_app_server_message
    import capo_elastic_beanstalk.types.retrieve_environment_info_message
    import capo_elastic_beanstalk.types.retrieve_environment_info_result_message
    import capo_elastic_beanstalk.types.s3_location
    import capo_elastic_beanstalk.types.search_filters
    import capo_elastic_beanstalk.types.solution_stack_name
    import capo_elastic_beanstalk.types.source_build_information
    import capo_elastic_beanstalk.types.source_configuration
    import capo_elastic_beanstalk.types.string
    import capo_elastic_beanstalk.types.swap_environment_cnam_es_message
    import capo_elastic_beanstalk.types.tag_key_list
    import capo_elastic_beanstalk.types.tag_list
    import capo_elastic_beanstalk.types.tags
    import capo_elastic_beanstalk.types.terminate_env_force
    import capo_elastic_beanstalk.types.terminate_environment_message
    import capo_elastic_beanstalk.types.terminate_environment_resources
    import capo_elastic_beanstalk.types.time_filter_end
    import capo_elastic_beanstalk.types.time_filter_start
    import capo_elastic_beanstalk.types.token
    import capo_elastic_beanstalk.types.update_application_message
    import capo_elastic_beanstalk.types.update_application_resource_lifecycle_message
    import capo_elastic_beanstalk.types.update_application_version_message
    import capo_elastic_beanstalk.types.update_configuration_template_message
    import capo_elastic_beanstalk.types.update_environment_message
    import capo_elastic_beanstalk.types.update_tags_for_resource_message
    import capo_elastic_beanstalk.types.validate_configuration_settings_message
    import capo_elastic_beanstalk.types.version_label
    import capo_elastic_beanstalk.types.version_labels
    import capo_elastic_beanstalk.types.version_labels_list


class AsyncElasticBeanstalkClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncElasticBeanstalkClient:
    """A client for the ``ElasticBeanstalk`` service.

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
        self._config = AsyncElasticBeanstalkClientConfig(
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
        self, config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncElasticBeanstalkClientConfig = config_overrides or {}
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

    async def abort_environment_update(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
    ) -> None:
        """<p>Cancels in-progress environment configuration update or application version deployment.</p>

        Args:
            environment_id: <p>This specifies the ID of the environment with the in-progress update that you want to cancel.</p>
            environment_name: <p>This specifies the name of the environment with the in-progress update that you want to cancel.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To abort a deployment
            The following code aborts a running application version deployment for an environment named my-env:

            >>> await client.abort_environment_update(environment_name='my-env')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.abort_environment_update_message.AbortEnvironmentUpdateMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.abort_environment_update

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.abort_environment_update.async_abort_environment_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.abort_environment_update_message.AbortEnvironmentUpdateMessage = {}
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if environment_name is not None:
            input_["environment_name"] = environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def apply_environment_managed_action(
        self,
        action_id: "capo_elastic_beanstalk.types.string.String",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_name: Optional["capo_elastic_beanstalk.types.string.String"] = None,
        environment_id: Optional["capo_elastic_beanstalk.types.string.String"] = None,
    ) -> "capo_elastic_beanstalk.types.apply_environment_managed_action_result.ApplyEnvironmentManagedActionResult":
        """<p>Applies a scheduled managed action immediately. A managed action can be applied only if its status is <code>Scheduled</code>. Get the status and action ID of a managed action with <a>DescribeEnvironmentManagedActions</a>.</p>

        Args:
            environment_name: <p>The name of the target environment.</p>
            environment_id: <p>The environment ID of the target environment.</p>
            action_id: <p>The action ID of the scheduled managed action to execute.</p>

        Raises:
            capo_elastic_beanstalk.errors.elastic_beanstalk_service_exception.ElasticBeanstalkServiceException: <p>A generic service exception has occurred.</p>
            capo_elastic_beanstalk.errors.managed_action_invalid_state_exception.ManagedActionInvalidStateException: <p>Cannot modify the managed action in its current state.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.apply_environment_managed_action_request.ApplyEnvironmentManagedActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.apply_environment_managed_action_result.ApplyEnvironmentManagedActionResult"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.apply_environment_managed_action

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.apply_environment_managed_action.async_apply_environment_managed_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.apply_environment_managed_action_request.ApplyEnvironmentManagedActionRequest = {
            "action_id": action_id
        }
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if environment_id is not None:
            input_["environment_id"] = environment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_environment_operations_role(
        self,
        environment_name: "capo_elastic_beanstalk.types.environment_name.EnvironmentName",
        operations_role: "capo_elastic_beanstalk.types.operations_role.OperationsRole",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
    ) -> None:
        """<important> <p>The operations role feature of Elastic Beanstalk is in beta release and is subject to change.</p> </important> <p>Add or change the operations role used by an environment. After this call is made, Elastic Beanstalk uses the associated operations role for permissions to downstream services during subsequent calls acting on this environment.</p>

        Args:
            environment_name: <p>The name of the environment to which to set the operations role.</p>
            operations_role: <p>The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.associate_environment_operations_role_message.AssociateEnvironmentOperationsRoleMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.associate_environment_operations_role

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.associate_environment_operations_role.async_associate_environment_operations_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.associate_environment_operations_role_message.AssociateEnvironmentOperationsRoleMessage = {
            "environment_name": environment_name,
            "operations_role": operations_role,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def check_dns_availability(
        self,
        cname_prefix: "capo_elastic_beanstalk.types.dns_cname_prefix.DNSCnamePrefix",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
    ) -> "capo_elastic_beanstalk.types.check_dns_availability_result_message.CheckDNSAvailabilityResultMessage":
        """<p>Checks if the specified CNAME is available.</p>

        Args:
            cname_prefix: <p>The prefix used when this CNAME is reserved.</p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To check the availability of a CNAME
            The following operation checks the availability of the subdomain my-cname:

            >>> await client.check_dns_availability(cname_prefix='my-cname')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.check_dns_availability_message.CheckDNSAvailabilityMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.check_dns_availability_result_message.CheckDNSAvailabilityResultMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.check_dns_availability

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.check_dns_availability.async_check_dns_availability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.check_dns_availability_message.CheckDNSAvailabilityMessage = {
            "cname_prefix": cname_prefix
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def compose_environments(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        application_name: Optional[
            "capo_elastic_beanstalk.types.application_name.ApplicationName"
        ] = None,
        group_name: Optional[
            "capo_elastic_beanstalk.types.group_name.GroupName"
        ] = None,
        version_labels: Optional[
            "capo_elastic_beanstalk.types.version_labels.VersionLabels"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.environment_descriptions_message.EnvironmentDescriptionsMessage":
        """<p>Create or update a group of environments that each run a separate component of a single application. Takes a list of version labels that specify application source bundles for each of the environments to create or update. The name of each environment and other required information must be included in the source bundles in an environment manifest named <code>env.yaml</code>. See <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-mgmt-compose.html">Compose Environments</a> for details.</p>

        Args:
            application_name: <p>The name of the application to which the specified source bundles belong.</p>
            group_name: <p>The name of the group to which the target environments belong. Specify a group name only if the environment name defined in each target environment's manifest ends with a + (plus) character. See <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html">Environment Manifest (env.yaml)</a> for details.</p>
            version_labels: <p>A list of version labels, specifying one or more application source bundles that belong to the target application. Each source bundle must include an environment manifest that specifies the name of the environment and the name of the solution stack to use, and optionally can specify environment links to create.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.too_many_environments_exception.TooManyEnvironmentsException: <p>The specified account has reached its limit of environments.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.compose_environments_message.ComposeEnvironmentsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.environment_descriptions_message.EnvironmentDescriptionsMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.compose_environments

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.compose_environments.async_compose_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.compose_environments_message.ComposeEnvironmentsMessage = {}
        if application_name is not None:
            input_["application_name"] = application_name
        if group_name is not None:
            input_["group_name"] = group_name
        if version_labels is not None:
            input_["version_labels"] = version_labels

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_application(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        description: Optional[
            "capo_elastic_beanstalk.types.description.Description"
        ] = None,
        resource_lifecycle_config: Optional[
            "capo_elastic_beanstalk.types.application_resource_lifecycle_config.ApplicationResourceLifecycleConfig"
        ] = None,
        tags: Optional["capo_elastic_beanstalk.types.tags.Tags"] = None,
    ) -> "capo_elastic_beanstalk.types.application_description_message.ApplicationDescriptionMessage":
        """<p>Creates an application that has one configuration template named <code>default</code> and no application versions.</p>

        Args:
            application_name: <p>The name of the application. Must be unique within your account.</p>
            description: <p>Your description of the application.</p>
            resource_lifecycle_config: <p>Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.</p>
            tags: <p>Specifies the tags applied to the application.</p> <p>Elastic Beanstalk applies these tags only to the application. Environments that you create in the application don't inherit the tags.</p>

        Raises:
            capo_elastic_beanstalk.errors.too_many_applications_exception.TooManyApplicationsException: <p>The specified account has reached its limit of applications.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new application
            The following operation creates a new application named my-app:

            >>> await client.create_application(application_name='my-app', description='my application')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.create_application_message.CreateApplicationMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.application_description_message.ApplicationDescriptionMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_application

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.create_application_message.CreateApplicationMessage = {
            "application_name": application_name
        }
        if description is not None:
            input_["description"] = description
        if resource_lifecycle_config is not None:
            input_["resource_lifecycle_config"] = resource_lifecycle_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_application_version(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        version_label: "capo_elastic_beanstalk.types.version_label.VersionLabel",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        description: Optional[
            "capo_elastic_beanstalk.types.description.Description"
        ] = None,
        source_build_information: Optional[
            "capo_elastic_beanstalk.types.source_build_information.SourceBuildInformation"
        ] = None,
        source_bundle: Optional[
            "capo_elastic_beanstalk.types.s3_location.S3Location"
        ] = None,
        build_configuration: Optional[
            "capo_elastic_beanstalk.types.build_configuration.BuildConfiguration"
        ] = None,
        auto_create_application: Optional[
            "capo_elastic_beanstalk.types.auto_create_application.AutoCreateApplication"
        ] = None,
        process: Optional[
            "capo_elastic_beanstalk.types.application_version_proccess.ApplicationVersionProccess"
        ] = None,
        tags: Optional["capo_elastic_beanstalk.types.tags.Tags"] = None,
        image_configuration: Optional[
            "capo_elastic_beanstalk.types.image_configuration.ImageConfiguration"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.application_version_description_message.ApplicationVersionDescriptionMessage":
        """<p>Creates an application version for the specified application. You can create an application version from a source bundle in Amazon S3, a commit in CodeCommit, or the output of an CodeBuild build as follows:</p> <p>Specify a commit in an CodeCommit repository with <code>SourceBuildInformation</code>.</p> <p>Specify a build in an CodeBuild with <code>SourceBuildInformation</code> and <code>BuildConfiguration</code>.</p> <p>Specify a source bundle in Amazon S3 with <code>SourceBundle</code> </p> <p>Omit both <code>SourceBuildInformation</code> and <code>SourceBundle</code> to use the default sample application.</p> <note> <p>After you create an application version with a specified Amazon S3 bucket and key location, you can't change that Amazon S3 location. If you change the Amazon S3 location, you receive an exception when you attempt to launch an environment from the application version.</p> </note>

        Args:
            application_name: <p> The name of the application. If no application is found with this name, and <code>AutoCreateApplication</code> is <code>false</code>, returns an <code>InvalidParameterValue</code> error. </p>
            version_label: <p>A label identifying this version.</p> <p>Constraint: Must be unique per application. If an application version already exists with this label for the specified application, Elastic Beanstalk returns an <code>InvalidParameterValue</code> error. </p>
            description: <p>A description of this application version.</p>
            source_build_information: <p>Specify a commit in an CodeCommit Git repository to use as the source code for the application version.</p>
            source_bundle: <p>The Amazon S3 bucket and key that identify the location of the source bundle for this version.</p> <note> <p>The Amazon S3 bucket must be in the same region as the environment.</p> <p>Unless you're specifying a source bundle in the bucket that Elastic Beanstalk manages in your account, you must assign a custom policy to your user, and grant <code>Allow</code> permission to the <code>s3:Get*</code> actions on your S3 object resource, for example, <code>arn:aws:s3:::your-bucket/your-source-bundle-object</code>.</p> </note> <p>Specify a source bundle in Amazon S3 or a commit in an CodeCommit repository (with <code>SourceBuildInformation</code>), but not both. If neither <code>SourceBundle</code> nor <code>SourceBuildInformation</code> are provided, Elastic Beanstalk uses a sample application.</p>
            build_configuration: <p>Settings for an CodeBuild build.</p> <p>Don't specify <code>BuildConfiguration</code> together with <code>ImageConfiguration</code>, which configures a container image build instead.</p>
            auto_create_application: <p>Set to <code>true</code> to create an application with the specified name if it doesn't already exist.</p>
            process: <p>Pre-processes and validates the environment manifest (<code>env.yaml</code>) and configuration files (<code>*.config</code> files in the <code>.ebextensions</code> folder) in the source bundle. Validating configuration files can identify issues prior to deploying the application version to an environment.</p> <p>You must turn processing on for application versions that you create using CodeBuild or CodeCommit. For application versions built from a source bundle in Amazon S3, processing is optional.</p> <note> <p>The <code>Process</code> option validates Elastic Beanstalk configuration files. It doesn't validate your application's configuration files, like proxy server or Docker configuration.</p> </note>
            tags: <p>Specifies the tags applied to the application version.</p> <p>Elastic Beanstalk applies these tags only to the application version. Environments that use the application version don't inherit the tags.</p>
            image_configuration: <p>The source of the container image for this application version. You can specify an image that you built and pushed to a container registry yourself, or settings for Elastic Beanstalk to build one from your source bundle. Specify exactly one of the <code>Source</code> and <code>Build</code> members.</p> <p>Don't specify <code>ImageConfiguration</code> together with <code>BuildConfiguration</code>, which configures an CodeBuild build instead.</p>

        Raises:
            capo_elastic_beanstalk.errors.code_build_not_in_service_region_exception.CodeBuildNotInServiceRegionException: <p>CodeBuild is not available in the specified region.</p>
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.s3_location_not_in_service_region_exception.S3LocationNotInServiceRegionException: <p>The specified S3 bucket does not belong to the S3 region in which the service is running. The following regions are supported:</p> <ul> <li> <p>IAD/us-east-1</p> </li> <li> <p>PDX/us-west-2</p> </li> <li> <p>DUB/eu-west-1</p> </li> </ul>
            capo_elastic_beanstalk.errors.too_many_applications_exception.TooManyApplicationsException: <p>The specified account has reached its limit of applications.</p>
            capo_elastic_beanstalk.errors.too_many_application_versions_exception.TooManyApplicationVersionsException: <p>The specified account has reached its limit of application versions.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new application
            The following operation creates a new version (v1) of an application named my-app:

            >>> await client.create_application_version(application_name='my-app', version_label='v1', description='my-app-v1', source_bundle={'S3Bucket': 'my-bucket', 'S3Key': 'sample.war'}, auto_create_application=True, process=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.create_application_version_message.CreateApplicationVersionMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.application_version_description_message.ApplicationVersionDescriptionMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_application_version

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_application_version.async_create_application_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.create_application_version_message.CreateApplicationVersionMessage = {
            "application_name": application_name,
            "version_label": version_label,
        }
        if description is not None:
            input_["description"] = description
        if source_build_information is not None:
            input_["source_build_information"] = source_build_information
        if source_bundle is not None:
            input_["source_bundle"] = source_bundle
        if build_configuration is not None:
            input_["build_configuration"] = build_configuration
        if auto_create_application is not None:
            input_["auto_create_application"] = auto_create_application
        if process is not None:
            input_["process"] = process
        if tags is not None:
            input_["tags"] = tags
        if image_configuration is not None:
            input_["image_configuration"] = image_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configuration_template(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        template_name: "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        solution_stack_name: Optional[
            "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
        ] = None,
        platform_arn: Optional[
            "capo_elastic_beanstalk.types.platform_arn.PlatformArn"
        ] = None,
        source_configuration: Optional[
            "capo_elastic_beanstalk.types.source_configuration.SourceConfiguration"
        ] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        description: Optional[
            "capo_elastic_beanstalk.types.description.Description"
        ] = None,
        option_settings: Optional[
            "capo_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList"
        ] = None,
        tags: Optional["capo_elastic_beanstalk.types.tags.Tags"] = None,
    ) -> "capo_elastic_beanstalk.types.configuration_settings_description.ConfigurationSettingsDescription":
        """<p>Creates an Elastic Beanstalk configuration template, associated with a specific Elastic Beanstalk application. You define application configuration settings in a configuration template. You can then use the configuration template to deploy different versions of the application with the same configuration settings.</p> <p>Templates aren't associated with any environment. The <code>EnvironmentName</code> response element is always <code>null</code>.</p> <p>Related Topics</p> <ul> <li> <p> <a>DescribeConfigurationOptions</a> </p> </li> <li> <p> <a>DescribeConfigurationSettings</a> </p> </li> <li> <p> <a>ListAvailableSolutionStacks</a> </p> </li> </ul>

        Args:
            application_name: <p>The name of the Elastic Beanstalk application to associate with this configuration template.</p>
            template_name: <p>The name of the configuration template.</p> <p>Constraint: This name must be unique per application.</p>
            solution_stack_name: <p>The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, <code>64bit Amazon Linux 2013.09 running Tomcat 7 Java 7</code>. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html">Supported Platforms</a> in the <i>Elastic Beanstalk Developer Guide</i>.</p> <p>You must specify <code>SolutionStackName</code> if you don't specify <code>PlatformArn</code>, <code>EnvironmentId</code>, or <code>SourceConfiguration</code>.</p> <p>Use the <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html"> <code>ListAvailableSolutionStacks</code> </a> API to obtain a list of available solution stacks.</p>
            platform_arn: <p>The Amazon Resource Name (ARN) of the custom platform. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html"> Custom Platforms</a> in the <i>Elastic Beanstalk Developer Guide</i>.</p> <note> <p>If you specify <code>PlatformArn</code>, then don't specify <code>SolutionStackName</code>.</p> </note>
            source_configuration: <p>An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.</p> <p>Values specified in <code>OptionSettings</code> override any values obtained from the <code>SourceConfiguration</code>.</p> <p>You must specify <code>SourceConfiguration</code> if you don't specify <code>PlatformArn</code>, <code>EnvironmentId</code>, or <code>SolutionStackName</code>.</p> <p>Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.</p>
            environment_id: <p>The ID of an environment whose settings you want to use to create the configuration template. You must specify <code>EnvironmentId</code> if you don't specify <code>PlatformArn</code>, <code>SolutionStackName</code>, or <code>SourceConfiguration</code>.</p>
            description: <p>An optional description for this configuration.</p>
            option_settings: <p>Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html">Option Values</a> in the <i>Elastic Beanstalk Developer Guide</i>.</p>
            tags: <p>Specifies the tags applied to the configuration template.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.too_many_buckets_exception.TooManyBucketsException: <p>The specified account has reached its limit of Amazon S3 buckets.</p>
            capo_elastic_beanstalk.errors.too_many_configuration_templates_exception.TooManyConfigurationTemplatesException: <p>The specified account has reached its limit of configuration templates.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a configuration template
            The following operation creates a configuration template named my-app-v1 from the settings applied to an environment with the id e-rpqsewtp2j:

            >>> await client.create_configuration_template(application_name='my-app', template_name='my-app-v1', environment_id='e-rpqsewtp2j')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.create_configuration_template_message.CreateConfigurationTemplateMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.configuration_settings_description.ConfigurationSettingsDescription"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_configuration_template

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_configuration_template.async_create_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.create_configuration_template_message.CreateConfigurationTemplateMessage = {
            "application_name": application_name,
            "template_name": template_name,
        }
        if solution_stack_name is not None:
            input_["solution_stack_name"] = solution_stack_name
        if platform_arn is not None:
            input_["platform_arn"] = platform_arn
        if source_configuration is not None:
            input_["source_configuration"] = source_configuration
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if description is not None:
            input_["description"] = description
        if option_settings is not None:
            input_["option_settings"] = option_settings
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_environment(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        group_name: Optional[
            "capo_elastic_beanstalk.types.group_name.GroupName"
        ] = None,
        description: Optional[
            "capo_elastic_beanstalk.types.description.Description"
        ] = None,
        cname_prefix: Optional[
            "capo_elastic_beanstalk.types.dns_cname_prefix.DNSCnamePrefix"
        ] = None,
        tier: Optional[
            "capo_elastic_beanstalk.types.environment_tier.EnvironmentTier"
        ] = None,
        tags: Optional["capo_elastic_beanstalk.types.tags.Tags"] = None,
        version_label: Optional[
            "capo_elastic_beanstalk.types.version_label.VersionLabel"
        ] = None,
        template_name: Optional[
            "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
        ] = None,
        solution_stack_name: Optional[
            "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
        ] = None,
        platform_arn: Optional[
            "capo_elastic_beanstalk.types.platform_arn.PlatformArn"
        ] = None,
        option_settings: Optional[
            "capo_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList"
        ] = None,
        options_to_remove: Optional[
            "capo_elastic_beanstalk.types.options_specifier_list.OptionsSpecifierList"
        ] = None,
        operations_role: Optional[
            "capo_elastic_beanstalk.types.operations_role.OperationsRole"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.environment_description.EnvironmentDescription":
        """<p>Launches an Elastic Beanstalk environment for the specified application using the specified configuration.</p>

        Args:
            application_name: <p>The name of the application that is associated with this environment.</p>
            environment_name: <p>A unique name for the environment.</p> <p>Constraint: Must be from 4 to 40 characters in length. The name can contain only letters, numbers, and hyphens. It can't start or end with a hyphen. This name must be unique within a region in your account. If the specified name already exists in the region, Elastic Beanstalk returns an <code>InvalidParameterValue</code> error. </p> <p>If you don't specify the <code>CNAMEPrefix</code> parameter, the environment name becomes part of the CNAME, and therefore part of the visible URL for your application.</p>
            group_name: <p>The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name parameter. See <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html">Environment Manifest (env.yaml)</a> for details.</p>
            description: <p>Your description for this environment.</p>
            cname_prefix: <p>If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.</p>
            tier: <p>Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources on Amazon EC2 instances or on an Amazon EKS cluster, and, for Amazon EC2, whether the environment serves HTTP(S) requests or processes background tasks from a queue.</p>
            tags: <p>Specifies the tags applied to resources in the environment.</p>
            version_label: <p>The name of the application version to deploy.</p> <p>Default: If not specified, Elastic Beanstalk attempts to deploy the sample application.</p>
            template_name: <p>The name of the Elastic Beanstalk configuration template to use with the environment.</p> <note> <p>If you specify <code>TemplateName</code>, then don't specify <code>SolutionStackName</code>.</p> </note>
            solution_stack_name: <p>The name of an Elastic Beanstalk solution stack (platform version) to use with the environment. If specified, Elastic Beanstalk sets the configuration values to the default values associated with the specified solution stack. For a list of current solution stacks, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html">Elastic Beanstalk Supported Platforms</a> in the <i>Elastic Beanstalk Platforms</i> guide.</p> <note> <p>If you specify <code>SolutionStackName</code>, don't specify <code>PlatformArn</code> or <code>TemplateName</code>.</p> </note>
            platform_arn: <p>The Amazon Resource Name (ARN) of the custom platform to use with the environment. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html">Custom Platforms</a> in the <i>Elastic Beanstalk Developer Guide</i>.</p> <note> <p>If you specify <code>PlatformArn</code>, don't specify <code>SolutionStackName</code>.</p> </note>
            option_settings: <p>If specified, Elastic Beanstalk sets the specified configuration options to the requested value in the configuration set for the new environment. These override the values obtained from the solution stack or the configuration template.</p>
            options_to_remove: <p>A list of custom user-defined configuration options to remove from the configuration set for this new environment.</p>
            operations_role: <important> <p>The operations role feature of Elastic Beanstalk is in beta release and is subject to change.</p> </important> <p>The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role. If specified, Elastic Beanstalk uses the operations role for permissions to downstream services during this call and during subsequent calls acting on this environment. To specify an operations role, you must have the <code>iam:PassRole</code> permission for the role.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.too_many_environments_exception.TooManyEnvironmentsException: <p>The specified account has reached its limit of environments.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new environment for an application
            The following operation creates a new environment for version v1 of a java application named my-app:

            >>> await client.create_environment(application_name='my-app', environment_name='my-env', cname_prefix='my-app', version_label='v1', solution_stack_name='64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.create_environment_message.CreateEnvironmentMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.environment_description.EnvironmentDescription"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_environment

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_environment.async_create_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.create_environment_message.CreateEnvironmentMessage = {
            "application_name": application_name
        }
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if group_name is not None:
            input_["group_name"] = group_name
        if description is not None:
            input_["description"] = description
        if cname_prefix is not None:
            input_["cname_prefix"] = cname_prefix
        if tier is not None:
            input_["tier"] = tier
        if tags is not None:
            input_["tags"] = tags
        if version_label is not None:
            input_["version_label"] = version_label
        if template_name is not None:
            input_["template_name"] = template_name
        if solution_stack_name is not None:
            input_["solution_stack_name"] = solution_stack_name
        if platform_arn is not None:
            input_["platform_arn"] = platform_arn
        if option_settings is not None:
            input_["option_settings"] = option_settings
        if options_to_remove is not None:
            input_["options_to_remove"] = options_to_remove
        if operations_role is not None:
            input_["operations_role"] = operations_role

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_platform_version(
        self,
        platform_name: "capo_elastic_beanstalk.types.platform_name.PlatformName",
        platform_version: "capo_elastic_beanstalk.types.platform_version.PlatformVersion",
        platform_definition_bundle: "capo_elastic_beanstalk.types.s3_location.S3Location",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        option_settings: Optional[
            "capo_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList"
        ] = None,
        tags: Optional["capo_elastic_beanstalk.types.tags.Tags"] = None,
    ) -> "capo_elastic_beanstalk.types.create_platform_version_result.CreatePlatformVersionResult":
        """<p>Create a new version of your custom platform.</p>

        Args:
            platform_name: <p>The name of your custom platform.</p>
            platform_version: <p>The number, such as 1.0.2, for the new platform version.</p>
            platform_definition_bundle: <p>The location of the platform definition archive in Amazon S3.</p>
            environment_name: <p>The name of the builder environment.</p>
            option_settings: <p>The configuration option settings to apply to the builder environment.</p>
            tags: <p>Specifies the tags applied to the new platform version.</p> <p>Elastic Beanstalk applies these tags only to the platform version. Environments that you create using the platform version don't inherit the tags.</p>

        Raises:
            capo_elastic_beanstalk.errors.elastic_beanstalk_service_exception.ElasticBeanstalkServiceException: <p>A generic service exception has occurred.</p>
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.too_many_platforms_exception.TooManyPlatformsException: <p>You have exceeded the maximum number of allowed platforms associated with the account.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.create_platform_version_request.CreatePlatformVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.create_platform_version_result.CreatePlatformVersionResult"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_platform_version

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_platform_version.async_create_platform_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.create_platform_version_request.CreatePlatformVersionRequest = {
            "platform_name": platform_name,
            "platform_version": platform_version,
            "platform_definition_bundle": platform_definition_bundle,
        }
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if option_settings is not None:
            input_["option_settings"] = option_settings
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_storage_location(
        self, *, config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None
    ) -> "capo_elastic_beanstalk.types.create_storage_location_result_message.CreateStorageLocationResultMessage":
        """<p>Creates a bucket in Amazon S3 to store application versions, logs, and other files used by Elastic Beanstalk environments. The Elastic Beanstalk console and EB CLI call this API the first time you create an environment in a region. If the storage location already exists, <code>CreateStorageLocation</code> still returns the bucket name but does not create a new bucket.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.s3_subscription_required_exception.S3SubscriptionRequiredException: <p>The specified account does not have a subscription to Amazon S3.</p>
            capo_elastic_beanstalk.errors.too_many_buckets_exception.TooManyBucketsException: <p>The specified account has reached its limit of Amazon S3 buckets.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new environment for an application
            The following operation creates a new environment for version v1 of a java application named my-app:

            >>> await client.create_storage_location()
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.create_storage_location_result_message.CreateStorageLocationResultMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_storage_location

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.create_storage_location.async_create_storage_location(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_application(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        terminate_env_by_force: Optional[
            "capo_elastic_beanstalk.types.terminate_env_force.TerminateEnvForce"
        ] = None,
    ) -> None:
        """<p>Deletes the specified application along with all associated versions and configurations. The application versions will not be deleted from your Amazon S3 bucket.</p> <note> <p>You cannot delete an application that has a running environment.</p> </note>

        Args:
            application_name: <p>The name of the application to delete.</p>
            terminate_env_by_force: <p>When set to true, running environments will be terminated before deleting the application.</p>

        Raises:
            capo_elastic_beanstalk.errors.operation_in_progress_exception.OperationInProgressException: <p>Unable to perform the specified operation because another operation that effects an element in this activity is already in progress.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an application
            The following operation deletes an application named my-app:

            >>> await client.delete_application(application_name='my-app')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.delete_application_message.DeleteApplicationMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.delete_application

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.delete_application_message.DeleteApplicationMessage = {
            "application_name": application_name
        }
        if terminate_env_by_force is not None:
            input_["terminate_env_by_force"] = terminate_env_by_force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_application_version(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        version_label: "capo_elastic_beanstalk.types.version_label.VersionLabel",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        delete_source_bundle: Optional[
            "capo_elastic_beanstalk.types.delete_source_bundle.DeleteSourceBundle"
        ] = None,
    ) -> None:
        """<p>Deletes the specified version from the specified application.</p> <note> <p>You cannot delete an application version that is associated with a running environment.</p> </note>

        Args:
            application_name: <p>The name of the application to which the version belongs.</p>
            version_label: <p>The label of the version to delete.</p>
            delete_source_bundle: <p>Set to <code>true</code> to delete the source bundle from your storage bucket. Otherwise, the application version is deleted only from Elastic Beanstalk and the source bundle remains in Amazon S3.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.operation_in_progress_exception.OperationInProgressException: <p>Unable to perform the specified operation because another operation that effects an element in this activity is already in progress.</p>
            capo_elastic_beanstalk.errors.s3_location_not_in_service_region_exception.S3LocationNotInServiceRegionException: <p>The specified S3 bucket does not belong to the S3 region in which the service is running. The following regions are supported:</p> <ul> <li> <p>IAD/us-east-1</p> </li> <li> <p>PDX/us-west-2</p> </li> <li> <p>DUB/eu-west-1</p> </li> </ul>
            capo_elastic_beanstalk.errors.source_bundle_deletion_exception.SourceBundleDeletionException: <p>Unable to delete the Amazon S3 source bundle associated with the application version. The application version was deleted successfully.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an application version
            The following operation deletes an application version named 22a0-stage-150819_182129 for an application named my-app:

            >>> await client.delete_application_version(application_name='my-app', version_label='22a0-stage-150819_182129', delete_source_bundle=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.delete_application_version_message.DeleteApplicationVersionMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.delete_application_version

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.delete_application_version.async_delete_application_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.delete_application_version_message.DeleteApplicationVersionMessage = {
            "application_name": application_name,
            "version_label": version_label,
        }
        if delete_source_bundle is not None:
            input_["delete_source_bundle"] = delete_source_bundle

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_template(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        template_name: "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified configuration template.</p> <note> <p>When you launch an environment using a configuration template, the environment gets a copy of the template. You can delete or modify the environment's copy of the template without affecting the running environment.</p> </note>

        Args:
            application_name: <p>The name of the application to delete the configuration template from.</p>
            template_name: <p>The name of the configuration template to delete.</p>

        Raises:
            capo_elastic_beanstalk.errors.operation_in_progress_exception.OperationInProgressException: <p>Unable to perform the specified operation because another operation that effects an element in this activity is already in progress.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a configuration template
            The following operation deletes a configuration template named my-template for an application named my-app:

            >>> await client.delete_configuration_template(application_name='my-app', template_name='my-template')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.delete_configuration_template_message.DeleteConfigurationTemplateMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.delete_configuration_template

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.delete_configuration_template.async_delete_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.delete_configuration_template_message.DeleteConfigurationTemplateMessage = {
            "application_name": application_name,
            "template_name": template_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment_configuration(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        environment_name: "capo_elastic_beanstalk.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
    ) -> None:
        """<p>Deletes the draft configuration associated with the running environment.</p> <p>Updating a running environment with any configuration changes creates a draft configuration set. You can get the draft configuration using <a>DescribeConfigurationSettings</a> while the update is in progress or if the update fails. The <code>DeploymentStatus</code> for the draft configuration indicates whether the deployment is in process or has failed. The draft configuration remains in existence until it is deleted with this action.</p>

        Args:
            application_name: <p>The name of the application the environment is associated with.</p>
            environment_name: <p>The name of the environment to delete the draft configuration from.</p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a draft configuration
            The following operation deletes a draft configuration for an environment named my-env:

            >>> await client.delete_environment_configuration(application_name='my-app', environment_name='my-env')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.delete_environment_configuration_message.DeleteEnvironmentConfigurationMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.delete_environment_configuration

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.delete_environment_configuration.async_delete_environment_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.delete_environment_configuration_message.DeleteEnvironmentConfigurationMessage = {
            "application_name": application_name,
            "environment_name": environment_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_platform_version(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        platform_arn: Optional[
            "capo_elastic_beanstalk.types.platform_arn.PlatformArn"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.delete_platform_version_result.DeletePlatformVersionResult":
        """<p>Deletes the specified version of a custom platform.</p>

        Args:
            platform_arn: <p>The ARN of the version of the custom platform.</p>

        Raises:
            capo_elastic_beanstalk.errors.elastic_beanstalk_service_exception.ElasticBeanstalkServiceException: <p>A generic service exception has occurred.</p>
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.operation_in_progress_exception.OperationInProgressException: <p>Unable to perform the specified operation because another operation that effects an element in this activity is already in progress.</p>
            capo_elastic_beanstalk.errors.platform_version_still_referenced_exception.PlatformVersionStillReferencedException: <p>You cannot delete the platform version because there are still environments running on it.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.delete_platform_version_request.DeletePlatformVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.delete_platform_version_result.DeletePlatformVersionResult"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.delete_platform_version

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.delete_platform_version.async_delete_platform_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.delete_platform_version_request.DeletePlatformVersionRequest = {}
        if platform_arn is not None:
            input_["platform_arn"] = platform_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_account_attributes(
        self, *, config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None
    ) -> "capo_elastic_beanstalk.types.describe_account_attributes_result.DescribeAccountAttributesResult":
        """<p>Returns attributes related to Elastic Beanstalk that are associated with the calling Amazon Web Services account.</p> <p>The result currently has one set of attributes—resource quotas.</p> <p>This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.describe_account_attributes_result.DescribeAccountAttributesResult"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_account_attributes

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_account_attributes.async_describe_account_attributes(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_applications(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        application_names: Optional[
            "capo_elastic_beanstalk.types.application_names_list.ApplicationNamesList"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.application_descriptions_message.ApplicationDescriptionsMessage":
        """<p>Returns the descriptions of existing applications.</p> <p>This action only returns information about applications that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access two of three applications. When the user calls the <i>DescribeApplications</i> action, the response will only include the two applications that the user has permission to access instead of all three applications. If the user doesn’t have access to any of the applications an empty result is returned.</p> <note> <p>The <i>AWSElasticBeanstalkReadOnly</i> managed policy allows operators to view information about resources related to Elastic Beanstalk environments. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Args:
            application_names: <p>If specified, Elastic Beanstalk restricts the returned descriptions to only include those with the specified names.</p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view a list of applications
            The following operation retrieves information about applications in the current region:

            >>> await client.describe_applications()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_applications_message.DescribeApplicationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.application_descriptions_message.ApplicationDescriptionsMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_applications

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_applications.async_describe_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_applications_message.DescribeApplicationsMessage = {}
        if application_names is not None:
            input_["application_names"] = application_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_application_versions(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        application_name: Optional[
            "capo_elastic_beanstalk.types.application_name.ApplicationName"
        ] = None,
        version_labels: Optional[
            "capo_elastic_beanstalk.types.version_labels_list.VersionLabelsList"
        ] = None,
        max_records: Optional[
            "capo_elastic_beanstalk.types.max_records.MaxRecords"
        ] = None,
        next_token: Optional["capo_elastic_beanstalk.types.token.Token"] = None,
    ) -> "capo_elastic_beanstalk.types.application_version_descriptions_message.ApplicationVersionDescriptionsMessage":
        """<p>Retrieve a list of application versions.</p> <p>This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Args:
            application_name: <p>Specify an application name to show only application versions for that application.</p>
            version_labels: <p>Specify a version label to show a specific application version.</p>
            max_records: <p>For a paginated request. Specify a maximum number of application versions to include in each response.</p> <p>If no <code>MaxRecords</code> is specified, all available application versions are retrieved in a single response.</p>
            next_token: <p>For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If no <code>NextToken</code> is specified, the first page is retrieved.</p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view information about an application version
            The following operation retrieves information about an application version labeled v2:

            >>> await client.describe_application_versions(application_name='my-app', version_labels=['v2'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_application_versions_message.DescribeApplicationVersionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.application_version_descriptions_message.ApplicationVersionDescriptionsMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_application_versions

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_application_versions.async_describe_application_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_application_versions_message.DescribeApplicationVersionsMessage = {}
        if application_name is not None:
            input_["application_name"] = application_name
        if version_labels is not None:
            input_["version_labels"] = version_labels
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_configuration_options(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        application_name: Optional[
            "capo_elastic_beanstalk.types.application_name.ApplicationName"
        ] = None,
        template_name: Optional[
            "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        solution_stack_name: Optional[
            "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
        ] = None,
        platform_arn: Optional[
            "capo_elastic_beanstalk.types.platform_arn.PlatformArn"
        ] = None,
        options: Optional[
            "capo_elastic_beanstalk.types.options_specifier_list.OptionsSpecifierList"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.configuration_options_description.ConfigurationOptionsDescription":
        """<p>Describes the configuration options that are used in a particular configuration template or environment, or that a specified solution stack defines. The description includes the values the options, their default values, and an indication of the required action on a running environment if an option value is changed.</p> <p>This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Args:
            application_name: <p>The name of the application associated with the configuration template or environment. Only needed if you want to describe the configuration options associated with either the configuration template or environment.</p>
            template_name: <p>The name of the configuration template whose configuration options you want to describe.</p>
            environment_name: <p>The name of the environment whose configuration options you want to describe.</p>
            solution_stack_name: <p>The name of the solution stack whose configuration options you want to describe.</p>
            platform_arn: <p>The ARN of the custom platform.</p>
            options: <p>If specified, restricts the descriptions to only the specified options.</p>

        Raises:
            capo_elastic_beanstalk.errors.too_many_buckets_exception.TooManyBucketsException: <p>The specified account has reached its limit of Amazon S3 buckets.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view configuration options for an environment
            The following operation retrieves descriptions of all available configuration options for an environment named my-env:

            >>> await client.describe_configuration_options(application_name='my-app', environment_name='my-env')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_configuration_options_message.DescribeConfigurationOptionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.configuration_options_description.ConfigurationOptionsDescription"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_configuration_options

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_configuration_options.async_describe_configuration_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_configuration_options_message.DescribeConfigurationOptionsMessage = {}
        if application_name is not None:
            input_["application_name"] = application_name
        if template_name is not None:
            input_["template_name"] = template_name
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if solution_stack_name is not None:
            input_["solution_stack_name"] = solution_stack_name
        if platform_arn is not None:
            input_["platform_arn"] = platform_arn
        if options is not None:
            input_["options"] = options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_configuration_settings(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        template_name: Optional[
            "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.configuration_settings_descriptions.ConfigurationSettingsDescriptions":
        """<p>Returns a description of the settings for the specified configuration set, that is, either a configuration template or the configuration set associated with a running environment.</p> <p>When describing the settings for the configuration set associated with a running environment, it is possible to receive two sets of setting descriptions. One is the deployed configuration set, and the other is a draft configuration of an environment that is either in the process of deployment or that failed to deploy.</p> <p>This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note> <p>Related Topics</p> <ul> <li> <p> <a>DeleteEnvironmentConfiguration</a> </p> </li> </ul>

        Args:
            application_name: <p>The application for the environment or configuration template.</p>
            template_name: <p>The name of the configuration template to describe.</p> <p> Conditional: You must specify either this parameter or an EnvironmentName, but not both. If you specify both, Elastic Beanstalk returns an <code>InvalidParameterCombination</code> error. If you do not specify either, Elastic Beanstalk returns a <code>MissingRequiredParameter</code> error. </p>
            environment_name: <p>The name of the environment to describe.</p> <p> Condition: You must specify either this or a TemplateName, but not both. If you specify both, Elastic Beanstalk returns an <code>InvalidParameterCombination</code> error. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>

        Raises:
            capo_elastic_beanstalk.errors.too_many_buckets_exception.TooManyBucketsException: <p>The specified account has reached its limit of Amazon S3 buckets.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view configurations settings for an environment
            The following operation retrieves configuration settings for an environment named my-env:

            >>> await client.describe_configuration_settings(application_name='my-app', environment_name='my-env')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_configuration_settings_message.DescribeConfigurationSettingsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.configuration_settings_descriptions.ConfigurationSettingsDescriptions"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_configuration_settings

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_configuration_settings.async_describe_configuration_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_configuration_settings_message.DescribeConfigurationSettingsMessage = {
            "application_name": application_name
        }
        if template_name is not None:
            input_["template_name"] = template_name
        if environment_name is not None:
            input_["environment_name"] = environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_environment_health(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        attribute_names: Optional[
            "capo_elastic_beanstalk.types.environment_health_attributes.EnvironmentHealthAttributes"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.describe_environment_health_result.DescribeEnvironmentHealthResult":
        """<p>Returns information about the overall health of the specified environment. The <b>DescribeEnvironmentHealth</b> operation is only available with Elastic Beanstalk Enhanced Health.</p> <p>This action only returns information about environments that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three environments. When the user calls this action, the response will only include the one environment that the user has permission to access instead of all three environments. If the user doesn’t have access to any of the environments an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk environments. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Args:
            environment_name: <p>Specify the environment by name.</p> <p>You must specify either this or an EnvironmentName, or both.</p>
            environment_id: <p>Specify the environment by ID.</p> <p>You must specify either this or an EnvironmentName, or both.</p>
            attribute_names: <p>Specify the response elements to return. To retrieve all attributes, set to <code>All</code>. If no attribute names are specified, returns the name of the environment.</p>

        Raises:
            capo_elastic_beanstalk.errors.elastic_beanstalk_service_exception.ElasticBeanstalkServiceException: <p>A generic service exception has occurred.</p>
            capo_elastic_beanstalk.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters is not valid. Please correct the input parameters and try the operation again.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view environment health
            The following operation retrieves overall health information for an environment named my-env:

            >>> await client.describe_environment_health(environment_name='my-env', attribute_names=['All'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_environment_health_request.DescribeEnvironmentHealthRequest]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.describe_environment_health_result.DescribeEnvironmentHealthResult"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_environment_health

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_environment_health.async_describe_environment_health(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_environment_health_request.DescribeEnvironmentHealthRequest = {}
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if attribute_names is not None:
            input_["attribute_names"] = attribute_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_environment_managed_action_history(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        next_token: Optional["capo_elastic_beanstalk.types.string.String"] = None,
        max_items: Optional[
            "capo_elastic_beanstalk.types.managed_action_history_max_items.ManagedActionHistoryMaxItems"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.describe_environment_managed_action_history_result.DescribeEnvironmentManagedActionHistoryResult":
        """<p>Lists an environment's completed and failed managed actions.</p>

        Args:
            environment_id: <p>The environment ID of the target environment.</p>
            environment_name: <p>The name of the target environment.</p>
            next_token: <p>The pagination token returned by a previous request.</p>
            max_items: <p>The maximum number of items to return for a single request.</p>

        Raises:
            capo_elastic_beanstalk.errors.elastic_beanstalk_service_exception.ElasticBeanstalkServiceException: <p>A generic service exception has occurred.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_environment_managed_action_history_request.DescribeEnvironmentManagedActionHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.describe_environment_managed_action_history_result.DescribeEnvironmentManagedActionHistoryResult"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_environment_managed_action_history

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_environment_managed_action_history.async_describe_environment_managed_action_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_environment_managed_action_history_request.DescribeEnvironmentManagedActionHistoryRequest = {}
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_environment_managed_action_history(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        next_token: Optional["capo_elastic_beanstalk.types.string.String"] = None,
        max_items: Optional[
            "capo_elastic_beanstalk.types.managed_action_history_max_items.ManagedActionHistoryMaxItems"
        ] = None,
    ) -> "AsyncIterator[capo_elastic_beanstalk.types.managed_action_history_item.ManagedActionHistoryItem]":
        _token = next_token
        while True:
            _response = await self.describe_environment_managed_action_history(
                config_overrides=config_overrides,
                environment_id=environment_id,
                environment_name=environment_name,
                next_token=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("managed_action_history_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_environment_managed_actions(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_name: Optional["capo_elastic_beanstalk.types.string.String"] = None,
        environment_id: Optional["capo_elastic_beanstalk.types.string.String"] = None,
        status: Optional[
            "capo_elastic_beanstalk.types.action_status.ActionStatus"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.describe_environment_managed_actions_result.DescribeEnvironmentManagedActionsResult":
        """<p>Lists an environment's upcoming and in-progress managed actions.</p> <p>This action only returns information about environments that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three environments. When the user calls this action, the response will only include the one environment that the user has permission to access instead of all three environments. If the user doesn’t have access to any of the environments an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk environments. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Args:
            environment_name: <p>The name of the target environment.</p>
            environment_id: <p>The environment ID of the target environment.</p>
            status: <p>To show only actions with a particular status, specify a status.</p>

        Raises:
            capo_elastic_beanstalk.errors.elastic_beanstalk_service_exception.ElasticBeanstalkServiceException: <p>A generic service exception has occurred.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_environment_managed_actions_request.DescribeEnvironmentManagedActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.describe_environment_managed_actions_result.DescribeEnvironmentManagedActionsResult"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_environment_managed_actions

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_environment_managed_actions.async_describe_environment_managed_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_environment_managed_actions_request.DescribeEnvironmentManagedActionsRequest = {}
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_environment_resources(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.environment_resource_descriptions_message.EnvironmentResourceDescriptionsMessage":
        """<p>Returns Amazon Web Services resources for this environment.</p>

        Args:
            environment_id: <p>The ID of the environment to retrieve Amazon Web Services resource usage data.</p> <p> Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>
            environment_name: <p>The name of the environment to retrieve Amazon Web Services resource usage data.</p> <p> Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view information about the AWS resources in your environment
            The following operation retrieves information about resources in an environment named my-env:

            >>> await client.describe_environment_resources(environment_name='my-env')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_environment_resources_message.DescribeEnvironmentResourcesMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.environment_resource_descriptions_message.EnvironmentResourceDescriptionsMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_environment_resources

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_environment_resources.async_describe_environment_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_environment_resources_message.DescribeEnvironmentResourcesMessage = {}
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if environment_name is not None:
            input_["environment_name"] = environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_environments(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        application_name: Optional[
            "capo_elastic_beanstalk.types.application_name.ApplicationName"
        ] = None,
        version_label: Optional[
            "capo_elastic_beanstalk.types.version_label.VersionLabel"
        ] = None,
        environment_ids: Optional[
            "capo_elastic_beanstalk.types.environment_id_list.EnvironmentIdList"
        ] = None,
        environment_names: Optional[
            "capo_elastic_beanstalk.types.environment_names_list.EnvironmentNamesList"
        ] = None,
        include_deleted: Optional[
            "capo_elastic_beanstalk.types.include_deleted.IncludeDeleted"
        ] = None,
        included_deleted_back_to: Optional[
            "capo_elastic_beanstalk.types.include_deleted_back_to.IncludeDeletedBackTo"
        ] = None,
        max_records: Optional[
            "capo_elastic_beanstalk.types.max_records.MaxRecords"
        ] = None,
        next_token: Optional["capo_elastic_beanstalk.types.token.Token"] = None,
    ) -> "capo_elastic_beanstalk.types.environment_descriptions_message.EnvironmentDescriptionsMessage":
        """<p>Returns descriptions for existing environments.</p> <p>This action only returns information about environments that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three environments. When the user calls the <i>DescribeEnvironments</i> action, the response will only include the one environment that the user has permission to access instead of all three environments. If the user doesn’t have access to any of the environments an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk environments. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Args:
            application_name: <p>If specified, Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application.</p>
            version_label: <p>If specified, Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application version.</p>
            environment_ids: <p>If specified, Elastic Beanstalk restricts the returned descriptions to include only those that have the specified IDs.</p>
            environment_names: <p>If specified, Elastic Beanstalk restricts the returned descriptions to include only those that have the specified names.</p>
            include_deleted: <p>Indicates whether to include deleted environments:</p> <p> <code>true</code>: Environments that have been deleted after <code>IncludedDeletedBackTo</code> are displayed.</p> <p> <code>false</code>: Do not include deleted environments.</p>
            included_deleted_back_to: <p> If specified when <code>IncludeDeleted</code> is set to <code>true</code>, then environments deleted after this date are displayed. </p>
            max_records: <p>For a paginated request. Specify a maximum number of environments to include in each response.</p> <p>If no <code>MaxRecords</code> is specified, all available environments are retrieved in a single response.</p>
            next_token: <p>For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If no <code>NextToken</code> is specified, the first page is retrieved.</p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view information about an environment
            The following operation retrieves information about an environment named my-env:

            >>> await client.describe_environments(environment_names=['my-env'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_environments_message.DescribeEnvironmentsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.environment_descriptions_message.EnvironmentDescriptionsMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_environments

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_environments.async_describe_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_environments_message.DescribeEnvironmentsMessage = {}
        if application_name is not None:
            input_["application_name"] = application_name
        if version_label is not None:
            input_["version_label"] = version_label
        if environment_ids is not None:
            input_["environment_ids"] = environment_ids
        if environment_names is not None:
            input_["environment_names"] = environment_names
        if include_deleted is not None:
            input_["include_deleted"] = include_deleted
        if included_deleted_back_to is not None:
            input_["included_deleted_back_to"] = included_deleted_back_to
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_events(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        application_name: Optional[
            "capo_elastic_beanstalk.types.application_name.ApplicationName"
        ] = None,
        version_label: Optional[
            "capo_elastic_beanstalk.types.version_label.VersionLabel"
        ] = None,
        template_name: Optional[
            "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
        ] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        platform_arn: Optional[
            "capo_elastic_beanstalk.types.platform_arn.PlatformArn"
        ] = None,
        request_id: Optional[
            "capo_elastic_beanstalk.types.request_id.RequestId"
        ] = None,
        severity: Optional[
            "capo_elastic_beanstalk.types.event_severity.EventSeverity"
        ] = None,
        start_time: Optional[
            "capo_elastic_beanstalk.types.time_filter_start.TimeFilterStart"
        ] = None,
        end_time: Optional[
            "capo_elastic_beanstalk.types.time_filter_end.TimeFilterEnd"
        ] = None,
        max_records: Optional[
            "capo_elastic_beanstalk.types.max_records.MaxRecords"
        ] = None,
        next_token: Optional["capo_elastic_beanstalk.types.token.Token"] = None,
    ) -> "capo_elastic_beanstalk.types.event_descriptions_message.EventDescriptionsMessage":
        """<p>Returns list of event descriptions matching criteria up to the last 6 weeks.</p> <p>This action returns the most recent 1,000 events from the specified <code>NextToken</code>.</p> <p>This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Args:
            application_name: <p>If specified, Elastic Beanstalk restricts the returned descriptions to include only those associated with this application.</p>
            version_label: <p>If specified, Elastic Beanstalk restricts the returned descriptions to those associated with this application version.</p>
            template_name: <p>If specified, Elastic Beanstalk restricts the returned descriptions to those that are associated with this environment configuration.</p>
            environment_id: <p>If specified, Elastic Beanstalk restricts the returned descriptions to those associated with this environment.</p>
            environment_name: <p>If specified, Elastic Beanstalk restricts the returned descriptions to those associated with this environment.</p>
            platform_arn: <p>The ARN of a custom platform version. If specified, Elastic Beanstalk restricts the returned descriptions to those associated with this custom platform version.</p>
            request_id: <p>If specified, Elastic Beanstalk restricts the described events to include only those associated with this request ID.</p>
            severity: <p>If specified, limits the events returned from this call to include only those with the specified severity or higher.</p>
            start_time: <p>If specified, Elastic Beanstalk restricts the returned descriptions to those that occur on or after this time.</p>
            end_time: <p> If specified, Elastic Beanstalk restricts the returned descriptions to those that occur up to, but not including, the <code>EndTime</code>. </p>
            max_records: <p>Specifies the maximum number of events that can be returned, beginning with the most recent event.</p>
            next_token: <p>Pagination token. If specified, the events return the next batch of results.</p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view events for an environment
            The following operation retrieves events for an environment named my-env:

            >>> await client.describe_events(environment_name='my-env')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_events_message.DescribeEventsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.event_descriptions_message.EventDescriptionsMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_events

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_events.async_describe_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_events_message.DescribeEventsMessage = {}
        if application_name is not None:
            input_["application_name"] = application_name
        if version_label is not None:
            input_["version_label"] = version_label
        if template_name is not None:
            input_["template_name"] = template_name
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if platform_arn is not None:
            input_["platform_arn"] = platform_arn
        if request_id is not None:
            input_["request_id"] = request_id
        if severity is not None:
            input_["severity"] = severity
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_events(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        application_name: Optional[
            "capo_elastic_beanstalk.types.application_name.ApplicationName"
        ] = None,
        version_label: Optional[
            "capo_elastic_beanstalk.types.version_label.VersionLabel"
        ] = None,
        template_name: Optional[
            "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
        ] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        platform_arn: Optional[
            "capo_elastic_beanstalk.types.platform_arn.PlatformArn"
        ] = None,
        request_id: Optional[
            "capo_elastic_beanstalk.types.request_id.RequestId"
        ] = None,
        severity: Optional[
            "capo_elastic_beanstalk.types.event_severity.EventSeverity"
        ] = None,
        start_time: Optional[
            "capo_elastic_beanstalk.types.time_filter_start.TimeFilterStart"
        ] = None,
        end_time: Optional[
            "capo_elastic_beanstalk.types.time_filter_end.TimeFilterEnd"
        ] = None,
        max_records: Optional[
            "capo_elastic_beanstalk.types.max_records.MaxRecords"
        ] = None,
        next_token: Optional["capo_elastic_beanstalk.types.token.Token"] = None,
    ) -> (
        "AsyncIterator[capo_elastic_beanstalk.types.event_description.EventDescription]"
    ):
        _token = next_token
        while True:
            _response = await self.describe_events(
                config_overrides=config_overrides,
                application_name=application_name,
                version_label=version_label,
                template_name=template_name,
                environment_id=environment_id,
                environment_name=environment_name,
                platform_arn=platform_arn,
                request_id=request_id,
                severity=severity,
                start_time=start_time,
                end_time=end_time,
                max_records=max_records,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_instances_health(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        attribute_names: Optional[
            "capo_elastic_beanstalk.types.instances_health_attributes.InstancesHealthAttributes"
        ] = None,
        next_token: Optional[
            "capo_elastic_beanstalk.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.describe_instances_health_result.DescribeInstancesHealthResult":
        """<p>Retrieves detailed information about the health of instances in your Elastic Beanstalk environments. This operation requires <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced.html">enhanced health reporting</a>.</p> <p>This action only returns information about environments that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three environments. When the user calls this action, the response will only include the one environment that the user has permission to access instead of all three environments. If the user doesn’t have access to any of the environments an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk environments. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Args:
            environment_name: <p>Specify the Elastic Beanstalk environment by name.</p>
            environment_id: <p>Specify the Elastic Beanstalk environment by ID.</p>
            attribute_names: <p>Specifies the response elements you wish to receive. To retrieve all attributes, set to <code>All</code>. If no attribute names are specified, returns a list of instances.</p>
            next_token: <p>Specify the pagination token returned by a previous call.</p>

        Raises:
            capo_elastic_beanstalk.errors.elastic_beanstalk_service_exception.ElasticBeanstalkServiceException: <p>A generic service exception has occurred.</p>
            capo_elastic_beanstalk.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters is not valid. Please correct the input parameters and try the operation again.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view environment health
            The following operation retrieves health information for instances in an environment named my-env:

            >>> await client.describe_instances_health(environment_name='my-env', attribute_names=['All'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_instances_health_request.DescribeInstancesHealthRequest]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.describe_instances_health_result.DescribeInstancesHealthResult"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_instances_health

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_instances_health.async_describe_instances_health(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_instances_health_request.DescribeInstancesHealthRequest = {}
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if attribute_names is not None:
            input_["attribute_names"] = attribute_names
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_platform_version(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        platform_arn: Optional[
            "capo_elastic_beanstalk.types.platform_arn.PlatformArn"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.describe_platform_version_result.DescribePlatformVersionResult":
        """<p>Describes a platform version. Provides full details. Compare to <a>ListPlatformVersions</a>, which provides summary information about a list of platform versions.</p> <p>For definitions of platform version and other platform-related terms, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html">Elastic Beanstalk Platforms Glossary</a>.</p> <p>This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Args:
            platform_arn: <p>The ARN of the platform version.</p>

        Raises:
            capo_elastic_beanstalk.errors.elastic_beanstalk_service_exception.ElasticBeanstalkServiceException: <p>A generic service exception has occurred.</p>
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.describe_platform_version_request.DescribePlatformVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.describe_platform_version_result.DescribePlatformVersionResult"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_platform_version

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.describe_platform_version.async_describe_platform_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.describe_platform_version_request.DescribePlatformVersionRequest = {}
        if platform_arn is not None:
            input_["platform_arn"] = platform_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_environment_operations_role(
        self,
        environment_name: "capo_elastic_beanstalk.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
    ) -> None:
        """<important> <p>The operations role feature of Elastic Beanstalk is in beta release and is subject to change.</p> </important> <p>Disassociate the operations role from an environment. After this call is made, Elastic Beanstalk uses the caller's permissions for permissions to downstream services during subsequent calls acting on this environment.</p>

        Args:
            environment_name: <p>The name of the environment from which to disassociate the operations role.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.disassociate_environment_operations_role_message.DisassociateEnvironmentOperationsRoleMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.disassociate_environment_operations_role

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.disassociate_environment_operations_role.async_disassociate_environment_operations_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.disassociate_environment_operations_role_message.DisassociateEnvironmentOperationsRoleMessage = {
            "environment_name": environment_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_available_solution_stacks(
        self, *, config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None
    ) -> "capo_elastic_beanstalk.types.list_available_solution_stacks_result_message.ListAvailableSolutionStacksResultMessage":
        """<p>Returns a list of the available solution stack names, with the public version first and then in reverse chronological order.</p> <p>This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view solution stacks
            The following operation lists solution stacks for all currently available platform configurations and any that you have used in the past:

            >>> await client.list_available_solution_stacks()
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.list_available_solution_stacks_result_message.ListAvailableSolutionStacksResultMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.list_available_solution_stacks

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.list_available_solution_stacks.async_list_available_solution_stacks(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_platform_branches(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        filters: Optional[
            "capo_elastic_beanstalk.types.search_filters.SearchFilters"
        ] = None,
        max_records: Optional[
            "capo_elastic_beanstalk.types.platform_branch_max_records.PlatformBranchMaxRecords"
        ] = None,
        next_token: Optional["capo_elastic_beanstalk.types.token.Token"] = None,
    ) -> "capo_elastic_beanstalk.types.list_platform_branches_result.ListPlatformBranchesResult":
        """<p>Lists the platform branches available for your account in an Amazon Web Services Region. Provides summary information about each platform branch.</p> <p>For definitions of platform branch and other platform-related terms, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html">Elastic Beanstalk Platforms Glossary</a>.</p> <p>This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Args:
            filters: <p>Criteria for restricting the resulting list of platform branches. The filter is evaluated as a logical conjunction (AND) of the separate <code>SearchFilter</code> terms.</p> <p>The following list shows valid attribute values for each of the <code>SearchFilter</code> terms. Most operators take a single value. The <code>in</code> and <code>not_in</code> operators can take multiple values.</p> <ul> <li> <p> <code>Attribute = BranchName</code>:</p> <ul> <li> <p> <code>Operator</code>: <code>=</code> | <code>!=</code> | <code>begins_with</code> | <code>ends_with</code> | <code>contains</code> | <code>in</code> | <code>not_in</code> </p> </li> </ul> </li> <li> <p> <code>Attribute = LifecycleState</code>:</p> <ul> <li> <p> <code>Operator</code>: <code>=</code> | <code>!=</code> | <code>in</code> | <code>not_in</code> </p> </li> <li> <p> <code>Values</code>: <code>beta</code> | <code>supported</code> | <code>deprecated</code> | <code>retired</code> </p> </li> </ul> </li> <li> <p> <code>Attribute = PlatformName</code>:</p> <ul> <li> <p> <code>Operator</code>: <code>=</code> | <code>!=</code> | <code>begins_with</code> | <code>ends_with</code> | <code>contains</code> | <code>in</code> | <code>not_in</code> </p> </li> </ul> </li> <li> <p> <code>Attribute = TierType</code>:</p> <ul> <li> <p> <code>Operator</code>: <code>=</code> | <code>!=</code> </p> </li> <li> <p> <code>Values</code>: <code>WebServer/Standard</code> | <code>Worker/SQS/HTTP</code> </p> </li> </ul> </li> </ul> <p>Array size: limited to 10 <code>SearchFilter</code> objects.</p> <p>Within each <code>SearchFilter</code> item, the <code>Values</code> array is limited to 10 items.</p>
            max_records: <p>The maximum number of platform branch values returned in one call.</p>
            next_token: <p>For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If no <code>NextToken</code> is specified, the first page is retrieved.</p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.list_platform_branches_request.ListPlatformBranchesRequest]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.list_platform_branches_result.ListPlatformBranchesResult"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.list_platform_branches

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.list_platform_branches.async_list_platform_branches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.list_platform_branches_request.ListPlatformBranchesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_platform_branches(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        filters: Optional[
            "capo_elastic_beanstalk.types.search_filters.SearchFilters"
        ] = None,
        max_records: Optional[
            "capo_elastic_beanstalk.types.platform_branch_max_records.PlatformBranchMaxRecords"
        ] = None,
        next_token: Optional["capo_elastic_beanstalk.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_elastic_beanstalk.types.list_platform_branches_result.ListPlatformBranchesResult]":
        _token = next_token
        while True:
            _response = await self.list_platform_branches(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_platform_versions(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        filters: Optional[
            "capo_elastic_beanstalk.types.platform_filters.PlatformFilters"
        ] = None,
        max_records: Optional[
            "capo_elastic_beanstalk.types.platform_max_records.PlatformMaxRecords"
        ] = None,
        next_token: Optional["capo_elastic_beanstalk.types.token.Token"] = None,
    ) -> "capo_elastic_beanstalk.types.list_platform_versions_result.ListPlatformVersionsResult":
        """<p>Lists the platform versions available for your account in an Amazon Web Services Region. Provides summary information about each platform version. Compare to <a>DescribePlatformVersion</a>, which provides full details about a single platform version.</p> <p>This action only returns information about platform versions that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of ten platform versions. When the user calls the <i>ListPlatformVersions</i> action, the response will only include the one platform version that the user has permission to access instead of all ten platform versions. If the user doesn’t have access to any of the platform versions an empty result is returned.</p> <note> <p>The <i>AWSElasticBeanstalkReadOnly</i> managed policy allows operators to view information about resources related to Elastic Beanstalk environments. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note> <p>For definitions of platform version and other platform-related terms, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html">Elastic Beanstalk Platforms Glossary</a>.</p>

        Args:
            filters: <p>Criteria for restricting the resulting list of platform versions. The filter is interpreted as a logical conjunction (AND) of the separate <code>PlatformFilter</code> terms.</p>
            max_records: <p>The maximum number of platform version values returned in one call.</p>
            next_token: <p>For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If no <code>NextToken</code> is specified, the first page is retrieved.</p>

        Raises:
            capo_elastic_beanstalk.errors.elastic_beanstalk_service_exception.ElasticBeanstalkServiceException: <p>A generic service exception has occurred.</p>
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.list_platform_versions_request.ListPlatformVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.list_platform_versions_result.ListPlatformVersionsResult"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.list_platform_versions

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.list_platform_versions.async_list_platform_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.list_platform_versions_request.ListPlatformVersionsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_platform_versions(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        filters: Optional[
            "capo_elastic_beanstalk.types.platform_filters.PlatformFilters"
        ] = None,
        max_records: Optional[
            "capo_elastic_beanstalk.types.platform_max_records.PlatformMaxRecords"
        ] = None,
        next_token: Optional["capo_elastic_beanstalk.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_elastic_beanstalk.types.platform_summary.PlatformSummary]":
        _token = next_token
        while True:
            _response = await self.list_platform_versions(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("platform_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_elastic_beanstalk.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
    ) -> "capo_elastic_beanstalk.types.resource_tags_description_message.ResourceTagsDescriptionMessage":
        """<p>Return the tags applied to an Elastic Beanstalk resource. The response contains a list of tag key-value pairs.</p> <p>Elastic Beanstalk supports tagging of all of its resources. For details about resource tagging, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html">Tagging Application Resources</a>.</p> <p>This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.</p> <note> <p>The <a href="https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html">AWSElasticBeanstalkReadOnly</a> managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html"> Managing Elastic Beanstalk user policies</a> in the <i>Elastic Beanstalk Developer Guide</i>. For detailed instructions to attach a policy to a user or group, see the section <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed"> Controlling access with managed policies</a> in the same topic.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resouce for which a tag list is requested.</p> <p>Must be the ARN of an Elastic Beanstalk resource.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN).</p>
            capo_elastic_beanstalk.errors.resource_type_not_supported_exception.ResourceTypeNotSupportedException: <p>The type of the specified Amazon Resource Name (ARN) isn't supported for this operation.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.list_tags_for_resource_message.ListTagsForResourceMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.resource_tags_description_message.ResourceTagsDescriptionMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.list_tags_for_resource_message.ListTagsForResourceMessage = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def rebuild_environment(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
    ) -> None:
        """<p>Deletes and recreates all of the Amazon Web Services resources (for example: the Auto Scaling group, load balancer, etc.) for a specified environment and forces a restart.</p>

        Args:
            environment_id: <p>The ID of the environment to rebuild.</p> <p> Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>
            environment_name: <p>The name of the environment to rebuild.</p> <p> Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To rebuild an environment
            The following operation terminates and recreates the resources in an environment named my-env:

            >>> await client.rebuild_environment(environment_name='my-env')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.rebuild_environment_message.RebuildEnvironmentMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.rebuild_environment

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.rebuild_environment.async_rebuild_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.rebuild_environment_message.RebuildEnvironmentMessage = {}
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if environment_name is not None:
            input_["environment_name"] = environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def request_environment_info(
        self,
        info_type: "capo_elastic_beanstalk.types.environment_info_type.EnvironmentInfoType",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
    ) -> None:
        """<p>Initiates a request to compile the specified type of information of the deployed environment.</p> <p> Setting the <code>InfoType</code> to <code>tail</code> compiles the last lines from the application server log files of every Amazon EC2 instance in your environment. </p> <p> Setting the <code>InfoType</code> to <code>bundle</code> compresses the application server log files for every Amazon EC2 instance into a <code>.zip</code> file. Legacy and .NET containers do not support bundle logs. </p> <p> Setting the <code>InfoType</code> to <code>analyze</code> collects recent events, instance health, and logs from your environment and sends them to Amazon Bedrock in your account to generate diagnostic insights and recommended next steps. </p> <p> Use <a>RetrieveEnvironmentInfo</a> to obtain the set of logs. </p> <p>Related Topics</p> <ul> <li> <p> <a>RetrieveEnvironmentInfo</a> </p> </li> </ul>

        Args:
            environment_id: <p>The ID of the environment of the requested data.</p> <p>If no such environment is found, <code>RequestEnvironmentInfo</code> returns an <code>InvalidParameterValue</code> error. </p> <p>Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>
            environment_name: <p>The name of the environment of the requested data.</p> <p>If no such environment is found, <code>RequestEnvironmentInfo</code> returns an <code>InvalidParameterValue</code> error. </p> <p>Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>
            info_type: <p>The type of information to request.</p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To request tailed logs
            The following operation requests logs from an environment named my-env:

            >>> await client.request_environment_info(environment_name='my-env', info_type='tail')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.request_environment_info_message.RequestEnvironmentInfoMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.request_environment_info

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.request_environment_info.async_request_environment_info(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.request_environment_info_message.RequestEnvironmentInfoMessage = {
            "info_type": info_type
        }
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if environment_name is not None:
            input_["environment_name"] = environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restart_app_server(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
    ) -> None:
        """<p>Causes the environment to restart the application container server running on each Amazon EC2 instance.</p>

        Args:
            environment_id: <p>The ID of the environment to restart the server for.</p> <p> Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>
            environment_name: <p>The name of the environment to restart the server for.</p> <p> Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To restart application servers
            The following operation restarts application servers on all instances in an environment named my-env:

            >>> await client.restart_app_server(environment_name='my-env')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.restart_app_server_message.RestartAppServerMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.restart_app_server

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.restart_app_server.async_restart_app_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.restart_app_server_message.RestartAppServerMessage = {}
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if environment_name is not None:
            input_["environment_name"] = environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retrieve_environment_info(
        self,
        info_type: "capo_elastic_beanstalk.types.environment_info_type.EnvironmentInfoType",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.retrieve_environment_info_result_message.RetrieveEnvironmentInfoResultMessage":
        """<p>Retrieves the compiled information from a <a>RequestEnvironmentInfo</a> request.</p> <p>Related Topics</p> <ul> <li> <p> <a>RequestEnvironmentInfo</a> </p> </li> </ul>

        Args:
            environment_id: <p>The ID of the data's environment.</p> <p>If no such environment is found, returns an <code>InvalidParameterValue</code> error.</p> <p>Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error.</p>
            environment_name: <p>The name of the data's environment.</p> <p> If no such environment is found, returns an <code>InvalidParameterValue</code> error. </p> <p> Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>
            info_type: <p>The type of information to retrieve.</p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve tailed logs
            The following operation retrieves a link to logs from an environment named my-env:

            >>> await client.retrieve_environment_info(environment_name='my-env', info_type='tail')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.retrieve_environment_info_message.RetrieveEnvironmentInfoMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.retrieve_environment_info_result_message.RetrieveEnvironmentInfoResultMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.retrieve_environment_info

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.retrieve_environment_info.async_retrieve_environment_info(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.retrieve_environment_info_message.RetrieveEnvironmentInfoMessage = {
            "info_type": info_type
        }
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if environment_name is not None:
            input_["environment_name"] = environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def swap_environment_cnam_es(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        source_environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        source_environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        destination_environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        destination_environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
    ) -> None:
        """<p>Swaps the CNAMEs of two environments.</p>

        Args:
            source_environment_id: <p>The ID of the source environment.</p> <p> Condition: You must specify at least the <code>SourceEnvironmentID</code> or the <code>SourceEnvironmentName</code>. You may also specify both. If you specify the <code>SourceEnvironmentId</code>, you must specify the <code>DestinationEnvironmentId</code>. </p>
            source_environment_name: <p>The name of the source environment.</p> <p> Condition: You must specify at least the <code>SourceEnvironmentID</code> or the <code>SourceEnvironmentName</code>. You may also specify both. If you specify the <code>SourceEnvironmentName</code>, you must specify the <code>DestinationEnvironmentName</code>. </p>
            destination_environment_id: <p>The ID of the destination environment.</p> <p> Condition: You must specify at least the <code>DestinationEnvironmentID</code> or the <code>DestinationEnvironmentName</code>. You may also specify both. You must specify the <code>SourceEnvironmentId</code> with the <code>DestinationEnvironmentId</code>. </p>
            destination_environment_name: <p>The name of the destination environment.</p> <p> Condition: You must specify at least the <code>DestinationEnvironmentID</code> or the <code>DestinationEnvironmentName</code>. You may also specify both. You must specify the <code>SourceEnvironmentName</code> with the <code>DestinationEnvironmentName</code>. </p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To swap environment CNAMES
            The following operation swaps the assigned subdomains of two environments:

            >>> await client.swap_environment_cnam_es(source_environment_name='my-env-blue', destination_environment_name='my-env-green')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.swap_environment_cnam_es_message.SwapEnvironmentCNAMEsMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.swap_environment_cnam_es

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.swap_environment_cnam_es.async_swap_environment_cnam_es(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.swap_environment_cnam_es_message.SwapEnvironmentCNAMEsMessage = {}
        if source_environment_id is not None:
            input_["source_environment_id"] = source_environment_id
        if source_environment_name is not None:
            input_["source_environment_name"] = source_environment_name
        if destination_environment_id is not None:
            input_["destination_environment_id"] = destination_environment_id
        if destination_environment_name is not None:
            input_["destination_environment_name"] = destination_environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def terminate_environment(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        terminate_resources: Optional[
            "capo_elastic_beanstalk.types.terminate_environment_resources.TerminateEnvironmentResources"
        ] = None,
        force_terminate: Optional[
            "capo_elastic_beanstalk.types.force_terminate.ForceTerminate"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.environment_description.EnvironmentDescription":
        """<p>Terminates the specified environment.</p>

        Args:
            environment_id: <p>The ID of the environment to terminate.</p> <p> Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>
            environment_name: <p>The name of the environment to terminate.</p> <p> Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>
            terminate_resources: <p>Indicates whether the associated Amazon Web Services resources should shut down when the environment is terminated:</p> <ul> <li> <p> <code>true</code>: The specified environment as well as the associated Amazon Web Services resources, such as Auto Scaling group and LoadBalancer, are terminated.</p> </li> <li> <p> <code>false</code>: Elastic Beanstalk resource management is removed from the environment, but the Amazon Web Services resources continue to operate.</p> </li> </ul> <p> For more information, see the <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/ug/"> Elastic Beanstalk User Guide. </a> </p> <p> Default: <code>true</code> </p> <p> Valid Values: <code>true</code> | <code>false</code> </p>
            force_terminate: <p>Terminates the target environment even if another environment in the same group is dependent on it.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To terminate an environment
            The following operation terminates an Elastic Beanstalk environment named my-env:

            >>> await client.terminate_environment(environment_name='my-env')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.terminate_environment_message.TerminateEnvironmentMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.environment_description.EnvironmentDescription"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.terminate_environment

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.terminate_environment.async_terminate_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.terminate_environment_message.TerminateEnvironmentMessage = {}
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if terminate_resources is not None:
            input_["terminate_resources"] = terminate_resources
        if force_terminate is not None:
            input_["force_terminate"] = force_terminate

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_application(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        description: Optional[
            "capo_elastic_beanstalk.types.description.Description"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.application_description_message.ApplicationDescriptionMessage":
        """<p>Updates the specified application to have the specified properties.</p> <note> <p>If a property (for example, <code>description</code>) is not provided, the value remains unchanged. To clear these properties, specify an empty string.</p> </note>

        Args:
            application_name: <p>The name of the application to update. If no such application is found, <code>UpdateApplication</code> returns an <code>InvalidParameterValue</code> error. </p>
            description: <p>A new description for the application.</p> <p>Default: If not specified, Elastic Beanstalk does not update the description.</p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To change an application's description
            The following operation updates the description of an application named my-app:

            >>> await client.update_application(application_name='my-app', description='my Elastic Beanstalk application')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.update_application_message.UpdateApplicationMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.application_description_message.ApplicationDescriptionMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_application

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.update_application_message.UpdateApplicationMessage = {
            "application_name": application_name
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_application_resource_lifecycle(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        resource_lifecycle_config: "capo_elastic_beanstalk.types.application_resource_lifecycle_config.ApplicationResourceLifecycleConfig",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
    ) -> "capo_elastic_beanstalk.types.application_resource_lifecycle_description_message.ApplicationResourceLifecycleDescriptionMessage":
        """<p>Modifies lifecycle settings for an application.</p>

        Args:
            application_name: <p>The name of the application.</p>
            resource_lifecycle_config: <p>The lifecycle configuration.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.update_application_resource_lifecycle_message.UpdateApplicationResourceLifecycleMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.application_resource_lifecycle_description_message.ApplicationResourceLifecycleDescriptionMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_application_resource_lifecycle

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_application_resource_lifecycle.async_update_application_resource_lifecycle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.update_application_resource_lifecycle_message.UpdateApplicationResourceLifecycleMessage = {
            "application_name": application_name,
            "resource_lifecycle_config": resource_lifecycle_config,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_application_version(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        version_label: "capo_elastic_beanstalk.types.version_label.VersionLabel",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        description: Optional[
            "capo_elastic_beanstalk.types.description.Description"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.application_version_description_message.ApplicationVersionDescriptionMessage":
        """<p>Updates the specified application version to have the specified properties.</p> <note> <p>If a property (for example, <code>description</code>) is not provided, the value remains unchanged. To clear properties, specify an empty string.</p> </note>

        Args:
            application_name: <p>The name of the application associated with this version.</p> <p> If no application is found with this name, <code>UpdateApplication</code> returns an <code>InvalidParameterValue</code> error.</p>
            version_label: <p>The name of the version to update.</p> <p>If no application version is found with this label, <code>UpdateApplication</code> returns an <code>InvalidParameterValue</code> error. </p>
            description: <p>A new description for this version.</p>

        Raises:
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To change an application version's description
            The following operation updates the description of an application version named 22a0-stage-150819_185942:

            >>> await client.update_application_version(application_name='my-app', version_label='22a0-stage-150819_185942', description='new description')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.update_application_version_message.UpdateApplicationVersionMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.application_version_description_message.ApplicationVersionDescriptionMessage"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_application_version

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_application_version.async_update_application_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.update_application_version_message.UpdateApplicationVersionMessage = {
            "application_name": application_name,
            "version_label": version_label,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configuration_template(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        template_name: "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        description: Optional[
            "capo_elastic_beanstalk.types.description.Description"
        ] = None,
        option_settings: Optional[
            "capo_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList"
        ] = None,
        options_to_remove: Optional[
            "capo_elastic_beanstalk.types.options_specifier_list.OptionsSpecifierList"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.configuration_settings_description.ConfigurationSettingsDescription":
        """<p>Updates the specified configuration template to have the specified properties or configuration option values.</p> <note> <p>If a property (for example, <code>ApplicationName</code>) is not provided, its value remains unchanged. To clear such properties, specify an empty string.</p> </note> <p>Related Topics</p> <ul> <li> <p> <a>DescribeConfigurationOptions</a> </p> </li> </ul>

        Args:
            application_name: <p>The name of the application associated with the configuration template to update.</p> <p> If no application is found with this name, <code>UpdateConfigurationTemplate</code> returns an <code>InvalidParameterValue</code> error. </p>
            template_name: <p>The name of the configuration template to update.</p> <p> If no configuration template is found with this name, <code>UpdateConfigurationTemplate</code> returns an <code>InvalidParameterValue</code> error. </p>
            description: <p>A new description for the configuration.</p>
            option_settings: <p>A list of configuration option settings to update with the new specified option value.</p>
            options_to_remove: <p>A list of configuration options to remove from the configuration set.</p> <p> Constraint: You can remove only <code>UserDefined</code> configuration options. </p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.too_many_buckets_exception.TooManyBucketsException: <p>The specified account has reached its limit of Amazon S3 buckets.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a configuration template
            The following operation removes the configured CloudWatch custom health metrics configuration ConfigDocument from a saved configuration template named my-template:

            >>> await client.update_configuration_template(application_name='my-app', template_name='my-template', options_to_remove=[{'Namespace': 'aws:elasticbeanstalk:healthreporting:system', 'OptionName': 'ConfigDocument'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.update_configuration_template_message.UpdateConfigurationTemplateMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.configuration_settings_description.ConfigurationSettingsDescription"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_configuration_template

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_configuration_template.async_update_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.update_configuration_template_message.UpdateConfigurationTemplateMessage = {
            "application_name": application_name,
            "template_name": template_name,
        }
        if description is not None:
            input_["description"] = description
        if option_settings is not None:
            input_["option_settings"] = option_settings
        if options_to_remove is not None:
            input_["options_to_remove"] = options_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_environment(
        self,
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        application_name: Optional[
            "capo_elastic_beanstalk.types.application_name.ApplicationName"
        ] = None,
        environment_id: Optional[
            "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
        group_name: Optional[
            "capo_elastic_beanstalk.types.group_name.GroupName"
        ] = None,
        description: Optional[
            "capo_elastic_beanstalk.types.description.Description"
        ] = None,
        tier: Optional[
            "capo_elastic_beanstalk.types.environment_tier.EnvironmentTier"
        ] = None,
        version_label: Optional[
            "capo_elastic_beanstalk.types.version_label.VersionLabel"
        ] = None,
        template_name: Optional[
            "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
        ] = None,
        solution_stack_name: Optional[
            "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
        ] = None,
        platform_arn: Optional[
            "capo_elastic_beanstalk.types.platform_arn.PlatformArn"
        ] = None,
        option_settings: Optional[
            "capo_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList"
        ] = None,
        options_to_remove: Optional[
            "capo_elastic_beanstalk.types.options_specifier_list.OptionsSpecifierList"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.environment_description.EnvironmentDescription":
        """<p>Updates the environment description, deploys a new application version, updates the configuration settings to an entirely new configuration template, or updates select configuration option values in the running environment.</p> <p> Attempting to update both the release and configuration is not allowed and Elastic Beanstalk returns an <code>InvalidParameterCombination</code> error. </p> <p> When updating the configuration settings to a new template or individual settings, a draft configuration is created and <a>DescribeConfigurationSettings</a> for this environment returns two setting descriptions with different <code>DeploymentStatus</code> values. </p>

        Args:
            application_name: <p>The name of the application with which the environment is associated.</p>
            environment_id: <p>The ID of the environment to update.</p> <p>If no environment with this ID exists, Elastic Beanstalk returns an <code>InvalidParameterValue</code> error.</p> <p>Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>
            environment_name: <p>The name of the environment to update. If no environment with this name exists, Elastic Beanstalk returns an <code>InvalidParameterValue</code> error. </p> <p>Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>
            group_name: <p>The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name or environment ID parameters. See <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html">Environment Manifest (env.yaml)</a> for details.</p>
            description: <p>If this parameter is specified, Elastic Beanstalk updates the description of this environment.</p>
            tier: <p>This specifies the tier to use to update the environment.</p> <p>Condition: At this time, if you change the tier version, name, or type, Elastic Beanstalk returns <code>InvalidParameterValue</code> error. </p>
            version_label: <p>If this parameter is specified, Elastic Beanstalk deploys the named application version to the environment. If no such application version is found, returns an <code>InvalidParameterValue</code> error. </p>
            template_name: <p>If this parameter is specified, Elastic Beanstalk deploys this configuration template to the environment. If no such configuration template is found, Elastic Beanstalk returns an <code>InvalidParameterValue</code> error. </p>
            solution_stack_name: <p>This specifies the platform version that the environment will run after the environment is updated.</p>
            platform_arn: <p>The ARN of the platform, if used.</p>
            option_settings: <p>If specified, Elastic Beanstalk updates the configuration set associated with the running environment and sets the specified configuration options to the requested value.</p>
            options_to_remove: <p>A list of custom user-defined configuration options to remove from the configuration set for this environment.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.too_many_buckets_exception.TooManyBucketsException: <p>The specified account has reached its limit of Amazon S3 buckets.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To configure option settings
            The following operation configures several options in the aws:elb:loadbalancer namespace:

            >>> await client.update_environment(environment_name='my-env', option_settings=[{'Namespace': 'aws:elb:healthcheck', 'OptionName': 'Interval', 'Value': '15'}, {'Namespace': 'aws:elb:healthcheck', 'OptionName': 'Timeout', 'Value': '8'}, {'Namespace': 'aws:elb:healthcheck', 'OptionName': 'HealthyThreshold', 'Value': '2'}, {'Namespace': 'aws:elb:healthcheck', 'OptionName': 'UnhealthyThreshold', 'Value': '3'}])
            To update an environment to a new version
            The following operation updates an environment named "my-env" to version "v2" of the application to which it belongs:

            >>> await client.update_environment(environment_name='my-env', version_label='v2')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.update_environment_message.UpdateEnvironmentMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.environment_description.EnvironmentDescription"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_environment

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_environment.async_update_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.update_environment_message.UpdateEnvironmentMessage = {}
        if application_name is not None:
            input_["application_name"] = application_name
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if group_name is not None:
            input_["group_name"] = group_name
        if description is not None:
            input_["description"] = description
        if tier is not None:
            input_["tier"] = tier
        if version_label is not None:
            input_["version_label"] = version_label
        if template_name is not None:
            input_["template_name"] = template_name
        if solution_stack_name is not None:
            input_["solution_stack_name"] = solution_stack_name
        if platform_arn is not None:
            input_["platform_arn"] = platform_arn
        if option_settings is not None:
            input_["option_settings"] = option_settings
        if options_to_remove is not None:
            input_["options_to_remove"] = options_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_tags_for_resource(
        self,
        resource_arn: "capo_elastic_beanstalk.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        tags_to_add: Optional["capo_elastic_beanstalk.types.tag_list.TagList"] = None,
        tags_to_remove: Optional[
            "capo_elastic_beanstalk.types.tag_key_list.TagKeyList"
        ] = None,
    ) -> None:
        """<p>Update the list of tags applied to an Elastic Beanstalk resource. Two lists can be passed: <code>TagsToAdd</code> for tags to add or update, and <code>TagsToRemove</code>.</p> <p>Elastic Beanstalk supports tagging of all of its resources. For details about resource tagging, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html">Tagging Application Resources</a>.</p> <p>If you create a custom policy to control permission to this operation, specify one of the following two virtual actions (or both) instead of the API operation name:</p> <dl> <dt>elasticbeanstalk:AddTags</dt> <dd> <p>Controls permission to call <code>UpdateTagsForResource</code> and pass a list of tags to add in the <code>TagsToAdd</code> parameter.</p> </dd> <dt>elasticbeanstalk:RemoveTags</dt> <dd> <p>Controls permission to call <code>UpdateTagsForResource</code> and pass a list of tag keys to remove in the <code>TagsToRemove</code> parameter.</p> </dd> </dl> <p>For details about creating a custom user policy, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#AWSHowTo.iam.policies">Creating a Custom User Policy</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resouce to be updated.</p> <p>Must be the ARN of an Elastic Beanstalk resource.</p>
            tags_to_add: <p>A list of tags to add or update. If a key of an existing tag is added, the tag's value is updated.</p> <p>Specify at least one of these parameters: <code>TagsToAdd</code>, <code>TagsToRemove</code>.</p>
            tags_to_remove: <p>A list of tag keys to remove. If a tag key doesn't exist, it is silently ignored.</p> <p>Specify at least one of these parameters: <code>TagsToAdd</code>, <code>TagsToRemove</code>.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.operation_in_progress_exception.OperationInProgressException: <p>Unable to perform the specified operation because another operation that effects an element in this activity is already in progress.</p>
            capo_elastic_beanstalk.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN).</p>
            capo_elastic_beanstalk.errors.resource_type_not_supported_exception.ResourceTypeNotSupportedException: <p>The type of the specified Amazon Resource Name (ARN) isn't supported for this operation.</p>
            capo_elastic_beanstalk.errors.too_many_tags_exception.TooManyTagsException: <p>The number of tags in the resource would exceed the number of tags that each resource can have.</p> <p>To calculate this, the operation considers both the number of tags the resource already has and the tags this operation would add if it succeeded.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.update_tags_for_resource_message.UpdateTagsForResourceMessage]",
        ) -> AsyncOperationResponse[None]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.update_tags_for_resource.async_update_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.update_tags_for_resource_message.UpdateTagsForResourceMessage = {
            "resource_arn": resource_arn
        }
        if tags_to_add is not None:
            input_["tags_to_add"] = tags_to_add
        if tags_to_remove is not None:
            input_["tags_to_remove"] = tags_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def validate_configuration_settings(
        self,
        application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName",
        option_settings: "capo_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList",
        *,
        config_overrides: Optional[AsyncElasticBeanstalkClientConfig] = None,
        template_name: Optional[
            "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
        ] = None,
        environment_name: Optional[
            "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
        ] = None,
    ) -> "capo_elastic_beanstalk.types.configuration_settings_validation_messages.ConfigurationSettingsValidationMessages":
        """<p>Takes a set of configuration settings and either a configuration template or environment, and determines whether those values are valid.</p> <p>This action returns a list of messages indicating any errors or warnings associated with the selection of option values.</p>

        Args:
            application_name: <p>The name of the application that the configuration template or environment belongs to.</p>
            template_name: <p>The name of the configuration template to validate the settings against.</p> <p>Condition: You cannot specify both this and an environment name.</p>
            environment_name: <p>The name of the environment to validate the settings against.</p> <p>Condition: You cannot specify both this and a configuration template name.</p>
            option_settings: <p>A list of the options and desired values to evaluate.</p>

        Raises:
            capo_elastic_beanstalk.errors.insufficient_privileges_exception.InsufficientPrivilegesException: <p>The specified account does not have sufficient privileges for one or more Amazon Web Services services.</p>
            capo_elastic_beanstalk.errors.too_many_buckets_exception.TooManyBucketsException: <p>The specified account has reached its limit of Amazon S3 buckets.</p>
            capo_elastic_beanstalk.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To validate configuration settings
            The following operation validates a CloudWatch custom metrics config document:

            >>> await client.validate_configuration_settings(application_name='my-app', environment_name='my-env', option_settings=[{'Namespace': 'aws:elasticbeanstalk:healthreporting:system', 'OptionName': 'ConfigDocument', 'Value': '{"CloudWatchMetrics": {"Environment": {"ApplicationLatencyP99.9": null,"InstancesSevere": 60,"ApplicationLatencyP90": 60,"ApplicationLatencyP99": null,"ApplicationLatencyP95": 60,"InstancesUnknown": 60,"ApplicationLatencyP85": 60,"InstancesInfo": null,"ApplicationRequests2xx": null,"InstancesDegraded": null,"InstancesWarning": 60,"ApplicationLatencyP50": 60,"ApplicationRequestsTotal": null,"InstancesNoData": null,"InstancesPending": 60,"ApplicationLatencyP10": null,"ApplicationRequests5xx": null,"ApplicationLatencyP75": null,"InstancesOk": 60,"ApplicationRequests3xx": null,"ApplicationRequests4xx": null},"Instance": {"ApplicationLatencyP99.9": null,"ApplicationLatencyP90": 60,"ApplicationLatencyP99": null,"ApplicationLatencyP95": null,"ApplicationLatencyP85": null,"CPUUser": 60,"ApplicationRequests2xx": null,"CPUIdle": null,"ApplicationLatencyP50": null,"ApplicationRequestsTotal": 60,"RootFilesystemUtil": null,"LoadAverage1min": null,"CPUIrq": null,"CPUNice": 60,"CPUIowait": 60,"ApplicationLatencyP10": null,"LoadAverage5min": null,"ApplicationRequests5xx": null,"ApplicationLatencyP75": 60,"CPUSystem": 60,"ApplicationRequests3xx": 60,"ApplicationRequests4xx": null,"InstanceHealth": null,"CPUSoftirq": 60}},"Version": 1}'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_elastic_beanstalk.types.validate_configuration_settings_message.ValidateConfigurationSettingsMessage]",
        ) -> AsyncOperationResponse[
            "capo_elastic_beanstalk.types.configuration_settings_validation_messages.ConfigurationSettingsValidationMessages"
        ]:
            import capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.validate_configuration_settings

            (
                output,
                http_response,
            ) = await capo_elastic_beanstalk._operations.aws_elastic_beanstalk_service.validate_configuration_settings.async_validate_configuration_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elastic_beanstalk.types.validate_configuration_settings_message.ValidateConfigurationSettingsMessage = {
            "application_name": application_name,
            "option_settings": option_settings,
        }
        if template_name is not None:
            input_["template_name"] = template_name
        if environment_name is not None:
            input_["environment_name"] = environment_name

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
