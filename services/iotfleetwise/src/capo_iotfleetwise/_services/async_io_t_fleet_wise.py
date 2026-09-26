"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#IoTAutobahnControlPlane``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_iotfleetwise._auth._signers
import capo_iotfleetwise._auth._sigv4
from capo_iotfleetwise._auth._identity import Credentials
from capo_iotfleetwise._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iotfleetwise._auth._zapros_handler import AuthMiddleware
from capo_iotfleetwise._pagination import resolve_path as _resolve_path
from capo_iotfleetwise._resources.io_t_autobahn_control_plane.campaign_resource import (
    AsyncCampaignResource,
)
from capo_iotfleetwise._resources.io_t_autobahn_control_plane.decoder_manifest_resource import (
    AsyncDecoderManifestResource,
)
from capo_iotfleetwise._resources.io_t_autobahn_control_plane.fleet_resource import (
    AsyncFleetResource,
)
from capo_iotfleetwise._resources.io_t_autobahn_control_plane.model_manifest_resource import (
    AsyncModelManifestResource,
)
from capo_iotfleetwise._resources.io_t_autobahn_control_plane.signal_catalog_resource import (
    AsyncSignalCatalogResource,
)
from capo_iotfleetwise._resources.io_t_autobahn_control_plane.state_template_resource import (
    AsyncStateTemplateResource,
)
from capo_iotfleetwise._resources.io_t_autobahn_control_plane.vehicle_resource import (
    AsyncVehicleResource,
)
from capo_iotfleetwise._services._aws_config import aaws_config
from capo_iotfleetwise._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_iotfleetwise.types.amazon_resource_name
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.associate_vehicle_fleet_request
    import capo_iotfleetwise.types.associate_vehicle_fleet_response
    import capo_iotfleetwise.types.attribute_names_list
    import capo_iotfleetwise.types.attribute_values_list
    import capo_iotfleetwise.types.attributes_map
    import capo_iotfleetwise.types.batch_create_vehicle_request
    import capo_iotfleetwise.types.batch_create_vehicle_response
    import capo_iotfleetwise.types.batch_update_vehicle_request
    import capo_iotfleetwise.types.batch_update_vehicle_response
    import capo_iotfleetwise.types.campaign_name
    import capo_iotfleetwise.types.campaign_summary
    import capo_iotfleetwise.types.cloud_watch_log_delivery_options
    import capo_iotfleetwise.types.collection_scheme
    import capo_iotfleetwise.types.compression
    import capo_iotfleetwise.types.create_campaign_request
    import capo_iotfleetwise.types.create_campaign_response
    import capo_iotfleetwise.types.create_decoder_manifest_request
    import capo_iotfleetwise.types.create_decoder_manifest_response
    import capo_iotfleetwise.types.create_fleet_request
    import capo_iotfleetwise.types.create_fleet_response
    import capo_iotfleetwise.types.create_model_manifest_request
    import capo_iotfleetwise.types.create_model_manifest_response
    import capo_iotfleetwise.types.create_signal_catalog_request
    import capo_iotfleetwise.types.create_signal_catalog_response
    import capo_iotfleetwise.types.create_state_template_request
    import capo_iotfleetwise.types.create_state_template_response
    import capo_iotfleetwise.types.create_vehicle_request
    import capo_iotfleetwise.types.create_vehicle_request_items
    import capo_iotfleetwise.types.create_vehicle_response
    import capo_iotfleetwise.types.data_destination_configs
    import capo_iotfleetwise.types.data_extra_dimension_node_path_list
    import capo_iotfleetwise.types.data_partitions
    import capo_iotfleetwise.types.decoder_manifest_summary
    import capo_iotfleetwise.types.default_for_unmapped_signals_type
    import capo_iotfleetwise.types.delete_campaign_request
    import capo_iotfleetwise.types.delete_campaign_response
    import capo_iotfleetwise.types.delete_decoder_manifest_request
    import capo_iotfleetwise.types.delete_decoder_manifest_response
    import capo_iotfleetwise.types.delete_fleet_request
    import capo_iotfleetwise.types.delete_fleet_response
    import capo_iotfleetwise.types.delete_model_manifest_request
    import capo_iotfleetwise.types.delete_model_manifest_response
    import capo_iotfleetwise.types.delete_signal_catalog_request
    import capo_iotfleetwise.types.delete_signal_catalog_response
    import capo_iotfleetwise.types.delete_state_template_request
    import capo_iotfleetwise.types.delete_state_template_response
    import capo_iotfleetwise.types.delete_vehicle_request
    import capo_iotfleetwise.types.delete_vehicle_response
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.diagnostics_mode
    import capo_iotfleetwise.types.disassociate_vehicle_fleet_request
    import capo_iotfleetwise.types.disassociate_vehicle_fleet_response
    import capo_iotfleetwise.types.encryption_type
    import capo_iotfleetwise.types.fleet_id
    import capo_iotfleetwise.types.fleet_summary
    import capo_iotfleetwise.types.formatted_vss
    import capo_iotfleetwise.types.fqns
    import capo_iotfleetwise.types.get_campaign_request
    import capo_iotfleetwise.types.get_campaign_response
    import capo_iotfleetwise.types.get_decoder_manifest_request
    import capo_iotfleetwise.types.get_decoder_manifest_response
    import capo_iotfleetwise.types.get_encryption_configuration_request
    import capo_iotfleetwise.types.get_encryption_configuration_response
    import capo_iotfleetwise.types.get_fleet_request
    import capo_iotfleetwise.types.get_fleet_response
    import capo_iotfleetwise.types.get_logging_options_request
    import capo_iotfleetwise.types.get_logging_options_response
    import capo_iotfleetwise.types.get_model_manifest_request
    import capo_iotfleetwise.types.get_model_manifest_response
    import capo_iotfleetwise.types.get_register_account_status_request
    import capo_iotfleetwise.types.get_register_account_status_response
    import capo_iotfleetwise.types.get_signal_catalog_request
    import capo_iotfleetwise.types.get_signal_catalog_response
    import capo_iotfleetwise.types.get_state_template_request
    import capo_iotfleetwise.types.get_state_template_response
    import capo_iotfleetwise.types.get_vehicle_request
    import capo_iotfleetwise.types.get_vehicle_response
    import capo_iotfleetwise.types.get_vehicle_status_request
    import capo_iotfleetwise.types.get_vehicle_status_response
    import capo_iotfleetwise.types.iam_resources
    import capo_iotfleetwise.types.import_decoder_manifest_request
    import capo_iotfleetwise.types.import_decoder_manifest_response
    import capo_iotfleetwise.types.import_signal_catalog_request
    import capo_iotfleetwise.types.import_signal_catalog_response
    import capo_iotfleetwise.types.interface_ids
    import capo_iotfleetwise.types.list_campaigns_request
    import capo_iotfleetwise.types.list_campaigns_response
    import capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_request
    import capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_response
    import capo_iotfleetwise.types.list_decoder_manifest_signals_request
    import capo_iotfleetwise.types.list_decoder_manifest_signals_response
    import capo_iotfleetwise.types.list_decoder_manifests_request
    import capo_iotfleetwise.types.list_decoder_manifests_response
    import capo_iotfleetwise.types.list_fleets_for_vehicle_request
    import capo_iotfleetwise.types.list_fleets_for_vehicle_response
    import capo_iotfleetwise.types.list_fleets_request
    import capo_iotfleetwise.types.list_fleets_response
    import capo_iotfleetwise.types.list_model_manifest_nodes_request
    import capo_iotfleetwise.types.list_model_manifest_nodes_response
    import capo_iotfleetwise.types.list_model_manifests_request
    import capo_iotfleetwise.types.list_model_manifests_response
    import capo_iotfleetwise.types.list_of_strings
    import capo_iotfleetwise.types.list_response_scope
    import capo_iotfleetwise.types.list_signal_catalog_nodes_request
    import capo_iotfleetwise.types.list_signal_catalog_nodes_response
    import capo_iotfleetwise.types.list_signal_catalogs_request
    import capo_iotfleetwise.types.list_signal_catalogs_response
    import capo_iotfleetwise.types.list_state_templates_request
    import capo_iotfleetwise.types.list_state_templates_response
    import capo_iotfleetwise.types.list_tags_for_resource_request
    import capo_iotfleetwise.types.list_tags_for_resource_response
    import capo_iotfleetwise.types.list_vehicles_in_fleet_request
    import capo_iotfleetwise.types.list_vehicles_in_fleet_response
    import capo_iotfleetwise.types.list_vehicles_max_results
    import capo_iotfleetwise.types.list_vehicles_request
    import capo_iotfleetwise.types.list_vehicles_response
    import capo_iotfleetwise.types.manifest_status
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.model_manifest_summary
    import capo_iotfleetwise.types.network_file_definitions
    import capo_iotfleetwise.types.network_interface
    import capo_iotfleetwise.types.network_interfaces
    import capo_iotfleetwise.types.next_token
    import capo_iotfleetwise.types.node
    import capo_iotfleetwise.types.node_paths
    import capo_iotfleetwise.types.nodes
    import capo_iotfleetwise.types.priority
    import capo_iotfleetwise.types.put_encryption_configuration_request
    import capo_iotfleetwise.types.put_encryption_configuration_response
    import capo_iotfleetwise.types.put_logging_options_request
    import capo_iotfleetwise.types.put_logging_options_response
    import capo_iotfleetwise.types.register_account_request
    import capo_iotfleetwise.types.register_account_response
    import capo_iotfleetwise.types.resource_identifier
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.signal_catalog_summary
    import capo_iotfleetwise.types.signal_decoder
    import capo_iotfleetwise.types.signal_decoders
    import capo_iotfleetwise.types.signal_fetch_information_list
    import capo_iotfleetwise.types.signal_information_list
    import capo_iotfleetwise.types.signal_node_type
    import capo_iotfleetwise.types.spooling_mode
    import capo_iotfleetwise.types.state_template_association_identifiers
    import capo_iotfleetwise.types.state_template_associations
    import capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list
    import capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list
    import capo_iotfleetwise.types.state_template_properties
    import capo_iotfleetwise.types.state_template_summary
    import capo_iotfleetwise.types.status_str
    import capo_iotfleetwise.types.tag_key_list
    import capo_iotfleetwise.types.tag_list
    import capo_iotfleetwise.types.tag_resource_request
    import capo_iotfleetwise.types.tag_resource_response
    import capo_iotfleetwise.types.timestamp
    import capo_iotfleetwise.types.timestream_resources
    import capo_iotfleetwise.types.uint32
    import capo_iotfleetwise.types.untag_resource_request
    import capo_iotfleetwise.types.untag_resource_response
    import capo_iotfleetwise.types.update_campaign_action
    import capo_iotfleetwise.types.update_campaign_request
    import capo_iotfleetwise.types.update_campaign_response
    import capo_iotfleetwise.types.update_decoder_manifest_request
    import capo_iotfleetwise.types.update_decoder_manifest_response
    import capo_iotfleetwise.types.update_fleet_request
    import capo_iotfleetwise.types.update_fleet_response
    import capo_iotfleetwise.types.update_mode
    import capo_iotfleetwise.types.update_model_manifest_request
    import capo_iotfleetwise.types.update_model_manifest_response
    import capo_iotfleetwise.types.update_signal_catalog_request
    import capo_iotfleetwise.types.update_signal_catalog_response
    import capo_iotfleetwise.types.update_state_template_request
    import capo_iotfleetwise.types.update_state_template_response
    import capo_iotfleetwise.types.update_vehicle_request
    import capo_iotfleetwise.types.update_vehicle_request_items
    import capo_iotfleetwise.types.update_vehicle_response
    import capo_iotfleetwise.types.vehicle_association_behavior
    import capo_iotfleetwise.types.vehicle_name
    import capo_iotfleetwise.types.vehicle_status
    import capo_iotfleetwise.types.vehicle_summary


class AsyncIoTFleetWiseClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncIoTFleetWiseClient:
    """A client for the ``IoTFleetWise`` service.

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
        self._config = AsyncIoTFleetWiseClientConfig(
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
        self.campaign_resource = AsyncCampaignResource(self)
        self.decoder_manifest_resource = AsyncDecoderManifestResource(self)
        self.fleet_resource = AsyncFleetResource(self)
        self.model_manifest_resource = AsyncModelManifestResource(self)
        self.signal_catalog_resource = AsyncSignalCatalogResource(self)
        self.state_template_resource = AsyncStateTemplateResource(self)
        self.vehicle_resource = AsyncVehicleResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIoTFleetWiseClientConfig = config_overrides or {}
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

    async def batch_create_vehicle(
        self,
        vehicles: "capo_iotfleetwise.types.create_vehicle_request_items.createVehicleRequestItems",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.batch_create_vehicle_response.BatchCreateVehicleResponse":
        r"""<p> Creates a group, or batch, of vehicles. </p> <note> <p> You must specify a decoder manifest and a vehicle model (model manifest) for each vehicle. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-vehicles-cli.html\">Create multiple vehicles (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>. </p>

        Args:
            vehicles: <p> A list of information about each vehicle to create. For more information, see the API data type.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.batch_create_vehicle_request.BatchCreateVehicleRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.batch_create_vehicle_response.BatchCreateVehicleResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.batch_create_vehicle

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.batch_create_vehicle.async_batch_create_vehicle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.batch_create_vehicle_request.BatchCreateVehicleRequest = {
            "vehicles": vehicles
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_vehicle(
        self,
        vehicles: "capo_iotfleetwise.types.update_vehicle_request_items.updateVehicleRequestItems",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.batch_update_vehicle_response.BatchUpdateVehicleResponse":
        r"""<p> Updates a group, or batch, of vehicles.</p> <note> <p> You must specify a decoder manifest and a vehicle model (model manifest) for each vehicle. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-vehicles-cli.html\">Update multiple vehicles (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>. </p>

        Args:
            vehicles: <p> A list of information about the vehicles to update. For more information, see the API data type.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.batch_update_vehicle_request.BatchUpdateVehicleRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.batch_update_vehicle_response.BatchUpdateVehicleResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.batch_update_vehicle

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.batch_update_vehicle.async_batch_update_vehicle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.batch_update_vehicle_request.BatchUpdateVehicleRequest = {
            "vehicles": vehicles
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_encryption_configuration(
        self, *, config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None
    ) -> "capo_iotfleetwise.types.get_encryption_configuration_response.GetEncryptionConfigurationResponse":
        """<p>Retrieves the encryption configuration for resources and data in Amazon Web Services IoT FleetWise.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_encryption_configuration_request.GetEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_encryption_configuration_response.GetEncryptionConfigurationResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_encryption_configuration

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_encryption_configuration.async_get_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_encryption_configuration_request.GetEncryptionConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_logging_options(
        self, *, config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None
    ) -> (
        "capo_iotfleetwise.types.get_logging_options_response.GetLoggingOptionsResponse"
    ):
        """<p>Retrieves the logging options.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_logging_options_request.GetLoggingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_logging_options_response.GetLoggingOptionsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_logging_options

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_logging_options.async_get_logging_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_logging_options_request.GetLoggingOptionsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_register_account_status(
        self, *, config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None
    ) -> "capo_iotfleetwise.types.get_register_account_status_response.GetRegisterAccountStatusResponse":
        r"""<p> Retrieves information about the status of registering your Amazon Web Services account, IAM, and Amazon Timestream resources so that Amazon Web Services IoT FleetWise can transfer your vehicle data to the Amazon Web Services Cloud. </p> <p>For more information, including step-by-step procedures, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/setting-up.html\">Setting up Amazon Web Services IoT FleetWise</a>. </p> <note> <p>This API operation doesn't require input parameters.</p> </note>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_register_account_status_request.GetRegisterAccountStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_register_account_status_response.GetRegisterAccountStatusResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_register_account_status

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_register_account_status.async_get_register_account_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_register_account_status_request.GetRegisterAccountStatusRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_vehicle_status(
        self,
        vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.get_vehicle_status_response.GetVehicleStatusResponse":
        """<p> Retrieves information about the status of campaigns, decoder manifests, or state templates associated with a vehicle.</p>

        Args:
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. This parameter is only supported for resources of type <code>CAMPAIGN</code>.</p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive. This parameter is only supported for resources of type <code>CAMPAIGN</code>.</p>
            vehicle_name: <p> The ID of the vehicle to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_vehicle_status_request.GetVehicleStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_vehicle_status_response.GetVehicleStatusResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_vehicle_status

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_vehicle_status.async_get_vehicle_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_vehicle_status_request.GetVehicleStatusRequest = {
            "vehicle_name": vehicle_name
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

    async def iter_get_vehicle_status(
        self,
        vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.vehicle_status.VehicleStatus]":
        _token = next_token
        while True:
            _response = await self.get_vehicle_status(
                vehicle_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("campaigns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_iotfleetwise.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags (metadata) you have assigned to the resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_encryption_configuration(
        self,
        encryption_type: "capo_iotfleetwise.types.encryption_type.EncryptionType",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        kms_key_id: Optional[str] = None,
    ) -> "capo_iotfleetwise.types.put_encryption_configuration_response.PutEncryptionConfigurationResponse":
        r"""<p>Creates or updates the encryption configuration. Amazon Web Services IoT FleetWise can encrypt your data and resources using an Amazon Web Services managed key. Or, you can use a KMS key that you own and manage. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/data-encryption.html\">Data encryption</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            kms_key_id: <p>The ID of the KMS key that is used for encryption.</p>
            encryption_type: <p>The type of encryption. Choose <code>KMS_BASED_ENCRYPTION</code> to use a KMS key or <code>FLEETWISE_DEFAULT_ENCRYPTION</code> to use an Amazon Web Services managed key.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.put_encryption_configuration_request.PutEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.put_encryption_configuration_response.PutEncryptionConfigurationResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.put_encryption_configuration

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.put_encryption_configuration.async_put_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.put_encryption_configuration_request.PutEncryptionConfigurationRequest = {
            "encryption_type": encryption_type
        }
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_logging_options(
        self,
        cloud_watch_log_delivery: "capo_iotfleetwise.types.cloud_watch_log_delivery_options.CloudWatchLogDeliveryOptions",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> (
        "capo_iotfleetwise.types.put_logging_options_response.PutLoggingOptionsResponse"
    ):
        """<p>Creates or updates the logging option.</p>

        Args:
            cloud_watch_log_delivery: <p>Creates or updates the log delivery option to Amazon CloudWatch Logs.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.put_logging_options_request.PutLoggingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.put_logging_options_response.PutLoggingOptionsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.put_logging_options

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.put_logging_options.async_put_logging_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.put_logging_options_request.PutLoggingOptionsRequest = {
            "cloud_watch_log_delivery": cloud_watch_log_delivery
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_account(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        timestream_resources: Optional[
            "capo_iotfleetwise.types.timestream_resources.TimestreamResources"
        ] = None,
        iam_resources: Optional[
            "capo_iotfleetwise.types.iam_resources.IamResources"
        ] = None,
    ) -> "capo_iotfleetwise.types.register_account_response.RegisterAccountResponse":
        r"""<important> <p>This API operation contains deprecated parameters. Register your account again without the Timestream resources parameter so that Amazon Web Services IoT FleetWise can remove the Timestream metadata stored. You should then pass the data destination into the <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateCampaign.html\">CreateCampaign</a> API operation.</p> <p>You must delete any existing campaigns that include an empty data destination before you register your account again. For more information, see the <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteCampaign.html\">DeleteCampaign</a> API operation.</p> <p>If you want to delete the Timestream inline policy from the service-linked role, such as to mitigate an overly permissive policy, you must first delete any existing campaigns. Then delete the service-linked role and register your account again to enable CloudWatch metrics. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServiceLinkedRole.html\">DeleteServiceLinkedRole</a> in the <i>Identity and Access Management API Reference</i>.</p> </important> <p>Registers your Amazon Web Services account, IAM, and Amazon Timestream resources so Amazon Web Services IoT FleetWise can transfer your vehicle data to the Amazon Web Services Cloud. For more information, including step-by-step procedures, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/setting-up.html\">Setting up Amazon Web Services IoT FleetWise</a>. </p> <note> <p>An Amazon Web Services account is <b>not</b> the same thing as a \"user.\" An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_identity-management.html#intro-identity-users\">Amazon Web Services user</a> is an identity that you create using Identity and Access Management (IAM) and takes the form of either an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html\">IAM user</a> or an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html\">IAM role, both with credentials</a>. A single Amazon Web Services account can, and typically does, contain many users and roles.</p> </note>

        Args:
            iam_resources: <p>The IAM resource that allows Amazon Web Services IoT FleetWise to send data to Amazon Timestream.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.register_account_request.RegisterAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.register_account_response.RegisterAccountResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.register_account

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.register_account.async_register_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.register_account_request.RegisterAccountRequest = {}
        if timestream_resources is not None:
            input_["timestream_resources"] = timestream_resources
        if iam_resources is not None:
            input_["iam_resources"] = iam_resources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_iotfleetwise.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_iotfleetwise.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.tag_resource_response.TagResourceResponse":
        """<p>Adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>The new or modified tags for the resource.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.tag_resource

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_iotfleetwise.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_iotfleetwise.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the given tags (metadata) from the resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>A list of the keys of the tags to be removed from the resource.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.untag_resource

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_campaign(
        self,
        name: "capo_iotfleetwise.types.campaign_name.campaignName",
        signal_catalog_arn: "capo_iotfleetwise.types.arn.arn",
        target_arn: "capo_iotfleetwise.types.arn.arn",
        collection_scheme: "capo_iotfleetwise.types.collection_scheme.CollectionScheme",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        start_time: Optional["capo_iotfleetwise.types.timestamp.timestamp"] = None,
        expiry_time: Optional["capo_iotfleetwise.types.timestamp.timestamp"] = None,
        post_trigger_collection_duration: Optional[
            "capo_iotfleetwise.types.uint32.uint32"
        ] = None,
        diagnostics_mode: Optional[
            "capo_iotfleetwise.types.diagnostics_mode.DiagnosticsMode"
        ] = None,
        spooling_mode: Optional[
            "capo_iotfleetwise.types.spooling_mode.SpoolingMode"
        ] = None,
        compression: Optional["capo_iotfleetwise.types.compression.Compression"] = None,
        priority: Optional["capo_iotfleetwise.types.priority.priority"] = None,
        signals_to_collect: Optional[
            "capo_iotfleetwise.types.signal_information_list.SignalInformationList"
        ] = None,
        data_extra_dimensions: Optional[
            "capo_iotfleetwise.types.data_extra_dimension_node_path_list.DataExtraDimensionNodePathList"
        ] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
        data_destination_configs: Optional[
            "capo_iotfleetwise.types.data_destination_configs.DataDestinationConfigs"
        ] = None,
        data_partitions: Optional[
            "capo_iotfleetwise.types.data_partitions.DataPartitions"
        ] = None,
        signals_to_fetch: Optional[
            "capo_iotfleetwise.types.signal_fetch_information_list.SignalFetchInformationList"
        ] = None,
    ) -> "capo_iotfleetwise.types.create_campaign_response.CreateCampaignResponse":
        r"""<p>Creates an orchestration of data collection rules. The Amazon Web Services IoT FleetWise Edge Agent software running in vehicles uses campaigns to decide how to collect and transfer data to the cloud. You create campaigns in the cloud. After you or your team approve campaigns, Amazon Web Services IoT FleetWise automatically deploys them to vehicles. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/campaigns.html\">Collect and transfer data with campaigns</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            name: <p> The name of the campaign to create. </p>
            description: <p>An optional description of the campaign to help identify its purpose.</p>
            signal_catalog_arn: <p>The Amazon Resource Name (ARN) of the signal catalog to associate with the campaign. </p>
            target_arn: <p> The ARN of the vehicle or fleet to deploy a campaign to. </p>
            start_time: <p>The time, in milliseconds, to deliver a campaign after it was approved. If it's not specified, <code>0</code> is used.</p> <p>Default: <code>0</code> </p>
            expiry_time: <p>The time the campaign expires, in seconds since epoch (January 1, 1970 at midnight UTC time). Vehicle data isn't collected after the campaign expires. </p> <p>Default: 253402214400 (December 31, 9999, 00:00:00 UTC)</p>
            post_trigger_collection_duration: <p>How long (in milliseconds) to collect raw data after a triggering event initiates the collection. If it's not specified, <code>0</code> is used.</p> <p>Default: <code>0</code> </p>
            diagnostics_mode: <p>Option for a vehicle to send diagnostic trouble codes to Amazon Web Services IoT FleetWise. If you want to send diagnostic trouble codes, use <code>SEND_ACTIVE_DTCS</code>. If it's not specified, <code>OFF</code> is used.</p> <p>Default: <code>OFF</code> </p>
            spooling_mode: <p>Determines whether to store collected data after a vehicle lost a connection with the cloud. After a connection is re-established, the data is automatically forwarded to Amazon Web Services IoT FleetWise. If you want to store collected data when a vehicle loses connection with the cloud, use <code>TO_DISK</code>. If it's not specified, <code>OFF</code> is used.</p> <p>Default: <code>OFF</code> </p>
            compression: <p>Determines whether to compress signals before transmitting data to Amazon Web Services IoT FleetWise. If you don't want to compress the signals, use <code>OFF</code>. If it's not specified, <code>SNAPPY</code> is used. </p> <p>Default: <code>SNAPPY</code> </p>
            priority: <p>A number indicating the priority of one campaign over another campaign for a certain vehicle or fleet. A campaign with the lowest value is deployed to vehicles before any other campaigns. If it's not specified, <code>0</code> is used. </p> <p>Default: <code>0</code> </p>
            signals_to_collect: <p>A list of information about signals to collect. </p> <note> <p>If you upload a signal as a condition in a data partition for a campaign, then those same signals must be included in <code>signalsToCollect</code>.</p> </note>
            collection_scheme: <p> The data collection scheme associated with the campaign. You can specify a scheme that collects data based on time or an event.</p>
            data_extra_dimensions: <p>A list of vehicle attributes to associate with a campaign. </p> <p>Enrich the data with specified vehicle attributes. For example, add <code>make</code> and <code>model</code> to the campaign, and Amazon Web Services IoT FleetWise will associate the data with those attributes as dimensions in Amazon Timestream. You can then query the data against <code>make</code> and <code>model</code>.</p> <p>Default: An empty array</p>
            tags: <p>Metadata that can be used to manage the campaign.</p>
            data_destination_configs: <p>The destination where the campaign sends data. You can send data to an MQTT topic, or store it in Amazon S3 or Amazon Timestream.</p> <p>MQTT is the publish/subscribe messaging protocol used by Amazon Web Services IoT to communicate with your devices.</p> <p>Amazon S3 optimizes the cost of data storage and provides additional mechanisms to use vehicle data, such as data lakes, centralized data storage, data processing pipelines, and analytics. Amazon Web Services IoT FleetWise supports at-least-once file delivery to S3. Your vehicle data is stored on multiple Amazon Web Services IoT FleetWise servers for redundancy and high availability.</p> <p>You can use Amazon Timestream to access and analyze time series data, and Timestream to query vehicle data so that you can identify trends and patterns.</p>
            data_partitions: <p>The data partitions associated with the signals collected from the vehicle.</p>
            signals_to_fetch: <p>A list of information about signals to fetch.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_campaign_request.CreateCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_campaign_response.CreateCampaignResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_campaign

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_campaign.async_create_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_campaign_request.CreateCampaignRequest = {
            "name": name,
            "signal_catalog_arn": signal_catalog_arn,
            "target_arn": target_arn,
            "collection_scheme": collection_scheme,
        }
        if description is not None:
            input_["description"] = description
        if start_time is not None:
            input_["start_time"] = start_time
        if expiry_time is not None:
            input_["expiry_time"] = expiry_time
        if post_trigger_collection_duration is not None:
            input_["post_trigger_collection_duration"] = (
                post_trigger_collection_duration
            )
        if diagnostics_mode is not None:
            input_["diagnostics_mode"] = diagnostics_mode
        if spooling_mode is not None:
            input_["spooling_mode"] = spooling_mode
        if compression is not None:
            input_["compression"] = compression
        if priority is not None:
            input_["priority"] = priority
        if signals_to_collect is not None:
            input_["signals_to_collect"] = signals_to_collect
        if data_extra_dimensions is not None:
            input_["data_extra_dimensions"] = data_extra_dimensions
        if tags is not None:
            input_["tags"] = tags
        if data_destination_configs is not None:
            input_["data_destination_configs"] = data_destination_configs
        if data_partitions is not None:
            input_["data_partitions"] = data_partitions
        if signals_to_fetch is not None:
            input_["signals_to_fetch"] = signals_to_fetch

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_campaign(
        self,
        name: "capo_iotfleetwise.types.campaign_name.campaignName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_campaign_response.GetCampaignResponse":
        r"""<p> Retrieves information about a campaign. </p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            name: <p> The name of the campaign to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_campaign_request.GetCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_campaign_response.GetCampaignResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_campaign

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_campaign.async_get_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_campaign_request.GetCampaignRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_campaign(
        self,
        name: "capo_iotfleetwise.types.campaign_name.campaignName",
        action: "capo_iotfleetwise.types.update_campaign_action.UpdateCampaignAction",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        data_extra_dimensions: Optional[
            "capo_iotfleetwise.types.data_extra_dimension_node_path_list.DataExtraDimensionNodePathList"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_campaign_response.UpdateCampaignResponse":
        """<p> Updates a campaign. </p>

        Args:
            name: <p> The name of the campaign to update. </p>
            description: <p>The description of the campaign.</p>
            data_extra_dimensions: <p> A list of vehicle attributes to associate with a signal. </p> <p>Default: An empty array</p>
            action: <p> Specifies how to update a campaign. The action can be one of the following:</p> <ul> <li> <p> <code>APPROVE</code> - To approve delivering a data collection scheme to vehicles. </p> </li> <li> <p> <code>SUSPEND</code> - To suspend collecting signal data. The campaign is deleted from vehicles and all vehicles in the suspended campaign will stop sending data.</p> </li> <li> <p> <code>RESUME</code> - To reactivate the <code>SUSPEND</code> campaign. The campaign is redeployed to all vehicles and the vehicles will resume sending data.</p> </li> <li> <p> <code>UPDATE</code> - To update a campaign. </p> </li> </ul>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_campaign_request.UpdateCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_campaign_response.UpdateCampaignResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_campaign

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_campaign.async_update_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_campaign_request.UpdateCampaignRequest = {
            "name": name,
            "action": action,
        }
        if description is not None:
            input_["description"] = description
        if data_extra_dimensions is not None:
            input_["data_extra_dimensions"] = data_extra_dimensions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_campaign(
        self,
        name: "capo_iotfleetwise.types.campaign_name.campaignName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_campaign_response.DeleteCampaignResponse":
        """<p> Deletes a data collection campaign. Deleting a campaign suspends all data collection and removes it from any vehicles. </p>

        Args:
            name: <p> The name of the campaign to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_campaign_request.DeleteCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_campaign_response.DeleteCampaignResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_campaign

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_campaign.async_delete_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_campaign_request.DeleteCampaignRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_campaigns(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        status: Optional["capo_iotfleetwise.types.status_str.statusStr"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_campaigns_response.ListCampaignsResponse":
        """<p> Lists information about created campaigns. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            status: <p>An optional parameter to filter the results by the status of each created campaign in your account. The status can be one of: <code>CREATING</code>, <code>WAITING_FOR_APPROVAL</code>, <code>RUNNING</code>, or <code>SUSPENDED</code>.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: campaign name, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_campaigns_request.ListCampaignsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_campaigns_response.ListCampaignsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_campaigns

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_campaigns.async_list_campaigns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_campaigns_request.ListCampaignsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_campaigns(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        status: Optional["capo_iotfleetwise.types.status_str.statusStr"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.campaign_summary.CampaignSummary]":
        _token = next_token
        while True:
            _response = await self.list_campaigns(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                status=status,
                list_response_scope=list_response_scope,
            )
            _page = _resolve_path(_response, ("campaign_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_decoder_manifest(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        model_manifest_arn: "capo_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        signal_decoders: Optional[
            "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
        ] = None,
        network_interfaces: Optional[
            "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
        ] = None,
        default_for_unmapped_signals: Optional[
            "capo_iotfleetwise.types.default_for_unmapped_signals_type.DefaultForUnmappedSignalsType"
        ] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_decoder_manifest_response.CreateDecoderManifestResponse":
        r"""<p>Creates the decoder manifest associated with a model manifest. To create a decoder manifest, the following must be true:</p> <ul> <li> <p>Every signal decoder has a unique name.</p> </li> <li> <p>Each signal decoder is associated with a network interface.</p> </li> <li> <p>Each network interface has a unique ID.</p> </li> <li> <p>The signal decoders are specified in the model manifest.</p> </li> </ul>

        Args:
            name: <p> The unique name of the decoder manifest to create.</p>
            description: <p>A brief description of the decoder manifest. </p>
            model_manifest_arn: <p> The Amazon Resource Name (ARN) of the vehicle model (model manifest). </p>
            signal_decoders: <p> A list of information about signal decoders. </p>
            network_interfaces: <p> A list of information about available network interfaces. </p>
            default_for_unmapped_signals: <p>Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>
            tags: <p>Metadata that can be used to manage the decoder manifest.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.decoder_manifest_validation_exception.DecoderManifestValidationException: <p>The request couldn't be completed because it contains signal decoders with one or more validation errors.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_decoder_manifest_request.CreateDecoderManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_decoder_manifest_response.CreateDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_decoder_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_decoder_manifest.async_create_decoder_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_decoder_manifest_request.CreateDecoderManifestRequest = {
            "name": name,
            "model_manifest_arn": model_manifest_arn,
        }
        if description is not None:
            input_["description"] = description
        if signal_decoders is not None:
            input_["signal_decoders"] = signal_decoders
        if network_interfaces is not None:
            input_["network_interfaces"] = network_interfaces
        if default_for_unmapped_signals is not None:
            input_["default_for_unmapped_signals"] = default_for_unmapped_signals
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_decoder_manifest(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_decoder_manifest_response.GetDecoderManifestResponse":
        """<p> Retrieves information about a created decoder manifest. </p>

        Args:
            name: <p> The name of the decoder manifest to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_decoder_manifest_request.GetDecoderManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_decoder_manifest_response.GetDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_decoder_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_decoder_manifest.async_get_decoder_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_decoder_manifest_request.GetDecoderManifestRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_decoder_manifest(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        signal_decoders_to_add: Optional[
            "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
        ] = None,
        signal_decoders_to_update: Optional[
            "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
        ] = None,
        signal_decoders_to_remove: Optional["capo_iotfleetwise.types.fqns.Fqns"] = None,
        network_interfaces_to_add: Optional[
            "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
        ] = None,
        network_interfaces_to_update: Optional[
            "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
        ] = None,
        network_interfaces_to_remove: Optional[
            "capo_iotfleetwise.types.interface_ids.InterfaceIds"
        ] = None,
        status: Optional[
            "capo_iotfleetwise.types.manifest_status.ManifestStatus"
        ] = None,
        default_for_unmapped_signals: Optional[
            "capo_iotfleetwise.types.default_for_unmapped_signals_type.DefaultForUnmappedSignalsType"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_decoder_manifest_response.UpdateDecoderManifestResponse":
        r"""<p> Updates a decoder manifest.</p> <p>A decoder manifest can only be updated when the status is <code>DRAFT</code>. Only <code>ACTIVE</code> decoder manifests can be associated with vehicles.</p>

        Args:
            name: <p> The name of the decoder manifest to update.</p>
            description: <p> A brief description of the decoder manifest to update. </p>
            signal_decoders_to_add: <p> A list of information about decoding additional signals to add to the decoder manifest. </p>
            signal_decoders_to_update: <p> A list of updated information about decoding signals to update in the decoder manifest. </p>
            signal_decoders_to_remove: <p> A list of signal decoders to remove from the decoder manifest. </p>
            network_interfaces_to_add: <p> A list of information about the network interfaces to add to the decoder manifest. </p>
            network_interfaces_to_update: <p> A list of information about the network interfaces to update in the decoder manifest. </p>
            network_interfaces_to_remove: <p> A list of network interfaces to remove from the decoder manifest.</p>
            status: <p> The state of the decoder manifest. If the status is <code>ACTIVE</code>, the decoder manifest can't be edited. If the status is <code>DRAFT</code>, you can edit the decoder manifest. </p>
            default_for_unmapped_signals: <p>Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.decoder_manifest_validation_exception.DecoderManifestValidationException: <p>The request couldn't be completed because it contains signal decoders with one or more validation errors.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_decoder_manifest_request.UpdateDecoderManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_decoder_manifest_response.UpdateDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_decoder_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_decoder_manifest.async_update_decoder_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_decoder_manifest_request.UpdateDecoderManifestRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if signal_decoders_to_add is not None:
            input_["signal_decoders_to_add"] = signal_decoders_to_add
        if signal_decoders_to_update is not None:
            input_["signal_decoders_to_update"] = signal_decoders_to_update
        if signal_decoders_to_remove is not None:
            input_["signal_decoders_to_remove"] = signal_decoders_to_remove
        if network_interfaces_to_add is not None:
            input_["network_interfaces_to_add"] = network_interfaces_to_add
        if network_interfaces_to_update is not None:
            input_["network_interfaces_to_update"] = network_interfaces_to_update
        if network_interfaces_to_remove is not None:
            input_["network_interfaces_to_remove"] = network_interfaces_to_remove
        if status is not None:
            input_["status"] = status
        if default_for_unmapped_signals is not None:
            input_["default_for_unmapped_signals"] = default_for_unmapped_signals

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_decoder_manifest(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_decoder_manifest_response.DeleteDecoderManifestResponse":
        """<p> Deletes a decoder manifest. You can't delete a decoder manifest if it has vehicles associated with it. </p>

        Args:
            name: <p> The name of the decoder manifest to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_decoder_manifest_request.DeleteDecoderManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_decoder_manifest_response.DeleteDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_decoder_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_decoder_manifest.async_delete_decoder_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_decoder_manifest_request.DeleteDecoderManifestRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_decoder_manifests(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        model_manifest_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_decoder_manifests_response.ListDecoderManifestsResponse":
        """<p> Lists decoder manifests. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            model_manifest_arn: <p> The Amazon Resource Name (ARN) of a vehicle model (model manifest) associated with the decoder manifest. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: decoder manifest name, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_decoder_manifests_request.ListDecoderManifestsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_decoder_manifests_response.ListDecoderManifestsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifests

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifests.async_list_decoder_manifests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_decoder_manifests_request.ListDecoderManifestsRequest = {}
        if model_manifest_arn is not None:
            input_["model_manifest_arn"] = model_manifest_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_decoder_manifests(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        model_manifest_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.decoder_manifest_summary.DecoderManifestSummary]":
        _token = next_token
        while True:
            _response = await self.list_decoder_manifests(
                config_overrides=config_overrides,
                model_manifest_arn=model_manifest_arn,
                next_token=_token,
                max_results=max_results,
                list_response_scope=list_response_scope,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def import_decoder_manifest(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        network_file_definitions: "capo_iotfleetwise.types.network_file_definitions.NetworkFileDefinitions",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.import_decoder_manifest_response.ImportDecoderManifestResponse":
        """<p> Creates a decoder manifest using your existing CAN DBC file from your local device. </p> <p>The CAN signal name must be unique and not repeated across CAN message definitions in a .dbc file. </p>

        Args:
            name: <p> The name of the decoder manifest to import. </p>
            network_file_definitions: <p> The file to load into an Amazon Web Services account. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.decoder_manifest_validation_exception.DecoderManifestValidationException: <p>The request couldn't be completed because it contains signal decoders with one or more validation errors.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.import_decoder_manifest_request.ImportDecoderManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.import_decoder_manifest_response.ImportDecoderManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_decoder_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_decoder_manifest.async_import_decoder_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.import_decoder_manifest_request.ImportDecoderManifestRequest = {
            "name": name,
            "network_file_definitions": network_file_definitions,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_decoder_manifest_network_interfaces(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_response.ListDecoderManifestNetworkInterfacesResponse":
        """<p> Lists the network interfaces specified in a decoder manifest. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the decoder manifest to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_request.ListDecoderManifestNetworkInterfacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_response.ListDecoderManifestNetworkInterfacesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_network_interfaces

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_network_interfaces.async_list_decoder_manifest_network_interfaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_decoder_manifest_network_interfaces_request.ListDecoderManifestNetworkInterfacesRequest = {
            "name": name
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

    async def iter_list_decoder_manifest_network_interfaces(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.network_interface.NetworkInterface]":
        _token = next_token
        while True:
            _response = await self.list_decoder_manifest_network_interfaces(
                name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("network_interfaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_decoder_manifest_signals(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_decoder_manifest_signals_response.ListDecoderManifestSignalsResponse":
        """<p> A list of information about signal decoders specified in a decoder manifest. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the decoder manifest to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_decoder_manifest_signals_request.ListDecoderManifestSignalsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_decoder_manifest_signals_response.ListDecoderManifestSignalsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_signals

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_decoder_manifest_signals.async_list_decoder_manifest_signals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_decoder_manifest_signals_request.ListDecoderManifestSignalsRequest = {
            "name": name
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

    async def iter_list_decoder_manifest_signals(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.signal_decoder.SignalDecoder]":
        _token = next_token
        while True:
            _response = await self.list_decoder_manifest_signals(
                name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("signal_decoders",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_fleet(
        self,
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        signal_catalog_arn: "capo_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_fleet_response.CreateFleetResponse":
        r"""<p> Creates a fleet that represents a group of vehicles. </p> <note> <p>You must create both a signal catalog and vehicles before you can create a fleet. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleets.html\">Fleets</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            fleet_id: <p> The unique ID of the fleet to create. </p>
            description: <p> A brief description of the fleet to create. </p>
            signal_catalog_arn: <p> The Amazon Resource Name (ARN) of a signal catalog. </p>
            tags: <p>Metadata that can be used to manage the fleet.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_fleet_request.CreateFleetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_fleet_response.CreateFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_fleet

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_fleet.async_create_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_fleet_request.CreateFleetRequest = {
            "fleet_id": fleet_id,
            "signal_catalog_arn": signal_catalog_arn,
        }
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

    async def get_fleet(
        self,
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_fleet_response.GetFleetResponse":
        """<p> Retrieves information about a fleet. </p>

        Args:
            fleet_id: <p> The ID of the fleet to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_fleet_request.GetFleetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_fleet_response.GetFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_fleet

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_fleet.async_get_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_fleet_request.GetFleetRequest = {
            "fleet_id": fleet_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_fleet(
        self,
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
    ) -> "capo_iotfleetwise.types.update_fleet_response.UpdateFleetResponse":
        """<p> Updates the description of an existing fleet. </p>

        Args:
            fleet_id: <p> The ID of the fleet to update. </p>
            description: <p> An updated description of the fleet. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_fleet_request.UpdateFleetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_fleet_response.UpdateFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_fleet

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_fleet.async_update_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_fleet_request.UpdateFleetRequest = {
            "fleet_id": fleet_id
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

    async def delete_fleet(
        self,
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_fleet_response.DeleteFleetResponse":
        r"""<p> Deletes a fleet. Before you delete a fleet, all vehicles must be dissociated from the fleet. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-fleet-cli.html\">Delete a fleet (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            fleet_id: <p> The ID of the fleet to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_fleet_request.DeleteFleetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_fleet_response.DeleteFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_fleet

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_fleet.async_delete_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_fleet_request.DeleteFleetRequest = {
            "fleet_id": fleet_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_fleets(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_fleets_response.ListFleetsResponse":
        """<p> Retrieves information for each created fleet in an Amazon Web Services account. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: fleet ID, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_fleets_request.ListFleetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_fleets_response.ListFleetsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets.async_list_fleets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_fleets_request.ListFleetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_fleets(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.fleet_summary.FleetSummary]":
        _token = next_token
        while True:
            _response = await self.list_fleets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                list_response_scope=list_response_scope,
            )
            _page = _resolve_path(_response, ("fleet_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_vehicles_in_fleet(
        self,
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_vehicles_in_fleet_response.ListVehiclesInFleetResponse":
        """<p> Retrieves a list of summaries of all vehicles associated with a fleet. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            fleet_id: <p> The ID of a fleet. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_vehicles_in_fleet_request.ListVehiclesInFleetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_vehicles_in_fleet_response.ListVehiclesInFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_vehicles_in_fleet

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_vehicles_in_fleet.async_list_vehicles_in_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_vehicles_in_fleet_request.ListVehiclesInFleetRequest = {
            "fleet_id": fleet_id
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

    async def iter_list_vehicles_in_fleet(
        self,
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.vehicle_name.vehicleName]":
        _token = next_token
        while True:
            _response = await self.list_vehicles_in_fleet(
                fleet_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("vehicles",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_model_manifest(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        nodes: "capo_iotfleetwise.types.list_of_strings.listOfStrings",
        signal_catalog_arn: "capo_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_model_manifest_response.CreateModelManifestResponse":
        r"""<p> Creates a vehicle model (model manifest) that specifies signals (attributes, branches, sensors, and actuators). </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicle-models.html\">Vehicle models</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            name: <p> The name of the vehicle model to create.</p>
            description: <p> A brief description of the vehicle model. </p>
            nodes: <p> A list of nodes, which are a general abstraction of signals. </p>
            signal_catalog_arn: <p> The Amazon Resource Name (ARN) of a signal catalog. </p>
            tags: <p>Metadata that can be used to manage the vehicle model.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_model_manifest_request.CreateModelManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_model_manifest_response.CreateModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_model_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_model_manifest.async_create_model_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_model_manifest_request.CreateModelManifestRequest = {
            "name": name,
            "nodes": nodes,
            "signal_catalog_arn": signal_catalog_arn,
        }
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

    async def get_model_manifest(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_model_manifest_response.GetModelManifestResponse":
        """<p> Retrieves information about a vehicle model (model manifest). </p>

        Args:
            name: <p> The name of the vehicle model to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_model_manifest_request.GetModelManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_model_manifest_response.GetModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_model_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_model_manifest.async_get_model_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_model_manifest_request.GetModelManifestRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_model_manifest(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        nodes_to_add: Optional["capo_iotfleetwise.types.node_paths.NodePaths"] = None,
        nodes_to_remove: Optional[
            "capo_iotfleetwise.types.node_paths.NodePaths"
        ] = None,
        status: Optional[
            "capo_iotfleetwise.types.manifest_status.ManifestStatus"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_model_manifest_response.UpdateModelManifestResponse":
        """<p> Updates a vehicle model (model manifest). If created vehicles are associated with a vehicle model, it can't be updated.</p>

        Args:
            name: <p> The name of the vehicle model to update. </p>
            description: <p> A brief description of the vehicle model. </p>
            nodes_to_add: <p> A list of <code>fullyQualifiedName</code> of nodes, which are a general abstraction of signals, to add to the vehicle model. </p>
            nodes_to_remove: <p> A list of <code>fullyQualifiedName</code> of nodes, which are a general abstraction of signals, to remove from the vehicle model. </p>
            status: <p> The state of the vehicle model. If the status is <code>ACTIVE</code>, the vehicle model can't be edited. If the status is <code>DRAFT</code>, you can edit the vehicle model. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_model_manifest_request.UpdateModelManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_model_manifest_response.UpdateModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_model_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_model_manifest.async_update_model_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_model_manifest_request.UpdateModelManifestRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if nodes_to_add is not None:
            input_["nodes_to_add"] = nodes_to_add
        if nodes_to_remove is not None:
            input_["nodes_to_remove"] = nodes_to_remove
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_model_manifest(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_model_manifest_response.DeleteModelManifestResponse":
        """<p> Deletes a vehicle model (model manifest).</p>

        Args:
            name: <p> The name of the model manifest to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_model_manifest_request.DeleteModelManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_model_manifest_response.DeleteModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_model_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_model_manifest.async_delete_model_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_model_manifest_request.DeleteModelManifestRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_model_manifests(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        signal_catalog_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_model_manifests_response.ListModelManifestsResponse":
        """<p> Retrieves a list of vehicle models (model manifests). </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            signal_catalog_arn: <p> The ARN of a signal catalog. If you specify a signal catalog, only the vehicle models associated with it are returned.</p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: model manifest name, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_model_manifests_request.ListModelManifestsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_model_manifests_response.ListModelManifestsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifests

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifests.async_list_model_manifests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_model_manifests_request.ListModelManifestsRequest = {}
        if signal_catalog_arn is not None:
            input_["signal_catalog_arn"] = signal_catalog_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_model_manifests(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        signal_catalog_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.model_manifest_summary.ModelManifestSummary]":
        _token = next_token
        while True:
            _response = await self.list_model_manifests(
                config_overrides=config_overrides,
                signal_catalog_arn=signal_catalog_arn,
                next_token=_token,
                max_results=max_results,
                list_response_scope=list_response_scope,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_model_manifest_nodes(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_model_manifest_nodes_response.ListModelManifestNodesResponse":
        """<p> Lists information about nodes specified in a vehicle model (model manifest). </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the vehicle model to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_model_manifest_nodes_request.ListModelManifestNodesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_model_manifest_nodes_response.ListModelManifestNodesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifest_nodes

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifest_nodes.async_list_model_manifest_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_model_manifest_nodes_request.ListModelManifestNodesRequest = {
            "name": name
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

    async def iter_list_model_manifest_nodes(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.node.Node]":
        _token = next_token
        while True:
            _response = await self.list_model_manifest_nodes(
                name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_signal_catalog(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        nodes: Optional["capo_iotfleetwise.types.nodes.Nodes"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_signal_catalog_response.CreateSignalCatalogResponse":
        """<p> Creates a collection of standardized signals that can be reused to create vehicle models.</p>

        Args:
            name: <p> The name of the signal catalog to create. </p>
            description: <p>A brief description of the signal catalog.</p>
            nodes: <p> A list of information about nodes, which are a general abstraction of signals. For more information, see the API data type.</p>
            tags: <p>Metadata that can be used to manage the signal catalog.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_node_exception.InvalidNodeException: <p>The specified node type doesn't match the expected node type for a node. You can specify the node type as branch, sensor, actuator, or attribute.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_signal_catalog_request.CreateSignalCatalogRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_signal_catalog_response.CreateSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_signal_catalog

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_signal_catalog.async_create_signal_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_signal_catalog_request.CreateSignalCatalogRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if nodes is not None:
            input_["nodes"] = nodes
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_signal_catalog(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_signal_catalog_response.GetSignalCatalogResponse":
        """<p> Retrieves information about a signal catalog. </p>

        Args:
            name: <p> The name of the signal catalog to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_signal_catalog_request.GetSignalCatalogRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_signal_catalog_response.GetSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_signal_catalog

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_signal_catalog.async_get_signal_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_signal_catalog_request.GetSignalCatalogRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_signal_catalog(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        nodes_to_add: Optional["capo_iotfleetwise.types.nodes.Nodes"] = None,
        nodes_to_update: Optional["capo_iotfleetwise.types.nodes.Nodes"] = None,
        nodes_to_remove: Optional[
            "capo_iotfleetwise.types.node_paths.NodePaths"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_signal_catalog_response.UpdateSignalCatalogResponse":
        """<p> Updates a signal catalog. </p>

        Args:
            name: <p> The name of the signal catalog to update. </p>
            description: <p> A brief description of the signal catalog to update.</p>
            nodes_to_add: <p> A list of information about nodes to add to the signal catalog. </p>
            nodes_to_update: <p> A list of information about nodes to update in the signal catalog. </p>
            nodes_to_remove: <p> A list of <code>fullyQualifiedName</code> of nodes to remove from the signal catalog. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_node_exception.InvalidNodeException: <p>The specified node type doesn't match the expected node type for a node. You can specify the node type as branch, sensor, actuator, or attribute.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_signal_catalog_request.UpdateSignalCatalogRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_signal_catalog_response.UpdateSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_signal_catalog

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_signal_catalog.async_update_signal_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_signal_catalog_request.UpdateSignalCatalogRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if nodes_to_add is not None:
            input_["nodes_to_add"] = nodes_to_add
        if nodes_to_update is not None:
            input_["nodes_to_update"] = nodes_to_update
        if nodes_to_remove is not None:
            input_["nodes_to_remove"] = nodes_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_signal_catalog(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_signal_catalog_response.DeleteSignalCatalogResponse":
        """<p> Deletes a signal catalog. </p>

        Args:
            name: <p> The name of the signal catalog to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_signal_catalog_request.DeleteSignalCatalogRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_signal_catalog_response.DeleteSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_signal_catalog

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_signal_catalog.async_delete_signal_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_signal_catalog_request.DeleteSignalCatalogRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_signal_catalogs(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_signal_catalogs_response.ListSignalCatalogsResponse":
        """<p> Lists all the created signal catalogs in an Amazon Web Services account. </p> <p>You can use to list information about each signal (node) specified in a signal catalog.</p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_signal_catalogs_request.ListSignalCatalogsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_signal_catalogs_response.ListSignalCatalogsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalogs

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalogs.async_list_signal_catalogs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_signal_catalogs_request.ListSignalCatalogsRequest = {}
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

    async def iter_list_signal_catalogs(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.signal_catalog_summary.SignalCatalogSummary]":
        _token = next_token
        while True:
            _response = await self.list_signal_catalogs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def import_signal_catalog(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        vss: Optional["capo_iotfleetwise.types.formatted_vss.FormattedVss"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.import_signal_catalog_response.ImportSignalCatalogResponse":
        """<p> Creates a signal catalog using your existing VSS formatted content from your local device. </p>

        Args:
            name: <p>The name of the signal catalog to import.</p>
            description: <p> A brief description of the signal catalog. </p>
            vss: <p>The contents of the Vehicle Signal Specification (VSS) configuration. VSS is a precise language used to describe and model signals in vehicle networks.</p>
            tags: <p>Metadata that can be used to manage the signal catalog.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.import_signal_catalog_request.ImportSignalCatalogRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.import_signal_catalog_response.ImportSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_signal_catalog

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_signal_catalog.async_import_signal_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.import_signal_catalog_request.ImportSignalCatalogRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if vss is not None:
            input_["vss"] = vss
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_signal_catalog_nodes(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        signal_node_type: Optional[
            "capo_iotfleetwise.types.signal_node_type.SignalNodeType"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_signal_catalog_nodes_response.ListSignalCatalogNodesResponse":
        """<p> Lists of information about the signals (nodes) specified in a signal catalog. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the signal catalog to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            signal_node_type: <p>The type of node in the signal catalog.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_signal_catalog_nodes_request.ListSignalCatalogNodesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_signal_catalog_nodes_response.ListSignalCatalogNodesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalog_nodes

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalog_nodes.async_list_signal_catalog_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_signal_catalog_nodes_request.ListSignalCatalogNodesRequest = {
            "name": name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if signal_node_type is not None:
            input_["signal_node_type"] = signal_node_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_signal_catalog_nodes(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        signal_node_type: Optional[
            "capo_iotfleetwise.types.signal_node_type.SignalNodeType"
        ] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.node.Node]":
        _token = next_token
        while True:
            _response = await self.list_signal_catalog_nodes(
                name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                signal_node_type=signal_node_type,
            )
            _page = _resolve_path(_response, ("nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_state_template(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        signal_catalog_arn: "capo_iotfleetwise.types.arn.arn",
        state_template_properties: "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        data_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.StateTemplateDataExtraDimensionNodePathList"
        ] = None,
        metadata_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.StateTemplateMetadataExtraDimensionNodePathList"
        ] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_state_template_response.CreateStateTemplateResponse":
        r"""<p>Creates a state template. State templates contain state properties, which are signals that belong to a signal catalog that is synchronized between the Amazon Web Services IoT FleetWise Edge and the Amazon Web Services Cloud.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            name: <p>The name of the state template.</p>
            description: <p>A brief description of the state template.</p>
            signal_catalog_arn: <p>The ARN of the signal catalog associated with the state template.</p>
            state_template_properties: <p>A list of signals from which data is collected. The state template properties contain the fully qualified names of the signals.</p>
            data_extra_dimensions: <p>A list of vehicle attributes to associate with the payload published on the state template's MQTT topic. (See <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data\"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will enrich the protobuf encoded payload with those attributes in the <code>extraDimensions</code> field.</p>
            metadata_extra_dimensions: <p>A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. (See <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data\"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will include these attributes as User Properties with the MQTT message.</p> <p>Default: An empty array</p>
            tags: <p>Metadata that can be used to manage the state template.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_state_template_request.CreateStateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_state_template_response.CreateStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_state_template

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_state_template.async_create_state_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_state_template_request.CreateStateTemplateRequest = {
            "name": name,
            "signal_catalog_arn": signal_catalog_arn,
            "state_template_properties": state_template_properties,
        }
        if description is not None:
            input_["description"] = description
        if data_extra_dimensions is not None:
            input_["data_extra_dimensions"] = data_extra_dimensions
        if metadata_extra_dimensions is not None:
            input_["metadata_extra_dimensions"] = metadata_extra_dimensions
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_state_template(
        self,
        identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_state_template_response.GetStateTemplateResponse":
        r"""<p>Retrieves information about a state template.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            identifier: <p>The unique ID of the state template.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_state_template_request.GetStateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_state_template_response.GetStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_state_template

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_state_template.async_get_state_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_state_template_request.GetStateTemplateRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_state_template(
        self,
        identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        state_template_properties_to_add: Optional[
            "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties"
        ] = None,
        state_template_properties_to_remove: Optional[
            "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties"
        ] = None,
        data_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.StateTemplateDataExtraDimensionNodePathList"
        ] = None,
        metadata_extra_dimensions: Optional[
            "capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.StateTemplateMetadataExtraDimensionNodePathList"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_state_template_response.UpdateStateTemplateResponse":
        r"""<p>Updates a state template.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            identifier: <p>The unique ID of the state template.</p>
            description: <p>A brief description of the state template.</p>
            state_template_properties_to_add: <p>Add signals from which data is collected as part of the state template.</p>
            state_template_properties_to_remove: <p>Remove signals from which data is collected as part of the state template.</p>
            data_extra_dimensions: <p>A list of vehicle attributes to associate with the payload published on the state template's MQTT topic. (See <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data\"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will enrich the protobuf encoded payload with those attributes in the <code>extraDimensions</code> field.</p> <p>Default: An empty array</p>
            metadata_extra_dimensions: <p>A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. (See <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data\"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will include these attributes as User Properties with the MQTT message.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_state_template_request.UpdateStateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_state_template_response.UpdateStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_state_template

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_state_template.async_update_state_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_state_template_request.UpdateStateTemplateRequest = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if state_template_properties_to_add is not None:
            input_["state_template_properties_to_add"] = (
                state_template_properties_to_add
            )
        if state_template_properties_to_remove is not None:
            input_["state_template_properties_to_remove"] = (
                state_template_properties_to_remove
            )
        if data_extra_dimensions is not None:
            input_["data_extra_dimensions"] = data_extra_dimensions
        if metadata_extra_dimensions is not None:
            input_["metadata_extra_dimensions"] = metadata_extra_dimensions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_state_template(
        self,
        identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_state_template_response.DeleteStateTemplateResponse":
        """<p>Deletes a state template.</p>

        Args:
            identifier: <p>The unique ID of the state template.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_state_template_request.DeleteStateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_state_template_response.DeleteStateTemplateResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_state_template

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_state_template.async_delete_state_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_state_template_request.DeleteStateTemplateRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_state_templates(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_state_templates_response.ListStateTemplatesResponse":
        r"""<p>Lists information about created state templates.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            next_token: <p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: state template ID, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_state_templates_request.ListStateTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_state_templates_response.ListStateTemplatesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_state_templates

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_state_templates.async_list_state_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_state_templates_request.ListStateTemplatesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_state_templates(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.state_template_summary.StateTemplateSummary]":
        _token = next_token
        while True:
            _response = await self.list_state_templates(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                list_response_scope=list_response_scope,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_vehicle(
        self,
        vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName",
        model_manifest_arn: "capo_iotfleetwise.types.arn.arn",
        decoder_manifest_arn: "capo_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        attributes: Optional[
            "capo_iotfleetwise.types.attributes_map.attributesMap"
        ] = None,
        association_behavior: Optional[
            "capo_iotfleetwise.types.vehicle_association_behavior.VehicleAssociationBehavior"
        ] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
        state_templates: Optional[
            "capo_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
        ] = None,
    ) -> "capo_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse":
        r"""<p> Creates a vehicle, which is an instance of a vehicle model (model manifest). Vehicles created from the same vehicle model consist of the same signals inherited from the vehicle model.</p> <note> <p> If you have an existing Amazon Web Services IoT thing, you can use Amazon Web Services IoT FleetWise to create a vehicle and collect data from your thing. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-vehicle-cli.html\">Create a vehicle (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            vehicle_name: <p> The unique ID of the vehicle to create. </p>
            model_manifest_arn: <p> The Amazon Resource Name ARN of a vehicle model. </p>
            decoder_manifest_arn: <p> The ARN of a decoder manifest. </p>
            attributes: <p>Static information about a vehicle in a key-value pair. For example: <code>\"engineType\"</code> : <code>\"1.3 L R2\"</code> </p> <p>To use attributes with Campaigns or State Templates, you must include them using the request parameters <code>dataExtraDimensions</code> and/or <code>metadataExtraDimensions</code> (for state templates only) when creating your campaign/state template. </p>
            association_behavior: <p> An option to create a new Amazon Web Services IoT thing when creating a vehicle, or to validate an existing Amazon Web Services IoT thing as a vehicle. </p> <p>Default: <code/> </p>
            tags: <p>Metadata that can be used to manage the vehicle.</p>
            state_templates: <p>Associate state templates with the vehicle. You can monitor the last known state of the vehicle in near real time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_vehicle_request.CreateVehicleRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_vehicle

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_vehicle.async_create_vehicle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_vehicle_request.CreateVehicleRequest = {
            "vehicle_name": vehicle_name,
            "model_manifest_arn": model_manifest_arn,
            "decoder_manifest_arn": decoder_manifest_arn,
        }
        if attributes is not None:
            input_["attributes"] = attributes
        if association_behavior is not None:
            input_["association_behavior"] = association_behavior
        if tags is not None:
            input_["tags"] = tags
        if state_templates is not None:
            input_["state_templates"] = state_templates

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_vehicle(
        self,
        vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_vehicle_response.GetVehicleResponse":
        """<p> Retrieves information about a vehicle. </p>

        Args:
            vehicle_name: <p> The ID of the vehicle to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_vehicle_request.GetVehicleRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_vehicle_response.GetVehicleResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_vehicle

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_vehicle.async_get_vehicle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_vehicle_request.GetVehicleRequest = {
            "vehicle_name": vehicle_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_vehicle(
        self,
        vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        model_manifest_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        decoder_manifest_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        attributes: Optional[
            "capo_iotfleetwise.types.attributes_map.attributesMap"
        ] = None,
        attribute_update_mode: Optional[
            "capo_iotfleetwise.types.update_mode.UpdateMode"
        ] = None,
        state_templates_to_add: Optional[
            "capo_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
        ] = None,
        state_templates_to_remove: Optional[
            "capo_iotfleetwise.types.state_template_association_identifiers.StateTemplateAssociationIdentifiers"
        ] = None,
        state_templates_to_update: Optional[
            "capo_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_vehicle_response.UpdateVehicleResponse":
        r"""<p> Updates a vehicle.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            vehicle_name: <p>The unique ID of the vehicle to update.</p>
            model_manifest_arn: <p>The ARN of a vehicle model (model manifest) associated with the vehicle.</p>
            decoder_manifest_arn: <p>The ARN of the decoder manifest associated with this vehicle.</p>
            attributes: <p>Static information about a vehicle in a key-value pair. For example:</p> <p> <code>\"engineType\"</code> : <code>\"1.3 L R2\"</code> </p>
            attribute_update_mode: <p>The method the specified attributes will update the existing attributes on the vehicle. Use<code>Overwite</code> to replace the vehicle attributes with the specified attributes. Or use <code>Merge</code> to combine all attributes.</p> <p>This is required if attributes are present in the input.</p>
            state_templates_to_add: <p>Associate state templates with the vehicle.</p>
            state_templates_to_remove: <p>Remove state templates from the vehicle.</p>
            state_templates_to_update: <p>Change the <code>stateTemplateUpdateStrategy</code> of state templates already associated with the vehicle.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_vehicle_request.UpdateVehicleRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_vehicle_response.UpdateVehicleResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_vehicle

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_vehicle.async_update_vehicle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_vehicle_request.UpdateVehicleRequest = {
            "vehicle_name": vehicle_name
        }
        if model_manifest_arn is not None:
            input_["model_manifest_arn"] = model_manifest_arn
        if decoder_manifest_arn is not None:
            input_["decoder_manifest_arn"] = decoder_manifest_arn
        if attributes is not None:
            input_["attributes"] = attributes
        if attribute_update_mode is not None:
            input_["attribute_update_mode"] = attribute_update_mode
        if state_templates_to_add is not None:
            input_["state_templates_to_add"] = state_templates_to_add
        if state_templates_to_remove is not None:
            input_["state_templates_to_remove"] = state_templates_to_remove
        if state_templates_to_update is not None:
            input_["state_templates_to_update"] = state_templates_to_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_vehicle(
        self,
        vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_vehicle_response.DeleteVehicleResponse":
        """<p> Deletes a vehicle and removes it from any campaigns.</p>

        Args:
            vehicle_name: <p>The ID of the vehicle to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_vehicle_request.DeleteVehicleRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_vehicle_response.DeleteVehicleResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_vehicle

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_vehicle.async_delete_vehicle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_vehicle_request.DeleteVehicleRequest = {
            "vehicle_name": vehicle_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_vehicles(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        model_manifest_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        attribute_names: Optional[
            "capo_iotfleetwise.types.attribute_names_list.attributeNamesList"
        ] = None,
        attribute_values: Optional[
            "capo_iotfleetwise.types.attribute_values_list.attributeValuesList"
        ] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_iotfleetwise.types.list_vehicles_max_results.listVehiclesMaxResults"
        ] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_vehicles_response.ListVehiclesResponse":
        r"""<p> Retrieves a list of summaries of created vehicles. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            model_manifest_arn: <p> The Amazon Resource Name (ARN) of a vehicle model (model manifest). You can use this optional parameter to list only the vehicles created from a certain vehicle model. </p>
            attribute_names: <p>The fully qualified names of the attributes. You can use this optional parameter to list the vehicles containing all the attributes in the request. For example, <code>attributeNames</code> could be \"<code>Vehicle.Body.Engine.Type, Vehicle.Color</code>\" and the corresponding <code>attributeValues</code> could be \"<code>1.3 L R2, Blue</code>\" . In this case, the API will filter vehicles with an attribute name <code>Vehicle.Body.Engine.Type</code> that contains a value of <code>1.3 L R2</code> AND an attribute name <code>Vehicle.Color</code> that contains a value of \"<code>Blue</code>\". A request must contain unique values for the <code>attributeNames</code> filter and the matching number of <code>attributeValues</code> filters to return the subset of vehicles that match the attributes filter condition.</p>
            attribute_values: <p>Static information about a vehicle attribute value in string format. You can use this optional parameter in conjunction with <code>attributeNames</code> to list the vehicles containing all the <code>attributeValues</code> corresponding to the <code>attributeNames</code> filter. For example, <code>attributeValues</code> could be \"<code>1.3 L R2, Blue</code>\" and the corresponding <code>attributeNames</code> filter could be \"<code>Vehicle.Body.Engine.Type, Vehicle.Color</code>\". In this case, the API will filter vehicles with attribute name <code>Vehicle.Body.Engine.Type</code> that contains a value of <code>1.3 L R2</code> AND an attribute name <code>Vehicle.Color</code> that contains a value of \"<code>Blue</code>\". A request must contain unique values for the <code>attributeNames</code> filter and the matching number of <code>attributeValues</code> filter to return the subset of vehicles that match the attributes filter condition.</p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: vehicle name, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_vehicles_request.ListVehiclesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_vehicles_response.ListVehiclesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_vehicles

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_vehicles.async_list_vehicles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_vehicles_request.ListVehiclesRequest = {}
        if model_manifest_arn is not None:
            input_["model_manifest_arn"] = model_manifest_arn
        if attribute_names is not None:
            input_["attribute_names"] = attribute_names
        if attribute_values is not None:
            input_["attribute_values"] = attribute_values
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_vehicles(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        model_manifest_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        attribute_names: Optional[
            "capo_iotfleetwise.types.attribute_names_list.attributeNamesList"
        ] = None,
        attribute_values: Optional[
            "capo_iotfleetwise.types.attribute_values_list.attributeValuesList"
        ] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional[
            "capo_iotfleetwise.types.list_vehicles_max_results.listVehiclesMaxResults"
        ] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.vehicle_summary.VehicleSummary]":
        _token = next_token
        while True:
            _response = await self.list_vehicles(
                config_overrides=config_overrides,
                model_manifest_arn=model_manifest_arn,
                attribute_names=attribute_names,
                attribute_values=attribute_values,
                next_token=_token,
                max_results=max_results,
                list_response_scope=list_response_scope,
            )
            _page = _resolve_path(_response, ("vehicle_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def associate_vehicle_fleet(
        self,
        vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName",
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.associate_vehicle_fleet_response.AssociateVehicleFleetResponse":
        """<p> Adds, or associates, a vehicle with a fleet. </p>

        Args:
            vehicle_name: <p> The unique ID of the vehicle to associate with the fleet. </p>
            fleet_id: <p> The ID of a fleet. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.associate_vehicle_fleet_request.AssociateVehicleFleetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.associate_vehicle_fleet_response.AssociateVehicleFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.associate_vehicle_fleet

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.associate_vehicle_fleet.async_associate_vehicle_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.associate_vehicle_fleet_request.AssociateVehicleFleetRequest = {
            "vehicle_name": vehicle_name,
            "fleet_id": fleet_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_vehicle_fleet(
        self,
        vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName",
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.disassociate_vehicle_fleet_response.DisassociateVehicleFleetResponse":
        """<p>Removes, or disassociates, a vehicle from a fleet. Disassociating a vehicle from a fleet doesn't delete the vehicle.</p>

        Args:
            vehicle_name: <p> The unique ID of the vehicle to disassociate from the fleet.</p>
            fleet_id: <p> The unique ID of a fleet. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.disassociate_vehicle_fleet_request.DisassociateVehicleFleetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.disassociate_vehicle_fleet_response.DisassociateVehicleFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.disassociate_vehicle_fleet

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.disassociate_vehicle_fleet.async_disassociate_vehicle_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.disassociate_vehicle_fleet_request.DisassociateVehicleFleetRequest = {
            "vehicle_name": vehicle_name,
            "fleet_id": fleet_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_fleets_for_vehicle(
        self,
        vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_fleets_for_vehicle_response.ListFleetsForVehicleResponse":
        """<p>Retrieves a list of IDs for all fleets that the vehicle is associated with.</p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            vehicle_name: <p> The ID of the vehicle to retrieve information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_fleets_for_vehicle_request.ListFleetsForVehicleRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_fleets_for_vehicle_response.ListFleetsForVehicleResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets_for_vehicle

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets_for_vehicle.async_list_fleets_for_vehicle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_fleets_for_vehicle_request.ListFleetsForVehicleRequest = {
            "vehicle_name": vehicle_name
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

    async def iter_list_fleets_for_vehicle(
        self,
        vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "AsyncIterator[capo_iotfleetwise.types.fleet_id.fleetId]":
        _token = next_token
        while True:
            _response = await self.list_fleets_for_vehicle(
                vehicle_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("fleets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
