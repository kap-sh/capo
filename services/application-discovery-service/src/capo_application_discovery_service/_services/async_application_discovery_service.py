"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#AWSPoseidonService_V2015_11_01``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_application_discovery_service._auth._signers
import capo_application_discovery_service._auth._sigv4
from capo_application_discovery_service._auth._identity import Credentials
from capo_application_discovery_service._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_application_discovery_service._auth._zapros_handler import AuthMiddleware
from capo_application_discovery_service._pagination import resolve_path as _resolve_path
from capo_application_discovery_service._services._aws_config import aaws_config
from capo_application_discovery_service._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_application_discovery_service.types.agent_ids
    import capo_application_discovery_service.types.agent_info
    import capo_application_discovery_service.types.application_description
    import capo_application_discovery_service.types.application_id
    import capo_application_discovery_service.types.application_ids_list
    import capo_application_discovery_service.types.application_name
    import capo_application_discovery_service.types.application_wave
    import capo_application_discovery_service.types.associate_configuration_items_to_application_request
    import capo_application_discovery_service.types.associate_configuration_items_to_application_response
    import capo_application_discovery_service.types.batch_delete_agents_request
    import capo_application_discovery_service.types.batch_delete_agents_response
    import capo_application_discovery_service.types.batch_delete_import_data_request
    import capo_application_discovery_service.types.batch_delete_import_data_response
    import capo_application_discovery_service.types.boolean
    import capo_application_discovery_service.types.client_request_token
    import capo_application_discovery_service.types.configuration
    import capo_application_discovery_service.types.configuration_id
    import capo_application_discovery_service.types.configuration_id_list
    import capo_application_discovery_service.types.configuration_item_type
    import capo_application_discovery_service.types.configuration_tag
    import capo_application_discovery_service.types.configurations_export_id
    import capo_application_discovery_service.types.continuous_export_description
    import capo_application_discovery_service.types.continuous_export_ids
    import capo_application_discovery_service.types.create_application_request
    import capo_application_discovery_service.types.create_application_response
    import capo_application_discovery_service.types.create_tags_request
    import capo_application_discovery_service.types.create_tags_response
    import capo_application_discovery_service.types.delete_agents
    import capo_application_discovery_service.types.delete_applications_request
    import capo_application_discovery_service.types.delete_applications_response
    import capo_application_discovery_service.types.delete_tags_request
    import capo_application_discovery_service.types.delete_tags_response
    import capo_application_discovery_service.types.deletion_configuration_item_type
    import capo_application_discovery_service.types.describe_agents_request
    import capo_application_discovery_service.types.describe_agents_response
    import capo_application_discovery_service.types.describe_batch_delete_configuration_task_request
    import capo_application_discovery_service.types.describe_batch_delete_configuration_task_response
    import capo_application_discovery_service.types.describe_configurations_request
    import capo_application_discovery_service.types.describe_configurations_response
    import capo_application_discovery_service.types.describe_continuous_exports_max_results
    import capo_application_discovery_service.types.describe_continuous_exports_request
    import capo_application_discovery_service.types.describe_continuous_exports_response
    import capo_application_discovery_service.types.describe_export_configurations_request
    import capo_application_discovery_service.types.describe_export_configurations_response
    import capo_application_discovery_service.types.describe_export_tasks_request
    import capo_application_discovery_service.types.describe_export_tasks_response
    import capo_application_discovery_service.types.describe_import_tasks_filter_list
    import capo_application_discovery_service.types.describe_import_tasks_max_results
    import capo_application_discovery_service.types.describe_import_tasks_request
    import capo_application_discovery_service.types.describe_import_tasks_response
    import capo_application_discovery_service.types.describe_tags_request
    import capo_application_discovery_service.types.describe_tags_response
    import capo_application_discovery_service.types.disassociate_configuration_items_from_application_request
    import capo_application_discovery_service.types.disassociate_configuration_items_from_application_response
    import capo_application_discovery_service.types.export_configurations_response
    import capo_application_discovery_service.types.export_data_formats
    import capo_application_discovery_service.types.export_filters
    import capo_application_discovery_service.types.export_ids
    import capo_application_discovery_service.types.export_info
    import capo_application_discovery_service.types.export_preferences
    import capo_application_discovery_service.types.filters
    import capo_application_discovery_service.types.get_discovery_summary_request
    import capo_application_discovery_service.types.get_discovery_summary_response
    import capo_application_discovery_service.types.import_task
    import capo_application_discovery_service.types.import_task_name
    import capo_application_discovery_service.types.import_url
    import capo_application_discovery_service.types.integer
    import capo_application_discovery_service.types.list_configurations_request
    import capo_application_discovery_service.types.list_configurations_response
    import capo_application_discovery_service.types.list_server_neighbors_request
    import capo_application_discovery_service.types.list_server_neighbors_response
    import capo_application_discovery_service.types.next_token
    import capo_application_discovery_service.types.order_by_list
    import capo_application_discovery_service.types.start_batch_delete_configuration_task_request
    import capo_application_discovery_service.types.start_batch_delete_configuration_task_response
    import capo_application_discovery_service.types.start_continuous_export_request
    import capo_application_discovery_service.types.start_continuous_export_response
    import capo_application_discovery_service.types.start_data_collection_by_agent_ids_request
    import capo_application_discovery_service.types.start_data_collection_by_agent_ids_response
    import capo_application_discovery_service.types.start_export_task_request
    import capo_application_discovery_service.types.start_export_task_response
    import capo_application_discovery_service.types.start_import_task_request
    import capo_application_discovery_service.types.start_import_task_response
    import capo_application_discovery_service.types.stop_continuous_export_request
    import capo_application_discovery_service.types.stop_continuous_export_response
    import capo_application_discovery_service.types.stop_data_collection_by_agent_ids_request
    import capo_application_discovery_service.types.stop_data_collection_by_agent_ids_response
    import capo_application_discovery_service.types.string
    import capo_application_discovery_service.types.tag_filters
    import capo_application_discovery_service.types.tag_set
    import capo_application_discovery_service.types.time_stamp
    import capo_application_discovery_service.types.to_delete_identifier_list
    import capo_application_discovery_service.types.update_application_request
    import capo_application_discovery_service.types.update_application_response
    import capo_application_discovery_service.types.uuid


class AsyncApplicationDiscoveryServiceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncApplicationDiscoveryServiceClient:
    """A client for the ``ApplicationDiscoveryService`` service.

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
        self._config = AsyncApplicationDiscoveryServiceClientConfig(
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
        self,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncApplicationDiscoveryServiceClientConfig = config_overrides or {}
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

    async def associate_configuration_items_to_application(
        self,
        application_configuration_id: "capo_application_discovery_service.types.application_id.ApplicationId",
        configuration_ids: "capo_application_discovery_service.types.configuration_id_list.ConfigurationIdList",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.associate_configuration_items_to_application_response.AssociateConfigurationItemsToApplicationResponse":
        """<p>Associates one or more configuration items with an application.</p>

        Args:
            application_configuration_id: <p>The configuration ID of an application with which items are to be associated.</p>
            configuration_ids: <p>The ID of each configuration item to be associated with an application.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.associate_configuration_items_to_application_request.AssociateConfigurationItemsToApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.associate_configuration_items_to_application_response.AssociateConfigurationItemsToApplicationResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.associate_configuration_items_to_application

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.associate_configuration_items_to_application.async_associate_configuration_items_to_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.associate_configuration_items_to_application_request.AssociateConfigurationItemsToApplicationRequest = {
            "application_configuration_id": application_configuration_id,
            "configuration_ids": configuration_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_agents(
        self,
        delete_agents: "capo_application_discovery_service.types.delete_agents.DeleteAgents",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.batch_delete_agents_response.BatchDeleteAgentsResponse":
        """<p> Deletes one or more agents or collectors as specified by ID. Deleting an agent or collector does not delete the previously discovered data. To delete the data collected, use <code>StartBatchDeleteConfigurationTask</code>. </p>

        Args:
            delete_agents: <p> The list of agents to delete. </p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.batch_delete_agents_request.BatchDeleteAgentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.batch_delete_agents_response.BatchDeleteAgentsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.batch_delete_agents

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.batch_delete_agents.async_batch_delete_agents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.batch_delete_agents_request.BatchDeleteAgentsRequest = {
            "delete_agents": delete_agents
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_import_data(
        self,
        import_task_ids: "capo_application_discovery_service.types.to_delete_identifier_list.ToDeleteIdentifierList",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        delete_history: Optional[
            "capo_application_discovery_service.types.boolean.Boolean"
        ] = None,
    ) -> "capo_application_discovery_service.types.batch_delete_import_data_response.BatchDeleteImportDataResponse":
        """<p>Deletes one or more import tasks, each identified by their import ID. Each import task has a number of records that can identify servers or applications. </p> <p>Amazon Web Services Application Discovery Service has built-in matching logic that will identify when discovered servers match existing entries that you've previously discovered, the information for the already-existing discovered server is updated. When you delete an import task that contains records that were used to match, the information in those matched records that comes from the deleted records will also be deleted.</p>

        Args:
            import_task_ids: <p>The IDs for the import tasks that you want to delete.</p>
            delete_history: <p> Set to <code>true</code> to remove the deleted import task from <a>DescribeImportTasks</a>. </p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.batch_delete_import_data_request.BatchDeleteImportDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.batch_delete_import_data_response.BatchDeleteImportDataResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.batch_delete_import_data

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.batch_delete_import_data.async_batch_delete_import_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.batch_delete_import_data_request.BatchDeleteImportDataRequest = {
            "import_task_ids": import_task_ids
        }
        if delete_history is not None:
            input_["delete_history"] = delete_history

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_application(
        self,
        name: "capo_application_discovery_service.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        description: Optional[
            "capo_application_discovery_service.types.application_description.ApplicationDescription"
        ] = None,
        wave: Optional[
            "capo_application_discovery_service.types.application_wave.ApplicationWave"
        ] = None,
    ) -> "capo_application_discovery_service.types.create_application_response.CreateApplicationResponse":
        """<p>Creates an application with the given name and description.</p>

        Args:
            name: <p>The name of the application to be created.</p>
            description: <p>The description of the application to be created.</p>
            wave: <p>The name of the migration wave of the application to be created.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.create_application

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.create_application_request.CreateApplicationRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if wave is not None:
            input_["wave"] = wave

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_tags(
        self,
        configuration_ids: "capo_application_discovery_service.types.configuration_id_list.ConfigurationIdList",
        tags: "capo_application_discovery_service.types.tag_set.TagSet",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.create_tags_response.CreateTagsResponse":
        """<p>Creates one or more tags for configuration items. Tags are metadata that help you categorize IT assets. This API accepts a list of multiple configuration items.</p> <important> <p>Do not store sensitive information (like personal data) in tags.</p> </important>

        Args:
            configuration_ids: <p>A list of configuration items that you want to tag.</p>
            tags: <p>Tags that you want to associate with one or more configuration items. Specify the tags that you want to create in a <i>key</i>-<i>value</i> format. For example:</p> <p> <code>{"key": "serverType", "value": "webServer"}</code> </p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified configuration ID was not located. Verify the configuration ID and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.create_tags_request.CreateTagsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.create_tags_response.CreateTagsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.create_tags

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.create_tags.async_create_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.create_tags_request.CreateTagsRequest = {
            "configuration_ids": configuration_ids,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_applications(
        self,
        configuration_ids: "capo_application_discovery_service.types.application_ids_list.ApplicationIdsList",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.delete_applications_response.DeleteApplicationsResponse":
        """<p>Deletes a list of applications and their associations with configuration items.</p>

        Args:
            configuration_ids: <p>Configuration ID of an application to be deleted.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.delete_applications_request.DeleteApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.delete_applications_response.DeleteApplicationsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.delete_applications

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.delete_applications.async_delete_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.delete_applications_request.DeleteApplicationsRequest = {
            "configuration_ids": configuration_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_tags(
        self,
        configuration_ids: "capo_application_discovery_service.types.configuration_id_list.ConfigurationIdList",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        tags: Optional[
            "capo_application_discovery_service.types.tag_set.TagSet"
        ] = None,
    ) -> "capo_application_discovery_service.types.delete_tags_response.DeleteTagsResponse":
        """<p>Deletes the association between configuration items and one or more tags. This API accepts a list of multiple configuration items.</p>

        Args:
            configuration_ids: <p>A list of configuration items with tags that you want to delete.</p>
            tags: <p>Tags that you want to delete from one or more configuration items. Specify the tags that you want to delete in a <i>key</i>-<i>value</i> format. For example:</p> <p> <code>{"key": "serverType", "value": "webServer"}</code> </p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified configuration ID was not located. Verify the configuration ID and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.delete_tags_request.DeleteTagsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.delete_tags_response.DeleteTagsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.delete_tags

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.delete_tags.async_delete_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.delete_tags_request.DeleteTagsRequest = {
            "configuration_ids": configuration_ids
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

    async def describe_agents(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        agent_ids: Optional[
            "capo_application_discovery_service.types.agent_ids.AgentIds"
        ] = None,
        filters: Optional[
            "capo_application_discovery_service.types.filters.Filters"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.integer.Integer"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_discovery_service.types.describe_agents_response.DescribeAgentsResponse":
        """<p>Lists agents or collectors as specified by ID or other filters. All agents/collectors associated with your user can be listed if you call <code>DescribeAgents</code> as is without passing any parameters.</p>

        Args:
            agent_ids: <p>The agent or the collector IDs for which you want information. If you specify no IDs, the system returns information about all agents/collectors associated with your user.</p>
            filters: <p>You can filter the request using various logical operators and a <i>key</i>-<i>value</i> format. For example: </p> <p> <code>{"key": "collectionStatus", "value": "STARTED"}</code> </p>
            max_results: <p>The total number of agents/collectors to return in a single page of output. The maximum value is 100.</p>
            next_token: <p>Token to retrieve the next set of results. For example, if you previously specified 100 IDs for <code>DescribeAgentsRequest$agentIds</code> but set <code>DescribeAgentsRequest$maxResults</code> to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.describe_agents_request.DescribeAgentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.describe_agents_response.DescribeAgentsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_agents

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_agents.async_describe_agents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.describe_agents_request.DescribeAgentsRequest = {}
        if agent_ids is not None:
            input_["agent_ids"] = agent_ids
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

    async def iter_describe_agents(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        agent_ids: Optional[
            "capo_application_discovery_service.types.agent_ids.AgentIds"
        ] = None,
        filters: Optional[
            "capo_application_discovery_service.types.filters.Filters"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.integer.Integer"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_application_discovery_service.types.agent_info.AgentInfo]":
        _token = next_token
        while True:
            _response = await self.describe_agents(
                config_overrides=config_overrides,
                agent_ids=agent_ids,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agents_info",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_batch_delete_configuration_task(
        self,
        task_id: "capo_application_discovery_service.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.describe_batch_delete_configuration_task_response.DescribeBatchDeleteConfigurationTaskResponse":
        """<p> Takes a unique deletion task identifier as input and returns metadata about a configuration deletion task.</p>

        Args:
            task_id: <p> The ID of the task to delete. </p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.describe_batch_delete_configuration_task_request.DescribeBatchDeleteConfigurationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.describe_batch_delete_configuration_task_response.DescribeBatchDeleteConfigurationTaskResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_batch_delete_configuration_task

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_batch_delete_configuration_task.async_describe_batch_delete_configuration_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.describe_batch_delete_configuration_task_request.DescribeBatchDeleteConfigurationTaskRequest = {
            "task_id": task_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_configurations(
        self,
        configuration_ids: "capo_application_discovery_service.types.configuration_id_list.ConfigurationIdList",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.describe_configurations_response.DescribeConfigurationsResponse":
        """<p>Retrieves attributes for a list of configuration item IDs.</p> <note> <p>All of the supplied IDs must be for the same asset type from one of the following:</p> <ul> <li> <p>server</p> </li> <li> <p>application</p> </li> <li> <p>process</p> </li> <li> <p>connection</p> </li> </ul> <p>Output fields are specific to the asset type specified. For example, the output for a <i>server</i> configuration item includes a list of attributes about the server, such as host name, operating system, number of network cards, etc.</p> <p>For a complete list of outputs for each asset type, see <a href="https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#DescribeConfigurations">Using the DescribeConfigurations Action</a> in the <i>Amazon Web Services Application Discovery Service User Guide</i>.</p> </note>

        Args:
            configuration_ids: <p>One or more configuration IDs.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.describe_configurations_request.DescribeConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.describe_configurations_response.DescribeConfigurationsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_configurations

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_configurations.async_describe_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.describe_configurations_request.DescribeConfigurationsRequest = {
            "configuration_ids": configuration_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_continuous_exports(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        export_ids: Optional[
            "capo_application_discovery_service.types.continuous_export_ids.ContinuousExportIds"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.describe_continuous_exports_max_results.DescribeContinuousExportsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_discovery_service.types.describe_continuous_exports_response.DescribeContinuousExportsResponse":
        """<p>Lists exports as specified by ID. All continuous exports associated with your user can be listed if you call <code>DescribeContinuousExports</code> as is without passing any parameters.</p>

        Args:
            export_ids: <p>The unique IDs assigned to the exports.</p>
            max_results: <p>A number between 1 and 100 specifying the maximum number of continuous export descriptions returned.</p>
            next_token: <p>The token from the previous call to <code>DescribeExportTasks</code>.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not permitted.</p>
            capo_application_discovery_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified configuration ID was not located. Verify the configuration ID and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.describe_continuous_exports_request.DescribeContinuousExportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.describe_continuous_exports_response.DescribeContinuousExportsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_continuous_exports

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_continuous_exports.async_describe_continuous_exports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.describe_continuous_exports_request.DescribeContinuousExportsRequest = {}
        if export_ids is not None:
            input_["export_ids"] = export_ids
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

    async def iter_describe_continuous_exports(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        export_ids: Optional[
            "capo_application_discovery_service.types.continuous_export_ids.ContinuousExportIds"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.describe_continuous_exports_max_results.DescribeContinuousExportsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_application_discovery_service.types.continuous_export_description.ContinuousExportDescription]":
        _token = next_token
        while True:
            _response = await self.describe_continuous_exports(
                config_overrides=config_overrides,
                export_ids=export_ids,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("descriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_export_configurations(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        export_ids: Optional[
            "capo_application_discovery_service.types.export_ids.ExportIds"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.integer.Integer"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_discovery_service.types.describe_export_configurations_response.DescribeExportConfigurationsResponse":
        """<p> <code>DescribeExportConfigurations</code> is deprecated. Use <a href="https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html">DescribeExportTasks</a>, instead.</p>

        Args:
            export_ids: <p>A list of continuous export IDs to search for.</p>
            max_results: <p>A number between 1 and 100 specifying the maximum number of continuous export descriptions returned.</p>
            next_token: <p>The token from the previous call to describe-export-tasks.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified configuration ID was not located. Verify the configuration ID and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.describe_export_configurations_request.DescribeExportConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.describe_export_configurations_response.DescribeExportConfigurationsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_export_configurations

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_export_configurations.async_describe_export_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.describe_export_configurations_request.DescribeExportConfigurationsRequest = {}
        if export_ids is not None:
            input_["export_ids"] = export_ids
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

    async def iter_describe_export_configurations(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        export_ids: Optional[
            "capo_application_discovery_service.types.export_ids.ExportIds"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.integer.Integer"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_application_discovery_service.types.export_info.ExportInfo]"
    ):
        _token = next_token
        while True:
            _response = await self.describe_export_configurations(
                config_overrides=config_overrides,
                export_ids=export_ids,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("exports_info",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_export_tasks(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        export_ids: Optional[
            "capo_application_discovery_service.types.export_ids.ExportIds"
        ] = None,
        filters: Optional[
            "capo_application_discovery_service.types.export_filters.ExportFilters"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.integer.Integer"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_discovery_service.types.describe_export_tasks_response.DescribeExportTasksResponse":
        """<p>Retrieve status of one or more export tasks. You can retrieve the status of up to 100 export tasks.</p>

        Args:
            export_ids: <p>One or more unique identifiers used to query the status of an export request.</p>
            filters: <p>One or more filters.</p> <ul> <li> <p> <code>AgentId</code> - ID of the agent whose collected data will be exported</p> </li> </ul>
            max_results: <p>The maximum number of volume results returned by <code>DescribeExportTasks</code> in paginated output. When this parameter is used, <code>DescribeExportTasks</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeExportTasks</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.describe_export_tasks_request.DescribeExportTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.describe_export_tasks_response.DescribeExportTasksResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_export_tasks

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_export_tasks.async_describe_export_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.describe_export_tasks_request.DescribeExportTasksRequest = {}
        if export_ids is not None:
            input_["export_ids"] = export_ids
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

    async def iter_describe_export_tasks(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        export_ids: Optional[
            "capo_application_discovery_service.types.export_ids.ExportIds"
        ] = None,
        filters: Optional[
            "capo_application_discovery_service.types.export_filters.ExportFilters"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.integer.Integer"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_application_discovery_service.types.export_info.ExportInfo]"
    ):
        _token = next_token
        while True:
            _response = await self.describe_export_tasks(
                config_overrides=config_overrides,
                export_ids=export_ids,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("exports_info",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_import_tasks(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        filters: Optional[
            "capo_application_discovery_service.types.describe_import_tasks_filter_list.DescribeImportTasksFilterList"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.describe_import_tasks_max_results.DescribeImportTasksMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_discovery_service.types.describe_import_tasks_response.DescribeImportTasksResponse":
        """<p>Returns an array of import tasks for your account, including status information, times, IDs, the Amazon S3 Object URL for the import file, and more.</p>

        Args:
            filters: <p>An array of name-value pairs that you provide to filter the results for the <code>DescribeImportTask</code> request to a specific subset of results. Currently, wildcard values aren't supported for filters.</p>
            max_results: <p>The maximum number of results that you want this request to return, up to 100.</p>
            next_token: <p>The token to request a specific page of results.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.describe_import_tasks_request.DescribeImportTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.describe_import_tasks_response.DescribeImportTasksResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_import_tasks

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_import_tasks.async_describe_import_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.describe_import_tasks_request.DescribeImportTasksRequest = {}
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

    async def iter_describe_import_tasks(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        filters: Optional[
            "capo_application_discovery_service.types.describe_import_tasks_filter_list.DescribeImportTasksFilterList"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.describe_import_tasks_max_results.DescribeImportTasksMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_application_discovery_service.types.import_task.ImportTask]"
    ):
        _token = next_token
        while True:
            _response = await self.describe_import_tasks(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_tags(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        filters: Optional[
            "capo_application_discovery_service.types.tag_filters.TagFilters"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.integer.Integer"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_discovery_service.types.describe_tags_response.DescribeTagsResponse":
        """<p>Retrieves a list of configuration items that have tags as specified by the key-value pairs, name and value, passed to the optional parameter <code>filters</code>.</p> <p>There are three valid tag filter names:</p> <ul> <li> <p>tagKey</p> </li> <li> <p>tagValue</p> </li> <li> <p>configurationId</p> </li> </ul> <p>Also, all configuration items associated with your user that have tags can be listed if you call <code>DescribeTags</code> as is without passing any parameters.</p>

        Args:
            filters: <p>You can filter the list using a <i>key</i>-<i>value</i> format. You can separate these items by using logical operators. Allowed filters include <code>tagKey</code>, <code>tagValue</code>, and <code>configurationId</code>. </p>
            max_results: <p>The total number of items to return in a single page of output. The maximum value is 100.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified configuration ID was not located. Verify the configuration ID and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.describe_tags_request.DescribeTagsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.describe_tags_response.DescribeTagsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_tags

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.describe_tags.async_describe_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.describe_tags_request.DescribeTagsRequest = {}
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

    async def iter_describe_tags(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        filters: Optional[
            "capo_application_discovery_service.types.tag_filters.TagFilters"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.integer.Integer"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_application_discovery_service.types.configuration_tag.ConfigurationTag]":
        _token = next_token
        while True:
            _response = await self.describe_tags(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disassociate_configuration_items_from_application(
        self,
        application_configuration_id: "capo_application_discovery_service.types.application_id.ApplicationId",
        configuration_ids: "capo_application_discovery_service.types.configuration_id_list.ConfigurationIdList",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.disassociate_configuration_items_from_application_response.DisassociateConfigurationItemsFromApplicationResponse":
        """<p>Disassociates one or more configuration items from an application.</p>

        Args:
            application_configuration_id: <p>Configuration ID of an application from which each item is disassociated.</p>
            configuration_ids: <p>Configuration ID of each item to be disassociated from an application.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.disassociate_configuration_items_from_application_request.DisassociateConfigurationItemsFromApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.disassociate_configuration_items_from_application_response.DisassociateConfigurationItemsFromApplicationResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.disassociate_configuration_items_from_application

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.disassociate_configuration_items_from_application.async_disassociate_configuration_items_from_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.disassociate_configuration_items_from_application_request.DisassociateConfigurationItemsFromApplicationRequest = {
            "application_configuration_id": application_configuration_id,
            "configuration_ids": configuration_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_configurations(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.export_configurations_response.ExportConfigurationsResponse":
        """<p>Deprecated. Use <code>StartExportTask</code> instead.</p> <p>Exports all discovered configuration data to an Amazon S3 bucket or an application that enables you to view and evaluate the data. Data includes tags and tag associations, processes, connections, servers, and system performance. This API returns an export ID that you can query using the <i>DescribeExportConfigurations</i> API. The system imposes a limit of two configuration exports in six hours.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not permitted.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.export_configurations_response.ExportConfigurationsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.export_configurations

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.export_configurations.async_export_configurations(
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

    async def get_discovery_summary(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.get_discovery_summary_response.GetDiscoverySummaryResponse":
        """<p>Retrieves a short summary of discovered assets.</p> <p>This API operation takes no request parameters and is called as is at the command prompt as shown in the example.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.get_discovery_summary_request.GetDiscoverySummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.get_discovery_summary_response.GetDiscoverySummaryResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.get_discovery_summary

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.get_discovery_summary.async_get_discovery_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.get_discovery_summary_request.GetDiscoverySummaryRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configurations(
        self,
        configuration_type: "capo_application_discovery_service.types.configuration_item_type.ConfigurationItemType",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        filters: Optional[
            "capo_application_discovery_service.types.filters.Filters"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.integer.Integer"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
        order_by: Optional[
            "capo_application_discovery_service.types.order_by_list.OrderByList"
        ] = None,
    ) -> "capo_application_discovery_service.types.list_configurations_response.ListConfigurationsResponse":
        """<p>Retrieves a list of configuration items as specified by the value passed to the required parameter <code>configurationType</code>. Optional filtering may be applied to refine search results.</p>

        Args:
            configuration_type: <p>A valid configuration identified by Application Discovery Service. </p>
            filters: <p>You can filter the request using various logical operators and a <i>key</i>-<i>value</i> format. For example: </p> <p> <code>{"key": "serverType", "value": "webServer"}</code> </p> <p>For a complete list of filter options and guidance about using them with this action, see <a href="https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#ListConfigurations">Using the ListConfigurations Action</a> in the <i>Amazon Web Services Application Discovery Service User Guide</i>.</p>
            max_results: <p>The total number of items to return. The maximum value is 100.</p>
            next_token: <p>Token to retrieve the next set of results. For example, if a previous call to ListConfigurations returned 100 items, but you set <code>ListConfigurationsRequest$maxResults</code> to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.</p>
            order_by: <p>Certain filter criteria return output that can be sorted in ascending or descending order. For a list of output characteristics for each filter, see <a href="https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#ListConfigurations">Using the ListConfigurations Action</a> in the <i>Amazon Web Services Application Discovery Service User Guide</i>.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified configuration ID was not located. Verify the configuration ID and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.list_configurations_request.ListConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.list_configurations_response.ListConfigurationsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.list_configurations

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.list_configurations.async_list_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.list_configurations_request.ListConfigurationsRequest = {
            "configuration_type": configuration_type
        }
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order_by is not None:
            input_["order_by"] = order_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_configurations(
        self,
        configuration_type: "capo_application_discovery_service.types.configuration_item_type.ConfigurationItemType",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        filters: Optional[
            "capo_application_discovery_service.types.filters.Filters"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.integer.Integer"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.next_token.NextToken"
        ] = None,
        order_by: Optional[
            "capo_application_discovery_service.types.order_by_list.OrderByList"
        ] = None,
    ) -> "AsyncIterator[capo_application_discovery_service.types.configuration.Configuration]":
        _token = next_token
        while True:
            _response = await self.list_configurations(
                configuration_type,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
                order_by=order_by,
            )
            _page = _resolve_path(_response, ("configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_server_neighbors(
        self,
        configuration_id: "capo_application_discovery_service.types.configuration_id.ConfigurationId",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        port_information_needed: Optional[
            "capo_application_discovery_service.types.boolean.Boolean"
        ] = None,
        neighbor_configuration_ids: Optional[
            "capo_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
        ] = None,
        max_results: Optional[
            "capo_application_discovery_service.types.integer.Integer"
        ] = None,
        next_token: Optional[
            "capo_application_discovery_service.types.string.String"
        ] = None,
    ) -> "capo_application_discovery_service.types.list_server_neighbors_response.ListServerNeighborsResponse":
        """<p>Retrieves a list of servers that are one network hop away from a specified server.</p>

        Args:
            configuration_id: <p>Configuration ID of the server for which neighbors are being listed.</p>
            port_information_needed: <p>Flag to indicate if port and protocol information is needed as part of the response.</p>
            neighbor_configuration_ids: <p>List of configuration IDs to test for one-hop-away.</p>
            max_results: <p>Maximum number of results to return in a single page of output.</p>
            next_token: <p>Token to retrieve the next set of results. For example, if you previously specified 100 IDs for <code>ListServerNeighborsRequest$neighborConfigurationIds</code> but set <code>ListServerNeighborsRequest$maxResults</code> to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.list_server_neighbors_request.ListServerNeighborsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.list_server_neighbors_response.ListServerNeighborsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.list_server_neighbors

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.list_server_neighbors.async_list_server_neighbors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.list_server_neighbors_request.ListServerNeighborsRequest = {
            "configuration_id": configuration_id
        }
        if port_information_needed is not None:
            input_["port_information_needed"] = port_information_needed
        if neighbor_configuration_ids is not None:
            input_["neighbor_configuration_ids"] = neighbor_configuration_ids
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

    async def start_batch_delete_configuration_task(
        self,
        configuration_type: "capo_application_discovery_service.types.deletion_configuration_item_type.DeletionConfigurationItemType",
        configuration_ids: "capo_application_discovery_service.types.configuration_id_list.ConfigurationIdList",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.start_batch_delete_configuration_task_response.StartBatchDeleteConfigurationTaskResponse":
        """<p> Takes a list of configurationId as input and starts an asynchronous deletion task to remove the configurationItems. Returns a unique deletion task identifier. </p>

        Args:
            configuration_type: <p> The type of configuration item to delete. Supported types are: SERVER. </p>
            configuration_ids: <p> The list of configuration IDs that will be deleted by the task. </p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.limit_exceeded_exception.LimitExceededException: <p> The limit of 200 configuration IDs per request has been exceeded. </p>
            capo_application_discovery_service.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not permitted.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.start_batch_delete_configuration_task_request.StartBatchDeleteConfigurationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.start_batch_delete_configuration_task_response.StartBatchDeleteConfigurationTaskResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.start_batch_delete_configuration_task

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.start_batch_delete_configuration_task.async_start_batch_delete_configuration_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.start_batch_delete_configuration_task_request.StartBatchDeleteConfigurationTaskRequest = {
            "configuration_type": configuration_type,
            "configuration_ids": configuration_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_continuous_export(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.start_continuous_export_response.StartContinuousExportResponse":
        """<p>Start the continuous flow of agent's discovered data into Amazon Athena.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.conflict_error_exception.ConflictErrorException: <p>Conflict error.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not permitted.</p>
            capo_application_discovery_service.errors.resource_in_use_exception.ResourceInUseException: <p>This issue occurs when the same <code>clientRequestToken</code> is used with the <code>StartImportTask</code> action, but with different parameters. For example, you use the same request token but have two different import URLs, you can encounter this issue. If the import tasks are meant to be different, use a different <code>clientRequestToken</code>, and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.start_continuous_export_request.StartContinuousExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.start_continuous_export_response.StartContinuousExportResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.start_continuous_export

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.start_continuous_export.async_start_continuous_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.start_continuous_export_request.StartContinuousExportRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_data_collection_by_agent_ids(
        self,
        agent_ids: "capo_application_discovery_service.types.agent_ids.AgentIds",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.start_data_collection_by_agent_ids_response.StartDataCollectionByAgentIdsResponse":
        """<p>Instructs the specified agents to start collecting data.</p>

        Args:
            agent_ids: <p>The IDs of the agents from which to start collecting data. If you send a request to an agent ID that you do not have permission to contact, according to your Amazon Web Services account, the service does not throw an exception. Instead, it returns the error in the <i>Description</i> field. If you send a request to multiple agents and you do not have permission to contact some of those agents, the system does not throw an exception. Instead, the system shows <code>Failed</code> in the <i>Description</i> field.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.start_data_collection_by_agent_ids_request.StartDataCollectionByAgentIdsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.start_data_collection_by_agent_ids_response.StartDataCollectionByAgentIdsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.start_data_collection_by_agent_ids

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.start_data_collection_by_agent_ids.async_start_data_collection_by_agent_ids(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.start_data_collection_by_agent_ids_request.StartDataCollectionByAgentIdsRequest = {
            "agent_ids": agent_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_export_task(
        self,
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        export_data_format: Optional[
            "capo_application_discovery_service.types.export_data_formats.ExportDataFormats"
        ] = None,
        filters: Optional[
            "capo_application_discovery_service.types.export_filters.ExportFilters"
        ] = None,
        start_time: Optional[
            "capo_application_discovery_service.types.time_stamp.TimeStamp"
        ] = None,
        end_time: Optional[
            "capo_application_discovery_service.types.time_stamp.TimeStamp"
        ] = None,
        preferences: Optional[
            "capo_application_discovery_service.types.export_preferences.ExportPreferences"
        ] = None,
    ) -> "capo_application_discovery_service.types.start_export_task_response.StartExportTaskResponse":
        """<p>Begins the export of a discovered data report to an Amazon S3 bucket managed by Amazon Web Services.</p> <note> <p>Exports might provide an estimate of fees and savings based on certain information that you provide. Fee estimates do not include any taxes that might apply. Your actual fees and savings depend on a variety of factors, including your actual usage of Amazon Web Services services, which might vary from the estimates provided in this report.</p> </note> <p>If you do not specify <code>preferences</code> or <code>agentIds</code> in the filter, a summary of all servers, applications, tags, and performance is generated. This data is an aggregation of all server data collected through on-premises tooling, file import, application grouping and applying tags.</p> <p>If you specify <code>agentIds</code> in a filter, the task exports up to 72 hours of detailed data collected by the identified Application Discovery Agent, including network, process, and performance details. A time range for exported agent data may be set by using <code>startTime</code> and <code>endTime</code>. Export of detailed agent data is limited to five concurrently running exports. Export of detailed agent data is limited to two exports per day.</p> <p>If you enable <code>ec2RecommendationsPreferences</code> in <code>preferences</code> , an Amazon EC2 instance matching the characteristics of each server in Application Discovery Service is generated. Changing the attributes of the <code>ec2RecommendationsPreferences</code> changes the criteria of the recommendation.</p>

        Args:
            export_data_format: <p>The file format for the returned export data. Default value is <code>CSV</code>. <b>Note:</b> <i>The</i> <code>GRAPHML</code> <i>option has been deprecated.</i> </p>
            filters: <p>If a filter is present, it selects the single <code>agentId</code> of the Application Discovery Agent for which data is exported. The <code>agentId</code> can be found in the results of the <code>DescribeAgents</code> API or CLI. If no filter is present, <code>startTime</code> and <code>endTime</code> are ignored and exported data includes both Amazon Web Services Application Discovery Service Agentless Collector collectors data and summary data from Application Discovery Agent agents. </p>
            start_time: <p>The start timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, data is exported starting from the first data collected by the agent.</p>
            end_time: <p>The end timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, exported data includes the most recent data collected by the agent.</p>
            preferences: <p> Indicates the type of data that needs to be exported. Only one <a href="https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ExportPreferences.html">ExportPreferences</a> can be enabled at any time. </p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not permitted.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.start_export_task_request.StartExportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.start_export_task_response.StartExportTaskResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.start_export_task

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.start_export_task.async_start_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.start_export_task_request.StartExportTaskRequest = {}
        if export_data_format is not None:
            input_["export_data_format"] = export_data_format
        if filters is not None:
            input_["filters"] = filters
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if preferences is not None:
            input_["preferences"] = preferences

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_import_task(
        self,
        name: "capo_application_discovery_service.types.import_task_name.ImportTaskName",
        import_url: "capo_application_discovery_service.types.import_url.ImportURL",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        client_request_token: Optional[
            "capo_application_discovery_service.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_application_discovery_service.types.start_import_task_response.StartImportTaskResponse":
        """<p>Starts an import task, which allows you to import details of your on-premises environment directly into Amazon Web Services Migration Hub without having to use the Amazon Web Services Application Discovery Service (Application Discovery Service) tools such as the Amazon Web Services Application Discovery Service Agentless Collector or Application Discovery Agent. This gives you the option to perform migration assessment and planning directly from your imported data, including the ability to group your devices as applications and track their migration status.</p> <p>To start an import request, do this:</p> <ol> <li> <p>Download the specially formatted comma separated value (CSV) import template, which you can find here: <a href="https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import_template.csv">https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import_template.csv</a>.</p> </li> <li> <p>Fill out the template with your server and application data.</p> </li> <li> <p>Upload your import file to an Amazon S3 bucket, and make a note of it's Object URL. Your import file must be in the CSV format.</p> </li> <li> <p>Use the console or the <code>StartImportTask</code> command with the Amazon Web Services CLI or one of the Amazon Web Services SDKs to import the records from your file.</p> </li> </ol> <p>For more information, including step-by-step procedures, see <a href="https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html">Migration Hub Import</a> in the <i>Amazon Web Services Application Discovery Service User Guide</i>.</p> <note> <p>There are limits to the number of import tasks you can create (and delete) in an Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/application-discovery/latest/userguide/ads_service_limits.html">Amazon Web Services Application Discovery Service Limits</a> in the <i>Amazon Web Services Application Discovery Service User Guide</i>.</p> </note>

        Args:
            client_request_token: <p>Optional. A unique token that you can provide to prevent the same import request from occurring more than once. If you don't provide a token, a token is automatically generated.</p> <p>Sending more than one <code>StartImportTask</code> request with the same client request token will return information about the original import task with that client request token.</p>
            name: <p>A descriptive name for this request. You can use this name to filter future requests related to this import task, such as identifying applications and servers that were included in this import task. We recommend that you use a meaningful name for each import task.</p>
            import_url: <p>The URL for your import file that you've uploaded to Amazon S3.</p> <note> <p>If you're using the Amazon Web Services CLI, this URL is structured as follows: <code>s3://BucketName/ImportFileName.CSV</code> </p> </note>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.resource_in_use_exception.ResourceInUseException: <p>This issue occurs when the same <code>clientRequestToken</code> is used with the <code>StartImportTask</code> action, but with different parameters. For example, you use the same request token but have two different import URLs, you can encounter this issue. If the import tasks are meant to be different, use a different <code>clientRequestToken</code>, and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.start_import_task_request.StartImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.start_import_task_response.StartImportTaskResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.start_import_task

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.start_import_task.async_start_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.start_import_task_request.StartImportTaskRequest = {
            "name": name,
            "import_url": import_url,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_continuous_export(
        self,
        export_id: "capo_application_discovery_service.types.configurations_export_id.ConfigurationsExportId",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.stop_continuous_export_response.StopContinuousExportResponse":
        """<p>Stop the continuous flow of agent's discovered data into Amazon Athena.</p>

        Args:
            export_id: <p>The unique ID assigned to this export.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.operation_not_permitted_exception.OperationNotPermittedException: <p>This operation is not permitted.</p>
            capo_application_discovery_service.errors.resource_in_use_exception.ResourceInUseException: <p>This issue occurs when the same <code>clientRequestToken</code> is used with the <code>StartImportTask</code> action, but with different parameters. For example, you use the same request token but have two different import URLs, you can encounter this issue. If the import tasks are meant to be different, use a different <code>clientRequestToken</code>, and try again.</p>
            capo_application_discovery_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified configuration ID was not located. Verify the configuration ID and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.stop_continuous_export_request.StopContinuousExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.stop_continuous_export_response.StopContinuousExportResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.stop_continuous_export

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.stop_continuous_export.async_stop_continuous_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.stop_continuous_export_request.StopContinuousExportRequest = {
            "export_id": export_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_data_collection_by_agent_ids(
        self,
        agent_ids: "capo_application_discovery_service.types.agent_ids.AgentIds",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
    ) -> "capo_application_discovery_service.types.stop_data_collection_by_agent_ids_response.StopDataCollectionByAgentIdsResponse":
        """<p>Instructs the specified agents to stop collecting data.</p>

        Args:
            agent_ids: <p>The IDs of the agents from which to stop collecting data.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.stop_data_collection_by_agent_ids_request.StopDataCollectionByAgentIdsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.stop_data_collection_by_agent_ids_response.StopDataCollectionByAgentIdsResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.stop_data_collection_by_agent_ids

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.stop_data_collection_by_agent_ids.async_stop_data_collection_by_agent_ids(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.stop_data_collection_by_agent_ids_request.StopDataCollectionByAgentIdsRequest = {
            "agent_ids": agent_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_application(
        self,
        configuration_id: "capo_application_discovery_service.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncApplicationDiscoveryServiceClientConfig] = None,
        name: Optional[
            "capo_application_discovery_service.types.application_name.ApplicationName"
        ] = None,
        description: Optional[
            "capo_application_discovery_service.types.application_description.ApplicationDescription"
        ] = None,
        wave: Optional[
            "capo_application_discovery_service.types.application_wave.ApplicationWave"
        ] = None,
    ) -> "capo_application_discovery_service.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates metadata about an application.</p>

        Args:
            configuration_id: <p>Configuration ID of the application to be updated.</p>
            name: <p>New name of the application to be updated.</p>
            description: <p>New description of the application to be updated.</p>
            wave: <p>The new migration wave of the application that you want to update.</p>

        Raises:
            capo_application_discovery_service.errors.authorization_error_exception.AuthorizationErrorException: <p>The user does not have permission to perform the action. Check the IAM policy associated with this user.</p>
            capo_application_discovery_service.errors.home_region_not_set_exception.HomeRegionNotSetException: <p>The home Region is not set. Set the home Region to continue.</p>
            capo_application_discovery_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid. Verify the parameters and try again.</p>
            capo_application_discovery_service.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.</p>
            capo_application_discovery_service.errors.server_internal_error_exception.ServerInternalErrorException: <p>The server experienced an internal error. Try again.</p>
            capo_application_discovery_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_discovery_service.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_discovery_service.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.update_application

            (
                output,
                http_response,
            ) = await capo_application_discovery_service._operations.aws_poseidon_service_v2015_11_01.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_discovery_service.types.update_application_request.UpdateApplicationRequest = {
            "configuration_id": configuration_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if wave is not None:
            input_["wave"] = wave

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
