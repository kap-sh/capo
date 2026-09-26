"""Generated from Smithy shape ``com.amazonaws.groundstation#GroundStation``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_groundstation._auth._signers
import capo_groundstation._auth._sigv4
from capo_groundstation._auth._identity import Credentials
from capo_groundstation._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_groundstation._auth._zapros_handler import AuthMiddleware
from capo_groundstation._pagination import resolve_path as _resolve_path
from capo_groundstation._resources.ground_station.agent import AsyncAgent
from capo_groundstation._resources.ground_station.config import AsyncConfig
from capo_groundstation._resources.ground_station.contact import AsyncContact
from capo_groundstation._resources.ground_station.dataflow_endpoint_group import (
    AsyncDataflowEndpointGroup,
)
from capo_groundstation._resources.ground_station.dataflow_endpoint_group_v2 import (
    AsyncDataflowEndpointGroupV2,
)
from capo_groundstation._resources.ground_station.ephemeris import AsyncEphemeris
from capo_groundstation._resources.ground_station.ground_station_resource import (
    AsyncGroundStationResource,
)
from capo_groundstation._resources.ground_station.mission_profile import (
    AsyncMissionProfile,
)
from capo_groundstation._resources.ground_station.satellite import AsyncSatellite
from capo_groundstation._services._aws_config import aaws_config
from capo_groundstation._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_groundstation.types.agent_details
    import capo_groundstation.types.aggregate_status
    import capo_groundstation.types.antenna_list_item
    import capo_groundstation.types.any_arn
    import capo_groundstation.types.cancel_contact_request
    import capo_groundstation.types.client_token
    import capo_groundstation.types.component_status_list
    import capo_groundstation.types.config_arn
    import capo_groundstation.types.config_capability_type
    import capo_groundstation.types.config_id_response
    import capo_groundstation.types.config_list_item
    import capo_groundstation.types.config_type_data
    import capo_groundstation.types.contact_data
    import capo_groundstation.types.contact_id_response
    import capo_groundstation.types.contact_version
    import capo_groundstation.types.create_config_request
    import capo_groundstation.types.create_dataflow_endpoint_group_request
    import capo_groundstation.types.create_dataflow_endpoint_group_v2_request
    import capo_groundstation.types.create_dataflow_endpoint_group_v2_response
    import capo_groundstation.types.create_endpoint_details_list
    import capo_groundstation.types.create_ephemeris_request
    import capo_groundstation.types.create_mission_profile_request
    import capo_groundstation.types.customer_ephemeris_priority
    import capo_groundstation.types.dataflow_edge_list
    import capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds
    import capo_groundstation.types.dataflow_endpoint_group_id_response
    import capo_groundstation.types.dataflow_endpoint_list_item
    import capo_groundstation.types.delete_config_request
    import capo_groundstation.types.delete_dataflow_endpoint_group_request
    import capo_groundstation.types.delete_ephemeris_request
    import capo_groundstation.types.delete_mission_profile_request
    import capo_groundstation.types.describe_contact_request
    import capo_groundstation.types.describe_contact_response
    import capo_groundstation.types.describe_contact_version_request
    import capo_groundstation.types.describe_contact_version_response
    import capo_groundstation.types.describe_ephemeris_request
    import capo_groundstation.types.describe_ephemeris_response
    import capo_groundstation.types.discovery_data
    import capo_groundstation.types.duration_in_seconds
    import capo_groundstation.types.endpoint_details_list
    import capo_groundstation.types.ephemeris_data
    import capo_groundstation.types.ephemeris_filter
    import capo_groundstation.types.ephemeris_id_response
    import capo_groundstation.types.ephemeris_item
    import capo_groundstation.types.ephemeris_priority
    import capo_groundstation.types.ephemeris_status_list
    import capo_groundstation.types.ephemeris_type
    import capo_groundstation.types.get_agent_configuration_request
    import capo_groundstation.types.get_agent_configuration_response
    import capo_groundstation.types.get_agent_task_response_url_request
    import capo_groundstation.types.get_agent_task_response_url_response
    import capo_groundstation.types.get_config_request
    import capo_groundstation.types.get_config_response
    import capo_groundstation.types.get_dataflow_endpoint_group_request
    import capo_groundstation.types.get_dataflow_endpoint_group_response
    import capo_groundstation.types.get_minute_usage_request
    import capo_groundstation.types.get_minute_usage_response
    import capo_groundstation.types.get_mission_profile_request
    import capo_groundstation.types.get_mission_profile_response
    import capo_groundstation.types.get_satellite_request
    import capo_groundstation.types.get_satellite_response
    import capo_groundstation.types.ground_station_data
    import capo_groundstation.types.ground_station_name
    import capo_groundstation.types.ground_station_reservation_list_item
    import capo_groundstation.types.key_arn
    import capo_groundstation.types.kms_key
    import capo_groundstation.types.list_antennas_request
    import capo_groundstation.types.list_antennas_response
    import capo_groundstation.types.list_configs_request
    import capo_groundstation.types.list_configs_response
    import capo_groundstation.types.list_contact_versions_request
    import capo_groundstation.types.list_contact_versions_response
    import capo_groundstation.types.list_contacts_request
    import capo_groundstation.types.list_contacts_response
    import capo_groundstation.types.list_dataflow_endpoint_groups_request
    import capo_groundstation.types.list_dataflow_endpoint_groups_response
    import capo_groundstation.types.list_ephemerides_request
    import capo_groundstation.types.list_ephemerides_response
    import capo_groundstation.types.list_ground_station_reservations_request
    import capo_groundstation.types.list_ground_station_reservations_response
    import capo_groundstation.types.list_ground_stations_request
    import capo_groundstation.types.list_ground_stations_response
    import capo_groundstation.types.list_mission_profiles_request
    import capo_groundstation.types.list_mission_profiles_response
    import capo_groundstation.types.list_satellites_request
    import capo_groundstation.types.list_satellites_response
    import capo_groundstation.types.list_tags_for_resource_request
    import capo_groundstation.types.list_tags_for_resource_response
    import capo_groundstation.types.mission_profile_arn
    import capo_groundstation.types.mission_profile_id_response
    import capo_groundstation.types.mission_profile_list_item
    import capo_groundstation.types.month
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token
    import capo_groundstation.types.positive_duration_in_seconds
    import capo_groundstation.types.register_agent_request
    import capo_groundstation.types.register_agent_response
    import capo_groundstation.types.reservation_type_filter_list
    import capo_groundstation.types.reserve_contact_request
    import capo_groundstation.types.role_arn
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.satellite_arn
    import capo_groundstation.types.satellite_list_item
    import capo_groundstation.types.status_list
    import capo_groundstation.types.tag_keys
    import capo_groundstation.types.tag_resource_request
    import capo_groundstation.types.tag_resource_response
    import capo_groundstation.types.tags_map
    import capo_groundstation.types.tracking_overrides
    import capo_groundstation.types.untag_resource_request
    import capo_groundstation.types.untag_resource_response
    import capo_groundstation.types.update_agent_status_request
    import capo_groundstation.types.update_agent_status_response
    import capo_groundstation.types.update_config_request
    import capo_groundstation.types.update_contact_request
    import capo_groundstation.types.update_contact_response
    import capo_groundstation.types.update_ephemeris_request
    import capo_groundstation.types.update_mission_profile_request
    import capo_groundstation.types.uuid
    import capo_groundstation.types.version_id
    import capo_groundstation.types.year


class AsyncGroundStationClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncGroundStationClient:
    """A client for the ``GroundStation`` service.

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
        self._config = AsyncGroundStationClientConfig(
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
        self.agent = AsyncAgent(self)
        self.config = AsyncConfig(self)
        self.contact = AsyncContact(self)
        self.dataflow_endpoint_group = AsyncDataflowEndpointGroup(self)
        self.dataflow_endpoint_group_v2 = AsyncDataflowEndpointGroupV2(self)
        self.ephemeris = AsyncEphemeris(self)
        self.ground_station_resource = AsyncGroundStationResource(self)
        self.mission_profile = AsyncMissionProfile(self)
        self.satellite = AsyncSatellite(self)

    def operation_options(
        self, config_overrides: Optional[AsyncGroundStationClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncGroundStationClientConfig = config_overrides or {}
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

    async def get_agent_task_response_url(
        self,
        agent_id: "capo_groundstation.types.uuid.Uuid",
        task_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_agent_task_response_url_response.GetAgentTaskResponseUrlResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Gets a presigned URL for uploading agent task response logs.</p>

        Args:
            agent_id: <p>UUID of agent requesting the response URL.</p>
            task_id: <p>GUID of the agent task for which the response URL is being requested.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.get_agent_task_response_url_request.GetAgentTaskResponseUrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.get_agent_task_response_url_response.GetAgentTaskResponseUrlResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_agent_task_response_url

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.get_agent_task_response_url.async_get_agent_task_response_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.get_agent_task_response_url_request.GetAgentTaskResponseUrlRequest = {
            "agent_id": agent_id,
            "task_id": task_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_minute_usage(
        self,
        month: "capo_groundstation.types.month.Month",
        year: "capo_groundstation.types.year.Year",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_minute_usage_response.GetMinuteUsageResponse":
        """<p>Returns the number of reserved minutes used by account.</p>

        Args:
            month: <p>The month being requested, with a value of 1-12.</p>
            year: <p>The year being requested, in the format of YYYY.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.get_minute_usage_request.GetMinuteUsageRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.get_minute_usage_response.GetMinuteUsageResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_minute_usage

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.get_minute_usage.async_get_minute_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.get_minute_usage_request.GetMinuteUsageRequest = {
            "month": month,
            "year": year,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_groundstation.types.any_arn.AnyArn",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a specified resource.</p>

        Args:
            resource_arn: <p>ARN of a resource.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_groundstation.types.any_arn.AnyArn",
        tags: "capo_groundstation.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns a tag to a resource.</p>

        Args:
            resource_arn: <p>ARN of a resource tag.</p>
            tags: <p>Tags assigned to a resource.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_groundstation._operations.ground_station.tag_resource

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_groundstation.types.any_arn.AnyArn",
        tag_keys: "capo_groundstation.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.untag_resource_response.UntagResourceResponse":
        """<p>Deassigns a resource tag.</p>

        Args:
            resource_arn: <p>ARN of a resource.</p>
            tag_keys: <p>Keys of a resource tag.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_groundstation._operations.ground_station.untag_resource

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.untag_resource_request.UntagResourceRequest = {
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

    async def register_agent(
        self,
        discovery_data: "capo_groundstation.types.discovery_data.DiscoveryData",
        agent_details: "capo_groundstation.types.agent_details.AgentDetails",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "capo_groundstation.types.register_agent_response.RegisterAgentResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p> Registers a new agent with AWS Ground Station. </p>

        Args:
            discovery_data: <p>Data for associating an agent with the capabilities it is managing.</p>
            agent_details: <p>Detailed information about the agent being registered.</p>
            tags: <p>Tags assigned to an <code>Agent</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.register_agent_request.RegisterAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.register_agent_response.RegisterAgentResponse"
        ]:
            import capo_groundstation._operations.ground_station.register_agent

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.register_agent.async_register_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.register_agent_request.RegisterAgentRequest = {
            "discovery_data": discovery_data,
            "agent_details": agent_details,
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

    async def get_agent_configuration(
        self,
        agent_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_agent_configuration_response.GetAgentConfigurationResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Gets the latest configuration information for a registered agent.</p>

        Args:
            agent_id: <p>UUID of agent to get configuration information for.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.get_agent_configuration_request.GetAgentConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.get_agent_configuration_response.GetAgentConfigurationResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_agent_configuration

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.get_agent_configuration.async_get_agent_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.get_agent_configuration_request.GetAgentConfigurationRequest = {
            "agent_id": agent_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_agent_status(
        self,
        agent_id: "capo_groundstation.types.uuid.Uuid",
        task_id: "capo_groundstation.types.uuid.Uuid",
        aggregate_status: "capo_groundstation.types.aggregate_status.AggregateStatus",
        component_statuses: "capo_groundstation.types.component_status_list.ComponentStatusList",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.update_agent_status_response.UpdateAgentStatusResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Update the status of the agent.</p>

        Args:
            agent_id: <p>UUID of agent to update.</p>
            task_id: <p>GUID of agent task.</p>
            aggregate_status: <p>Aggregate status for agent.</p>
            component_statuses: <p>List of component statuses for agent.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.update_agent_status_request.UpdateAgentStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.update_agent_status_response.UpdateAgentStatusResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_agent_status

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.update_agent_status.async_update_agent_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.update_agent_status_request.UpdateAgentStatusRequest = {
            "agent_id": agent_id,
            "task_id": task_id,
            "aggregate_status": aggregate_status,
            "component_statuses": component_statuses,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_config(
        self,
        name: "capo_groundstation.types.safe_name.SafeName",
        config_data: "capo_groundstation.types.config_type_data.ConfigTypeData",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "capo_groundstation.types.config_id_response.ConfigIdResponse":
        """<p>Creates a <code>Config</code> with the specified <code>configData</code> parameters.</p> <p>Only one type of <code>configData</code> can be specified.</p>

        Args:
            name: <p>Name of a <code>Config</code>.</p>
            config_data: <p>Parameters of a <code>Config</code>.</p>
            tags: <p>Tags assigned to a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.create_config_request.CreateConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.config_id_response.ConfigIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.create_config

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.create_config.async_create_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.create_config_request.CreateConfigRequest = {
            "name": name,
            "config_data": config_data,
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

    async def get_config(
        self,
        config_id: "capo_groundstation.types.uuid.Uuid",
        config_type: "capo_groundstation.types.config_capability_type.ConfigCapabilityType",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_config_response.GetConfigResponse":
        """<p>Returns <code>Config</code> information.</p> <p>Only one <code>Config</code> response can be returned.</p>

        Args:
            config_id: <p>UUID of a <code>Config</code>.</p>
            config_type: <p>Type of a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.get_config_request.GetConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.get_config_response.GetConfigResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_config

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.get_config.async_get_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.get_config_request.GetConfigRequest = {
            "config_id": config_id,
            "config_type": config_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_config(
        self,
        config_id: "capo_groundstation.types.uuid.Uuid",
        name: "capo_groundstation.types.safe_name.SafeName",
        config_type: "capo_groundstation.types.config_capability_type.ConfigCapabilityType",
        config_data: "capo_groundstation.types.config_type_data.ConfigTypeData",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.config_id_response.ConfigIdResponse":
        """<p>Updates the <code>Config</code> used when scheduling contacts.</p> <p>Updating a <code>Config</code> will not update the execution parameters for existing future contacts scheduled with this <code>Config</code>.</p>

        Args:
            config_id: <p>UUID of a <code>Config</code>.</p>
            name: <p>Name of a <code>Config</code>.</p>
            config_type: <p>Type of a <code>Config</code>.</p>
            config_data: <p>Parameters of a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.update_config_request.UpdateConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.config_id_response.ConfigIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_config

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.update_config.async_update_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.update_config_request.UpdateConfigRequest = {
            "config_id": config_id,
            "name": name,
            "config_type": config_type,
            "config_data": config_data,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_config(
        self,
        config_id: "capo_groundstation.types.uuid.Uuid",
        config_type: "capo_groundstation.types.config_capability_type.ConfigCapabilityType",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.config_id_response.ConfigIdResponse":
        """<p>Deletes a <code>Config</code>.</p>

        Args:
            config_id: <p>UUID of a <code>Config</code>.</p>
            config_type: <p>Type of a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.delete_config_request.DeleteConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.config_id_response.ConfigIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.delete_config

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.delete_config.async_delete_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.delete_config_request.DeleteConfigRequest = {
            "config_id": config_id,
            "config_type": config_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configs(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_configs_response.ListConfigsResponse":
        """<p>Returns a list of <code>Config</code> objects.</p>

        Args:
            max_results: <p>Maximum number of <code>Configs</code> returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListConfigs</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_configs_request.ListConfigsRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_configs_response.ListConfigsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_configs

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_configs.async_list_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.list_configs_request.ListConfigsRequest = {}
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

    async def iter_list_configs(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_groundstation.types.config_list_item.ConfigListItem]":
        _token = next_token
        while True:
            _response = await self.list_configs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("config_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reserve_contact(
        self,
        mission_profile_arn: "capo_groundstation.types.mission_profile_arn.MissionProfileArn",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        ground_station: "capo_groundstation.types.ground_station_name.GroundStationName",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        satellite_arn: Optional[
            "capo_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
        tracking_overrides: Optional[
            "capo_groundstation.types.tracking_overrides.TrackingOverrides"
        ] = None,
    ) -> "capo_groundstation.types.contact_id_response.ContactIdResponse":
        """<p>Reserves a contact using specified parameters.</p>

        Args:
            mission_profile_arn: <p>ARN of a mission profile.</p>
            satellite_arn: <p>ARN of a satellite</p>
            start_time: <p>Start time of a contact in UTC.</p>
            end_time: <p>End time of a contact in UTC.</p>
            ground_station: <p>Name of a ground station.</p>
            tags: <p>Tags assigned to a contact.</p>
            tracking_overrides: <p>Tracking configuration overrides for the contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.reserve_contact_request.ReserveContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.contact_id_response.ContactIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.reserve_contact

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.reserve_contact.async_reserve_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.reserve_contact_request.ReserveContactRequest = {
            "mission_profile_arn": mission_profile_arn,
            "start_time": start_time,
            "end_time": end_time,
            "ground_station": ground_station,
        }
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn
        if tags is not None:
            input_["tags"] = tags
        if tracking_overrides is not None:
            input_["tracking_overrides"] = tracking_overrides

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_contact(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.describe_contact_response.DescribeContactResponse":
        """<p>Describes an existing contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.describe_contact_request.DescribeContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.describe_contact_response.DescribeContactResponse"
        ]:
            import capo_groundstation._operations.ground_station.describe_contact

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.describe_contact.async_describe_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.describe_contact_request.DescribeContactRequest = {
            "contact_id": contact_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_contact(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        client_token: Optional[
            "capo_groundstation.types.client_token.ClientToken"
        ] = None,
        tracking_overrides: Optional[
            "capo_groundstation.types.tracking_overrides.TrackingOverrides"
        ] = None,
        satellite_arn: Optional[
            "capo_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
    ) -> "capo_groundstation.types.update_contact_response.UpdateContactResponse":
        """<p>Updates a specific contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            client_token: <p>A client token is a unique, case-sensitive string of up to 64 ASCII characters. It is generated by the client to ensure idempotent operations, allowing safe retries without unintended side effects.</p>
            satellite_arn: <p>ARN of a satellite.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.update_contact_request.UpdateContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.update_contact_response.UpdateContactResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_contact

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.update_contact.async_update_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.update_contact_request.UpdateContactRequest = {
            "contact_id": contact_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tracking_overrides is not None:
            input_["tracking_overrides"] = tracking_overrides
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_contact(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.contact_id_response.ContactIdResponse":
        r"""<p>Cancels or stops a contact with a specified contact ID based on its position in the <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/contacts.lifecycle.html\">contact lifecycle</a>.</p> <p>For contacts that:</p> <ul> <li> <p>Have yet to start, the contact will be cancelled.</p> </li> <li> <p>Have started but have yet to finish, the contact will be stopped.</p> </li> </ul>

        Args:
            contact_id: <p>UUID of a contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.cancel_contact_request.CancelContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.contact_id_response.ContactIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.cancel_contact

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.cancel_contact.async_cancel_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.cancel_contact_request.CancelContactRequest = {
            "contact_id": contact_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_contacts(
        self,
        status_list: "capo_groundstation.types.status_list.StatusList",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
        ground_station: Optional[
            "capo_groundstation.types.ground_station_name.GroundStationName"
        ] = None,
        satellite_arn: Optional[
            "capo_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
        mission_profile_arn: Optional[
            "capo_groundstation.types.mission_profile_arn.MissionProfileArn"
        ] = None,
        ephemeris: Optional[
            "capo_groundstation.types.ephemeris_filter.EphemerisFilter"
        ] = None,
    ) -> "capo_groundstation.types.list_contacts_response.ListContactsResponse":
        r"""<p>Returns a list of contacts.</p> <p>If <code>statusList</code> contains AVAILABLE, the request must include <code> groundStation</code>, <code>missionprofileArn</code>, and <code>satelliteArn</code>. </p>

        Args:
            max_results: <p>Maximum number of contacts returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListContacts</code> call. Used to get the next page of results.</p>
            status_list: <p>Status of a contact reservation.</p>
            start_time: <p>Start time of a contact in UTC.</p>
            end_time: <p>End time of a contact in UTC.</p>
            ground_station: <p>Name of a ground station.</p>
            satellite_arn: <p>ARN of a satellite.</p>
            mission_profile_arn: <p>ARN of a mission profile.</p>
            ephemeris: <p>Filter for selecting contacts that use a specific ephemeris\".</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_contacts_request.ListContactsRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_contacts_response.ListContactsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_contacts

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_contacts.async_list_contacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.list_contacts_request.ListContactsRequest = {
            "status_list": status_list,
            "start_time": start_time,
            "end_time": end_time,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if ground_station is not None:
            input_["ground_station"] = ground_station
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn
        if mission_profile_arn is not None:
            input_["mission_profile_arn"] = mission_profile_arn
        if ephemeris is not None:
            input_["ephemeris"] = ephemeris

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_contacts(
        self,
        status_list: "capo_groundstation.types.status_list.StatusList",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
        ground_station: Optional[
            "capo_groundstation.types.ground_station_name.GroundStationName"
        ] = None,
        satellite_arn: Optional[
            "capo_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
        mission_profile_arn: Optional[
            "capo_groundstation.types.mission_profile_arn.MissionProfileArn"
        ] = None,
        ephemeris: Optional[
            "capo_groundstation.types.ephemeris_filter.EphemerisFilter"
        ] = None,
    ) -> "AsyncIterator[capo_groundstation.types.contact_data.ContactData]":
        _token = next_token
        while True:
            _response = await self.list_contacts(
                status_list,
                start_time,
                end_time,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                ground_station=ground_station,
                satellite_arn=satellite_arn,
                mission_profile_arn=mission_profile_arn,
                ephemeris=ephemeris,
            )
            _page = _resolve_path(_response, ("contact_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_contact_version(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        version_id: "capo_groundstation.types.version_id.VersionId",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse":
        """<p>Describes a specific version of a contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            version_id: <p>Version ID of a contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse"
        ]:
            import capo_groundstation._operations.ground_station.describe_contact_version

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.describe_contact_version.async_describe_contact_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest = {
            "contact_id": contact_id,
            "version_id": version_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_contact_versions(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_contact_versions_response.ListContactVersionsResponse":
        """<p>Returns a list of versions for a specified contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            max_results: <p>Maximum number of contact versions returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListContactVersions</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_contact_versions_request.ListContactVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_contact_versions_response.ListContactVersionsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_contact_versions

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_contact_versions.async_list_contact_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.list_contact_versions_request.ListContactVersionsRequest = {
            "contact_id": contact_id
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

    async def iter_list_contact_versions(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_groundstation.types.contact_version.ContactVersion]":
        _token = next_token
        while True:
            _response = await self.list_contact_versions(
                contact_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("contact_versions_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_dataflow_endpoint_group(
        self,
        endpoint_details: "capo_groundstation.types.endpoint_details_list.EndpointDetailsList",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
        contact_pre_pass_duration_seconds: Optional[
            "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
    ) -> "capo_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse":
        r"""<p>Creates a <code>DataflowEndpoint</code> group containing the specified list of <code> DataflowEndpoint</code> objects.</p> <p>The <code>name</code> field in each endpoint is used in your mission profile <code> DataflowEndpointConfig</code> to specify which endpoints to use during a contact.</p> <p>When a contact uses multiple <code>DataflowEndpointConfig</code> objects, each <code> Config</code> must match a <code>DataflowEndpoint</code> in the same group.</p>

        Args:
            endpoint_details: <p>Endpoint details of each endpoint in the dataflow endpoint group. All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix <a href=\"https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AwsGroundStationAgentEndpoint.html\"> AWS Ground Station Agent endpoints</a> with <a href=\"https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpoint.html\">Dataflow endpoints</a> in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint groups for each type. </p>
            tags: <p>Tags of a dataflow endpoint group.</p>
            contact_pre_pass_duration_seconds: <p> Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a <code>PREPASS</code> state. A <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html\">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>PREPASS</code> state. </p>
            contact_post_pass_duration_seconds: <p> Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a <code>POSTPASS</code> state. A <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html\">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>POSTPASS</code> state. </p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.create_dataflow_endpoint_group_request.CreateDataflowEndpointGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.create_dataflow_endpoint_group

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.create_dataflow_endpoint_group.async_create_dataflow_endpoint_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.create_dataflow_endpoint_group_request.CreateDataflowEndpointGroupRequest = {
            "endpoint_details": endpoint_details
        }
        if tags is not None:
            input_["tags"] = tags
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_dataflow_endpoint_group(
        self,
        dataflow_endpoint_group_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_dataflow_endpoint_group_response.GetDataflowEndpointGroupResponse":
        """<p>Returns the dataflow endpoint group.</p>

        Args:
            dataflow_endpoint_group_id: <p>UUID of a dataflow endpoint group.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.get_dataflow_endpoint_group_request.GetDataflowEndpointGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.get_dataflow_endpoint_group_response.GetDataflowEndpointGroupResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_dataflow_endpoint_group

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.get_dataflow_endpoint_group.async_get_dataflow_endpoint_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.get_dataflow_endpoint_group_request.GetDataflowEndpointGroupRequest = {
            "dataflow_endpoint_group_id": dataflow_endpoint_group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dataflow_endpoint_group(
        self,
        dataflow_endpoint_group_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse":
        """<p>Deletes a dataflow endpoint group.</p>

        Args:
            dataflow_endpoint_group_id: <p>UUID of a dataflow endpoint group.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.delete_dataflow_endpoint_group_request.DeleteDataflowEndpointGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.delete_dataflow_endpoint_group

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.delete_dataflow_endpoint_group.async_delete_dataflow_endpoint_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.delete_dataflow_endpoint_group_request.DeleteDataflowEndpointGroupRequest = {
            "dataflow_endpoint_group_id": dataflow_endpoint_group_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_dataflow_endpoint_groups(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_dataflow_endpoint_groups_response.ListDataflowEndpointGroupsResponse":
        """<p>Returns a list of <code>DataflowEndpoint</code> groups.</p>

        Args:
            max_results: <p>Maximum number of dataflow endpoint groups returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListDataflowEndpointGroups</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_dataflow_endpoint_groups_request.ListDataflowEndpointGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_dataflow_endpoint_groups_response.ListDataflowEndpointGroupsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_dataflow_endpoint_groups

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_dataflow_endpoint_groups.async_list_dataflow_endpoint_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.list_dataflow_endpoint_groups_request.ListDataflowEndpointGroupsRequest = {}
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

    async def iter_list_dataflow_endpoint_groups(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_groundstation.types.dataflow_endpoint_list_item.DataflowEndpointListItem]":
        _token = next_token
        while True:
            _response = await self.list_dataflow_endpoint_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("dataflow_endpoint_group_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_dataflow_endpoint_group_v2(
        self,
        endpoints: "capo_groundstation.types.create_endpoint_details_list.CreateEndpointDetailsList",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        contact_pre_pass_duration_seconds: Optional[
            "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "capo_groundstation.types.create_dataflow_endpoint_group_v2_response.CreateDataflowEndpointGroupV2Response":
        r"""<p>Creates a <code>DataflowEndpoint</code> group containing the specified list of Ground Station Agent based endpoints.</p> <p>The <code>name</code> field in each endpoint is used in your mission profile <code> DataflowEndpointConfig</code> to specify which endpoints to use during a contact.</p> <p>When a contact uses multiple <code>DataflowEndpointConfig</code> objects, each <code> Config</code> must match a <code>DataflowEndpoint</code> in the same group.</p>

        Args:
            endpoints: <p>Dataflow endpoint group's endpoint definitions</p>
            contact_pre_pass_duration_seconds: <p> Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a <code>PREPASS</code> state. A <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html\">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>PREPASS</code> state. </p>
            contact_post_pass_duration_seconds: <p> Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a <code>POSTPASS</code> state. A <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html\">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>POSTPASS</code> state. </p>
            tags: <p>Tags of a V2 dataflow endpoint group.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.create_dataflow_endpoint_group_v2_request.CreateDataflowEndpointGroupV2Request]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.create_dataflow_endpoint_group_v2_response.CreateDataflowEndpointGroupV2Response"
        ]:
            import capo_groundstation._operations.ground_station.create_dataflow_endpoint_group_v2

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.create_dataflow_endpoint_group_v2.async_create_dataflow_endpoint_group_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.create_dataflow_endpoint_group_v2_request.CreateDataflowEndpointGroupV2Request = {
            "endpoints": endpoints
        }
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_ephemeris(
        self,
        name: "capo_groundstation.types.safe_name.SafeName",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        satellite_id: Optional["capo_groundstation.types.uuid.Uuid"] = None,
        enabled: Optional[bool] = None,
        priority: Optional[
            "capo_groundstation.types.customer_ephemeris_priority.CustomerEphemerisPriority"
        ] = None,
        expiration_time: Optional[datetime.datetime] = None,
        kms_key_arn: Optional["capo_groundstation.types.key_arn.KeyArn"] = None,
        ephemeris: Optional[
            "capo_groundstation.types.ephemeris_data.EphemerisData"
        ] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "capo_groundstation.types.ephemeris_id_response.EphemerisIdResponse":
        """<p>Create an ephemeris with your specified <a>EphemerisData</a>.</p>

        Args:
            satellite_id: <p>The satellite ID that associates this ephemeris with a satellite in AWS Ground Station.</p>
            enabled: <p>Set to <code>true</code> to enable the ephemeris after validation. Set to <code>false</code> to keep it disabled.</p>
            priority: <p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>
            expiration_time: <p>An overall expiration time for the ephemeris in UTC, after which it will become <code>EXPIRED</code>.</p>
            name: <p>A name that you can use to identify the ephemeris.</p>
            kms_key_arn: <p>The ARN of the KMS key to use for encrypting the ephemeris.</p>
            ephemeris: <p>Ephemeris data.</p>
            tags: <p>Tags assigned to an ephemeris.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.create_ephemeris_request.CreateEphemerisRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.ephemeris_id_response.EphemerisIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.create_ephemeris

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.create_ephemeris.async_create_ephemeris(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.create_ephemeris_request.CreateEphemerisRequest = {
            "name": name
        }
        if satellite_id is not None:
            input_["satellite_id"] = satellite_id
        if enabled is not None:
            input_["enabled"] = enabled
        if priority is not None:
            input_["priority"] = priority
        if expiration_time is not None:
            input_["expiration_time"] = expiration_time
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if ephemeris is not None:
            input_["ephemeris"] = ephemeris
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_ephemeris(
        self,
        ephemeris_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> (
        "capo_groundstation.types.describe_ephemeris_response.DescribeEphemerisResponse"
    ):
        """<p>Retrieve information about an existing ephemeris.</p>

        Args:
            ephemeris_id: <p>The AWS Ground Station ephemeris ID.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.describe_ephemeris_request.DescribeEphemerisRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.describe_ephemeris_response.DescribeEphemerisResponse"
        ]:
            import capo_groundstation._operations.ground_station.describe_ephemeris

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.describe_ephemeris.async_describe_ephemeris(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.describe_ephemeris_request.DescribeEphemerisRequest = {
            "ephemeris_id": ephemeris_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ephemeris(
        self,
        ephemeris_id: "capo_groundstation.types.uuid.Uuid",
        enabled: bool,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        name: Optional["capo_groundstation.types.safe_name.SafeName"] = None,
        priority: Optional[
            "capo_groundstation.types.ephemeris_priority.EphemerisPriority"
        ] = None,
    ) -> "capo_groundstation.types.ephemeris_id_response.EphemerisIdResponse":
        """<p>Update an existing ephemeris.</p>

        Args:
            ephemeris_id: <p>The AWS Ground Station ephemeris ID.</p>
            enabled: <p>Enable or disable the ephemeris. Changing this value doesn't require re-validation.</p>
            name: <p>A name that you can use to identify the ephemeris.</p>
            priority: <p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.update_ephemeris_request.UpdateEphemerisRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.ephemeris_id_response.EphemerisIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_ephemeris

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.update_ephemeris.async_update_ephemeris(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.update_ephemeris_request.UpdateEphemerisRequest = {
            "ephemeris_id": ephemeris_id,
            "enabled": enabled,
        }
        if name is not None:
            input_["name"] = name
        if priority is not None:
            input_["priority"] = priority

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ephemeris(
        self,
        ephemeris_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.ephemeris_id_response.EphemerisIdResponse":
        """<p>Delete an ephemeris.</p>

        Args:
            ephemeris_id: <p>The AWS Ground Station ephemeris ID.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in use by non-terminal state contacts and cannot be modified or deleted.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.delete_ephemeris_request.DeleteEphemerisRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.ephemeris_id_response.EphemerisIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.delete_ephemeris

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.delete_ephemeris.async_delete_ephemeris(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.delete_ephemeris_request.DeleteEphemerisRequest = {
            "ephemeris_id": ephemeris_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ephemerides(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        satellite_id: Optional["capo_groundstation.types.uuid.Uuid"] = None,
        ephemeris_type: Optional[
            "capo_groundstation.types.ephemeris_type.EphemerisType"
        ] = None,
        status_list: Optional[
            "capo_groundstation.types.ephemeris_status_list.EphemerisStatusList"
        ] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_ephemerides_response.ListEphemeridesResponse":
        """<p>List your existing ephemerides.</p>

        Args:
            satellite_id: <p>The AWS Ground Station satellite ID to list ephemeris for.</p>
            ephemeris_type: <p>Filter ephemerides by type. If not specified, all ephemeris types will be returned.</p>
            start_time: <p>The start time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.</p>
            end_time: <p>The end time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.</p>
            status_list: <p>The list of ephemeris status to return.</p>
            max_results: <p>Maximum number of ephemerides to return.</p>
            next_token: <p>Pagination token.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_ephemerides_request.ListEphemeridesRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_ephemerides_response.ListEphemeridesResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_ephemerides

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_ephemerides.async_list_ephemerides(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.list_ephemerides_request.ListEphemeridesRequest = {
            "start_time": start_time,
            "end_time": end_time,
        }
        if satellite_id is not None:
            input_["satellite_id"] = satellite_id
        if ephemeris_type is not None:
            input_["ephemeris_type"] = ephemeris_type
        if status_list is not None:
            input_["status_list"] = status_list
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

    async def iter_list_ephemerides(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        satellite_id: Optional["capo_groundstation.types.uuid.Uuid"] = None,
        ephemeris_type: Optional[
            "capo_groundstation.types.ephemeris_type.EphemerisType"
        ] = None,
        status_list: Optional[
            "capo_groundstation.types.ephemeris_status_list.EphemerisStatusList"
        ] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_groundstation.types.ephemeris_item.EphemerisItem]":
        _token = next_token
        while True:
            _response = await self.list_ephemerides(
                start_time,
                end_time,
                config_overrides=config_overrides,
                satellite_id=satellite_id,
                ephemeris_type=ephemeris_type,
                status_list=status_list,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ephemerides",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_ground_stations(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        satellite_id: Optional["capo_groundstation.types.uuid.Uuid"] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_ground_stations_response.ListGroundStationsResponse":
        """<p>Returns a list of ground stations. </p>

        Args:
            satellite_id: <p>Satellite ID to retrieve on-boarded ground stations.</p>
            max_results: <p>Maximum number of ground stations returned.</p>
            next_token: <p>Next token that can be supplied in the next call to get the next page of ground stations.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_ground_stations_request.ListGroundStationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_ground_stations_response.ListGroundStationsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_ground_stations

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_ground_stations.async_list_ground_stations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.list_ground_stations_request.ListGroundStationsRequest = {}
        if satellite_id is not None:
            input_["satellite_id"] = satellite_id
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

    async def iter_list_ground_stations(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        satellite_id: Optional["capo_groundstation.types.uuid.Uuid"] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_groundstation.types.ground_station_data.GroundStationData]"
    ):
        _token = next_token
        while True:
            _response = await self.list_ground_stations(
                config_overrides=config_overrides,
                satellite_id=satellite_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ground_station_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_antennas(
        self,
        ground_station_id: "capo_groundstation.types.ground_station_name.GroundStationName",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_antennas_response.ListAntennasResponse":
        """<p>Returns a list of antennas at a specified ground station.</p>

        Args:
            ground_station_id: <p>ID of a ground station.</p>
            max_results: <p>Maximum number of antennas returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListAntennas</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_antennas_request.ListAntennasRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_antennas_response.ListAntennasResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_antennas

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_antennas.async_list_antennas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.list_antennas_request.ListAntennasRequest = {
            "ground_station_id": ground_station_id
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

    async def iter_list_antennas(
        self,
        ground_station_id: "capo_groundstation.types.ground_station_name.GroundStationName",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_groundstation.types.antenna_list_item.AntennaListItem]":
        _token = next_token
        while True:
            _response = await self.list_antennas(
                ground_station_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("antenna_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_ground_station_reservations(
        self,
        ground_station_id: "capo_groundstation.types.ground_station_name.GroundStationName",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        reservation_types: Optional[
            "capo_groundstation.types.reservation_type_filter_list.ReservationTypeFilterList"
        ] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_ground_station_reservations_response.ListGroundStationReservationsResponse":
        """<p>Returns a list of reservations for a specified ground station.</p>

        Args:
            ground_station_id: <p>ID of a ground station.</p>
            start_time: <p>Start time of the reservation window in UTC.</p>
            end_time: <p>End time of the reservation window in UTC.</p>
            reservation_types: <p>Types of reservations to filter by.</p>
            max_results: <p>Maximum number of ground station reservations returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListGroundStationReservations</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_ground_station_reservations_request.ListGroundStationReservationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_ground_station_reservations_response.ListGroundStationReservationsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_ground_station_reservations

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_ground_station_reservations.async_list_ground_station_reservations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.list_ground_station_reservations_request.ListGroundStationReservationsRequest = {
            "ground_station_id": ground_station_id,
            "start_time": start_time,
            "end_time": end_time,
        }
        if reservation_types is not None:
            input_["reservation_types"] = reservation_types
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

    async def iter_list_ground_station_reservations(
        self,
        ground_station_id: "capo_groundstation.types.ground_station_name.GroundStationName",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        reservation_types: Optional[
            "capo_groundstation.types.reservation_type_filter_list.ReservationTypeFilterList"
        ] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_groundstation.types.ground_station_reservation_list_item.GroundStationReservationListItem]":
        _token = next_token
        while True:
            _response = await self.list_ground_station_reservations(
                ground_station_id,
                start_time,
                end_time,
                config_overrides=config_overrides,
                reservation_types=reservation_types,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("reservation_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_mission_profile(
        self,
        name: "capo_groundstation.types.safe_name.SafeName",
        minimum_viable_contact_duration_seconds: "capo_groundstation.types.positive_duration_in_seconds.PositiveDurationInSeconds",
        dataflow_edges: "capo_groundstation.types.dataflow_edge_list.DataflowEdgeList",
        tracking_config_arn: "capo_groundstation.types.config_arn.ConfigArn",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        contact_pre_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        telemetry_sink_config_arn: Optional[
            "capo_groundstation.types.config_arn.ConfigArn"
        ] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
        streams_kms_key: Optional["capo_groundstation.types.kms_key.KmsKey"] = None,
        streams_kms_role: Optional["capo_groundstation.types.role_arn.RoleArn"] = None,
    ) -> (
        "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
    ):
        """<p>Creates a mission profile.</p> <p> <code>dataflowEdges</code> is a list of lists of strings. Each lower level list of strings has two elements: a <i>from</i> ARN and a <i>to</i> ARN.</p>

        Args:
            name: <p>Name of a mission profile.</p>
            contact_pre_pass_duration_seconds: <p>Amount of time prior to contact start you'd like to receive a Ground Station Contact State Change event indicating an upcoming pass.</p>
            contact_post_pass_duration_seconds: <p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>
            minimum_viable_contact_duration_seconds: <p>Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.</p>
            dataflow_edges: <p>A list of lists of ARNs. Each list of ARNs is an edge, with a <i>from</i> <code> Config</code> and a <i>to</i> <code>Config</code>.</p>
            tracking_config_arn: <p>ARN of a tracking <code>Config</code>.</p>
            telemetry_sink_config_arn: <p>ARN of a telemetry sink <code>Config</code>.</p>
            tags: <p>Tags assigned to a mission profile.</p>
            streams_kms_key: <p>KMS key to use for encrypting streams.</p>
            streams_kms_role: <p>Role to use for encrypting streams with KMS key.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.create_mission_profile_request.CreateMissionProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.create_mission_profile

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.create_mission_profile.async_create_mission_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.create_mission_profile_request.CreateMissionProfileRequest = {
            "name": name,
            "minimum_viable_contact_duration_seconds": minimum_viable_contact_duration_seconds,
            "dataflow_edges": dataflow_edges,
            "tracking_config_arn": tracking_config_arn,
        }
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )
        if telemetry_sink_config_arn is not None:
            input_["telemetry_sink_config_arn"] = telemetry_sink_config_arn
        if tags is not None:
            input_["tags"] = tags
        if streams_kms_key is not None:
            input_["streams_kms_key"] = streams_kms_key
        if streams_kms_role is not None:
            input_["streams_kms_role"] = streams_kms_role

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_mission_profile(
        self,
        mission_profile_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_mission_profile_response.GetMissionProfileResponse":
        """<p>Returns a mission profile.</p>

        Args:
            mission_profile_id: <p>UUID of a mission profile.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.get_mission_profile_request.GetMissionProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.get_mission_profile_response.GetMissionProfileResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_mission_profile

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.get_mission_profile.async_get_mission_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.get_mission_profile_request.GetMissionProfileRequest = {
            "mission_profile_id": mission_profile_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_mission_profile(
        self,
        mission_profile_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        name: Optional["capo_groundstation.types.safe_name.SafeName"] = None,
        contact_pre_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        minimum_viable_contact_duration_seconds: Optional[
            "capo_groundstation.types.positive_duration_in_seconds.PositiveDurationInSeconds"
        ] = None,
        dataflow_edges: Optional[
            "capo_groundstation.types.dataflow_edge_list.DataflowEdgeList"
        ] = None,
        tracking_config_arn: Optional[
            "capo_groundstation.types.config_arn.ConfigArn"
        ] = None,
        telemetry_sink_config_arn: Optional[
            "capo_groundstation.types.config_arn.ConfigArn"
        ] = None,
        streams_kms_key: Optional["capo_groundstation.types.kms_key.KmsKey"] = None,
        streams_kms_role: Optional["capo_groundstation.types.role_arn.RoleArn"] = None,
    ) -> (
        "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
    ):
        """<p>Updates a mission profile.</p> <p>Updating a mission profile will not update the execution parameters for existing future contacts.</p>

        Args:
            mission_profile_id: <p>UUID of a mission profile.</p>
            name: <p>Name of a mission profile.</p>
            contact_pre_pass_duration_seconds: <p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>
            contact_post_pass_duration_seconds: <p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>
            minimum_viable_contact_duration_seconds: <p>Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.</p>
            dataflow_edges: <p>A list of lists of ARNs. Each list of ARNs is an edge, with a <i>from</i> <code> Config</code> and a <i>to</i> <code>Config</code>.</p>
            tracking_config_arn: <p>ARN of a tracking <code>Config</code>.</p>
            telemetry_sink_config_arn: <p>ARN of a telemetry sink <code>Config</code>.</p>
            streams_kms_key: <p>KMS key to use for encrypting streams.</p>
            streams_kms_role: <p>Role to use for encrypting streams with KMS key.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.update_mission_profile_request.UpdateMissionProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_mission_profile

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.update_mission_profile.async_update_mission_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.update_mission_profile_request.UpdateMissionProfileRequest = {
            "mission_profile_id": mission_profile_id
        }
        if name is not None:
            input_["name"] = name
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )
        if minimum_viable_contact_duration_seconds is not None:
            input_["minimum_viable_contact_duration_seconds"] = (
                minimum_viable_contact_duration_seconds
            )
        if dataflow_edges is not None:
            input_["dataflow_edges"] = dataflow_edges
        if tracking_config_arn is not None:
            input_["tracking_config_arn"] = tracking_config_arn
        if telemetry_sink_config_arn is not None:
            input_["telemetry_sink_config_arn"] = telemetry_sink_config_arn
        if streams_kms_key is not None:
            input_["streams_kms_key"] = streams_kms_key
        if streams_kms_role is not None:
            input_["streams_kms_role"] = streams_kms_role

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_mission_profile(
        self,
        mission_profile_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> (
        "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
    ):
        """<p>Deletes a mission profile.</p>

        Args:
            mission_profile_id: <p>UUID of a mission profile.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.delete_mission_profile_request.DeleteMissionProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.delete_mission_profile

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.delete_mission_profile.async_delete_mission_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.delete_mission_profile_request.DeleteMissionProfileRequest = {
            "mission_profile_id": mission_profile_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_mission_profiles(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_mission_profiles_response.ListMissionProfilesResponse":
        """<p>Returns a list of mission profiles.</p>

        Args:
            max_results: <p>Maximum number of mission profiles returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListMissionProfiles</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_mission_profiles_request.ListMissionProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_mission_profiles_response.ListMissionProfilesResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_mission_profiles

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_mission_profiles.async_list_mission_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.list_mission_profiles_request.ListMissionProfilesRequest = {}
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

    async def iter_list_mission_profiles(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_groundstation.types.mission_profile_list_item.MissionProfileListItem]":
        _token = next_token
        while True:
            _response = await self.list_mission_profiles(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("mission_profile_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_satellite(
        self,
        satellite_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_satellite_response.GetSatelliteResponse":
        """<p>Returns a satellite.</p>

        Args:
            satellite_id: <p>UUID of a satellite.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.get_satellite_request.GetSatelliteRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.get_satellite_response.GetSatelliteResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_satellite

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.get_satellite.async_get_satellite(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.get_satellite_request.GetSatelliteRequest = {
            "satellite_id": satellite_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_satellites(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_satellites_response.ListSatellitesResponse":
        """<p>Returns a list of satellites.</p>

        Args:
            max_results: <p>Maximum number of satellites returned.</p>
            next_token: <p>Next token that can be supplied in the next call to get the next page of satellites.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_satellites_request.ListSatellitesRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_satellites_response.ListSatellitesResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_satellites

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_satellites.async_list_satellites(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_groundstation.types.list_satellites_request.ListSatellitesRequest = {}
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

    async def iter_list_satellites(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_groundstation.types.satellite_list_item.SatelliteListItem]"
    ):
        _token = next_token
        while True:
            _response = await self.list_satellites(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("satellites",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
