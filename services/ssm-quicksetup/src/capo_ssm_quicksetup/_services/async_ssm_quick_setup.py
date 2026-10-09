"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#QuickSetup``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_ssm_quicksetup._auth._signers
import capo_ssm_quicksetup._auth._sigv4
from capo_ssm_quicksetup._auth._identity import Credentials
from capo_ssm_quicksetup._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ssm_quicksetup._auth._zapros_handler import AuthMiddleware
from capo_ssm_quicksetup._pagination import resolve_path as _resolve_path
from capo_ssm_quicksetup._services._aws_config import aaws_config
from capo_ssm_quicksetup._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.configuration_definitions_input_list
    import capo_ssm_quicksetup.types.configuration_manager_summary
    import capo_ssm_quicksetup.types.configuration_parameters_map
    import capo_ssm_quicksetup.types.configuration_summary
    import capo_ssm_quicksetup.types.create_configuration_manager_input
    import capo_ssm_quicksetup.types.create_configuration_manager_output
    import capo_ssm_quicksetup.types.delete_configuration_manager_input
    import capo_ssm_quicksetup.types.filters_list
    import capo_ssm_quicksetup.types.get_configuration_input
    import capo_ssm_quicksetup.types.get_configuration_manager_input
    import capo_ssm_quicksetup.types.get_configuration_manager_output
    import capo_ssm_quicksetup.types.get_configuration_output
    import capo_ssm_quicksetup.types.get_service_settings_output
    import capo_ssm_quicksetup.types.iam_role_arn
    import capo_ssm_quicksetup.types.list_configuration_managers_input
    import capo_ssm_quicksetup.types.list_configuration_managers_output
    import capo_ssm_quicksetup.types.list_configurations_input
    import capo_ssm_quicksetup.types.list_configurations_output
    import capo_ssm_quicksetup.types.list_quick_setup_types_output
    import capo_ssm_quicksetup.types.list_tags_for_resource_request
    import capo_ssm_quicksetup.types.list_tags_for_resource_response
    import capo_ssm_quicksetup.types.tag_keys
    import capo_ssm_quicksetup.types.tag_resource_input
    import capo_ssm_quicksetup.types.tags_map
    import capo_ssm_quicksetup.types.untag_resource_input
    import capo_ssm_quicksetup.types.update_configuration_definition_input
    import capo_ssm_quicksetup.types.update_configuration_manager_input
    import capo_ssm_quicksetup.types.update_service_settings_input


class AsyncSSMQuickSetupClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSSMQuickSetupClient:
    """A client for the ``SSMQuickSetup`` service.

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
        self._config = AsyncSSMQuickSetupClientConfig(
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
        self, config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSSMQuickSetupClientConfig = config_overrides or {}
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

    async def create_configuration_manager(
        self,
        configuration_definitions: "capo_ssm_quicksetup.types.configuration_definitions_input_list.ConfigurationDefinitionsInputList",
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional["capo_ssm_quicksetup.types.tags_map.TagsMap"] = None,
    ) -> "capo_ssm_quicksetup.types.create_configuration_manager_output.CreateConfigurationManagerOutput":
        """<p>Creates a Quick Setup configuration manager resource. This object is a collection of desired state configurations for multiple configuration definitions and summaries describing the deployments of those definitions.</p>

        Args:
            name: <p>A name for the configuration manager.</p>
            description: <p>A description of the configuration manager.</p>
            configuration_definitions: <p>The definition of the Quick Setup configuration that the configuration manager deploys.</p>
            tags: <p>Key-value pairs of metadata to assign to the configuration manager.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.create_configuration_manager_input.CreateConfigurationManagerInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_quicksetup.types.create_configuration_manager_output.CreateConfigurationManagerOutput"
        ]:
            import capo_ssm_quicksetup._operations.quick_setup.create_configuration_manager

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.create_configuration_manager.async_create_configuration_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.create_configuration_manager_input.CreateConfigurationManagerInput = {
            "configuration_definitions": configuration_definitions
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_manager(
        self,
        manager_arn: str,
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
    ) -> None:
        """<p>Deletes a configuration manager.</p>

        Args:
            manager_arn: <p>The ID of the configuration manager.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. Check the ID or name and try again.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.delete_configuration_manager_input.DeleteConfigurationManagerInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_ssm_quicksetup._operations.quick_setup.delete_configuration_manager

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.delete_configuration_manager.async_delete_configuration_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.delete_configuration_manager_input.DeleteConfigurationManagerInput = {
            "manager_arn": manager_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configuration(
        self,
        configuration_id: str,
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
    ) -> "capo_ssm_quicksetup.types.get_configuration_output.GetConfigurationOutput":
        """<p>Returns details about the specified configuration.</p>

        Args:
            configuration_id: <p>A service generated identifier for the configuration.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. Check the ID or name and try again.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.get_configuration_input.GetConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_quicksetup.types.get_configuration_output.GetConfigurationOutput"
        ]:
            import capo_ssm_quicksetup._operations.quick_setup.get_configuration

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.get_configuration.async_get_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.get_configuration_input.GetConfigurationInput = {
            "configuration_id": configuration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configuration_manager(
        self,
        manager_arn: str,
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
    ) -> "capo_ssm_quicksetup.types.get_configuration_manager_output.GetConfigurationManagerOutput":
        """<p>Returns a configuration manager.</p>

        Args:
            manager_arn: <p>The ARN of the configuration manager.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. Check the ID or name and try again.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.get_configuration_manager_input.GetConfigurationManagerInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_quicksetup.types.get_configuration_manager_output.GetConfigurationManagerOutput"
        ]:
            import capo_ssm_quicksetup._operations.quick_setup.get_configuration_manager

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.get_configuration_manager.async_get_configuration_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.get_configuration_manager_input.GetConfigurationManagerInput = {
            "manager_arn": manager_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_settings(
        self, *, config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None
    ) -> (
        "capo_ssm_quicksetup.types.get_service_settings_output.GetServiceSettingsOutput"
    ):
        """<p>Returns settings configured for Quick Setup in the requesting Amazon Web Services account and Amazon Web Services Region.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_ssm_quicksetup.types.get_service_settings_output.GetServiceSettingsOutput"
        ]:
            import capo_ssm_quicksetup._operations.quick_setup.get_service_settings

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.get_service_settings.async_get_service_settings(
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

    async def list_configuration_managers(
        self,
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
        starting_token: Optional[str] = None,
        max_items: Optional[int] = None,
        filters: Optional["capo_ssm_quicksetup.types.filters_list.FiltersList"] = None,
    ) -> "capo_ssm_quicksetup.types.list_configuration_managers_output.ListConfigurationManagersOutput":
        """<p>Returns Quick Setup configuration managers.</p>

        Args:
            starting_token: <p>The token to use when requesting a specific set of items from a list.</p>
            max_items: <p>Specifies the maximum number of configuration managers that are returned by the request.</p>
            filters: <p>Filters the results returned by the request.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.list_configuration_managers_input.ListConfigurationManagersInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_quicksetup.types.list_configuration_managers_output.ListConfigurationManagersOutput"
        ]:
            import capo_ssm_quicksetup._operations.quick_setup.list_configuration_managers

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.list_configuration_managers.async_list_configuration_managers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.list_configuration_managers_input.ListConfigurationManagersInput = {}
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_items is not None:
            input_["max_items"] = max_items
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_configuration_managers(
        self,
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
        starting_token: Optional[str] = None,
        max_items: Optional[int] = None,
        filters: Optional["capo_ssm_quicksetup.types.filters_list.FiltersList"] = None,
    ) -> "AsyncIterator[capo_ssm_quicksetup.types.configuration_manager_summary.ConfigurationManagerSummary]":
        _token = starting_token
        while True:
            _response = await self.list_configuration_managers(
                config_overrides=config_overrides,
                starting_token=_token,
                max_items=max_items,
                filters=filters,
            )
            _page = _resolve_path(_response, ("configuration_managers_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_configurations(
        self,
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
        starting_token: Optional[str] = None,
        max_items: Optional[int] = None,
        filters: Optional["capo_ssm_quicksetup.types.filters_list.FiltersList"] = None,
        manager_arn: Optional[str] = None,
        configuration_definition_id: Optional[str] = None,
    ) -> (
        "capo_ssm_quicksetup.types.list_configurations_output.ListConfigurationsOutput"
    ):
        """<p>Returns configurations deployed by Quick Setup in the requesting Amazon Web Services account and Amazon Web Services Region.</p>

        Args:
            starting_token: <p>The token to use when requesting a specific set of items from a list.</p>
            max_items: <p>Specifies the maximum number of configurations that are returned by the request.</p>
            filters: <p>Filters the results returned by the request.</p>
            manager_arn: <p>The ARN of the configuration manager.</p>
            configuration_definition_id: <p>The ID of the configuration definition.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. Check the ID or name and try again.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.list_configurations_input.ListConfigurationsInput]",
        ) -> AsyncOperationResponse[
            "capo_ssm_quicksetup.types.list_configurations_output.ListConfigurationsOutput"
        ]:
            import capo_ssm_quicksetup._operations.quick_setup.list_configurations

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.list_configurations.async_list_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.list_configurations_input.ListConfigurationsInput = {}
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_items is not None:
            input_["max_items"] = max_items
        if filters is not None:
            input_["filters"] = filters
        if manager_arn is not None:
            input_["manager_arn"] = manager_arn
        if configuration_definition_id is not None:
            input_["configuration_definition_id"] = configuration_definition_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_configurations(
        self,
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
        starting_token: Optional[str] = None,
        max_items: Optional[int] = None,
        filters: Optional["capo_ssm_quicksetup.types.filters_list.FiltersList"] = None,
        manager_arn: Optional[str] = None,
        configuration_definition_id: Optional[str] = None,
    ) -> "AsyncIterator[capo_ssm_quicksetup.types.configuration_summary.ConfigurationSummary]":
        _token = starting_token
        while True:
            _response = await self.list_configurations(
                config_overrides=config_overrides,
                starting_token=_token,
                max_items=max_items,
                filters=filters,
                manager_arn=manager_arn,
                configuration_definition_id=configuration_definition_id,
            )
            _page = _resolve_path(_response, ("configurations_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_quick_setup_types(
        self, *, config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None
    ) -> "capo_ssm_quicksetup.types.list_quick_setup_types_output.ListQuickSetupTypesOutput":
        """<p>Returns the available Quick Setup types.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_ssm_quicksetup.types.list_quick_setup_types_output.ListQuickSetupTypesOutput"
        ]:
            import capo_ssm_quicksetup._operations.quick_setup.list_quick_setup_types

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.list_quick_setup_types.async_list_quick_setup_types(
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

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
    ) -> "capo_ssm_quicksetup.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns tags assigned to the resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource the tag is assigned to.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. Check the ID or name and try again.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm_quicksetup.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_ssm_quicksetup._operations.quick_setup.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        tags: "capo_ssm_quicksetup.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
    ) -> None:
        """<p>Assigns key-value pairs of metadata to Amazon Web Services resources.</p>

        Args:
            resource_arn: <p>The ARN of the resource to tag.</p>
            tags: <p>Key-value pairs of metadata to assign to the resource.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. Check the ID or name and try again.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_ssm_quicksetup._operations.quick_setup.tag_resource

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.tag_resource_input.TagResourceInput = {
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
        tag_keys: "capo_ssm_quicksetup.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
    ) -> None:
        """<p>Removes tags from the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to remove tags from.</p>
            tag_keys: <p>The keys of the tags to remove from the resource.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. Check the ID or name and try again.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_ssm_quicksetup._operations.quick_setup.untag_resource

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.untag_resource_input.UntagResourceInput = {
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

    async def update_configuration_definition(
        self,
        manager_arn: str,
        id: str,
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
        type_version: Optional[str] = None,
        parameters: Optional[
            "capo_ssm_quicksetup.types.configuration_parameters_map.ConfigurationParametersMap"
        ] = None,
        local_deployment_execution_role_name: Optional[str] = None,
        local_deployment_administration_role_arn: Optional[
            "capo_ssm_quicksetup.types.iam_role_arn.IAMRoleArn"
        ] = None,
    ) -> None:
        """<p>Updates a Quick Setup configuration definition.</p>

        Args:
            manager_arn: <p>The ARN of the configuration manager associated with the definition to update.</p>
            id: <p>The ID of the configuration definition you want to update.</p>
            type_version: <p>The version of the Quick Setup type to use.</p>
            parameters: <p>The parameters for the configuration definition type.</p>
            local_deployment_execution_role_name: <p>The name of the IAM role used to deploy local configurations.</p>
            local_deployment_administration_role_arn: <p>The ARN of the IAM role used to administrate local configuration deployments.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. Check the ID or name and try again.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.update_configuration_definition_input.UpdateConfigurationDefinitionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_ssm_quicksetup._operations.quick_setup.update_configuration_definition

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.update_configuration_definition.async_update_configuration_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.update_configuration_definition_input.UpdateConfigurationDefinitionInput = {
            "manager_arn": manager_arn,
            "id": id,
        }
        if type_version is not None:
            input_["type_version"] = type_version
        if parameters is not None:
            input_["parameters"] = parameters
        if local_deployment_execution_role_name is not None:
            input_["local_deployment_execution_role_name"] = (
                local_deployment_execution_role_name
            )
        if local_deployment_administration_role_arn is not None:
            input_["local_deployment_administration_role_arn"] = (
                local_deployment_administration_role_arn
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configuration_manager(
        self,
        manager_arn: str,
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        """<p>Updates a Quick Setup configuration manager.</p>

        Args:
            manager_arn: <p>The ARN of the configuration manager.</p>
            name: <p>A name for the configuration manager.</p>
            description: <p>A description of the configuration manager.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. Check the ID or name and try again.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.update_configuration_manager_input.UpdateConfigurationManagerInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_ssm_quicksetup._operations.quick_setup.update_configuration_manager

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.update_configuration_manager.async_update_configuration_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.update_configuration_manager_input.UpdateConfigurationManagerInput = {
            "manager_arn": manager_arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service_settings(
        self,
        *,
        config_overrides: Optional[AsyncSSMQuickSetupClientConfig] = None,
        explorer_enabling_role_arn: Optional[
            "capo_ssm_quicksetup.types.iam_role_arn.IAMRoleArn"
        ] = None,
    ) -> None:
        """<p>Updates settings configured for Quick Setup.</p>

        Args:
            explorer_enabling_role_arn: <p>The IAM role used to enable Explorer.</p>

        Raises:
            capo_ssm_quicksetup.errors.access_denied_exception.AccessDeniedException: <p>The requester has insufficient permissions to perform the operation.</p>
            capo_ssm_quicksetup.errors.conflict_exception.ConflictException: <p>Another request is being processed. Wait a few minutes and try again.</p>
            capo_ssm_quicksetup.errors.internal_server_exception.InternalServerException: <p>An error occurred on the server side.</p>
            capo_ssm_quicksetup.errors.throttling_exception.ThrottlingException: <p>The request or operation exceeds the maximum allowed request rate per Amazon Web Services account and Amazon Web Services Region.</p>
            capo_ssm_quicksetup.errors.validation_exception.ValidationException: <p>The request is invalid. Verify the values provided for the request parameters are accurate.</p>
            capo_ssm_quicksetup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_quicksetup.types.update_service_settings_input.UpdateServiceSettingsInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_ssm_quicksetup._operations.quick_setup.update_service_settings

            (
                output,
                http_response,
            ) = await capo_ssm_quicksetup._operations.quick_setup.update_service_settings.async_update_service_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_quicksetup.types.update_service_settings_input.UpdateServiceSettingsInput = {}
        if explorer_enabling_role_arn is not None:
            input_["explorer_enabling_role_arn"] = explorer_enabling_role_arn

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
